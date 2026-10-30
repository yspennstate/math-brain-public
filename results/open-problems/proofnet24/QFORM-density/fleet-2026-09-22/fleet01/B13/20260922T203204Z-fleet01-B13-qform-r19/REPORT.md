SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-22T20:32:04Z.
attacking: the exact-rank-three mixed branch by absorbing the longitudinal light residual into an orthogonal physical projection, then paying the diffuse residual regime without rotating the independent inputs.

# Longitudinal absorption in the one-heavy/two-transverse exact-rank-three branch

**Run:** `20260922T203204Z-fleet01-B13-qform-r19`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control observed:** owner revision `2026-09-22.15`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_REDUCTION / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full conjecture remains OPEN. This report proves a new universal paid subbranch and an exact deletion identity that reduces the complementary residual-concentration branch to a small-longitudinal-residual collar. It does not use arbitrary-joint coarea, conditional projected-density moments, post-rotation independence, law-uniform pointwise quadratic Fourier decay, a fixed good minor, or continuity from an exact zero pivot to a small pivot.

## 1. Exact dependencies and corrections

The designated partner result actually consumed is fleet02/B13's heavy/light rank-three trichotomy:

`yspennstate/math-open-problems@d511859edaa636cdc00fcd64155ab07506875c3d`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T182158Z-fleet02-B13-qform-4ebdd821/REPORT.md`.

For exact rank three

`A=R Lambda R^T`, `R^T R=I_3`, `min |eig(Lambda)|>=1`,

with heavy set `H={i:||r_i||^2>3/10}`, light set `L=H^c`, and light Gram `S=sum_{j in L}r_j r_j^T`, that theorem pays the regimes `s_3(S)>=3/5` and `s_2(S)<=3/5`. The only Gram regime left there is

`(MIXED)  s_3(S)<3/5<s_2(S)`.

I also use the exact fleet02/B13 bang-bang reduction

`yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T115714Z-fleet02-B13-qform-480ba28b/REPORT.md`:
for every measurable slab kernel, the supremum over all independent cap-one densities equals the supremum over arbitrary measure-one product indicators, with zero constant loss. No single-interval or bounded-fragment-count claim is inferred.

The immediately preceding fleet01/B13 reduction is

`yspennstate/math-open-problems@01c524aa389abf1b9b58c852bfa11fc747ec5b59`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260922T190849Z-fleet01-B13-qform-r17/REPORT.md`.

In the MIXED branch it produces one heavy original coordinate `i` with

`r_i=sqrt(c) u`, `c>3/10`, `||u||=1`,

such that, writing

`p_j=P_{u^perp}r_j`, `G=sum_{j in L}p_j p_j^T`,

one has

`(1/25) I_{u^perp} <= G <= I_{u^perp}`, `det G>=1/25`.

If some normalized transverse leverage `p_j^T G^{-1}p_j` is at least `1/32`, that preceding report already gives a universal bound `<8228`. Hence the only branch treated below may assume

`a_j:=p_j^T G^{-1}p_j<1/32` for every `j in L`.                    (1.1)

The Fourier input used below is the proved diffuse rank-three estimate appearing in the source chain of the partner report and in the orientation-free rank-two synthesis:
if `V^T V=I_3`, every physical row leverage of `V` is at most `1/2`, `M` is invertible symmetric, and the original independent cap-one coordinates are allowed arbitrary induced linear phases, then

`||p_{(V^T X)^T M(V^T X)+linear}||_infinity <= 3e |det M|^{-1/3}`.       (1.2)

Its proof is by complex Brascamp--Lieb/Hausdorff--Young followed by the three-dimensional Fresnel integral; it never declares rotated input coordinates independent.

Fresh corrections consumed before publication include `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` and `QFORM-R26-ARBITRARY-JOINT-COAREA-PREMISE-RETRACTED-v1`. The former forbids replacing an exact zero Schur diagonal by a merely small one using only a cross-row norm; the latter reiterates that an unrestricted three-dimensional joint-density coarea bound is false. Neither premise is used here.

## 2. Exact longitudinal regression decomposition

Fix the heavy coordinate `i` supplied above. Choose an orthonormal spectral basis whose first vector is `u`. For `j in L` write

`r_j = alpha_j u + p_j`,       `p_j in u^perp`.

Set

`s=sum_{j in L} alpha_j^2`,
`h=sum_{j in L} alpha_j p_j`,
`ell=G^{-1}h`,
`q_j=alpha_j-<ell,p_j>`,
`tau=s-h^T G^{-1}h`.

Then the following identities are exact:

`sum_{j in L} q_j p_j=0`,                                      (2.1)
`sum_{j in L} q_j^2=tau`,                                      (2.2)
`0<=tau<=s<=1-c`.                                               (2.3)

Indeed (2.1) is `h-G ell=0`, and expanding the left side of (2.2) gives `s-2 ell^T h+ell^T G ell=tau`. For (2.3), Parseval gives `sum_k <r_k,u>^2=1`; the selected row contributes `c` and all other heavy rows contribute nonnegative mass, so the light longitudinal mass `s` is at most `1-c`.

The quantity `tau` is the squared physical coefficient norm of the part of the light longitudinal direction not explained by the transverse light plane. The previous run paid the exact graph endpoint `tau=0` with zero heavy pivot. The point here is to treat a substantial positive-`tau` regime without a perturbative zero-pivot argument.

## 3. Orthogonal absorption theorem

Let the active original coordinates be `{i} union L`; the other heavy original coordinates may be conditioned on. Such conditioning creates only deterministic affine terms in the active variables and preserves their independence and density caps.

Define three physical coefficient columns on `{i} union L`. The first is

`v_0(i)=sqrt(c)/sqrt(c+tau)`,
`v_0(j)=q_j/sqrt(c+tau)` for `j in L`.

The remaining two columns are the rows of the two-dimensional matrix `P G^{-1/2}`, where `P` has rows `p_j^T`; their `i`-th entries are zero. Let `V` be the resulting physical matrix with these three columns.

### Theorem 3.1 — `QFORM-LONGITUDINAL-ORTHOGONAL-ABSORPTION-v1`

`V^T V=I_3`. In the new three-dimensional projected variable `Y=V^T X`, the conditional quadratic form has coefficient matrix `M` satisfying

`boxed(|det M|=(c+tau) det(G) |det Lambda|)`.                  (3.1)

The physical row leverages of `V` are

`boxed(h_i=c/(c+tau))`,                                       (3.2)

and, for `j in L`,

`boxed(h_j=q_j^2/(c+tau)+a_j)`,                               (3.3)

where `a_j=p_j^T G^{-1}p_j`.

#### Proof

The transverse two columns have Gram identity because

`G^{-1/2} P^T P G^{-1/2}=I_2`.

Their inner products with `v_0` vanish by (2.1), while `||v_0||^2=(c+tau)/(c+tau)=1` by (2.2). Thus `V^T V=I_3`.

Let `z=sum_{j in L}p_j X_j` and `T=sqrt(c)X_i+sum_{j in L}q_jX_j`. The longitudinal spectral coordinate equals

`sqrt(c)X_i+sum alpha_jX_j = T+ell^T z`.

Also

`T=sqrt(c+tau)Y_0`, `z=G^{1/2}Y_perp`.

Hence, in the spectral basis beginning with `u`, the actual spectral vector is obtained from `Y` by the upper-triangular map

`C = [[sqrt(c+tau), ell^T G^{1/2}], [0, G^{1/2}]]`.

Its determinant has magnitude `sqrt((c+tau)det G)`. If `Lambda_u` is `Lambda` written in this orthonormal spectral basis, then `M=C^T Lambda_u C`. Therefore

`|det M|=|det C|^2 |det Lambda|=(c+tau)det G |det Lambda|`,

proving (3.1). Formulas (3.2)-(3.3) are just the squared row norms of `V`. QED.

This construction is product-preserving in the only sense needed by the diffuse theorem: it changes the three-dimensional projection basis, not the original independent variables. All original variables remain independent and the induced linear terms are retained.

## 4. A new paid positive-residual regime

### Theorem 4.1 — `QFORM-LONGITUDINAL-DIFFUSE-PAID-v1`

Assume (1.1) and, in addition,

`tau>=c`,                                                       (4.1)

`max_{j in L} q_j^2/(c+tau) <=15/32`.                          (4.2)

Then the full exact-rank-three quadratic form, including arbitrary terms generated by conditioning the other heavy original coordinates, satisfies

`boxed(||p_Q||_infinity <= 3e (125/3)^(1/3) <28.272)`.         (4.3)

#### Proof

By (4.1), the heavy row leverage (3.2) is at most `1/2`. By (1.1), (4.2), and (3.3), every light row leverage is strictly below

`15/32+1/32=1/2`.

Thus the diffuse rank-three theorem (1.2) applies. From the partner/preceding geometric reduction,

`det G>=1/25`, `c>3/10`, `|det Lambda|>=1`.

Since `tau>=c`,

`(c+tau)det G |det Lambda| > (3/5)(1/25)=3/125`.

Insert this in (1.2) and use (3.1):

`||p_Q||_infinity <=3e |det M|^{-1/3}`
`                    <=3e(125/3)^(1/3)`
`                    =28.2712702893...`.

The conditional bound is uniform in the conditioned original heavy variables, so averaging preserves it. QED.

### Geometric product-set form via the designated partner

Apply fleet02/B13's exact bang-bang theorem to Theorem 4.1. For every interval `J` and every family of arbitrary measurable sets `E_k subset R` with `|E_k|=1`, throughout the hypotheses of Theorem 4.1,

`boxed(|{x in prod_k E_k : x^T A x in J}| <=29 |J|)`.         (4.4)

This is an actual use of the designated partner result: (4.4) is the exact product-indicator geometric slab inequality corresponding to the new analytic branch. No interval, centered-uniform, bounded-diameter, or bounded-fragment-count reduction is inserted.

## 5. If the diffuse payment fails at `tau>=c`, only one residual atom can be responsible

Assume `tau>=c` but Theorem 4.1 does not apply. Because all `a_j<1/32`, (3.3) shows that failure of the row-leverage condition implies that some `j` has

`q_j^2/(c+tau)>15/32`.                                        (5.1)

There is at most one such index. Indeed

`sum_j q_j^2/(c+tau)=tau/(c+tau)`.

By `tau<=1-c`, the right side is at most `1-c<7/10`, whereas two indices satisfying (5.1) would contribute more than `30/32>7/10`.

Thus the entire complementary `tau>=c` branch has a unique possible longitudinal residual atom.

## 6. Exact deletion formula and collapse to the small-residual collar

Let `j` be the unique index from (5.1). Delete/condition this one original light coordinate and set

`G'=G-p_jp_j^T`,
`h'=h-alpha_j p_j`,
`s'=s-alpha_j^2`,
`tau'=s'-(h')^T(G')^{-1}h'`.

### Lemma 6.1 — leverage downdate identity

With `a_j=p_j^TG^{-1}p_j` and `q_j=alpha_j-p_j^TG^{-1}h`,

`boxed(det G'=(1-a_j)det G)`,                                 (6.1)

`boxed(tau'=tau-q_j^2/(1-a_j))`.                              (6.2)

Moreover

`boxed(G' >= (1-a_j)G > (31/800)I_2)`.                        (6.3)

#### Proof

Equation (6.1) is the matrix determinant lemma. Write `z=G^{-1/2}p_j`; then `||z||^2=a_j`, and

`G'=G^{1/2}(I-zz^T)G^{1/2}`,

whose smallest relative eigenvalue is `1-a_j`; this proves (6.3). For (6.2), apply Sherman--Morrison to `(G-p_jp_j^T)^{-1}` and expand `s'-(h')^T(G')^{-1}h'`. The numerator remaining after cancellation is exactly the squared regression residual

`(alpha_j-p_j^TG^{-1}h)^2=q_j^2`,

with denominator `1-p_j^TG^{-1}p_j=1-a_j`. This is the standard exact leave-one-out least-squares identity. QED.

### Corollary 6.2 — one deletion forces `tau'<c`

Under (5.1),

`boxed(0<=tau'<c)`.                                           (6.4)

Indeed, since `1-a_j<1`, (6.2) and (5.1) give

`tau' < tau-(15/32)(c+tau)`
`     =(17/32)tau-(15/32)c`.

Using `tau<=1-c`,

`tau'<17/32-c`.

Because `c>3/10>17/64`, one has `17/32-c<c`, proving (6.4). Nonnegativity is automatic because `tau'` is a Schur complement / squared regression residual.

In addition, the active rank-three row Gram after conditioning `j` and the other heavy coordinates has determinant

`det S_active=(c+tau')det G'`,

so by (6.1), (6.3), and `c>3/10`,

`boxed(det S_active > (3/10)(31/800)=93/8000)`.                (6.5)

Thus the deletion does not collapse the three-dimensional active spectral volume even though it pushes the longitudinal regression residual below the heavy mass.

## 7. What has changed in the exact-rank-three decision tree

Before this run, after the partner trichotomy and the preceding B13 Pluecker reduction, the only unresolved exact-rank-three branch was one heavy original coordinate plus a uniformly elliptic transverse light plane (or two transverse banks), with a longitudinal residual `tau` not yet controlled.

This report removes a substantial positive-residual region:

1. If `tau>=c` and no light coordinate carries more than `15/32` of the normalized residual direction, the full density is `<28.272` by Theorem 4.1.
2. If `tau>=c` and that diffuse condition fails, exactly one original light coordinate is responsible. Conditioning that one coordinate gives a new active rank-three configuration with `tau'<c`, transverse Gram `G'>31I/800`, and active Gram determinant `>93/8000`.
3. Therefore every still-unpaid configuration in this mixed exact-rank-three route can be reduced, after conditioning at most one additional original coordinate, to the **small-longitudinal-residual collar**

`boxed(0<=tau<c)`                                              (7.1)

with a uniformly nondegenerate transverse plane and a uniformly noncollapsed total active rank-three Gram.

The exact `tau=0`, zero-heavy-pivot endpoint was paid in the preceding B13 run by `QFORM-NULLPIVOT-1PLUS2-PRODUCT-SMOOTHING-v1`. A merely small nonzero residual or merely small physical pivot is not declared paid: the live `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` correction forbids that inference.

## 8. Remaining implication

The next precise debt is

`QFORM-RANK3-SMALL-LONGITUDINAL-RESIDUAL-CLOSURE-v1`:

> In the mixed exact-rank-three branch, after conditioning at most the other heavy original coordinates and one exceptional residual-heavy light coordinate, prove a universal density bound when `0<=tau<c`, `G>=31I/800`, and `det S_active>93/8000`, while retaining original-coordinate product provenance. The difficult endpoint is a zero or very small heavy physical pivot together with a positive but sub-heavy longitudinal residual. One must use the transverse product banks jointly with that residual; continuity from the exact-zero case is not available.

Arbitrary additional spectral directions beyond exact rank three remain a separate full-target bridge. Hence the unrestricted QFORM conjecture remains OPEN.
