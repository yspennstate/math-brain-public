SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-24T10:09:32Z.
attacking: `QFORM-R47-DIAGONAL-SCHUR-E2-DIFFUSE-OR-FIXED-CARRIER-v1`; spend the scalar-Schur pair-volume at the half-Riesz level with the reviewed sharp-HY compiler, and identify the exact physical concentration endpoint without selecting one tiny minor.

# account02/B02 r11 — sharp D2 payment of the r47 diagonal branch and a diffuse two-star exact-target obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Integrated Fourier estimate / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Execution: `VERIFIED_BRAIN` in the programme's narrow sense: authenticated repository retrieval plus actual use of the preceding account02/B02 receiver-memory snapshot; no native learned-memory ingestion is claimed.

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities at most one; arbitrary real symmetric `A`; at least three eigenvalues of modulus at least one. No moments, support bounds, log-concavity, iid hypothesis, diagonal-basis independence, or post-rotation independence is used. Continuity remains a separate conclusion.

The early note in this run re-derived the sharp D2 half-potential constant. A fresh source search then located the already-completed theorem at account03/B01; accordingly **the D2 theorem itself is not claimed as new here**. The new work is its source-pinned application to the newest designated-partner r47 diagonal endpoint, the resulting quantitative anchor tradeoff, and the exact-target family showing why aggregate D2 rather than one-minor/D'/D5 extraction is genuinely necessary.

## 1. Fresh sources and correction boundary

Owner control remains revision `2026-09-22.15`, QFORM-only. I read the required pinned package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Its D', D5, fractional-potential and square-peel interfaces are retained at their stated scopes. In particular no law-uniform scalar pointwise Fresnel estimate is used.

The reviewed sharp Hausdorff--Young volume calculation is source-pinned at

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For a literal physical cross block `B`, the degree-three theorem has the genuine Fourier-L1 conclusion

`||p_Q||infinity <= 3e/[(3-2q)sqrt(q)] E3(B)^(-1/6)`

when all relevant third-volume row marginals are at most `q/2`, `1<=q<3/2`; the reviewed degree-five ungated exit is

`||p_Q||infinity <= (5e/sqrt(2)) E5(B)^(-1/10)`.

Both keep arbitrary same-bank curvature and outside coefficients.

The completed general fractional-volume theorem actually used here is

`QFORM-CRITICAL-RANK2-HALFRIESZ` / Theorem 2.1-Section 3 of

`yspennstate/math-open-problems@936b0f0bad22de82921c2a743fb0738226270348`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T013054Z-auto11/REPORT.md`.

For disjoint ORIGINAL banks and

`R=F(X_I)+2 X_I^T M X_J+G(X_J)`,

put

`Z2=e2(M^T M)>0`,

and let `alpha_i` be the row marginals of the normalized squared `2x2`-minor law. If `h=max_i alpha_i<1` and

`q=max(1,2h)<2`,

then

`H_(1/2)(R)
 <= [4 sqrt(2e) q^(-1/4)/(2-q)] Z2^(-1/8).`                 (1.1)

At `h<=1/2`, the coefficient is `4sqrt(2e)=9.326575926388...`; at `h<=3/4`, it is

`8sqrt(2e)(3/2)^(-1/4)=16.855025387808...`.                 (1.2)

This is a half-potential receiver, not an unweighted Fourier-L1 theorem. It is exactly suited to a scalar square peel.

A complementary completed scalar-pair structural theorem is account02/B13's

`QFORM-SCALAR-D2-SINGLE-BISTAR-v1`,

`yspennstate/math-open-problems@e499a26f35ec939d0fae47bbc5ccf8c0b7683516`,

which used the earlier rough-HY D2 constant. Section 3 below gives the sharper fixed-r47 specialization using (1.1).

The newest completed designated partner `account03/B02` is r47,

`yspennstate/math-open-problems@859066cc3edee1bbeafe367e3bf2d630a4c425d9`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260924T045848Z-account03-B02-qform-r47/REPORT.md`.

Its diffuse `1/19` spectral-window branch is already paid by genuine Fourier L1. Failure yields a literal strong physical certificate, including the diagonal alternative

`boxed: |A_ii|>1/228,`                                      (1.3)

or a strong off-diagonal/carrier alternative. On its live near-rank-two full cut it also preserves `x1*x2>247/576`.

The live correction boundary is retained: no post-rotation independence; no arbitrary-joint coarea; no conditional projection-density cap; no deletion of a nonzero tail; no universally good single physical minor; and no mixed-norm absolute-value closure forbidden by the newest hub-star correction.

## 2. Exact scalar completion of the partner's diagonal branch

Take the literal physical coordinate `i` supplied by (1.3), and write

`d=A_ii`, `|d|>1/228`.

Complete this ORIGINAL coordinate exactly. The full form has the source-valid representation

`Q=d(X_i+H(X_{i^c}))^2+R(X_{i^c}),`                          (2.1)

where the quadratic coefficient of `R` is the exact scalar Schur complement

`S=A[i^c,i^c]-A[i^c,i] d^(-1) A[i,i^c]`.                    (2.2)

No independence is asserted between the shift `H` and `R`. The pinned scalar-square peel is precisely designed for this situation:

`||p_Q||infinity <= |d|^(-1/2) H_(1/2)(R).`                  (2.3)

Now choose any disjoint ORIGINAL-coordinate banks `I,J subset i^c`, put

`M=S[I,J]`, `Z2=e2(M^T M)>0`,                               (2.4)

and denote the row/column pair-volume marginals by `alpha_r,beta_c` under the single joint normalized law

`w_(P,T)=det M[P,T]^2/Z2`, `|P|=|T|=2`.                     (2.5)

This is the exact physical Schur block; no cross-only pseudo-Schur object is substituted for it.

## 3. New r47 compiler — `QFORM-R47-DIAGONAL-D2-ANCHORTRADEOFF-v1`

Fix `0<=theta<1` and set

`h=(1+theta)/2`.                                             (3.1)

Then one of the following two conclusions holds for the physical Schur cross block (2.4).

### Diffuse payment

If either every row marginal obeys `alpha_r<=h` or every column marginal obeys `beta_c<=h`, then (1.1), its transpose, and (2.3) give

`boxed:
 ||p_Q||infinity
 < C_r47(theta) Z2^(-1/8),
}`                                                            (3.2)

where

`C_r47(theta)
 =4 sqrt(2e) sqrt(228) (1+theta)^(-1/4)/(1-theta).`          (3.3)

For `theta=0`,

`boxed: ||p_Q||infinity <140.828209 Z2^(-1/8).}`             (3.4)

For `theta=1/2`,

`boxed: ||p_Q||infinity <254.505303 Z2^(-1/8).}`             (3.5)

Continuity is not asserted by this square-peel splice.

### Physical bi-star concentration

If neither diffuse gate holds, choose a physical row `r` and physical column `c` with

`alpha_r>h`, `beta_c>h`.                                    (3.6)

Because these are marginals of the **same** squared-minor law (2.5), inclusion-exclusion gives

`P(r in P and c in T)>2h-1=theta`.                           (3.7)

Equivalently the common incident pair-volume

`H2^(r,c)(M)
 :=sum_(P contains r, T contains c) det M[P,T]^2`            (3.8)

obeys

`boxed: H2^(r,c)(M)>theta Z2.}`                              (3.9)

At the convenient fixed choice `theta=1/2`, failure of the quantitative bound (3.5) therefore forces **one literal physical Schur row/column pair carrying more than half of all pair-volume**.

This proves the diffuse half of the previous B02 unpaid implication and turns its failure into a fixed physical bi-star/near-coloop carrier. It does not select a single `2x2` minor and therefore does not violate the one-good-minor correction.

### Adaptive high-ratio sharpening

The same calculation sharpens the completed B13 scalar-D2 concentration threshold. Let a slab have ratio `rho` and define

`T=rho |d|^(1/2) Z2^(1/8).`                                  (3.10)

Put `K=2sqrt(2e)`. If

`T>=4K=8sqrt(2e)=18.6531518528...`,                          (3.11)

choose `epsilon=2K/T`, `h=1-epsilon`. Since `(2h)^(-1/4)<=1`, the sharp D2 constant is at most `K/epsilon=T/2`. If all row marginals were at most `h`, the slab ratio would contradict the D2/square-peel bound; hence a row marginal exceeds `h`. The same argument after transposition gives a column marginal exceeding `h`, and therefore

`boxed:
 P(r in P and c in T)
 >1-8sqrt(2e)/T.
}`                                                            (3.12)

The rough-HY B13 threshold was `16e^(1/4)=20.5444066670...`; the sharp-HY threshold here is `8sqrt(2e)=18.6531518528...` on the same exact scalar-Schur scope.

## 4. Exact-target family showing aggregate D2 is indispensable

For every integer `k>=2`, use ORIGINAL coordinates

`W`, `U_1,...,U_k`, `U'_1,...,U'_k`, `V_1,V_2`.

Let the only nonzero coefficients of `A_k` be

`A_WW=1`,

`A_(U_j,V_1)=A_(V_1,U_j)=1/sqrt(k)`,

`A_(U'_j,V_2)=A_(V_2,U'_j)=1/sqrt(k)`, `1<=j<=k`.            (4.1)

Thus `A_k` is the direct sum of one scalar `1` and two normalized physical stars.

Each star block has nonzero eigenvalues `+1,-1`; hence

`boxed: spec_nonzero(A_k)={-1,-1,1,1,1}.}`                   (4.2)

So every `A_k` satisfies the exact owner's three-large-eigenvalue target.

The r47 diffuse `1/19` window does not pay this family: the isolated pivot and the two star centers are highly localized. Instead the partner's strong physical-diagonal alternative fires at `W`, with `d=1`.

After pivoting `W`, take the literal leaf-to-center Schur cross block

`M_k =`
`[ 1/sqrt(k) * 1_k    0 ]`
`[ 0                  1/sqrt(k) * 1_k ]`,                    (4.3)

viewed as a `2k x 2` matrix. Its singular values are exactly `1,1`, so

`boxed: Z2=e2(M_k^T M_k)=1.}`                                (4.4)

A nonzero `2x2` minor must choose one leaf from each star and both center columns. There are `k^2` such minors, each with determinant modulus `1/k`, hence squared weight `1/k^2`. Therefore every leaf-row marginal is exactly

`alpha_j=1/k<=1/2`,                                           (4.5)

while both column marginals equal one; the endpoint columns are allowed in the pinned BL proof.

Applying the completed sharp D2 theorem and the scalar square peel gives, uniformly in `k` and in **all** cap-one product input laws,

`boxed:
 ||p_(X^T A_k X)||infinity
 <=4sqrt(2e)
 =9.326575927... .
}`                                                            (4.6)

This is an actual payment of the newest partner's strong-diagonal branch by aggregate physical Schur pair-volume.

### Why selecting one physical 2x2 carrier is the wrong replacement

Every nonzero physical `2x2` minor of `M_k` has determinant modulus `1/k`; in fact its second singular value is `1/sqrt(k)`. The preceding B02 local four-variable scalar-pivot receiver would therefore produce a bound deteriorating like `k^(1/4)`, whereas (4.6) is uniform. Thus the aggregate pair-volume cannot be replaced by a uniformly good single physical `2x2` minor.

### D', reviewed E3 sharp-HY, and D5 have zero currency on the same exact-target family

Each of the two nontrivial connected components of `A_k` is a star. For any disjoint physical row/column sets, the center of a given star can lie on at most one side, so that star contributes rank at most one to the cross block. The two stars together therefore give

`rank A_k[I,J]<=2`                                             (4.7)

for every disjoint physical `I,J`; the isolated diagonal pivot contributes no cross edge. Consequently

`boxed:
 E3(A_k[I,J])=E5(A_k[I,J])=0
 for every disjoint physical cut.
}`                                                            (4.8)

Hence D', the reviewed sharp-HY E3 density compiler, and D5 are all genuinely unavailable on this exact-target family. This is a source-valid obstruction to the proof architecture

> every strong-diagonal survivor must eventually create positive physical E3/E5 or one uniformly good physical 2x2 minor.

It is **not** a QFORM counterexample.

## 5. The exact family still has a uniform integrated characteristic-function bound

The preceding obstruction does not refute the target-wide Fourier-L1 possibility. In fact the same `A_k` has a clean product-preserving integrated estimate.

Write

`Y_1=k^(-1/2) sum_(j=1)^k U_j`,
`Y_2=k^(-1/2) sum_(j=1)^k U'_j`.                              (5.1)

Then

`Q_k=W^2+2V_1Y_1+2V_2Y_2`,                                   (5.2)

and the three ORIGINAL-coordinate groups

`{W}`, `{V_1,U_1,...,U_k}`, `{V_2,U'_1,...,U'_k}`

are genuinely independent. No spectral rotation is used.

For one star factor, apply the completed general sharp volume theorem at exterior degree `k=1` (here `k` denotes exterior degree, not the family parameter), with `q=1`, `Z1=1`, and row marginals `1/k<=1/2`. It gives

`|phi_star(t)|<=min(1,sqrt(e*pi)|t|^(-1/2)).`                 (5.3)

Therefore

`||phi_star||_3^3<=6e*pi`,
`||phi_star||_3<=(6e*pi)^(1/3).`                              (5.4)

For the scalar square `W^2`, the completed square-density/Hausdorff--Young estimate from the preceding B02 report gives

`||phi_(W^2)||_3 <= (2pi)^(1/3) 5^(2/3).`                    (5.5)

Hölder in the common time variable and the genuine group independence in (5.2) now yield

`boxed:
 integral_R |phi_(Q_k)(t)| dt
 <= pi (1800 e^2)^(1/3)
 =74.433829332... .
}`                                                            (5.6)

Hence this family has a continuous `C0` density, with the Fourier-inversion estimate

`||p_Qk||infinity <=(1800e^2)^(1/3)/2
 =11.846511872...`,                                           (5.7)

while the sharper half-potential density bound is (4.6).

The conceptual point is precise: **D'/D5 can be identically zero and every single `2x2` minor can vanish with dimension, yet an aggregate D2 half-potential plus source-separated lower-degree Fourier credits still gives uniform control.** This is the mechanism that the remaining bi-star branch should preserve.

## 6. What remains

Three unchanged mechanisms are now ruled out on the strong-diagonal endpoint:

1. force a physical E3 block — impossible on (4.1);
2. force D5 — impossible on (4.1);
3. select one uniformly conditioned physical `2x2` Schur minor — quantitatively false on (4.3).

The mechanism therefore changes to aggregate pair-volume and source-separated star credits.

The first unpaid implication is now

`QFORM-R47-DIAGONAL-SCHUR-E2-SIZE-OR-BISTAR-GLUE-v1`:

after the exact partner pivot `|d|>1/228`, use Schur persistence of two large spectral directions to show that either some literal physical Schur cross block has quantitative `Z2` and is paid by Section 3, or the second-compound mass is forced into an overlap/principal/bi-star carrier that admits a product-preserving grouped receiver. If the D2 volume is concentrated, preserve the common physical row/column from (3.9) rather than selecting one minor. The newest mixed-norm correction forbids taking absolute values too early in a hub-star/fiber-L2 splice.

The carrier-aligned off-diagonal-hub and at-most-four-near-coloop alternatives from r47 remain separately unpaid.

No exact-target QFORM counterexample was found. The unrestricted essential-density theorem remains OPEN; full-target continuity remains OPEN; and the target-wide unweighted Fourier-L1 criterion remains OPEN / not refuted.

## 7. Telemetry boundary

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort: `UNKNOWN`. Provider reasoning-token count and provider thinking seconds: `null / NOT_EXPOSED`. Elapsed wall time is `UNKNOWN/null`; no pure-thinking duration is inferred.
