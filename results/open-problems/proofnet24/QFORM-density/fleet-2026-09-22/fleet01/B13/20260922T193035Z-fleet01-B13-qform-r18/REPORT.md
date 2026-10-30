SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B13, 2026-09-22T19:30:35Z.
attacking: the remaining exact-rank-three one-heavy/two-transverse geometry, beginning with the zero-heavy-pivot endpoint and keeping the original product provenance.

# A 1+2 null-pivot product-smoothing lemma and closure of the graph-plane endpoint

**Run:** `20260922T193035Z-fleet01-B13-qform-r18`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_ENDPOINT / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full quadratic-form bounded-density conjecture remains OPEN. This report proves a new product-preserving endpoint theorem inside the exact-rank-three mixed branch isolated in the preceding run. It does not use arbitrary-joint rank-three coarea, conditional projection-density moments, law-uniform pointwise quadratic Fourier decay, post-rotation independence, a fixed good minor, bounded support, or a fixed fragment count.

## 1. Fresh sources and exact dependencies


The designated partner result actually consumed is fleet02/B13 run `20260922T182158Z-fleet02-B13-qform-4ebdd821`, canonical proof

`yspennstate/math-open-problems@d511859edaa636cdc00fcd64155ab07506875c3d`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T182158Z-fleet02-B13-qform-4ebdd821/REPORT.md`.

It gives the exact-rank-three heavy/light trichotomy with the only surviving Gram regime `s_3<3/5<s_2`, and its earlier exact bang-bang theorem

`yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T115714Z-fleet02-B13-qform-480ba28b/REPORT.md`

identifies the slab supremum over all cap-one product densities with the supremum over arbitrary measure-one product indicators, with zero loss.

The immediate predecessor is fleet01/B13 run `20260922T190849Z-fleet01-B13-qform-r17`,
`yspennstate/math-open-problems@01c524aa389abf1b9b58c852bfa11fc747ec5b59`, which proves in the surviving mixed regime that one heavy original coordinate `i` can be chosen so that, with `u=r_i/||r_i||`, `c=||r_i||^2>3/10`, and transverse light rows `p_j=P_{u^perp}r_j`,

`G=sum_{j in L} p_j p_j^T` satisfies `det G>=1/25` and `(1/25)I<=G<=I`.

The projection-density input used below is `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, fleet02/B06,
`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. For a two-dimensional linear projection with coefficient Gram `G`, it gives the joint density cap `e/sqrt(det G)` without creating independence after a rotation.

## 2. New analytic lemma: one independent scalar plus a capped two-dimensional source

### Theorem 2.1 — `QFORM-NULLPIVOT-1PLUS2-PRODUCT-SMOOTHING-v1`

Let `X` be independent of a random vector `(V,W)`. Assume `X` has a probability density `f` with `||f||_infinity<=K`, while `(V,W)` has a joint probability density `g` with `||g||_infinity<=M`. Let

`Q=2b X V + kappa V^2 + 2d V W + e W^2 + (arbitrary affine terms)`,

where `b!=0` and `e!=0`. Then `Q` is absolutely continuous and

`boxed(||p_Q||_infinity <= 6 K^(2/3) M^(2/3) |b|^(-2/3) |e|^(-1/3)).`      (2.1)

Equivalently, if the quadratic matrix in `(X,V,W)` is

`B=[[0,b,0],[b,*,*],[0,*,e]]`,

then `|det B|=b^2|e|` and

`boxed(||p_Q||_infinity <= 6 K^(2/3) M^(2/3) |det B|^(-1/3)).`            (2.2)

#### Proof

First shear `W` by `W -> W+(d/e)V`. This has determinant one, preserves the joint density cap `M`, preserves independence from `X`, and removes the `VW` term. Since `b e!=0`, the resulting quadratic matrix is invertible, so fixed translations of `X,V,W` remove all affine terms. Such translations preserve independence and both density caps. Thus it suffices to treat

`Q=2bXV+kappa V^2+eW^2`.                                                (2.3)

Let

`m(v)=int_R g(v,w)dw`

be the marginal density of `V`. For almost every `v` with `m(v)>0`, the conditional density of `W|V=v` is bounded by `M/m(v)`.

There are two complementary conditional estimates.

**Linear-X estimate.** Conditional on `V=v,W=w`, the map in `X` is affine with slope `2bv`. Hence for `v!=0`,

`h_v(t):=p_(Q|V=v)(t) <= K/(2|bv|)`,

and therefore

`m(v)h_v(t) <= K m(v)/(2|b||v|)`.                                    (2.4)

**Square-W estimate.** Conditional on `V=v`, the density of `eW^2` is bounded by

`[M/(m(v)sqrt(|e|))] |y|^(-1/2)`

on its supported half-line. Consequently

`h_v(t) <= [M/(m(v)sqrt(|e|))] int f(x)|t'-2bvx|^(-1/2)dx`.              (2.5)

For every probability density `f<=K`, symmetric decreasing rearrangement of the kernel gives

`sup_a int f(x)|x-a|^(-1/2)dx
 <= K int_{-1/(2K)}^{1/(2K)} |x|^(-1/2)dx
 =2sqrt(2K)`.                                                         (2.6)

Scaling (2.6) by `2bv` in (2.5) yields

`m(v)h_v(t) <= [2M sqrt(K)/sqrt(|be|)] |v|^(-1/2)`.                    (2.7)

Now split the `v` integral at an arbitrary `R>0`. On `|v|<=R`, (2.7) gives

`int_{|v|<=R} m(v)h_v(t)dv
 <= [8M sqrt(K)/sqrt(|be|)] sqrt(R)`.                                 (2.8)

On `|v|>R`, (2.4) and `int m=1` give

`int_{|v|>R} m(v)h_v(t)dv
 <= K/(2|b|R)`.                                                       (2.9)

Thus

`p_Q(t) <= A sqrt(R)+B/R`,
`A=8M sqrt(K)/sqrt(|be|)`, `B=K/(2|b|)`.                              (2.10)

The exact minimum occurs at `R^(3/2)=2B/A` and equals

`3*2^(-2/3) A^(2/3)B^(1/3)
 =6 K^(2/3)M^(2/3)|b|^(-2/3)|e|^(-1/3)`.                             (2.11)

The exceptional fiber `v=0` has zero probability because `V` has a density. The conditional densities above therefore also establish absolute continuity. QED.

### Why this lemma is product-safe

Only the scalar `X` is required to be independent of the **whole** pair `(V,W)`. The two coordinates `V,W` may be arbitrarily dependent. An orthogonal change of variables inside their already-joint two-dimensional law is therefore legitimate and preserves its density cap; no post-rotation independence is asserted.

## 3. Application to the mixed exact-rank-three endpoint

Work in the mixed branch delivered by the designated partner and the preceding B13 reduction. Thus

`A=R Lambda R^T`, `R^T R=I_3`, `min |eig(Lambda)|>=1`,

and the chosen heavy row is

`r_i=sqrt(c)u`, `c>3/10`,

while the light rows decompose as

`r_j=q_j u+p_j`, `p_j in u^perp`,

with

`G=sum_{j in L}p_jp_j^T >=(1/25)I`, `det G>=1/25`.                     (3.1)

Write the full light Gram in the orthogonal decomposition `Ru direct_sum u^perp` as

`S=[[s,h^T],[h,G]]`,
`s=sum q_j^2`, `h=sum q_j p_j`.                                       (3.2)

Define the nonnegative regression residual

`tau=s-h^T G^(-1)h=det(S)/det(G)`.                                    (3.3)

The endpoint treated here is

`boxed(tau=0 and A_ii=0)`.                                             (3.4)

The first condition says that the light spectral cloud is exactly a two-dimensional graph over its transverse plane. Indeed, if `P` is the matrix with rows `p_j` and `q=(q_j)`, then

`||q-PG^(-1)h||_2^2=tau=0`.                                           (3.5)

Therefore with `ell=G^(-1)h`, for every light input vector,

`eta:=sum q_j X_j = ell^T Z`,
`Z:=sum p_j X_j in u^perp`.                                            (3.6)

Condition on all other heavy **original** coordinates. They only create a fixed spectral translation and hence affine terms. The remaining random spectral vector is

`Y=sqrt(c)u X_i +(ell^T Z)u+Z + fixed shift`.                          (3.7)

The scalar `X_i` is independent of `Z` and retains density cap one.

### Projection cap for `Z`

Normalize `P` by `U=P G^(-1/2)`, so `U^TU=I_2`. The weighted affine-fiber Brascamp--Lieb theorem gives

`||p_(U^T X_L)||_infinity<=e`.

Since `Z=G^(1/2)U^T X_L`,

`boxed(||p_Z||_infinity <= e/sqrt(det G) <=5e).`                       (3.8)

This is where the original product law is aggregated **before** the quadratic pushforward.

### Null heavy pivot creates the exact 1+2 normal form

Choose an orthonormal spectral basis beginning with `u`. In the variables `(X_i,Z)`, the linear map into spectral space is

`L=[[sqrt(c), ell^T],[0,I_2]]`,

so the quadratic coefficient matrix is

`B=L^T Lambda L`,                                                     (3.9)

and

`|det B|=c |det Lambda|`.                                             (3.10)

The heavy physical pivot is precisely

`B_11=c u^T Lambda u=A_ii=0`.                                        (3.11)

Rotate only the already-joint two-dimensional variable `Z` so that the nonzero first-row cross vector of `B` points along the first coordinate. (It is nonzero because `B` is invertible.) Then

`B=[[0,b,0],[b,kappa,d],[0,d,e]]`.                                    (3.12)

Since `det B=-b^2e`,

`b!=0`, `e!=0`, and

`b^2|e|=c|det Lambda| >= c>3/10`.                                    (3.13)

Theorem 2.1 with `K=1` and `M<=5e` now gives, uniformly in the conditioned heavy coordinates,

`||p_(Q|X_(H minus {i}))||_infinity
 <=6(5e)^(2/3)(c|det Lambda|)^(-1/3)
 <6(5e)^(2/3)(10/3)^(1/3)
 =51.0450722631...`.                                                   (3.14)

Averaging the conditional laws proves the same unconditional bound.

### Theorem 3.1 — `QFORM-RANK3-NULLPIVOT-GRAPHPLANE-CLOSURE-v1`

In the exact-rank-three mixed branch of the fleet02/B13 trichotomy, take the heavy coordinate furnished by the preceding fleet01/B13 transverse-Pluecker argument. If its physical pivot is zero and the light Gram has regression residual `tau=0`, then for every independent cap-one product law

`boxed(||p_Q||_infinity <51.1).`                                      (3.15)

By the designated partner's exact bang-bang theorem, equivalently, for every interval `J` and every family of arbitrary measurable sets `E_j` with `|E_j|=1`,

`boxed(|{x in product E_j : x^T A x in J}| <=51.1 |J|)`               (3.16)

in this endpoint. No single-interval, centered, bounded-diameter, or fixed-fragment assumption is present.

## 4. What changed and what remains unpaid

Before this run the final exact-rank-three mixed branch was reduced to one heavy original scalar plus two uniformly elliptic transverse product banks, but the near-null heavy-pivot endpoint still lacked a source-safe joint smoothing argument.

This run closes the **exact zero heavy pivot + graph light plane** endpoint. The key new mechanism is neither an arbitrary-joint coarea estimate nor a conditional projected-density cap: first aggregate the light product law into its genuine two-dimensional transverse projection, keep the heavy original scalar independent of that entire pair, and then balance a linear-in-heavy `|v|^-1` estimate against a square-direction `|v|^-1/2` estimate. The determinant identity makes the local coefficients collapse to the invariant `c|det Lambda|`.

The first unpaid implication is now

`QFORM-RANK3-ONEHEAVY-LONGITUDINAL-RESIDUAL-v1`:

> In the same final mixed geometry, control the case `tau>0`, where the light longitudinal coordinate has a genuine residual component not determined by the transverse pair, while preserving the original product provenance; or produce a valid independent-product counterexample. Separately, a merely small nonzero heavy pivot cannot be handled by continuity of the exact-zero half-Riesz mechanism because that route is explicitly refuted in the live correction inbox.

Arbitrary additional spectral directions beyond exact rank three remain a separate full-target bridge. Therefore **FULL-QFORM remains OPEN**.

## 5. Integrity / changed-file review

This report contains only source-pinned mathematical material in the authorized private QFORM root. No credentials, scheduler IDs, personal data, paid/remote compute, email, public release, permission change, or cross-account authentication was used. Repository transport is not native learned-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
