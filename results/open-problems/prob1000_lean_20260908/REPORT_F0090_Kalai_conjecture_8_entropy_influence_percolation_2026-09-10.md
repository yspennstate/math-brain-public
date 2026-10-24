# The spectral entropy of the percolation crossing event is bounded by its total influence

Problem F0090 of the intake-F ledger. Source: G. Kalai, *Three puzzles on mathematics, computation, and games*, Proc. ICM 2018 (arXiv:1801.02602), Section 3.3.2, Conjecture 8: "Let f represent the crossing event in planar percolation. Show that H(S(f)) = O(I(f)) and H(P(f)) = O(I(f))." The same question is open problem 1 in the list closing Garban, Pete and Schramm, *The Fourier spectrum of critical percolation*, Acta Math. 205 (2010), arXiv:0803.3750, Section 11: "As was pointed out to us by Gil Kalai, it is natural to test the conjecture in the setting of percolation: if f_R is the +-1 indicator function of the left-right crossing in the square [0,R]^2, is it true that Ent(f_R) = O(R^2 alpha_4(R))?"

Written 2026-09-10 by the Claude agent claude-prob1000-0910. Status: author-checked argument; a first independent read by the Codex agent codex-probability-publishability-20260910 (same day, 13:45-14:04Z) found the inputs (GPS Lemma 3.2, (2.6)) and the square quadtree scale-sum mechanism sound, no defect in the square theorem, and two corrections to the commentary that are incorporated below (the majority aside; the o(1) in the triangular-lattice exponent). It also recommends keeping the theorem to squares, which this memo does. Novelty is not certified. Every input is a stated result of the GPS paper or of the standard planar-percolation toolkit (Kesten 1987, Nolin 2008); the new step is a hierarchical coding bound on the entropy of a random subset of the plane, which turns the question into a sum of one-box hitting probabilities that GPS already control.

## Statement

Fix critical bond percolation on Z^2 or critical site percolation on the triangular lattice. Let f_R be the +-1 indicator of a left-right crossing of the square Q_R = [0,R]^2, let S = S_{f_R} be its spectral sample (the random subset of bits with P[S = A] = hat f_R(A)^2), and let P = P_{f_R} be the random set of pivotal bits. Write Ent(f_R) = H(S) = sum_A hat f_R(A)^2 log(1/hat f_R(A)^2) and I(f_R) = sum_x Inf_x(f_R) = E|S| = E|P|.

**Theorem.** There is a constant C, depending only on the lattice, such that for every R >= 2

    H(S_{f_R}) <= C I(f_R)   and   H(P_{f_R}) <= C I(f_R).

In particular Ent(f_R) = O(R^2 alpha_4(R)), which answers GPS's open problem 1 and both halves of Kalai's Conjecture 8 for the square. The argument is not specific to the square: it works for any fixed quad Q in place of [0,R]^2 with the same inputs (see the remark at the end).

## Notation and the three inputs

Tile the plane by the bits (edges of Z^2, or hexagons of the triangular lattice). For 1 <= r <= R let alpha_4(r,R) be the probability of four alternating arms from radius r to radius R, alpha_3^+(r,R) the probability of three arms (two of one colour, one of the other) from radius r to radius R inside a half-plane, and for a set of bits B inside Q_R let alpha_box(B,Q_R) be the probability of the event Lambda_B that there are four alternating arms from B to the four sides of the square (open arms to the left and right sides, closed arms to the top and bottom). We use three standard facts.

(I1) *GPS Lemma 3.2, inequality (3.4).* For every union of tiles B meeting Q_R in a nonempty connected set, P[S cap B != emptyset] <= 4 alpha_box(B,Q_R). The proof is one line once one sees that P[S cap B != emptyset] = E[Var(f_R | bits outside B)], which vanishes unless the outside configuration leaves f_R undetermined, and an outside configuration that leaves f_R undetermined must carry the four arms of Lambda_B. The same argument, with no constant, gives P[P cap B != emptyset] <= alpha_box(B,Q_R): a pivotal bit in B has an open crossing and a closed dual crossing through it, and their parts outside B are the four arms. Also, by (3.6) of the same lemma, P[x in S] = P[x in P] = alpha_box(x,Q_R) for a single bit x.

(I2) *Quasi-multiplicativity and the polynomial lower bound, GPS (2.6).* There are constants c, C, epsilon > 0 with c alpha_4(r,s) alpha_4(s,R) <= alpha_4(r,R) for r <= s <= R, and C^{-1} (r/R)^{2-epsilon} <= alpha_4(r,R) for all 1 <= r <= R. GPS derive the lower bound from alpha_5(r,R) asymptotically (r/R)^2, the RSW bound alpha_1(r,R) <= O(1)(r/R)^epsilon, and Reimer's inequality alpha_1 alpha_4 >= alpha_5. On the triangular lattice alpha_4(r,R) = (r/R)^{5/4+o(1)} and the lower bound holds with any epsilon < 3/4.

(I3) *The half-plane three-arm bound.* alpha_3^+(r,R) <= C (r/R)^2 for all 1 <= r <= R (Nolin, *Near-critical percolation in two dimensions*, EJP 2008, the universal half-plane exponent; also GPS's appendix). Only the weaker two-arm bound alpha_2^+(r,R) <= C r/R is actually needed, at the cost of a logarithm that the sum absorbs; see the remark after Step 2.

Finally, the lower bound I(f_R) >= c R^2 alpha_4(1,R) is the standard first-moment estimate for the pivotal set (GPS, Section 3, E|S| = E|P| asymptotically R^2 alpha_4(R)): a bit in the middle square [R/4, 3R/4]^2 has alpha_box(x,Q_R) >= c alpha_4(1,R) by RSW gluing of the four arms to the four sides, and there are of order R^2 such bits.

## Step 1: a coding bound for the entropy of a random set in the plane

Let A be a random subset of the bits of Q_R (either S or P). Choose K with 2^K >= 2R and cover Q_R by the dyadic squares of side 2^k, k = 0, ..., K, nested in the usual quadtree. For a scale r = 2^k let A_r be the set of dyadic squares of side r that meet A (GPS's S_r). We describe A by the following prefix-free code, read from the coarsest scale down: one bit saying whether A is empty; then, for each k = K, K-1, ..., 1 and for each square of side 2^k in A_{2^k}, taken in a fixed order, four bits saying which of its four children of side 2^{k-1} meet A. At the finest scale 2^0 = 1 each square contains a bounded number of bits (one edge or hexagon, or a bounded number if the tiling is coarser than the dyadic grid), so a further bounded number of bits per hit unit square identifies A exactly. The decoder always knows how many bits to read next, so the code is uniquely decodable, and by Shannon's source coding theorem the entropy of A is at most the expected code length:

    H(A) <= 1 + 4 sum_{k=1}^{K} E|A_{2^k}| + C_0 E|A_1|.                       (1)

Since |A_1| <= |A| and E|A| = I(f_R) for both A = S and A = P, the last term is C_0 I(f_R). Everything therefore rests on the coarser scales.

The point of (1) is that it is a hierarchical version of the entropy-influence inequality: the finest scale contributes exactly a multiple of E|A| = I(f), and the conjecture holds for every Boolean function whose spectral sample hits the coarser dyadic squares no more often, in total, than it hits the finest ones. For critical percolation that is the statement that the spectral sample is a fractal of dimension strictly less than 2, which is exactly what (I2) says.

## Step 2: the one-scale sum

Fix a scale r = 2^k with 2 <= r <= R (squares of side larger than R are one square and contribute at most 4 each, at most 4K = O(log R) in all). By (I1),

    E|A_r| = sum_{B: side r} P[A cap B != emptyset] <= 4 sum_{B} alpha_box(B,Q_R).      (2)

We bound the sum on the right by C (R/r)^2 alpha_4(r,R) + C log R. Classify a square B of side r by d = dist(B, boundary of Q_R) and by D = the distance from B to the second nearest side of the square (so d <= D, and D is of order R for all but the squares near a corner). For d >= 2r and D >= 8d the event Lambda_B forces (a) four alternating arms from B to radius d/2 around B, an event of the disc of radius d/2, which lies inside Q_R, and (b) three arms of alternating colours from radius 2d to radius D/2 around B, inside the half-plane bounded by the line of the nearest side: the three arms of Lambda_B that end on the three farther sides each start on B and end at distance at least D, so each crosses the half-annulus. The two events live on disjoint sets of bits, hence are independent, and by (I3)

    alpha_box(B,Q_R) <= alpha_4(r, d/2) alpha_3^+(2d, D/2) <= C alpha_4(r,d) (d/D)^2.        (3)

If d < 2r drop the first factor (it is at most 1); if D < 8d drop the second. The number of squares of side r with d and D in given dyadic ranges [d, 2d) x [D, 2D) is at most C (d/r)(D/r): their centres lie in a strip of width about d along one side, within distance about D of one of that side's ends. Summing (3) over the dyadic classes,

    sum_B alpha_box(B,Q_R) <= C sum_{d} sum_{D >= d} (dD/r^2) alpha_4(r,d) (d/D)^2 + (boundary terms)
                           <= C sum_{d} (d^2/r^2) alpha_4(r,d) sum_{D >= d} (d/D)
                           <= C sum_{d} (d^2/r^2) alpha_4(r,d),

the D-sum being geometric. By (I2), alpha_4(r,d) <= C alpha_4(r,R)/alpha_4(d,R) <= C alpha_4(r,R) (R/d)^{2-epsilon}, so the d-sum is at most C alpha_4(r,R) (R^{2-epsilon}/r^2) sum_d d^{epsilon} <= C alpha_4(r,R) R^2/r^2, again geometric and dominated by d of order R. The boundary terms are the classes with d < 2r, for which alpha_box(B,Q_R) <= alpha_3^+(2r, D/2) <= C (r/D)^2 and the count is at most C D/r, giving sum_D C r/D <= C; and the classes with D < 8d, whose count is at most C (d/r)^2 with the bound C alpha_4(r,d) each, giving C sum_d (d^2/r^2) alpha_4(r,d), which is the sum already handled. Altogether

    E|A_r| <= C (R/r)^2 alpha_4(r,R) + C.                                              (4)

Remark. With only the half-plane two-arm bound alpha_2^+(2d, D/2) <= C d/D in place of (I3), the D-sum becomes sum_{D >= d} 1 <= log_2(R/d) and the d-sum is sum_d (d/R)^{epsilon} log_2(R/d), still bounded; the boundary classes then contribute C log R per scale, and C log^2 R in all, which is o(R^2 alpha_4(1,R)) by (I2). So (4) survives with a log R in place of the constant, and the theorem is unchanged.

## Step 3: the sum over scales

By (I2) again, (R/r)^2 alpha_4(r,R) <= C R^2 alpha_4(1,R) / (r^2 alpha_4(1,r)) <= C R^2 alpha_4(1,R) r^{-epsilon}. Inserting (4) into (1) and summing over r = 2^k,

    H(A) <= 1 + C R^2 alpha_4(1,R) sum_{k >= 1} 2^{-epsilon k} + C K + C_0 I(f_R)
         <= C' R^2 alpha_4(1,R) + C' log R + C_0 I(f_R).

Since I(f_R) >= c R^2 alpha_4(1,R) >= c R^{epsilon} by (I2), the logarithm is absorbed and H(A) <= C I(f_R) for both A = S and A = P. On the triangular lattice the scale-r term is (R/r)^{3/4+o(1)}, so the coding bound is dominated by the finest scale and gives H(S) = O(R^2 alpha_4(R)) = R^{3/4+o(1)}, as expected for a random fractal of dimension 3/4 with R^{3/4+o(1)} points. (The o(1) cannot be dropped from the exponent: GPS (2.5) gives alpha_4(R) = R^{-5/4+o(1)}, not a pure power with a bounded prefactor; the theorem itself is stated with alpha_4 and needs no such prefactor. Pointed out by the same independent reader.)

## What is and is not new

The identity P[S cap B != emptyset] = E[Var(f | outside B)] and its four-arm bound are GPS's Lemma 3.2, and GPS's Section 4 already works with the sets S_r of hit r-squares; (I2) and (I3) are quoted from the same paper. What the two 2010 and 2018 sources leave open is the entropy itself, and the argument above shows the entropy is controlled once one encodes the spectral sample scale by scale: the expected code length is the sum of the first-moment quantities E|S_r| over scales, and the polynomial lower bound alpha_4(r,R) >= (r/R)^{2-epsilon} makes that sum a geometric series dominated by its finest term, which is I(f). No second-moment or clustering information about S is used, which is why the argument does not see the difference between S and P. (An earlier draft of this paragraph illustrated the failure of H(P) = O(I) with the majority; the independent reader, the Codex agent codex-probability-publishability-20260910, pointed out on 2026-09-10 that with P the set of pivotal variables this is wrong: for n = 2m - 1 the pivotal set of the majority is empty unless the sum is +-1, and then it is the m bits of the majority sign, so with q = 2 C(n,m) 2^{-n} one has H(P) = h(q) + q log C(n,m) and I = q m, whose ratio tends to 2 log 2; they checked n = 3, 5, 7, 9 by enumeration. The clean general counterexample is OR_n: the n singleton pivotal sets and the full set each have mass 2^{-n}, so H(P)/I ~ (n/2) log 2. Kalai's parenthetical about the majority presumably refers to a different normalisation of the pivotality distribution.)

The bound is not the Friedgut-Kalai conjecture for a new abstract class of functions; it is the conjecture for the crossing event, obtained from the geometry of critical percolation. What it does show in general is that the entropy-influence inequality holds for any Boolean function on a two-dimensional array of bits whose spectral sample satisfies sum_{r = 2^k, k >= 1} E|S_r| = O(E|S|), and that condition is a first-moment statement.

Remark on general quads. For a fixed quad Q scaled by R, (I1) is stated by GPS for quads, and the boundary analysis of Step 2 goes through with the half-plane three-arm estimate replaced by the corresponding arm bound in the smooth-boundary or piecewise-smooth domain, with constants depending on Q; the geometric sums are unchanged. I have checked only the square in detail.

## Prior-art check (2026-09-10)

Searched for a published resolution: the FEI literature since 2010 (O'Donnell, Wright, Zhou 2011; Keller, Mossel, Schlank 2011, arXiv:1105.2651; Chakraborty et al.; Wan et al. on read-k decision trees; Shalev 2018, arXiv:1806.03646; the Combinatorica 2024 bound Ent(f) <= O(I(f) + sum_k I_k(f) log(1/I_k(f))), arXiv:2312.08271; the June 2026 note arXiv:2606.00246 on stopping binary trees and delta-tribes) covers symmetric, read-k, extremal-influence, extremal-entropy, tribes-type and semi-separated classes, and none mentions percolation or a geometric spectral sample. For the crossing event the 2024 bound gives only Ent(f_R) = O(I(f_R) log R), since every bulk bit has influence of order alpha_4(1,R) = R^{-5/4+o(1)}, which is the trivial bound. The Garban-Steif lecture notes (arXiv:1102.5761) use the word entropy only for the entropy-versus-clustering heuristic. I found no paper stating Ent(f_R) = O(R^2 alpha_4(R)). Citation check (Semantic Scholar graph API, 2026-09-10, 16:3x local): of the 116 papers it lists as citing GPS 2010 and the 13 citing Kalai 2018, ten mention entropy in title or abstract, and all are either general FEI papers (Chakraborty et al. 2015, Upper bounds on Fourier entropy; arXiv:2308.00509; arXiv:2312.08271), Brascamp-Lieb or hypercontractivity papers, the sparse-reconstruction papers of Galicza and Pete, one-arm bounds for dependent percolation, or entropy noise sensitivity of random walks on groups (arXiv:1901.03617); none states the percolation case. Semantic Scholar's citation coverage is incomplete, so this is evidence, not proof, of novelty.

## Exact small-box control (computed 2026-09-10, `prob1000_lean_20260908/f0090_small_box_check.py`)

Critical bond percolation on m x m sites, the exact spectrum by a Walsh-Hadamard transform over all 2^E configurations, and the quantities of Step 1 computed as defined there (the conditional-variance identity checked against the direct Fourier sum for one square):

    m = 2 (4 edges):  H(S) = 2.000 bits, I(f) = 1.000, E|S_1| = 1.000, E|S_2| = 0.750, coding bound 6.00
    m = 3 (12 edges): H(S) = 5.331 bits, I(f) = 1.719, E|S_1| = 1.633, E|S_2| = 1.154, coding bound 8.88

The inequality H(S) <= 1 + 4 sum_{r>=2} E|S_r| + 2 E|S_1| holds in both cases, as Shannon's theorem says it must; this is a control on the definitions, not evidence for the asymptotic statement, whose content is the geometric decay of E|S_r| in r that only appears for R large. m = 4 (24 edges) was not run in the session.

## Monte Carlo control of the scale sum on the pivotal set (measured 2026-09-10, `f0090_pivotal_scale_sum_mc.py`)

The pivotal set is sampled exactly (an edge is pivotal iff its endpoints join the left and right sides in the open graph and its dual endpoints join the top and bottom in the closed dual graph; the rule was checked against brute-force flipping on every configuration of the 3 x 3 square, 49,152 edge cases, zero mismatches). Critical bond percolation on Z^2, R x R sites, E|P_r| / E|P| by dyadic scale r:

    R     samples  E|P|     r=2    r=4    r=8    r=16   r=32   r=64   r=128  sum_{r>=2} / E|P|
    16    4000     7.62     0.575  0.356  0.211  0.107                              1.249
    32    4000     12.78    0.575  0.358  0.217  0.125  0.064                       1.338
    64    2000     22.14    0.569  0.355  0.213  0.127  0.073  0.037                1.374
    128   1000     37.81    0.571  0.355  0.214  0.127  0.074  0.042  0.021         1.405
    256   400      62.64    0.575  0.356  0.216  0.130  0.077  0.046  0.026         1.439

Each column is stable in R and decays like r^{-0.74}, i.e. E|P_r| is of order E|P| r^{-3/4}, which is (R/r)^2 alpha_4(r,R) with the 5/4 four-arm exponent (the growth of E|P| itself, x1.68 per doubling, is R^{0.75}). The scale sum ratio rises slowly towards sum_k 2^{-3k/4} = 1.46. This is the geometric decay that Step 3 needs, seen directly on Z^2; since E|S_r| <= 4 alpha_box(B) and E|P_r| <= alpha_box(B) are the same box sums, it is the relevant control for the spectral sample as well, though the spectral sample itself was not sampled.

## Checks made on this argument

1. The identity P[S cap B != emptyset] = E[Var(f | bits outside B)]: from E[f | outside B] = sum_{A subset of B^c} hat f(A) chi_A, so f - E[f | outside B] = sum_{A cap B != emptyset} hat f(A) chi_A, whose squared norm is P[S cap B != emptyset] by Parseval and E[(f - E[f|G])^2] = E[Var(f|G)] on the other side.
2. The dyadic code is uniquely decodable: the number of bits read at scale 2^{k-1} is four times the number of hit squares at scale 2^k, which the decoder has just reconstructed; termination is at the fixed finest scale.
3. The triangular-lattice numbers: scale-r term (R/r)^2 (r/R)^{5/4} = (R/r)^{3/4}; sum over dyadic r of order R^{3/4}; I(f_R) of order R^{3/4}. Consistent.
4. The exponent condition: the scale sum converges if and only if r^2 alpha_4(1,r) grows polynomially, which is GPS (2.6) on Z^2 and the 5/4 exponent on the triangular lattice; with the 5-arm bound alone (exponent exactly 2) the sum would give only the trivial O(I log R).
5. Independence in (3): the disc of radius d/2 around B and the half-annulus from radius 2d to D/2 are disjoint, and both lie in Q_R because d is the distance to the boundary and D/2 <= the distance to the second nearest side.
