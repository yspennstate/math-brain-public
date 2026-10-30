SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-24T04:04:38Z.
attacking: zero-loss smooth-core reduction for essential height, sharp obstruction to stronger density-level rough-input stability, and an independent audit of the ruled one-sheet rough-input bridge.

# fleet02/B15 — zero-loss smooth-core theorem and sharp majority-sheet stability obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `SMOOTH-CORE-EQUIVALENCE-PROVED / POSITIVE-SUBMEASURE-TV-COMPILER-PROVED / RULED-BRIDGE-RECHECKED / SQRT-STABILITY-SHARP-ON-MAJORITY-SHEET / FULL-QFORM-OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Full-problem status and first unpaid implication

The unrestricted owner target remains OPEN. The central constant is most cleanly expressed without presupposing absolute continuity. For an admissible matrix `A` and cap-one product law `F=prod_i f_i`, write `mu_{A,F}` for the law of `X^T A X`, and define

`H(mu)=sup_{interval I, |I|>0} mu(I)/|I|`.

If `H(mu)<infinity`, then `mu` is absolutely continuous and its essential density height equals `H(mu)` (up to the immaterial choice of open/closed intervals). Thus the owner theorem is exactly the finiteness of

`C_* = sup_{n,A:s_3(A)>=1, f_i<=1} H(mu_{A,F})`.

This run proves that rough-input limiting is not an unpaid part of that final implication: `C_*` is unchanged if every original-coordinate marginal is required to be smooth. The first unpaid implication is therefore structural/analytic already on the smooth cap-one source class: obtain a dimension- and matrix-uniform interval bound, or a valid counterexample. In particular, one still has to remove aggregate-before-inversion losses (including diffuse Schur-bank/log-dimension losses and the no-good-outer-pivot branch) while retaining original-coordinate product provenance.

## 2. Zero-loss smooth-core theorem for the exact owner height

### Theorem 2.1 — `QFORM-ROUGH-SMOOTH-HEIGHT-EQUIVALENCE-v1`

Let `C_rough` be the supremum of `H(mu_{A,F})` over the full owner class. Let `C_smooth` be the same supremum restricted to product laws whose one-dimensional marginals are `C^infinity` probability densities bounded by one. Then

`boxed(C_rough = C_smooth.)`

The inclusion of the smooth class gives `C_smooth<=C_rough`. For the reverse inequality, fix arbitrary admissible `f_1,...,f_n` and a nonnegative probability approximate identity `rho_eta`. Put

`f_i^(eta)=f_i*rho_eta`.

Then

`0<=f_i^(eta)<=1`, `integral f_i^(eta)=1`, and `||f_i^(eta)-f_i||_1 -> 0`.

Writing `F_eta=prod_i f_i^(eta)` and `F=prod_i f_i`, telescoping the product and using that every factor has `L^1` norm one gives

`boxed( ||F_eta-F||_1 <= sum_i ||f_i^(eta)-f_i||_1 -> 0. )`       (2.1)

For every Borel set `B`, deterministic quadratic pushforward contracts total variation:

`|mu_eta(B)-mu(B)| <= integral |F_eta-F| -> 0`.                  (2.2)

If the smooth theorem has constant `C`, then for every fixed interval `I`,

`mu_eta(I)<=C|I|`.

Taking `eta->0` in (2.2) yields

`boxed( mu(I)<=C|I| )`                                          (2.3)

with exactly the same `C`. Since (2.3) for all intervals implies `mu<=C dx`, the rough output has a density with essential height at most `C`. No output continuity, pointwise density convergence, moment bound, support bound, log-concavity, or post-rotation independence appears.

A useful warning is built into the statement: a future smooth-input proof may use smoothness only through estimates uniform in the smoothing parameter. Bounds involving derivative norms, compact-support radii, moments, or a smoothing scale do not survive this reduction unless they disappear before (2.3) is taken to the limit.

## 3. Positive-submeasure version: the rough ruled bridge is also zero-loss

The same argument works before taking the full quadratic pushforward. Let `G` be any fixed measurable event in the original-coordinate sample space and define

`nu_eta(B)=integral 1_G(x) 1_{q(x) in B} F_eta(x) dx`,
`nu(B)=integral 1_G(x) 1_{q(x) in B} F(x) dx`.

Then

`sup_B |nu_eta(B)-nu(B)| <= integral |F_eta-F| -> 0`.             (3.1)

Consequently any smooth estimate

`nu_eta(I)<=C|I|`

passes with the identical constant to the rough submeasure. This is the exact limiting mechanism needed for the ruled majority sheet. It is stronger for the present purpose than proving pointwise convergence of selected density representatives, because it targets the owner inequality itself.

For an ambient form, condition on every coordinate outside an invertible active physical `3x3` block `B`. The conditional polynomial has the form

`Q_w(x)=x^T Bx+2d(w)^T x+c_0(w)`
`       =(x+B^{-1}d(w))^T B(x+B^{-1}d(w))+c(w)`.                 (3.2)

The square completion in (3.2) is a deterministic translation in the three ORIGINAL independent coordinates. Thus the density cap and independence are preserved. If only those active marginals are mollified, the product `L^1` error is still bounded by the sum of their one-dimensional `L^1` errors, uniformly under the conditional translation. Restriction to the conditional majority event and quadratic pushforward then contract total variation by (3.1). Hence a smooth ruled interval bound passes to arbitrary measurable cap-one marginals with zero constant loss.

No continuity is used to obtain essential boundedness here.

## 4. Exact geometric recheck of the owner-pinned ruled theorem

The required source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, together with its `FOURIER_ROUTE_REPORT.md` and `COUNTEREXAMPLE_SEARCH.md`.

For the standard cone

`q_0(z)=z_1^2+z_2^2-z_3^2`

and positive level `s`, use the ruling

`F(theta,t)=sqrt(s)e_theta+t(e_theta^perp+e_3)`.

A direct calculation gives

`F_theta x F_t = (1/2) grad q_0(F)`,

so

`boxed( d sigma / |grad q_0| = (1/2) d theta d t. )`             (4.1)

For spectral magnitudes `(lambda_1,lambda_2,mu)` of a `(+,+,-)` block, undoing the spectral scaling gives ruling direction

`v_theta=(-sin(theta)/sqrt(lambda_1), cos(theta)/sqrt(lambda_2), 1/sqrt(mu))`.  (4.2)

The parameter `t` is not arclength. Therefore the one-dimensional trace along a ruling contributes the indispensable factor `1/|v_theta|`. The two-dimensional product-projection cap is `2`, which cancels the coarea factor `1/2` in (4.1). This reproduces exactly

`C_+ = (lambda_1 lambda_2 mu)^(-1/2)
       integral_0^(2pi) [sin^2(theta)/lambda_1 + cos^2(theta)/lambda_2 + 1/mu]^(-1/2) dtheta`.  (4.3)

The later affine-range correction is harmless whenever the active physical block is invertible, because the conditional affine term lies in the range and (3.2) applies.

## 5. Apply the completed ruled result to an exact target inequality

Take

`boxed( Q=2XY+Z^2 )`                                             (5.1)

with independent cap-one marginals. Its matrix is

`A=[[0,1,0],[1,0,0],[0,0,1]]`

with eigenvalues `{1,-1,1}`. Thus it is exactly on the owner threshold `s_3(A)=1`.

In (4.3), `lambda_1=lambda_2=mu=1`, hence

`C_+= integral_0^(2pi) 1/sqrt(2) dtheta = pi sqrt(2)`.           (5.2)

Therefore the completed source theorem, followed by the zero-loss rough bridge in Sections 2-3, gives for arbitrary rough cap-one marginals

`boxed( P(Q in I, Q>=0) <= pi sqrt(2) |I|. )`                   (5.3)

Equivalently at the triangular-kernel scale,

`boxed( E[(epsilon-|Q-y|)_+ 1_{Q>=0}] <= pi sqrt(2) epsilon^2. )` (5.4)

This is a real essential-density payment. It uses the completed source in its proved one-sheet scope, and it does not invoke continuity.

## 6. Sharp obstruction to replacing the TV bridge by stronger pointwise-density stability

The newest compatible fleet03/B15 result proves fixed-matrix `L^1`-to-output-`L^infinity` stability with exponent `1/2`, and states that exponent is sharp already for (5.1). Here is an independent exact calculation, additionally locating the sharpness entirely on the paid majority sheet.

Let `Y,Z` be iid `Unif[0,1]`. In the `X` coordinate set

`f=1_[0,1]`,
`g=1_[m,1]+1_[2,2+m]`,                                         (6.1)

where `0<m<1/2`. Both are cap-one probability densities and

`delta:=||f-g||_1=2m`.                                          (6.2)

For fixed `x>0`, the conditional density of `2xY+Z^2` at `t` is

`p_x(t)=(1/(2x)) Leb{z in [0,1]: 0<=t-z^2<=2x}`.               (6.3)

Evaluate at `t=2m=delta`. For `0<x<m`,

`p_x(2m)=[sqrt(2m)-sqrt(2(m-x))]/(2x)`,                         (6.4)

while for `2<x<2+m`,

`p_x(2m)=sqrt(2m)/(2x)`.                                        (6.5)

Thus the only pieces surviving in `p_f-p_g` are the deleted interval `[0,m]` and the added interval `[2,2+m]`. Direct integration gives

`integral_0^m p_x(2m) dx = sqrt(2m)(1-log 2)`,                  (6.6)

`integral_2^(2+m) p_x(2m) dx = (sqrt(2m)/2) log(1+m/2)`.        (6.7)

Using `delta=2m`,

`boxed(
 p_f(delta)-p_g(delta)
 = sqrt(delta) [1-log 2 -(1/2)log(1+delta/4)].
)`                                                               (6.8)

Hence

`lim_(delta->0) |p_f(delta)-p_g(delta)|/sqrt(delta)=1-log 2>0`.  (6.9)

In particular, for every `alpha>1/2` there is no finite constant, even for this fixed owner-target matrix, such that

`||p_f-p_g||_infinity <= C ||f-g||_1^alpha`.                    (6.10)

This is stronger than an abstract regularity warning. The sources in (6.1) are nonnegative, so `Q=2XY+Z^2>=0` almost surely. Thus the discrepancy (6.8) occurs wholly inside the same majority/one-sheet submeasure already paid in (5.3). A universal interval cap and only square-root pointwise stability coexist perfectly well.

Consequently the correct rough-input interface for the owner height theorem is the zero-loss total-variation/interval passage of Sections 2-3, not a hoped-for Lipschitz (or better-than-square-root) convergence theorem for output densities.

## 7. Relation to the newest partner theorem

The newest compatible fleet03/B15 theorem is

`yspennstate/math-open-problems@696a0784ba7d270db657c1596d9c2ee940a1745d`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260924T032517Z-fleet03-B15-qform-auto32/REPORT.md`.

For every fixed symmetric `A` of rank at least three and original coordinate `j`, it constructs a finite matrix-dependent `K(A,j)` such that a cap-one subdensity of mass `m` in coordinate `j` produces a `C_0` output subdensity of height at most `K(A,j)sqrt(m)`. It derives

`||p_f-p_g||_infinity <= sqrt(2) K(A,j) ||f_j-g_j||_1^(1/2)`    (7.1)

and uniform output-density convergence under cap-preserving mollification for fixed `A`.

Theorem 2.1 above separates what is and is not needed for the universal conjecture. The fixed-`A` theorem is a strong regularity statement and supplies canonical `C_0` convergence, but a future universal smooth-input interval bound passes to rough inputs without any matrix-dependent `K(A,j)` at all. Formula (6.8) independently checks the partner's sharp exponent and shows why trying to improve (7.1) is not the missing route.

## 8. Absolute continuity, essential boundedness, continuity: implication ledger

1. **Absolute continuity.** If `A!=0` and the joint input is absolutely continuous, `q(x)=x^T A x+b^T x+c` has critical set empty or a proper affine subspace. Local coarea on `{|grad q|>=1/k}`, followed by exhaustion away from the critical set, shows `q_#(F dx)<<dx`. This gives existence of a density and no quantitative height.

2. **Essential boundedness.** The owner target is exactly interval domination `mu(I)<=C|I|`. Sections 2-5 pay and transport such inequalities directly. This is logically prior to continuity.

3. **Continuity.** For fixed `rank(A)>=3`, the newest partner theorem gives a canonical `C_0` density and uniform density convergence under mollification with matrix-dependent constants. This is downstream regularity. It is not used to create any bound in Sections 2-5.

Thus no continuity assumption has been smuggled into the essential-height argument.

## 9. First unpaid continuation

Rough-input limiting is now fully paid at the exact final inequality level. The first unpaid implication is:

`SMOOTH ORIGINAL MARGINALS, s_3(A)>=1  =>  mu(I)<=C|I| with C universal`,

with constants uniform in dimension, matrix geometry, and smoothing scale.

The previous fleet02/B15 continuation already showed that physical-entry inversion can create spurious logarithmic dimension losses on diffuse Schur banks. The next useful step must therefore aggregate a bank/grouped crossing/hub/Schur spectral currency before reciprocating a physical entry or minor, and must also cover the branch in which no quantitatively useful outer physical pair exists. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction remains binding: generic X-ray control of the two-sheet trace is not an admissible substitute.

Full QFORM remains OPEN.
