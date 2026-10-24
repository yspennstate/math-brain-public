SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T00:51:47Z.
attacking: aggregate-before-collision for one mixed hub bank plus one rank-one square bank, using the partner's sharp product L3 endpoint.

# account01/B03 auto11 — mixed hub/bank collision compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Fresh owner control at entry:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM / FULL_TARGET_OPEN`.

The full conjecture remains open. This report proves a dimension-free aggregate branch and an exact weighted independent-copy estimate. It uses no moments, compact support, connected support, log-concavity, post-rotation independence, law-uniform pointwise quadratic-phase decay, conditional cap for a conjugate sum/difference variable, arbitrary-joint coarea bound, or fixed-good-minor selection.

## 1. Source-valid inputs

The current brain state records the full target as open and retains the corrections refuting the arbitrary-joint rank-three coarea claim, positive conditional projection-density moments, law-uniform pointwise Fresnel decay, universal single-Schur extraction, and local-triple/cross-rank-three dichotomies.

The designated partner result actually used is **account02/B03**, run `20260922T150949Z-account02-B03-QFORM-r11`, canonical mathematics

`yspennstate/math-open-problems@f40d5d4f5013b0a6af275a19aa3dc0fa2d76c347`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260922T150949Z-account02-B03-QFORM-r11/REPORT.md`.

It proves, for independent cap-one scalars `X,Y,Z`, arbitrary outside variable `W`, arbitrary measurable shifts depending on `W`, and nonzero `c,a`,

`Q=c(X+alpha)(Y+beta)+a(Z+h)^2+R(W)`

has

`||p_Q||_infinity <= 4 sqrt(3)|c|^(-2/3)|a|^(-1/3)`.          (1.1)

The proof is the exact `L^3` product-density estimate

`||p_(XY)||_3 <= 2 sqrt(3)`                                    (1.2)

paired by Young with

`||p_(a(Z-h)^2)||_(3/2) <= 2|a|^(-1/3)`.                       (1.3)

The partner explicitly notes the corresponding density-cap scaling for three independent aggregate scalars. I rederive that scaling below so no hidden normalization is used.

A compatible completed bank-projection theorem, recorded in account02/B04 at `yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7`, states that for independent cap-one original coordinates and a nonzero coefficient vector `u`,

`||p_(u^T X)||_infinity <= sqrt(2)/||u||_2`.                    (1.4)

Only disjoint original-coordinate banks are combined below, so independence is genuine.

The latest designated-partner handoff, account02/B03 run `20260923T001512Z-account02-B03-QFORM-auto11`, canonical mathematics `yspennstate/math-open-problems@90b9e0b5438b950fd2a0ed054833c055fdb92967`, supplies the mixed-hub family and the exact local-collision lower bound used in Section 5.

## 2. Density-cap scaling of the partner packet

### Lemma 2.1 — scaled product-square packet

Let `A,B,C` be independent real random variables with density caps `M_A,M_B,M_C`, let `W` be independent of them, and allow arbitrary measurable `alpha(W), beta(W), gamma(W), R(W)`. For `c lambda !=0`, put

`T=c(A+alpha)(B+beta)+lambda(C+gamma)^2+R`.                     (2.1)

Then

`boxed:
 ||p_T||_infinity
 <= 4 sqrt(3) |c|^(-2/3)|lambda|^(-1/3)
    (M_A M_B M_C)^(2/3).
`                                                                  (2.2)

Moreover `T` has a continuous density.

#### Proof

Condition on `W=w`. Set

`A'=M_A A`, `B'=M_B B`, `C'=M_C C`.                              (2.3)

Each primed scalar has density cap at most one. The conditional polynomial is

`[c/(M_A M_B)](A'+M_A alpha)(B'+M_B beta)
 +[lambda/M_C^2](C'+M_C gamma)^2+R(w)`.                           (2.4)

Apply the partner theorem (1.1) to (2.4), obtaining exactly (2.2), uniformly in `w`.

For continuity, use the proof ingredients rather than only its final supremum estimate. The translated product term has an `L^3` density and the translated square term an `L^(3/2)` density. Their convolution therefore belongs to `C_0(R)`: for `g in L^3`, `h in L^(3/2)`,

`|(g*h)(x+r)-(g*h)(x)|
 <= ||g||_3 ||tau_r h-h||_(3/2) ->0`.                             (2.5)

The conditional density is thus continuous. Its uniform bound (2.2) supplies domination, so averaging over `W` and applying dominated convergence preserves continuity. QED.

This proof makes no assertion that a rotated set of spectral coordinates is independent; it only rescales three genuinely independent scalar sources.

## 3. New weighted independent-copy time estimate

The density theorem above can be converted into an exact dependence-safe collision estimate without ever splitting a conjugate sum/difference pair.

### Lemma 3.1 — cap-to-half-collision energy

If a real random variable `T` has a probability density with `||p_T||_infinity <= M`, and `T'` is an independent copy, then

`E|T-T'|^(-1/2) <= 4 sqrt(M)`.                                    (3.1)

Consequently, with `phi_T(t)=E exp(itT)`,

`boxed:
 integral_R |t|^(-1/2)|phi_T(t)|^2 dt
 <=4 sqrt(2 pi M).
`                                                                  (3.2)

#### Proof

The difference density is `g=p_T * check(p_T)`, so `||g||_infinity<=M`. For every `r>0`,

`E|T-T'|^(-1/2)
 <= M integral_(|x|<=r)|x|^(-1/2)dx + r^(-1/2)
 =4M sqrt(r)+r^(-1/2)`.                                           (3.3)

Choosing `sqrt(r)=1/(2sqrt(M))` gives (3.1).

The one-dimensional Riesz-energy identity with the Fourier convention used here is

`integral_R |t|^(-1/2)|phi_T(t)|^2 dt
 =sqrt(2pi) E|T-T'|^(-1/2)`.                                    (3.4)

It follows from the positive Riesz kernel Fourier transform
`Fourier(|x|^(-1/2))(t)=sqrt(2pi)|t|^(-1/2)` (or by standard Abel regularization). Combining (3.1) and (3.4) proves (3.2). QED.

Applying Lemma 3.1 to Lemma 2.1 yields

`boxed:
 integral_R |t|^(-1/2)|phi_T(t)|^2 dt
 <=8 sqrt(2pi) 3^(1/4)
   |c|^(-1/3)|lambda|^(-1/6)
   (M_A M_B M_C)^(1/3).
`                                                                  (3.5)

This is an actual independent-copy integrated estimate. The object `|phi_T|^2` is the characteristic function of `T-T'`; no normalization or conditional-independence claim is made for `X-X'` and `X+X'` separately.

The same packet already has the linear small-ball estimate

`P(T in I) <=4 sqrt(3)|c|^(-2/3)|lambda|^(-1/3)
              (M_A M_B M_C)^(2/3)|I|`                            (3.6)

for every interval `I`. Importantly, (3.6) comes from the partner's `L^3 x L^(3/2)` endpoint; I do **not** claim that the negative-weight collision energy (3.5), by itself, implies an `L^infinity` density bound for an arbitrary law.

## 4. Aggregate physical-bank theorem

Let `{0},I,J,W` be disjoint sets of **original** coordinates. Write

`Z=X_0`, `U=u^T X_I`, `V=v^T X_J`,
`s=||u||_2`, `t=||v||_2`, `s,t>0`.                               (4.1)

Allow arbitrary outside-measurable shifts `alpha(W),beta(W),gamma(W),R(W)` and consider

`Q=c(Z+alpha)(U+beta)+lambda(V+gamma)^2+R(W)`.                    (4.2)

By (1.4),

`M_Z<=1`, `M_U<=sqrt(2)/s`, `M_V<=sqrt(2)/t`.                    (4.3)

Therefore Lemmas 2.1 and 3.1 give

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(3)|c|^(-2/3)|lambda|^(-1/3)(2/(st))^(2/3),
`                                                                  (4.4)

and

`boxed:
 integral_R |r|^(-1/2)|phi_Q(r)|^2 dr
 <=8 sqrt(2pi)3^(1/4)|c|^(-1/3)|lambda|^(-1/6)(2/(st))^(1/3).
`                                                                  (4.5)

The density is continuous. These bounds depend on the aggregate bank norms `s,t`, not on any individual physical coefficient. Hence they survive exactly the high-cardinality regime in which all individual hub/bank entries tend to zero.

## 5. Apply the latest account02/B03 obstruction family

The latest partner run studies

`A_m(a,b)=star_(h,V)(a/sqrt(m)) direct_sum (b/m) J_m`,
`|a|,|b|>=1`.                                                       (5.1)

Its nonzero spectrum is exactly

`{+|a|,-|a|,b}`.                                                    (5.2)

In original coordinates the corresponding quadratic variable is

`Q_m=2 X_h U_m + b V_m^2`,                                        (5.3)

where

`U_m=(a/sqrt(m)) sum_(j=1)^m Y_j`,
`V_m=(1/sqrt(m)) sum_(k=1)^m Z_k`,                                (5.4)

and the hub, `Y` bank and `Z` bank are disjoint. Thus

`||u||_2=|a|`, `||v||_2=1`, `c=2`, `lambda=b`.                   (5.5)

Substituting into (4.4), all powers of two cancel:

`boxed:
 ||p_(Q_m)||_infinity
 <=4 sqrt(3)|a|^(-2/3)|b|^(-1/3)
 <=4 sqrt(3)
 =6.9282032302... .
`                                                                  (5.6)

This improves the `3*4^(2/3)=7.559526...` bound used in the latest partner handoff for the same family. It is uniform in `m`, for **all** admissible cap-one input laws, and the density is continuous.

The weighted global collision endpoint also becomes

`boxed:
 I_global(m):=integral_R |r|^(-1/2)|phi_(Q_m)(r)|^2 dr
 <=8 sqrt(2pi)3^(1/4)|a|^(-1/3)|b|^(-1/6)
 <26.392 |a|^(-1/3)|b|^(-1/6).
`                                                                  (5.7)

This is a genuine aggregate-before-collision statement: it is dimension-free although every individual hub coefficient is only `a/sqrt(m)`.

Now apply the partner's **newest** local collision lower bound to the same family. For the admissible law `Uniform[1,2]`, every physical hub--`Y_j` pair has local term

`F_(m,j)=2a X_h Y_j/sqrt(m)`                                      (5.8)

and the partner proves

`I_local(m,j)
 := integral_R |r|^(-1/2)|E exp(ir F_(m,j))|^2 dr
 >= sqrt(pi/(3|a|)) m^(1/4)`.                                    (5.9)

Combining (5.7) and (5.9), for fixed nonzero `a,b`,

`boxed:
 I_local(m,j)/I_global(m)
 >= c_0 m^(1/4)|a|^(-1/6)|b|^(1/6),
 c_0= sqrt(pi/3)/(8 sqrt(2pi)3^(1/4))
     =0.03877520246... .
`                                                                  (5.10)

Hence the separation tends to infinity like `m^(1/4)`. The local physical-pair collision endpoint diverges while the correctly aggregated global collision endpoint stays bounded. This quantitatively strengthens the partner's conclusion that collision aggregation must occur **before** local reciprocal payment in the mixed-hub/no-pivot branch.

No statement in (5.9) treats `X-X'` and `X+X'` as independent; it is the partner's exact independent-copy/Riesz calculation.

## 6. What this pays and what remains

This run closes the analytic mixed-hub/rank-one-square packet at the sharper constant `4sqrt(3)` and upgrades it to a continuous density plus the explicit weighted collision estimate (5.7). It also gives a quantitative local/global collision separation (5.10) on the latest partner obstruction.

It does **not** solve the unrestricted conjecture. The remaining implication is structural: from only `s_3(A)>=1`, produce a dimension-free product-preserving alternative which either contains such an aligned mixed hub/bank plus square packet, a previously paid ridge/cross-bank packet, or a genuinely hybrid no-pivot packet. The latest partner family proves that selecting one physical pair before aggregation cannot be part of an exhaustive proof.

The natural next B03 step is to allow a second low-rank contamination in (4.2) and seek a multi-packet interpolation in which the full bank singular scale is paid before any half-Riesz endpoint. The existing refutations of one-Schur extraction, fixed minor selection, and conditional sum/difference caps remain binding.
