SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-24T00:24:32Z.
attacking: the punctured near-coloop normal form: compress one physical hub plus its residual product source to an exact four-dimensional rank-three model, quantify the overlap defect, and identify the exact third-curvature invariant.

# account03/B11 r45 — exact null-puncture normal form and a sharp warning against projection-cap collapse

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: indefinite signatures `(2,1)` / `(1,2)`.
Status: **NEW STRUCTURAL NORMAL FORM / PARTNER RESULT APPLIED / SOURCE-VALID INTERFACE FALSIFIER / FULL QFORM OPEN**.
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted owner conjecture remains OPEN. This report does not claim a full exact-rank-three proof and does not address arbitrary additional nonseparable spectrum. It stays within the live corrections: no post-rotation independence, no arbitrary-joint rank-three coarea bound, no conditional-density-cap substitute for independence, no law-uniform pointwise quadratic-phase decay, and no deletion of a small nonzero coefficient.

## 1. Sources and immediate predecessor

The immediate B11 predecessor is account03/B11 r44, canonical mathematics

`yspennstate/math-open-problems@388ba1f1ccf6a89dad0ca0a0fdb71d281ad6239b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T231333Z-account03-B11-QFORM-r44/REPORT.md`.

It proves an arbitrary-pivot shared-hub tensor receiver when two source-disjoint star banks have a genuine rank-one transverse crossing. The first unpaid branch there is the non-rank-one or aligned shared-hub collar.

The earlier account03/B11 null-heavy normal form is

`yspennstate/math-open-problems@e100de67669c37c8243fe9e389efc909f3179839`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260922T182528Z-account03-B11-QFORM-r12/REPORT.md`.

The completed designated partner used below is account04/B11:

`yspennstate/math-open-problems@4110bbfd21beffa0260a017d468b0a486af56db1`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T222040Z-account04-B11-cone-envelope-r3/REPORT.md`.

Its partition-stable null-scalar theorem gives, for a cap-`L` scalar independent of an arbitrary pair of joint cap `M`,

`||p||_infinity <= 3*2^(2/3)(LM)^(2/3)|alpha|^(-2/3)|beta|^(-1/3)`

for `2 alpha ZW + beta V^2 + 2 gamma VW + delta W^2 + affine`.

## 2. Exact source-normalized puncture theorem

Let

`A=R M R^T`, `R^T R=I_3`,

with `M` real symmetric invertible and

`s := min_a |lambda_a(M)| > 0`.

Fix one ORIGINAL physical coordinate `i`. Write its spectral row as `r_i`, its leverage as

`q = ||r_i||^2`,

and assume

`0<q<1`, `A_ii = r_i^T M r_i = 0`.

Set

`e_1 = r_i/sqrt(q)`.

Because `e_1^T M e_1=0` and `M` is invertible,

`kappa := ||M e_1|| > 0`,

and

`e_2 := M e_1/kappa`

is a unit vector orthogonal to `e_1`. Complete `(e_1,e_2,e_3)` to an orthonormal spectral basis. In this basis

`M = [[0,kappa,0],[kappa,d,e],[0,e,c]]`,

hence

`det M = -kappa^2 c`,

so

`boxed: kappa^2 |c| = |det M| >= s^3`.                         (2.1)

Now inspect the coefficient vectors across the residual ORIGINAL coordinates `j!=i`. Define

`T = (1/sqrt(1-q)) sum_{j!=i} (r_j dot e_1) X_j`,
`W = sum_{j!=i} (r_j dot e_2) X_j`,
`V = sum_{j!=i} (r_j dot e_3) X_j`.

Parseval gives exactly

`sum_{j!=i}(r_j dot e_1)^2 = 1-q`,
`sum_{j!=i}(r_j dot e_2)^2 = sum_{j!=i}(r_j dot e_3)^2 = 1`,

and every cross inner product among those three residual coefficient vectors is zero. Therefore `(T,W,V)` is a genuine THREE-DIMENSIONAL ORTHONORMAL PROJECTION of the residual original-coordinate product source. It is generally internally dependent. The physical scalar `H:=X_i` is genuinely independent of the whole triple.

The active spectral coordinate in direction `e_1` is

`S = sqrt(q) H + sqrt(1-q) T`.

Consequently the quadratic form is EXACTLY

`boxed:
 Q = 2 kappa (sqrt(q) H + sqrt(1-q) T) W
     + d W^2 + 2 e W V + c V^2.`                         (2.2)

No coefficient has been dropped and no spectral coordinate has been declared independent.

After the determinant-one shear

`V' = V + (e/c)W`,

(2.2) becomes

`boxed:
 Q = 2 kappa sqrt(q) H W
     + 2 kappa sqrt(1-q) T W
     + c (V')^2
     + (d-e^2/c) W^2.`                                      (2.3)

The shear preserves the three-dimensional Lebesgue density cap of the projected residual triple, but it does not create independence inside that triple.

### Theorem 2.1 — `QFORM-NULL-PUNCTURE-ONEPARAMETER-NORMALFORM-v1`

Every exact-rank-three indefinite zero-physical-pivot state with `0<q<1` has the product-valid representation (2.3), in which

`boxed: |det M| = kappa^2 |c|`,

and the ratio of the overlapping leakage coefficient to the independent-hub saddle coefficient is exactly

`boxed:
  [kappa sqrt(1-q)]/[kappa sqrt(q)]
  = sqrt((1-q)/q).`                                          (2.4)

Thus, after normalization, the puncture is not an arbitrary extra small parameter: it is exactly the leverage defect of the selected physical hub.

In the live near-coloop chamber `q>=63/64`,

`sqrt((1-q)/q) <= 1/sqrt(63) = 0.125988...`.

This does NOT justify perturbatively deleting the `TW` term. It identifies precisely what a valid overlap compiler must control.

### Equivalent four-dimensional compression

The same statement can be written as an exact four-dimensional matrix compression. Let

`G=I-r_i r_i^T`, `U=R_{-i} G^(-1/2)`,

so `U^T U=I_3`, and put `Z=U^T X_{-i}`. With

`S4 = [r_i^T ; G^(1/2)]`

(one top row and a 3x3 lower block), one has

`S4^T S4=I_3`,
`Q=(H,Z)^T B(H,Z)`, `B=S4 M S4^T`.

Hence `B` has exactly the same three nonzero eigenvalues as `M`. Its unit kernel vector is explicitly

`boxed: n=(sqrt(1-q), -r_i)`,                                  (2.5)

because `G^(1/2) r_i=sqrt(1-q)r_i`. The near-coloop limit `q->1` is therefore exactly the limit in which the null direction loses its physical-hub component and moves into the residual projected bank.

## 3. Designated account04/B11 theorem applied at an actual inequality

The partner theorem quoted in Section 1 applies immediately at the genuine separated endpoint `q=1`. Then the leakage term in (2.3) vanishes, `H` is independent of the orthonormal residual pair `(V,W)`, the scalar cap is `L=1`, and the standard product-projection cap used by the partner is `M<=e`. Since

`|alpha|^2 |beta| = kappa^2 |c| = |det M| >= s^3`,

the partner theorem gives the actual target inequality

`boxed:
 ||p_Q||_infinity
 <= 3*2^(2/3)e^(2/3)|det M|^(-1/3)
 <= 9.275505198/s.`                                           (3.1)

The same calculation works in the separated-leakage branch for `0<q<1`: convolution with the independent physical hub gives the scalar `S` density cap `L<=q^(-1/2)`, hence

`boxed:
 ||p_Q||_infinity <= 9.275505198 q^(-1/3)/s.`                  (3.2)

In particular, for the current near-coloop threshold `q>=63/64`, this is `<9.324325/s`. Equation (3.2) is a control branch only; the unresolved fully overlapping case is exactly that `T` belongs to the same residual product projection as `(V,W)`.

The partner result proves essential boundedness in this scope. This run does not add a continuity theorem for the overlapping punctured branch.

## 4. A sharper falsifier: scalar independence plus a three-dimensional density cap is still not enough

The four-dimensional compression is useful only if the fact that `Z` is an ORTHONORMAL PRODUCT PROJECTION is retained. Replacing that provenance by a bare three-dimensional `L^infinity` density cap is invalid even when the physical scalar is perfectly independent and has maximal leverage.

Fix `0<epsilon<1`. Let

`H ~ Uniform[0,1]`

and independently let `(T,V,W)` have joint density exactly one on the rectangular box

`0<=T<=epsilon^(-3/2)`,
`0<=V<=sqrt(epsilon)`,
`0<=W<=epsilon`.

The box has volume

`epsilon^(-3/2)*sqrt(epsilon)*epsilon=1`,

so this is a probability density with cap one. Consider

`Q_epsilon = V^2 + 2 H W`.

Its coefficient matrix in `(H,V,W,T)` is

`[[0,0,1,0],
  [0,1,0,0],
  [1,0,0,0],
  [0,0,0,0]]`,

whose eigenvalues are exactly `{-1,0,1,1}`. The physical scalar `H` has leverage one in the active rank-three subspace. Nevertheless

`0 <= Q_epsilon <= 3 epsilon`

almost surely. Therefore

`boxed:
 P{Q_epsilon in [0,3 epsilon]}=1,`                              (4.1)

so no inequality of the form

`P{Q in I} <= C |I|`

can hold uniformly over `H` cap one independent of an ARBITRARY three-dimensional joint density of cap one. Any such `C` would have to satisfy

`C >= 1/(3 epsilon) -> infinity`.

This is **not** a counterexample to QFORM. The rectangular three-dimensional law above is not asserted to be an orthogonal projection of a cap-one product law; indeed its `(V,W)` marginal has height `epsilon^(-3/2)`, which is forbidden by the product-projection bounds available in the actual target. The point is narrower and important:

`QFORM-SCALARxJOINT3-CAP-INTERFACE-FALSE-v1`:

> even an independent cap-one scalar, a cap-one three-dimensional companion density, exact rank three, and maximal scalar leverage do not suffice. The residual orthogonal-product-projection provenance must be used quantitatively.

This is a source-matched strengthening of the live correction that a bounded projected density alone does not control an indefinite quadratic pushforward.

## 5. Rank-two logarithm and the exact third-direction mechanism

The benchmark remains the opposite-sign rank-two example

`p_{2XY}(t)=log(1/(2|t|))`

for independent centered unit uniforms. In the null-heavy rank-three normal form, the missing third curvature is exactly the coefficient `c(V')^2`, and (2.1) says the saddle coupling and that third curvature cannot both be weak:

`kappa^2|c|=|det M|>=s^3`.

At the separated endpoint the account04/B11 theorem converts the hyperbolic `1/|W|` kernel into the integrable `|W|^(-1/2)` kernel after averaging against the third square. In the punctured overlapping state, the third square is still quantitatively present; the only unresolved issue is source overlap through the exact term

`2 kappa sqrt(1-q) T W`.

So the third direction does not vanish as `q->1`; what degenerates is only the product separation needed by the current null-scalar receiver.

## 6. First unpaid implication after r45

The next B11 implication is

`QFORM-ORTHOGONAL-PROJECTION-PUNCTURE-COMPILER-v1`:

> For the exact model (2.3), where `H` is an original cap-one scalar independent of `(T,V,W)` and `(T,V,W)` is specifically a three-dimensional orthonormal projection of the residual cap-one product source, prove a uniform linear small-ball bound as `q->1` while retaining the `TW` term. The estimate must use more than the bare 3D density cap; r40 already rules out the naive `L1_T(L2_{V,W})` fiber route, and Section 4 above rules out replacing product-projection provenance by arbitrary joint density.

A plausible next mechanism is an original-source Brascamp--Lieb / weighted-section estimate applied before the `(T,V,W)` pushforward, or a source-disjoint recut whose loss is charged to an already completed pair/cross-volume receiver. The r44 rank-one shared-hub tensor branch remains paid and should be used whenever the recut exposes its transverse crossing.

Arbitrary additional nonseparable spectrum remains a separate full-target bridge. Full-target continuity remains open.

## 7. Verification

`VERIFY.py` performs 500 random algebraic regressions of the four-dimensional compression. It verifies:

- the residual normalized map is orthonormal;
- the explicit kernel vector (2.5);
- equality of the three nonzero eigenvalues of `B` and `M`;
- exact quadratic-form preservation;
- `det M=-kappa^2 c`;
- the puncture ratio (2.4).

It also checks the volume-one interface-falsifier boxes and records the partner constants. The observed maximum floating-point errors are below `8e-15`; the output terminates

`QFORM_B11_R45_NULL_PUNCTURE_CHECK_PASS`.

The full owner target remains OPEN / NOT PROVED / NOT DISPROVED.
