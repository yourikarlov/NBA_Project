import pandas as pd
import numpy as np


#Important note: 

#This program compares each young player in a given cluster to role players in the same/most similar cluster,
#and other players to have a bigger pool size, using the features specific to that cluster.
#
# For example, the features used for the young players in the "shot creator" cluster are: 
# Feature list:
#- Scoring: %PTS, TS%, PAINT_FREQ, MID_FREQ, AB3_FREQ, FGM_%UAST
#- Fouls/Turnovers: %PFD, %TOV (sign-flipped)
#- Playmaking: %AST

# ---------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------

ROLE_PLAYERS_FILE = 'Spreadsheets/role_players.xlsx'
YOUNG_PLAYERS_FILE = 'Spreadsheets/young_players.xlsx'

ROLE_PLAYERS = [
    "Andre Drummond", "Daniel Gafford", "Isaiah Hartenstein", "Ivica Zubac", "Jusuf Nurkić", "Luke Kornet", "Mitchell Robinson", "Robert Williams III",
    "Aaron Gordon", "Bobby Portis", "Brook Lopez", "John Collins", "Naz Reid", "Nikola Vučević", "P.J. Washington"
]

YOUNG_PLAYERS = [
   "Kel'el Ware", "Kyle Filipowski", "Leonard Miller",
]

# Feature -> (category, weight, flip_sign)
# Defense/rebounding bucket sums to 0.55, scoring bucket sums to 0.45

#Change the stats depending on the cluster of players you're comparing.
#Change the weigths depending on the importance of each stat.

# flipped: fewer fouls = better for example.

FEATURES = {
    '%STL':        ('defending', 0.30/3, False),
    '%BLK':    ('defending', 0.30/3, False),
    '%PF': ('defending', 0.30/3, True),
    '%REB': ('rebounding', 0.30, False),
    '%AST': ('playmaking', 0.05, False),
    'TS%': ('scoring', 0.35/5, False),
    'FG%': ('scoring', 0.35/5, False),
    'RA_FREQ': ('scoring', 0.35/5, False),
    'PAINT_FREQ': ('scoring', 0.35/5, False),
    'AB3_FREQ': ('scoring', 0.35/5, False),
}

FEATURE_COLS = list(FEATURES.keys())


# ---------------------------------------------------------------
# LOAD + FLATTEN
# ---------------------------------------------------------------

def load(path):
    df = pd.read_excel(path, header=[0, 1])
    # flatten multiindex -> just use the second level (stat name),
    # since stat names are unique across categories in this dataset
    df.columns = [c[1] for c in df.columns]
    return df


def career_aggregate(df, players, mode):
    """
    mode='last4'  -> use each player's last 4 seasons (by SEASON desc)
    mode='all'    -> use every season on record
    Aggregation is minutes-weighted (MIN * GP = total minutes played).
    """
    rows = []
    for player in players:
        pdf = df[df['PLAYER'] == player].copy()
        if pdf.empty:
            print(f"WARNING: no rows found for {player}")
            continue
        pdf = pdf.sort_values('SEASON')
        if mode == 'last4':
            pdf = pdf.tail(4)
        # else 'all' -> keep everything

        weights = pdf['MIN'] * pdf['GP']
        if weights.sum() == 0:
            print(f"WARNING: zero total minutes for {player}, skipping")
            continue

        agg = {'PLAYER': player}
        for col in FEATURE_COLS:
            agg[col] = np.average(pdf[col], weights=weights)
        rows.append(agg)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------
# PIPELINE
# ---------------------------------------------------------------

role_df = load(ROLE_PLAYERS_FILE)
young_df = load(YOUNG_PLAYERS_FILE)

role_agg = career_aggregate(role_df, ROLE_PLAYERS, mode='all')
young_agg = career_aggregate(young_df, YOUNG_PLAYERS, mode='all')

role_agg['POOL'] = 'role'
young_agg['POOL'] = 'young'

combined = pd.concat([role_agg, young_agg], ignore_index=True)

# Apply sign flips BEFORE Z-scoring so direction is consistent
for col, (cat, w, flip) in FEATURES.items():
    if flip:
        combined[col] = -combined[col]

# Z-score using ONLY the role player pool as the reference distribution
# (mu, sigma computed from role players; applied to both role + young players).
# This frames the question as "how many SDs is this player from the
# established archetype," rather than standardizing against a combined pool.
role_mask = combined['POOL'] == 'role'

z = combined.copy()
for col in FEATURE_COLS:
    mu = combined.loc[role_mask, col].mean()
    sigma = combined.loc[role_mask, col].std(ddof=0)
    z[col] = (combined[col] - mu) / sigma

# Apply weights to get weighted Z vectors
weighted_z = z.copy()
for col, (cat, w, flip) in FEATURES.items():
    weighted_z[col] = z[col] * w

# ---------------------------------------------------------------
# SIMILARITY: cosine similarity between weighted Z vectors
# ---------------------------------------------------------------

def cosine_sim(v1, v2):
    num = np.dot(v1, v2)
    denom = np.linalg.norm(v1) * np.linalg.norm(v2)
    return num / denom if denom != 0 else 0.0

young_rows = weighted_z[weighted_z['POOL'] == 'young']
role_rows = weighted_z[weighted_z['POOL'] == 'role']

results = []
for _, yrow in young_rows.iterrows():
    yvec = yrow[FEATURE_COLS].values.astype(float)
    for _, rrow in role_rows.iterrows():
        rvec = rrow[FEATURE_COLS].values.astype(float)
        sim = cosine_sim(yvec, rvec)
        dist = np.linalg.norm(yvec - rvec)
        results.append({
            'young_player': yrow['PLAYER'],
            'role_comp': rrow['PLAYER'],
            'cosine_similarity': round(sim, 4),
            'euclidean_distance': round(dist, 4),
        })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values(['young_player', 'cosine_similarity'], ascending=[True, False])

print("\n=== RAW AGGREGATED STATS (career-weighted) ===")
print(combined[['PLAYER', 'POOL'] + FEATURE_COLS].round(3).to_string(index=False))

print("\n=== TOP COMPS PER YOUNG PLAYER (by cosine similarity) ===")
for player in YOUNG_PLAYERS:
    sub = results_df[results_df['young_player'] == player]
    print(f"\n{player}:")
    print(sub[['role_comp', 'cosine_similarity', 'euclidean_distance']].to_string(index=False))

results_df.to_csv('Spreadsheets/versatile_bigs22.csv', index=False)
print("\nSaved full results to versatile_bigs22.csv")
#print(z[z['POOL']=='role'][['PLAYER'] + FEATURE_COLS].round(2))