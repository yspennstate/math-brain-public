# QFORM B01 — weighted Riesz square-lift below the ordinary L1 threshold

Run: `20260922T151044Z-b01-qform-auto11c`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: account01/B01, Oscillatory replacement  
Status: **ESSENTIAL_STEP_APPLIED / supporting theorem proved / full target OPEN / WITHOUT_VERIFIED_BRAIN**

## 1. Exact target and preserved correction

The sole target remains: for independent real coordinates with probability densities bounded by one and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal essential-supremum bound for the density of `Q=X^TAX`, or give a valid target-level counterexample. Continuity is a separate desired conclusion.

The phase-aligned fragmented-support construction remains decisive: bounded scalar density alone does not imply any law-uniform pointwise power decay for `E exp(it X^2)`. Nothing below uses such a pointwise scalar Fresnel estimate. The mechanism is instead a **weighted integrated Fourier estimate**.

## 2. Source-pinned inputs actually consumed

### 2.1 Regularized determinant theorem

Canonical proof:

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

path

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

For any quadratic form `R(Y)=Y^T C Y`, any disjoint original-coordinate cut with cross block `B=C[I,J]`, and `1<=q<2`, if the diagonal of the orthogonal projection onto `range(B)` on one side is at most `q/2`, then

`|phi_R(t)| <= det(I + 2q t^2 BB^T/(pi^2 e^2))^(-1/(4q)).`      (2.1)

For `q=2` the same estimate holds without a leverage condition. Arbitrary self-block phases and outside couplings are retained.

### 2.2 Assigned partner account02/B01 r22

Canonical proof:

`yspennstate/math-open-problems@08e91d2cd50db663646e7c25983c421ccaa78c7c`

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260922T150052Z-account02-B01-qform-r22/REPORT.md`.

For a physical triple `I`, arbitrary outside bank `K`, rank-two `M=C[I,K]`, unit `nu` spanning `ker(M^T)`, transverse curvature `b=nu^T C[I,I]nu !=0`, and

`Delta_2=sqrt(pdet(MM^T))`,

that theorem proves a continuous residual density with

`M_R := ||p_R||_infinity`
` <= 1/pi + 4 sqrt(2) pi^(1/3) Delta_2^(-1/2)`
`       * max(3^(1/4), |b|^(-1/4)).`                            (2.2)

This partner theorem is applied below to an actual new lifted inequality, not cited only nominally.

### 2.3 Comparison theorem

Account03/B04 `QFORM-SQUARE-ASSISTED-L32-v1`, canonical proof

`yspennstate/math-open-problems@f447c650e04ef27d14be3380ac541c1cec60ab0c`

path

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/B04-20260922T145033Z-r12/REPORT.md`,

uses the same determinant estimate through an `L^(3/2)_t -> L^3 -> half-Riesz` route. Its rank-two branch requires `r>4q/3`; the direct weighted-Riesz argument below lowers this to `r>q` and gives a smaller endpoint constant.

## 3. Exact half-Riesz Fourier identity

Let `R` be any real random variable with characteristic function `phi_R(t)=E exp(itR)`. Assume

`J_R := integral_R |t|^(-1/2) |phi_R(t)| dt < infinity.`         (3.1)

Then for every real `x`,

`E |x-R|^(-1/2)`
` = (1/sqrt(2pi)) integral_R exp(itx) phi_R(-t) |t|^(-1/2) dt`,  (3.2)

and therefore

`sup_x E |x-R|^(-1/2) <= J_R/sqrt(2pi).`                         (3.3)

A direct justification avoiding distributional ambiguity is the Gaussian representation

`|z|^(-1/2)=Gamma(1/4)^(-1) integral_0^infinity s^(-3/4) exp(-s z^2) ds`.

Insert the ordinary Fourier representation of the Gaussian. The inner `s` integral equals

`4^(1/4) Gamma(1/4) |t|^(-1/2)`,

leaving exactly the factor `1/sqrt(2pi)` in (3.2). Assumption (3.1) permits the final absolute interchange.

## 4. Scalar-square lift

Let `X` be an original coordinate, independent of `Y`, with density at most one. Let `a!=0`, let `m(Y)` be any finite measurable function, and let `R(Y)` be any real random variable. Put

`Q = a (X+m(Y))^2 + R(Y).`                                     (4.1)

Conditionally on `Y`, the square term has density bounded by

`|a|^(-1/2) |u|^(-1/2)`

on the appropriate half-line. Hence the mixture is absolutely continuous and

`p_Q(x) <= |a|^(-1/2) E |x-R|^(-1/2).`                          (4.2)

Combining (3.3) and (4.2),

`||p_Q||_infinity <= J_R / sqrt(2pi |a|).`                       (4.3)

This is the basic square-lift: it needs a weighted `L^1` Fourier budget for the residual, not ordinary `L^1` integrability of `phi_R`.

## 5. New theorem — the cross-rank threshold drops from `r>2q` to `r>q`

### Theorem `QFORM-RIESZ-SQUARE-LIFT-v1`

Assume the residual quadratic form `R(Y)=Y^T C Y` has an original-coordinate cross block `B=C[I,J]`. Fix `1<=q<=2`. For `q<2`, assume the diagonal of the range projection of `B` on one side of the cut is at most `q/2`; for `q=2` no leverage assumption is needed. Suppose `B` has at least `r` singular values at least `sigma>0` and

`r > q.`                                                        (5.1)

Then the variable (4.1) has an essentially bounded density and

`||p_Q||_infinity <= C_R(q,r) / sqrt(|a| sigma),`                (5.2)

where

`C_R(q,r)`
` = sqrt(e) / (2^(3/4) q^(1/4))`
`   * Beta(1/4, (r-q)/(4q)).`                                   (5.3)

The theorem proves absolute continuity and the essential-supremum bound. It does **not** by itself prove continuity when `m(Y)` depends on `Y`.

### Proof

From the determinant theorem and the `r` singular values,

`|phi_R(t)| <= (1 + beta^2 t^2)^(-r/(4q)),`                     (5.4)

with

`beta=sqrt(2q) sigma/(pi e).`

Therefore

`J_R`
` <= 2 integral_0^infinity t^(-1/2)(1+beta^2 t^2)^(-r/(4q)) dt`
` = beta^(-1/2) Beta(1/4, r/(4q)-1/4).`                         (5.5)

The beta integral is finite exactly when `r>q`. Substitute (5.5) into (4.3). Since

`beta^(-1/2)/sqrt(2pi)`
` = sqrt(e)/(2^(3/4) q^(1/4) sqrt(sigma)),`

(5.2)-(5.3) follow. QED.

### Comparison with the ordinary density threshold

Without the scalar square, ordinary Fourier inversion from the same determinant estimate requires `r>2q`. The new square-lift spends the kernel `|x|^(-1/2)`, so only the weighted condition `r>q` is needed. This is precisely the missing half power.

At `q=1,r=2`,

`C_R(1,2)=7.270461147134126...`,                                (5.6)

improving the `10.748739899...` constant of the completed `L^(3/2)->L^3` route and using a direct weighted integral instead.

At `q=2,r=3` the unconditional endpoint constant is

`C_R(2,3)=9.499315272418068...`.

## 6. Anisotropic rank-two version — pay the full aggregate product, not the smallest singular value

Suppose `B` has exactly or at least two relevant singular values `s_1,s_2>0` and `q<2`. From (2.1),

`|phi_R(t)|`
` <= [(1+c_q s_1^2 t^2)(1+c_q s_2^2 t^2)]^(-1/(4q)),`

where `c_q=2q/(pi^2 e^2)`. Since

`(1+c_q s_1^2 t^2)(1+c_q s_2^2 t^2)`
` >= (1+c_q s_1 s_2 t^2)^2`,

we obtain

`|phi_R(t)| <= (1+c_q Delta_2 t^2)^(-1/(2q)),`

with `Delta_2=s_1 s_2`. Hence

`||p_Q||_infinity`
` <= C_2(q) |a|^(-1/2) Delta_2^(-1/4),`                         (6.1)

where

`C_2(q)`
` = sqrt(e)/(2^(3/4)q^(1/4))`
`   * Beta(1/4,(2-q)/(4q)),     1<=q<2.`                        (6.2)

Thus one very large and one smaller cross singular value are aggregated by their geometric mean before reciprocal payment.

For `q=1`, (6.1) is

`||p_Q||_infinity <= 7.270461148 |a|^(-1/2) Delta_2^(-1/4).`     (6.3)

## 7. Actual application to the canonical two-bank stress family

Consider

`A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`.

Its nonzero spectrum is `{1,1,-1}`. Use the singleton coordinate as the scalar pivot, so `a=1`, and split each `m`-coordinate bank into two nonempty original-coordinate halves. For `m>=4`, choose `k=floor(m/2)` coordinates of each bank on the left and the rest on the right. The residual cross block then has rank two with equal singular values

`s_m=sqrt(k(m-k))/m.`                                           (7.1)

The left range projection has diagonal `1/k` on each bank, so `q=1` is valid because `k>=2`. Consequently

`||p_Q||_infinity <= C_R(1,2)/sqrt(s_m).`                       (7.2)

For even `m`, `s_m=1/2`, giving

`||p_Q||_infinity <= 10.28198475898373... .`                    (7.3)

For every `m>=4`, `s_m>=sqrt(6)/5`, hence

`||p_Q||_infinity <= 10.387454812187682... .`                   (7.4)

This is a direct bank-level proof for the standard family that defeated every fixed physical-triple rank-two gate. It aggregates the bank **before** conditioning and uses only two residual cross directions because the physical scalar square supplies the missing half power.

## 8. Actual application of assigned partner account02/B01

The new square-lift also turns the partner's no-leverage rank-two theorem into a four-level hierarchical branch.

Assume the residual `R` satisfies the exact account02/B01 r22 hypotheses, so (2.2) holds. If a probability density `p` satisfies `||p||_infinity<=M`, then the one-dimensional bathtub principle gives

`sup_x integral |x-y|^(-1/2) p(y) dy <= 2 sqrt(2M).`            (8.1)

Indeed the maximizing cap-`M`, mass-one density occupies the centered interval of length `1/M` around the singularity.

Applying (8.1) in (4.2) gives the **new partner-lift inequality**

`||p_Q||_infinity`
` <= 2 sqrt(2/|a|)`
`    * sqrt( 1/pi + 4 sqrt(2) pi^(1/3) Delta_2^(-1/2)`
`            * max(3^(1/4),|b|^(-1/4)) ).`                     (8.2)

No leverage assumption is present in (8.2). Thus the two rank-two mechanisms are complementary:

1. if a residual rank-two cross bank has leverage strictly below one on either side, choose some `q<2` and use the new direct Riesz determinant branch, even when its transverse curvature vanishes;
2. if the leverage endpoint is bad but the physical-triple kernel curvature `b` is nonzero, use the completed account02/B01 theorem and then (8.2).

For a `3 x K` rank-two residual cross bank, write

`ell_L=max diag P_range(M)`, `ell_R=max diag P_range(M^T)`,
`ell_*=min(ell_L,ell_R)`.

If `ell_*<1`, choose `q=max(1,2 ell_*)<2` (or any slightly larger value if desired) and branch 1 closes. Therefore the currently isolated local boundary left by these two completed mechanisms is

`ell_L=ell_R=1` **and** `b=0`.                                  (8.3)

This is a substantially sharper unpaid boundary than the earlier generic statement “rank-two crossbank plus transverse curvature”. It does not solve the global spectral extraction problem.

## 9. Compact conditional end-to-end route and first unpaid implication

A potential full proof can now use the following analytic exits without any scalar pointwise Fresnel bound:

- ordinary regularized-determinant density branch when a cut supplies `r>2q` residual cross directions;
- **new square-lift branch** when a physical scalar pivot is available and the Schur-complement residual supplies only `r>q` cross directions;
- partner account02/B01 no-leverage rank-two-plus-transverse-curvature branch, lifted through (8.2);
- existing diffuse-range and aggregate hyperbolic-square branches.

The first unpaid global implication remains structural: derive, from only three eigenvalues of modulus at least one, a dimension-free heavy/diffuse decomposition that forces one of these exits without paying a tiny selected pivot/minor. For the rank-two square-assisted subproblem specifically, the analytic endpoint has now been reduced to the exceptional boundary (8.3).

The full QFORM conjecture remains OPEN. No full-proof candidate or novelty claim is made.

## 10. Exact computation used

The only numerical calculation used is the evaluation of the beta-function constants and the stress-family bound:

```python
import mpmath as mp

def C(q,r):
    return (mp.sqrt(mp.e)/(2**(mp.mpf(3)/4)*q**(mp.mpf(1)/4))
            * mp.beta(mp.mpf(1)/4,(mp.mpf(r)-q)/(4*q)))

print(C(1,2))
print(C(2,3))
print(C(1,2)*mp.sqrt(2))
smin=mp.sqrt(6)/5
print(C(1,2)/mp.sqrt(smin))
```

Output:

```text
7.270461147134126
9.499315272418068
10.28198475898373
10.387454812187682
```

The formulas themselves are exact; these decimals are only convenience values.

## 11. Source/status integrity

- `QFORM-RIESZ-SQUARE-LIFT-v1`: **proved in the stated scope**.
- anisotropic rank-two aggregate-product form (6.1): **proved in the stated scope**.
- partner-lift inequality (8.2): **proved by combining the completed account02/B01 r22 density theorem with the scalar-square half-Riesz bound**.
- canonical bank stress family: **uniformly controlled for `m>=4` by the new branch**.
- full arbitrary-matrix three-large-eigenvalue conjecture: **OPEN**.
- full continuity: **not proved by this mechanism**.
- execution context: `WITHOUT_VERIFIED_BRAIN`; repository retrieval/writeback is source transport, not native learned-memory ingestion.

No credentials, scheduler identifiers, machine paths, email, Drive, unrelated private data, benchmark material, public release, paid calls, remote workflow, permission change or cross-account authentication are included.