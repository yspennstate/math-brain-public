SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T11:12:51Z.
attacking: indefinite exact-rank-three null-hub geometry: derive a canonical saddle/shear/square normal form and identify a determinant-conserving third-direction dichotomy; apply account02/B11 balanced-bank output quantitatively.

# account01/B11 — null-hub curvature conservation for exact rank three

**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / DIFFUSE_SUBBRANCH_PAID / FULL_TARGET_OPEN`.

**Programme:** `QFORM-DENSITY-3EIG-20260922`.  **Execution:** `WITHOUT_VERIFIED_BRAIN`.

The result below concerns the genuinely indefinite exact-rank-three chamber and is valid for both signatures `(2,1)` and `(1,2)`. It does not prove the unrestricted theorem with additional spectrum. The live corrections are respected: there is no arbitrary-joint coarea step, no declaration that rotated spectral coordinates are independent, no pointwise van-der-Corput claim, and no perturbative deletion of a small coefficient.

## 1. Source-pinned premises

Fresh control before publication remained OWNER CONTROL revision `2026-09-22.15`, QFORM-only. The correction inbox blob remained `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.

Three previously completed ingredients are used only in their stated scopes.

1. **Fresnel--Brascamp--Lieb Theorem F.** Source:
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.
   If a rank-three quadratic part on a bank of ORIGINAL coordinates has normalized spectral-row leverages at most `1/2`, then, allowing arbitrary affine terms and a diagonal twist, the density is continuous and
   `||p||_infinity <= 12 (|lambda_1 lambda_2 lambda_3| det G)^(-1/3)`.

2. **B11 unit-leverage null-scalar endpoint.** Source:
   `yspennstate/math-open-problems@1515e474fa8110a0b704a6ff73a25fc554005017`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T211147Z/REPORT.md`.
   For exact rank three, if an ORIGINAL coordinate has spectral leverage one and physical diagonal zero, then
   `||p_Q||_infinity < 9.276 |det M|^(-1/3)`.
   This endpoint proves essential boundedness; continuity was not proved there.

3. **Designated partner account02/B11 balanced four-bank theorem.** Source:
   `yspennstate/math-open-problems@ba000d70d1d4f523a2396155a24d5088d5c94802`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T095139Z-account02-B11-qform-r11-86d203a2/REPORT.md`.
   Its explicit target-valid Walsh/four-bank family is paid by a product-preserving three-mode estimate, despite every fixed physical packet losing the second/third scale.

## 2. Canonical null-hub normal form

### Theorem 2.1 — `QFORM-NULL-HUB-CURVATURE-CONSERVATION-v1`

Let `A` be a real symmetric matrix of **exact rank three** and indefinite signature `(2,1)` or `(1,2)`. Assume the ORIGINAL coordinate `0` has

`A_00=0`

and its row is nonzero. Write, after separating that coordinate,

`A = [[0, b^T], [b, C]]`,

and set

`beta=||b||_2>0`, `e=b/beta`.

Then there exist orthonormal vectors `w,z` in the complement of the coordinate `0`, with `w,z` orthogonal to `e` (the vector `z` is omitted when the coefficient below is zero), and real numbers `c,gamma,lambda,D` with `lambda!=0`, `D>=0`, such that on the only possibly nonzero four-dimensional subspace `span{x_0,e,w,z}`, the matrix of `A` is

```
H = [ 0      beta      0       0
      beta   c         gamma   D
      0      gamma     lambda  0
      0      D         0       0 ].                         (2.1)
```

Moreover, if `h` denotes the leverage of the physical coordinate `0` in `Ran(A)`, then

`h = beta^2/(beta^2+D^2)`,                                  (2.2)

and the signed product of the three nonzero eigenvalues is

`pdet(A) = -lambda (beta^2+D^2).`                           (2.3)

Consequently the third-direction determinant splits **exactly** as

`|lambda| beta^2 = h |pdet(A)|`,                            (2.4)

`|lambda| D^2 = (1-h) |pdet(A)|`.                           (2.5)

If `D>0`, the complementary principal block `C=A_{-0,-0}` has exact rank three and

`pdet(C) = -lambda D^2 = (1-h) pdet(A).`                   (2.6)

If the nonzero spectrum of `A` is represented as `A=R M R^T`, `R^T R=I_3`, then `pdet(A)=det M`, so (2.4)-(2.6) can be written with `det M`.

Finally, the sign of `lambda` is forced by inertia:

- in signature `(+,+,-)`, `lambda>0`;
- in signature `(+,-,-)`, `lambda<0`.

Thus the transverse square in (2.1) always has the **majority sign**.

### Proof

Use the orthogonal decomposition of the complement

`R^{n-1} = span{e} direct_sum e^perp`.

In this basis write

`C = [[c, d^T], [d, E]]`.                                  (2.7)

The physical two-dimensional block on `(x_0,e)` is

`B = [[0,beta],[beta,c]]`,                                  (2.8)

with determinant `-beta^2`, so it is invertible and indefinite. Its inverse is

`B^{-1} = [[-c/beta^2, 1/beta],[1/beta,0]].`                (2.9)

The bottom-right entry in (2.9) is exactly zero. Therefore the Schur complement of `B` in `A` is simply `E`: the coupling `d` contributes nothing because it meets that zero entry. Hence

`rank A = rank B + rank E = 2 + rank E`.                    (2.10)

Since `rank A=3`, `rank E=1`. Thus

`E=lambda w w^T`                                            (2.11)

for a unit `w in e^perp` and nonzero `lambda`. Decompose

`d = gamma w + D z`,                                        (2.12)

where `D>=0` and, if `D>0`, `z` is unit and orthogonal to both `e,w`. Equations (2.7), (2.11), (2.12) give (2.1). All directions orthogonal to `e,w,z` lie in the kernel.

When `D>0`, the active four-dimensional block (2.1) has kernel vector

`k = (-D/beta, 0, 0, 1)`.                                  (2.13)

All other kernel directions are orthogonal to the physical coordinate `x_0`. Therefore the squared norm of the projection of `x_0` onto the kernel equals

`(D^2/beta^2)/(1+D^2/beta^2)=D^2/(beta^2+D^2)`,             (2.14)

which proves (2.2). The formula also remains valid at `D=0`, where `h=1`.

For a rank-three `4x4` symmetric matrix the signed product of the nonzero eigenvalues is the third elementary symmetric polynomial, i.e. the sum of its `3x3` principal minors. In (2.1), only two such minors are nonzero:

- deleting the `z` coordinate gives `-lambda beta^2`;
- deleting the `x_0` coordinate gives `-lambda D^2`.

Hence

`pdet(A)=-lambda(beta^2+D^2)`,                              (2.15)

which proves (2.3)-(2.5). For `D>0`, the active matrix of `C` on `(e,w,z)` is

```
K = [ c       gamma   D
      gamma   lambda  0
      D       0       0 ],                                  (2.16)
```

so

`det K=-lambda D^2`.                                        (2.17)

This proves (2.6). The sign assertion follows from the sign of the product of the nonzero eigenvalues: negative in signature `(2,1)`, positive in signature `(1,2)`. QED.

## 3. Two further exact identities

The normal form records two useful facts that are easy to lose in a coordinate-free argument.

First,

`beta^2 = sum_{j!=0} A_{0j}^2 = (A^2)_{00}.`                (3.1)

If `A=RMR^T`, and `r_0` is the spectral row belonging to coordinate `0`, then

`beta^2 = r_0^T M^2 r_0`.                                  (3.2)

Consequently, if every nonzero eigenvalue has magnitude at least `s`,

`beta^2 >= s^2 ||r_0||^2 = s^2 h`.                         (3.3)

Together with (2.2),

`D^2 = beta^2 (1-h)/h >= s^2(1-h)`.                         (3.4)

Second, for `D>0`, the inverse of the complement active block satisfies

`K^{-1} e = z/D`,                                           (3.5)

where `e=(1,0,0)` and `z=(0,0,1)` in the basis of (2.16). In particular

`e^T K^{-1} e=0`.                                           (3.6)

Thus deleting the null hub creates an invertible rank-three block, but the old hub-coupling direction remains null for the inverse quadratic form. This is the exact algebraic trace of the hyperbolic saddle.

## 4. A paid diffuse-complement branch

### Corollary 4.1 — `QFORM-NULL-HUB-DIFFUSE-DELETION-v1`

In Theorem 2.1 assume `D>0`. Let `P_C` be the orthogonal projection onto `Ran(C)` inside the ORIGINAL complement coordinates. If

`max_{j!=0} (P_C)_{jj} <= 1/2,`                             (4.1)

then for arbitrary independent input densities bounded by one,

`Q=X^T A X`

has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <= 12 [(1-h)|det M|]^(-1/3).`       (4.2)

If `min |lambda(M)| >= s`, then

`boxed: ||p_Q||_infinity <= 12 (1-h)^(-1/3) s^(-1).`         (4.3)

**Proof.** Condition on the ORIGINAL coordinate `X_0`. The remaining variables are still independent. Their quadratic matrix is exactly `C`; fixing `X_0` adds only an affine term `2X_0 b^T X_{-0}` and a constant. By (2.6), `C` has exact rank three with

`|pdet(C)|=(1-h)|det M|`.                                   (4.4)

Choose the three orthonormal eigenvectors of `C` and apply Theorem F with the entire complement as the original-coordinate bank, no residual quadratic part, and Gram matrix `G=I_3`. Hypothesis (4.1) is exactly the required normalized-row leverage bound. Uniformly in the conditioned value of `X_0`, Theorem F gives

`|phi_cond(t)| <= (4pi)^(3/2) |t|^(-3/2) |pdet(C)|^(-1/2)`  (4.5)

at large frequency and the corresponding density bound `12|pdet(C)|^(-1/3)`. Averaging the conditional characteristic functions preserves the same integrable envelope, hence Fourier inversion gives a continuous `C_0` unconditional density with (4.2). Since `|det M|>=s^3`, (4.3) follows. QED.

A simple numerical threshold is worth recording: if `h<=1/2`, then (4.3) gives

`||p_Q||_infinity <= 12*2^(1/3)/s < 15.120/s`               (4.6)

whenever (4.1) holds.

## 5. The unit-leverage endpoint and what the conservation law says

At `h=1`, (2.2) forces `D=0`. The physical null coordinate then becomes an exact unit-leverage coordinate of the spectral range. The previously completed B11 endpoint applies and gives

`boxed: ||p_Q||_infinity < 9.276 |det M|^(-1/3) <= 9.276/s.` (5.1)

This endpoint uses genuine original-coordinate independence and does **not** follow by taking `h up to 1` in (4.2). Indeed, (4.2) blows up as `(1-h)^(-1/3)`.

The exact identities (2.4)-(2.5) show why that blow-up is not a loss of spectral determinant. The third-direction volume is conserved and merely moves between two channels:

`deletion channel:       |lambda|D^2    = (1-h)|det M|`,     (5.2)

`hub saddle/square channel: |lambda|beta^2 = h|det M|`.      (5.3)

The diffuse-deletion theorem pays (5.2); the exact unit-leverage theorem pays (5.3) at `h=1`. A complete near-unit theorem must use both channels jointly while retaining the product provenance. Treating `D` as a perturbatively small coefficient is invalid because the input supports and moments are unrestricted.

## 6. Why the third direction removes the rank-two logarithm

The active `(x_0,e)` block in (2.8) is indefinite for every `beta!=0`, even though the physical diagonal at the hub is zero. With ordinary bounded inputs, the model saddle

`2XY`

has a logarithmically divergent density. For independent `X,Y~Unif[-1/2,1/2]`,

`p_{2XY}(t)=log(1/(2|t|)),   0<|t|<1/2`.                    (6.1)

The normal form (2.1) identifies the missing third direction without diagonalizing the product law. Its majority-sign square is `lambda w^2`. It couples to the saddle through the same `e` coordinate, while the shear `D z` records how much of the third determinant survives after deleting the physical hub.

- At the exact endpoint `D=0`, the third square contributes the transverse `|y|^{-1/2}` smoothing in the earlier null-scalar determinant theorem and turns the saddle's local `1/|y|` kernel into an integrable one.
- For `D>0` and diffuse complement, the same third determinant is visible as the exact deletion volume `(1-h)|det M|`; Theorem F converts the three surviving modes into an integrable `|t|^{-3/2}` Fourier envelope.

Thus the third direction is not an independent spectral coordinate after rotation. Its effect is an exact determinant-conserving transfer between a hub-square smoothing channel and a deletion-volume channel.

Negating `A` exchanges `(2,1)` and `(1,2)` and leaves the density norm unchanged.

## 7. Designated partner result applied to an actual inequality

The latest completed account02/B11 report proves for its balanced four-bank target family

`A_delta = (1-2delta)J + delta vv^T - delta uu^T + 2delta I`

that, under the exact target gate `delta(n-2)>=1`,

`||p_{X^T A_delta X}||_infinity
 <= 12/[n delta^(2/3)(1-2delta)^(1/3)].`                    (7.1)

The partner optimizes (7.1) exactly over the admissible family and obtains

`boxed: ||p||_infinity <= 9/4^(1/3) = 5.6696447245... .`     (7.2)

This is used here as the concrete **distributed** side of the structural picture. That family defeats every bounded-size physical-pair/minor extraction, yet its three spectral rows all have leverage `3/n` and the product-preserving bank theorem pays it uniformly. The present null-hub theorem addresses the opposite localization extreme: a physical null coordinate can carry leverage `h` close to one, and (2.4)-(2.5) identify exactly where the third determinant goes. Together these results rule out the idea that one should pay a reciprocal fixed physical minor before aggregating the product banks.

No assertion is made that every target matrix already falls into one of these two branches.

## 8. First unpaid implication

The new exact bottleneck is

**`QFORM-NEAR-UNIT-NULL-HUB-SHEAR-SQUARE-STABILITY-v1`.**

For an exact-rank-three indefinite form with a null physical hub of leverage `0<h<1`, especially `h up to 1`, prove a product-preserving estimate that exploits the conserved pair

`h|det M|` and `(1-h)|det M|`

simultaneously when the complement range has a row of normalized leverage `>1/2`.

The desired bridge must remain bounded as `h up to 1` and match the finite endpoint (5.1). It may use a second physical hub, ray/bank aggregation, or the exact linear provenance of the shear. It may **not**:

- declare the rotated variables `(e dot X,w dot X,z dot X)` independent;
- replace independence by a mere bounded conditional density (the live conditional-cap correction gives an explicit false interface);
- discard the `D`-term as a small perturbation;
- assume bounded support or moments.

For `D>0` with complement leverage at most `1/2`, Corollary 4.1 is already complete. For `D=0`, the unit-leverage endpoint is already complete. The remaining gap is therefore a sharply localized high-leverage stability problem, not a missing determinant identity.

Arbitrary extra nonseparable spectrum remains a separate interface to the full conjecture.

## 9. Status and regularity

- Theorem 2.1 is an exact structural theorem.
- Corollary 4.1 gives **continuous `C_0` density** in its diffuse-complement branch.
- The `h=1` endpoint gives an **essentially bounded density**; continuity is not claimed there.
- The unrestricted exact-rank-three near-unit high-leverage branch remains open.
- The full all-dimensions/all-extra-spectrum QFORM conjecture remains **OPEN**.
