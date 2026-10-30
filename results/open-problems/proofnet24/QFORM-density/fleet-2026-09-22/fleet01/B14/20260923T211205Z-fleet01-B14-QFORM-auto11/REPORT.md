SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-23T21:12:05Z.
attacking: heat-flow localization — exact constant-preserving mollification of arbitrary cap-one laws, with fragment/location/moment-free Fisher control from fleet02/B14 and a quantitative target-level inequality.

# fleet01/B14 auto11 — exact heat-flow localization of the full QFORM constant

Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.  
Status: **PROVED SUPPORTING LOCALIZATION THEOREM + FULL-TARGET REGULARIZED INEQUALITY / FULL QFORM OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source-valid premises

The target remains: independent real `X_i` with densities `0<=f_i<=1`, symmetric `A` with at least three eigenvalues of modulus at least one, and a universal bound for the density of `X^T A X`. No moments, bounded support, connected support, centering, log-concavity, or post-rotation independence are assumed.


The designated partner result actually used below is fleet02/B14 run `20260923T193835Z-fleet02-B14-QFORM-auto11`, canonical report

`yspennstate/math-open-problems@b2d5f5354dfe179e18e366cf49c485e5326e9288`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T193835Z-fleet02-B14-QFORM-auto11/REPORT.md`.

Its relevant completed statement is the Fisher positive-mixture compiler: Fisher action is mass-homogeneous, convex under positive aggregation, and translation invariant. The underlying projected-Fisher theorem is source-pinned at

`yspennstate/math-open-problems@4a65677d185d35154dc3dfae320c5df9f939b8a2`,
`proofnet24/QFORM-density/interactive/20260923T184054Z-fisher-continuation/FISHER_INFORMATION.md`.

## 2. Density functional and total-variation closure

For a finite Borel measure `mu` on the line define

`D(mu)=sup_{a<b} mu((a,b))/(b-a)`.

If `D(mu)<infinity`, interval domination gives `mu<=D(mu) Leb`, hence `mu` has a density bounded by `D(mu)`; conversely an essentially bounded density gives exactly this interval bound. Thus `D` is the correct extended-valued density constant, including singular laws.

If `mu_k -> mu` in total variation, then for every fixed interval `(a,b)`,

`mu_k((a,b))/(b-a) -> mu((a,b))/(b-a)`.

Taking the supremum over fixed intervals after the limit gives

`boxed{ D(mu) <= liminf_k D(mu_k). }`                                      (2.1)

So the output-density functional is lower semicontinuous for total variation.

## 3. Heat flow preserves the admissible cap exactly

Let

`gamma_t(x)=(2 pi t)^(-1/2) exp(-x^2/(2t))`, `t>0`,

and write `H_t f=f*gamma_t`. If `f` is any probability density with `0<=f<=1`, then

`int H_t f=1`,
`0<=H_t f<=||f||_infinity ||gamma_t||_1<=1`,                              (3.1)

and the standard `L^1` approximate-identity theorem gives

`||H_t f-f||_1 ->0` as `t downarrow0`.                                     (3.2)

No support or moment hypothesis is used. Translations commute with heat flow, and positive fragments are reassembled before convolution:

`H_t(tau_a f)=tau_a H_t f`,
`H_t(sum_j rho_j)=sum_j H_t rho_j`.                                        (3.3)

Hence arbitrary distant/countably many pieces and unbounded supports create no localization parameter.

For finitely many independent coordinates, tensor telescoping yields

`|| tensor_i H_t f_i - tensor_i f_i ||_1
 <= sum_i ||H_t f_i-f_i||_1 ->0`.                                          (3.4)

Pushforward by any Borel map contracts total variation. Therefore, for every Borel `F:R^n->R`, if `X^(t)` has independent marginals `H_t f_i`,

`Law(F(X^(t))) -> Law(F(X))` in total variation.                            (3.5)

This applies in particular to every affine quadratic form

`F(x)=x^T A x+b^T x+c`.                                                     (3.6)

## 4. Exact constant-preserving localization theorem

Define `C_all` to be the supremum of `D(Law(X^TAX))` over every dimension, every admissible cap-one product law, and every symmetric `A` satisfying `s_3(A)>=1`. Define `C_heat` by the same supremum but restrict each marginal to be a common-time heat regularization `H_t f_i` of an arbitrary admissible marginal, with some `t>0`.

Because every heat-regularized marginal is itself admissible,

`C_heat<=C_all`.                                                           (4.1)

Conversely fix any admissible `(A,f_1,...,f_n)`. By (3.5) and (2.1),

`D(Law(X^TAX))
 <= liminf_{t downarrow0} D(Law((X^(t))^T A X^(t)))
 <= C_heat`.                                                               (4.2)

Taking the supremum gives the reverse inequality. Thus

`boxed{ C_all = C_heat }`                                                   (4.3)

including the value `+infinity`.

The identical statement holds for the optimal affine-quadratic constant because the proof used only Borel pushforward. This is `QFORM-HEAT-FLOW-EXACT-CONSTANT-LOCALIZATION-v1`.

**Interpretation.** The full optimal QFORM constant can be studied on real-analytic strictly positive marginals obtained by Gaussian heat flow, with absolutely no tax for translations, fragment separation/count, support diameter, tails, or moments. Unlike a bounded-diameter or fixed-fragment reduction, (4.3) is exact and does not contradict the live localization counterexamples.

## 5. The partner Fisher result gives a full-target regularized bound

The extra gain from the heat model is a law-independent Fisher budget. The fleet02/B14 positive-mixture theorem applied to the Gaussian translation mixture

`H_t f(x)=int gamma_t(x-y) f(y)dy`

gives

`I(H_t f)<=I(gamma_t)=1/t`.                                                (5.1)

This can also be read directly from the partner's formula `I(g*nu)<=I(g)`; here the mixing law is `f(y)dy` and the base shape is `gamma_t`.

Now let `A` be an arbitrary target matrix with at least three eigenvalues of modulus at least one. Select any three corresponding orthonormal eigenvectors and let `U` be their `n x 3` frame. Put

`ell_i=(UU^T)_{ii}`.

No rotation of the random variables is made. The leverage identity is simply

`sum_i ell_i=tr(UU^T)=3`.                                                   (5.2)

For the heat-regularized original-coordinate product law, (5.1) therefore gives the projected information budget

`J_E=sum_i ell_i I(H_t f_i)<=3/t`.                                         (5.3)

The completed projected-Fisher theorem permits arbitrary remaining spectrum and arbitrary affine terms and, under the original cap-one hypothesis, states for `r=3`, `s=1`

`||p_Q||_infinity <= [3 d + sqrt(J_E d)]/4`,
`d=min(D_3,J_E)`,
`D_3=6(4pi/3)^(2/3)=15.591108358883012...`.                                (5.4)

Its right side is monotone in `J_E`. Substituting (5.3) gives the actual full-target inequality

`boxed{
 ||p_{Q_t}||_infinity
 <= [3 d_t + sqrt((3/t)d_t)]/4,
 d_t=min(D_3,3/t).
}`                                                                          (5.5)

No structural assumption on `A` beyond the owner's three-large-eigenvalue hypothesis is added.

Equivalently, with

`t_0=3/D_3=0.19241736577956334...`,

`boxed{
 ||p_{Q_t}||_infinity <=
   11.69333126916226 + 1.7097756628547982/sqrt(t),   0<t<=t_0,
   3/t,                                               t>=t_0.
}`                                                                          (5.6)

This is a concrete application of the completed designated-partner localization result to an actual inequality on the **full rotated/indefinite target**, not a projection-only or diagonal theorem.

## 6. What localization has and has not solved

Equations (4.3) and (5.5) isolate the remaining difficulty sharply.

1. Law-class localization itself is zero-loss: roughness, arbitrary shifts, remote/countable fragments, unbounded supports, and no moments can all be passed through a canonical one-parameter heat regularization without changing the optimal QFORM constant.
2. At every fixed `t>0`, the full arbitrary matrix problem is bounded by (5.5).
3. The present Fisher payment is not uniform as `t downarrow0`; (5.6) grows like `t^(-1/2)`. Therefore lower semicontinuity alone cannot pass this quantitative bound to `t=0`.
4. This divergence is an interface obstruction, not a counterexample. It is consistent with fleet02/B14's exact narrow-fragment Fisher barrier: absolute regularity norms can explode although whole-law quadratic density remains uniformly controlled by other mechanisms.

Thus the next exact B14 obligation is:

`QFORM-HEAT-SCORE-CANCELLATION-OR-WHOLE-ACTIVE-EXIT-v1` — replace the absolute projected-Fisher score payment in the heat-regularized theorem by a signed/product-provenance estimate uniform as `t downarrow0`, or force a whole-active ridge/volume/hub/pair/rough-core exit before paying the regularity norm.

Uniform pointwise quadratic Fourier decay is not used. The full conjecture is **not** promoted to solved, and full-target continuity remains separate.
