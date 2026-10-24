# account02/B17 — one-heavy mixed-leverage no-escape and exact two-heavy control

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Run:** B17-20260922T181037Z-r11  
**Assignment:** Sharp constant and witnesses  
**Status:** SUBSTANTIVE SHARP-WITNESS EXCLUSION / FULL CONJECTURE OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. Target and source status

The unrestricted target remains: for every dimension, every product law of independent real coordinates with one-dimensional densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal finite essential-density bound for `Q=X^TAX`, or give a valid counterexample. No moment, centering, identical-law, compact-support, log-concavity, or eigenbasis-independence assumption may be inserted.

Fresh brain control at start was `yspennstate/math-research-brain@99b5c53603ff0f8d0ae6e8dab890f4fe94ba7688`, OWNER CONTROL revision `2026-09-22.11`. Before publication, main was refreshed through `2b995c0ba388ed88d33028547e5b0e966f4d94ea`; no protected-control change or later B17 stop occurred in that interval. The live mathematical corrections refuting arbitrary-joint coarea bounds, positive conditional projection moments, and scalar-`Q_rest` worst-condition bounds were consumed. None is used below.

This run attacks a remaining sharp-witness escape left after the designated partner's fixed-frame and finite-dimensional analyses: one genuinely non-infinitesimal physical coordinate, with an arbitrary cap-one law and arbitrary spectral orientation, coupled to a diffuse rank-three completion. The main result is that this canonical mixed-leverage mechanism still cannot asymptotically raise the zero-density above `3 sqrt(2)`.

## 2. Partner result actually applied

The designated partner `account03/B17` completed the source-pinned run

- brain handoff: `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account03/B17/20260922T180732Z-account03-B17-QFORM-r14.md`;
- mathematics: `yspennstate/math-open-problems@0fe842ad60b590ca774ecfd71cf2bb9d15639f90`;
- report: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260922T180732Z-account03-B17-QFORM-r14/REPORT.md`.

It proves an exact six-variable rotated witness with peak

`4.06307061680603726012548442259... < 3 sqrt(2)`

and, by an exact bathtub argument, proves that arbitrary **one-coordinate fragmentation** cannot improve its prior cross witness when the other five laws remain centered unit intervals. Thus a stronger finite witness must coordinate at least two law changes, use a different orientation, or enter a growing/multiscale architecture. I use that conclusion to move to a genuinely different mixed-leverage construction rather than repeat a one-coordinate fragment swap. I also use its exact `4.0630706...` value as the finite benchmark in Section 7.

The preceding partner run `account03/B17` at `math-open-problems@3bb57a5517de87855824e393ec1601b8921abc13` proved that every **fixed finite tight-frame pattern repeated diffusely with centered unit intervals** approaches `3 sqrt(2)` from below, with a strictly negative first Edgeworth correction. The present theorem covers a complementary canonical regime in which one row does **not** become diffuse and its physical law is completely arbitrary subject only to the density cap.

## 3. A sharp cap-one square-Laplace inequality

### Lemma 3.1 — cap-one bathtub Gaussian bound

If `X` is any real random variable with probability density `f_X<=1`, then for every `a>=0`,

`E exp(-a X^2) <= int_{-1/2}^{1/2} exp(-a x^2) dx <= (1+a/6)^(-1/2)`.

No centering, symmetry, connected support, or moment hypothesis is used.

**Proof.** The first inequality is the one-dimensional bathtub/rearrangement principle: among all `0<=f<=1` of integral one, a symmetric strictly decreasing function of `|x|` is maximized by `f=1_{[-1/2,1/2]}`.

For the second inequality set `y=sqrt(a)/2`. The desired inequality is

`erf(y) <= (2y/sqrt(pi)) (1+2y^2/3)^(-1/2)`.

Both sides vanish at `y=0`. The derivative of the right side is

`(2/sqrt(pi))(1+2y^2/3)^(-3/2)`,

while the derivative of `erf(y)` is `(2/sqrt(pi)) exp(-y^2)`. Since

`(3/2) log(1+2y^2/3) <= y^2`

by `log(1+t)<=t`, the derivative of the right side is at least that of the left side. Integrating from zero proves the claim. ∎

### Corollary 3.2 — Gaussian square-Laplace domination after one heavy coordinate

Fix `ell in [0,1]`. Let `G~N(0,1)` be independent of `X` and define

`H = sqrt(12 ell) X + sqrt(1-ell) G`.

Then for every `s>=0`,

`E exp(-s H^2) <= (1+2s)^(-1/2) = E exp(-s G_0^2)`,

where `G_0~N(0,1)`.

**Proof.** Put `D=1+2s(1-ell)`. Conditioning on `X`,

`E_G exp[-s(sqrt(12ell)X+sqrt(1-ell)G)^2]`

`=D^(-1/2) exp[-(12 ell s/D)X^2]`.

Lemma 3.1 with `a=12 ell s/D` gives

`<=D^(-1/2)(1+2 ell s/D)^(-1/2)=(1+2s)^(-1/2)`. ∎

This is the decisive unpaid implication for the one-heavy mechanism: a cap-one physical coordinate cannot make the relevant square-Laplace transforms larger than the variance-minimizing centered Gaussian calibration once the complementary Gaussian variance is included.

## 4. Exact cone kernel is completely monotone in the heavy square

Let

`q(z)=z_1^2+z_2^2-z_3^2`

and fix an arbitrary unit vector `u in S^2`. Let `G_perp` be a standard two-dimensional Gaussian on the plane `u^perp`, independent of the scalar `h`, and define

`k_u(h) = density at 0 of q(h u + G_perp)`.

The following exact representation keeps the spectral orientation completely arbitrary.

### Lemma 4.1 — positive square-exponential mixture

Let `theta` be uniform on `[0,2pi)` and `sigma` uniform on `{+1,-1}`, independently, and set

`d(theta,sigma)=(cos theta, sin theta, sigma)`, `A=u dot d(theta,sigma)`.

Then, for `h!=0` and by monotone extension at `h=0`,

`k_u(h) = (1/2) E_A [ |A|^(-1) exp{-h^2(1/A^2-1/2)} ]`.

Since `|A|<=|d|=sqrt(2)`, every rate

`s_A = 1/A^2-1/2`

is nonnegative. Hence `k_u(h)` is a positive mixture of functions `exp(-s h^2)`: it is completely monotone as a function of `h^2`.

**Proof.** Use the exact cone delta formula

`int F(z) delta(q(z)) dz = (1/2) sum_{sigma=+/-1} int_0^{2pi} int_0^infinity F(r d(theta,sigma)) dr dtheta`.

For a standard three-dimensional Gaussian `Z`, resolve jointly the constraints `q(Z)=0` and `u dot Z=h`. The second delta function gives `r=h/A`, restricted to `hA>0`, and a Jacobian `1/|A|`. Dividing the resulting joint density by the standard-normal marginal density of `u dot Z` gives

`k_u(h)=(1/(4pi)) sum_sigma int_{hA>0}|A|^(-1) exp[-h^2(1/A^2-1/2)] dtheta`.

The law of `A` is symmetric, so the half-space restriction contributes exactly one half of the full expectation, giving the displayed formula. ∎

### Corollary 4.2 — orientation-uniform `3 sqrt(2)` limit bound

For `H` from Corollary 3.2,

`E k_u(H) <= 1/(2 sqrt(2))`

for every unit orientation `u` and every `ell in [0,1]`.

**Proof.** Tonelli is legitimate because the mixture is nonnegative. Apply Corollary 3.2 rate-by-rate:

`E k_u(H) <= (1/2) E_A [ |A|^(-1)(1+2s_A)^(-1/2) ]`.

But `1+2s_A=2/A^2`, so the integrand is identically `1/sqrt(2)` wherever `A!=0`; the null set `A=0` is harmless by monotone interpretation. Hence the result is `1/(2sqrt(2))`. ∎

Notice what is **not** used: there is no arbitrary-joint-density coarea estimate and no conditional density-cap claim. The proof first keeps the exact Gaussian conditional cone kernel, then uses only the original cap-one one-dimensional source through Lemma 3.1.

## 5. Exact source-valid one-heavy stress family

Fix any `u in S^2`, any leverage `ell in [0,1]`, and complete `u` to an orthonormal basis `{u,v,w}` of `R^3`. For each `m>=1`, let `R_m` be the `(1+3m) x 3` matrix whose rows are

- one heavy row `sqrt(ell) u`;
- `m` rows `sqrt((1-ell)/m) u`;
- `m` rows `m^(-1/2) v`;
- `m` rows `m^(-1/2) w`.

Then exactly

`R_m^T R_m = ell uu^T+(1-ell)uu^T+vv^T+ww^T=I_3`.

Let `Lambda=diag(1,1,-1)` in the fixed spectral eigenbasis and set

`A_m=R_m Lambda R_m^T`.

Therefore, for every finite `m`,

`spec_nonzero(A_m)={1,1,-1}`.

This is an exact target matrix, not an asymptotic spectral approximation.

Take the physical coordinates independent. The heavy coordinate `X_0` has an **arbitrary** density bounded by one. Every other physical coordinate is `Unif[-1/2,1/2]`. Put

`Y_m=R_m^T X`, `Z_m=sqrt(12)Y_m`.

If

`S_m=(sqrt(12)/sqrt(m)) sum_{r=1}^m U_r`, `U_r iid Unif[-1/2,1/2]`,

then, in the `{u,v,w}` basis,

`Z_m = H_m u + S_m' v + S_m'' w`,

where the three scalar terms are independent,

`H_m=sqrt(12 ell)X_0+sqrt(1-ell)S_m`,

and `S_m',S_m''` are independent copies of `S_m`. Hence

`Z_m ==> Z_infty = H u + G_v v + G_w w`,

with `H=sqrt(12ell)X_0+sqrt(1-ell)G_u` and three independent standard Gaussians in the limiting decomposition.

Finally

`X^T A_m X = Y_m^T Lambda Y_m = q(Z_m)/12`.

## 6. Local density convergence at the cone and the no-escape theorem

Weak convergence alone is not enough to compare point densities, so the pointwise limit is justified directly.

Let `s_m` denote the density of `S_m`. The standard local CLT for bounded continuous summands gives

`||s_m-phi||_infinity ->0`, `||s_m-phi||_1->0`,

and `sup_m ||s_m||_infinity<infinity` after absorbing finitely many initial values. For `0<ell<1`, the density `h_m` of `H_m` is the convolution of the scaled cap-one heavy law with the scaled `s_m`; convolution contraction gives uniform and `L^1` convergence to the density `h` of `H`, together with a finite uniform cap. The endpoint cases `ell=0` and `ell=1` are immediate from `s_m` itself and the fixed scaled cap-one heavy density, respectively.

Parameterize the cone by `d(theta,sigma)` as above and write its coordinates in the `{u,v,w}` basis as

`a_u=u dot d`, `a_v=v dot d`, `a_w=w dot d`.

The exact coarea representative at zero is

`p_{q(Z_m)}(0)`

`=(1/2) sum_sigma int_0^{2pi} int_0^infinity h_m(r a_u)s_m(r a_v)s_m(r a_w) dr dtheta`.

For every cone direction,

`a_u^2+a_v^2+a_w^2=|d|^2=2`,

so at least one coefficient has magnitude at least `sqrt(2/3)`. If all three one-dimensional densities are bounded by `M`, choosing such a largest coefficient gives

`int_0^infinity h_m(r a_u)s_m(r a_v)s_m(r a_w) dr <= M^2 sqrt(3/2)`.

This is an angularly integrable bound independent of `m`. Radial convergence follows from the uniform/`L^1` convergence of the one-dimensional densities: choose a largest coefficient, use its `L^1` convergence for the corresponding factor and uniform convergence for the other factors, and telescope the product. Dominated convergence in `theta` therefore yields

`p_{q(Z_m)}(0) -> p_{q(Z_infty)}(0)=E k_u(H)`.

Combining this with Corollary 4.2 and the scale factor `Q=q/12` proves the main result.

### Theorem 6.1 — QFORM-ONE-HEAVY-DIFFUSE-NOESCAPE-v1

For the exact source-valid family above, for every spectral orientation `u`, every fixed leverage `ell in [0,1]`, and every heavy-coordinate law with density bounded by one,

`lim_{m->infinity} p_{X^T A_m X}(0) <= 3 sqrt(2)`.

The bound is sharp within this mechanism at `ell=0`, where the family reduces to the standard diffuse Gaussian-limit construction and the limit is exactly `3sqrt(2)`.

This theorem is a sharp-witness exclusion, **not** a universal upper bound for all QFORM matrices or all output levels. It does not rule out finite-`m` overshoot, multiple non-infinitesimal rows, growing nonorthogonal row patterns, higher-rank spectral interactions, or a peak away from zero.

## 7. Exact two-heavy collinear control

The next simplest escape has two non-infinitesimal rows. One exact control can also be evaluated in closed form.

Take two physical rows `e_3/sqrt(2)` on the negative eigendirection, and use two diffuse positive banks consisting of `m` copies of `e_1/sqrt(m)` and `e_2/sqrt(m)`. Again `R_m^TR_m=I_3`, so `A_m=R_m diag(1,1,-1)R_m^T` has exact nonzero spectrum `{1,1,-1}` for every `m`. Let all physical inputs be centered unit intervals.

In standardized coordinates the limiting negative component is

`H=(V_1+V_2)/sqrt(2)`, `V_i~Unif[-sqrt(3),sqrt(3)]`,

while the positive components are independent standard Gaussians. Conditional on `H=h`, `G_1^2+G_2^2` is `chi_2^2`, so the density of `G_1^2+G_2^2-H^2` at zero is `(1/2)e^{-h^2/2}`. The triangular density of `H` gives

`E e^{-H^2/2}`

`= -1/3 + e^{-3}/3 + [sqrt(3pi)/3] erf(sqrt(3))`.

Hence the physical quadratic-form zero-density converges to the exact constant

`C_2 = -2+2e^{-3}+2sqrt(3pi) erf(sqrt(3))`

`    = 4.1516968595129935...`

which still satisfies

`C_2 < 3sqrt(2)=4.242640687119285...`

by a gap `0.090943827606292...`.

This exceeds the partner's new exact six-variable benchmark `4.063070616806037...` by about `0.08862624`, so mixed leverage can move finite/limiting benchmarks upward without yet beating the diffuse `3sqrt(2)` scale. This is only one two-heavy geometry; it is not a two-heavy no-escape theorem.

## 8. Consequences for the sharp-witness search

The source-valid witness landscape is now narrower:

1. Partner account03/B17: every fixed repeated shared-coordinate tight-frame architecture with centered unit intervals approaches `3sqrt(2)` from below.
2. Partner account03/B17: the best new exact six-variable benchmark is `4.0630706...`, and one-coordinate arbitrary fragmentation cannot improve the prior cross geometry.
3. This run: one arbitrary cap-one non-infinitesimal coordinate plus the canonical diffuse rank-three completion has limiting zero peak at most `3sqrt(2)`, uniformly in its leverage and spectral orientation.
4. This run: a symmetric two-heavy collinear exact family reaches `4.1516968...` but remains below `3sqrt(2)`.

Therefore a witness above `3sqrt(2)`, if one exists, must leave at least one of these regimes. The most credible next B17 stress mechanisms are:

- two or more **non-collinear** heavy rows with coordinated cap-one fragmented laws;
- a finite/mesoscopic overshoot that disappears in every one-heavy diffuse limit;
- a row architecture whose complexity grows with dimension rather than a fixed-pattern or orthogonal-bank completion;
- interaction with additional spectral directions beyond exact rank three.

The first of these is now the highest-value sharp-witness attack: optimize a two-heavy non-collinear frame with the remaining covariance supplied diffusely, and use the same positive cone-kernel representation to test whether the two-dimensional cap-one product source can ever dominate the standard Gaussian cone average.

## 9. Scope and correction compatibility

The unrestricted conjecture remains **OPEN / NOT PROVED**. Nothing here asserts that `3sqrt(2)` is the universal sharp constant. The theorem concerns a precise exact target family and the zero-density limit.

The proof is compatible with all live corrections read in this run:

- it does not use a law-uniform pointwise Fresnel decay;
- it does not use an arbitrary-joint `L^infinity` coarea lemma;
- it does not condition on a high-dimensional complement and take positive moments of conditional projection caps;
- it does not condition on scalar `Q_rest` and demand a uniform worst-conditioned density;
- it retains original-coordinate product provenance throughout.

The cone calculation is used only for the explicit Gaussian conditional kernel, where the positive mixture is exact.

## 10. Reproducibility

`CHECK.py` in this immutable run directory checks the elementary error-function envelope on a wide logarithmic grid as a numerical sanity test (the proof is analytic), evaluates the exact two-heavy constant, and compares it with `3sqrt(2)` and the source-pinned partner benchmark. `CHECK_OUTPUT.txt` records the output. Numerical checks are not used as proof of Lemma 3.1 or Theorem 6.1.
