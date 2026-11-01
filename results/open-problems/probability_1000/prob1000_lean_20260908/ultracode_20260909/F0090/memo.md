# F0090 - Kalai's Conjecture 8: entropy of the spectral and pivotal samples of the crossing event

Written 2026-09-09. Source: G. Kalai, Three puzzles on mathematics, computation, and games, ICM 2018 (arXiv 1801.02602), Conjecture 8, Section 3.3.2, p. 22.

## 1. The problem as the source states it

Verbatim from p. 21-22 (the typo "H(S)(f))" is in the source):

> 3.3.2. Spectral distribution and Pivotal distribution. Let f be a monotone Boolean function with n variables. We can associate to f two important probability distributions on subsets of {1, 2, ..., n}. The spectral distribution of f, S(f) gives a set S a probability f-hat^2(S). Given x in Omega_n the i-th variable is pivotal if when we flip the value of x_i the value of f is flipped as well. The pivotality distribution P(f) gives a set S the probability that S is the set of pivotal variables. It is known that the first two moments of S and P agree.
>
> Conjecture 8. Let f represents the crossing event in planar percolation. Show that H(S)(f)) = O(I(f)) and H(P(f)) = O(I(f)). (Here H is the entropy function.)
>
> The first inequality is a special case of the entropy-influence conjecture of Friedgut and Kalai (1996) that applies to general Boolean functions. The second inequality is not so general (it fails for the majority).

The crossing event is defined on p. 21: "an n by n square grid and ... the event, when every edge is chosen with probability 1/2, that there is a path crossing from the left side to the right side of the square." I(f) is the total influence, I(f) = sum_i Inf_i(f) = E|P(f)| = E|S(f)| (for the +-1 valued f). Both inequalities ask for an upper bound on an entropy by a constant times I(f); the constant must not depend on n.

The same question (the spectral half) is Open Problem 1 in Section 11 of Garban, Pete and Schramm, The Fourier spectrum of critical percolation, Acta Math. 205 (2010): "As was pointed out to us by Gil Kalai, it is natural to test the conjecture in the setting of percolation: if f_R is the +-1 indicator function of the left-right crossing in the square [0,R]^2, is it true that Ent(f_R) = O(R^2 alpha_4(R))?"

The ledger row quotes the statement correctly.

## 2. Finding

Both inequalities hold. Write R for the side of the square (Kalai's n), alpha_4(r,R) for the alternating four-arm probability between radii r and R, alpha_4(R) = alpha_4(O(1),R).

Theorem. Let f_R be the left-right crossing event of the R x R square for critical site percolation on the triangular lattice or critical bond percolation on Z^2, S its spectral sample and P its pivotal set. There is a constant C (depending only on the lattice) such that for all R

    H(S) <= C R^2 alpha_4(R) <= C' I(f_R)   and   H(P) <= C R^2 alpha_4(R) <= C' I(f_R).

On the triangular lattice R^2 alpha_4(R) = R^{3/4+o(1)}. The proof uses only standard facts, all of which are stated with references in GPS Section 2 and Section 4.3: RSW, quasi-multiplicativity of arm events, the bounds C^{-1}(r/R)^{2-eps} <= alpha_4(r,R) <= C (r/R)^{1+eps} (GPS (2.6), on Z^2 from Kesten 1987 / BKS 1999 / Reimer; on the triangular lattice from the exponent 5/4), the half-plane three-arm estimate alpha_3^+(r,R) asymp (r/R)^2 (GPS (4.12), Werner's 2007 lecture notes), the quarter-plane bound alpha_2^{++}(r,R)^2 <= O(1) alpha_3^+(r,R)(r/R)^eps (GPS (4.13)), and the first-moment estimate E|S cap RU| asymp R^2 alpha_4(R) for U compactly inside the square (GPS Lemma 3.1 and (3.1)).

## 3. Proof

### 3.1 An entropy bound for any random subset of the square, by dyadic coding

Let T be any random subset of the sites (or edges) of the R x R box. Embed the box in the dyadic square [0, 2^K)^2 with 2^{K-1} < R <= 2^K. For 0 <= k <= K let the level-k boxes be the 4^k dyadic sub-squares of side r_k = 2^{K-k}, and let

    pattern_k(T) = the set of level-k boxes that intersect T,      N_k = |pattern_k(T)|.

Level-0 is the whole square, level-K boxes are single sites, so pattern_K(T) = T. Each pattern_k is a function of T, so by the chain rule

    H(T) = H(pattern_0, ..., pattern_K) = H(pattern_0) + sum_{k=0}^{K-1} H(pattern_{k+1} | pattern_0, ..., pattern_k)
         <= H(pattern_0) + sum_{k=0}^{K-1} H(pattern_{k+1} | pattern_k).

Given pattern_k = p, the next pattern is determined by choosing, for each of the N_k(p) occupied level-k boxes, which nonempty subset of its four children is occupied: at most 15^{N_k(p)} values, so H(pattern_{k+1} | pattern_k = p) <= N_k(p) log 15, and averaging over p,

    H(pattern_{k+1} | pattern_k) <= (log 15) E[N_k] = (log 15) sum_{B at level k} P(T cap B nonempty).

Since pattern_0 takes two values,

    (E)   H(T) <= log 2 + (log 15) sum_{k=0}^{K-1} sum_{B at level k} P(T cap B nonempty).

This holds for every random set T. (The count 15 and the geometric-sum step below are the parts certified in Lean, Section 5.)

### 3.2 The one-box marginals are bounded by the box-pivotality probability

For a set B of variables let Lambda_B be the event that B is pivotal for f as a set: there is a configuration agreeing with omega outside B on which f takes the other value (GPS's Lambda_B, Section 2.3).

Pivotal set: if some site of B is pivotal then B is pivotal as a set, so P(P cap B nonempty) <= P(Lambda_B).

Spectral sample (+-1 normalisation, so Q[S = .] = f-hat(.)^2 is a probability): E[f | F_A] = sum_{S subset A} f-hat(S) chi_S, hence Q[S subset B^c] = E[E[f|F_{B^c}]^2] and

    Q[S cap B nonempty] = E[f^2] - E[E[f|F_{B^c}]^2] = E[ Var(f | F_{B^c}) ].

On the complement of Lambda_B the conditional law of f given F_{B^c} is a point mass, so the conditional variance vanishes; on Lambda_B it is at most 1 since |f| = 1. Therefore

    Q[S cap B nonempty] <= P(Lambda_B).

(This is GPS Lemma 2.2 with W empty, up to their factor 4.) If one prefers the 0/1 indicator and normalises the spectral measure by 1/E f^2 = 2, the bound becomes P(Lambda_B)/2. Either way both random sets have one-box marginals at most P(Lambda_B), so by (E)

    (E')  max(H(S), H(P)) <= log 2 + (log 15) sum_{k=0}^{K-1} sum_{B at level k} P(Lambda_B).

Note the finest level of the sum, r = 1, is sum_x P(Lambda_{x}) = sum_x Inf_x(f) = I(f) exactly. The work is to show the coarser levels add only a constant multiple of it.

### 3.3 One scale of the box sum: sum_{B of side r} P(Lambda_B) <= C (R/r)^2 alpha_4(r,R)

Fix a level with box side r and let B be a box of side r with centre x. If Lambda_B occurs then (GPS, proof of (3.1) and Section 4.3): in the configuration outside B there are open paths from B to the left and right sides and closed (dual) paths from B to the top and bottom sides, i.e. the four-arm event from the boundary of B to the sides of the square, with GPS's convention that an arm to a side that B touches is present. Let d = dist(x, boundary of the square) be the distance to the nearest side L, y the projection of x onto L, and e = dist(y, nearest corner z of L). Three cases; in each, the arm events named live in disjoint regions and are therefore independent, and each factor is bounded by the standard estimates.

(a) d >= R/8 (bulk boxes). The four arms leave B(x, R/8), so P(Lambda_B) <= alpha_4(r, R/8) <= C alpha_4(r, R) by GPS (2.3). There are at most (R/r)^2 such boxes: contribution <= C (R/r)^2 alpha_4(r,R).

(b) d < R/8 and e >= R/4 (near a side, away from corners). Four arms cross the annulus B(x,d) \ B (with alpha_4(r,d) := 1 if d <= 2r), and, since B is contained in the boundary-centred box B(y, 3d) and Lambda_B implies Lambda_{B(y,3d)}, the three-arm event in the half-annulus (B(y, R/4) \ B(y, 3d)) cap square occurs (GPS Section 4.3, first paragraph, with r' = R/4). The regions are disjoint, so

    P(Lambda_B) <= alpha_4(r,d) alpha_3^+(3d, R/4) <= C alpha_4(r,d) (d/R)^2       by (4.12)
               <= C alpha_4(r,R) (R/d)^{2-eps'} (d/R)^2 = C alpha_4(r,R) (d/R)^{eps'}   by quasi-multiplicativity and the left side of (2.6).

The number of such boxes with d in [2^j, 2^{j+1}) is at most C (R/r)(2^j/r), so their contribution is at most C (R/r)^2 alpha_4(r,R) sum_j (2^j/R)^{1+eps'} <= C (R/r)^2 alpha_4(r,R).

(c) d < R/8 and e < R/4 (near a corner), with d <= e. Three disjoint regions: the annulus B(x,d) \ B (four arms), the half-annulus (B(y, e/2) \ B(y, 3d)) cap square (three arms; take the factor to be 1 when e < 6d), and the quarter-annulus (B(z, R/2) \ B(z, 2e)) cap square (two arms, by the corner statement in GPS Section 4.3, since B is inside B(z, 2e)). So

    P(Lambda_B) <= alpha_4(r,d) alpha_3^+(3d, e/2) alpha_2^{++}(2e, R/2)
               <= C alpha_4(r,R) (R/d)^{2-eps'} (d/e)^2 (e/R)^{1+eps/2}        by quasi-multiplicativity, (2.6) left, (4.12), (4.13).

The number of boxes with d in [2^i, 2^{i+1}) and e in [2^j, 2^{j+1}) is at most C (2^i/r)(2^j/r) = C (R/r)^2 (d e / R^2) with d = 2^i, e = 2^j. Count times bound:

    C (R/r)^2 alpha_4(r,R) * (d e / R^2) (R/d)^{2-eps'} (d/e)^2 (e/R)^{1+eps/2}
      = C (R/r)^2 alpha_4(r,R) * d^{1+eps'} e^{eps/2} R^{-1-eps'-eps/2}
      = C (R/r)^2 alpha_4(r,R) * (d/R)^{1+eps'} (e/R)^{eps/2}.

Summing over dyadic d <= e gives C (R/r)^2 alpha_4(r,R) (e/R)^{1+eps'+eps/2}, and summing over dyadic e <= R/4 gives C (R/r)^2 alpha_4(r,R). When e < 6d the half-annulus factor is replaced by 1; then e is within a constant of d, the count-times-bound is C (R/r)^2 alpha_4(r,R) (d e / R^2)(R/d)^{2-eps'}(e/R)^{1+eps/2} = C (R/r)^2 alpha_4(r,R) (d/R)^{1+eps'+eps/2} up to constants, and there are boundedly many such (d, e) pairs per d, so this part is also summable. Contribution <= C (R/r)^2 alpha_4(r,R).

All three cases together:

    (S)   sum_{B of side r} P(Lambda_B) <= C (R/r)^2 alpha_4(r,R)     for every 1 <= r <= R.

### 3.4 Summing over scales

By quasi-multiplicativity (GPS (2.2)), alpha_4(r) alpha_4(r,R) <= C alpha_4(R), and by the left side of (2.6), r^2 alpha_4(r) >= c r^{eps'}. Hence (Lean lemma scale_term_bound)

    (R/r)^2 alpha_4(r,R) <= C R^2 alpha_4(R) / (r^2 alpha_4(r)) <= C R^2 alpha_4(R) r^{-eps'}.

With r = r_k = 2^{K-k} the right side is geometric in k, and sum_k 2^{-(K-k) eps'} <= 1/(1 - 2^{-eps'}) (Lean lemma geom_tail). So

    sum_{k=0}^{K-1} sum_{B at level k} P(Lambda_B) <= C R^2 alpha_4(R).

By (E') this gives H(S), H(P) <= log 2 + C R^2 alpha_4(R).

### 3.5 Comparison with I(f)

I(f) = E|S| = E|P| >= E|S cap RU| >= c R^2 alpha_4(R) for a fixed sub-square U compactly inside the unit square (GPS (3.1) and Lemma 3.1: every site of RU is pivotal with probability asymp alpha_4(R)). Also I(f) >= c R^{eps'} -> infinity by (2.6), which absorbs the additive log 2. Hence

    H(S) <= C' I(f),   H(P) <= C' I(f).

Both inequalities of Conjecture 8 hold, on the triangular lattice and on Z^2, with constants depending only on the lattice. On the triangular lattice the bound reads H(S), H(P) <= C R^{3/4+o(1)}, and the level sum is dominated by the finest scale: level k contributes about (R/r_k)^{3/4}.

## 4. What is not done

- I did not attempt a matching lower bound H(S) >= c I(f) (not asked). The second-moment bounds in GPS make it plausible.
- The argument is written for the square; the same steps work for any quad by GPS Section 7.4-type boundary control, but I did not check the corner analysis for a general quad.
- The percolation inputs are cited, not re-proved: RSW, quasi-multiplicativity, (2.6), (4.12), (4.13), (3.1) of GPS. On Z^2 the exponent inputs are the classical ones (Kesten 1987, BKS 1999, Reimer 2000, Werner 2007); the proof never needs the exact value of the four-arm exponent, only that it lies strictly between 1 and 2 and the half-plane three-arm exponent equals 2.
- Kalai's remark that the second inequality "fails for the majority" does not match the literal definitions: for majority on an odd number of variables the pivotal set is either empty or everything, so H(P) = h(c/sqrt(n)) -> 0 while I(f) = c sqrt(n). I read his remark as pointing at a different failure (that H(P) and I(f) need not be comparable in general); it does not affect the crossing-event statement.

## 5. Checks

1. Exact enumeration (check_entropy_bound.py): site percolation crossings on 2x2, 2x3, 3x3, 3x4, 4x4 grids, all 2^{nm} configurations, full Walsh transform. Verified to machine precision: the identity Q[S cap B nonempty] = E Var(f | F_{B^c}) for every box of the dyadic-style tree; Q[S cap B nonempty] <= P(Lambda_B) and P(P cap B nonempty) <= P(Lambda_B) for every box (equality for single sites, as it must be since both equal Inf_i); and the entropy bound (E) for both S and P. Output: e.g. 4x4: I(f) = 2.1685, H(S) = 5.43 <= 13.06, H(P) = 4.66 <= 12.46.

2. Direct simulation of the object (pivotal_box_scales.py): critical site percolation on the triangular lattice, R = 32, 64, 128, 256, pivotal sites computed exactly per sample (a site is pivotal iff its open-neighbour clusters reach both left and right and its closed-neighbour clusters reach both top and bottom), then N_r = number of r-boxes containing a pivotal site at each dyadic r. The claim behind (S) and Section 3.4 is sum_{r<R} E N_r <= C I(f) with the sum dominated by r = 1. Measured ratios sum_r E N_r / I(f): 2.56, 2.66, 2.70, 2.76 for R = 32, 64, 128, 256 (prediction about 2.47 if E N_r were exactly c (R/r)^{3/4}; the per-scale log2 ratios are 0.54-0.8, below 3/4 at the smallest r because of lattice effects, which raises the constant a little but keeps it bounded). This is a check of the scale-sum claim by a different route (counting pivotal boxes on real samples, no arm-exponent arithmetic), not a proof.

3. Lean 4 (U_F0090.lean, Mathlib): the three elementary steps that carry the arithmetic - 15 nonempty child patterns of a 4-child box; the one-scale inequality (R/r)^2 a4(r,R) <= C R^2 a4(R)/g from a4(r) a4(r,R) <= C a4(R) and g <= r^2 a4(r); and the geometric-tail bound sum_{k<K} q^k <= 1/(1-q) for 0 <= q < 1. Compile record in U_F0090.compile_output.txt; axioms printed for all three theorems (outcome at the end of Section 7). The information-theoretic step (chain rule) and the percolation inputs are not formalised.

## 6. The strongest case that this is wrong, and the check that would show it

The cheapest place for a hole is Section 3.3(b)/(c): that box-pivotality near a side forces the half-plane three-arm event, and near a corner the quarter-plane two-arm event, in regions disjoint from the four-arm annulus around the box. This is exactly the statement GPS make in the first paragraph of Section 4.3 ("the percolation configuration inside B(x,r) has an effect on the crossing event only if we have the 3-arm event in the half-annulus ... Similarly, if x is one of the corners ... we need the 2-arm event in the quarter-annulus"), applied to the enlarged boundary-centred box that contains B (pivotality is monotone in the set). The half-plane exponent (4.12) is cited by GPS for both lattices and used by them in the Z^2 case of Proposition 4.1. If (4.12) held only on the triangular lattice, the Z^2 case of the theorem would lose its boundary control, but the triangular case would stand. The check I ran that would have exposed a wrong boundary estimate is the simulation: the total pivotal-box count per scale, including boundary boxes, followed the bulk scaling (R/r)^{3/4} with a bounded constant across R = 32..256; a boundary contribution growing like (R/r) would have shown up as a ratio drifting upward like R^{1/4} (a factor 1.7 from R = 32 to 256), and it drifted by 8 percent.

A second worry: whether Kalai's H(S(f)) uses the 0/1 or +-1 normalisation. Both are covered (Section 3.2).

## 7. Prior art

Web searches run 2026-09-09 (before any derivation): "entropy" "spectral sample" percolation crossing influence Kalai; Fourier entropy influence conjecture percolation crossing event proved; "entropy of the pivotal" OR "entropy of the spectral sample" percolation; Garban Pete Schramm first moment spectral sample box four-arm; Kalai entropy pivotal spectral percolation 2019-2025; "anomaly of majority"; "Fourier entropy" percolation Garban O(n^{3/4}). None returned a paper treating the percolation special case. The general FEI conjecture remains open; the best general bound is Han, A new bound for the Fourier-Entropy-Influence conjecture, Combinatorica 2025 (arXiv 2312.08271). The question itself appears as Open Problem 1 of GPS (Acta Math. 2010, Section 11), which I read in full; GPS do not answer it, and the Garban-Steif lecture notes (arXiv 1102.5761) mention entropy only in the heuristic "clustering versus entropy" sense. The session's web-search budget ran out before a separate search for the half-plane three-arm citation; I rely on GPS (4.12) -> Werner 2007 for it.

Lean outcome: U_F0090.lean compiled clean on the second attempt (the first attempt had one tactic error, a redundant `ring` after `field_simp` had already closed the goal; that line was the one fix). `#print axioms` for all three theorems: [propext, Classical.choice, Quot.sound]. Compiler: Lean v4.33.1 with the project's Mathlib, run inline at BelowNormal priority; record in U_F0090.compile_output.txt.
