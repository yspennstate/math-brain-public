# account03/B10 — zero-pivot determinant smoothing and the heavy-isotropic product-origin frontier

**Run:** `20260922T131341Z-account03-B10-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Rank-three coupled case`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / PRODUCT-ORIGIN ROUTE OBSTRUCTION`; full target **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Fresh target, corrections, and peer state

The exact target remains: for every dimension, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and real symmetric `A` with at least three eigenvalues of absolute value at least one, prove

`P(X^T A X in [t,t+h]) <= C h`

for one universal finite `C`, every real `t`, and every `h>0`.

Fresh owner controls keep QFORM as the sole programme. The live correction set is enforced: no law-uniform pointwise one-dimensional Fresnel decay; no post-rotation independence; no naive spectral fiber supremum; no single-cross-minor or single-Schur-pivot universal extraction; no conditional-density-cap substitute for genuine independence.

The assigned partner is `account04/B10`. No completed current-QFORM handoff/report from that slot existed at the startup or pre-work source checks, so no result is attributed to it. Two completed compatible sources are used substantively:

1. **account02/B10**, `math-open-problems@11c9ae19edfd07e3a0bd4053a910667c20e721ab`, proves the independent-leakage heavy-isotropic branch and gives the exact correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`: bounded pair density plus bounded conditional scalar density does not replace genuine independence.
2. **account01/B19**, `math-open-problems@072cf685a12893b44d555f14e4e610bcf2154037`, gives the hard high-cardinality rank-three star-plus-square family and its aggregate hyperbolic-square closure, showing that reciprocal local-minor costs cannot be paid before aggregation.

The present run attacks the first unpaid heavy-isotropic implication while preserving an original physical coordinate as the genuinely independent scalar.

---

## 2. Main new theorem: every nonsingular physical zero-pivot triple has determinant-only smoothing

### Theorem 2.1 — `QFORM-ZERO-PIVOT-DET3-v1`

Let `X,Y,Z` be independent real random variables with probability densities bounded by one. Let

`M = [[0,a,d],[a,b,e],[d,e,c]]`

be a real symmetric `3x3` matrix with `det M != 0`. For arbitrary real linear coefficients and a constant, put

`Q = (X,Y,Z) M (X,Y,Z)^T + l_1 X + l_2 Y + l_3 Z + l_0`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= C0 |det M|^(-1/3)`,

where

`C0 = 3 * 2^(2/3) = 4.7622031559...`.

The estimate depends only on the determinant of the physical principal triple, not on its smallest singular value or condition number. No sign assumption is imposed. In particular every invertible symmetric `3x3` block with one zero diagonal entry is indefinite and is covered.

### Proof

Because `det M !=0`, at least one of the two pivot couplings `a,d` is nonzero. Interchange `Y,Z` if necessary and assume `d!=0`.

Define the original-product-preserving affine variable

`W = aY + dZ + l_1/2`.

Then the entire dependence on `X` becomes exactly

`2 X W`.

The change of variables `(Y,Z) -> (W,Y)` has Jacobian magnitude `|d|`, hence `(W,Y)` has joint density

`h(w,y) = |d|^(-1) f_Y(y) f_Z((w-l_1/2-a y)/d)`

and therefore

`||h||_infinity <= H := |d|^(-1)`.

Crucially, the original physical variable `X` is still genuinely independent of the entire pair `(W,Y)`. This is exactly the independence that the live account02/B10 correction says must not be replaced by a conditional-density cap.

Ignoring affine terms for a moment, solve `Z=(W-aY)/d`. The residual quadratic part becomes

`A Y^2 + 2 E W Y + C W^2`,

where

`A = b - 2ea/d + c a^2/d^2`.

A direct determinant calculation gives

`det M = -a^2 c + 2ade - b d^2 = -d^2 A`.                 (2.1)

Thus `A!=0`. Restoring the affine terms changes only the linear coefficients in `Y,W`. Completing the square in `Y` gives measurable (indeed affine/quadratic) functions `theta,F` such that

`Q = 2 X W + F(W) + A [Y + theta(W)]^2`.                 (2.2)

Now apply the previously proved account03/B10 dependence-tolerant hyperbolic-square theorem: if one scalar variable is independent of a possibly dependent pair of joint density at most `H`, then

`2 alpha X W + F(W) + beta [Y+theta(W)]^2`

has density at most

`3*2^(2/3) H^(2/3) |alpha|^(-2/3)|beta|^(-1/3)`.

Here `alpha=1`, `beta=A`, `H=|d|^(-1)`. Therefore

`||p_Q||_infinity`

` <= 3*2^(2/3) |d|^(-2/3)|A|^(-1/3)`

` = 3*2^(2/3) |d^2 A|^(-1/3)`

` = C0 |det M|^(-1/3)`

by (2.1). QED.

### Density-cap scaling corollary

If the three independent variables have density caps `K_X,K_Y,K_Z` instead of one, scaling each variable to cap one preserves the zero pivot and gives

`||p_Q||_infinity <= C0 (K_X K_Y K_Z)^(2/3)|det M|^(-1/3)`.          (2.3)

### Arbitrary ambient corollary

For an arbitrary-dimensional symmetric matrix `A`, suppose an original-coordinate principal triple `I={i,j,k}` satisfies

`A_ii=0`, `det A[I,I] !=0`.

Condition on every coordinate outside `I`. The conditional polynomial has the same quadratic block `A[I,I]` and only acquires affine terms. Theorem 2.1 therefore gives the full conditional and unconditional bound

`||p_{X^T A X}||_infinity <= C0 |det A[I,I]|^(-1/3)`.                 (2.4)

Thus arbitrary outside couplings and arbitrary extra spectrum are harmless once such a zero-pivot physical triple is quantitatively available.

---

## 3. Direct application to the exact heavy-isotropic rank-three residual

Let

`A=U Lambda U^T`, `U^T U=I_3`, `|lambda_r(Lambda)|>=1`,

and let a physical row be

`u_i=sqrt(c)e`, `c>1/2`, `e^T Lambda e=0`.

Then `A_ii=0`, so every principal triple containing `i` is in the zero-pivot geometry of Theorem 2.1 whenever it is nonsingular.

For `j,k !=i`, write

`u_j=s_j e+w_j`, `u_k=s_k e+w_k`, `w_j,w_k in e^perp`.

The projected residual rows form a Parseval frame in the two-dimensional plane:

`sum_{j!=i} w_j w_j^T = I_(e^perp)`.

Consequently Cauchy--Binet gives the exact determinant-mass identity

`sum_{j<k, j,k!=i} det(w_j,w_k)^2 = 1`.                              (3.1)

For `I={i,j,k}`,

`det A[I,I] = det(U_I)^2 det Lambda`

and

`det(U_I)^2 = c det(w_j,w_k)^2`.

Hence

`|det A[I,I]| = c |det Lambda| omega_jk`,

where

`omega_jk := det(w_j,w_k)^2`, `omega_jk>=0`, `sum omega_jk=1`.         (3.2)

The new theorem therefore supplies, for every positive determinant-mass atom,

`||p_Q||_infinity <= C0 [c |det Lambda| omega_jk]^(-1/3)`.            (3.3)

If `omega_* = max omega_jk`, then

`||p_Q||_infinity <= C0 [c |det Lambda| omega_*]^(-1/3)
                     < C0 (2/omega_*)^(1/3)`.                         (3.4)

This is a genuine closure of the heavy-isotropic branch whenever one physical transverse determinant atom has dimension-free mass. Compared with the general anisotropic principal-triple estimate `O((sigma_min |det|)^(-1/4))`, (3.3) has no smallest-singular-value penalty at all; the exact zero pivot converts anisotropy into a hyperbolic-square smoother.

The surviving hard branch is correspondingly sharper: **the zero-pivot determinant mass (3.1) must be highly delocalized**, so every `omega_jk` can be tiny even though their sum is one. This is exactly the setting in which account01/B19 shows that aggregation has to precede reciprocal local payment.

---

## 4. Why linear averaging of the new local bounds still does not finish the problem

The exponent in (3.3) is milder than the old reciprocal-square-root local costs, but naive determinant-mass averaging still loses dimension. If one tried to average (3.3) with weights `omega_jk`, the resulting factor would be

`sum omega_jk^(2/3)`,                                                    (4.1)

which is unbounded when the determinant mass is spread over many atoms.

The account01/B19 star-plus-square family calibrates this exactly. In its leverage-one isotropic realization, the residual `e^perp` frame has `m` rows on one transverse axis and `m` rows on the other, each of norm `m^(-1/2)`. Thus

`omega_jk=1/m^2`

on `m^2` cross-axis pairs and zero otherwise. Formula (4.1) equals `m^(2/3)`, while the same target family has a dimension-free density bound after the two coordinate banks are aggregated first. Hence Theorem 2.1 is a local closure theorem, not permission to average reciprocal determinant constants.

This is an actual use of the account01/B19 completed stress family: it determines the correct interpretation of (3.3) and prevents a false global conclusion.

---

## 5. Product-origin stress test: the conditional-Renyi route is unbounded even inside the exact heavy-isotropic geometry

The live account02/B10 correction already proves that bounded pair density plus bounded conditional scalar density is insufficient for an arbitrary correlated triple. Here is a stronger stress test of the specific next idea suggested by the previous B10 theorem: condition on the leakage `T`, apply the dependence-tolerant hyperbolic-square theorem on each fiber, and average its `H(T)^(2/3)` cost.

That mixed-norm route is unbounded **even when `(T,Y,Z)` is an orthogonal linear image of an original-coordinate product law and the entire construction is an exact rank-three target form**.

Fix any `c in (1/2,1)` and put `d=1-c`. Define four physical spectral rows in the basis `(e,f,g)` by

`u_0=(sqrt(c),0,0)`,

`u_1=(sqrt(d/2), 1/sqrt(2), 0)`,

`u_2=(-sqrt(d/2),1/sqrt(2),0)`,

`u_3=(0,0,1)`.

Then `U^T U=I_3`. Take

`Lambda=[[0,1,0],[1,0,0],[0,0,1]]`,

whose eigenvalues are exactly `{1,-1,1}`. Thus `A=U Lambda U^T` is an exact target matrix and `u_0` is a heavy isotropic row.

The quadratic form is

`Q = 2( sqrt(c) X_0 + T )Y + Z^2`,                                    (5.1)

with

`T=sqrt(d)(X_1-X_2)/sqrt(2)`,
`Y=(X_1+X_2)/sqrt(2)`,
`Z=X_3`.

For integer `M>=3`, let

`E_M = union_{k=1}^M [10^k,10^k+1/M]`

and take `X_1,X_2` independently with density `1_(E_M)`; this is a probability density because `|E_M|=1`. Take `X_0,X_3` uniform on `[0,1]`.

Put

`R=(X_1-X_2)/sqrt(2)`.

The orthogonal map `(X_1,X_2)->(R,Y)` has Jacobian one and joint density

`h(r,y)=1_(E_M)((y+r)/sqrt(2)) 1_(E_M)((y-r)/sqrt(2))`,

so `h` takes only the values zero and one. Let `m(r)=int h(r,y)dy` be the density of `R`. Conditional on `R=r`, the density of `Y` has essential supremum exactly `1/m(r)` whenever `m(r)>0`. Since `Z` is independent uniform, the conditional joint density cap of `(Y,Z)` given `T=sqrt(d)r` is also

`H(T)=1/m(r)`.                                                         (5.2)

For each ordered off-diagonal interval pair `(p,q)`, `p!=q`, the corresponding difference-density component is a triangle supported near `(10^p-10^q)/sqrt(2)`. Those supports are disjoint for `M>=3`, and if `ell=1/M`, each contributes

`m(r)=sqrt(2)(ell-|sqrt(2)(r-r_pq)|)_+`.

Therefore

`int_(one triangle) m(r)^(1/3) dr
 = [3*2^(2/3)/4] ell^(4/3)`.                                          (5.3)

There are `M(M-1)` such disjoint off-diagonal triangles, so

`E[ H(T)^(2/3) ]
 = int m(r)^(1/3) dr
 >= [3*2^(2/3)/4] (M-1) M^(-1/3) -> infinity`.                        (5.4)

Thus the natural conditional application of the previous dependence-tolerant theorem cannot yield a universal bound by averaging its `H^(2/3)` fiber cost. This is consistent with, and sharper in product provenance than, the account02/B10 conditional-cap correction and the account02/B03 Renyi-spread warning.

### The target family itself is nevertheless uniformly bounded

Equation (5.4) is a proof-route obstruction, not a QFORM counterexample. To demonstrate that distinction explicitly, condition instead on the original physical coordinate `X_2=x_2`. Expanding (5.1) gives

`Q = sqrt(2c) X_0 (X_1+x_2) + sqrt(d)(X_1^2-x_2^2) + X_3^2`.

Set `Y'=X_1+x_2`. Conditional on `x_2`, the variables `X_0,Y',X_3` are independent and each has density cap one, while

`Q = 2 a X_0 Y' + H_x2(Y') + X_3^2`,

with

`a=sqrt(c/2)`

and an explicit quadratic function `H_x2`. Apply the completed account02/B10 hyperbolic-square theorem:

`||p_(Q|X_2=x_2)||_infinity <= 4/sqrt(a)
 = 4 (c/2)^(-1/4)
 < 4 sqrt(2)`.                                                         (5.5)

The bound is uniform in `x_2`, hence also unconditional. This is a direct application of completed compatible peer mathematics to a real target derivation. It shows precisely why original-coordinate conditioning can succeed while conditioning on a projected leakage variable destroys the useful product structure.

---

## 6. Updated exact frontier

This run pays a real part of `QFORM-ISOTROPIC-PRODUCT-PROVENANCE-TRACE-v1`:

1. **Local zero-pivot physical mass is fully paid.** Any nonsingular physical `3x3` zero-pivot block has the scale-correct determinant-only bound
   `C0 |det|^(-1/3)` with no condition-number loss.
2. **Heavy-isotropic rank three is closed whenever one transverse determinant-mass atom `omega_jk` is dimension-free.** The exact weights sum to one by Cauchy--Binet.
3. **The remaining branch is genuinely high-cardinality.** Local reciprocal payment cannot simply be averaged; the B19 family exhibits the loss.
4. **Conditioning on spectral leakage is not the aggregation mechanism.** The exact target family in Section 5 makes the conditional `H^(2/3)` cost diverge while original-coordinate conditioning gives a uniform `<4 sqrt(2)` bound.

The first unpaid implication is therefore narrower:

### `QFORM-ISOTROPIC-DELOCALIZED-DET-MASS-AGGREGATION-v1`

In the heavy-isotropic normal form, assume the determinant mass

`omega_jk=det(w_j,w_k)^2`, `sum omega_jk=1`

is delocalized so that no single zero-pivot physical triple is quantitatively useful. Prove a product-preserving aggregate smoother that consumes this determinant mass **before** any `omega_jk^(-1/3)` payment, while retaining the leakage coefficients `s_j` and the exact orthogonality relations

`sum s_j y_j=sum s_j z_j=sum y_j z_j=0`.

The theorem must include the high-cardinality star-plus-square family and must not condition first on the projected leakage `T`.

This is materially sharper than the preceding `one-heavy-isotropic-leakage` residual: the locally concentrated determinant-mass portion is now completely solved, and a specific tempting projected-conditioning route is ruled out inside the actual target class.

## 7. Status

- `QFORM-ZERO-PIVOT-DET3-v1`: **PROVED SUPPORTING THEOREM**.
- Heavy-isotropic branch with `omega_*>=eta>0`: **PROVED**, with explicit `C0(c|det Lambda|eta)^(-1/3)`.
- Conditional projected-leakage `H^(2/3)` mixed-norm completion: **REFUTED AS A UNIFORM MECHANISM**, by an exact product-origin rank-three target family.
- Full arbitrary rank-three orientation: **OPEN**.
- Full owner target with arbitrary extra spectrum: **OPEN**.
- Continuity: not claimed for Theorem 2.1; essential boundedness is proved.

No projected coordinates are declared independent. No refuted pointwise decay or naive fiber supremum is used. The named account04/B10 partner had no completed current-QFORM artifact at the source checks and no result was fabricated.
