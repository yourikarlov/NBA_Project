# NBA Player Comps: Clustering Young Players to Role-Player Archetypes

## Motivation

Apply the algorithms studied in class to a field I'm passionate about: basketball.

## Goal

Determine the statistical profile of young players by comparing them to some of the NBA's best role players, to help teams find the players that best fit their needs.

## Example results

| Young player | Closest role-player comp | Cosine similarity |
|---|---|---|
| Dereck Lively II | Daniel Gafford | 97.35% |
| Jaden Hardy | Malik Monk | 90.37% |

## How it works

1. **Collect data** with the `nba_api` package and store the stats in Excel spreadsheets.
2. **Cluster with K-means:** group young players and role players into clusters based on their statistics.
3. **Weighted Z-scores:** turn each player into a vector so a young player can be compared to every role player in the same or closest cluster.
4. **Similarity:** use cosine similarity (tendencies) and Euclidean distance (volume-sensitive) to identify the closest comp for each young player.

## Learn more

- **[clustering.md](https://github.com/yourikarlov/NBA_Project/blob/main/Clustering/clustering.md)**: how players are grouped into archetypes (features, K-means setup, cluster quality).
- **[player_comps.md](https://github.com/yourikarlov/NBA_Project/blob/main/Comparisons/player_comps.md)**: how young players are matched to role players (standardization, weighting, similarity metrics, results).

## Technologies

- Python
- `nba_api`: data extraction source
- Excel: data files
- NumPy: statistical calculations
- Pandas: data manipulation and handling
- Scikit-learn: machine-learning algorithms
