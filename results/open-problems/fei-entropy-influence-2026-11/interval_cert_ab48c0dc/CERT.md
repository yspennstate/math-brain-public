# Interval enclosures for the monotone tower records

`tower_iv.py` evaluates the composition recursion of `referee_r9/tower_recompute_mp.py` with every quantity an
mpmath interval (outward rounding, 60 digits). Truth tables are exact integers and the start state is exact, so
each printed interval contains the exact value of E/Inf for the composed function, as given by that recursion.
FEIB31 = 4.506400645515568.

| Word | Enclosure of E/Inf (first 30 digits) | Width | Lower end > FEIB31 |
|---|---|---|---|
| M, D^8, P, D, D, dual T(4,3), T(3,5), T(3,5) | 4.506428465445233177909286392452 | 9.6e-49 | yes, by 2.78e-5 |
| D, M^12 | 4.506428305525435411086248568791 | 1.9e-51 | yes, by 2.77e-5 |
| D, M^8, dual PM(4), M, M, T(3,5) | 4.506428462939128775313109412801 | 7.9e-51 | yes, by 2.78e-5 |
| D, M^8, dual PM(K4), M, M, T(3,5) (not a record word) | 4.506427807018563983964577202147 | 1.8e-51 | yes, by 2.72e-5 |

Gates: M = PM(3), D = dual PM(3), P = PM(4), T(k,m) and PMK4 as in `referee_r9/tower_recompute.py`.

The first row is the best word (beam15, 15 levels); its enclosure agrees with the 40-digit point value
4.506428465445233177909286 in `referee_r9/beam15_mp.log` to every printed digit.

Scope: the enclosure is rigorous for the recursion. That the recursion computes E/Inf of the composed Boolean
function is the derivation checked in `referee_r9/REFEREE.md`; this file does not re-prove it.

Logs: `tower_iv_dps60.txt` (rows 1, 2, 4), `tower_iv_dps60_word2_pd.txt` (row 3).
