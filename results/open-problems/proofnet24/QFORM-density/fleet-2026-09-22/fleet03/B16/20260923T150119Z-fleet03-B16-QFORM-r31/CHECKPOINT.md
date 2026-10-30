SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B16, 2026-09-23T15:01:19Z.
attacking: the superdiffuse near-coloop survivor by extracting a pivot-uniform half-power of smoothing from the genuine physical hub and the bounded-density star projection, while retaining all dependence between the star and the residual quadratic curvature.

# Early substantive checkpoint — hub phase-space Plancherel

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T150119Z-fleet03-B16-QFORM-r31`.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Full QFORM remains open; continuity is not claimed here.

## New lemma under proof

Let `X` be independent of a random object `Y`, with density `f_X<=L`. Let `S=S(Y)` have a probability density bounded by `M`, while `R=R(Y)` may be arbitrarily dependent on `S`. For any real `a`, define

`Q=a X^2+2 X S+R`.

Then for every `t!=0`,

`|E exp(i t Q)| <= sqrt(pi L M/|t|)`.

Proof: for fixed `t`, set

`F_t(s)=int f_X(x) exp(i t(a x^2+2sx)) dx`.

With Fourier convention `hat g(omega)=int g(x)e^{i omega x}dx`, Plancherel and `omega=2ts` give

`int |F_t(s)|^2 ds = (pi/|t|) int f_X(x)^2 dx <= pi L/|t|`.

Since `phi_Q(t)=E_Y[e^{itR}F_t(S)]`, Cauchy-Schwarz and `p_S<=M` give the displayed estimate. The quadratic self-term `aX^2` is a unit-modulus twist and therefore costs nothing. No conditional projection-density supremum and no pointwise one-dimensional van der Corput estimate is used.

## Target application queued

In fleet03/B16 r29's exact-rank-three true-near-coloop survivor, writing the genuine physical hub as `X_0`,

`Q=A_00 X_0^2+2X_0 S+R(X_{-0})`,
`S=sum_{j!=0} A_0j X_j`,

with `R_*^2=sum A_0j^2>4031/4096`. The established scalar product-projection theorem gives

`||p_S||_infinity <= sqrt(2)/R_*`.

Therefore this lemma gives, uniformly through the null pivot `A_00=0`,

`|phi_Q(t)| <= [pi sqrt(2)/(R_* |t|)]^(1/2)`.

This is only a half-power and does not by itself prove a density. The next calculation is to turn it into an explicit interval-concentration bound and identify exactly what extra half-power must be supplied by the retained rank-two leaf curvature. The logarithmic hyperbola control shows why bounded projection density alone cannot finish the problem.
