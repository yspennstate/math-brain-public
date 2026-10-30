SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-24T04:36:26Z.
attacking: same-sign transverse-curvature localization and the exact opposite-sign Schur-cancellation barrier, with zero translation/support/moment tax.

# QFORM fleet03/B14 — definite physical-pair localization

Run: `20260924T043626Z-fleet03-B14-QFORM-auto11`.
Status: `SUPPORTING_THEOREM_PROVED / INTERMEDIATE_BARRIER_PROVED / FULL_QFORM_OPEN / FULL_TARGET_CONTINUITY_OPEN`.

## 1. Exact target and scope

The owner target remains: for independent real coordinates with marginal densities at most one and symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal essential density bound for `X^T A X`, or give a valid counterexample. No moment, compact-support, connected-support, log-concavity, Gaussian, or eigen-coordinate independence hypothesis is used below.

The theorem proved here is a supporting localization chamber. It does not derive a good physical pair from the bare spectral hypothesis.

## 2. Main theorem: definite physical pair, exact determinant cost

### Theorem `QFORM-DEFINITE-PHYSICAL-PAIR-ZERO-TAX-LOCALIZATION-v1`

Let `A` be any real symmetric `n x n` matrix. Suppose two original coordinates, after permutation the first two, form a definite principal block

`B = [[a,c],[c,b]]`,

so `det(B)=ab-c^2>0` and `a,b` have the same sign. Let `X=(W,U,Y)` have independent coordinates, with `||p_W||_infinity<=K_W`, `||p_U||_infinity<=K_U`; no restriction beyond probability-law measurability is needed on the outside independent bank `Y` for the conditional argument. Then

`||p_{X^T A X}||_{infinity,ess} <= pi K_W K_U / sqrt(det B)`.

In particular, for the QFORM cap-one class,

`boxed: ||p_{X^T A X}||_{infinity,ess} <= pi / sqrt(det B)`.

The constant is uniform over dimension, every outside quadratic block, every active-outside coupling, all conditioning-generated affine translations, arbitrarily distant/countable fragments, unbounded supports, and all moments/tails.

### Proof

Write, after conditioning on the outside original coordinates `Y=y`,

`Q_y(w,u)=a w^2 + 2cwu + b u^2 + 2 r_1(y) w + 2 r_2(y) u + k(y)`.

Because `B` is definite, `a!=0` and

`d := b-c^2/a = det(B)/a`

has the same sign as `a`.

Complete only the `w` square:

`Q_y(w,u)=a (w + (c/a)u + r_1(y)/a)^2 + d u^2 + 2 e(y)u + k_1(y)`,

where `e(y)=r_2(y)-c r_1(y)/a`. Completing the scalar `u` square gives

`Q_y(w,u)=a (w+Phi_y(u))^2 + d (u+theta_y)^2 + k_2(y)`

for deterministic `theta_y,k_2(y)` and an affine `Phi_y(u)`. The first square's center is allowed to depend on the same transverse coordinate `u`; this is the overlap that a rotation would mishandle.

It is enough to prove the estimate when `a,d>0`; the negative-definite case follows by reflecting the output. Fix `y` and `q`. Conditional on `U=u`, the pushforward of `W` by

`w -> a(w+Phi_y(u))^2`

has density bounded by

`K_W / (sqrt(a) sqrt(v))` for `v>0`,

independently of the translation `Phi_y(u)`. Therefore, with `s=q-k_2(y)`,

`p_{Q_y}(q) <= (K_W/sqrt(a)) int p_U(u) 1_{d(u+theta_y)^2 < s} / sqrt(s-d(u+theta_y)^2) du`.

If `s<=0` the right side is zero. If `s>0`, use `p_U<=K_U` and translate `u`:

`p_{Q_y}(q) <= K_W K_U / sqrt(a) * int_{|v|<sqrt(s/d)} dv / sqrt(s-dv^2)`

`= pi K_W K_U / sqrt(a d)`

`= pi K_W K_U / sqrt(det B)`.

This is uniform in `y`. Averaging the conditional laws over the arbitrary outside product law preserves the same interval estimate and hence the same essential density cap. No normalization of spatial fragments occurs.

The proof also covers arbitrary deterministic affine perturbations of the full quadratic form, because they only change the conditional translations above.

## 3. More general overlap form

The same calculation proves the following reusable formulation. Let `W,U,Z` be mutually independent, with density caps `K_W,K_U`. Let `a,d` be nonzero and of the same sign. For arbitrary measurable `Phi(U,Z)`, arbitrary measurable shift `theta(Z)`, and arbitrary measurable residual `R(Z)`,

`T = a (W+Phi(U,Z))^2 + d (U+theta(Z))^2 + R(Z)`

satisfies

`||p_T||_{infinity,ess} <= pi K_W K_U / sqrt(|a d|)`.

Thus an arbitrary random affine slope `D(Z) U` in a same-sign transverse curvature `d U^2` costs zero: complete

`dU^2 + D(Z)U = d(U+D(Z)/(2d))^2 - D(Z)^2/(4d)`

and absorb the last term into `R(Z)`. The square vertex of the first resource may still depend arbitrarily on `U` and `Z`.

## 4. Opposite-sign barrier: the random slope can be Schur-cancelled

The preceding same-sign hypothesis is not a cosmetic proof restriction. A random slope with a bounded density does not, by itself, repair an opposite-sign transverse square when the residual quadratic term is allowed to correlate with that slope.

Let `W,U,Z` be independent `Unif[-1/2,1/2]` and set

`Q = W^2 - U^2 + U Z - Z^2/4 = W^2 - (U-Z/2)^2`.

Here the random slope `D(Z)=Z` has density cap one, the square coefficient is `a=1`, the transverse curvature is `d=-1`, and the residual `R(Z)=-Z^2/4` is an admissible quadratic function of the independent slope source.

Put `V=U-Z/2`. Then `V` is independent of `W`, and its density is exactly one on `[-1/4,1/4]`. Hence on the square `0<=w,v<=1/8` the joint density of `(W,V)` is one. For `0<epsilon<1/4096`, take

`2 sqrt(epsilon) <= v <= 1/8`,

`v <= w <= v + epsilon/(3v)`.

Since `epsilon/(3v)<=v/12`, one has `w+v<=3v`, and therefore

`0 <= w^2-v^2 = (w-v)(w+v) <= epsilon`.

Consequently

`P(0<=Q<=epsilon) >= int_{2sqrt(epsilon)}^{1/8} epsilon/(3v) dv`

`= (epsilon/3) log(1/(16 sqrt(epsilon)))`.

The ratio to `epsilon` diverges as `epsilon->0`. Thus `Q` has no essentially bounded density. This does not refute the owner target: the corresponding homogeneous matrix has spectrum `{1,-5/4,0}`, so only two eigenvalues have modulus at least one. It refutes precisely the attempted intermediate extension that would combine an opposite-sign transverse square with only a bounded-density random slope while allowing the Schur-correlated residual.

This barrier identifies what the third spectral resource must prevent: after completing the transverse square, the Schur defect must retain genuine curvature/smoothing instead of collapsing to a rank-two opposite-sign form.

## 5. Actual target-valid chamber and designated partner application

Consider the active three-coordinate block

`A_* = [[2,1,0],[1,2,0],[0,0,-1]]`.

Its spectrum is `{3,1,-1}`, so it exactly satisfies the three-large-eigenvalue target. The definite pair `B=[[2,1],[1,2]]` has `det(B)=3`. Therefore the new theorem yields, for arbitrary independent cap-one inputs and arbitrary outside ambient extension/couplings after conditioning,

`boxed: ||p_Q||_{infinity,ess} <= pi/sqrt(3) = 1.8137993642342178...`.

The designated completed partner result actually applied is fleet04/B14 r10,

`yspennstate/math-open-problems@deb713bc8e6df3f7e0ac5398e8cccbf00d1e7513`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260924T001624Z-fleet04-B14-scaled-schur-localization-r10/REPORT.md`.

For this same physical triple, its minimum absolute eigenvalue is `sigma=1`, so the partner theorem gives the actual inequality

`||p_Q||_{infinity,ess} <= 6 sqrt(pi) = 10.634723105433096...`.

Combining two proved estimates on the same target-valid chamber,

`boxed: ||p_Q||_{infinity,ess} <= min(pi/sqrt(3),6sqrt(pi)) = pi/sqrt(3)`.

The partner theorem is not treated as proving the full conjecture; it is used only in its pinned physical-triple scope.

## 6. Structural consequence and remaining implication

A new paid chamber is now explicit: if some physical pair is definite and

`det A[{i,j}] >= delta^2`,

then the entire ambient form has density cap at most `pi/delta`, regardless of all outside couplings and support geometry. Hence a future structural decomposition may treat only matrices for which every definite physical pair has very small determinant.

What remains unpaid is to derive, from `s_3(A)>=1` alone, either a definite physical pair with determinant bounded below, one of the already-certified three-coordinate/cross-bank chambers, or a genuinely three-resource mechanism that survives the opposite-sign Schur cancellation above. Diffuse target matrices can make all physical pair/triple scales small, so this report does not claim such an extraction.

## 7. Regularity ledger

The theorem establishes absolute continuity and an essential `L^infinity` bound. It does not prove a continuous density representative for arbitrary rough cap-one marginals. Full-target continuity remains open.

## 8. Corrections respected

No pointwise van-der-Corput estimate is used. No rotation of the independent coordinates is used. No bounded-support, connected-support, moment, fragment-count, Gaussian, log-concavity, or interval-extremality assumption is introduced. No fiber-supremum dimension argument is used. The opposite-sign rank-two logarithmic obstruction is explicitly retained as a required control.

Full unrestricted QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`.
