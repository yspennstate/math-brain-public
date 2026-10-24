SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T01:01:43Z.
attacking: QFORM-O3-ROBUST-2PLUS1-GROUPED-PAYMENT-v1 — pay the robust one-scalar plus rank-two original-product grouped block without post-rotation independence or an arbitrary-joint coarea bound.

# account03/B19 r21 — robust 2+1 grouped payment

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly  
**Owner control at prepublication refresh:** revision `2026-09-22.15`, brain main `0da7ea6e2937acfda046079667a2939026c41a8e`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / PROVED TARGET-LEVEL BRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`.

## 1. Exact target and correction boundary

The unrestricted theorem remains open: for arbitrary independent real coordinates with marginal densities at most one and arbitrary symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal finite essential bound for the density of `X^T A X`, or give a target-valid counterexample. Global continuity is also open.

This argument does not use the refuted law-uniform pointwise Fresnel bound, the refuted arbitrary-joint rank-three coarea inequality, a positive conditional projection-density moment, post-rotation independence, a worst-fiber supremum, or selection of one uniformly good physical minor. The current correction inbox was refreshed before publication.

The immediate predecessor is account03/B19 r20,

`yspennstate/math-open-problems@9280165827267931c007f3c9885d3e56dfcd0723`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T002541Z-account03-B19-QFORM-r20/REPORT.md`.

Its surviving exact-rank-three O3 state supplies two disjoint original-coordinate source banks: a rank-one companion bank `H` and a genuinely rank-two bank `G`. In spectral coordinates,

`sum_(i in H) u_i u_i^T = lambda v v^T`,                         (1.1)

`sum_(i in G) u_i u_i^T = S_G = W W^T`,                         (1.2)

where `W` is `3 x 2` of rank two. For one of the two possible companions r20 proved the grouped spectral map

`L=[sqrt(lambda) v, W]`                                          (1.3)

satisfies

`det(L)^2 > 1/6`,                                                (1.4)

and, because the third source bank is the other companion,

`L L^T = I-lambda_b v_b v_b^T <= I`.                            (1.5)

The missing implication was to turn this grouped volume into a universal density payment while retaining the original product provenance.

## 2. Physicalize the rank-two bank without inventing independence

Let `R_G` be the `|G| x 3` matrix whose rows are the spectral rows `u_i^T`, so

`R_G^T R_G = W W^T`.                                             (2.1)

Define

`U = R_G W (W^T W)^(-1)`.                                       (2.2)

Then

`U^T U = I_2`,                                                   (2.3)

and

`R_G^T = W U^T`.                                                 (2.4)

Indeed, (2.3) follows by substituting (2.1), and (2.4) follows because every column of `R_G^T` lies in `range(W)=range(W W^T)`.

Therefore, with the untouched original product source `X_G`,

`Z:=U^T X_G`                                                     (2.5)

is a genuine two-dimensional orthogonal projection of the original independent coordinates, and the entire spectral contribution of `G` is exactly `WZ`. No assertion is made that the two coordinates of `Z` are independent.

By account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical mathematics

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`,

the joint density of `Z` satisfies the safe dimension-free bound

`||p_Z||_infinity <= e`.                                         (2.6)

For the rank-one bank, write its rows as `u_i=c_i v`, so `sum c_i^2=lambda`. Set

`Y=lambda^(-1/2) sum_(i in H) c_i X_i`.                         (2.7)

The coefficient vector in (2.7) has Euclidean norm one. The one-dimensional product-projection theorem gives

`||p_Y||_infinity <= sqrt(2)`.                                  (2.8)

Because `H` and `G` are disjoint original-coordinate banks, `Y` and `Z` are genuinely independent. Put

`X_0=sqrt(2)Y`; then `||p_(X_0)||_infinity<=1`.                  (2.9)

Conditioning on every original coordinate outside `H union G` contributes only affine and constant terms in `(X_0,Z)` and preserves this independence.

## 3. The grouped volume forces a uniformly nondegenerate 3x3 active matrix

After the scalar normalization (2.9), the active spectral map is

`L_0=[sqrt(lambda/2)v, W]
    =L diag(1/sqrt(2),1,1)`.                                    (3.1)

Hence

`det(L_0)^2 = det(L)^2/2 > 1/12`.                               (3.2)

Also

`L_0 L_0^T <= L L^T <= I`,                                      (3.3)

so every singular value of `L_0` is at most one. Since their product is `|det L_0|>1/sqrt(12)`,

`s_min(L_0)>1/sqrt(12)`.                                        (3.4)

Let the exact-rank-three spectral coefficient satisfy

`M=M^T`, `s_min(M)>=1`,                                         (3.5)

and define the active grouped quadratic matrix

`B=L_0^T M L_0`.                                                 (3.6)

Then

`s:=s_min(B)
 >=s_min(L_0)^2 s_min(M)
 >1/12`,                                                         (3.7)

while

`D:=|det B|
 =|det M| det(L_0)^2
 >1/12`.                                                         (3.8)

Thus the grouped packet is not merely a large determinant packet: after paying the scalar density cap, the full active three-dimensional quadratic matrix has a uniform least singular value.

## 4. Scaled near-null cross-resource lemma

Write a general symmetric invertible `3 x 3` matrix with `s_min(B)>=s>0` as

`B=[[a,b^T],[b,C]]`.                                             (4.1)

Assume `|a|<s`. Rotate only the already-joint two-dimensional receiver plane so `b=(beta,0)` and

`C=[[c,d],[d,e_0]]`.                                             (4.2)

Set

`P=beta^2 |e_0|`.                                                (4.3)

### Lemma 4.1 — `QFORM-SCALED-NEARNULL-CROSS-RESOURCE-v1`

`b!=0` and

`boxed: P >= (1-|a|/s) |det B|.`                                (4.4)

### Proof

If `det C=0`, the determinant identity

`det B=a det C-beta^2 e_0`                                      (4.5)

gives `P=|det B|`.

If `det C!=0`, let

`r=a-b^T C^(-1)b`                                               (4.6)

be the scalar Schur complement. Since `(B^(-1))_00=r^(-1)` and `||B^(-1)||_op<=1/s`, we have `|r|>=s`. Because

`|det B|=|det C| |r|`,                                          (4.7)

it follows that

`|det C|<=|det B|/s`.                                           (4.8)

Now (4.5) and reverse triangle give

`P=|a det C-det B|
 >=|det B|-|a||det C|
 >=(1-|a|/s)|det B|`.                                           (4.9)

If `b=0`, then `r=a`, contradicting `|a|<s`. QED.

This is the scale-correct version of account01/B16's completed near-null cross-resource lemma and is the extra currency that the live projection-cap counterexample shows is necessary.

## 5. Pay the near-null grouped branch

Return to (3.6) and split at

`|a|<=1/24`.                                                     (5.1)

By (3.7), `|a|<s/2`, so Lemma 4.1 yields

`P>D/2`.                                                         (5.2)

Now apply account01/B16 `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1`, canonical report

`yspennstate/math-open-problems@8d262d18e5581cd02b8ea8be5102aa2a6d30ddd7`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260923T003846Z/REPORT.md`.

For a cap-one scalar independent of a two-dimensional receiver of density cap `M_2`, that theorem gives, with arbitrary affine terms,

`||p_Q||_infinity
 <=103680^(1/3) M_2^(2/3) (D P)^(-1/6)`.                        (5.3)

Using `M_2<=e`, (5.2), and `D>1/12`,

`||p_Q||_infinity
 <103680^(1/3) e^(2/3) 2^(1/6) 12^(1/3)
 =235.1401181449...
 <236`.                                                          (5.4)

This is exactly where the nonzero transverse resource is spent; a bare two-dimensional density cap is not used as a substitute.

## 6. Pay the non-small scalar-pivot branch

Assume now

`|a|>1/24`.                                                       (6.1)

Complete the square only in the independent cap-one scalar `X_0`. The square-pushforward kernel gives, uniformly in the `Z`-dependent translation,

`p_Q(t)
 <=|a|^(-1/2) E |t-[Z^T S Z+ell^T Z+c]|^(-1/2)`,               (6.2)

where

`S=C-bb^T/a`,                                                    (6.3)

and

`|det S|=D/|a|`.                                                 (6.4)

The completed orientation-free rank-two affine half-Riesz theorem,

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`,

applies directly to `Z=U^T X_G`. The affine term lies in the same two-dimensional projection range, so its sharper in-range constant yields

`sup_t E |t-[Z^T S Z+ell^T Z+c]|^(-1/2)
 <=16 sqrt(30)|det S|^(-1/4)`.                                  (6.5)

Combining (6.2)-(6.5),

`||p_Q||_infinity
 <=16 sqrt(30)|a|^(-1/4)D^(-1/4)`.                              (6.6)

Using (6.1) and `D>1/12`,

`||p_Q||_infinity
 <16 sqrt(30)(24*12)^(1/4)
 =361.0178969362...
 <362`.                                                          (6.7)

No joint receiver coarea estimate is invoked; the product-projection provenance enters through the rank-two half-Riesz theorem.

## 7. Main closure theorem

### Theorem 7.1 — `QFORM-O3-ROBUST-2PLUS1-GROUPED-PAYMENT-v1`

Every exact-rank-three O3 state satisfying the grouped conclusion of account03/B19 r20,

`det([sqrt(lambda)v,W])^2>1/6`,                                 (7.1)

has an essentially bounded output density, for every admissible independent cap-one product law and all affine terms induced by conditioning outside the two active source banks, with

`boxed: ||p_Q||_infinity <362.`                                 (7.2)

The proof is the exhaustive split (5.1)/(6.1). All signs are allowed because only singular values, absolute determinants, Schur identities and the sign-free source theorems enter. Exact zero scalar pivot belongs to the near-null case. The active matrix cannot be singular by (3.7). Repeated eigenvalues cause no issue.

This closes the exact implication left open by r20 and therefore removes the near-singular/double-near-null exactly-one-internal-rank-two O3 chamber from the current proof tree.

Continuity is **not claimed** for Theorem 7.1: the near-null source theorem used here supplies essential boundedness, and the present assembly does not upgrade it to a continuous representative.

## 8. Designated partner account04/B19 applied to an actual inequality

Fresh search found the completed designated-partner report

`account04/B19`, `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`,

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`.

In its residual-diffuse exact null-coloop scope it proves, for `0<D_res<=1`,

`||p_Q||_infinity <34 sqrt(log(e/D_res))`.                       (8.1)

Therefore on the actual range

`e^(-8)<=D_res<=1`,                                              (8.2)

`log(e/D_res)<=9`, and hence

`boxed: ||p_Q||_infinity<102.`                                  (8.3)

The same partner source pays `D_res>=1` by `<11.748` and the exact singular endpoint `D_res=0` by `<5.844`; thus its branch is explicitly bounded by `<102` on `{0} union [e^(-8),infinity)`. This is an equation-level application of the designated partner result, not a citation-only mention. I do not extend it beyond its stated null-coloop residual-diffuse scope.

## 9. Compact proof map and first remaining debt

This run pays the precise r20 robust `2+1` grouped block. The full QFORM theorem is nevertheless still **OPEN / NOT PROVED / NOT DISPROVED**. In particular, this argument is exact-rank-three and does not provide the missing descent in the presence of arbitrary additional spectrum.

Within the r20 O3 decomposition, the first structural chamber not covered by the just-closed exactly-one-internal-rank-two argument is the state with **at least two resource banks of internal spectral rank at least two**. A source-valid successor implication is therefore

`QFORM-O3-TWO-INTERNAL-RANK2-BANKS-ROUTING-v1`:

> Starting from two robust original-product rank-two source banks in the exact-rank-three O3 decomposition, extract a uniformly payable grouped packet (possibly by a 1+2 compression as above, a stable-rank cross bank, or a paid diffuse-ridge certificate) without selecting a vanishing local minor; then separately splice that exact-rank-three closure into arbitrary-extra-spectrum descent.

The other global debt is precisely that arbitrary-extra-spectrum splice. Neither is silently claimed here.

## 10. Checks

`CHECK.py` and `CHECK_OUTPUT.txt` in this run directory verify the numerical constants and thresholds. The output terminates

`QFORM_B19_R21_GROUPED_PAYMENT_CHECK_PASS`.

Those computations are arithmetic regression only; the mathematical proof is Sections 2-7 above.
