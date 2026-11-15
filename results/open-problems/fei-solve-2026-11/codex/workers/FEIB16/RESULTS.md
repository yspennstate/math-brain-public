# FEIB16 results

CHECKED: no unbounded family was found. The strongest values here are the PM(K33) nine-coin tower. All entropies are bits; all three ratios are bits per unit total or coordinate influence.

| Statistic | Current best found | Family and source |
|---|---:|---|
| H/I | 6.521845710923 (limit) | PM nine-coin tower; entropy_highprecision.json |
| H^-/I | 4.588257057307 (limit to shown digits) | PM tower depth 30 plus analytic tail; tail_bounds.json |
| min D_i/Inf_i | 7.111618180512 (limit to shown digits) | same |

PROVED: the tower limits are finite. CHECKED: the depth-30 erasure and minimum-drop tails are below 4.9e-18; logarithms used 80-digit arithmetic, without directed-rounding interval certification. Finite depth-20 functions already give H^-/I > 4.5882570573 and min D_i/Inf_i > 7.1116181805. See highprecision.json.

## Composition search scope

CHECKED: all 222 four-variable NPN representatives and all 16 input phases, with 701 AND/majority/XOR/tribes inner parameter choices, were evaluated uniformly. Mixed assignments used three deterministic starts per objective and coordinate ascent, with at most three sweeps. The three-level search used a 52-message beam from the strongest two-level constructions; it covered every outer gate and input phase uniformly and also optimized mixed assignments. Exact catalog: pool_wide.tsv and pool_wide3_catalog.json.

OPEN: global optimality over mixed assignments, omitted intermediate messages, arbitrary widths, and unrestricted depths. The tables rank evaluated parameterizations; symmetry-equivalent ties can occur. A primitive tribes choice is one allowed inner family, even though it itself has an AND/OR description. “Two-level” and “three-level” count the outer census-gate composition layers above/between these primitive family choices.

CHECKED: notation Fm[hex,p=mask](children) means the exact m-input truth table, with input j negated when bit j of mask is one. Children use disjoint consecutive blocks. “x4” repeats a child on four blocks. truth_hex is printed whenever n<=10; full tables are in small_truth_tables.json.

## 2-level top 20 for H/I

CHECKED within the search scope above. Numeric ranking and exact parameters follow.

| Rank | Ratio | n | Exact construction | truth_hex if n<=10 |
|---:|---:|---:|---|---|
| 1 | 5.100527688049 | 240 | F4[0xfe,p=7](TRIBES(3,14), TRIBES(3,14), TRIBES(3,14), TRIBES(3,38)) |  |
| 2 | 5.100527395349 | 237 | F4[0xfe,p=7](TRIBES(3,14), TRIBES(3,14), TRIBES(3,14), TRIBES(3,37)) |  |
| 3 | 5.100471750348 | 243 | F4[0xfe,p=7](TRIBES(3,14), TRIBES(3,14), TRIBES(3,14), TRIBES(3,39)) |  |
| 4 | 5.100460715081 | 234 | F4[0xfe,p=7](TRIBES(3,14), TRIBES(3,14), TRIBES(3,14), TRIBES(3,36)) |  |
| 5 | 5.095381173652 | 264 | F4[0x88e,p=12](TRIBES(3,22) x4) |  |
| 6 | 5.095246456266 | 252 | F4[0x88e,p=12](TRIBES(3,21) x4) |  |
| 7 | 5.094050053331 | 264 | F4[0x177e,p=0](TRIBES(3,22) x4) |  |
| 8 | 5.094015613166 | 276 | F4[0x88e,p=12](TRIBES(3,23) x4) |  |
| 9 | 5.093381380544 | 252 | F4[0x177e,p=0](TRIBES(3,21) x4) |  |
| 10 | 5.093065377795 | 276 | F4[0x177e,p=0](TRIBES(3,23) x4) |  |
| 11 | 5.092945858388 | 240 | F4[0x88e,p=12](TRIBES(3,20) x4) |  |
| 12 | 5.091656890263 | 288 | F4[0x88e,p=12](TRIBES(3,24) x4) |  |
| 13 | 5.090978081579 | 288 | F4[0x177e,p=0](TRIBES(3,24) x4) |  |
| 14 | 5.090333679447 | 240 | F4[0x177e,p=0](TRIBES(3,20) x4) |  |
| 15 | 5.089277464384 | 252 | F4[0x8ae,p=12](TRIBES(3,21) x4) |  |
| 16 | 5.088692455734 | 240 | F4[0x8ae,p=12](TRIBES(3,20) x4) |  |
| 17 | 5.088685998907 | 300 | F4[0x88e,p=12](TRIBES(3,25) x4) |  |
| 18 | 5.088321972626 | 264 | F4[0x8ae,p=12](TRIBES(3,22) x4) |  |
| 19 | 5.088200563447 | 300 | F4[0x177e,p=0](TRIBES(3,25) x4) |  |
| 20 | 5.087713702516 | 252 | F4[0x77e,p=0](TRIBES(3,21) x4) |  |

## 2-level top 20 for H^-/I

CHECKED within the search scope above. Numeric ranking and exact parameters follow.

| Rank | Ratio | n | Exact construction | truth_hex if n<=10 |
|---:|---:|---:|---|---|
| 1 | 3.850121291403 | 32 | F4[0x2,p=14](TRIBES(2,4) x4) |  |
| 2 | 3.842618848029 | 40 | F4[0xace,p=12](TRIBES(2,5) x4) |  |
| 3 | 3.828086304415 | 32 | F4[0xe,p=15](TRIBES(2,4) x4) |  |
| 4 | 3.810096512264 | 40 | F4[0xe,p=15](TRIBES(2,5) x4) |  |
| 5 | 3.809909199015 | 40 | F4[0x776,p=0](TRIBES(2,5) x4) |  |
| 6 | 3.798629187480 | 32 | F4[0xe,p=7](TRIBES(2,4) x4) |  |
| 7 | 3.798629187480 | 32 | F4[0xe,p=11](TRIBES(2,4) x4) |  |
| 8 | 3.795527046239 | 32 | F4[0xace,p=12](TRIBES(2,4) x4) |  |
| 9 | 3.791400587977 | 32 | F4[0x2,p=10](TRIBES(2,4) x4) |  |
| 10 | 3.791400587977 | 32 | F4[0x2,p=12](TRIBES(2,4) x4) |  |
| 11 | 3.791400587977 | 32 | F4[0x2,p=15](TRIBES(2,4) x4) |  |
| 12 | 3.791400587977 | 32 | F4[0x2,p=6](TRIBES(2,4) x4) |  |
| 13 | 3.783969373526 | 24 | F4[0x2,p=14](TRIBES(2,3) x4) |  |
| 14 | 3.781159227042 | 40 | F4[0x12a,p=8](TRIBES(2,5) x4) |  |
| 15 | 3.774954864949 | 48 | F4[0xace,p=12](TRIBES(2,6) x4) |  |
| 16 | 3.772908965062 | 40 | F4[0x2,p=12](TRIBES(2,5) x4) |  |
| 17 | 3.772908965062 | 40 | F4[0x2,p=6](TRIBES(2,5) x4) |  |
| 18 | 3.772908965062 | 40 | F4[0x2,p=10](TRIBES(2,5) x4) |  |
| 19 | 3.772908965062 | 40 | F4[0x2,p=15](TRIBES(2,5) x4) |  |
| 20 | 3.766954308312 | 48 | F4[0x776,p=0](TRIBES(2,6) x4) |  |

## 2-level top 20 for min D_i/Inf_i

CHECKED within the search scope above. Numeric ranking and exact parameters follow.

| Rank | Ratio | n | Exact construction | truth_hex if n<=10 |
|---:|---:|---:|---|---|
| 1 | 6.258363742048 | 32 | F4[0x2,p=14](TRIBES(2,4) x4) |  |
| 2 | 6.247459273764 | 40 | F4[0xace,p=12](TRIBES(2,5) x4) |  |
| 3 | 6.214381944554 | 40 | F4[0x776,p=0](TRIBES(2,5) x4) |  |
| 4 | 6.210649263536 | 32 | F4[0xe,p=15](TRIBES(2,4) x4) |  |
| 5 | 6.202945526245 | 32 | F4[0xace,p=12](TRIBES(2,4) x4) |  |
| 6 | 6.190745951571 | 24 | F4[0x2,p=14](TRIBES(2,3) x4) |  |
| 7 | 6.176152174609 | 48 | F4[0xace,p=12](TRIBES(2,6) x4) |  |
| 8 | 6.168152408387 | 48 | F4[0x776,p=0](TRIBES(2,6) x4) |  |
| 9 | 6.167945081878 | 40 | F4[0xe,p=15](TRIBES(2,5) x4) |  |
| 10 | 6.145054762246 | 40 | F4[0x12a,p=8](TRIBES(2,5) x4) |  |
| 11 | 6.138779729150 | 48 | F4[0x88ee,p=3](TRIBES(2,6) x4) |  |
| 12 | 6.138779729150 | 48 | F4[0x88ee,p=7](TRIBES(2,6) x4) |  |
| 13 | 6.138779729150 | 48 | F4[0x88ee,p=8](TRIBES(2,6) x4) |  |
| 14 | 6.138779729150 | 48 | F4[0x88ee,p=12](TRIBES(2,6) x4) |  |
| 15 | 6.134259012376 | 40 | F4[0x8e,p=11](TRIBES(2,5) x4) |  |
| 16 | 6.133843965226 | 48 | F4[0x8ae,p=12](TRIBES(2,6) x4) |  |
| 17 | 6.130474785250 | 40 | F4[0x8ae,p=1](TRIBES(2,5) x4) |  |
| 18 | 6.130474785250 | 40 | F4[0x8ae,p=7](TRIBES(2,5) x4) |  |
| 19 | 6.129171565655 | 48 | F4[0x8e,p=11](TRIBES(2,6) x4) |  |
| 20 | 6.128981988324 | 56 | F4[0x88e,p=12](TRIBES(2,7) x4) |  |

## 3-level top 20 for H/I

CHECKED within the search scope above. Numeric ranking and exact parameters follow.

| Rank | Ratio | n | Exact construction | truth_hex if n<=10 |
|---:|---:|---:|---|---|
| 1 | 5.299241089783 | 160 | F4[0xe,p=12](F4[0xe,p=15](TRIBES(2,5) x4) x4) |  |
| 2 | 5.297014623722 | 152 | F4[0xe,p=8](F4[0xe,p=15](TRIBES(2,5) x4), F4[0xe,p=15](TRIBES(2,5) x4), F4[0xace,p=12](TRIBES(2,4) x4), F4[0xe,p=15](TRIBES(2,5) x4)) |  |
| 3 | 5.297014623722 | 152 | F4[0xe,p=4](F4[0xe,p=15](TRIBES(2,5) x4), F4[0xe,p=15](TRIBES(2,5) x4), F4[0xe,p=15](TRIBES(2,5) x4), F4[0xace,p=12](TRIBES(2,4) x4)) |  |
| 4 | 5.289393399806 | 128 | F4[0x2,p=5](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 5 | 5.289393399806 | 128 | F4[0x2,p=9](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 6 | 5.289393399806 | 128 | F4[0x2,p=0](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 7 | 5.289393399806 | 128 | F4[0x2,p=3](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 8 | 5.287758540357 | 160 | F4[0x2,p=6](F4[0xe,p=15](TRIBES(2,5) x4) x4) |  |
| 9 | 5.287758540357 | 160 | F4[0x2,p=10](F4[0xe,p=15](TRIBES(2,5) x4) x4) |  |
| 10 | 5.287758540357 | 160 | F4[0x2,p=12](F4[0xe,p=15](TRIBES(2,5) x4) x4) |  |
| 11 | 5.287758540357 | 160 | F4[0x2,p=15](F4[0xe,p=15](TRIBES(2,5) x4) x4) |  |
| 12 | 5.285230918622 | 128 | F4[0xe,p=3](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 13 | 5.281716053566 | 160 | F4[0x2,p=2](F4[0xe,p=15](TRIBES(2,5) x4) x4) |  |
| 14 | 5.281716053566 | 160 | F4[0x2,p=4](F4[0xe,p=15](TRIBES(2,5) x4) x4) |  |
| 15 | 5.281716053566 | 160 | F4[0x2,p=7](F4[0xe,p=15](TRIBES(2,5) x4) x4) |  |
| 16 | 5.281716053566 | 160 | F4[0x2,p=8](F4[0xe,p=15](TRIBES(2,5) x4) x4) |  |
| 17 | 5.281716053566 | 160 | F4[0x2,p=11](F4[0xe,p=15](TRIBES(2,5) x4) x4) |  |
| 18 | 5.281716053566 | 160 | F4[0x2,p=13](F4[0xe,p=15](TRIBES(2,5) x4) x4) |  |
| 19 | 5.281508002369 | 128 | F4[0x2,p=1](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 20 | 5.281118120121 | 128 | F4[0x2,p=4](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |

## 3-level top 20 for H^-/I

CHECKED within the search scope above. Numeric ranking and exact parameters follow.

| Rank | Ratio | n | Exact construction | truth_hex if n<=10 |
|---:|---:|---:|---|---|
| 1 | 4.059086444978 | 128 | F4[0xace,p=12](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 2 | 4.057330439061 | 128 | F4[0xace,p=4](F4[0xace,p=12](TRIBES(2,4) x4), F4[0xace,p=12](TRIBES(2,4) x4), F4[0xace,p=12](TRIBES(2,4) x4), F4[0xe,p=15](TRIBES(2,4) x4)) |  |
| 3 | 4.057330439061 | 128 | F4[0xace,p=8](F4[0xace,p=12](TRIBES(2,4) x4), F4[0xace,p=12](TRIBES(2,4) x4), F4[0xe,p=15](TRIBES(2,4) x4), F4[0xace,p=12](TRIBES(2,4) x4)) |  |
| 4 | 4.055280967586 | 128 | F4[0xe,p=15](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 5 | 4.050834130681 | 128 | F4[0x2,p=14](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 6 | 4.049088356602 | 128 | F4[0xace,p=3](F4[0xe,p=15](TRIBES(2,4) x4) x4) |  |
| 7 | 4.038860140561 | 128 | F4[0x2,p=15](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 8 | 4.038860140561 | 128 | F4[0x2,p=10](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 9 | 4.038860140561 | 128 | F4[0x2,p=12](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 10 | 4.038860140561 | 128 | F4[0x2,p=6](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 11 | 4.037537914344 | 128 | F4[0xe,p=11](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 12 | 4.037537914344 | 128 | F4[0xe,p=7](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 13 | 4.035875155959 | 128 | F4[0xe,p=0](F4[0xe,p=15](TRIBES(2,4) x4) x4) |  |
| 14 | 4.031627973626 | 128 | F4[0x776,p=0](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 15 | 4.031499918773 | 128 | F4[0x776,p=15](F4[0xe,p=15](TRIBES(2,4) x4) x4) |  |
| 16 | 4.028782420122 | 128 | F4[0xace,p=3](F4[0x2,p=14](TRIBES(2,4) x4) x4) |  |
| 17 | 4.026212970234 | 128 | F4[0x12a,p=8](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 18 | 4.021245424336 | 128 | F4[0xae,p=1](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 19 | 4.021245424336 | 128 | F4[0xae,p=7](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 20 | 4.020370317152 | 128 | F4[0xee,p=3](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |

## 3-level top 20 for min D_i/Inf_i

CHECKED within the search scope above. Numeric ranking and exact parameters follow.

| Rank | Ratio | n | Exact construction | truth_hex if n<=10 |
|---:|---:|---:|---|---|
| 1 | 6.468607549690 | 128 | F4[0xace,p=12](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 2 | 6.460778843604 | 128 | F4[0xe,p=15](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 3 | 6.460338356632 | 128 | F4[0x2,p=14](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 4 | 6.446486611341 | 128 | F4[0xace,p=3](F4[0xe,p=15](TRIBES(2,4) x4) x4) |  |
| 5 | 6.441052929120 | 128 | F4[0x776,p=0](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 6 | 6.437764767115 | 128 | F4[0xace,p=3](F4[0x2,p=14](TRIBES(2,4) x4) x4) |  |
| 7 | 6.435089472171 | 128 | F4[0x12a,p=8](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 8 | 6.427778072142 | 128 | F4[0x776,p=15](F4[0xe,p=15](TRIBES(2,4) x4) x4) |  |
| 9 | 6.427222205215 | 128 | F4[0x776,p=15](F4[0x2,p=14](TRIBES(2,4) x4) x4) |  |
| 10 | 6.424316237711 | 128 | F4[0x180,p=7](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 11 | 6.424316237711 | 128 | F4[0x180,p=8](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 12 | 6.414040467932 | 128 | F4[0xe,p=0](F4[0xe,p=15](TRIBES(2,4) x4) x4) |  |
| 13 | 6.404902704411 | 128 | F4[0xaee,p=3](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 14 | 6.404902704411 | 128 | F4[0xaee,p=12](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 15 | 6.401277822483 | 128 | F4[0x2,p=1](F4[0xe,p=15](TRIBES(2,4) x4) x4) |  |
| 16 | 6.400135429679 | 128 | F4[0x12a,p=7](F4[0xe,p=15](TRIBES(2,4) x4) x4) |  |
| 17 | 6.397572664584 | 128 | F4[0xe,p=0](F4[0x2,p=14](TRIBES(2,4) x4) x4) |  |
| 18 | 6.397129768048 | 128 | F4[0x8e,p=11](F4[0xace,p=12](TRIBES(2,4) x4) x4) |  |
| 19 | 6.396596310561 | 128 | F4[0x88ee,p=3](F4[0x2,p=14](TRIBES(2,4) x4) x4) |  |
| 20 | 6.396596310561 | 128 | F4[0x88ee,p=7](F4[0x2,p=14](TRIBES(2,4) x4) x4) |  |

## Five-variable biased-inner scan

CHECKED: 616,126 imported NPN representatives, all 32 input phases, and 13 inner choices gave 256,308,416 evaluations. Uniform inner blocks make outer variable permutations irrelevant; global output sign leaves all ratios unchanged. The input phases therefore cover every outer function on at most five variables modulo these invariances. The imported census includes lower-dimensional functions with dummies.

CHECKED inner parameters: AND(2), AND(3), AND(4), AND(6), AND(8), THR(3,2), THR(4,2), THR(5,2), THR(5,3), THR(6,2), THR(7,3), THR(8,3), THR(9,4). Complete top-20 tables for all three statistics are in ranked_compositions.json under key 5; native outputs are census5.tsv and census5_entropy.tsv. The entropy rescan uses stable empty-mass normalization.

| Statistic | Best | Exact construction | truth_hex if n<=10 |
|---|---:|---|---|
| H/I | 4.128880076270 | F5[0xe0eee,p=28](AND(3) x5) |  |
| H^-/I | 3.433874258511 | F5[0xe,p=0](AND(2) x5) | 000000000000000000000000000000000000000000000000000000000000000000000000000000000000f888f888f8880000f888f888f8880000f888f888f88800000000000000000000f888f888f8880000f888f888f8880000f888f888f88800000000000000000000f888f888f8880000f888f888f8880000f888f888f888 |
| min D_i/Inf_i | 5.784103212114 | F5[0xeee,p=12](AND(2) x5) | 0000000000000000000000000000000000000000000000000000000000000000f888f888f888f888f888000000000000f888000000000000f888000000000000f888f888f888f888f888000000000000f888000000000000f888000000000000f888f888f888f888f888000000000000f888000000000000f888000000000000 |

OPEN: no claim that these finite inner-parameter ranges optimize all thresholds or all biases.

## Plain tribes and the other families

CHECKED: tribes_grid.json scans 4,679,850 pairs (w,s) with 1<=w<=60, ws<=1,000,000; FORMULAS.md bounds all larger widths out of these maxima. The H/I grid uses scaled formulas even where entropy and influence separately underflow.

| Ratio | Best in the requested tribes size range | Parameters |
|---|---:|---|
| H/I | 5.073260334252 | w=3, s=333333, n=999999 |
| H^-/I | 3.606847002096 | w=2, s=8, n=16 |
| min D_i/Inf_i | 6.003746056559 | w=2, s=8, n=16 |

PROVED: formulas and limits for tribes, majority, bent/MM, complete quadratics, address, fresh-dictator patches, XOR and AND are in FORMULAS.md. CHECKED: families_clean.json is the family survey, stable_readonce.json covers every requested regular-tree depth through six, family_limits.json compares depth six with depth twenty, majority_large.json reaches 1,000,001 variables, and pm_biased_towers.json records the additional biased seed and host towers. Its variance cutoff is explicit; rows beyond the cutoff were not evaluated.

CHECKED: PM tower orbit ratios are in pm_orbits_depth6.csv and pm_orbits_depth10.csv. The exact word formula in FORMULAS.md gives every orbit at depth 20, 30 or 50 without expanding their exponential list. WITNESSES.md gives the parity, block and level statistics.

## Family growth and limits

PROVED: FORMULAS.md gives the limits below. CHECKED: the depth-20 rows are finite evaluations, not replacements for certified decimal limits. All triples are (H/I, H^-/I, min D_i/Inf_i).

| Family | Limit or exact relation |
|---|---|
| AND/OR on growing arity | (4, 2, 4) |
| Balanced tribes, growing width | (4, 2, 4) |
| Fixed-width tribes, growing count | exact three limits in FORMULAS.md Section 2 |
| Majority of growing odd arity | (2/ln 2, 0, 0) |
| Iterated fixed odd majority g | (H(g)/(I(g)-1), 0, 0) |
| Bent, Maiorana–McFarland, even complete quadratic | (2, 2, 4), exactly |
| Odd complete quadratic, growing dimension | (2, 0, 0); exact H/I=2-2/n |
| Address with growing selector count | (4, 2, 0) |
| Bent subspace patches, replaced fraction tending to zero | (2, 2, 4); fresh coordinates individually have growing erasure cost |
| Disjoint XOR | H/I and H^-/I are influence-weighted averages; R is the component minimum |
| Disjoint AND | exact biased two-input composition law in Section 1 |
| PM nine-coin self-compositions | (6.521845710923, 4.588257057307, 7.111618180512) |

PROVED: each fixed recursive-tribes and regular AND/OR family below has finite limits, by FORMULAS.md Section 8. CHECKED: finite growth through depth 20 follows.

| Family | Depth 6 triple | Depth 20 triple | Largest last-step change at depth 20 |
|---|---|---|---:|
| TRIBES(2,2) | 5.319033756, 3.656019453, 6.045958468 | 5.344866758, 3.655710535, 6.045649549 | 1.53e-06 |
| TRIBES(2,3) | 5.832214004, 4.126377832, 6.538053883 | 5.836303667, 4.126377832, 6.538053883 | 1.71e-09 |
| TRIBES(2,4) | 5.471465018, 3.909867702, 6.318555773 | 5.471989825, 3.909867702, 6.318555773 | 5.87e-12 |
| TRIBES(2,6) | 5.201346754, 3.655393105, 6.055959952 | 5.201386491, 3.655393105, 6.055959952 | 2.66e-15 |
| TRIBES(2,8) | 5.071354792, 3.512733779, 5.908637527 | 5.071361525, 3.512733779, 5.908637527 | 0 |
| TRIBES(2,12) | 4.937407179, 3.392193551, 5.784237313 | 4.937407748, 3.392193551, 5.784237313 | 0 |
| TRIBES(3,2) | 4.430895502, 2.574333463, 4.752779320 | 4.432544367, 2.574333463, 4.752779320 | 6.89e-10 |
| TRIBES(3,3) | 4.820796775, 2.962629740, 5.169100365 | 4.822623002, 2.962629740, 5.169100365 | 7.64e-10 |
| TRIBES(3,4) | 5.233994125, 3.249737142, 5.464004631 | 5.236165149, 3.249737142, 5.464004631 | 9.08e-10 |
| TRIBES(3,6) | 5.911713019, 3.576656944, 5.794451799 | 5.911918567, 3.576656944, 5.794451799 | 1.33e-14 |
| TRIBES(3,8) | 5.703828141, 3.579990253, 5.798037223 | 5.703845398, 3.579990253, 5.798037223 | 0 |
| TRIBES(3,12) | 5.500130241, 3.492059543, 5.709569357 | 5.500131351, 3.492059543, 5.709569357 | 0 |
| TRIBES(4,2) | 4.213321051, 2.255668487, 4.341001058 | 4.213602274, 2.255668487, 4.341001058 | 3.14e-12 |
| TRIBES(4,3) | 4.384131999, 2.427180416, 4.527735151 | 4.384422945, 2.427180416, 4.527735151 | 3.25e-12 |
| TRIBES(4,4) | 4.533185916, 2.552561010, 4.658171390 | 4.533487692, 2.552561010, 4.658171390 | 3.37e-12 |
| TRIBES(4,6) | 4.809840968, 2.729757658, 4.838616223 | 4.810171457, 2.729757658, 4.838616223 | 3.69e-12 |
| TRIBES(4,8) | 5.092330647, 2.854404102, 4.964188841 | 5.092711958, 2.854404102, 4.964188841 | 4.26e-12 |
| TRIBES(4,12) | 5.675577480, 3.012969495, 5.123209792 | 5.675588360, 3.012969495, 5.123209792 | 0 |
| AND_OR_TREE(2) | 4.592436422, 3.655077346, 6.045062735 | 5.343302839, 3.655710535, 6.045649549 | 0 |
| OR_OR_TREE(2) | 4.592436422, 3.655077346, 6.045062735 | 5.343302839, 3.655710535, 6.045649549 | 0 |
| AND_OR_TREE(3) | 4.767716381, 2.965644815, 5.172115634 | 4.822600456, 2.962629740, 5.169100365 | 0 |
| OR_OR_TREE(3) | 4.767716381, 2.965644815, 5.172115634 | 4.822600456, 2.962629740, 5.169100365 | 0 |
| AND_OR_TREE(4) | 4.514173878, 2.552561078, 4.658171458 | 4.533486514, 2.552561010, 4.658171390 | 0 |
| OR_OR_TREE(4) | 4.514173878, 2.552561078, 4.658171458 | 4.533486514, 2.552561010, 4.658171390 | 0 |

OPEN: the displayed depth-20 triples do not have the PM tower’s separate certified analytic remainder enclosure. PM host and biased-seed tower values and numerical cutoffs are in pm_biased_towers.json.

## Validation

CHECKED: validation.json, audit.json, stable_readonce_audit.json and results_build_audit.json contain independent numerical checks. Direct small truth tables agree to tolerance 1e-12. Larger formulas were checked with independent Python/native implementations, exact dyadic spectra, direct restriction entropy, path dynamic programming and 80-digit arithmetic.

CHECKED: all writes stayed in FEIB16; no hill climb, helper agent, git push, external post or trading process was used. Brain recall identified the exact PM record and supplied relevant prior cautions.
