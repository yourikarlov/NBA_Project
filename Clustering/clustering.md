# NBA Player Clustering Analysis

## Overview

This project applies clustering to two groups of NBA players:
- **Role players** — based on their average statistical profile over the last **4 seasons**
- **Young players** — based on all available seasons

The analysis focuses on players who:
- Played more than **25 games**
- Were grouped using a combination of shooting profile, creation, rebounding, and defensive metrics

The goal is to identify **player archetypes**:

- What type of shots does a player take?
- Are they primary creators or connectors?
- Are they elite rebounders or interior defenders?
- What role do they fill on a team?

---

## Features Used

The clustering model uses the following features:

### Shot Profile
- `RA_FREQ` — Restricted area shot frequency
- `MID_FREQ` — Mid-range shot frequency
- `LC3_FREQ` — Left corner 3 frequency
- `RC3_FREQ` — Right corner 3 frequency
- `AB3_FREQ` — Above-the-break 3 frequency

### Creation
- `%AST` — Of the team's assists while this player is on court, the percentage credited to him.
- `USG%` — Usage percentage
- `AST/TO` — Assist-to-turnover ratio

### Rebounding
- `%OREB` — Of the team's offensive rebounds while this player is on court, the percentage grabbed by him.
- `%DREB` — Of the team's defensive rebounds while this player is on court, the percentage grabbed by him.

	
### Defense
- `%STL` — Steal percentage
- `%BLK` — Block percentage

---

## Clustering Results

### Model Performance

- **Number of clusters:** 6
- **Role Players Silhouette Score:** `0.2192`
- **Young Players Silhouette Score:** `0.2322`

The silhouette scores suggest moderate separation between player archetypes, which is expected given the correlated nature of NBA statistics and the positional fluidity of modern players. The clusters still represent meaningful and coherent NBA roles.

---

# Role Player Archetypes

## Cluster 0 — Defensive Wings

**Profile**
- High defensive impact
- Low offensive usage
- Disruptive perimeter defenders

**Players (4)**

- Alex Caruso
- Derrick Jones Jr.
- Gary Payton II
- Matisse Thybulle

**Role Description**

> Defensive specialists who provide elite point-of-attack defense, steals, and athletic impact.

---

## Cluster 1 — Scoring Forwards / Stretch Bigs

**Profile**
- Versatile scoring forwards
- Mix of inside scoring and perimeter shooting
- Moderate usage and rebounding impact

**Players (14)**

- Aaron Gordon
- Bobby Portis
- Brook Lopez
- Dillon Brooks
- Jerami Grant
- John Collins
- Kelly Oubre Jr.
- Michael Porter Jr.
- Miles Bridges
- Naz Reid
- Nikola Vučević
- P.J. Washington
- Rui Hachimura
- Tobias Harris

**Role Description**

> Frontcourt scorers who provide size, spacing, and secondary offense.

---

## Cluster 2 — Interior Anchors

**Profile**
- Elite rebounders
- Strong rim protection
- High paint presence

**Players (8)**

- Andre Drummond
- Daniel Gafford
- Isaiah Hartenstein
- Ivica Zubac
- Jusuf Nurkić
- Luke Kornet
- Mitchell Robinson
- Robert Williams III

**Role Description**

> Traditional big men who dominate the interior through rebounding, screening, and rim protection.

---

## Cluster 3 — Two-Way Connectors / Playmakers

**Profile**
- Balanced offensive and defensive contribution
- Secondary playmaking
- Versatility

**Players (8)**

- Bruce Brown
- Caris LeVert
- Derrick White
- Josh Hart
- Marcus Smart
- Mikal Bridges
- Payton Pritchard
- Ty Jerome

**Role Description**

> Versatile role players who connect lineups through passing, defense, shooting, and decision-making.

---

## Cluster 4 — Snipers / Movement Shooters

**Profile**
- High three-point volume
- Low creation responsibility
- Spacing-focused offensive role

**Players (10)**

- Al Horford
- Cameron Johnson
- Donte DiVincenzo
- Duncan Robinson
- Grayson Allen
- Landry Shamet
- Max Strus
- Nickeil Alexander-Walker
- Royce O'Neale
- Tim Hardaway Jr.

**Role Description**

> Elite floor spacers who create value through shooting gravity, off-ball movement, and efficient perimeter scoring.

---

## Cluster 5 — Shot Creators

**Profile**
- High usage
- Ball-dominant offense
- Self-created scoring ability

**Players (6)**

- CJ McCollum
- Dennis Schröder
- Fred VanVleet
- Jordan Clarkson
- Khris Middleton
- Malik Monk

**Role Description**

> Guards and wings capable of generating offense through isolation, pick-and-roll, and difficult shot creation.

---

# Young Player Archetypes

## Cluster 0 — Two-Way Connectors / Playmakers

**Profile**
- Balanced offensive and defensive contribution
- Secondary playmaking
- Versatility

**Players (4)**

- Brandin Podziemski
- Isaiah Collier
- Jamal Shead
- Reed Sheppard

**Role Description**

> Young connectors who contribute through passing, decision-making, and two-way play.

---

## Cluster 1 — Shot Creators

**Profile**
- High usage and shot volume
- Self-created scoring ability
- Limited playmaking responsibility

**Players (9)**

- Brice Sensabaugh
- GG Jackson
- Jabari Smith Jr.
- Jaden Hardy
- Jarace Walker
- Jared McCain
- Jonathan Kuminga
- Ousmane Dieng
- Shaedon Sharpe

**Role Description**

> Young scorers who generate offense through individual creation and high shot volume.

---

## Cluster 2 — Defensive Specialists / Two-Way Wings

**Profile**
- High defensive impact
- Athletic, disruptive defenders
- Versatile across positions

**Players (7)**

- Anthony Black
- Ausar Thompson
- Bilal Coulibaly
- Dominick Barlow
- Dyson Daniels
- Jeremy Sochan
- Peyton Watson

**Role Description**

> Young wings who make their mark through defensive versatility, athleticism, and two-way impact.

---

## Cluster 3 — Versatile Bigs

**Profile**
- Mix of interior and perimeter play
- Developing shot profile
- Moderate rebounding and size

**Players (3)**

- Kel'el Ware
- Kyle Filipowski
- Leonard Miller

**Role Description**

> Big men with versatile skill sets who don't fit the traditional interior anchor mold.

---

## Cluster 4 — Interior Anchors

**Profile**
- Elite rebounders
- Strong rim protection
- High paint presence

**Players (3)**

- Adem Bona
- Dereck Lively II
- Yves Missi

**Role Description**

> Young big men who dominate the interior through rebounding and rim protection.

---

## Cluster 5 — 3&D Wings

**Profile**
- High three-point volume
- Defensive engagement
- Low creation responsibility

**Players (4)**

- Ja'Kobe Walter
- Jaylen Wells
- Max Christie
- Ryan Dunn

**Role Description**

> Wings who create value through perimeter shooting and on-ball defense.

---

# Summary

## Role Players

| Cluster | Archetype | Main Value |
|---|---|---|
| 0 | Defensive Wings | Perimeter defense |
| 1 | Scoring Forwards / Stretch Bigs | Frontcourt scoring versatility |
| 2 | Interior Anchors | Rebounding & rim protection |
| 3 | Two-Way Connectors / Playmakers | Versatility & playmaking |
| 4 | Snipers / Movement Shooters | Shooting & spacing |
| 5 | Shot Creators | Self-generated offense |

## Young Players

| Cluster | Archetype | Main Value |
|---|---|---|
| 0 | Two-Way Connectors / Playmakers | Versatility & playmaking |
| 1 | Shot Creators | Self-generated offense |
| 2 | Defensive Specialists / Two-Way Wings | Defensive versatility |
| 3 | Versatile Bigs | Frontcourt versatility |
| 4 | Interior Anchors | Rebounding & rim protection |
| 5 | 3&D Wings | Shooting & perimeter defense |

The biggest distinction between clusters comes from the balance between:

- **Shot profile**
- **Offensive creation responsibility**
- **Defensive impact**
- **Rebounding role**

These clusters provide a statistical view of how modern NBA players contribute beyond traditional positions.
