SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-23T07:10:13Z.
attacking: probability-level extreme-product localization before fragment normalization, with arbitrary translations, distant fragments and unbounded supports.

# QFORM-PROBABILITY-LEVEL-EXTREME-MIXTURE-LOCALIZATION-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account01/B14`  
Run: `20260923T071013Z-account01-B14-QFORM-r31`  
Status: **PROVED SUPPORTING ZERO-LOSS LOCALIZATION RECONCILIATION + COMPLETED PARTNER APPLICATION; FULL QFORM OPEN.**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact obligation and source-pinned input

The target remains: for arbitrary dimension, independent real inputs with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal bound on the density of `X^T A X`, or give a valid counterexample. No support radius, moment, connected-support, centering, log-concavity, identical-law or post-rotation independence assumption is allowed.

The B14 localization obligation is to make translations, distant fragments and unbounded supports harmless without paying a hidden normalization factor.

This run applies the completed designated-partner theorem

`account02/B14 r27, QFORM-DK-SUBPROBABILITY-HOMOGENEITY-v1`,

canonical source

`yspennstate/math-open-problems@8f29d24c80043bd45bcd1c6e8957760f048c98ff`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T070336Z-account02-B14-QFORM-r27/REPORT.md`.

For a `D_k` cross-volume certificate, that theorem proves the exact subprobability density estimate

`||p_(Q#nu)||_infinity <= C_(k,q) Z_k^(-1/(2k))`
`    * prod_i m_i^(1-alpha_i/k) prod_j m_j^(1-beta_j/k)`,       (1.1)

where `m_i,m_j` are the coordinate subprobability masses and the volume marginals satisfy

`sum_i alpha_i=sum_j beta_j=k`.                                (1.2)

Consequently, if all volume-active coordinates are split into `N` equal subprobability pieces before applying the certificate, the black-box bound acquires the exact factor `N^2`. That is a localization-order obstruction, not a QFORM counterexample.

The new contribution of this run is the **reconciliation with that fresh r27 obstruction**: the `N^2` loss is not a defect of the already-developed B14 extreme-law localization principle. It is caused by localizing one extreme probability law further into normalized subprobability fragments. The correct proof order is probability-level localization: approximate each arbitrary cap-one marginal by a convex mixture of whole unit-mass indicator marginals, and never split those indicators before applying the probability theorem. Earlier B14 work already established simultaneous extremal-envelope localization in abstract convex/TV form; Sections 2-4 below give a self-contained constructive finite-mixture realization and apply it to the new r27 mass exponents. This report does not claim that the abstract extremal principle itself is first proved here.

## 2. One-dimensional probability-level extreme-mixture lemma

Let

`D={f in L1(R): 0<=f<=1 a.e., integral_R f=1}`.

Let `F` be the class of densities `1_E`, where `E` is a bounded finite union of intervals and `|E|=1`.

### Theorem 2.1 — finite probability mixture approximation

For every `f in D` and every `epsilon>0`, there are finitely many weights

`theta_r>=0,    sum_r theta_r=1`,

and sets `E_r` in `F` such that

`boxed( || f - sum_r theta_r 1_(E_r) ||_1 < epsilon. )`        (2.1)

There is no common support-radius bound and no common fragment-count bound.

### Proof

Choose `R>0` so that

`tau=int_{|x|>R} f(x) dx < epsilon/8`.                         (2.2)

Choose any bounded interval `J` of length one disjoint from `[-R,R]` and define

`g(x)=f(x)1_{[-R,R]}(x)+tau 1_J(x)`.                           (2.3)

Then `0<=g<=1`, `int g=1`, and `g` has bounded support. Moreover

`||f-g||_1`
` <= int_{|x|>R} f(x)dx + tau |J|`
` =2tau < epsilon/4`.                                          (2.4)

Now choose a bounded interval containing `supp g` and partition it into finitely many half-open cells

`I_1,...,I_M`

of common length `1/N`, enlarging the containing interval slightly if needed. Let `s_N` be the conditional expectation of `g` on this grid. Then

`s_N=sum_{r=1}^M a_r 1_(I_r),    0<=a_r<=1`,                  (2.5)

and

`int s_N=int g=1`, so `sum_r a_r=N`.                           (2.6)

As the mesh tends to zero, step-function conditional expectations converge to `g` in `L1`; choose `N` so that

`||s_N-g||_1<3epsilon/4`.                                      (2.7)

Consider the finite polytope

`P={a in [0,1]^M: sum_r a_r=N}`.                               (2.8)

Every extreme point of `P` is a `0-1` vector with exactly `N` ones. Indeed, if two coordinates are strictly between zero and one, a sufficiently small `(+delta,-delta)` perturbation writes the point as a nontrivial midpoint; if exactly one coordinate were fractional, the integer equality `sum a_r=N` would be impossible. Hence

`a=sum_s theta_s v^(s)`,                                       (2.9)

with `theta_s>=0`, `sum_s theta_s=1`, and each `v^(s)` a `0-1` vector containing exactly `N` ones.

Let

`E_s=union_{r:v_r^(s)=1} I_r`.                                 (2.10)

Then `E_s` is a bounded finite union of intervals and

`|E_s|=N*(1/N)=1`.                                             (2.11)

Equations (2.5),(2.9) give the exact identity

`s_N=sum_s theta_s 1_(E_s)`.                                  (2.12)

Combining (2.4),(2.7),(2.12) proves (2.1). QED.

### Translation covariance

For every `a in R`, translating `f` by `a` translates every approximating set `E_s` by `a` and changes no weight or density cap. Thus the approximation is exactly translation-covariant. Since `R` and the locations of the `E_s` may depend on the input law and on `epsilon`, the theorem imposes no hidden support or moment bound.

## 3. Product version and random-environment localization

Let `f_1,...,f_m in D`. Apply Theorem 2.1 with errors summing to less than `epsilon`, obtaining

`g_i=sum_{r_i} theta_(i,r_i) 1_(E_(i,r_i))`.                   (3.1)

Because every factor has `L1` norm one, the telescoping product identity gives

`|| prod_i f_i - prod_i g_i ||_1`
` <= sum_i ||f_i-g_i||_1 < epsilon.                            (3.2)

Expanding the product gives a finite convex mixture of full probability product laws,

`prod_i g_i`
` =sum_(r_1,...,r_m) [prod_i theta_(i,r_i)]`
`    prod_i 1_(E_(i,r_i)),                                    (3.3)

and the weights in (3.3) sum to one.

This yields a random-environment version needed for outside conditioning.

### Theorem 3.1 — zero-loss conditional localization

Let `(Omega,eta)` be an arbitrary probability space and let

`F_omega:R^m -> R`

be a jointly measurable family. Assume that for every choice of extreme marginals `1_(E_i)` with `E_i in F` and every interval `J`,

`int_Omega int 1_{F_omega(x) in J}`
`             prod_i 1_(E_i)(x_i) dx d eta(omega)`
` <= C |J|.                                                     (3.4)

Then the identical estimate

`boxed(`
`int_Omega int 1_{F_omega(x) in J}`
`             prod_i f_i(x_i) dx d eta(omega)`
` <= C |J|`
`)`                                                             (3.5)

holds for every arbitrary cap-one product law `prod_i f_i`, with the **same constant C**.

### Proof

For the finite mixture approximation (3.3), the left side of (3.5) is a convex combination of quantities bounded by `C|J|`, hence is at most `C|J|`. The difference between this mixture probability and the original one is bounded by the `L1` distance (3.2). Let `epsilon` tend to zero. QED.

A key special case is

`F_omega(x)=x^T Bx + ell(omega)^T x + c(omega)`.               (3.6)

Thus arbitrary affine coefficients generated by conditioning on outside original coordinates cost zero, provided the analytic theorem on the active probability law is uniform in those affine coefficients. No normalization of a thin fiber is involved.

## 4. Exact localization of the full small-ball/density envelope

The previous theorem treats each fixed interval. One can localize the entire density objective simultaneously.

For a parameter family `F_theta`, define on product probability laws

`SB(mu)=sup_(theta,t,h>0) mu{F_theta in [t,t+h]}/h`.            (4.1)

For every fixed `(theta,t,h)`, the displayed quotient is continuous in total variation. Therefore `SB` is lower semicontinuous as a supremum of continuous functionals. It is also convex, being a supremum of positive linear functionals of `mu`.

Let `mu_n` be the finite convex-mixture approximants from Section 3. Then

`SB(mu) <= liminf_n SB(mu_n)`                                  (4.2)

and convexity gives

`SB(mu_n) <= sup_{nu in F_product} SB(nu)`.                    (4.3)

Since the reverse inequality is trivial,

`boxed(`
`sup_{all cap-one product laws mu} SB(mu)`
` = sup_{bounded finite-union unit-indicator product laws nu} SB(nu).`
`)`                                                             (4.4)

Equality is in the extended nonnegative reals and therefore preserves the optimal constant even if it is infinite.

For a fixed output probability measure `rho`,

`sup_{t,h>0} rho([t,t+h])/h`                                   (4.5)

is the extended `L^infinity` density norm: finiteness of (4.5) implies domination by that constant times Lebesgue measure first on intervals and then on Borel sets; conversely Lebesgue differentiation recovers the essential supremum. Hence (4.4) is an exact localization of the full bounded-density target, not only of a fixed event.

## 5. Translation quotient for affine terms

Let `B=B^T` and decompose an affine coefficient

`ell=ell_R+ell_K`,

with `ell_R in Range(B)` and `ell_K in Ker(B)`. Choose `s` with

`2Bs=ell_R`.                                                   (5.1)

Writing `y=x+s`,

`x^T Bx+ell^T x+c`
` =y^T By+ell_K^T y+c'`.                                      (5.2)

Coordinatewise translation maps the cap-one product class bijectively to itself, and maps the extreme class in Theorem 2.1 bijectively to itself. Therefore the worst-law small-ball constant for the active block depends only on the kernel component `ell_K`. In particular, if `B` is invertible, **all affine terms are removable at zero localization cost**. This remains a worst-law statement; it does not assert independence after rotating the variables.

## 6. Equation-level application of completed partner r27

Take ten original coordinates and

`A_5 = [[0,I_5],[I_5,0]]`,                                    (6.1)

so

`Q=2 sum_(j=1)^5 X_j X_(5+j)`.                                (6.2)

The spectrum of `A_5` is `+1` and `-1`, each with multiplicity five, so this is a genuine target-valid matrix.

For the cross block `M=I_5`, the completed `D_5` probability theorem gives

`boxed( ||p_Q||_infinity <= 5 sqrt(2e) = 11.6582199079... . )` (6.3)

Now take every marginal to be the legal remote-fragment density

`f_N=1_(E_N),`
`E_N=union_(r=1)^N [L_r,L_r+1/N]`,                             (6.4)

where the locations `L_r` can be arbitrarily far apart.

If one performs the **unsafe** operation of decomposing every `f_N` into its `N` interval subdensities before invoking `D_5`, partner r27 has `k=5`, `alpha_i=beta_j=1`, and all ten cell masses equal `1/N`. Equation (1.1) therefore gives for each cell

`||p_cell||_infinity`
` <=5 sqrt(2e) (1/N)^(10*(1-1/5))`
` =5 sqrt(2e) N^(-8).`                                        (6.5)

There are `N^10` product cells, so summing those black-box estimates yields only

`5 sqrt(2e) N^2`.                                              (6.6)

By contrast, the **safe probability-level localization** does not split (6.4): `f_N` itself is already one extreme marginal of Theorem 2.1. Thus (6.3) applies directly and is independent of `N`, of the fragment locations, and of all moments.

For a completely arbitrary cap-one marginal, Theorem 2.1 approximates it by a convex mixture of such whole unit-mass extremes; applying (6.3) to every product component and averaging gives again exactly

`boxed( ||p_Q||_infinity <= 5 sqrt(2e) )`                      (6.7)

with **no `N^2`, fragment-count, diameter, translation or tail factor**.

The same argument survives arbitrary outside original-coordinate conditioning whenever the probability-level analytic theorem is uniform in the resulting affine parameters; Theorem 3.1 supplies the formal averaging step.

This is an actual use of the completed account02/B14 r27 mass exponents, not a copied citation: equations (6.5)-(6.6) identify exactly where the partner's subprobability homogeneity loses `N^2`, and equations (2.1)-(4.4) show how to preserve the probability theorem's original constant instead.

## 7. Consequence for the QFORM proof architecture

The localization debt separates cleanly into two layers.

1. **Law layer, paid at probability level.** Any probability-level small-ball theorem that is uniform over bounded finite-union unit-indicator product laws and over its conditioning-generated affine parameters extends with the identical constant to all cap-one product laws. Arbitrary shifts, distant fragments and unbounded supports create no extra constant. There is no need to assume a bounded support diameter or a uniform fragment count.

2. **Analytic/matrix layer, still open globally.** One must first expose a probability-level ridge, volume, physical-core, mixed-hub, pair-log, grouped-bank or other valid certificate from the bare spectral hypothesis `s_3(A)>=1`. Splitting active extreme supports into normalized interval fragments before reciprocal curvature/volume payment is not a valid substitute: partner r27 quantifies the resulting `N^2` loss.

Thus the remaining obstruction for the full theorem is structural/analytic, not a need for support truncation or moment control. This report does **not** prove that the current matrix certificates are exhaustive and therefore does not claim the full conjecture.

## 8. Integrity and scope

No law-uniform pointwise quadratic Fourier decay is used. No arbitrary-joint coarea estimate is used. No post-rotation independence is asserted. No positive moment of a worst conditional projection-density cap is used. No support radius, fragment count, moment, tail, or perturbative-random-variable assumption enters.

The full conjecture remains OPEN. The proved statement is a supporting exact localization reconciliation preserving the full density constant once a probability-level analytic certificate is available.
