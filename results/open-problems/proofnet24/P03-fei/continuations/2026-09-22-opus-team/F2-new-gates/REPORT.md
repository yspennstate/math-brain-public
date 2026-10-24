# F2: new balanced base functions for the FEI lower bound

No balanced function with H/(I-1) above 6.521845710923046575 was found.

- PROVED (elementary; proofs in Section 1): the exact spectral formulas for a partial core whose holes are filled by fresh variables; the per-site influence formula; the entropy cost 4/N when two coin sites share one variable; a mediant bound showing that balanced disjoint fills other than dictators cannot raise the ratio unless the fill beats it on its own.
- CERTIFIED (`code/certify.py`: exact integer Walsh transform, exact rational I, mpmath outward-rounded interval arithmetic for H): Numaro's value; the identification of Numaro's g as the perfect-matching property of K_{3,3} with nine coins (the rebuilt table has the published SHA-256); the 17-variable record as the same construction with two sites sharing one coin (all 36 choices give 6.514326913930565372650…); a 14-variable member of the same family with H/(I-1) = 6.49177052295312176…, above the published 14-variable value 6.4901128435233943.
- NUMERICAL (float64; exhaustive over the stated neighbourhoods, or annealing): g is a strict local optimum under every balanced two-cell change of its 9-variable core (best 6.50148), of its 10-variable embedding (best 6.51711), under every relocation of one coin site (best 6.48279), and under every new coin on a true-false edge of the 18-cube (best 6.52170); it is the unique optimum among all 3^13 cores invariant under its symmetry group; other hosts and design groups gave at most 5.94.
- FAILED: no new record, and no family with growing ratio.

## 1. Cores with holes

Let m be the number of core variables, N = 2^m, and c0 : {0,1}^m -> {-1,0,+1} with Σ c0 = 0. Let the holes Z = c0^{-1}(0) be partitioned into groups A_1, …, A_k, with fresh uniform ±1 variables y_j, and put F(x,y) = c0(x) + Σ_j 1_{A_j}(x) y_j. Then F is ±1-valued and balanced. Write W0(S) = Σ_x c0(x) χ_S(x) and W_j(S) = Σ_{x ∈ A_j} χ_S(x).

(1.1) F^(S, ∅) = W0(S)/N, F^(S, {y_j}) = W_j(S)/N, and F^(S, T) = 0 for |T| ≥ 2 (F is affine in y).

(1.2) H(F) = Σ_S φ(W0(S)/N) + Σ_j Σ_S φ(W_j(S)/N), where φ(t) = t² log2(1/t²).

(1.3) I(F) = (1/2N) [ Σ_{edges xy of Q_m} (c0(x) - c0(y))² + Σ_j ((m+2)|A_j| - 2 e(A_j)) ], where e(A) is the number of cube edges inside A.

Proof of (1.3). For real g, Σ_S |S| g^(S)² = (1/4) E Σ_i (g(x) - g(x ⊕ e_i))². Apply this to c0 and to 1_{A_j}; for the latter it gives (m|A| - 2e(A))/(2N). The y_j-degree adds |A_j|/N. This was checked exactly against the 2^18 Walsh transform of g (`code/decompose_numaro.py`).

Group entropies. A singleton has 2m/N. Any two cells have 4(m-1)/N. A d-dimensional subcube has 2^{d+1}(m-d)/N.

Merging lemma. Take P = {a, a ⊕ e_i} and Q = {b, b ⊕ e_j} with i ≠ j and a ⊕ b ∉ span{e_i, e_j}. Then (χ_S(e_i), χ_S(e_j), χ_S(a ⊕ b)) is uniform on {±1}^3, so |W_{P∪Q}| takes the values 4, 2, 0 with frequencies 1/8, 1/2, 3/8. The shared-variable entropy is (8m - 12)/N, against (8m - 8)/N for two variables: a loss of 4/N. Influence is unchanged if no edge joins P and Q.

Per-site influence. Turning a cube edge {a, b} of two false cells (value +1) into one coin pair changes I by 2(m - T)/N, where T is the number of true neighbours of a and b other than each other.

Mediant lemma. Filling A_j with a balanced f on fresh variables instead of y_j adds w_j H(f) to H and w_j (I(f) - 1) to I - 1, with w_j = |A_j|/N. The new ratio is therefore a mediant of the old one and H(f)/(I(f) - 1). Unbalanced fills are biased compositions (group F1).

## 2. Numaro's g is the perfect-matching function of K_{3,3} with nine coins

Identify core variable i = 3r + c with the edge rc of K_{3,3}, and let X be the set of present edges. For p = rc put cross(p) = star(r) ∪ star(c), a 5-edge graph without a perfect matching. Then

  g(X, y) = TRUE iff X contains a perfect matching, or (X ∈ {cross(p), cross(p) \ {p}} and y_p = TRUE).

`code/pm33_coins.py` builds g from this description alone and reproduces SHA-256 f8a7bb2c…9c7839 (coin j acts at point [0,3,8,4,1,7,5,2,6][j]).

- Pr[perfect matching] = 247/512, so the deficit of 18 true cells is exactly the 18 cells of the nine crosses.
- Each site is a cube edge between Hamming weights 4 and 5, one site in each coordinate direction.
- I(PM) = 513/256. Each site has T = 8, so each adds 2/512: I(g) = 513/256 + 9/256 = 261/128.
- H(g) = H_core + 9/16, where H_core = 6.214105309005978082519790221891882314787235038… is the entropy of PM with the 18 site cells set to 0.
- I_core = 477/256, I_aux = 45/256.
- By König's theorem the crosses are exactly the maximal graphs covered by one left vertex and one right vertex.
- In AG(2,3) language: stars are the lines of two parallel classes, and perfect matchings are the lines of the other two classes.
- Exhaustive over S_9 (`code/autgroup.py`): the plain automorphism group of the core is Aut(K_{3,3}), of order 72, and there are 72 anti-automorphisms X -> complement(πX), c0 -> -c0.

## 3. The published notes

Letting two sites share a coin lowers H by 4/512 = 1/128 at identical influence. The sites are pairwise non-adjacent and the lemma's condition holds for all pairs, so the ratio drops by (1/128)/(133/128) = 1/133 exactly. Read in reverse, this is the published "2+2 split with the new 18th variable": H rises by twice the moved weight 2/512.

CERTIFIED: all 36 merges give 6.51432691393056537265…, the published 17-variable value (`logs/check_17var_merges.log`).

## 4. What limits the construction at 18 variables

Maximum H/(I-1) against the number k of auxiliaries (`code/aux_count_curve.py`, 60 digits; k = 5, 8, 9 also interval-certified). For k ≤ 9, the maximum is over all 21147 partitions of the 9 sites. For k ≥ 10, j = k - 9 sites are split into two singleton coins each; every split adds (4/512, 1/512) to (H, I-1), a direction of ratio 4.

| k | n | max H/(I-1) |
|---|---|---|
| 1 | 10 | 6.401103254143229 |
| 2 | 11 | 6.447467561975327 |
| 3 | 12 | 6.467901167915776 |
| 4 | 13 | 6.481307805609846 |
| 5 | 14 | 6.491770522953122 |
| 6 | 15 | 6.499289319945603 |
| 7 | 16 | 6.506808116938084 |
| 8 | 17 | 6.514326913930565 |
| 9 | 18 | 6.521845710923047 |
| 10 | 19 | 6.517114293078913 |
| 11 | 20 | 6.512400595900863 |
| 12 | 21 | 6.507704520020674 |
| 13 | 22 | 6.503025966811681 |
| 14 | 23 | 6.498364838381864 |
| 15 | 24 | 6.493721037567027 |
| 16 | 25 | 6.489094467924046 |
| 17 | 26 | 6.484485033724187 |
| 18 | 27 | 6.479892639946508 |

Other changes (NUMERICAL, every candidate enumerated):

| Change | Best | Log |
|---|---|---|
| Any balanced two-cell change of the core | 6.501477 | `scan_numaro_2cell.log` |
| Relocation of one site to any false-false edge | 6.482786 | `scan_relocate_sites.log` |
| New coin on any true-false edge of the 18-cube (19 variables; rechecked from scratch) | 6.521699935 | `scan_newcoin_18_fixed.log` |
| Two-cell change of the 10-variable embedding | 6.517114 | `scan_m10_embedding.log` |

The limit is the core: PM(K_{3,3}) has exactly nine coin sites, its deficit is exactly their 18 cells, and one variable per site is optimal.

## 5. Searches beyond the record (NUMERICAL)

- Invariant cores at 9 variables: exhaustive over all 3^13 cores invariant under the order-144 group gives a unique optimum, g (`enum_G144_m9.log`). Invariant pure Boolean cores reach at most 6.283175. Of the 24 subgroup classes, the three with at most 15 orbits all give g (`subgroups_m9.log`).
- Annealing from g: at m = 9 (T0 = 0.003–0.03, 4·10^6 steps) and m = 10, nothing above g.
- Random-start annealing: at m = 4–6 it always returns a 6-variable function with 6.347067498702. At m = 7 it fails to reach even that value, so it is not evidence about m = 7.
- Design groups with complement duality (exhaustive): Fano plane 5.0456, AGL(3,2) 5.3799, AGL(2,3) 5.3570.
- Other hosts (Aut-invariant cores, exact balance, pair-matched coins; heuristic):

| Host | Variables | Matching / line probability | Best ratio |
|---|---|---|---|
| K_{3,4} | 12 | 3125/4096 | 5.9389 |
| K_{4,4} | 16 | 37823/65536 | 4.98 (one restart) |
| PG(2,3) line containment | 13 | 3862/8192 | ≤ 5.3890 |
| AG(2,4), three line classes | 16 | 30539/65536 | not searched |

- Observation (not a theorem): in K_{n,n}, the matching-free graphs covered by one left and one right vertex have 2n - 1 edges. That sits at the middle layer only for n = 3.

## 6. Growth

- In the record family the ratio is a finite sequence in k, with its maximum at Numaro's value, attained.
- Self-composition keeps H/(I-1) exactly constant.
- Balanced disjoint fills give mediants (PROVED). F1 reports that g is locally optimal under input bias.
- The fleet's shared-coordinate grafts converge near 6.52185 (their tail bounds; not recomputed here).
- No family with growing H/(I-1) was found; everything examined is bounded by about 6.5219.

## 7. Files

Code is in `code/`, outputs in `logs/`.

- Checker: `python code/certify.py logs/desc_numaro18.json 6.521845710923046575` (self-check in `logs/certify_numaro18_selfcheck.log`).
- Identification check: `python code/pm33_coins.py inputs/numaro18_pm1_table.npy`.
- 14-variable certificate: `logs/desc_pm33_5coins_n14.json`, checked in `logs/certify_pm33_5coins_n14.log`.
- One scan had an influence-bookkeeping error; its log is renamed `SUPERSEDED_…` with the correction written inside the file, and the corrected run is `logs/scan_newcoin_18_fixed.log`.
