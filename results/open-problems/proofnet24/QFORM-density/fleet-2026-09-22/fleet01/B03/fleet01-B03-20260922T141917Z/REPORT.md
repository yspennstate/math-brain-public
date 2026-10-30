# fleet01/B03 — rank-two fractional trace from decoupled time integration

**Run:** `fleet01-B03-20260922T141917Z`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Decoupled time integral  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target, source state, and correction discipline

The full target is unchanged: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove one universal essential-supremum bound for the density of `X^T A X`, or give a genuine counterexample. Continuity is a separate requested conclusion.

This report does **not** use the refuted law-uniform pointwise Fresnel estimate, does not rotate the input vector and declare spectral coordinates independent, and does not condition on a sum/difference variable and retain a unit density cap. It instead derives an integrated `|t|^{-1/2}` Fourier estimate, exactly the fractional trace needed after one quadratic pivot.

Dependencies actually source-read before this proof:

1. `QFORM-REGULARIZED-DETERMINANT-v1`, `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`. For an original-coordinate cut `B=A[I,J]`, under range leverage at most `1/2` on one side,
   
   `|phi_Q(t)| <= det(I+2 t^2 B B^T/(pi^2 e^2))^(-1/4)`.
   
   The same report states the two-part MSS partition consequence for a tight frame.
2. `QFORM-INDEFINITE-PRODUCT-FRACTIONAL-TRACE-v1`, `yspennstate/math-open-problems@1defc84f1bfd79994a103a6d683c887d9dead1e7`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/B16-20260922T135620Z-r11/REPORT.md`. Its weak-`L^2` product trace estimate is used in the heavy-row branch.
3. Sharp one-dimensional product marginal cap from `yspennstate/math-open-problems@1f85677029fc5ae27fc69b278620ae89d789efd2`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260922T132134Z-fleet04-B20-QFORM-r1/REPORT.md`: every normalized original-coordinate linear aggregate has density cap at most `sqrt(2)`.
4. Named assignment partner `fleet02/B03`, `yspennstate/math-open-problems@24fc7b37c60f77b399936faa7f280296a7ce8c8c`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260922T131240Z-b03-qform-auto11/REPORT.md`. Its exact coloop-bank family and the failure of every rank-three original-coordinate cut are applied in Section 7.

## 2. Abel/Riesz bridge from time integration to fractional trace

Let `R` be a real random variable with characteristic function `phi_R(t)=E exp(itR)`. If

`int_R |phi_R(t)| |t|^(-1/2) dt < infinity`,

then

`sup_z E |z-R|^(-1/2)
 <= (2 pi)^(-1/2) int_R |phi_R(t)| |t|^(-1/2) dt`.                 (2.1)

A short rigorous proof avoids any unproved density regularity. For `epsilon>0`, put

`k_epsilon(x)=(2 pi)^(-1/2) int_R exp(-itx) exp(-epsilon |t|) |t|^(-1/2) dt`.

The Gamma integral gives

`k_epsilon(x)=sqrt(2) Re (epsilon+i x)^(-1/2) >=0`,

and `k_epsilon(x)->|x|^(-1/2)` for every `x!=0` (with the limit `+infinity` at zero). Fubini is legitimate at fixed `epsilon`, hence

`E k_epsilon(z-R)
 =(2 pi)^(-1/2) int exp(-itz) exp(-epsilon|t|) phi_R(t)|t|^(-1/2)dt`.

Fatou and the assumed weighted `L^1` bound give (2.1).

This is the exact integrated replacement for a false pointwise one-dimensional oscillatory bound.

## 3. A two-singular-value weighted integral

For every `a,b>0`,

`int_0^infinity t^(-1/2)
 [(1+a^2 t^2)(1+b^2 t^2)]^(-1/4) dt
 <=4 (ab)^(-1/4)`.                                               (3.1)

Proof. Assume `a>=b` and write `R=a/b>=1`. Split at `1/a` and `1/b`.

* On `[0,1/a]`, the integral is at most `2a^(-1/2)`.
* On `[1/a,1/b]`, it is at most `a^(-1/2) log R`.
* On `[1/b,infinity)`, it is at most `2a^(-1/2)`.

Thus the total is at most `a^(-1/2)(4+log R)`. Since `(4+s)e^{-s/4}` is decreasing for `s>=0`, `4+log R<=4R^(1/4)`, proving (3.1). Therefore the corresponding integral on all of `R` is at most `8(ab)^(-1/4)`.

## 4. Main theorem: arbitrary rotated exact-rank-two quadratic forms

### Theorem `QFORM-RANK2-FRACTIONAL-TRACE-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities bounded by one. Let

`A=U Lambda U^T`, `U^T U=I_2`,

where `Lambda` is an invertible real symmetric `2x2` matrix. Put

`D=|det Lambda|`,

which is the absolute product of the two nonzero eigenvalues of `A`. Then

`boxed{
 sup_z E |z-X^T A X|^(-1/2)
 <=48 sqrt(10) D^(-1/4).
}`                                                                    (4.1)

No moments, support assumptions, log-concavity, post-rotation independence, or sign restriction on `Lambda` are used.

### 4.1 Diffuse-row branch

Write the rows of `U` as `u_i^T` and their leverages as `ell_i=||u_i||^2`. Suppose first

`max_i ell_i <=1/18`.                                                (4.2)

Apply the two-part Marcus--Spielman--Srivastava partition theorem to the tight frame `sum_i u_i u_i^T=I_2`. Since

`(1/sqrt(2)+sqrt(1/18))^2 = 8/9`,

there is a partition of the **original coordinates** into `S,T` for which

`(1/9)I_2 <= G_S:=U_S^T U_S <=(8/9)I_2`,
`(1/9)I_2 <= G_T:=U_T^T U_T <=(8/9)I_2`.                             (4.3)

Let `B=A[S,T]=U_S Lambda U_T^T`. It has rank two. If `s_1,s_2` are its two nonzero singular values, then

`Delta:=s_1s_2
 =D sqrt(det G_S det G_T)
 >=D/81`.                                                            (4.4)

Moreover `range(B)=range(U_S)`, and the coordinate leverage on the `S` side is

`u_i^T G_S^(-1)u_i <=9 ell_i <=1/2`.                                 (4.5)

The regularized-determinant theorem with `q=1` therefore applies to the **actual** characteristic function of `X^TAX`:

`|phi(t)|
 <=[(1+c t^2 s_1^2)(1+c t^2 s_2^2)]^(-1/4),
 c=2/(pi^2 e^2)`.                                                    (4.6)

By (3.1) on both half-lines,

`int_R |phi(t)||t|^(-1/2)dt
 <=8 c^(-1/4) Delta^(-1/4)`.                                        (4.7)

Insert (4.4) into (4.7), then use the Abel/Riesz bridge (2.1):

`sup_z E|z-X^TAX|^(-1/2)
 <=3*2^(9/4)*sqrt(e) D^(-1/4)
 <24 D^(-1/4)`.                                                      (4.8)

This branch keeps the original-coordinate product law throughout.

### 4.2 Heavy-row branch

Now suppose some row has

`ell:=ell_i >=1/18`.                                                 (4.9)

Rotate only the **two-dimensional spectral representation**, not the random input, so that

`u_i=(sqrt(ell),0)`.

For `j!=i` write `u_j=(a_j,b_j)` and define

`W=sum_{j!=i} a_j X_j`, `Z=sum_{j!=i} b_j X_j`.

Column orthonormality gives

`sum_{j!=i} b_j^2=1`.                                                (4.10)

Hence, by the sharp one-dimensional product-marginal theorem, `Z` has a density cap

`M_Z<=sqrt(2)`.                                                       (4.11)

Write, in this rotated spectral basis,

`Lambda=[[alpha,beta],[beta,gamma]]`.

#### Case alpha !=0

The quadratic form is exactly

`Q=alpha(sqrt(ell)X_i+W+(beta/alpha)Z)^2
  +(det Lambda/alpha) Z^2`.                                         (4.12)

Condition on all variables except `X_i`; the shift of `X_i` in (4.12) preserves its unit density cap. The weak-`L^2` product-trace estimate underlying `QFORM-INDEFINITE-PRODUCT-FRACTIONAL-TRACE-v1` also works with either sign of the second square, because `Psi(a-y^2)=Psi(-a+y^2)`. Scaling a second marginal of density cap `M_Z` gives

`sup_z E|z-Q|^(-1/2)
 <=16 sqrt(15) M_Z^(1/2) (ell D)^(-1/4)`.                            (4.13)

Using (4.9)--(4.11),

`16 sqrt(15) *2^(1/4)*18^(1/4)
 =48 sqrt(10)`.                                                       (4.14)

Thus (4.1) holds.

#### Case alpha=0

Invertibility gives `beta!=0` and `D=beta^2`. Now

`Q=2 beta sqrt(ell) Z X_i + H(W,Z)`                                  (4.15)

for a function `H` independent of `X_i`. For every unit-cap probability density `f`, the bathtub principle gives

`sup_a int f(x)|a-cx|^(-1/2)dx <=2 sqrt(2)|c|^(-1/2)`.               (4.16)

Conditioning on `(W,Z)` and using (4.15) therefore yields

`E_{X_i}|z-Q|^(-1/2)
 <=2 |beta|^(-1/2) ell^(-1/4)|Z|^(-1/2)`.                            (4.17)

A probability density of cap `M` satisfies

`E|Z|^(-1/2)<=2 sqrt(2M)`                                            (4.18)

again by the centered-interval bathtub bound. With `M=M_Z<=sqrt(2)` and `ell>=1/18`, (4.17)--(4.18) give a constant below `48 sqrt(10) D^(-1/4)` (indeed below `16 D^(-1/4)` if the stronger threshold `ell>=1/32` is used, and still far below the generic constant here). This completes the heavy branch and proves (4.1).

## 5. Exact-rank-three consequence after one nonisotropic heavy pivot

Let now

`A=U Lambda U^T`, `U^TU=I_3`,

have exact rank three. Pick a row `u_i` with leverage `ell=||u_i||^2>0`, rotate the three-dimensional spectral representation so `u_i=sqrt(ell)e_1`, and write

`alpha=e_1^T Lambda e_1`.

If `alpha!=0`, completing the square in the physical coordinate `X_i` gives

`Q=alpha ell (X_i+shift(X_{-i}))^2 + R(X_{-i})`,                    (5.1)

where `R` is an exact-rank-two quadratic form on the remaining **independent original coordinates**. Its nonzero spectral matrix is the Schur complement

`S=Gamma-beta beta^T/alpha`,

and

`|det S|=|det Lambda|/|alpha|`.                                      (5.2)

For fixed `X_{-i}`, the one-variable square pushforward bound gives

`p_Q(t)
 <=(|alpha| ell)^(-1/2)
   E |t-R|^(-1/2)`.                                                  (5.3)

Applying Theorem 4.1 to `R` and (5.2),

`boxed{
 ||p_Q||_infinity
 <=48 sqrt(10)
   ell^(-1/2)|alpha|^(-1/4)|det Lambda|^(-1/4).
}`                                                                    (5.4)

Thus every exact-rank-three form with a heavy original-coordinate row that is quantitatively away from the `Lambda`-isotropic cone is paid by an integrated decoupled-time argument. Under the owner normalization `|lambda_1|,|lambda_2|,|lambda_3|>=1`, the determinant factor in (5.4) is at most one.

The remaining exact-rank-three obstruction is now sharply localized: leverage-heavy rows can lie arbitrarily near the indefinite null cone `u^T Lambda u=0`, where the scalar quadratic pivot loses strength. Additional eigendirections in the full problem remain a separate interaction debt.

## 6. Why this is a genuine integrated estimate

The proof never asks for a pointwise law-uniform `|t|^{-1/2}` Fresnel estimate. In the diffuse branch it controls the weighted time integral

`int |phi(t)| |t|^(-1/2)dt`,

using an original-coordinate cross block and determinant regularization. The weight is exactly the Fourier multiplier of the square-root kernel generated by one quadratic pivot. In the heavy branch the same kernel is paid directly by source-product weak-`L^2` integration. The two branches therefore implement the same decoupled-time quantity by complementary mechanisms.

## 7. Named partner application: the coloop-bank obstruction is paid without a rank-three cut

The latest completed named partner `fleet02/B03` produced the exact family

`A_m=[1] direct_sum (J_m/m) direct_sum (-J_m/m)`,                    (7.1)

with nonzero spectrum `(1,1,-1)`, every original-coordinate cross cut of rank at most two, and every nonsingular physical triple degenerating like `1/m`. The partner also writes

`Q_m=X_0^2+P_m^2-R_m^2`.                                            (7.2)

Apply (5.4) to the partner's family using its hub row: `ell=1`, `alpha=1`, `|det Lambda|=1`. This gives the actual dimension-free inequality

`boxed{ ||p_{Q_m}||_infinity <=48 sqrt(10) }`                        (7.3)

for every `m` and every admissible product input law, despite the complete absence of a rank-three cross cut.

The partner's bank-specific sharp aggregation gives the much better `pi sqrt(2)` bound. Equation (7.3) is not offered as a constant improvement; its significance is structural: a single nonisotropic heavy pivot plus the new **arbitrary rotated rank-two fractional trace** pays a family that defeats both the fixed-triple and rank-three-cut mechanisms.

## 8. Status and first unpaid implication

- `QFORM-FULL`: **OPEN**.
- `QFORM-RANK2-FRACTIONAL-TRACE-v1`: **PROVED**, equation (4.1).
- heavy nonisotropic exact-rank-three branch: **PROVED**, equation (5.4).
- named partner `fleet02/B03` coloop-bank family: **APPLIED** to the actual density inequality (7.3).
- continuity: **NOT proved** by the new branch; only absolute continuity with an essentially bounded density is obtained in (5.4).
- execution: `WITHOUT_VERIFIED_BRAIN`.

The first unpaid implication is an **isotropic-heavy-row bridge**: for an exact-rank-three indefinite frame in which the rows carrying substantial leverage satisfy `|u_i^T Lambda u_i|/||u_i||^2` very small, exploit a two-coordinate/bilinear pivot or prove that the remaining diffuse mass supplies a decoupled cut. Any such bridge must then be made robust to arbitrary additional spectral directions without discarding their couplings.

No full-solution status is claimed.
