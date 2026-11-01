# F0081 attempt — 2026-10-11

**Second-attempt update:** [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md) proves the upper tail bound C_d r^(-d/2) in every dimension and, using the source lower theorem, the complete positive-moment criterion in d=2. The remaining gap is critical-moment divergence in d>=3. Sections 1-7 preserve the first attempt; statements below that no unconditional bound was improved describe that earlier stage.

## Exact target and verdict
For each integer d>=2 let R,B be independent intensity-one homogeneous Poisson processes in Euclidean R^d and M their unique stable perfect matching. For a typical red point, X=|x-M(x)|. Prove or refute, for positive alpha, E*X^alpha<infinity iff alpha<d/2. No complete answer was obtained. The results below are reductions and deterministic obstructions, not an improved unconditional tail bound. Their novelty relative to all literature is not asserted.

## 1. Exact residual-charge identity (proved)
For r>0 define R_r={x in R: |x-M(x)|>r} and B_r analogously. Write p(r)=P*(X>r). In a bounded deterministic Borel set Q of diameter at most r let A_r(Q)=#(R_r intersect Q), C_r(Q)=#(B_r intersect Q), and D_r(Q)=A_r(Q)-C_r(Q).

Then, almost surely,
    A_r(Q) C_r(Q)=0,
    |D_r(Q)|=A_r(Q)+C_r(Q),
and
    E D_r(Q)=0,   E|D_r(Q)|=2 |Q| p(r).             (1)

Proof. If x belongs to R_r intersect Q and y belongs to B_r intersect Q, then |x-y|<=r is strictly less than both |x-M(x)| and |y-M(y)|. Also x,y cannot be matched to one another, since that distance is at most r. They therefore form a blocking pair, contradicting stability. Thus at least one of A,C is zero, and the absolute-value identity follows. The intensity of R_r is p(r) by the defining Palm/Campbell formula in the source. The intensity of B_r is also p(r), by exchange of red and blue in the input and uniqueness of the equivariant stable matching. Consequently EA=EC=|Q|p(r). Counts are integrable because bounded above by R(Q)+B(Q). Taking expectations proves (1).

Choose Q_r=[0,r/sqrt(d))^d, with v_r=|Q_r|=d^{-d/2}r^d. Formula (1) holds for this half-open cube, whose supremal diameter is r. The signed residual charge is not the original signed Poisson charge.

## 2. Sufficient fluctuation estimates for a full solution (conditional theorem, proved)
Suppose constants c,C,K>0 and r_0 exist, depending only on d, such that for every r>=r_0,
    c v_r <= E D_r(Q_r)^2 <= C v_r,                  (2)
    E D_r(Q_r)^4 <= K v_r^2.                       (3)
Then positive constants a,b give
    a r^{-d/2} <= p(r) <= b r^{-d/2}, r>=r_0,
and the target positive-moment criterion follows, including divergence at alpha=d/2.

Proof. Mean zero in (1) makes the second moment a variance. Cauchy–Schwarz and (1) give p(r)<=sqrt(C)/(2 sqrt(v_r)). For the other direction apply Hölder with exponents 3/2 and 3 to |D|^{2/3} and |D|^{4/3}:
    E D^2 <= (E|D|)^{2/3} (E D^4)^{1/3}.
If E D^2>0, rearranging gives E|D|>=(E D^2)^{3/2}/(E D^4)^{1/2}. Assumptions (2),(3) give E|D|>=c^{3/2}sqrt(v_r)/sqrt(K). Divide by 2v_r using (1). Since sqrt(v_r)=d^{-d/4}r^{d/2}, the asserted constants exist. For every alpha>0 Tonelli applied to X^alpha=integral_0^X alpha t^{alpha-1}dt gives E*X^alpha=alpha integral_0^infinity t^{alpha-1}p(t)dt. The integral below r_0 is finite. The integral above r_0 has integrand bounded above and below by constant multiples of t^{alpha-1-d/2}; it converges precisely when alpha<d/2. At equality it diverges logarithmically. This proves the conditional theorem.

All bounded-window moments exist at each fixed r, because |D|<=R(Q)+B(Q), a Poisson variable of mean 2v_r. That fact alone gives bounds of order v_r^2 and v_r^4 for the second and fourth moments, respectively, NOT (2),(3). Establishing (2),(3) for growing Q_r is the unresolved probabilistic work. These conditions are sufficient; their necessity for the moment conjecture is not claimed.

There is also an exact equivalent formulation of the moment question, without (2),(3):
    E*X^alpha = (alpha d^{d/2}/2) integral_0^infinity
        r^{alpha-d-1} E|D_r(Q_r)| dr.              (4)
This follows by substitution of (1) in the same nonnegative integral. Thus estimates on the first absolute moment of residual charge would suffice directly.

## 3. Why raw Poisson discrepancy does not prove (2) (proved conservation identity)
Let Z(Q)=R(Q)-B(Q). Define F_r(Q) as the sum over all matched edges (u red, v blue) of length <=r which have exactly one endpoint in Q, with contribution 1_Q(u)-1_Q(v). There are finitely many such edges because each touches a bounded window and each point has one partner. Then
    D_r(Q)=Z(Q)-F_r(Q).                            (5)
Indeed every length<=r internal edge removes one point of each colour and contributes zero signed charge; every short crossing edge removes its sole endpoint's signed charge; all longer edges leave their endpoints in the residual sets. This exhaustive classification proves (5).

The original Z(Q) has second moment 2|Q| and fourth moment 12|Q|^2+2|Q|, since R(Q),B(Q) are independent Poisson variables of mean |Q|. For completeness the cumulant generating function is |Q|(e^t+e^{-t}-2), with second and fourth cumulants both 2|Q|, so the centered fourth moment is 2|Q|+3(2|Q|)^2. This does not control D: F is dependent on Z and is a matching-dependent boundary flux. Bounds on Z cannot be transferred across (5) without bounds on F and its covariance with Z. For Q_r the r-thick boundary neighborhood has volume comparable to v_r, so merely bounding crossing edges by all boundary points loses the desired square-root scale.

## 4. Arbitrarily long stable edge despite a uniformly short alternative (proved deterministic obstruction)
For n>=2 on the real line take red points R_i=8i and blue points B_i=8i+5, i=0,...,n-1. This embeds into every R^d along its first coordinate. In every stable matching the pairs (R_{i+1},B_i), i=0,...,n-2, are forced, with distance 3. The remaining pair (R_0,B_{n-1}) has distance 8n-3. Yet the perfect matching (R_i,B_i) has all distances 5. Consequently stable matching has no universal deterministic constant-factor bound for its maximum edge in terms of the smallest possible maximum edge, even in Euclidean spaces and balanced configurations.

Proof. The signed coordinate difference R_i-B_j is 8(i-j)-5. If i=j+1 the absolute distance is 3. If i<=j, it is at least 5. If i>=j+2, it is at least 11. Hence B_j and R_{j+1} for j<n-1 are each other's unique closest permissible partners. Any matching omitting such a pair gives both endpoints a strictly worse partner (or no partner), hence a blocking pair. All these forced pairs are disjoint. Removing them leaves precisely R_0 and B_{n-1}; perfection forces the claimed final pair. The resulting matching is stable: each internal endpoint has its closest possible partner, so it cannot participate in a blocking pair; the only two endpoints without this property are matched to one another. The alternative matching has every distance exactly 5. The ratio (8n-3)/5 tends to infinity.

The displayed configuration has repeated distances across distinct pairs, but has strict endpoint preferences for the forced pairs. If generic non-equidistance is desired, perturb each coordinate by less than delta<1/4, then choose a generic perturbation avoiding the finitely many distance-equality hypersurfaces. Every forced distance is at most 3+2delta<3.5; every competing distance is at least 5-2delta>4.5. The same forced pairs remain. The final distance is at least 8n-3-2delta, and the alternative maximum is at most 5+2delta. In R^d perturb within delta-balls; the triangle inequality gives the same margins. Thus this is a robust open-set obstruction, not an artefact of ties or exact collinearity.

This construction does not supply a Poisson power-law lower bound. Its probability and isolation cost in an infinite Poisson environment are not estimated at polynomial scale. It refutes a proposed deterministic route only; it is NOT a counterexample to F0081.

## 5. Referee checks and remaining work
Potential failure: use stability without strict preference. Checked: residual distances are >r, while separation is <=r, so the blocking inequalities are strict.
Potential failure: wrong Palm normalization. Checked: red intensity is 1 and blue intensity agrees by colour symmetry, giving the factor 2 in (1).
Potential failure: unbounded random window. Checked: Q_r is deterministic and bounded for each r; all counts and four moments are finite.
Potential failure: infer original Poisson independence after thinning. Rejected explicitly in (5); residual processes are dependent.
Potential failure: infer critical divergence from only exponent d/2+o(1). Rejected: the conditional lower bound is a constant multiple at every large r, giving the actual divergent integral. The exact moment question is (4).
Potential failure: finite simulations silently replace infinite Palm law. Rejected: experiments below are balanced binomial processes on a flat torus, and no infinite-volume conclusion follows.
Potential failure: finite chain ties. Strict closest-partner margins and generic perturbation establish robustness; numerical blocking checks independently verify small cases.

Remaining gap: prove sufficient estimates on E|D_r(Q_r)| in (4), or uniform residual-charge estimates (2),(3), or find a different argument for the moment criterion. In particular, finite residual charges may have scale-dependent spatial correlations; neither their variance upper bound nor the square-root-volume lower bound has been established here. Source Theorem 6 still supplies only its original upper exponent s(d) and d-th-moment divergence (plus Theorem 2 in d=2). No unconditional bound is improved.

## 6. Reproducible finite computations

`experiment.py` uses a full red-blue distance matrix and processes edges in increasing order, accepting an edge if both endpoints are still unused. On a finite balanced configuration this produces a perfect stable matching: an omitted edge had an endpoint already matched via a no-longer edge; with strict preferences this rules out blocking. For the continuous torus samples ties occur with probability zero. Independently, after construction all red-blue pairs were checked for the two strict blocking inequalities.

Integer chain tests used n=2,3,5,10,30, asserting the complete predicted partner array, final edge length 8n-3, and zero blocking pairs.

The random tests used n=2048 red and 2048 blue independent uniform points on a flat torus of volume n, in dimensions 2 and 3, seeds 8100+100*d+seed with seed=0,1,2,3. This is a pair of balanced binomial processes, not independent Poisson counts and not infinite Euclidean space. For partitions into k^d cubes, k=4,8,16, the residual threshold was r=sqrt(d)*L/k. Every cube was checked for no coexistence of residual colours, and the global exact sum identity sum|D|=2*number of long red edges was checked. All assertions passed. Finite-size effects are particularly severe for k=4, where r is a substantial fraction of the torus diameter.

Average descriptive results over four replicates:

| d | k | r | tail | E D^2 / cube volume | E D^4 / volume squared |
|---|---|---|---|---|---|
| 2 | 4 | 16.000000 | 0.00939941 | 0.12133789 | 0.08188057 |
| 2 | 8 | 8.000000 | 0.03308105 | 0.40380859 | 1.05169678 |
| 2 | 16 | 4.000000 | 0.06628418 | 0.42968750 | 1.23748779 |
| 3 | 4 | 5.498919 | 0.01147461 | 0.10839844 | 0.18360901 |
| 3 | 8 | 2.749459 | 0.04565430 | 0.18847656 | 0.48291016 |
| 3 | 16 | 1.374730 | 0.12744141 | 0.31201172 | 1.47363281 |

Runtime: 17.43 seconds. Raw results: experiment_results.json. Distance matrices have 2048^2 double entries (32 MiB); sorting indices and auxiliary arrays keep this job's planned array allocation comfortably below 1 GB. No empirical exponent is estimated from these six scales, and no uniform moment bound is inferred.

## 7. Lean scope

ResidualChecks.lean formalizes five finite arithmetic lemmas: residual one-colour count addition, the internal chain distance, both competing-distance lower bounds, and the endpoint length. It does not formalize Campbell's theorem, Hölder, stability of the whole finite matching, or the infinite Poisson conjecture. The handwritten proofs above are the source for those claims. Only the narrow imports Mathlib.Data.Int.Basic and Lean.Elab.Tactic.Omega are used; no sorry or native_decide. The final compile result is recorded in lean_check.log.

The initial compile attempts exposed missing Mathlib.Tactic.Omega and shell encoding/BOM issues, all local to the input/imports. The final check uses the core Omega module and a UTF-8 file without BOM. The wrapper gives a 3600-second subprocess timeout, as requested for shared Lean checking, and runs only one Lean process at a time. All actual invocations completed well below ten minutes.

## 8. Second attempt: two genuinely different approaches (2026-10-11)

Approach A (selected): use one-point insertion comparative statics, conservation of signed residual charge, and the Poisson Poincare inequality. Rather than estimate dependent boundary flux directly, seek a sharp bound on the add-one difference of residual charge. A finite-volume torus could then transfer the estimate to infinite Euclidean space using descending-chain localization. This was not tried in the first attempt.

Approach B (not selected): expose the stable matching in increasing distance order and express loss of survivor density through a two-point Palm survival probability at separation r. This is a radius-ordered two-species annihilation process. An exact pair-correlation evolution or a controlled annihilation comparison might locate the d/2 exponent. The obstruction is that the opposite-colour two-point Palm law near the moving hard-core boundary is not the product of the survivor densities. A naive mean-field closure would be unproved and potentially wrong.

Brain requests made for the gap itself: 'Poisson stable matching residual charge boundary flux covariance second fourth moment', and 'Harris FKG Poisson association add one cost Poincare inequality stable marriage monotonicity'. The first mostly returned unrelated Gaussian-chaos cards, whose hypotheses do not hold here. The second returned the Harris association card and generic Poincare cards; these are leads, not a substitute for checking the Poisson inequality. Brain recall on covariance mistakes warns against dependence conclusions from conditioning. All new experiments will therefore use independent Poisson counts, not conditioned equal counts, for variance tests.

Finite probe: probe_monotonicity.py tested 4500 independent planar point configurations (n=2,...,10, 500 each), comparing stable partial matchings before and after one red insertion. All old red distances were nondecreasing and all old blue distances nonincreasing. This is numerical evidence only. The proof and the infinite-volume limit are being checked next.

## 9. Second attempt completed

The selected insertion/variance route succeeded in proving the variance upper bound from the first attempt, with constant 2, and therefore the conjectured upper-tail exponent. Full proofs, independent checks, and the precise remaining lower-half gap are in SECOND_ATTEMPT.md sections A-G. The all-dimensions problem is still PARTIAL. For d>=3, proving E*X^(d/2)=infinity would finish the conjectured positive-moment criterion; no proof of this has been obtained. The upper result and d=2 special case are mathematical derivations in this attempt, not claimed as solutions found in print.
