import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

#Step 1: Load the data
data = pd.read_excel("Spreadsheets/young_players.xlsx", sheet_name="Young Players", header=1)

#Step 2: Dedupe mid-season trades (keep TOT row)
def keep_tot_or_only_row(group):
    if(group["TEAM"] == "TOT").any():
        return group[group["TEAM"] == "TOT"]
    return group

data = (data.groupby(["PLAYER", "SEASON"], group_keys=False)[data.columns]
    .apply(keep_tot_or_only_row)
    .reset_index(drop=True))


#Step 3: One profile row per player (avg of last 4 qualifying seasons)
stat_cols = []

for col in data.columns:
    if col not in ("PLAYER", "SEASON", "TEAM", "POSITION", "AGE"):
       stat_cols.append(col)

profiles = []
for player, group in data.groupby("PLAYER"):
    group = group.sort_values("SEASON")
    qualifying = group[group["GP"] >= 25]
    profile = qualifying[stat_cols].mean(numeric_only=True)
    profile["PLAYER"] = player
    profiles.append(profile)

player_profiles = pd.DataFrame(profiles).reset_index(drop=True)


#Step 4: Features selection
features = [

    # Shooting
    "RA_FREQ",
    "MID_FREQ",
    "LC3_FREQ",
    "RC3_FREQ",
    "AB3_FREQ",

    # Creation
    "%AST",
    "USG%",
    "AST/TO",

    # Rebounding
    "%OREB",
    "%DREB",

    # Defense
    "%STL",
    "%BLK"
]

X = player_profiles[features]

#Step 5: Scale + KMeans

scaler = StandardScaler()
scaled_data = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=6, n_init = 100)
kmeans.fit(scaled_data)

#Step 6: Validation - Silhouette Score
silhouette_avg = silhouette_score(scaled_data, kmeans.labels_)
print(f"Silhouette score: {silhouette_avg}")

#Step 7: Assign clusters to player profiles
player_profiles["Cluster"] = kmeans.labels_

#Step 8: Save cluster stats to CSV

print()
for c in sorted(player_profiles["Cluster"].unique()):
    members = player_profiles[player_profiles["Cluster"] == c]["PLAYER"].tolist()
    print(f"[{c}] ({len(members)}): {', '.join(members)}")

cluster_stats = player_profiles.groupby(["Cluster"])[features].agg(["mean", "median"])
cluster_stats.to_csv("cluster_stats_k6_young_players_1.csv")
print("\nSaved → cluster_stats_k6_young_players_1.csv")