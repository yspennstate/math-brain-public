# RG4AR - first-reader report, first-passage-pattern-waiting-time

Reader: an agent, 14 Nov 2026 03:3x. Read on the queued PDF q4/first-passage-pattern-waiting-time/final_e4c5ae2.pdf (7 pp, GitHub e4c5ae2, Zenodo 10.5281/zenodo.24199998), single author.

Paper: "The waiting time for a first-passage pattern in simple random walk". Proves Peres's conjecture (Pitman-Tang, Sem. Prob. XLVII, LNM 2137 (2015) 49-88, Conjecture 1; answers the order question of Pitman-Tang arXiv 1411.0041v3 Question 1.7): for fixed lambda < 0, E T_n is of order n log n, where T_n is the first time the last n steps form a first-passage path to lambda_n.

## Verdict: MINOR REVISION - the proof is correct; one required fix in Table 1 before posting

## Required fix
Table 1 does not follow the paper's own definition of lambda_n. Section 1 (main.tex l.43) defines lambda_n = floor(lambda sqrt n), +1 on a parity mismatch. code/exact.py l.78 uses math.ceil(-math.sqrt(n)) instead. For lambda = -1 the two rules disagree at n = 5, 7, 10, 12, so four rows of Table 1 are E T(FP) for a different level than T_n:

| n | a (table) | a (definition) | |FP| | E T_n under the definition |
|---|---|---|---|---|
| 5 | 1 | 3 | 3 | 18 |
| 7 | 1 | 3 | 9 | 5142/221 = 23.266968 |
| 10 | 2 | 4 | 48 | 5324994284406/140042945269 = 38.024010 |
| 12 | 2 | 4 | 165 | 544077538234598077691978/12502825937677827844627 = 43.516365 |

The other six rows (n = 3, 4, 6, 8, 9, 11) agree with the definition, and every value in the table is exact for the a it lists. The theorem and Table 2 are unaffected: Table 2's a column (10, 14, 22, 32, 44, 100, 316, 1000) follows the floor rule.

The fix:
1. Change line 78 of code/exact.py to math.floor.
2. Rerun to regenerate data/exact.csv.
3. Replace the four rows of Table 1.
4. Rebuild the PDF.
5. Make a new Zenodo version of 24199998.

## What was checked, line by line
- Lemma 2.1: correct.
  - The hitting-time identity f_s(b) = (b/s) p_s(b) follows from the reflection step f_s(b) = (1/2)(p_{s-1}(b-1) - p_{s-1}(b+1)).
  - Gaussian bound (2.3):
    - The even case is a product ratio, with sum_{r<=j}(2r-1) = j^2 and j <= k giving e^{-j^2/(2k)}.
    - The odd case has j(j+1)/(k+j+1) >= (b^2-1)/(4s).
  - sup_b f_s(b) <= C/s.
  - The asymptotic f_n(a_n) ~ alpha sqrt(2/pi) e^{-alpha^2/2}/n checks against Stirling.
- Lemma 3.1: correct.
  - P(J_s = 1) = E|Y_s|/(2s) <= 1/(2 sqrt s), so E V_L <= 1 + sqrt L.
  - The closed form g_s = 4^{-s} C(s-1, floor((s-1)/2))^2 is right by the telescoping identity. Checked by hand for s = 1..4: 1/4, 1/16, 1/16, 9/256.
  - g_s ~ (2 pi s)^{-1}.
  - Strong Markov at sigma_z for the pair holds: a strict new minimum at sigma_z makes later ladder times those of the shifted walk.
  - Each ladder time in [0, 2L] is counted for one z, so G_L E|R_L| <= E V_{2L}.
- Lemma 4.1: correct.
  - The three-piece split is valid. Window [s, n+s] with s <= m < n contains n..n+s-1, so s is a ladder time of Y. The displacement equation gives B in R_m - X_m - a.
  - B is independent of (X, Y) with law S_{n-m}.
  - The bound C sqrt(m)/(sqrt(n-m) log(m+2)) <= C/log n holds uniformly in a.
- Lemma 4.2: correct.
  - The window ending at t+s must end at S_t + w(s), and it needs w(s) < 0 because time t lies inside it.
  - The earlier part of the window sits above the minimum S_t. The remaining event is a first passage of the s new steps.
- Lemma 4.3: correct, and s <= m < n is respected. Decomposing on the first window rho gives E N <= (1 + C H_m) P(N > 0).
- Section 5: correct.
  - f_n(a_n) >= kappa/(2n) gives c/log n <= q_n <= C/log n.
  - The covering count 1 + floor(h/(m+1)) <= 1 + 2h/n holds since m+1 > n/2.
  - h = floor(delta n log n) gives E T_n >= delta n log n/3.
  - Blocks of length n+m are independent with success probability q_n. This gives E T_n <= (n+m)/q_n and the geometric tail.
  - The Moreover clause follows from (5.2) with h = Mn.
- Remark 5.1 and Section 6: the lower bound E T_n >= 2^n/|FP| holds. In the Gerber-Li system, p'M = (E T/2^n) 1' with p >= 0, M_ii >= 1 and M_ij >= 0. Recomputed 1/f_100(10) = 206.29.
- Table 1: recomputed independently (Aho-Corasick automaton, float solve, plus an exact matching-matrix solve). All ten listed values match for the listed a; see the required fix for the level.

## Literature
- Pitman-Tang arXiv 1411.0041v3, read directly:
  - Theorem 1.8(4) (c n <= E T <= C n^{5/4}), Question 1.7, (2.21) and (2.23) (column sums O(n^{1/4})) are cited correctly.
  - Their Table 1 gives 179.8050 at n = 100, as the paper says.
- Published version, Crossref 10.1007/978-3-319-18585-9_4: LNM 2137, pp. 49-88, Pitman and Tang. This matches [5]. The REFCHECK 404 was the escaped underscore in the bib, not the DOI.
- Not checked here: the wording of [5, Conjecture 1] (Springer paywall) and Tang's thesis Conjecture 2.5.2 (escholarship returned 403).
- Gerber-Li, Guibas-Odlyzko and Li DOIs resolve (REFCHECK_auto).
- [7] doi:10.5281/zenodo.24150837 resolves; it is the concept DOI of record 24156239. That record's current title is the Math Brain paper's title, not "public snapshot, code and tests". This is optional and shared by every paper that cites [7], so fix it across the set or leave it.
- Forward citations of Pitman-Tang (OpenAlex, 14 Nov): Pitman-Tang EJP 2015 (Slepian zero set), Ouaki-Pitman / argmin EJP 2018, the spans paper AIHP 2017, Tang's thesis 2017. None addresses the order of E T(FP). A search for later work on first-passage pattern waiting times found nothing that settles the conjecture.

## Recommendation for ResearchGate
Hold #4 from the 05:30 run until Table 1 is fixed and the new Zenodo version exists. The fix is mechanical: the four corrected rows are above, and code/exact.py needs the one-word change.

## Addendum, 14 Nov 03:4x
Fix landed: GitHub aa745db (code/exact.py floor, data/exact.csv regenerated by the repo's own code and matching the rows above, Table 1 rows replaced, PDF rebuilt, 7 pp). Staged as q4/first-passage-pattern-waiting-time/final_aa745db.pdf (md5 67ee35854bd39f0928d8b72050213d99). New Zenodo version of 24199998 requested from an agent; #4 stays held until it exists.
