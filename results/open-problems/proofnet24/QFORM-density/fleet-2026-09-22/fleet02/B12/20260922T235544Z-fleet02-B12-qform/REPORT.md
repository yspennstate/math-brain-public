SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-22T23:55:44Z.
attacking: localized physical-core shielding under arbitrary dense small tails plus arbitrarily large low-footprint spectral additions; apply the current fleet03/B12 weighted-volume stability theorem and the newest finite-core projected-gradient bound without treating the quadratic tail as a small random perturbation.

# Localized-core shielding, low-footprint large eigenvalues, and quantitative no-pivot tail stability

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260922T235544Z-fleet02-B12-qform`.
Status: `PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and first unpaid implication

The full target remains open: for independent real `X_i` with probability densities at most one and real symmetric `A` with at least three eigenvalues of absolute value at least one, prove one universal essential density bound for `X^T A X`, or give a genuine counterexample.

This run closes a concrete stability obligation but not the extraction problem. The first unpaid implication after the results below is:

> From the bare global hypothesis `s_3(A)>=1`, force either a protected physical three-coordinate core, a protected weighted three-volume packet with row marginal `<3/4`, or the owner’s remaining no-pivot class `N3`, at a universal quantitative scale.

The point is that once either protected certificate exists, arbitrary-rank dense tails of sufficiently small operator norm and arbitrarily large extra spectral additions of sufficiently small physical footprint can be retained **inside the actual final matrix** without any false convolution or post-rotation independence step.

## 2. Source pins actually used

1. Newest Claude package requested by the owner:
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.
   `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` were read. In particular, the completed D/D' volume theorem is stable under extra singular directions and the physical-coordinate method conditions only on original coordinates.

2. Newest finite-core synthesis:
   `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371:proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`.
   Its Theorem 3.1 / Corollary 4.1 gives, in dimension three and with arbitrary affine terms,

   `||p_q||_infinity <= 6 sqrt(pi)/sigma`

   whenever the actual `3x3` quadratic matrix has all singular values at least `sigma>0`. The proof is in original coordinates and permits arbitrary outside spectrum after conditioning.

3. Assigned partner fleet03/B12, latest completed run:
   `yspennstate/math-open-problems@287541ac87d8fa9d977eb1214c8b61e69858bb47:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260922T234350Z-qform-eigenvalue-r20/REPORT.md`.
   Its theorem `QFORM-LOCAL-FOOTPRINT-HYBRID-STABILITY-v1` proves the weighted D' packet branch for arbitrary determinant weights. If supported baseline `3x3` cross minors have singular gap `kappa`, I-side packet marginals are at most `h<3/4`, and the final perturbation footprint on every supported cross minor is `<kappa`, then the final full form has

   `||p_Q||_infinity <= C(h)/(kappa-delta_V)`,

   with `C(h)=6 sqrt(e)` for `h<=1/2`, and
   `C(h)=6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1)` for `1/2<=h<3/4`.
   The outside quadratic term is restored by a dependence-safe mixed-norm shear, not independent convolution.

4. New no-pivot reduction:
   `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371:proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`.
   For fixed `tau`, the full conjecture is reduced to the class `N3(tau)`: actual matrices with three absolute eigenvalues at least one and all `|A_ii|<tau`, `|det A[{i,j},{i,j}]|<tau`.

No arbitrary-joint coarea bound, worst normalized conditional-fiber bound, uniformly good physical minor, or independence after rotation is used.

## 3. Main theorem: localized-core shielding with arbitrary large added eigenvalues

### Theorem 3.1 (`QFORM-LOCALIZED-CORE-SPECTRAL-FOOTPRINT-STABILITY-v1`)

Let `A0` be any real symmetric `n x n` matrix and let `S` be three **original** coordinates such that

`sigma_min(A0[S,S]) >= kappa > 0`.

Let

`A = A0 + T + L`,

where `T` is any symmetric matrix with

`||T||_op <= delta`,

and `L` is any symmetric spectral addition. Write one spectral decomposition

`L = sum_r tau_r v_r v_r^T`,

with orthonormal `v_r` and real `tau_r`, and put

`eta_S(L) = ||L[S,S]||_op`.

Then

`eta_S(L) <= sum_r |tau_r| ||(v_r)_S||_2^2`.

If

`Delta := delta + eta_S(L) < kappa`,

then for every independent cap-one product input and every affine term,

`||p_(X^T A X + b^T X + c)||_infinity <= 6 sqrt(pi)/(kappa-Delta)`.      (3.1)

All coefficients outside `S x S`, including all other eigenvalues and all cross couplings, are unrestricted. The added eigenvalues `tau_r` may have either sign and arbitrarily large magnitude; only their actual physical footprint on the protected triple is charged.

#### Proof

Compression cannot increase operator norm, so

`||T[S,S]||_op <= delta`.

For each rank-one term,

`||(tau_r v_r v_r^T)[S,S]||_op = |tau_r| ||(v_r)_S||_2^2`.

Therefore

`||(T+L)[S,S]||_op <= Delta`.

Weyl’s singular-value inequality gives

`sigma_min(A[S,S]) >= kappa-Delta =: gamma > 0`.               (3.2)

Now condition on all original coordinates `X_(S^c)=z`. The three variables `X_S` remain independent with their original density caps. The conditional polynomial has quadratic matrix exactly `A[S,S]`; every cross term to `S^c` becomes only an arbitrary deterministic affine term in `X_S`. Corollary 4.1 of the newest finite-core synthesis, in dimension three, applies uniformly in this affine term and gives the conditional density cap

`6 sqrt(pi)/gamma`.

Averaging the conditional interval bound over `z` proves (3.1). The outside quadratic term is never separated as an independent random variable. QED.

### Remark 3.2: this is stronger than the partner’s physical-triple constant

The current fleet03/B12 partner theorem gives `20/(kappa-delta_P)` on the same physical-triple branch. The source-pinned dimension-three projected-gradient theorem improves this branch to `6 sqrt(pi)/(kappa-delta_P)`, with

`6 sqrt(pi) = 10.6347231054... < 20`.

The partner’s **weighted volume branch**, however, has no analogue in the finite-core theorem and is used below.

## 4. Partner application: weighted cross-volume packets survive the same tail/spike decomposition

### Corollary 4.1 (`QFORM-WEIGHTED-PACKET-SPECTRAL-FOOTPRINT-COROLLARY-v1`)

Let `I,J` be disjoint original-coordinate sets. Suppose a probability packet `w` of baseline `3x3` cross minors `(S,T)` satisfies

`max_i P_w(i in S) <= h < 3/4`

and every supported baseline minor obeys

`sigma_min(A0[S,T]) >= kappa`.

For the same decomposition `A=A0+T+L`, define

`Delta_V := delta + max_(w_ST>0) sum_r |tau_r| ||(v_r)_S||_2 ||(v_r)_T||_2`.

If `Delta_V<kappa`, then the completed fleet03/B12 weighted D' theorem gives the **actual final form** a continuous density with

`||p_(X^T A X+b^T X+c)||_infinity <= C(h)/(kappa-Delta_V)`,       (4.1)

where

`C(h)=6 sqrt(e)` for `h<=1/2`,

and

`C(h)=6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1)` for `1/2<=h<3/4`.

#### Proof

For each supported `(S,T)`,

`||T[S,T]||_op <= delta`,

and

`||L[S,T]||_op
 <= sum_r |tau_r| ||(v_r)_S||_2 ||(v_r)_T||_2`.

Thus the partner theorem’s cross-footprint is at most `Delta_V`. Rectangular Weyl gives final supported minor gap at least `kappa-Delta_V`. Apply `QFORM-LOCAL-FOOTPRINT-HYBRID-STABILITY-v1`, Branch V, to the final matrix. QED.

This is a real application of the assigned partner result. It shows that an arbitrary-rank dense tail is paid by operator norm, while arbitrarily large additional eigenvalues are paid only through their overlap with the protected determinant packet.

## 5. Exact target-class stress family: an unbounded fourth eigenvalue plus an arbitrary dense tail

The preceding theorem is non-vacuous even when the added eigenvalue tends to infinity.

Fix `n>=12`. Let

`u1=(e1-e4)/sqrt(2)`,
`u2=(e2-e5)/sqrt(2)`,
`u3=(e3-e6)/sqrt(2)`,

and let

`v=n^(-1/2)(1,...,1)^T`.

The four vectors `u1,u2,u3,v` are orthonormal. Define

`A0 = 2 u1 u1^T + 2 u2 u2^T - 2 u3 u3^T`,

`Astar = A0 + tau v v^T`.

Then exactly

`spec(Astar) = {2,2,-2,tau,0,...,0}`.                         (5.1)

Thus `tau` is a literal additional spectral eigenvalue, of either sign and arbitrary magnitude. On the physical triple `S={1,2,3}`,

`A0[S,S] = diag(1,1,-1)`,

so `kappa=1`, while

`||(tau v v^T)[S,S]||_op = |tau| ||v_S||_2^2 = 3|tau|/n`.      (5.2)

Now add **any** symmetric dense tail `T` with

`||T||_op <= 1/4`.

If

`|tau| <= n/12`,

then the physical footprint is at most

`Delta <= 1/4 + 3(n/12)/n = 1/2`.

Theorem 3.1 therefore gives

`||p_(X^T(Astar+T)X)||_infinity <= 12 sqrt(pi)
 = 21.2694462109...`.                                         (5.3)

Moreover, before the small tail `Astar` has three singular values exactly two, so after the tail

`s_3(Astar+T) >= 2-1/4 = 7/4 > 1`.                            (5.4)

Hence every matrix in (5.3) lies in the exact target class. Taking `tau=+n/12` or `tau=-n/12` gives a fourth eigenvalue whose magnitude tends to infinity with `n`, while the universal density bound (5.3) is independent of `n` and of the tail’s rank, signs, orientation, and outside couplings.

This supplies a concrete source-valid arbitrary-larger-eigenvalue stability family rather than an abstract perturbation slogan.

## 6. Quantitative stability of the remaining no-pivot class under dense tails

The newest geometric synthesis reduces the full theorem to one class `N3(tau)`. A useful complementary fact is that this class itself is stable, with an explicit threshold loss, under a genuinely dense small operator-norm tail.

### Lemma 6.1 (`QFORM-NOPIVOT-DENSE-TAIL-STABILITY-v1`)

Say a symmetric matrix `B` is `no-tau-pivot` if

`|B_ii|<tau`,

`|B_ii B_jj-B_ij^2|<tau` for all `i!=j`.

Then every off-diagonal entry satisfies

`|B_ij| < r_tau := sqrt(tau+tau^2)`.                           (6.1)

If `A=B+E` with symmetric `||E||_op<=delta`, then

`|A_ii| < tau+delta`,                                         (6.2)

and every physical `2x2` principal determinant satisfies

`|A_ii A_jj-A_ij^2|
 < tau + 2 delta(tau+r_tau)+2 delta^2`.                        (6.3)

Consequently `A` is `no-hat_tau-pivot` for every

`hat_tau > max{tau+delta,
               tau+2 delta(tau+sqrt(tau+tau^2))+2 delta^2}`.  (6.4)

Also

`s_3(A) >= s_3(B)-delta`.                                     (6.5)

#### Proof

From the no-pivot inequalities,

`B_ij^2 <= |B_ii B_jj| + |B_ii B_jj-B_ij^2|
          < tau^2+tau`,

which proves (6.1). Since every entry of a matrix is bounded by its operator norm in absolute value, `|E_ij|<=delta`, giving (6.2). For a pair `i,j`, write `b_i=B_ii`, `b_j=B_jj`, `b=B_ij`, and `e_i,e_j,e` for the corresponding entries of `E`. Then

`det A_{ij}-det B_{ij}
 = b_i e_j+b_j e_i+e_i e_j-2be-e^2`.

Thus

`|det A_{ij}-det B_{ij}|
 <= 2 tau delta + 2 r_tau delta + 2 delta^2`,

proving (6.3)-(6.4). Equation (6.5) is Weyl’s singular-value inequality. QED.

### Concrete reduction

Take

`tau=1/16`, `delta=1/64`.

Then

`r_tau=sqrt(17)/16`,

`tau+delta=5/64<1/8`,

and

`tau+2delta(tau+r_tau)+2delta^2
 = (133+4sqrt(17))/2048
 < 1/8`.

Therefore

> every no-`1/16`-pivot matrix `B` with `s_3(B)>=65/64`, after **any** symmetric dense tail `E` of operator norm at most `1/64`, becomes a no-`1/8`-pivot target matrix.

Hence a future proof of the single owner reduction `N3(1/8,C0)` would automatically give the same density cap `C0` on this whole dense-tail neighbourhood. No random-variable perturbation estimate is needed; one simply verifies that the **actual final matrix** remains in the N3 class.

This reduction is complementary to fleet03/B12: their theorem stabilizes already-good physical or volume certificates; Lemma 6.1 stabilizes the complementary **absence** of one- and two-coordinate pivots.

## 7. Why small matrix norm is not a small quadratic random perturbation

For completeness, the forbidden shortcut fails in the strongest elementary way. Fix any `delta>0`, let

`E=delta e_1 e_1^T`,

and take `X_1` uniform on `[R,R+1]` (density exactly one). Then

`X^T E X = delta X_1^2 >= delta R^2` almost surely.

As `R` grows, the allegedly “small” quadratic perturbation becomes arbitrarily large despite `||E||_op=delta`. Therefore none of the arguments above compares `X^T(A0+E)X` to `X^T A0 X` pointwise or convolves them as if independent. The tail is retained in the actual physical blocks or actual N3 inequalities.

## 8. What this does and does not settle

**Proved here.** A protected physical triple survives arbitrary-rank dense tails and arbitrary signed added eigenvalues with small local spectral footprint, with the sharper cap `6sqrt(pi)/(gap)`. The assigned partner’s weighted-volume theorem yields the analogous packet result. An exact family with spectrum `{2,2,-2,tau,0,...}` and `|tau|~n` remains uniformly controlled after an arbitrary dense operator-norm-`1/4` tail. The no-pivot class has an explicit dimension-free threshold stability modulus under dense tails.

**Not proved.** The bare assumption `s_3(A)>=1` has not been shown to force a protected triple or packet. `N3` itself remains unproved. Therefore the full target remains `OPEN / NOT PROVED / NOT DISPROVED`.

**Next mathematical step.** In the final no-pivot class, use the entry bound `|A_ij|<sqrt(tau+tau^2)` together with exterior-cube mass `e_3(A^2)>=1` to force an aggregate disjoint/minor packet before taking reciprocal local costs, or prove directly that the overlap-two mass is payable by a grouped original-coordinate product estimate. The known singleton-plus-two-banks examples show why selecting one minor or one rank-three cross cut cannot be the whole argument.
