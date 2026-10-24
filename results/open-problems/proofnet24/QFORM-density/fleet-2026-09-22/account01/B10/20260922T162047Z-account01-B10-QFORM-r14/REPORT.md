# account01/B10 — grouped isotropic-ray saturation and heavy-cascade geometry

**Run:** `20260922T162047Z-account01-B10-QFORM-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** rank-three coupled case  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and conditional end-to-end route

The exact-rank-three target considered here is

`A = U Lambda U^T`, `U^T U = I_3`,

where `Lambda` is real symmetric invertible and all three eigenvalues have modulus at least one, while the physical coordinates `X_i` are independent with densities at most one. The full owner target also permits additional spectrum and remains open.

The current rank-three route is now:

1. diffuse frames are already paid by the completed diffuse theorems;
2. nonzero physical pivots are paid on several Schur-diffuse/nonisotropic branches;
3. account02/B10 proved that bounded-depth heavy-row deletion is not a valid closure mechanism: an arbitrarily long sequence of heavy, exactly isotropic rows can occur;
4. the first question is therefore whether the entire isotropic ray can be aggregated before any reciprocal local pivot is paid.

This report answers item 4 affirmatively when the ray is **spectrally saturated by one block of original coordinates**, allowing arbitrarily many physical variables in that block. The proof keeps an actual independent original-coordinate bank and allows arbitrary dependence inside the two-dimensional transverse projection.

It also gives an exact determinant identity for every heavy-row cascade and a quantitative ray-or-area dichotomy at the second heavy row. These identify the next unpaid mechanism: approximate/non-saturated longitudinal cascades versus macroscopic two-row spectral area with light-cone pivots.

No post-rotation independence, scalar pointwise Fresnel decay, generic fiber supremum, fixed good minor, bounded-support assumption, or conditional-density surrogate is used.

## 2. Sources used at theorem level

### 2.1 Designated partner account02/B10

The newest completed partner report is

`yspennstate/math-open-problems@9a34dc516006d7eb417687b3d7d409f7dfaf33d9`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T154900Z-account02-B10-QFORM-r13/REPORT.md`.

It proves that failure of the currently paid heavy-row branches can force a second whitened physical row of leverage `>1/2`, and it constructs, for every `K`, an exact spectrum `{1,-1,1}` example with `K` successively heavy zero-pivot rows on one isotropic ray. In that example the first `K-1` successive whitened leverages equal `2/3` and the last equals `1`. The same report applies the completed three-disjoint-bank theorem to give the actual density inequality

`||p_Q||_infinity <= 8 sqrt(2)`                                      (2.1)

for that entire family. I use both the `h>1/2` conclusion and (2.1) below; the family is therefore a structural obstruction to bounded-depth peeling, not a density obstruction.

The earlier partner theorem

`QFORM-HYPERBOLIC-SQUARE-v1`,
`yspennstate/math-open-problems@1eba911614ef9f6683f8eacb5d6608a0f9a4b833`,

also remains a paid disjoint-variable control.

### 2.2 Dependence-tolerant transverse-pair theorem

I also use the completed account03/B10 theorem

`QFORM-DEPENDENT-PAIR-HYPERBOLIC-SQUARE-v1`

from `yspennstate/math-open-problems@e660a9e78abad2a6718dd0d91dcead5a31a3a56f`, path
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/account03-B10-20260922T121625Z-qform-r11/REPORT.md`.

In the notation needed here: if `X` has density cap one, is independent of a pair `(Y,Z)` whose joint density is at most `H`, and

`T = 2 a X Y + F(Y) + b (Z+theta(Y))^2`,

then

`||p_T||_infinity <= 3*2^(2/3) H^(2/3) |a|^(-2/3)|b|^(-1/3)`.       (2.2)

If instead `X` has density cap `M`, apply (2.2) to `X'=MX`; since `X'/M=X`,

`||p_T||_infinity <= 3*2^(2/3) H^(2/3) M^(2/3)
                     |a|^(-2/3)|b|^(-1/3)`.                          (2.3)

The source-recorded product-projection bounds used by the same team give cap `sqrt(2)` for a normalized one-dimensional product projection and cap `2` for a two-dimensional orthogonal product projection.

## 3. Main theorem: aggregate an arbitrarily large saturated isotropic ray

### Theorem 3.1 — `QFORM-GROUPED-ISOTROPIC-SATURATION-v1`

Let

`A=U Lambda U^T`, `U^T U=I_3`,

with `Lambda` real symmetric invertible. Let `u_i^T` be the physical rows of `U`. Suppose there is a nonempty set of original coordinate indices `S` and a Euclidean unit vector `e in R^3` such that

`sum_{i in S} u_i u_i^T = e e^T`,                                  (3.1)

and suppose `e` is isotropic for the spectral quadratic form,

`e^T Lambda e = 0`.                                                   (3.2)

Then for independent physical inputs with densities at most one, `Q=X^TAX` has an essentially bounded density satisfying

`boxed(
 ||p_Q||_infinity
 <= 3*2^(5/3) |det Lambda|^(-1/3).
)`                                                                    (3.3)

In particular, under the exact target normalization `|lambda_r(Lambda)|>=1`,

`||p_Q||_infinity <= 3*2^(5/3) < 9.525`.                             (3.4)

The set `S` may have arbitrary cardinality. No individual row in `S` need have leverage bounded below.

### Proof

Because the left side of (3.1) is a sum of positive semidefinite rank-one matrices and the right side has range `span{e}`, every selected row lies on that ray. Thus

`u_i = alpha_i e`, `i in S`, and `sum_{i in S} alpha_i^2=1`.          (3.5)

Parseval then gives

`sum_{j notin S} u_j u_j^T = I_3-ee^T`.                              (3.6)

In particular every complementary row is orthogonal to `e`.

Define the genuine original-coordinate bank

`R = sum_{i in S} alpha_i X_i`.                                      (3.7)

The coefficient vector has Euclidean norm one. The one-dimensional product-projection theorem therefore gives

`||p_R||_infinity <= sqrt(2)`.                                       (3.8)

Most importantly, `R` is independent of every random variable formed from coordinates outside `S`.

Since (3.2) holds, `Lambda e` is Euclidean-orthogonal to `e`. Put

`B=||Lambda e||>0`, `f=Lambda e/B`,                                  (3.9)

and choose a unit `g` orthogonal to both `e` and `f`. In the orthonormal spectral basis `(e,f,g)`,

`Lambda = [[0,B,0],[B,r,s],[0,s,tau]]`.                              (3.10)

Hence

`det Lambda = -B^2 tau`,                                             (3.11)

so `tau!=0` and

`B^2 |tau| = |det Lambda|`.                                          (3.12)

For complementary physical rows write

`u_j = y_j f+z_j g`.

Equation (3.6) says exactly

`sum y_j^2=1`, `sum z_j^2=1`, `sum y_j z_j=0`.                        (3.13)

Thus the two coefficient vectors are orthonormal in the original complement coordinate space. Define

`Y=sum_{j notin S} y_j X_j`, `Z=sum_{j notin S} z_j X_j`.             (3.14)

Their joint law need not be a product law; however the completed two-dimensional product-projection theorem gives

`||p_(Y,Z)||_infinity <=2`.                                          (3.15)

By disjoint physical support, `R` is independent of the **pair** `(Y,Z)`.

The full quadratic form is now exactly

`Q = 2 B R Y + rY^2+2sYZ+tau Z^2`

`  = 2 B R Y + (r-s^2/tau)Y^2
     + tau (Z+(s/tau)Y)^2`.                                          (3.16)

Apply (2.3) with

`M=sqrt(2)`, `H=2`, `a=B`, `b=tau`.

This gives

`||p_Q||_infinity`
` <= 3*2^(2/3) * 2^(2/3) * (sqrt(2))^(2/3)
      * B^(-2/3)|tau|^(-1/3)`
` = 3*2^(5/3) (B^2|tau|)^(-1/3)`
` = 3*2^(5/3)|det Lambda|^(-1/3)`,                                  (3.17)

which is (3.3). QED.

### What was gained

The previous leverage-one isotropic theorem treated one physical coordinate carrying the whole null direction. Theorem 3.1 replaces that single coordinate by an **arbitrarily large block of original independent coordinates**. The aggregation is performed first, through the normalized bank `R`, before any local reciprocal coefficient is paid. The transverse variables are allowed to be dependent; only their joint projection density is used.

Thus the exact pure-ray mechanism behind the partner's unbounded peeling example is not merely an example that happens to be paid by three disjoint banks: the whole saturated-ray class is paid even when the two transverse spectral coordinates overlap on every complementary physical coordinate.

## 4. Exact heavy-cascade determinant identity

The bounded-depth-peeling obstruction has a simple invariant that is useful beyond the partner example.

### Lemma 4.1 — `QFORM-CASCADE-GRAM-PRODUCT-v1`

Let `u_1,...,u_m` be distinct rows selected successively from a Parseval three-frame. Put

`G_0=I_3`,
`G_k=G_{k-1}-u_k u_k^T`,                                             (4.1)

and suppose `G_{k-1}` is positive definite at the `k`th step. Define the whitened leverage

`h_k=u_k^T G_{k-1}^(-1)u_k`.                                         (4.2)

Then

`boxed( det G_m = product_{k=1}^m (1-h_k). )`                         (4.3)

In particular, if every selected row is heavy, `h_k>1/2`, then

`det G_m < 2^(-m)`.                                                   (4.4)

### Proof

The matrix determinant lemma gives

`det(G_{k-1}-u_ku_k^T)
 =det(G_{k-1})[1-u_k^T G_{k-1}^(-1)u_k]
 =det(G_{k-1})(1-h_k)`.                                               (4.5)

Iterating from `det G_0=1` proves (4.3), and (4.4) is immediate. QED.

### Exact application to the designated partner's cascade

In account02/B10 r13, the ray weights are

`w_k=2/3^k` for `k<K`, `w_K=1/3^(K-1)`.

Before the `k`th ray deletion the remaining variance on the ray is

`R_k=sum_{s=k}^K w_s=3^(-(k-1))`.                                    (4.6)

Hence, for `k<K`,

`h_k=w_k/R_k=2/3`,                                                    (4.7)

and therefore

`det G_m=(1/3)^m` for `m<K`.                                         (4.8)

The final row has leverage one and saturates the ray. At that point the full set of ray rows satisfies exactly (3.1), so Theorem 3.1 applies. Independently, the partner's disjoint-bank result supplies the actual family inequality (2.1). Thus the cascade's arbitrary length is a failure of **local termination**, not a failure of global bank anti-concentration.

## 5. The first departure from a ray has a quantitative spectral-area cost

The previous theorem pays exact saturated rays. The next question is what happens when a second heavy row leaves the first isotropic direction.

Let a physical row be

`u_i=sqrt(c)e`, `c>1/2`,                                              (5.1)

where `e` is a unit vector. Put `rho=1-c`. After deleting this row, the residual Gram matrix is

`G=I_3-c ee^T`.                                                       (5.2)

Write another physical row as

`u_j=s e+w`, `w perpendicular e`.                                    (5.3)

Then its whitened residual leverage is exactly

`h_j=u_j^T G^(-1)u_j = s^2/rho + ||w||^2,                            (5.4)

while the two-row Euclidean spectral area is

`Delta_ij=||u_i wedge u_j||^2 = c ||w||^2`.                           (5.5)

### Lemma 5.1 — `QFORM-SECOND-HEAVY-RAY-OR-AREA-v1`

If `h_j>1/2`, then for every `eta in (0,1/2)` at least one of

`(LONGITUDINAL)  s^2/rho > 1/2-eta`,                                 (5.6)

or

`(AREA)          Delta_ij > c eta > eta/2`                            (5.7)

holds.

This is immediate from (5.4)-(5.5). For the concrete choice `eta=1/8`,

`boxed(
 s^2/rho >3/8
 \quad or \quad
 Delta_ij>1/16.
)`                                                                    (5.8)

### Application to account02/B10 r13

The partner's hard two-level branch supplies exactly a second whitened row with `h_j>1/2`. Therefore (5.8) applies to every exact-isotropic first-row specialization of that branch. The hard state is not an amorphous second-heavy-row configuration: it is forced into either

1. a quantitatively longitudinal continuation of the same depleted ray, or
2. a pair carrying macroscopic spectral area `>1/16`.

This is a direct new inequality obtained by inserting the completed partner conclusion into (5.4)-(5.5).

If the first row is isotropic for `Lambda`, choose the basis (3.10) and write `w=yf+zg`. Then

`A_ij=sqrt(c) B y`,                                                   (5.9)

while

`Delta_ij=c(y^2+z^2)`.                                                (5.10)

Consequently an area departure has one of two concrete resources:

- `y^2>eta/2`, hence, since `B=||Lambda e||>=1`,

  `|A_ij| > sqrt(c eta/2) > sqrt(eta)/2`;                             (5.11)

- or `z^2>eta/2`, i.e. the departing row carries a fixed fraction of the determinant-bearing transverse `g` direction for which `B^2|tau|=|det Lambda|`.

The current corrections prevent converting either resource by selecting one arbitrary local minor: same-sign Pluecker mass and useful two-pivot support can be disjoint, and a single heavy cross coefficient plus a same-bank square can collapse to one square. The resource must therefore be aggregated before inversion.

## 6. Why exact saturation is the correct theorem boundary

It is tempting to replace (3.1) by an approximate condition such as

`sum_{i in S} u_i u_i^T approximately e e^T`.

Under the owner's hypotheses this is **not** automatically a small probabilistic perturbation. A coefficient vector of very small Euclidean norm can multiply an input variable whose law has arbitrarily remote fragmented support; no moment or support bound exists. Thus small residual spectral variance does not imply a small random leakage in probability or in any `L^p` norm.

This is why the theorem is stated at exact saturated product structure, and why the remaining approximate-ray branch requires an anti-concentration argument that keeps the residual product coordinates rather than a perturbative moment estimate.

## 7. New reduced first implication

The bounded-depth peeling route is now replaced by the following more precise obligation.

### `QFORM-RANK3-APPROX-RAY-OR-AREA-AGGREGATION-v1`

In an exact-rank-three hard state with an isotropic heavy row, iterate only while the next heavy row is in the longitudinal alternative (5.6). Prove one of:

1. the longitudinal rows can be aggregated, together with the residual original-coordinate leakage, by a product-preserving extension of Theorem 3.1 before any reciprocal pivot cost is paid; or
2. at the first area alternative (5.7), aggregate the macroscopic wedge resource with the determinant-bearing transverse direction into an existing cross-square / balanced-rank-two / two-pivot endpoint theorem without requiring a single favorable principal minor; or
3. a previously paid diffuse or nonisotropic branch fires.

The exact partner cascade lies in alternative 1 and terminates at exact saturation, hence is now fully paid by Theorem 3.1. The genuinely unresolved case is an **approximate**, not exact, ray with arbitrary product-law leakage, or a macroscopic-area departure whose physical scalar pivots remain on the light cone.

## 8. Status and regularity

- `QFORM-GROUPED-ISOTROPIC-SATURATION-v1`: **PROVED supporting theorem**.
- `QFORM-CASCADE-GRAM-PRODUCT-v1`: **PROVED exact structural identity**.
- `QFORM-SECOND-HEAVY-RAY-OR-AREA-v1`: **PROVED exact structural dichotomy**.
- Partner account02/B10 unbounded pure-ray cascade: **structurally reproduced and density-paid**, not a counterexample.
- Arbitrary exact-rank-three orientation: **OPEN**.
- Full owner target with additional spectrum: **OPEN**.
- Theorem 3.1 proves existence of an essentially bounded density in its scope. **Continuity is not proved by Theorem 3.1.** The partner's more special disjoint three-bank family has a continuous density by its separate cross-square theorem.

The result uses no Gaussianity, moments, compact support, log-concavity, connected support, Monte Carlo extremality, post-rotation independence, or law-uniform scalar oscillatory decay.