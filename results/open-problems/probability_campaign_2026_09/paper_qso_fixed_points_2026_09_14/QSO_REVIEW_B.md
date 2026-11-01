# Referee B report: Rozikov's Problem 11 (strictly non-Volterra QSOs), the E0064 result

Reviewed 2026-09-14. Documents read in full: the memo
`downloads_memos/Probability_E0064_strictly_nonVolterra_fixed_point_uniqueness_fails_for_five_types_2026-09-11.md`,
the audit passage (results_B_settled_and_audits.md lines 968-1044) and the report row
(Probability_1000_open_problems_report_2026-09-12.md lines 5492-5556). I also read pages 6-8 of the source
survey (arXiv:0902.4207): Problem 11 is worded "Is Theorem 6 true for m >= 4?" and Theorem 6 is stated exactly as
the memo quotes it (unique fixed point, not attractive; 2-cycles and 3-cycles depending on the parameters), for the
family (14) with a+b = c+d = alpha+beta = 1. Reference [40] is Rozikov and Jamilov, Sb. Math. 200 (2009) 1339-1351.

Everything below was recomputed independently; scripts are in this scratchpad directory
(`qso_m5_exact.py`, `qso_dyn_vec.py`, `qso_controls.py`, `qso_equiprobable.py`, `qso_m4_lp.py`, `qso_fold_grid.py`).
Exact arithmetic is sympy rationals; the LPs are scipy/HiGHS; nothing ran in the background; each script finishes in
under two minutes on this machine.

## 1. The five-type example, exact arithmetic - CLEAN

1.1 The tensor as written (face: P_{ii,k} = 1/2, P_{ij,k} = 1 for {i,j,k} = F; across: P_{i4,5} = P_{i5,4} = 1,
P_{44,5} = P_{55,4} = 1, P_{45,k} = 1/3) is symmetric in (i,j), nonnegative, every one of the 25 (i,j) rows sums to
1, and P_{ij,k} = 0 whenever k is in {i,j}, with no exception. Expanding V from the tensor reproduces the memo's
coordinate formulas exactly (V_k = (x_a^2+x_b^2)/2 + 2x_a x_b + (2/3)x_4x_5 on the face, V_4 = 2(x_1+x_2+x_3)x_5 + x_5^2,
V_5 likewise).

1.2 V(p) - p = 0 and V(q) - q = 0 exactly for p = (1/3,1/3,1/3,0,0), q = (1/9,1/9,1/9,1/3,1/3).

1.3 Jacobians. DV(p) is the 3x3 all-ones-minus-identity block on the face plus the block [[0,2],[2,0]] on (x_4,x_5);
DV(q) has entries in {1/3, 2/9, 2/3, 4/3}. Both have trace 0 and satisfy DV(x)x = 2x (Euler). Restricting to the
tangent space (sum-zero vectors; invariant because every column of DV sums to 2) the characteristic polynomials are
(t-2)(t+1)^2(t+2) at p and t(3t+1)^2(3t+4)/27 at q, i.e. eigenvalues (2,-1,-1,-2) and (0,-1/3,-1/3,-4/3), as claimed.

1.4 Index. det(I - DV|T) = -12 at p and 112/27 at q, so the sign is -1 at p and +1 at q, as claimed - but see
finding 6.1 for what this index is an index of.

1.5 Attractiveness. Spectral radius on the tangent space is 2 at p and 4/3 at q, so neither point is attracting in
the spectral sense; and by iteration (renormalising to the simplex each step) five starts at distance 1e-5 from q
are at median distance 0.57 after 40 steps and five starts at 1e-5 from p are at 0.89 after 20 steps. Neither is
attracting in the topological sense either.

1.6 The count is exact, not just "at least two". Solving V(x) = x together with sum x = 1 in exact arithmetic gives a
zero-dimensional system with 16 solutions on the affine hull (all real, e.g. (-1,-1,3,0,0), (17/9,-7/9,-7/9,1/3,1/3),
(-2/3,-2/3,-2/3, 3/2 -+ sqrt(21)/2, 3/2 +- sqrt(21)/2)), of which exactly two lie in the closed simplex: p and q. The
paper can say "exactly two fixed points" rather than "two fixed points".

1.7 The m >= 6 two-face construction and the "why it stops at m = 5" paragraph are correct as written: two invariant
triples sharing a pair {i,j} would need P_{ij,.} supported on two different single types; at m = 4 an invariant
face F forces V_4 = 0 identically. The numerical count "two in 27, three in 3" for random six-type operators was not
re-run (the script is not among the files I was given); it is not load-bearing.

## 2. Dynamics of the five-type example (for clause (2) of Theorem 6)

2.1 The vertex pair is a 2-cycle: V(e_4) = e_5 and V(e_5) = e_4, because P_{44,5} = P_{55,4} = 1. It is
superattracting: D(V^2)(e_4) is the rank-one matrix with row 4 equal to (4,4,4,4,4) and all other rows zero, so its
eigenvalues are 4 (the radial direction, 2^2) and 0 with multiplicity 4 - every tangent multiplier is zero.

2.2 Generic orbits go to that vertex 2-cycle. From 300 Dirichlet(1) interior starts and 200 Dirichlet(0.2) sparse
starts, 500 of 500 orbits are within 1e-8 of the cycle e_4 <-> e_5 after 3000 steps. (Iteration must renormalise each
step: the map is homogeneous of degree 2, so a floating-point error eps in the sum becomes (1+eps)^{2^n}; my first
unnormalised run overflowed. Any long-iteration numerics in the paper should say they renormalised.)

2.3 The hyperplane x_4 = x_5 is invariant (V_4 = V_5 there) and on it every orbit converges to q (100 of 100 starts);
q's eigenvalues -1/3, -1/3, 0 are the in-slice ones and -4/3, with eigenvector (0,0,0,-1,1), is the transverse
direction that expels everything else. So q is a saddle whose stable set is the codimension-one slice x_4 = x_5.

2.4 The face x_4 = x_5 = 0 is invariant and carries the symmetric three-type operator. Its fixed point (1/3,1/3,1/3)
has tangent eigenvalues exactly -1, -1. Orbits there do not settle into an exact 2-cycle: they look 2-periodic to
five decimals but drift, and the drift is toward the fixed point at rate n^{-1/2} (median |x_n - barycentre| over
200 starts: 0.109, 0.036, 0.0115, 0.0037 at n = 10^2, 10^3, 10^4, 10^5; |V^2(x_n) - x_n| ~ n^{-3/2}). Exact solving
of V^2(x) = x on the face finds only the fixed point in the simplex; a Newton search for period-2 points of the
five-type operator (1500 starts) returns, besides the vertex cycle, only points within 1e-5 of p where V^2 = id +
cubic terms - artefacts of the degenerate multipliers (1,1), not cycles. A Newton search for period-3 points (1500
starts) found none.

2.5 What the paper can say about clause (2): the example has a 2-cycle (the vertices e_4, e_5), it is the global
attractor off the slice x_4 = x_5, and no 3-cycle was found. It does not address whether 3-cycles exist for some
parameter values in higher dimension, and the paper should keep saying that the cycle clause is not addressed.

## 3. The non-attractiveness half (equiprobable family, m = 4) - CLEAN, with the constant now proved

3.1 The identity V_k - V_l = (x_l - x_k)[2 - m(x_k+x_l)/(m-1)]/(m-2) was verified symbolically at m = 4, 5, 6 (in the
homogenised form with 2 replaced by 2(x_1+...+x_m), which is the same thing on the simplex).

3.2 The contraction constant (2m-1)/(m-1)^2 is correct and sharp. Numerically the supremum of diam V(x)/diam x over
the simplex is 0.777718 (m = 4), 0.562441 (m = 5), 0.439935 (m = 6) against 7/9, 9/16, 11/25, attained at
x = (0, 1/(m-1), ..., 1/(m-1)). Neither the row nor the memo derives it, so here is a proof. Take any pair k, l with
x_k <= x_l, write d = x_l - x_k <= D = diam x and s = x_k + x_l; then |V_k - V_l| = d(2 - ms/(m-1))/(m-2). If
s >= 1/(m-1) the bracket factor is at most (2 - m/(m-1)^2)/(m-2) = (2m-1)/(m-1)^2 and d <= D. If s < 1/(m-1), the other
m-2 coordinates sum to 1-s, so x_max >= (1-s)/(m-2) and D >= (1-s)/(m-2) - x_k, whence
d/D <= (s - 2x_k)/((1-s)/(m-2) - x_k) <= s(m-2)/(1-s) (the quotient is decreasing in x_k because s < 2/m); therefore
|V_k - V_l|/D <= h(s) = s(2 - ms/(m-1))/(1-s), which is increasing on (0, 1/(m-1)) with h(1/(m-1)) = (2m-1)/(m-1)^2.
Since (2m-1)/(m-1)^2 < 1 iff m^2 - 4m + 2 > 0 iff m >= 4 (it is 5/4 at m = 3), the diameter contracts geometrically for
m >= 4 and every orbit converges to the barycentre.

3.3 Iteration confirms it: from 3000 starts at m = 4 (500 of them on the boundary), after 60 steps max |x - 1/4| =
1.1e-11; at m = 5 and 6, 5.6e-17.

3.4 The zero-trace argument is correct: for a fully generic symbolic 4-type strictly non-Volterra tensor, every
diagonal entry of DV vanishes (dV_k/dx_k = 2 sum_j P_{kj,k}x_j = 0), tr DV = 0, DV(x)x = 2V(x), so at a fixed point 2 is
the radial eigenvalue and the m-1 tangent eigenvalues sum to -2. At the barycentre of the equiprobable operator they
are -2/(m-1) each. A sharper general fact worth adding: DV(x) = 2M(x) with M_{kl} = sum_j P_{lj,k}x_j column-stochastic
and zero-diagonal, and M x = x at a fixed point, so every tangent eigenvalue has modulus at most 2 (p in the
five-type example attains -2).

3.5 A wording caveat, not a defect: "attractive" in the source and in the memo has to mean the spectral notion (all
tangent eigenvalues of modulus < 1), which is the usage in the QSO literature. The face operator in 2.4 shows the two
notions differ: its fixed point has eigenvalues -1, -1 and is not attractive spectrally, yet every orbit converges to
it at rate n^{-1/2}. The row's sentence that the trace bound "reproduces Theorem 6's non-attractiveness" at m = 3 is
true only under the spectral definition (a tangent eigenvalue of modulus >= 1), and the paper should say which
definition it uses. For the five-type example both notions agree (1.5).

## 4. The open case m = 4: what I did and what it gave

No proof; the case stays open. What follows is (a) three structural facts that constrain any counterexample, all
proved, (b) a reduction of uniqueness to a single "fold" condition, and (c) a numerical attack on that condition and
on two-fixed-point pairs that is more exhaustive than a random Newton search.

4.1 Every fixed point of a 4-type operator that is not face-invariant is interior. A vertex is never fixed
(V_i(e_i) = P_{ii,i} = 0). An edge point (a, 1-a, 0, 0) is never fixed: V_3 + V_4 >= 2a(1-a) > 0 because
P_{12,3} + P_{12,4} = 1. A face point with three positive coordinates and x_4 = 0 needs sum_{i,j<=3} P_{ij,4} x_i x_j = 0,
i.e. P_{ij,4} = 0 for all i, j <= 3, i.e. the face is invariant; then V_4 = 0 identically, every fixed point lies in
the face, and the face restriction is a three-type operator with exactly one fixed point by Theorem 6.

4.2 Lefschetz makes the count odd. V is a continuous self-map of a compact convex set, so the fixed-point indices
sum to 1; an interior nondegenerate fixed point has index sign det(I - DV|T). Hence a non-face-invariant 4-type
operator whose fixed points are all nondegenerate has an odd number of them. Two fixed points is impossible at
m = 4 except through a degenerate one; a counterexample must have at least three, one of index -1, which by 3.4
needs a real tangent eigenvalue in (1, 2] with the other two summing to below -3. (Random operators: 60 operators,
80 Newton starts each, Dirichlet concentrations 1 and 0.2 - always exactly one fixed point, index +1, and the
largest tangent eigenvalue modulus seen was 1.07, so genuine saddles do occur.)

4.3 Reduction. The coefficient polytope is convex, hence connected; the equiprobable operator has exactly one fixed
point (section 3); the number of fixed points is locally constant in P wherever every fixed point is nondegenerate,
because a fixed point can only appear or disappear by passing through a degenerate one (implicit function theorem)
or by leaving the simplex, and by 4.1 the latter can only happen at a face-invariant operator, where the count is
one and the fixed point is automatically nondegenerate (its transverse eigenvalue is 0 and a three-type operator
cannot have a tangent eigenvalue 1, since the other would then be -3, beyond the Perron bound 2 of 3.4). So:

    uniqueness for every 4-type strictly non-Volterra operator follows if no such operator has a fixed point
    x at which DV(x) has a tangent eigenvalue exactly 1 (a fold).

Both V_P(x) = x and DV_P(x)d = d are linear in P for fixed (x, d), so for each (x, d) the fold condition is an LP
feasibility problem with 24 variables (the free P_{ij,k}), 10 row-sum equalities and 8 further equalities. Likewise
"x and y are both fixed" is an LP for fixed (x, y). This is the "two-fixed-point objective over the coefficient
polytope" done properly: the inner problem in P is solved exactly and only the points are searched.

4.4 Numerical results (phase-1 residual = minimum over admissible P of the l1 norm of the violated equalities;
zero means feasible). Controls: at m = 5 the pair (p, q) of the memo gives residual exactly 0 and the LP returns an
operator fixing both; a random m = 5 pair gives 0.95; the LP's Jacobian rows agree with a central finite difference
of V to 8e-11.
  - Pairs, m = 4: 1750 random pairs drawn from five families (interior, sparse, face points, edge points, near the
    barycentre): smallest residual/|x-y|_1 = 0.695 (raw residual 0.313). Nelder-Mead from the best starts with the
    constraint |x-y|_1 >= 0.05: smallest 0.586. Grids of 25 x 25 on symmetric slices - (a,a,b,b) vs (c,c,d,d): 0.708;
    (a,b,b,b) vs (c,d,d,d): 1.000; (a,b,b,b) vs (d,c,d,d): 0.711; (a,a,b,b) vs (c,d,c,d): 0.904; a face point vs an
    interior point of the form (c,c,c,d): 0.689. Nothing approaches zero; the closest pairs are all a face point
    against a near-barycentre point, which 4.1 already rules out.
  - Folds, m = 4: exhaustive coarse grid (simplex step 1/10, 286 points, times 26 tangent directions on a Fibonacci
    sphere, 7436 LPs): smallest residual 1.0066, at x = (0, 1/2, 0, 1/2); 1500 steps of random local refinement do
    not lower it; an independent Nelder-Mead search from 150 random (x, d) gives 1.08. In l1 units on equalities
    whose right-hand sides are coordinates of a probability vector and a unit direction, a residual above 1 is far
    from feasibility.
  - One-parameter families through the equiprobable operator are covered by 4.3: along any path in the polytope an
    extra fixed point can only be born at a fold, and no fold was found anywhere.

4.5 What I did not manage. A proof would be a Farkas certificate for the fold LP that is valid for every (x, d): by
duality the LP at (x, d) is infeasible iff there are u, v in R^4 and w in R^10 with c_{ij}(x)u_k + c'_{ij}(x,d)v_k + w_{ij}
>= 0 for every admissible (ij, k) and <x, u> + <d, v> + sum w < 0, where c_{ij}(x) = x_i x_j or 2x_i x_j and
c'_{ij}(x,d) is its directional derivative. The certificate must be chosen piecewise in (x, d) and I did not find a
closed form. A Lyapunov function attempt got nowhere: the natural candidates (entropy, sum of squares, the diameter
of section 3) are not monotone for general coefficients even at m = 4, because the map is not a contraction near a
saddle (4.2 shows tangent eigenvalues above 1 in modulus occur). The reduction 4.3 and the odd-count fact 4.2 are, I
think, the right things to put in the paper's m = 4 paragraph; they are stronger than "numerically supported".

## 5. Prior art (WebSearch, 2026-09-14)

Queries and what came back:
  1. "strictly non-Volterra quadratic stochastic operator fixed points m=4 four-dimensional simplex" - the survey
     (0902.4207), the quasi-strictly paper (1808.00229, m = 3 only), a permutation family (2210.05107); nothing on
     strictly non-Volterra operators at m >= 4.
  2. "strictly non-Volterra ... two fixed points OR unique fixed point Jamilov Ladra Mukhitdinov" - confirms Jamilov,
     Ladra, Mukhitdinov, "On the equiprobable strictly non-Volterra quadratic stochastic operators", QTDS 16 (2017)
     645-655 (search summaries: unique fixed point, attracting, Lyapunov function, every limit set a singleton, on a
     finite-dimensional simplex); 1808.00229: four-parameter family on S^2, unique fixed point with one exception.
  3. "Rozikov Problem 11 ... Theorem 6" - only the survey itself.
  4. "Ganikhodzhaev Mukhamedov Rozikov strictly non-Volterra unique fixed point 2-cycles 3-cycles" - the source of
     Theorem 6 is Rozikov and Jamilov, Sb. Math. 200 (2009) 1339-1351; also Jamilov, "On a family of strictly
     non-Volterra QSOs", J. Phys. Conf. Ser. 697 (2016) 012013, and Jamilov, "On symmetric strictly non-Volterra
     QSOs", Discrete and Nonlinear Complex Systems 5 (2016) 263-283 - bibliographic hits only, texts not reachable.
  5. "non-Volterra ... three fixed points OR two fixed points OR several fixed points ... 2018..2026" - l-Volterra
     operators with up to three fixed points (a different class), and arXiv:2601.17494 (2026, a convex combination of
     non-Volterra operators; not strictly non-Volterra as far as the abstract shows).
  6. "arxiv strictly non-Volterra 2022-2026" - 2211.06186 (a continuous-time analogue on S^2) and 2601.17494.
  7. "Jamilov strictly non-Volterra three-dimensional simplex / S^3 / four types" - the 2013 paper "On non-ergodic
     transformations on S^3" (Ganikhodjaev, Jamilov, Mukhitdinov) is about extremal Volterra operators; irrelevant.
  8. The introduction of 1808.00229 (ar5iv) says only "In [11] the case m = 3 was studied" and states no higher-m result.
  9. Second pass, different phrasing: "strictly non-Volterra operator finite-dimensional simplex OR m-dimensional
     simplex fixed points dynamics" - only the S^2 results again (Rozikov-Jamilov 2009, 1808.00229) plus unrelated
     doubly stochastic and Lotka-Volterra papers.
 10. Second pass by the defining condition: "P_{ij,k}=0 k in {i,j} higher dimension fixed point not unique OR several
     fixed points" - returns Volterra-class results (the complementary condition), where non-uniqueness is classical
     and irrelevant here.
Result: nothing found. No post-2009 paper turned up that exhibits a strictly non-Volterra QSO with two or more fixed
points, and none that proves uniqueness for m >= 4. Two caveats: the two 2016 Jamilov papers (items 4) could not be
read and the "symmetric" one may treat a symmetric family in general dimension - the authors should check it before
claiming the equiprobable half is "only" in the 2017 paper; and the 2017 paper's own abstract is behind a login
redirect, so I could not confirm from the text which m it covers (the search summaries say a finite-dimensional
simplex, which fits the memo's attribution).

## 6. Defects and required wording changes

6.1 DEFECT (minor, affects the m = 4 remark). "p is a saddle with index -1" is the index of p as a fixed point of V
on the affine hull of the simplex. As a fixed point of V on the simplex its index is 0: the Lefschetz sum over the
simplex is 1, the interior point q contributes +1, and by 1.6 there are no other fixed points. The reason is visible
in the eigenvectors: the eigenvalue-2 eigenspace at p is spanned by (1,1,1,0,0) and (0,0,0,1,1), so the repelling
tangent direction points into the simplex, while the -2 direction (0,0,0,1,-1) leaves it on both sides. The memo's
inference that "the five-type example shows that the count can involve a saddle of index -1" therefore does not
follow from the example, and at m = 4 it cannot happen in the form of two fixed points at all (4.2). Suggested fix:
call p a saddle with sign det(I - DV|T) = -1 "in the ambient hyperplane", drop the sentence about the count, and
replace the m = 4 paragraph's last two sentences by the odd-count fact and the fold reduction.

6.2 DEFECT (wording). Define "attractive" (spectral: all tangent eigenvalues of modulus below 1) wherever the row or
the paper says the trace bound "reproduces" Theorem 6's non-attractiveness; see 3.5.

6.3 Not a defect but should be stated: the contraction constant (2m-1)/(m-1)^2 is asserted in the row without proof;
a proof is in 3.2 and the constant is sharp.

6.4 The memo's "two fixed points" can be strengthened to "exactly two" (1.6), and the dynamics (section 2) can be
quoted for clause (2): a superattracting vertex 2-cycle that captures every orbit off the invariant slice x_4 = x_5,
no 3-cycle found.

## 7. Verdict

The mathematics that the result rests on is right. The five-type operator is admissible and strictly non-Volterra,
has exactly two fixed points in the simplex with the stated tangent spectra, and neither is attracting; the m >= 6
two-face construction is sound; the m = 4 equiprobable operator is a geometric contraction of the coordinate
diameter with the stated (and sharp) constant, so clause (1)'s non-attractiveness fails from m = 4; the zero-trace
argument is correct. So: Theorem 6 does not extend to m >= 4 - non-attractiveness fails at m = 4, uniqueness fails
for every m >= 5 - and uniqueness at m = 4 remains open. Two wording defects (6.1, 6.2) should be fixed before
publication; 6.1 changes what the memo says about the route to m = 4. My own m = 4 work adds two proved facts
(all fixed points interior unless face-invariant; the count is odd) and a reduction to a fold condition that a
7436-cell exhaustive LP grid plus local searches leaves with residual above 1, i.e. no fold anywhere near; that
is the strongest evidence for m = 4 uniqueness I could produce, and it is evidence, not a theorem. Prior art:
nothing found beyond what the memo cites, with the two unread 2016 Jamilov papers flagged for the authors.

Recommendation: accept the settled claims (m >= 5 uniqueness failure; m >= 4 non-attractiveness failure, attributed
to Jamilov, Ladra and Mukhitdinov 2017) after the 6.1 and 6.2 changes; keep m = 4 uniqueness and the cycle clause
open, with the section-4 facts if the authors want them.
