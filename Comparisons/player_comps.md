# Player Comparisons 


## The method

### 1. Define the comparison pools
Two groups: the reference pool (role players in the matching cluster — e.g., the 8 Interior Anchors) and the target pool(young players in the matching cluster — e.g., Bona, Lively, Missi). The reference pool defines what the archetype looks like statistically; the target pool is what gets measured against it.

### 2. Aggregate each player to a single career profile
Each player has multiple season rows. Role players and young players use all seasons on record. Each stat is aggregated as a minutes-weighted average (weight = MIN × GP per season), so a season with heavy playing time counts more than a cameo.

### 3. Choose and sign-correct the features
Pick the stats that define the archetype (for Interior Anchors: 6 rebounding/defense stats + 5 scoring/shot-zone stats). Any stat where "lower is better" (fouls, turnovers) gets multiplied by -1 before standardizing, so that afterward, higher Z always means "better/more of that trait" across every feature, with no exceptions to remember later.

### 4. Standardize using the reference pool only
For each feature, compute μ and σ from the role players only. Apply that same μ/σ to both role and young players:
Z = (x − μ_role) / σ_role
Role players define the yardstick; young players are measured against it without being able to shift it. A role player's Z-distribution centers near 0 by construction; a young player's Z can land anywhere, including outside the role-player range — which is itself informative.

### 5. Weight each standardized feature
Multiply each Z-score by a weight reflecting how central that stat is to the archetype: weighted_Z = w × Z. Weights are organized into thematic buckets (e.g., defense 0.60 total, scoring 0.40 total) so the comp emphasizes what actually defines the role, not just whatever stats happen to be available.

### 6. Keep it as a vector, not a single number
Each player becomes a vector of weighted Z-scores — one per feature — rather than summing into one composite score. This preserves the shape of a player's skillset (where their strengths/weaknesses sit) instead of collapsing everyone to a single "goodness" number that could hide very different profiles behind the same total.

### 7. Compare vectors
For each young player, compute cosine similarity (shape match, ignores overall magnitude) and Euclidean distance (overall closeness, magnitude-sensitive) against every role player in the reference pool. Rank role players by similarity to surface the closest comps.


## Results

Results are available in *Spreadsheets/comps/*

Some notable player comparisons:


|Young Player            |Role Player             |Similarity Score|
|------------            |-----------             |----------------|
|Ausar Thompson          |Gary Payton II          | 73.47%         |
|Peyton Watson           |Derrick Jones Jr        | 88.41%         |
|Dominique Barlow        |Derrick Jones Jr        | 89.32%         |
|Max Christie            |Tim Hardaway Jr         | 73.41%         |
|Adem Bona               |Daniel Gafford          | 78.37%         |
|Dereck Lively II        |Daniel Gafford          | 97.35%         |
|Jabari Smith Jr         |Cameron Johnson         | 74.84%         |
|Jaden Hardy             |Malik Monk              | 90.37%         |
|Jarace Walker           |Nickeil Alexander-Walker| 79.67%         |
|Ousmane Dieng           |Nickeil Alexander-Walker| 78.22%         |
|Shaedon Sharpe          |CJ McCollum             | 70.26%         |
|Isaiah Collier          |Dennis Schröder         | 75.83%         |
|Reed Sheppard           |Marcus Smart            | 70.37%         |
|Kel'El Ware             |Andre Drummond          | 83.45%         |
|Leonard Miller          |Aaron Gordon            | 88.73%         |

