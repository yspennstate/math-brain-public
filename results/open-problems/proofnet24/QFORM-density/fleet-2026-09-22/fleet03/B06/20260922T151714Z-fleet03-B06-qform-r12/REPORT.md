# fleet03/B06 — two-stage curved pivot endpoint certificate

**Run:** `20260922T151714Z-fleet03-B06-qform-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Curved fiber integration  
**Classification:** `ESSENTIAL_STEP_APPLIED / TWO_STAGE_PIVOT_ENDPOINT_CERTIFICATE / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction-aware mechanism change

The full target remains open: for every dimension, every product law with independent real coordinates whose densities are bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove one universal essential bound for the density of `X^T A X`, or produce a genuine target counterexample. Continuity is a separate requested conclusion and is not inferred below.

This run changes mechanism from the previous heavy-isotropic all-finite-`Lp` endpoint attempt. Instead of trying to spend the third curvature directly in a spectral fiber, it derives an original-coordinate **two-stage Schur-pivot certificate**. The proof uses curved square kernels twice and never rotates the independent coordinates. It does not use the false law-uniform pointwise Fresnel decay, an unrestricted spectral-fiber supremum, a generic X-ray-only trace estimate, or a conditional-density claim created by spectral rotation.

The exact assigned partner is `fleet04/B06`. No completed current-QFORM artifact existed at its canonical handoff root at the fresh startup snapshot, so no result or PASS is fabricated. A compatible completed fleet04 result is applied at inequality level: fleet04/B18, scientific commit `441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, proves the dependent square-kernel domination used twice below.

The one-dimensional product projection input is source-pinned to fleet03/B02, scientific commit `18fb381e300dd86514835d27eedcf2507ab09227`: if independent coordinates have densities at most one and `v` is a unit coefficient vector, then `v.X` has density at most `sqrt(2)` (Rogozin comparison plus Ball cube slicing / Rudelson--Vershynin).

## 2. A rank-one square has a uniform `L^(6/5)` bank

### Lemma 2.1 — `QFORM-RANK1-SQUARE-L65-v1`

Let `L=sum_j v_j X_j`, where the `X_j` are independent with densities at most one and `sum_j v_j^2=1`. Let `gamma!=0` and `R=gamma L^2`. Then `R` has a density `q` satisfying

`||q||_(6/5) <= D * 2^(1/6) * |gamma|^(-1/6)`,                     (2.1)

where

`D=(15/2)^(5/6)<5.361`.                                               (2.2)

#### Proof

Let `m` be the density of `L`. The product-projection theorem gives `||m||_infinity<=H=sqrt(2)`. For definiteness take `gamma>0`; reflection handles `gamma<0`. For `r>0`,

`q(r)=[m(sqrt(r/gamma))+m(-sqrt(r/gamma))]/[2 sqrt(gamma r)]`

and therefore

`q(r)<=K r^(-1/2)`,  `K=H/sqrt(|gamma|)`.                            (2.3)

Since `q` is a probability density,

`|{q>s}|<=1/s`.                                                        (2.4)

The pointwise cap (2.3) also implies

`|{q>s}|<=K^2/s^2`.                                                    (2.5)

Using the layer-cake identity with `p=6/5` and splitting at `s=K^2`,

`||q||_p^p
 = p int_0^infinity s^(p-1)|{q>s}| ds`
`<= p[ int_0^(K^2) s^(p-2) ds + K^2 int_(K^2)^infinity s^(p-3) ds ]`
`= (15/2) K^(2/5)`.                                                   (2.6)

Raising to the power `5/6` gives

`||q||_(6/5)<=D K^(1/3)=D 2^(1/6)|gamma|^(-1/6)`.                    (2.7)

QED.

The rare square-root singularity is kept explicitly; no continuity estimate hides it.

## 3. An explicit `L^(6/5) -> L^3` half-Riesz estimate

Let

`Tf(t)=int_R f(r)|t-r|^(-1/2) dr`.                                   (3.1)

### Lemma 3.1 — `QFORM-HALF-RIESZ-65-TO-3-v1`

For every probability density `f in L^(6/5)`,

`||Tf||_3 <= C_H ||f||_(6/5)`,                                       (3.2)

with the explicit safe constant

`C_H=2[48(1+sqrt(2))]^(2/5)<13.386`.                                 (3.3)

#### Proof

Let `F=||f||_(6/5)` and let `Mf` be the centered Hardy--Littlewood maximal function. For `delta>0`, split (3.1) at distance `delta`. On dyadic annuli inside `delta`,

`int_(|u|<delta) f(t-u)|u|^(-1/2)du`
`<= A delta^(1/2) Mf(t)`,                                             (3.4)

where

`A=2 sqrt(2) sum_(k>=0)2^(-k/2)=4(1+sqrt(2))`.                       (3.5)

For the far part, Holder with exponents `6/5` and `6` gives

`int_(|u|>=delta) f(t-u)|u|^(-1/2)du <= F delta^(-1/3)`.              (3.6)

Choosing `delta=(F/(A Mf(t)))^(6/5)` (with the zero cases interpreted by limit) yields

`Tf(t)<=2 A^(2/5) F^(3/5) Mf(t)^(2/5)`.                              (3.7)

The standard one-dimensional maximal theorem gives the deliberately crude explicit bound

`||Mf||_(6/5)<=12||f||_(6/5)`.                                       (3.8)

Taking `L^3` in (3.7) therefore gives (3.2)--(3.3). QED.

No Fourier pointwise decay enters.

## 4. New rank-two theorem: every nonzero physical pivot pays `L^3`

Let `S` be a real symmetric rank-two matrix acting on independent original coordinates. Choose a physical coordinate `k` with

`b=S_kk !=0`.                                                         (4.1)

Complete the square only in `X_k`:

`X^T S X = b (X_k+h(X_-k))^2 + R_1(X_-k)`,                           (4.2)

where the Schur complement has rank one. Write it as

`R_1=gamma L^2`,                                                      (4.3)

with `||v||_2=1` in `L=v.X_-k` and `gamma!=0`.

### Theorem 4.1 — `QFORM-RANK2-PHYSICAL-PIVOT-L3-v1`

Under (4.1)--(4.3),

`||p_(X^T S X)||_3
 <= C_2 |b|^(-1/2)|gamma|^(-1/6)`,                                  (4.4)

where

`C_2=C_H D 2^(1/6)<80.543`.                                          (4.5)

#### Proof

Condition on the residual coordinates. The shifted variable

`V=X_k+h(X_-k)`                                                       (4.6)

has, conditional on the residual vector, a translate of the original density of `X_k`, hence density at most one. Disintegrating further only over the value `R_1=r` turns that law into a mixture of such translates, so the conditional density of `V | R_1=r` is still at most one.

The exact proof inequality from fleet04/B18 therefore applies:

`p_(X^T S X)(t)
 <= |b|^(-1/2) int p_(R_1)(r)|t-r|^(-1/2)dr`.                        (4.7)

Insert Lemma 3.1 and then Lemma 2.1. This gives (4.4). QED.

This is the promised concrete application of the completed fleet04 square-smoothing result. It treats definite and indefinite rank-two residual forms uniformly whenever one actual physical diagonal pivot is nonzero. The logarithmic rank-two singularity is allowed; only its `L^3` size is controlled.

## 5. Two-stage rank-three endpoint theorem

Now let `A` be a real symmetric matrix of **exact rank three**,

`A=R Lambda R^T`,  `R^T R=I_3`,                                     (5.1)

and assume the three nonzero eigenvalues (the diagonal entries of `Lambda` after spectral diagonalization) have modulus at least one. The input coordinates remain the original independent coordinates; (5.1) is used only for identities.

Choose two distinct physical coordinates `i,k` and define

`a=A_ii`,                                                            (5.2)

`d=d_ik=A_ii A_kk-A_ik^2`.                                          (5.3)

Assume

`a!=0`, `d!=0`.                                                       (5.4)

Let `r_i,r_k in R^3` be the corresponding rows of `R`, and put

`Delta_ik = det([[<r_i,r_i>,<r_i,r_k>],[<r_k,r_i>,<r_k,r_k>]])`
`         = ||r_i wedge r_k||^2 >0`.                                 (5.5)

First complete the square in `X_i`. The residual Schur form `S_i` has rank two, and its physical `k`-diagonal is exactly

`b=(S_i)_kk=d/a`.                                                     (5.6)

After the second physical pivot, the remaining Schur form has rank one. Let `gamma` be its sole nonzero eigenvalue.

### Lemma 5.1 — exact two-pivot spectral determinant identity

`gamma = det(Lambda) Delta_ik / d`.                                  (5.7)

#### Proof

Let `U` be the `2x3` matrix with rows `r_i,r_k`. The selected physical block is

`A_II=U Lambda U^T`,                                                  (5.8)

with determinant `d`. Eliminating these two coordinates in the rank-three factorization leaves a rank-one Schur complement. The standard Schur/Cauchy--Binet pseudodeterminant identity gives

`pdet(S_after_I)
 = det(Lambda) det(UU^T)/det(U Lambda U^T)`.                          (5.9)

Since the Schur complement has rank one, its pseudodeterminant is its unique nonzero eigenvalue. Since `det(UU^T)=Delta_ik`, (5.7) follows. QED.

A direct determinant proof can equivalently be obtained by orthogonally rotating the three-dimensional coefficient space so that `span{r_i,r_k}` is the first two coordinate directions; this rotates only the algebraic factorization, not the independent random variables.

### Theorem 5.2 — `QFORM-RANK3-TWO-PIVOT-ENDPOINT-v1`

Under (5.1)--(5.5), the law of `Q=X^TAX` has an essentially bounded density satisfying

`||p_Q||_infinity
 <= C_3 [ |a| |d|^2 |det Lambda| Delta_ik ]^(-1/8)`,                 (5.10)

where

`C_3=(8/3^(3/4)) C_2^(3/4) <94.356`.                                (5.11)

#### Proof

After the first physical completion,

`Q=a(X_i+h_i(X_-i))^2 + R_i(X_-i)`,                                 (5.12)

where `R_i` is the rank-two Schur form. Theorem 4.1 applied to its physical coordinate `k` gives

`M:=||p_(R_i)||_3
 <= C_2 |d/a|^(-1/2)|gamma|^(-1/6)`.                                (5.13)

The same fleet04/B18 kernel domination applies to (5.12): conditional on `R_i=r`, the shifted `X_i` is a mixture of translates of the original cap-one density, hence

`p_Q(t)<=|a|^(-1/2) int_(one side) p_(R_i)(r)|t-r|^(-1/2)dr`.        (5.14)

For a probability density `h` with `||h||_3=M`, split the one-sided integral at `rho`. Holder on the near part and mass one on the far part give

`int_0^infinity h(t-u)u^(-1/2)du
 <= 2^(4/3) M rho^(1/6)+rho^(-1/2)`.                                 (5.15)

Optimizing at `rho^(2/3)=3/(2^(4/3)M)` gives

`<= [8/3^(3/4)] M^(3/4)`.                                           (5.16)

Combining (5.13)--(5.16), then using (5.6)--(5.7), yields

`||p_Q||_infinity
 <= (8/3^(3/4)) C_2^(3/4)
    |a|^(-1/2)|d/a|^(-3/8)|det(Lambda)Delta_ik/d|^(-1/8)`
` = C_3 |a|^(-1/8)|d|^(-1/4)(|det Lambda|Delta_ik)^(-1/8)`,           (5.17)

which is exactly (5.10). QED.

### Interpretation

The theorem converts one physical diagonal pivot, one physical `2x2` principal determinant, and the corresponding spectral two-row area into a genuine endpoint density certificate. It keeps the distributed spectral geometry quantitatively rather than replacing a curved intersection by a fiber maximum.

Because `|det Lambda|>=1` under the exact-rank-three target threshold, a branch with

`|a| |d|^2 Delta_ik >= eta`                                          (5.18)

has the explicit target bound `94.356 eta^(-1/8)`.

This certificate is substantially less singular than a reciprocal smallest-eigenvalue or reciprocal determinant bound because every geometric payment appears with exponent at most `1/4`, and the spectral row-area only with exponent `1/8`.

## 6. Why this does not yet prove the full conjecture

The remaining structural implication is genuinely nonlocal:

`QFORM-TWO-PIVOT-CERTIFICATE-OR-AGGREGATE-v1` — starting only from three large eigenvalues, prove that either some ordered physical pair `(i,k)` makes the certificate quantity

`J_ik=|A_ii| |A_ii A_kk-A_ik^2|^2 ||r_i wedge r_k||^2`               (6.1)

uniformly positive, **or** aggregate the many small `J_ik` channels before inversion by a product-preserving curved-fiber inequality.

A uniform lower bound on a single `J_ik` is false in fully delocalized frames: all physical rows can have size `O(n^(-1/2))`, making every fixed local certificate tiny. Existing diffuse full-range arguments handle part of that regime, but a heavy-coordinate plus diffuse-residual configuration is not automatically covered. Therefore (5.10) is a real branch theorem, not a hidden fixed-minor claim.

The exact-rank-three restriction is also material. If `A` has further nonzero spectral components, a two-pivot Schur complement is no longer rank one after the second pivot, and those correlated components cannot simply be convolved away.

## 7. Relation to the previous heavy-isotropic endpoint debt

The preceding B06 run proved all finite `Lp` bounds in the heavy-isotropic normal form

`Q=2B(sqrt(c)X_i+T)Y+rY^2+2sYZ+tau Z^2`

without transverse diffuseness, but stopped before `L^infinity`. Theorem 5.2 attacks that endpoint from the opposite direction: rather than condition on the spectral light-cone coordinate `Y`, it looks for two actual original-coordinate pivots and transports the residual singularity through two half-Riesz kernels.

If a heavy-isotropic instance has a pair `(j,k)` away from the isotropic heavy row with certificate (6.1) bounded below, Theorem 5.2 closes that exact-rank-three instance immediately. The genuinely unpaid part is therefore the distributed regime where **every** such two-pivot certificate is small and the curvature must be aggregated across many original coordinates.

That is a sharper target for the assigned curved-fiber programme than the previous generic instruction to “spend the third curvature.”

## 8. Continuity status

Theorem 5.2 proves absolute continuity with an essentially bounded density. The argument is based on positive kernel domination and `Lp` estimates; it does **not** prove that the density has a continuous representative. Continuity remains separately open on this branch.

## 9. Status and provenance

Proved in this report:

- `QFORM-RANK1-SQUARE-L65-v1`;
- `QFORM-HALF-RIESZ-65-TO-3-v1`;
- `QFORM-RANK2-PHYSICAL-PIVOT-L3-v1`;
- `QFORM-RANK3-TWO-PIVOT-ENDPOINT-v1`.

Actually applied peer mathematics:

- fleet04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`;
- fleet03/B02 product projection bound, `yspennstate/math-open-problems@18fb381e300dd86514835d27eedcf2507ab09227`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T130245Z-fleet03-B02-QFORM-r11/REPORT.md`.

The exact assigned partner `fleet04/B06` had no completed canonical QFORM handoff at the startup snapshot and was not impersonated. The full conjecture remains **OPEN / NOT PROVED**.
