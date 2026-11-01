# A non-monotone Markov intensity whose speeded-up versions decrease in the supermodular order

Problem P0291 of the campaign ledger. Source: L. Leskelä, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022) 213-215, Problem 3 (journal numbering; Problem 2 in arXiv:2204.11856): "Does there exist a stationary and ergodic CTMC λ = (λ(t)) which is not stochastically monotone but satisfies (2)?", where (2) is the property

    c1 <= c2  implies  λ_{c1} >=_sm λ_{c2},      λ_c(t) := λ(ct),

and X <=_sm Y for processes means E φ(X_{t_1}, ..., X_{t_n}) <= E φ(Y_{t_1}, ..., Y_{t_n}) for all n, all times and all supermodular φ: R^n -> R for which the expectations exist. Bäuerle and Rolski (J. Appl. Probab. 35 (1998) 741-747) proved (2) for every doubly stochastically monotone finite-state CTMC (Q and its time reversal Q* both monotone for the strong order on the real line), and Leskelä notes that "outside the domain of stochastically monotone CTMCs, not much seems to be known ... even for state spaces of size 3".

Written 2026-09-10 by the Claude agent claude-prob1000-0910. Status: author-checked proof with an exact finite certificate for its one combinatorial step; not independently refereed; novelty not certified (no citation search beyond the source and the two papers it cites was run).

## Answer: yes, on three states

**Theorem.** Let a, b > 0 and let λ be the stationary CTMC on the intensity values 1 < 2 < 3 with generator

    Q = [ -2a   a    a ]
        [   b  -b    0 ]
        [   b   0   -b ]

(a star: from the middle value 1 the chain jumps to 2 or to 3 at rate a each, and from 2 and from 3 it returns to 1 at rate b). Then λ is stationary, ergodic and reversible with π = (b, a, a)/(b + 2a); it is not stochastically monotone; and it satisfies (2): for every c1 <= c2, λ_{c1} >=_sm λ_{c2}.

The values 1, 2, 3 can be replaced by any v1 < v2 < v3 (the supermodular order is invariant under a common increasing relabelling of the coordinates), so the intensity can be positive and as spread out as one likes. Since (2) implies Ross's monotonicity (1) by Bäuerle-Rolski, the star is also a non-monotone environment for which faster modulation never increases the mean stationary workload.

Non-monotonicity is immediate: P_t(1, {3}) = a t + O(t^2) while P_t(2, {3}) = O(t^2), so P_t(1, .) <=_st P_t(2, .) fails for small t. (Reversibility gives Q* = Q, so the chain is not doubly monotone either.)

## Proof of (2)

Write X for λ. Fix n, times t_1 < ... < t_n, a supermodular φ, and the gaps g_k = t_{k+1} - t_k. By stationarity the law of (X(c t_1), ..., X(c t_n)) depends only on the gaps c g_k, so it suffices to show that

    F(g_1, ..., g_{n-1}) := E φ(X(0), X(g_1), X(g_1 + g_2), ...)

is nonincreasing in each g_k separately, the other gaps being fixed: passing from (c1 g_k) to (c2 g_k) then increases the gaps one at a time.

**Step 1: one gap.** Fix k and write s_j for the sampling times. By the Markov property, conditionally on (X(s_k), X(s_{k+1})) = (x, y) the prefix (X(s_1), ..., X(s_{k-1})) and the suffix (X(s_{k+2}), ...) are independent, with laws depending only on x and on y respectively (and on the other gaps). Hence

    F = sum_{x,y} π(x) P_g(x, y) Φ(x, y),     Φ(x, y) := E φ(A^x, x, y, B^y),

where g = g_k, A^x has the law of the prefix given X(s_k) = x, B^y the law of the suffix given X(s_{k+1}) = y, A^x and B^y independent, and Φ does not depend on g.

**Step 2: the spectral reduction.** Q is reversible with right eigenvectors v_0 = (1,1,1), v_1 = (0, 1, -1), v_2 = (-2a/b, 1, 1) and eigenvalues 0, -b, -(2a+b) (Q v_1 = (a - a, -b, b) = -b v_1; Q v_2 = (4a^2/b + 2a, -2a - b, -2a - b) = -(2a+b) v_2), orthogonal in L^2(π). So P_g(x,y) = sum_l e^{-μ_l g} v_l(x) v_l(y) π(y)/<v_l, v_l>_π and

    F(g) = C + α e^{-b g} + β e^{-(2a+b) g},
    α = π_2^2 [Φ22 - Φ23 - Φ32 + Φ33] / (2 π_2),
    β = (b/2a) π_2^2 [4 Φ11 - 2(Φ12 + Φ13 + Φ21 + Φ31) + Φ22 + Φ23 + Φ32 + Φ33],

using π(1) v_2(1) = -2π_2, π(2) v_2(2) = π(3) v_2(3) = π_2, <v_1,v_1>_π = 2π_2 and <v_2,v_2>_π = 2a/b. Now F'(g) = -b α e^{-bg} - (2a+b) β e^{-(2a+b)g}, so F is nonincreasing on (0, ∞) if and only if b α + (2a+b) β u >= 0 for every u = e^{-2ag} in (0, 1), i.e. (the expression is affine in u) if and only if

    (C1)   Φ22 + Φ33 >= Φ23 + Φ32                         (u -> 0),
    (C2)   2 Φ11 + Φ22 + Φ33 >= Φ12 + Φ13 + Φ21 + Φ31     (u -> 1).

The second follows from b α + (2a+b) β = b π_2 [2Φ11 + Φ22 + Φ33 - Φ12 - Φ13 - Φ21 - Φ31], where one uses (2a+b) b π_2^2/(2a) = b π_2/2, which is π_2 = a/(b+2a). Both conditions are free of a and b.

**Step 3: the coin description of the star.** Let Y_t = 1{X_t in {2,3}} (the skeleton), a two-state chain with rates 2a up and b down. Given the whole path of Y, the values of X on the successive leaf excursions are independent fair coins with values in {2, 3}: from the centre the chain picks 2 or 3 with probability 1/2 each, independently of the holding times and of the past, and it cannot pass from 2 to 3 without visiting 1. Conditionally on X(s_k) = x in {2,3}, the prefix consists of the skeleton reversed from a leaf (the star is reversible, so the reversed chain is the star), the value x on every prefix index j < k such that Y stays at the leaf throughout [s_j, s_k] (the *current block* I of the prefix), and independent fair coins on the other excursions. Conditionally on X(s_k) = 1 the prefix is the skeleton reversed from the centre with fair coins on all its excursions. The same description holds for the suffix, forward from y, with current block J.

**Step 4: (C1).** Couple A^2 and A^3 on one skeleton with the same coins off the current block; they then differ exactly on I, where they equal 2 and 3. Do the same for B^2, B^3 on J. With ψ(u, v) := φ(vector with I ∪ {k} set to u, {k+1} ∪ J set to v, all other coordinates as coupled), ψ is supermodular on R^2 (the join and meet of two block-constant vectors are block-constant with the joined and met block values, so increasing differences of φ pass to ψ), and

    Φ22 + Φ33 - Φ23 - Φ32 = E [ψ(2,2) + ψ(3,3) - ψ(2,3) - ψ(3,2)] >= 0.

**Step 5: (C2), the coupling.** Couple the skeleton from the centre (Z^1) with the skeleton from the leaf (Z^L) by the usual order-preserving coupling of a monotone two-state chain: while they differ, Z^1 jumps up at rate 2a and Z^L jumps down at rate b independently; at the first of these jumps they coalesce and move together. The marginals are the correct ones (memorylessness). Two cases. If Z^L comes down first, the two skeletons coalesce at the centre: A^1 equals 1 on the whole current block I of Z^L and agrees with A^x (x = 2, 3, coupled as in Step 4) everywhere else, once the later excursions are given common coins. If Z^1 jumps up first, at a time τ inside Z^L's current block, then Z^1 starts an excursion whose coin c is fair and independent of everything else, and that excursion ends when Z^L's current block ends; so A^1 equals 1 on I \ O and c on O, where O is the set of prefix indices of the current block after τ, and agrees with A^x elsewhere. In both cases: A^x = x on I; A^1 = 1 on I \ O, c on O (O possibly empty); identical elsewhere. Likewise for the suffix, with J, O', a fair coin c', independently of the prefix.

Define ψ(u, u', v, v') := φ with the four disjoint blocks (I ∪ {k}) \ O, O, ({k+1} ∪ J) \ O', O' set to the constants u, u', v, v' and every other coordinate as coupled; ψ is supermodular on {1,2,3}^4. Then, writing the six terms of (C2) on the common space and using 2Φ11 = Φ11 + Φ11,

    2Φ11 + Φ22 + Φ33 - Φ12 - Φ13 - Φ21 - Φ31
      = E sum_{l in {2,3}} [ψ(l,l,l,l) - ψ(l,l,1,c') - ψ(1,c,l,l) + ψ(1,c,1,c')]
      = (1/4) E S(ψ),

    S(ψ) := sum_{l, c, c' in {2,3}} [ψ(l,l,l,l) - ψ(l,l,1,c') - ψ(1,c,l,l) + ψ(1,c,1,c')],

because c and c' are fair and independent of the rest. When O or O' is empty ψ simply does not depend on the corresponding argument.

**Step 6: the finite inequality S(ψ) >= 0.** For l = 3 every term is nonnegative by supermodularity, since (3,3) dominates (1,c) and (1,c') coordinatewise; for l = 2 the terms with c = 3 or c' = 3 are not individually signed, and the inequality holds only as a whole. It is an exact nonnegative combination of elementary increasing-difference inequalities. Writing E[x; i, j] := ψ(x + e_i + e_j) - ψ(x + e_i) - ψ(x + e_j) + ψ(x) >= 0, one has the identity (checked in rational arithmetic, `p0291_c2_certificate.py`)

    S(ψ) = 2 E[(1,2,1,2); 1,3] + 2 E[(1,2,1,3); 1,3] + 2 E[(1,2,2,3); 1,3]
         + 2 E[(1,3,1,2); 1,3] + 2 E[(1,3,1,3); 1,3] + 2 E[(1,3,2,3); 1,3]
         + 2 E[(2,2,2,2); 2,4] + 2 E[(2,2,2,3); 2,3]
         + 2 E[(2,3,1,2); 1,4] + 4 E[(2,3,1,3); 1,3] + 4 E[(2,3,2,3); 1,3],

which can be verified by expanding both sides (26 elementary terms; each side has the same 32 signed point evaluations). Hence S(ψ) >= 0 for every supermodular ψ, (C2) holds, F is nonincreasing in every gap, and (2) follows. QED.

## What the proof uses and what it does not

The Bäuerle-Rolski route (monotone kernels propagate supermodularity through the chain) is not available here: for the star, conditioning on two interior coordinates does not preserve supermodularity (an LP search finds supermodular φ on {1,2,3}^3 whose conditional Φ has increasing differences as negative as -0.64). What replaces it is the exact one-gap structure of a reversible three-state chain, which turns gap monotonicity into the two finite conditions (C1), (C2), and the fact that the star's non-monotonicity is entirely "which leaf": the skeleton is a monotone two-state chain and the leaf labels are exchangeable fair coins. Exchangeability is load-bearing: with unequal return rates b_2 < b_3 the LP test of (2) fails (worst violation 3.2e-2 at n = 3), whereas b_2 > b_3 and unequal arrival rates a_2 != a_3 passed the same test (measured, not proved).

## Numerical controls (all measured 2026-09-10, scripts in `06_math_research/prob1000_lean_20260908/`)

- `p0291_star_sm_lp.py`: exact LP test of (X(c1 t_k)) >=_sm (X(c2 t_k)) on {1,2,3}^n via the dual (maximise E_{c2} φ - E_{c1} φ over supermodular φ with |φ| <= 1): star chains (a,b) in {(1,1),(1,3),(3,1)}, n = 3, 4, four time layouts, speed ratios 2 across 0.25..8: maximum +2e-15 (pass). Controls: the clockwise 3-cycle fails (violations up to 6.1e-2), the monotone birth-death chain passes.
- `p0291_diagnostics.py`: single-gap monotonicity passes (worst +5e-16); supermodularity is not preserved by two-point conditioning (min increasing difference -0.64).
- `p0291_c2_block_lp.py` and `p0291_c2_certificate.py`: min of S over supermodular ψ with |ψ| <= 1 is 0 with and without the overlap blocks; the certificate above is exact.
- `p0291_final_checks.py`: (C1) and (C2) computed directly from conditional expectations (reversed chain for the prefix, forward for the suffix), n = 3 and 4, three rate pairs, four prefix/suffix layouts: minima 0 to 1e-15; the n = 5 LP test passes at three rate pairs and three layouts.

## Addendum (same day): unequal rates, and Leskelä's Problem 4 on the star family

Write the general star as 1 -> 2 at rate a2, 1 -> 3 at rate a3, 2 -> 1 at rate b2, 3 -> 1 at rate b3, all positive. It is always reversible (a tree), π ∝ (1, a2/b2, a3/b3), and never stochastically monotone.

**Theorem 2 (equal return rates, any arrival rates).** If b2 = b3 = b, the star satisfies (2) for all a2, a3 > 0.

*Proof.* The reduction of Steps 1-2 goes through verbatim: the eigenvectors are v_1 = (0, a3, -a2) with eigenvalue -b and v_2 = (-(a2+a3)/b, 1, 1) with eigenvalue -(a2+a3+b), and with p := a2/(a2+a3), q := 1 - p one finds α = (π_2+π_3) p q [Φ22 - Φ23 - Φ32 + Φ33] and

    μ_1 α + μ_2 β = b (π_2 + π_3) [Φ11 + p Φ22 + q Φ33 - p(Φ12 + Φ21) - q(Φ13 + Φ31)]

(closed forms checked against a direct eigendecomposition on random Φ to all printed digits). So (C1) is unchanged and (C2) becomes its p-weighted form (C2_p). The coin description of Step 3 holds with coin law P(2) = p, P(3) = q, since the direction of the jump from the centre is independent of the holding times and of the past. Step 4 is unchanged. In Step 5 the coins c, c' have law (p, q), and the integrand of (C2_p) is

    S_p(ψ) = sum_{l, c, c'} w_l w_c w_{c'} [ψ(l,l,l,l) - ψ(l,l,1,c') - ψ(1,c,l,l) + ψ(1,c,1,c')],   w_2 = p, w_3 = q,

which is a cubic in (p, q): S_p = p^3 T_3 + p^2 q T_2 + p q^2 T_1 + q^3 T_0, where T_k collects the eight terms with exactly k labels equal to 2. Each T_k is an exact nonnegative integer combination of elementary increasing-difference inequalities E[x; i, j] (`p0292_biased_coin_certificates.py`, verified in rational arithmetic):

    T_3 = E[(1,2,1,2); 1,3]
    T_0 = E[(1,3,1,3); 1,3] + E[(1,3,2,3); 1,3] + E[(2,3,1,3); 1,3] + E[(2,3,2,3); 1,3]
    T_2 = E[(1,2,1,2); 1,3] + E[(1,2,1,3); 1,3] + E[(1,2,2,3); 1,3] + E[(1,3,1,2); 1,3] + E[(2,2,2,2); 2,4]
        + E[(2,2,2,3); 2,3] + E[(2,3,1,2); 1,4] + E[(2,3,1,3); 1,3] + E[(2,3,2,3); 1,3]
    T_1 = E[(1,2,1,3); 1,3] + E[(1,2,2,3); 1,3] + E[(1,3,1,2); 1,3] + E[(1,3,1,3); 1,3] + E[(1,3,2,3); 1,3]
        + E[(2,2,2,2); 2,4] + E[(2,2,2,3); 1,3] + E[(2,3,1,2); 1,3] + E[(2,3,1,3); 1,3] + E[(2,3,2,2); 1,4]
        + E[(2,3,2,3); 1,3] + E[(3,2,2,3); 2,3].

Hence S_p >= 0 for every p in [0,1] and every supermodular ψ, and (C2_p) follows. (At p = 1/2 one recovers 8 S_{1/2} = S of Step 6.) QED.

**Theorem 3 (necessity of b2 >= b3).** If b3 > b2 the star violates (2) already for n = 2.

*Proof.* Let -μ be a nonzero eigenvalue with right eigenvector v. The leaf rows give v(2) = b2 v(1)/(b2 - μ) and v(3) = b3 v(1)/(b3 - μ). Symmetrising -Q by π^{1/2} and applying Cauchy interlacing to the leaf principal submatrix diag(b2, b3) gives min(b2,b3) <= μ_1 <= max(b2,b3) <= μ_2, and for b2 != b3 the first two inequalities are strict (μ_1 = b3 would force v(1) = 0, then v(2) = 0 from the second leaf row, then v(3) = 0 from the centre row). Hence for b3 > b2, b2 < μ_1 < b3 and the slow-mode coefficient of P_s(1,3) = π_3 + c_1 e^{-μ_1 s} + c_2 e^{-μ_2 s}, which is c_1 = π_3 v_1(1) v_1(3)/<v_1,v_1>_π = π_3 b3 v_1(1)^2 / ((b3 - μ_1) <v_1,v_1>_π), is strictly positive. So P_s(1,3) decreases to π_3 for large s, and P(X_0 <= 1, X_s <= 2) = π_1 (1 - P_s(1,3)) increases in s there: the lower-orthant indicator 1{x <= 1, y <= 2} is supermodular, so (X_0, X_s) >=_sm (X_0, X_{s'}) fails for s < s' large. QED.

The same computation shows that for b3 < b2 the coefficient c_1 is negative and the two-point concordance condition holds (P_s(1,3) is then nondecreasing, being affine in e^{-(μ_2-μ_1)s} with the right signs at both ends); for b2 = b3 it is zero.

**Conjecture (the star family).** The star satisfies (2) if and only if b2 >= b3, i.e. the top value returns to the centre no faster than the middle value. Theorems 2 and 3 prove it except for b2 > b3, where the LP test of (2) at n = 3, 4 (four time layouts, three speed pairs) passed at every parameter point tried; see the table in `p0292_star_family_map.out`. A proof for b2 > b3 is not attempted here: the leaf-period length then depends on the label, so the centre/leaf skeleton is no longer an autonomous Markov chain and the finite block reduction of Step 5 does not apply as it stands.

The finished star map (`p0292_star_family_map.out`, 23 parameter points including b2/b3 ratios 1.2, 2, 4 and both orders, and a2/a3 ratios up to 10): every point with b2 >= b3 passes the LP test and every point with b2 < b3 fails it; at every point the LP verdict coincides with the two-point test (is P_s(1,3) nondecreasing).

**Beyond stars: a conjecture for all reversible three-state chains.** For any reversible chain on 1 < 2 < 3 the one-gap function is F(g) = C + α e^{-μ_1 g} + β e^{-μ_2 g} and the two conditions read, in general form,

    [E2]  α >= 0,  i.e.  <Φ, ℓ_1 ⊗ ℓ_1> = sum_{x,y} ℓ_1(x) ℓ_1(y) Φ(x,y) >= 0,   ℓ_1 = π v_1 the slow left eigenvector;
    [E1]  F'(0) <= 0,  i.e.  sum_{x<y} π(x) q(x,y) [Φ(x,x) + Φ(y,y) - Φ(x,y) - Φ(y,x)] >= 0,

because μ_1 α + μ_2 β = -<Φ, π Q> = -F'(0) by the spectral decomposition of Q, and π Q is symmetric. [E1] is a conductance-weighted sum over the edges of the increasing difference of Φ across the edge; for the symmetric star it is (C2). Taking Φ = φ (n = 2) in [E2]: since ℓ_1 has zero sum, ℓ_1 ⊗ ℓ_1 lies in the cone dual to the supermodular functions iff the partial sums of ℓ_1 have one sign, i.e. iff ℓ_1(1) ℓ_1(3) <= 0. So for every reversible three-state chain the two-point concordance condition ((X_0, X_s) decreasing in s in the bivariate supermodular order) is exactly

    ℓ_1(1) ℓ_1(3) <= 0    (the slow left eigenvector has opposite signs, or a zero, at the two extreme states),

and it is necessary for (2). Forty random reversible three-state generators (all six rates positive, `p0292_random_3state_map.py`, seed 20260910) were tested against the LP dual test of (2) at n = 3, 4: the sign condition predicted the verdict in all forty cases. Ten of the forty are stochastically monotone (all satisfy (2), as they must); of the thirty non-monotone ones, thirteen satisfy (2) and seventeen do not. So the sign condition is a conjectural characterisation of (2) on three states, and it produces thirteen further non-monotone examples for Problem 3 beyond the stars. On the failing chains both [E1] and [E2] fail for suitable prefix/suffix layouts (`p0292_which_condition_fails.out`); on the passing ones both hold to machine precision. Whether the two-point condition is sufficient in general, i.e. whether [E1] and [E2] for all conditional Φ follow from [E2] for Φ = φ, is the open part; a proof would need a substitute for the coin structure of the star, and I do not have one.

## Second addendum: Problem 2 (Boolean images of doubly monotone chains), a negative search

Problem 2 asks whether Ross's workload monotonicity (1) holds for λ = f(X) with f Boolean or deterministic and X doubly stochastically monotone. Two instruments were used (`p0290_*.py`). At light traffic the campaign's uniform expansion gives w(c) = εa/2 + ε² J_f(c) + O(ε³) with J_f(c) = ∫_0^1 (1-u) E[f(X_0) f(X_{cu})] du, so (1) fails for small ε exactly when J_f rises somewhere; for a reversible X every autocovariance is a nonnegative mixture of decaying exponentials and J_f is automatically monotone, which is why the earlier attempt on this row (reversible birth-death chains) found nothing. Doubly monotone chains need not be reversible: the three-state generator with rows (-1.3, 1.2, 0.1), (0.8, -2.0, 1.2), (0.5, 0.8, -1.3) is doubly monotone with a circulation, and among forty random four-state doubly monotone chains seven have complex eigenvalues. Even so, over 140 random doubly monotone non-reversible generators on 3 to 5 states, all Boolean f and thirty random nonnegative f each, and a twenty-restart hill-climb inside the doubly monotone cone, J_f never rose (one apparent rise at eigenvalues -221 and -64 was an eigendecomposition artefact and vanishes under direct quadrature). The autocovariance itself can rise, slightly: a four-state doubly monotone chain with f = 1_{{2,3}} has E f(X_0)f(X_t) = 0.060015 at t = 0.90 and 0.061145 at t = 10 (checked with expm), so f(X) can have a non-monotone autocorrelation and hence violate (2), while the (1-u)-weighted second-order coefficient stays monotone. Beyond light traffic, the exact mean workload of the MMPP/M/1 queue (matrix-geometric solution of the QBD, exponential unit service, so mean workload = mean number in system) is monotone in c for the hand example at loads 0.2, 0.5 and 0.8 for five Boolean f, and in 320 (chain, Boolean f, load) cases over sixteen random doubly monotone non-reversible chains on 3 and 4 states at loads 0.3 and 0.7 (`p0290_qbd_random.out`), no rise appeared. So Problem 2 is neither refuted nor proved here; what the search says is that a counterexample, if one exists, is not at light traffic and not among small random doubly monotone chains at moderate load with exponential service.

## Relation to the other problems in the note

Problem 1 (Ross's second conjecture) was refuted by the campaign on 2026-09-07/08 with a one-directional cyclic environment (ledger P0289). Problem 4 (a necessary and sufficient condition for (2)) remains open; the present example shows that stochastic monotonicity is not the answer, and the b_2 < b_3 failure suggests the condition involves how the return rates align with the state values. Problem 2 (Boolean images of doubly monotone chains) is untouched here; note that a Markov image f(Z) of a doubly monotone chain Z under a nondecreasing f is itself monotone (its upper sets are up-sets of Z's order), so Problem 3 could not have been answered by lumping a monotone chain, which is why a genuinely different mechanism was needed.
