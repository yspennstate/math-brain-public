SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B13, 2026-09-22T21:31:18Z.
attacking: the near-null one-heavy/two-transverse-bank residual by proving a bankwise heavy-row energy floor and converting it, before any reciprocal-coordinate payment, into a uniform square-root small-ball bound.

# account03/B13 r17 — near-null two-bank row-energy floor and square-root small-ball theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Extremal product laws  
**Run:** `20260922T213118Z-account03-B13-qform-r17`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING TARGET-LEVEL THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and inherited unpaid state

The full owner target remains OPEN. Inputs are arbitrary independent real original-coordinate laws with densities at most one, and the symmetric matrix has at least three eigenvalues of modulus at least one. No moments, compact support, connected support, log-concavity, Gaussianity, interval extremality, post-rotation independence, or bounded fragment count is assumed.

This run starts from the exact-rank-three mixed residual isolated in account03/B13 r16. Write

`A=R Lambda R^T`, `R^T R=I_3`, `min_j |lambda_j(Lambda)|>=1`.

There is one heavy original coordinate `i` with

`r_i=sqrt(c)u`, `c>3/10`, `||u||=1`,

and two disjoint original-coordinate light banks `L_1,L_2`. For every `j in L_a`, write

`r_j=t_j u+p_j`, `p_j in u^perp`,

and

`G_a=sum_(j in L_a) p_j p_j^T >= kappa I_2`, `kappa=7/800`.

The previous run paid every state with either bank longitudinal Schur variance `rho_a>=1/100`, and every state with

`|a|:=|u^T Lambda u|>=1/100`.

Thus its explicit first unpaid collar is

`|a|<delta:=1/100`, `rho_1<1/100`, `rho_2<1/100`,              (1.1)

with the same quantitative transverse ellipticity. The result below in fact does not need the upper bounds on `rho_a`; only the near-null condition and `G_a>=kappa I_2` are used.

The designated partner account04/B13 result actually applied is `QFORM-AFFINE-BANK-BANGBANG-WITNESS-v1`, canonical report

`yspennstate/math-open-problems@451c19388a559167a609d82310c6087e8ba211e1`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T201036Z-account04-B13-affine-bank-bangbang-r1/REPORT.md`.

It proves exact, zero-loss coordinatewise bathtub reduction for every bounded measurable slab functional, including averaged outside parameters: an arbitrary cap-one product law is dominated, for that functional, by one fixed product of arbitrary measure-one indicator sets. It does not assert interval extremality.

A compatible completed Fourier input is the row-aggregate random-slope argument of account01/B01 r11, `QFORM-RANDOM-SLOPE-ROW-AGGREGATE-v1`. The short argument is reproduced below with the sharper one-dimensional projection cap `sqrt(2)`, so the new statement does not depend on an unspecified projection constant.

## 2. New algebraic theorem: each transverse bank carries a fixed heavy-row cross energy

Choose an orthonormal spectral basis beginning with `u` and write

`Lambda = [[a,b^T],[b,D]]`,                                    (2.1)

where `b in R^2`. Since every singular value of `Lambda` is at least one,

`||Lambda u||^2=a^2+||b||^2>=1`,

hence

`||b||>=sqrt(1-a^2)`.                                          (2.2)

For bank `L_a`, write its full spectral Gram in the splitting `span(u) direct_sum u^perp` as

`S_a=[[tau_a,h_a^T],[h_a,G_a]]`.

Set

`w_a=G_a^(-1)h_a`

and decompose the longitudinal coefficient vector exactly as

`t_j=w_a dot p_j+e_j`,

where

`sum_(j in L_a) e_j p_j=0`,
`sum_(j in L_a)e_j^2=rho_a`.                                   (2.3)

Because `S_a<=I_3`, `tau_a<=1`; therefore

`w_a^T G_a w_a=tau_a-rho_a<=1`,

and from `G_a>=kappa I_2`,

`||w_a||<=kappa^(-1/2)`.                                       (2.4)

Define the spectral heavy-to-bank coefficient vector

`s^(a)_j := u^T Lambda r_j = a t_j+b dot p_j`.                 (2.5)

### Theorem 2.1 — `QFORM-NEARNULL-BANK-CROSS-ENERGY-v1`

For either bank,

`boxed:
 sum_(j in L_a) |s^(a)_j|^2
 >= kappa ( sqrt(1-a^2)-|a|/sqrt(kappa) )^2.
`                                                                  (2.6)

Consequently, throughout `|a|<=delta<sqrt(kappa/(1+kappa))`,

`boxed:
 ||s^(a)||_2
 >= sqrt(kappa)sqrt(1-delta^2)-delta.
`                                                                  (2.7)

For the live values `kappa=7/800`, `delta=1/100`,

`||s^(a)||_2 >= 0.0835367574806824...`.                         (2.8)

#### Proof

Insert (2.3) into (2.5):

`s_j=(b+a w_a) dot p_j+a e_j`.

The orthogonality in (2.3) kills the mixed term after squaring and summing, giving the exact identity

`sum_j s_j^2
 =(b+a w_a)^T G_a(b+a w_a)+a^2 rho_a`.                       (2.9)

Discard the nonnegative second term, use `G_a>=kappa I_2`, then (2.2) and (2.4):

`sum_j s_j^2
 >=kappa ||b+a w_a||^2
 >=kappa (||b||-|a|||w_a||)^2
 >=kappa (sqrt(1-a^2)-|a|/sqrt(kappa))^2`.

The bracket is positive on the stated collar. This proves (2.6)-(2.8). QED.

### Physical-coordinate interpretation

The actual physical cross coefficients from the heavy coordinate `i` into bank `L_a` are

`A_ij=r_i^T Lambda r_j=sqrt(c) s^(a)_j`.

Therefore the whole physical cross row into **each** bank has Euclidean norm

`r_a:=||(A_ij)_(j in L_a)||_2`

satisfying

`boxed:
 r_a >= r_*:=sqrt(3/10)[sqrt(7/800)sqrt(1-10^(-4))-10^(-2)]
 =0.0457549664530082... .
`                                                                  (2.10)

This is aggregate-before-inversion currency. It does not select one coordinate from a diffuse bank, and it remains positive when `rho_a ->0`.

## 3. Product-safe random-slope Fourier decay with an explicit constant

### Lemma 3.1

Let `Q=X^TAX+ell^T X+c_0` for independent original-coordinate laws with density caps one. If one original coordinate `i` has a disjoint coordinate bank `J` such that

`r=||(A_ij)_(j in J)||_2>0`,

then for every `t!=0`,

`boxed:
 |phi_Q(t)| <= min(1, sqrt(pi sqrt(2)/(r|t|))).
`                                                                  (3.1)

#### Proof

Condition on all coordinates outside `{i} union J`. Write `x=X_i`, `Y=X_J`, and `c=(A_ij)_(j in J)`. The conditioned form is

`A_ii x^2 + 2x(c dot Y+d)+H(Y)`,

where `d` is a conditioned constant and `H` is arbitrary. Define

`F_t(beta)=int exp(it[A_ii x^2+beta x]) f_i(x) dx`.

Cauchy--Schwarz in `Y` discards only the unit phase `exp(itH(Y))`:

`|phi_(Q|outside)(t)|^2 <= E |F_t(2c dot Y+2d)|^2`.             (3.2)

The one-dimensional Rogozin--Ball product-marginal theorem gives a density cap `sqrt(2)/r` for `c dot Y`; hence the affine variable `beta=2c dot Y+2d` has density cap `sqrt(2)/(2r)`. Plancherel in the parameter `beta` gives

`int |F_t(beta)|^2 d beta
 =(2pi/|t|) int f_i(x)^2 dx
 <=2pi/|t|`.                                                     (3.3)

Multiplying the cap by (3.3) yields

`|phi_(Q|outside)(t)|^2 <= pi sqrt(2)/(r|t|)`.

The bound is uniform in the outside conditioning; averaging proves (3.1). QED.

This is not the refuted law-uniform scalar quadratic van-der-Corput estimate. The half-power comes from a genuine random **linear** slope carried by an independent original-coordinate bank.

## 4. New target-level consequence: uniform square-root concentration on the hard residual

Apply Lemma 3.1 with either bank and (2.10). Put

`A_* = sqrt(pi sqrt(2)/r_*) =9.85401716907443...`.               (4.1)

Then throughout the near-null two-bank residual,

`|phi_Q(t)| <= min(1,A_* |t|^(-1/2)).`                          (4.2)

This gives a direct support-free concentration estimate without claiming a bounded density.

### Theorem 4.1 — `QFORM-NEARNULL-TWOBANK-SQRT-SMALLBALL-v1`

For every interval `I`, every admissible product input in the residual (1.1) satisfies

`boxed:
 P(Q in I) <= min(1,C_* sqrt(|I|)),
 C_* = e^(1/2) Gamma(1/4)/sqrt(2 r_*)
     =19.7603302022318... .
`                                                                  (4.3)

#### Proof

Let the interval have center `x_0` and length `ell=|I|`, and put `epsilon=ell/2`. Since

`1_{|y-x_0|<=epsilon}
 <= e^(1/2) exp(-(y-x_0)^2/(2epsilon^2))`,

Fourier inversion for the Gaussian gives

`P(Q in I)
 <= e^(1/2) epsilon/sqrt(2pi)
    int_R exp(-epsilon^2 t^2/2)|phi_Q(t)|dt`.

Use the weaker but globally valid consequence of (4.2),

`|phi_Q(t)|<=A_* |t|^(-1/2)` for `t!=0`.

The exact gamma integral is

`int_R exp(-epsilon^2t^2/2)|t|^(-1/2)dt
 =2^(1/4) Gamma(1/4) epsilon^(-1/2)`.

Substitution and `epsilon=ell/2` give

`P(Q in I)
 <= e^(1/2) A_* Gamma(1/4)/(2^(3/4)sqrt(pi)) sqrt(ell)`.

Using `A_*^2=pi sqrt(2)/r_*` simplifies the coefficient exactly to

`e^(1/2)Gamma(1/4)/sqrt(2r_*)=C_*`.

Taking the minimum with one proves (4.3). QED.

### What is gained

The generic arbitrary-rank quarter-small-ball estimate available elsewhere in the programme has exponent `1/4`. On the precise hard exact-rank-three near-null/two-planar residual, (4.3) upgrades the exponent to `1/2`, uniformly over dimension and completely arbitrary support fragmentation. It also proves that the unresolved endpoint cannot be caused by disappearance of the heavy-to-bank interaction: each of the two independent banks carries a fixed amount of that interaction.

The theorem does **not** imply an `L^infinity` density; `|t|^(-1/2)` is not integrable. The remaining problem is to extract one additional integrability mechanism from the dependent within-bank curvature/orthogonal leakage rather than taking a forbidden worst fiber.

## 5. Designated account04/B13 theorem applied to the actual new inequality

First run the proof of Theorem 4.1 on arbitrary product indicators

`prod_j 1_{E_j}`, `|E_j|=1`,

with the outside heavy coordinates included as an averaged parameter. It gives the geometric slab inequality

`|{x in prod_j E_j : x^T A x in I}|
 <= C_* sqrt(|I|)`                                               (5.1)

throughout the residual.

Now apply account04/B13 `QFORM-AFFINE-BANK-BANGBANG-WITNESS-v1` to the exact bounded slab functional in (5.1), including its averaged outside parameter. The theorem selects fixed measure-one sets independently of the outside parameter and proves that every arbitrary cap-one product density has slab probability no larger than an extreme-product slab probability. Therefore (5.1) transfers with **zero constant loss** to all admissible input laws, giving exactly (4.3).

This is an actual application of the designated partner result to the new inequality. No single interval, centered set, bounded diameter, or finite fragment count is asserted to be extremal.

## 6. Relation to fresh completed fleet mathematics

Fresh account03/B10 r18 proves a complementary three-cross geometric-mean gate: when both banks carry quantitative third-direction residual leakage, an actual rank-three physical cross block yields an integrable Fourier bound and a continuous density, with a cost depending on `(tau_J tau_K)^(-1/6)`. The present theorem is orthogonal to that result: it remains uniform as the longitudinal residuals tend to zero, but obtains only square-root concentration. Together they isolate the genuinely difficult transition as **upgrading the endpoint `1/2` small-ball law to a linear small-ball law while the same-bank orthogonal leakage tends to zero**.

The exact generated-leakage endpoint from account03/B04 r18 closes certain `rho=0` overlap states when the heavy pivot is exactly null. Small nonzero heavy Rayleigh cannot be treated as an operator-norm perturbation because remote fragmented supports can amplify coefficient changes. Thus the next step must be an intrinsic near-null product-space interpolation, not continuity in matrix coefficients.

## 7. Remaining implication

Full exact-rank-three QFORM and full QFORM remain OPEN. Full continuity also remains OPEN.

The sharpened B13 successor is

`QFORM-NEARNULL-TWOBANK-LINEARIZE-SQRT-TO-LINEAR-v1`:

> In the state `|u^T Lambda u|<1/100`, `G_1,G_2>=7/800 I_2`, use the now-proved bankwise row-energy floor `r_a>=r_*` together with the two independent banks' same-coordinate transverse curvature to upgrade `P(Q in I)=O(|I|^(1/2))` to `O(|I|)` uniformly as `rho_1,rho_2 ->0`. The argument must aggregate dependent orthogonal leakage before reciprocal payment and may not replace a bank by a worst conditional projection-density cap.

The source-valid mechanisms to splice next are the account03/B04 generated-leakage endpoint, account03/B10 three-cross geometric-mean interior gate, and the fresh pair/coarea machinery; the bridge must be stable between those endpoints.

## 8. Verification and status

A deterministic checker beside this report verifies the exact constants and the algebraic lower-bound formula at the live values. Numerical checks are regression aids only; the proof is the displayed algebra.

- `QFORM-NEARNULL-BANK-CROSS-ENERGY-v1`: **PROVED**.
- `QFORM-NEARNULL-TWOBANK-SQRT-SMALLBALL-v1`: **PROVED SUPPORTING TARGET-LEVEL THEOREM**.
- designated account04/B13 bang-bang theorem: **APPLIED WITH ZERO LOSS TO THE NEW SLAB INEQUALITY**.
- full exact-rank-three conjecture: **OPEN**.
- full owner QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- continuity: **NOT PROVED by this theorem**.
