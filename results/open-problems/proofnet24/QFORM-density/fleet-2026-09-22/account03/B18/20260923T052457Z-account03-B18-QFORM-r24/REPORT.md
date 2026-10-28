SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T05:24:57Z.

attacking: high-shear/heavy-row exact-rank-three branch: transfer a sharp product-projection theorem into the completed account04/B18 zero-pivot packet without post-rotation independence.

# account03/B18 — source-separated high-shear Schur packet

**Run:** `20260923T052457Z-account03-B18-QFORM-r24`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Literature-to-proof transfer  
**Classification:** `PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / ESSENTIAL_PARTNER_RESULT_APPLIED`  
**Full target:** `OPEN / NOT PROVED`  
**Continuity:** proved for the new branch only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact theorem proved this run

### Theorem — `QFORM-SOURCE-SEPARATED-HIGHSHEAR-v1`

Let `X_0,X_1,...,X_m` be independent real random variables, each with a probability density bounded by one. Let `v_1,...,v_m in R^3` form a Parseval frame,

`sum_j v_j v_j^T = I_3`,

let `D` be an invertible real symmetric `3x3` matrix, let `n in S^2`, and let `r>0` satisfy

`n^T D n = 0`.

Put

`Y = sum_j v_j X_j`,

and

`Q = (Y + r n X_0)^T D (Y + r n X_0)`.

Assume the residual physical coordinates are **source-separated relative to n**: there is a partition `{1,...,m}=I disjoint_union J` such that

- `v_i in span{n}` for every `i in I`, and
- `v_j perpendicular n` for every `j in J`.

Then `Q` has a continuous density and

`||p_Q||_infinity <= 6*2^(2/3) r^(-2/3) |det D|^(-1/3)`.      (1.1)

If, moreover, the physical matrix of `Q` is exact rank three and its three nonzero eigenvalues all have modulus at least one, then

`||p_Q||_infinity <= 6*2^(2/3) ((1+r^2)/r^2)^(1/3)`.          (1.2)

Consequently,

- for every `r>=1`, `||p_Q||_infinity <=12`;
- for the genuinely high-shear range `r>=2`,

`||p_Q||_infinity <= 6*5^(1/3) = 10.25985568006018...`.       (1.3)

No leverage bound on the residual physical rows is imposed. Thus the result covers source-separated high-shear packets even when the capped-basis/diffuse-frame gates fail because of heavy rows.

## 2. Primary literature transfer and exact hypothesis audit

The source theorem used on the residual transverse bank is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889; arXiv:1507.07949. Their theorem says that if a probability density on `R^N` is a product `prod f_i`, with every one-dimensional density bounded by one, then every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`. No Gaussian, log-concavity, moment, bounded-support, connected-support, smoothness, centering, or iid assumption is required.

Primary source URL: https://arxiv.org/abs/1507.07949

I also rechecked Juškevičius--Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190. Its sharp Rogozin rearrangement theorem applies to sums of genuinely independent bounded-density random vectors. It cannot be applied termwise to the two-dimensional summands `w_j X_j` below, because each such summand is supported on a line and has no two-dimensional density. Hence the two-dimensional step below uses LPP, not an illicit termwise multidimensional Rogozin transfer.

Primary source URL: https://arxiv.org/abs/1503.09190

No exact published theorem matching the unrestricted QFORM target was found in this focused source check. This is not a novelty claim.

## 3. Product provenance created by the source-separated geometry

Choose an orthonormal basis `(n,e_2,e_3)` of `R^3`. Write

`S = n^T Y`,

`T = (e_2^T Y, e_3^T Y) in R^2`.

By source separation,

`S = sum_{i in I} (n^T v_i) X_i`,

while `T` depends only on the coordinates in `J`. Since the frame is Parseval and every `v_i` in `I` is parallel to `n` while every `v_j` in `J` is perpendicular to `n`, projecting

`sum_j v_j v_j^T=I_3`

onto `span{n}` and `n^perp` gives exactly

`sum_{i in I} (n^T v_i)^2 = 1`,                       (3.1)

and

`sum_{j in J} w_j w_j^T = I_2`,                       (3.2)

where `w_j=(e_2^T v_j,e_3^T v_j)`.

Thus `T` is a genuine two-dimensional orthogonal projection of the original cap-one product source on the coordinate bank `J`. LPP therefore gives

`||p_T||_infinity <= 2`.                              (3.3)

Define

`W = S + r X_0`.

The random vector `T` depends only on coordinates in `J`, whereas `W` depends only on `X_0` and coordinates in `I`. Hence

`W independent T`.                                    (3.4)

This is genuine independence in the original coordinates, not independence asserted after a rotation.

The density of `rX_0` is bounded by `1/r`, and convolution with the independent variable `S` cannot increase the `L^infinity` norm. Therefore

`||p_W||_infinity <= 1/r`.                            (3.5)

Notice that no density estimate for `S` is needed.

## 4. The designated account04/B18 result applied to an actual inequality

The completed account04/B18 result used here is the source-pinned banked zero-pivot theorem in

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

It applies the completed zero-pivot `1+2` theorem to a cap-one scalar independent of a two-dimensional vector of density cap `M`; for a nonsingular symmetric zero-pivot matrix `H` it yields a continuous density with

`||p||_infinity <= 6 M^(2/3)|det H|^(-1/3)`.          (4.1)

We need the scale-sensitive version when the scalar has density cap `N`, not merely cap one. This follows exactly by rescaling. If `Z` has density cap `N`, let `Z'=N Z`. Then `Z'` has density cap at most one. Replacing the first coordinate by `Z'/N` changes the coefficient matrix to

`H' = diag(N^(-1),1,1) H diag(N^(-1),1,1)`,

so

`det H' = N^(-2) det H`.

Applying (4.1) gives the dependence-safe scale-correct extension

`||p||_infinity <= 6 (MN)^(2/3)|det H|^(-1/3)`.       (4.2)

Now express `D` in the basis `(n,e_2,e_3)`. Since `n^T D n=0`,

`D_0 = [[0, ell^T],[ell,C]]`

is a symmetric zero-pivot matrix. It is nonsingular because `D` is. The quadratic form is exactly

`Q = (W,T)^T D_0 (W,T)`.                              (4.3)

Equations (3.3)--(3.5) match every hypothesis of (4.2) with

`M=2`, `N=1/r`, `|det D_0|=|det D|`.

Hence

`||p_Q||_infinity
 <= 6 (2/r)^(2/3)|det D|^(-1/3)`,                    (4.4)

which is (1.1). Continuity follows from the partner theorem after the harmless scalar rescaling.

This is an actual use of the designated partner theorem, not merely a citation to it.

## 5. Target normalization and the determinant identity

Let `L` be the `(m+1) x 3` coefficient matrix with first row `r n^T` and remaining rows `v_j^T`. The physical matrix is

`A = L D L^T`.

Because the residual frame is Parseval,

`L^T L = I_3 + r^2 n n^T`.                            (5.1)

Therefore

`det(L^T L)=1+r^2`.                                   (5.2)

The three nonzero eigenvalues of `A` are the eigenvalues of the symmetric matrix

`(L^T L)^(1/2) D (L^T L)^(1/2)`.

Indeed `L D L^T` and `D L^T L` have the same nonzero spectrum, while `D L^T L` is similar to the displayed symmetric matrix. Consequently the absolute product of the three nonzero eigenvalues is

`|det D| det(L^T L)=|det D|(1+r^2)`.                  (5.3)

Under the exact-rank-three target normalization all three nonzero eigenvalues have modulus at least one, so

`|det D|(1+r^2)>=1`.                                  (5.4)

Substituting (5.4) into (4.4) gives

`||p_Q||_infinity
 <= 6*2^(2/3) ((1+r^2)/r^2)^(1/3)`,                  (5.5)

which proves (1.2). The factor `((1+r^2)/r^2)^(1/3)` decreases for `r>0`. At `r=1` it equals `2^(1/3)`, giving exactly `12`. At `r=2` it equals `(5/4)^(1/3)`, so the high-shear range `r>=2` gives

`6*2^(2/3)*(5/4)^(1/3)=6*5^(1/3)=10.25985568006018...`.

## 6. Relation to the latest account04/B18 Schur-frame results

The newest account04/B18 diffuse-frame handoff (`math-open-problems@e9eb90e2a7746482fb3ba75bf449b224cbf507ce`) gives a continuous bound `<3e` when `0<r<=1` and every residual row has leverage at most `1/2`. Its mixed-volume predecessor (`math-open-problems@24a9362bd3f24a3849021093cf98611f95b5ab04`) gives `<8.785` on `1/2<=r<=2` under the row condition `p_j+q_j<=1`.

The present theorem pays a complementary region: it allows arbitrarily heavy residual rows and gives a uniform `<=10.260` bound for **all source-separated packets with r>=2**. Hence source-separated high shear is no longer an unpaid analytic branch. What remains is genuinely non-source-separated high shear, where the longitudinal aggregate and transverse pair share original coordinates.

## 7. Why the theorem does not silently overreach

A tempting normalization for a general Schur-isotropic packet is to combine `S+rX_0` into one zero-pivot scalar and then condition on the transverse projection. The scalar has a good marginal cap, but in the general packet it is dependent on the transverse pair because the same original coordinates contribute to both. The live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` explicitly rules out replacing the genuine scalar-vector independence in the zero-pivot theorem by bounded conditional densities. Therefore (4.2) is applied only after source separation supplies actual disjoint-coordinate independence.

This proof also does not use:

- post-rotation independence;
- arbitrary-joint coarea;
- a universal conditional projection-density moment;
- a fixed good physical minor or rank-three cross cut;
- pointwise law-uniform van-der-Corput decay;
- Gaussian, log-concave, moment, support, or connected-support hypotheses.

## 8. Literature non-transfer worth preserving

The Juškevičius--Lee multidimensional rearrangement theorem is powerful for sums of independent random vectors with actual ambient-dimensional density caps. In this packet the individual transverse summands `w_j X_j` are one-dimensional line laws in `R^2`, so that theorem does not directly supply the pair cap. LPP is precisely the correct source-valid theorem because it treats orthogonal marginals of the whole product density.

Likewise, a bounded two-dimensional projection density alone does not control an arbitrary indefinite quadratic pushforward. The nonlinear step here is supplied by the zero-pivot theorem and its genuine scalar-vector independence.

## 9. Scope and next unpaid implication

This theorem closes the **source-separated** exact-rank-three high-shear Schur-isotropic branch and proves continuity there. It does not solve arbitrary exact-rank-three high shear because the row vectors need not split into longitudinal-only and transverse-only source banks. It also does not absorb arbitrary extra spectrum.

The next local implication is therefore:

`QFORM-HIGHSHEAR-NONSOURCESEPARATED-AGGREGATION-v1`:

> in the exact-rank-three Schur-isotropic packet with `r>2`, either extract a product-preserving aggregate transformation that produces genuine scalar-versus-pair independence without conditioning-generated cap loss, or route the shared-source rows to an already-paid heavy-hub / physical-pair / ridge certificate.

The conjugate-shear theorem in account01/B14 (`math-open-problems@aa7d48b99329ae100c0b50fa12a23d4dfc6399b8`) is relevant to this next step because it shows that certain shears can be formed *before* conditioning while retaining a cap-one source. But no claim is made here that every nonsource-separated row geometry has that form.

**Full QFORM remains OPEN / NOT PROVED. Full-target continuity remains OPEN.**

## 10. Source pins

- LPP primary source: https://arxiv.org/abs/1507.07949
- Juškevičius--Lee primary source: https://arxiv.org/abs/1503.09190
- Designated account04/B18 banked zero-pivot result: `yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.
- Latest account04/B18 diffuse-frame addendum: `yspennstate/math-open-problems@e9eb90e2a7746482fb3ba75bf449b224cbf507ce`.
- account01/B14 conjugate-shear source: `yspennstate/math-open-problems@aa7d48b99329ae100c0b50fa12a23d4dfc6399b8`.

Repository retrieval is not native mathematical-brain ingestion. This run is `WITHOUT_VERIFIED_BRAIN`.
