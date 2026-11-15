# T189: an FPRAS for counting perfect matchings in general graphs

Checked 12 Nov 2026. Status of the row: **reported solved, and the report stands up to a partial check.** Two written
proofs exist, the second by authors independent of the first. Everything except the proof of the two-matching
Poincaré inequality was verified here by hand; that inequality was tested by computer on K_6 and K_8 and its proof was
read but not verified line by line.

## What is claimed

1. OpenAI, "A Fully Polynomial Randomized Approximation Scheme for Perfect Matchings in General Graphs",
   23 September 2026, 45 pages (repository openai/math at commit 1581d4cb,
   `preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/main.pdf`;
   not on arXiv).
2. Chenghua Liu and Boning Meng, "A simplified proof of the FPRAS for counting perfect matchings",
   arXiv 2610.26803 (19 October 2026), 20 pages. "We give a simplified, self-contained proof of OpenAI's FPRAS for
   counting perfect matchings in general graphs." It keeps the architecture of the original and replaces the proof
   of the central inequality (no auxiliary vertices, no tree constructions).

Theorem (Liu–Meng 1.1). There is a randomized algorithm which, given a graph G on n vertices, ε in (0,1) and δ in
(0,1), returns within time polynomial in n, 1/ε and log(1/δ) a number within a factor 1 ± ε of the number of perfect
matchings of G, with probability at least 1 − δ.

Before 2026: Jerrum–Sinclair (1989) handle graphs whose near-perfect matchings outnumber perfect matchings by at most a
polynomial factor; Jerrum–Sinclair–Vigoda (2004) the bipartite case; Štefankovič–Vigoda–Wilmes (arXiv 1712.07504) show
the standard chains mix slowly on some non-bipartite graphs.

The numbering below is that of Liu–Meng, which is the version checked.

## Architecture

- Weights (activities) on the edges of K_n; anneal from all weights 1 (nonedges of G included) to nonedges weighted
  b^{−J}, b = 1 + 1/n, in J_out = O(n(n log n + log 1/ε)) stages.
- Completion. For activities λ, B_ij = max(1, best bottleneck of λ over paths from i to j) is an ultrametric with
  λ ≤ B, and μ = λ + B/D with D = 10^8 (n+1)^4 lies between B/D and (D+1)B/D.
- Theorem 2.1 (two matchings). If B ≤ a ≤ rB with B ultrametric, then for all functions f, g of a matching,
  Var_π(f) ≤ C_pair E(f(M_1) + g(M_2)) with C_pair = (10n)^80 r^9, where E is the Dirichlet form of the chain on
  pairs that performs a two-edge switch in M_1 (Metropolis) or exchanges M_1 and M_2 along one of the cycles of their
  symmetric difference.
- Replication (Lemma 3.1) turns this additive two-matching bound into a spectral gap for a chain on
  q = 32 C_pair matchings per level, T + 1 levels of capped activities; Theorem 3.2 is the sampler.
- Marking. Each edge of a sample from π_μ is called virtual with probability B_e/(D μ_e); the all-real samples
  have law π_λ, the samples with one virtual edge give the two-hole ratios, and a balance condition
  1/4 ≤ r_i(λ) ≤ 1 (r_i = max_j Z(−ij)/Z), restored after every stage by a dyadic vertex rescaling, keeps
  Z_μ/Z_λ ≤ e^{0.001}.

## What was verified by hand

Sections 3, 4 and 5 and the assembly at the end of Section 2.4, every step.

- Section 3.1: capped activities min{c^t, D a_e}, c = 1 + 1/n; capping keeps the ultrametric inequality and the
  comparison with r = D + 1; adjacent levels have density ratio in [1/2, 2]; T ≤ 1 + 2n log(2D·4^Q).
- Lemma 3.1 (replication): the martingale increments h_x, the interaction parts r_xy, the identity
  r_xy = E[h_y | U_x, ξ_x, ξ_y] − E[h_y | U_x, ξ_y], the bound Σ_{x<y} ‖r_xy‖² ≤ ‖h_y‖², and the resulting
  (1 − 4C/q) Var ≤ (2C/q) ΣΣ E_xy + Σ E_i. With q = 16C this gives Var ≤ (8J/3) E and gap ≥ 3/(8J),
  J = Tq² + q. The passage from equal levels to adjacent levels costs the factor 2 as stated.
- Lemma 4.1: the path-exchange inequality (4.4), its special case (4.2), edge insertion (4.5), and the walk along a
  heavy path that gives g(U) ≤ 10^5 n / B_ij ((4.6), (4.7); the brackets are at most 96 and 8, and
  4[6144(n − 2) + 32] ≤ 10^5 n).
- Lemma 4.2: the two derivative formulas, the bound C(n,2)·10^5 n / D ≤ 10^{−3}, and the continuity argument that
  keeps every r_i in (1/8, 4) along the interpolation.
- Marked law (4.9), Theorem 4.3, the three means (5.4), the consequences (5.3) of one outer step, the error bounds
  (5.7) and (5.8), Lemma 5.1 (the dyadic pass: feasibility, m_i ≤ v_i < 2m_i, final multipliers at least 1/16, and
  1/2 − 512α = 3/8), and Section 5.3 (bias σ/2, Hoeffding, union bound, product of the ratios, the nonedge
  remainder n^{n/2} b^{−J_out} ≤ ε/32).
- End of Section 2.4: T_enc = 80 n^7 (1 + n²)^18 < (10n)^60, q* = 1/(30n²) is below the switch rate
  1/(6·C(n/2,2)), W < 4n, and 60 n³ T_enc r^9 ≤ C_pair.

No error was found in these parts.

## What was not verified

- The proof of Theorem 2.1 (Sections 2.2–2.4: threshold clusters, isolation of a discrepancy cycle, dissection into
  cells and polygon holes, the weight comparisons (2.17)–(2.19), and the encoding that bounds the congestion). It was
  read; the telescoping identities (2.12)–(2.14) and the count (2.15)–(2.16) were followed; the cell comparisons and
  the claim that the seven vertex slots, the flags and the two edit lists recover an occurrence were not checked case
  by case. This is the part on which the whole result rests.
- Appendix A (finite precision) was read, not checked.
- The original 45-page proof was read only through the start of its Section 2.3.
- No formalization of this theorem was found in `lean/formalization.yaml` of openai/math.

## Computer tests (`t189_check.py`, `t189_check.out`)

Brute force over all perfect matchings of K_4, K_6, K_8; floating point.

| statement | result |
| --- | --- |
| (4.2), 360 activity matrices, all 4-subsets | largest lhs/rhs − 1 = 2e-16 (an identity for n = 4) |
| (4.4), random hole sets; (4.5) | largest lhs/rhs − 1 = 4e-16; 2e-16 |
| (4.3) on 290 balanced instances, weights spread over up to 12 decades | largest g(U) B_ij / n: 0.284 (two holes), 0.162 (four holes); the lemma allows 10^5 |
| Lemma 4.2 on the same instances | largest Z_μ/Z_λ − 1 = 6e-11 |
| (2.2): 2 Var(f) ≤ S(f), 30 weights each for n = 6, 8 | largest 2Var/S − 1 = 6e-13 (rounding; the two sides nearly agree when one matching carries almost all the weight) |

Theorem 2.1 itself: the constant (10n)^80 r^9 is out of reach of any experiment, so the script computes the best
constant, λ* = inf over f, g of E(f + g)/Var(f), exactly (the minimum over g is a Schur complement, then the least
eigenvalue on the complement of the constants), for ultrametrics with two levels t^0, t^1 or more, and lets the
spread t grow.

| weights | n = 6, t = 1, 10, 10², 10⁴, 10⁶ | n = 8 |
| --- | --- | --- |
| ultrametric, blocks 3+3 / 4+4 | 0.278 0.168 0.167 0.167 0.167 | 0.194 0.030 0.028 0.028 0.028 |
| ultrametric, 2+2+2 / 3+3+2 | 0.278 0.050 0.055 0.056 0.056 | 0.194 0.035 0.028 0.028 0.028 |
| ultrametric, fully nested | 0.278 0.066 0.057 0.056 0.056 | 0.194 0.033 0.028 0.028 0.028 |
| same with a = Bχ, χ uniform in [1,4] | between 0.050 and 0.174 | between 0.026 and 0.101 |
| heavy chordless 6-cycle, chords 1 (t = 1, 10, 10², 10³, 10⁴) | 0.278 0.018 1.7e-3 1.7e-4 1.7e-5 | 0.194 0.021 2.0e-3 1.9e-4 1.9e-5 |

So for weights comparable to an ultrametric the best constant stays bounded as the spread goes to infinity, as
Theorem 2.1 says, and for a weight that is not (a cycle of heavy edges whose chords are light, r = t) it decays like
1/t, which is allowed by the factor r^9 and shows that the hypothesis is used. In most of the ultrametric families
the limit equals the rate of a single two-edge switch, 1/18 for n = 6 and 1/36 for n = 8, that is 1/(6·C(n/2,2)).

## Reception

arXiv searches of 12 Nov 2026 (`lit/search/s1.xml`, `s2.xml`): the Liu–Meng paper is the only follow-up found; no
paper disputes the result. Liu–Meng reprove the central inequality by a different construction and reuse OpenAI's
replication, completion and marked annealing with attribution.

## For the list

Take T189 off the problems to attack: an FPRAS exists (OpenAI, 23 Sep 2026; independent simplified proof by Liu and
Meng). Record the level of the check as partial: the reductions around Theorem 2.1 are verified, Theorem 2.1 is tested
on small cases and its proof read.

Open next to it:
- a practical running time. The gap is 3/(8J) with J of order T q², q = 32 (10n)^80 (D+1)^9, D = 10^8 (n+1)^4;
- the true order of the two-matching constant. On K_6 and K_8 it is about the inverse switch rate, of order n²;
  a polynomial of small degree in n and r in Theorem 2.1 would be a real improvement;
- a deterministic approximation scheme for perfect matchings, or for the permanent;
- which weights admit the inequality: comparability to an ultrametric is sufficient; the heavy-cycle example shows
  the constant must depend on r.

Reusable: Lemma 3.1 (an additive two-coordinate Poincaré inequality plus enough independent guide coordinates gives a
gap for all functions), the completion λ + B/D by the bottleneck ultrametric, and marking a sample to read several
partition-function ratios from one batch.
