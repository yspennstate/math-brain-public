# Referee notes on P7 (an agent), started 11 Nov before the draft, from p7/OUTLINE.md

## Theorem 3 (BIAS), checked ahead of the text

Statement (outline): H/I <= 2[n/r + 1 + log2(e)/r], r = log2(1/mu), mu = min(P[f=1], P[f=-1]), any Boolean f.

Proof sketch I expect it to follow, derived independently: fhat(empty)^2 = (1-2mu)^2, so the non-empty mass is
W = 4mu(1-mu) <= 4mu, spread over at most 2^n - 1 sets: H <= eta(1-W) + W n + W log2(1/W) <= W(n + log2(e/W)).
Edge isoperimetry gives I >= 2 mu log2(1/mu) = 2 mu r. With W <= 4mu and W log2(e/W) increasing for W <= 1:
H/I <= 4mu(n + log2(e/(4mu)))/(2mu r) = 2[n/r + 1 + (log2(e) - 2)/r], sharper than stated by 4/r. So the stated form
holds with room; check the paper does not need more than this. Edge case to watch: W log2(e/W) is increasing
only for W <= 1, and W = 4mu(1-mu) <= 1 always, fine; and eta(1-W) <= W log2 e is the term absorbed.

Numerics (code/referee_p7_bias_check.py, out in _out.txt): all non-constant f with n <= 4 (65,534 at n=4) and
~9,000 random/sparse/structured f per n = 5..10: 0 violations; max ratio (H/I)/bound 0.72 (n=4) rising to 0.906 (n=10),
so the bound is nearly tight for AND-like f, as the sketch predicts (AND_n: H/I -> 4, bound 4 + 2 log2(e)/n).

## To do when main.tex arrives
Census table against CENSUS_CHECK.md; LOCAL (Thm 2) constant 1/(64L^2); MIX against P6 Lemmas A, h, N; TD(w,Q) obstruction
and the TD(3,7) H/I 4.1346 > 3.8891 remark (census maxima are not class suprema); REL bound; literature (exhaustive small-n
FEI computations; whether BIAS is folklore - it is close to the standard small-bias argument).

## Literature, first pass (11 Nov)
One search for exhaustive small-n FEI computations (all functions, or all monotone / DNF classes, for n <= 8) found only the
theory papers (OWZ, Shalev 1806.03646, KKLMS 1911.10579); no published census of this kind. Not conclusive: check the
GMP 2606.00246 and Paraashar-Saurabh 2611.06451 related-work sections, which FEIB23 read, before the paper says "first".
For the intro: the census maxima (3.889 for H/I) and TD(3,7)'s 4.135 sit well below known lower bounds on the FEI
constant (our own tower records give more than 6.5), so the paper should present them as values for this class, not
as candidates for the constant.

## Census (Theorem 1), independent of the census code (11 Nov 02:1x)

`code/referee_p7_census_check.py` enumerates every labeled linear monotone DNF covering n variables by plain
backtracking over subsets (no canonical forms, no families file) and evaluates both ratios from a dense Walsh transform.

| n | labeled (mine) | sum n!/Aut (paper) | max H/I diff | max min E/Inf diff |
|---|---|---|---|---|
| 3 | 9 | 9 | -4.0e-13 | +2.0e-13 |
| 4 | 97 | 97 | -4.1e-13 | +3.8e-13 |
| 5 | 2625 | 2625 | +8.3e-14 | +1.0e-13 |
| 6 | 185521 | 185521 | +5.2e-14 | -1.4e-13 |

n = 8 attainers recomputed directly: OR of four variables with a 4-cycle on four others gives H/I = 3.889105419815
(its min E/Inf is 2.4194); two disjoint 4-cycles give min E/Inf = 3.304701322451 (its H/I is 3.6125). Both match.
n = 7 and n = 8 labeled counts (35,406,319 and 18,785,639,553) are beyond this script; the paper's two independent counts
(pair recursion and orbit-stabilizer) cover them. Nothing to fix in Theorem 1 as outlined.


## TD numerics (Theorem 5 table), own construction (11 Nov 02:1x)

`code/referee_p7_td_check.py` builds TD(w,Q), Q prime, as the lines {(g, a+bg mod Q)}, asserts linearity, and computes
exact ratios (one coordinate per group; the affine group acts transitively, so E/Inf is the same at every coordinate).
TD(3,3) n=9: P[F=0] 0.4180, H/I 3.0856, E/Inf 2.1015. TD(3,5): 0.1435, 3.8798, 2.7151. TD(4,5): 0.3219, 3.9024, 2.4713.
TD(3,7): 0.0408, 4.1346, 2.5335. All agree with the outline (H/I 3.8798, 3.9024, 4.1346; min E/Inf in 2.10-2.72).
So the remark that the n <= 8 maximum 3.889 is not the class supremum stands (TD(3,7) and TD(4,5) both exceed it).
TD(5,5) n=25: 0.5332, 3.8800, 2.2003. All five rows match the paper's Table 2.

## Report on the draft and re-check of the revision

The line-by-line report on `p7/main.tex`, the six fixes and the re-check of the revised text are in `referee_p7_report_51f2.md`
(kept as its own file because the paper loop cites it by that name). Constants of Theorem local: `code/referee_p7_local_check.py`.
The paper is public: github.com/yspennstate/fei-linear-dnf-census (0479a01).
