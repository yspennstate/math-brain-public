SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-22T20:46:37Z.
attacking: the integrated Fourier criterion through a product-preserving L3-to-fractional-trace synthesis, using account02/B02's physical-row Lp theorem and its indefinite-pair fractional-trace transducer.

# account01/B02 — subcritical row-to-pair synthesis with only logarithmic determinant loss

Run: `20260922T204637Z-account01-B02-qform-r14`.
Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN / WITHOUT_VERIFIED_BRAIN**.

Fresh owner control was read on `yspennstate/math-research-brain` main, initially at `f24887ffa34adb07615288708fdb4801dfe0f466` and refreshed before publication at `a4ddb5b0246ac8e7826eb5bc6f414a582ffb7ea2`; OWNER CONTROL revision remains `2026-09-22.15`, QFORM only.

## 1. Exact scope and correction discipline

The target remains: independent real coordinates with one-dimensional probability densities bounded by one, arbitrary dimension, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No Gaussian, moment, compact-support, log-concavity, connected-support, diagonal-basis, or post-rotation independence assumption is used.

This report does not use the refuted law-uniform pointwise Fresnel decay, arbitrary-joint rank-three coarea, positive conditional-projection-density moments, fixed-good-minor exhaustion, conditional-cap-as-independence, or same-square endpoint absorption. It also respects the fresh partner corrections `QFORM-SQUARE-COLLISION-ALPHA1-ENDPOINT-FALSE-v1` and `QFORM-CROSS-CYCLE-ARBITRARY-SELF-CURVATURE-FALSE-v1`: the argument stays strictly subcritical in the fractional exponent and allows the residual quadratic term to depend arbitrarily on the same coordinates that determine the physical linear form.

The target-wide unweighted criterion `int_R |phi_Q(t)| dt <= C` remains open in this run. I found no exact-target counterexample to it.

## 2. Two completed account02/B02 inputs actually applied

### 2.1 Physical-row Lp theorem

Source: `yspennstate/math-open-problems@23b3b82de685705bd40a0d1b0241c212bb879978`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260922T201015Z-account02-B02-qform-r12/REPORT.md`.

If `X` is independent of a random element `W`, `f_X<=1`, `U=U(W)` has marginal density cap `M`, `R=R(W)` is arbitrary and may depend completely on `U`, and

`T=a X^2+2 X U+R`,

then for every `1<q<2`,

`||p_T||_q <= [2^(q-1)/(2-q)]^(1/q) M^((q-1)/q)`.                 (2.1)

In particular the theorem is uniform in the scalar quadratic coefficient `a`, including `a=0`, and it preserves the original-coordinate product structure.

### 2.2 Indefinite-pair fractional-trace transducer

Source: `yspennstate/math-open-problems@853a4e86c7ff9789891c473905eeb57b13f615ed`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260922T190827Z-account02-B02-40617e89/REPORT.md`.

Let an invertible indefinite original-coordinate physical pair have symmetric principal block `B`, set

`D=|det B|`, `kappa=sigma_min(B)`,

and let `T` be the physical Schur-residual scalar random variable after completing the pair. For

`H_alpha(T)=sup_s E|T-s|^(-alpha)`,

and `0<alpha<=1/2`, the partner proves

`||p_Q||_infinity <= C_alpha D^(alpha-1/2) kappa^(-alpha) H_alpha(T)`,   (2.2)

where in the high-alpha range `1/(2sqrt(2))<=alpha<=1/2`,

`C_alpha=2^(alpha+3/2)`.                                               (2.3)

No independence between the pair translation and the residual is required.

## 3. General Lq-to-fractional-potential lemma

### Lemma 3.1

Let `Y` have a probability density `p` with `||p||_q<=L`, where `q>1`, and write `q'=q/(q-1)`. If `0<alpha<1/q'`, then for every `r>0`,

`H_alpha(Y)
 <= L [2/(1-alpha q')]^(1/q') r^(1/q'-alpha)+r^(-alpha)`.              (3.1)

### Proof

For any center `s`, split the integral into `|y-s|<r` and its complement. Holder on the inner region gives

`int_{|y-s|<r}|y-s|^(-alpha)p(y)dy
 <= ||p||_q [int_{-r}^r |u|^(-alpha q')du]^(1/q')`
` = L [2/(1-alpha q')]^(1/q') r^(1/q'-alpha)`.

On the complement, `|y-s|^(-alpha)<=r^(-alpha)` and the probability mass is at most one. Taking the supremum over `s` proves (3.1). QED.

This elementary step is the bridge from the partner's global physical-row `L^q` control to the pair transducer. It requires no pointwise characteristic-function decay.

## 4. Critical-near-endpoint specialization of the physical row

Take

`0<epsilon<=epsilon_0 := 1/2-1/(2sqrt(2))`,
`alpha=1/2-epsilon`,
`q=2-2epsilon`.

Then

`q'=2(1-epsilon)/(1-2epsilon)`,
`alpha q'=1-epsilon`.                                                  (4.1)

The partner row estimate (2.1) becomes

`L_q = 2^(-epsilon/(1-epsilon))
       epsilon^(-1/[2(1-epsilon)])
       M^((1-2epsilon)/[2(1-epsilon)]).`                               (4.2)

Apply Lemma 3.1 with `r=M^(-1)`. The powers of `M` collapse exactly to `M^alpha`, and the numerical factor simplifies to

`H_(1/2-epsilon)(T)
 <= B_epsilon M^(1/2-epsilon)`,                                        (4.3)

where

`B_epsilon
 = 1 + 2^((1-4epsilon)/(2(1-epsilon)))/epsilon`.                     (4.4)

This remains valid when the physical row diagonal is zero and when the remaining quadratic residual depends arbitrarily on `U`.

## 5. New theorem: the pair determinant costs only a logarithm

### Theorem 5.1 — `QFORM-INDEFINITE-PAIR-ROW-LOG-v1`

In the partner pair setting (2.2), assume the physical Schur residual contains an original coordinate `X` whose off-diagonal linear form `U` has a finite marginal density cap `M`. No condition is imposed on that row's diagonal, and the rest of the residual may depend arbitrarily on `U`. Then

`boxed:
 ||p_Q||_infinity
 <= 33 sqrt(M/kappa)
       [1+log_+(kappa/(M D))].
`                                                                        (5.1)

### Proof

Combining (2.2), (2.3), and (4.3) gives, for every `0<epsilon<=epsilon_0`,

`||p_Q||_infinity
 <= 2^(2-epsilon) B_epsilon sqrt(M/kappa)
    [kappa/(M D)]^epsilon`.                                            (5.2)

Put

`rho=kappa/(M D)`, `L=log_+(rho)`.

At the endpoint

`epsilon_0=0.14644660940672627...`,
`1/epsilon_0=6.82842712474619...`,

one has

`B_(epsilon_0)=9.07909665391885...`,
`2^(2-epsilon_0)B_(epsilon_0)=32.8108747244283... <33`.                (5.3)

If `L<=1/epsilon_0`, choose `epsilon=epsilon_0`. For `rho<=1`, the last factor in (5.2) is at most one. For `rho>1`, concavity of

`log(1+L)-epsilon_0 L`

on `[0,1/epsilon_0]`, together with its nonnegative endpoint values, gives

`exp(epsilon_0 L)<=1+L`.                                               (5.4)

Thus (5.1) follows in this range.

If `L>1/epsilon_0`, choose `epsilon=1/L<epsilon_0`. Since

`(1-4epsilon)/(2(1-epsilon)) <=1/2`,

we have

`B_epsilon <=1+sqrt(2)/epsilon=1+sqrt(2)L`.                            (5.5)

Also `rho^epsilon=e` and `2^(2-epsilon)<=4`, hence

`2^(2-epsilon)B_epsilon rho^epsilon
 <=4e(1+sqrt(2)L)
 <=4e sqrt(2)(1+L)
 <15.38(1+L)<33(1+L)`.                                                 (5.6)

This proves (5.1). QED.

The point is qualitative as well as quantitative: the previous direct quarter-Riesz row cascade carried the power penalty `D^(-1/4)`. The near-endpoint optimization converts that power loss into only a logarithm.

## 6. Automatic full-matrix form using one residual physical row

Let `S` be the physical Schur complement after removing the indefinite pair. Choose any residual original coordinate `k` with off-diagonal Schur-row norm

`sigma = (sum_{j != k} S_kj^2)^(1/2) >0`.                              (6.1)

The one-dimensional product-projection theorem used in the completed account02/B02 row report permits the admissible density cap

`M=sqrt(2)/sigma`.                                                      (6.2)

Substituting this cap directly into Theorem 5.1 gives

`boxed:
 ||p_Q||_infinity
 <= 33*2^(1/4) (kappa sigma)^(-1/2)
    [1+log_+(kappa sigma/(sqrt(2)D))].
`                                                                        (6.3)

Because `B` is symmetric `2x2` and invertible,

`D = kappa ||B||_op`,                                                   (6.4)

so equivalently

`boxed:
 ||p_Q||_infinity
 <= 33*2^(1/4) (kappa sigma)^(-1/2)
    [1+log_+(sigma/(sqrt(2)||B||_op))].
`                                                                        (6.5)

Thus **a tiny pair determinant by itself is no longer a power-law obstruction**. The remaining cost is the pair's smaller singular value through `(kappa sigma)^(-1/2)` and only a logarithmic residual-row/pair aspect ratio.

For comparison, the fresh account02/B02 addendum at `yspennstate/math-open-problems@99f0eb89b7b1ad3ef3f225460fb08d4d22c19a75` gives

`||p_Q||_infinity <19.210 (D kappa sigma)^(-1/4)`                       (6.6)

under the same type of outer indefinite-pair plus nonzero residual-row certificate. Both are valid, so one may take the minimum of (6.3) and (6.6). The new estimate is specifically useful in determinant-poor but row-energy-rich configurations.

## 7. Integrated-Fourier consequence and what remains open

The assignment's strongest target is a uniform unweighted `L^1_t` bound for the full characteristic function. The present argument does not prove that target-wide statement and produces no exact-target counterexample to it.

On the paid branch, (5.1) does give a genuine integrated estimate by Plancherel:

`int_R |phi_Q(t)|^2 dt
 =2pi ||p_Q||_2^2
 <=2pi ||p_Q||_infinity`
` <=66pi sqrt(M/kappa)[1+log_+(kappa/(MD))].`                           (7.1)

This is an `L^2_t` estimate, not `L^1_t`, so continuity is **not** proved by this run. Essential boundedness is proved on the stated branch.

## 8. Compact conditional end-to-end argument and first unpaid implication

A full proof would close if the surviving three-large-eigenvalue geometry can force, in every unhandled case, one of the already-paid diffuse/ridge/localized/grouped-coordinate branches, or an invertible indefinite original-coordinate pair `B` whose physical Schur residual has a row with `sigma>0` satisfying a dimension-free bound on

`(kappa sigma)^(-1/2)
 [1+log_+(sigma/(sqrt(2)||B||_op))]`.                                  (8.1)

Then (6.5) supplies the required universal essential-density bound.

This is a strictly weaker structural debt than the previous quarter-Riesz row route, which required quantitative payment of the product `D kappa sigma`. The determinant `D` no longer appears as a power. It is also more dependence-safe than the earlier affine-hyperbolic endpoint route: the residual quadratic term may depend arbitrarily on the same coordinates that determine `U`.

The first unpaid implication is therefore:

`QFORM-PAIR-ROW-LOG-EXTRACTION-v1` (OPEN): from the surviving aggregate third-compound / ridge / grouped-coordinate geometry under the bare three-large-eigenvalue hypothesis, force either an already-paid branch or an indefinite physical pair plus a nonzero Schur row for which (8.1) is universally bounded.

No claim is made that one fixed principal pair or row always has this property; the live correction ledger contains counterexamples to several such fixed-minor reductions. Aggregate-before-inversion may still be required.

## 9. Status

- `QFORM-INDEFINITE-PAIR-ROW-LOG-v1`: **PROVED** from two completed account02/B02 results plus Lemma 3.1.
- Power dependence `D^(-1/4)` in the pair-plus-residual-row branch: **reduced to a logarithmic aspect-ratio penalty**.
- Essential bounded density: **PROVED only on this stated branch**.
- Continuous density: **NOT PROVED by this run**.
- Universal unweighted `int |phi_Q|`: **OPEN; no target-valid counterexample found**.
- Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.

No simulation or histogram is used as proof. The numerical constants in (5.3) and (5.6) are evaluations of explicit elementary expressions; all substantive inequalities are analytic.