SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T08:21:15Z.
attacking: integrated Fourier estimate — resolve the four-anchor residual-E2 hub forced by failure of the account02/B02 mixed edge/E2 Fourier compiler, and splice its two-hub part into a genuine L1 characteristic-function bound.

# account01/B02 r27 — four-anchor E2 hub trichotomy and two-hub L1 splice

## Status

`ESSENTIAL_STEP_APPLIED / SUPPORTING_ANALYTIC_THEOREM / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains open. This run attacks the first failure branch of the completed account02/B02 theorem `QFORM-EDGE-E2-CROSSDISJOINT-SHARP-HY-L1-v1`. That theorem gives a genuine unweighted L1 characteristic-function estimate unless two determinant-weighted residual two-minor laws are almost cross-intersecting. Its exact failure certificate forces more than 7/8 of the residual second exterior volume through one fixed two-row/two-column physical compound hub.

The new contribution is an exact quantitative resolution of that four-anchor hub into three smaller physical resources. Two of the three resources are literal two-physical-hub wedges and can be fed directly into the completed two-hub Fourier smoother (with its stated leaf-curvature certificate), giving a new genuine L1_t bound. If both two-hub wedges are small, one single physical row-column anchor carries a fixed fraction of the residual E2 mass, and an exact 2x2 Schur identity turns this into either an edge-times-Schur-Frobenius resource or a two-star product. In the live D' edge/E2 branch this nested resource has universal scale relative to the third exterior volume.

No pointwise law-uniform oscillatory decay, arbitrary-joint coarea, post-rotation independence, matrix-perturbation continuity, fixed-good-minor inverse, moment bound, support regularity, log-concavity, or Gaussian assumption is used.

Continuity is proved on the explicit L1 two-hub branches below. It is not claimed for the full target.

## 1. Exact partner input actually applied

The designated completed partner source is account02/B02:

- brain handoff commit `cd7b64e5a13be8274370fd9b16814bb2666ea93c`;
- canonical mathematics `yspennstate/math-open-problems@5d35b697d95d20e66fd72c96a5ea2dffa1201958`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/account02-B02-20260923T071011Z-3508bbe2/REPORT.md`.

Write an actual physical cross block as

`B = [[a,r^T],[c,N]]`, `a != 0`,

and put

`S = N - c r^T/a`,
`J = a^2 E2(S)`,
`E = E2(N)`.

Let `nu_S,nu_N` be the normalized squared two-minor laws and

`delta_r=P(R_S cap R_N=empty)`,
`delta_c=P(T_S cap T_N=empty)`.

The partner theorem proves, if either disjointness probability is positive,

`integral_R |phi_Q(t)|dt <= 10 pi e^(4/5) (delta J E)^(-1/10)`,

and hence

`||p_Q||infinity <= 5 e^(4/5)(delta J E)^(-1/10)`.

More importantly for the present failure branch, for every `eta>0`, if `delta_r<eta` there is a physical residual row pair `H` such that

`E2(N[H^c,*]) < eta E`,

and if `delta_c<eta` there is a residual column pair `L` such that

`E2(N[*,L^c]) < eta E`.

Thus under the canonical squared-two-minor law `mu_N`,

`P(R cap H != empty, T cap L != empty) > 1-2 eta`.                 (1.1)

This is the partner result used at the first essential inequality below.

I also use the completed two-hub Fourier theorem from account02/B09 and its vertex-cover puncture corollary from account01/B09:

- base theorem `QFORM-TWOHUB-PLUCKER-SMOOTHING-v1`, canonical source `yspennstate/math-open-problems@bc348aa1a3631b0a0a3a9939cbb6b023578e9abc`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T064043Z-account02-B09-QFORM-r13/REPORT.md`;
- puncture theorem `QFORM-TWOHUB-VERTEXCOVER-PUNCTURE-v1`, canonical source `yspennstate/math-open-problems@c7dc3ed482691c13923c99a820877bfe07d0dfc6`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260923T074931Z-account01-B09-QFORM-auto12/REPORT.md`.

For two literal hubs with leaf-coupling matrix `C`, `G=C^T C`, and a leaf-curvature vertex cover with certificate

`zeta = 1 - Theta - 2 q > 0`,

that theorem gives the genuine L1 estimate

`integral |phi_Q| <= 4 pi sqrt(e) [zeta det G]^(-1/4)`              (1.2)

and density bound

`||p_Q||infinity <= 2 sqrt(e)[zeta det G]^(-1/4)`.                (1.3)

All physical hub curvature and all outside couplings are retained.

## 2. New deterministic theorem — `QFORM-FOURANCHOR-E2-HUB-TRICHOTOMY-v1`

Let `N` be any real matrix with

`E=E2(N)>0`.

Let `mu` be its normalized determinant-squared two-minor law:

`mu(R,T)=det N[R,T]^2/E`, `|R|=|T|=2`.

Fix row and column pairs

`H={h1,h2}`, `L={l1,l2}`

such that

`P_mu(R cap H != empty, T cap L != empty) > 1-2 eta`.             (2.1)

Define the two literal hub-wedge masses

`D_H = sum_T det N[H,T]^2
     = det(N[H,*] N[H,*]^T)`,                                    (2.2)

`D_L = sum_R det N[R,L]^2
     = det(N[*,L]^T N[*,L])`.                                    (2.3)

Fix `theta>0` with

`1-2 eta-2 theta >0`.                                             (2.4)

Then at least one of the following holds:

(A) `D_H >= theta E`;

(B) `D_L >= theta E`;

(C) there are `h in H`, `l in L` such that the joint incident two-volume

`K_hl := sum_(r!=h,c!=l) det N[{h,r},{l,c}]^2`                    (2.5)

satisfies

`boxed{ K_hl > [(1-2 eta-2 theta)/4] E. }`                        (2.6)

### Proof

If (A) or (B) holds there is nothing to prove. Assume both fail. Under `mu`,

`P(R=H)=D_H/E < theta`,
`P(T=L)=D_L/E < theta`.                                           (2.7)

Subtract these two exceptional events from (2.1):

`P(R cap H != empty, T cap L != empty, R!=H, T!=L)
 >1-2 eta-2 theta`.                                               (2.8)

Because `R,T,H,L` all have size two, on the event in (2.8) the intersections `R cap H` and `T cap L` are singletons. Hence the event is partitioned by the four choices `(h,l) in H x L`. One choice therefore has probability greater than `(1-2 eta-2 theta)/4`. Its mass is bounded above by the full incident mass `K_hl/E`, proving (2.6). QED.

### Canonical constants

Use the partner's natural failure scale

`eta=1/16`

and choose

`theta=1/8`.

Then either

`D_H >= E/8`,                                                     (2.9)

or

`D_L >= E/8`,                                                     (2.10)

or some physical `(h,l)` satisfies

`boxed{ K_hl > 5E/32. }`                                         (2.11)

Thus the partner's `>7/8` four-anchor compound hub has been sharpened into an exhaustive physical two-hub-or-single-anchor trichotomy.

## 3. New exact nested-anchor normal form

Take the third branch and reindex its selected row `h` and column `l` first:

`N = [[b,p^T],[q,D]]`.                                            (3.1)

Then directly from the 2x2 determinant formula,

`boxed{ K_hl = || b D - q p^T ||_F^2. }`                          (3.2)

Therefore:

- if `b!=0`, with `T=D-q p^T/b`,

  `boxed{ K_hl = b^2 ||T||_F^2; }`                               (3.3)

- if `b=0`,

  `boxed{ K_hl = ||q||_2^2 ||p||_2^2. }`                         (3.4)

This identity is exact in the original physical coordinates. It neither rotates random variables nor discards the rest of the matrix. Combining (2.11) with (3.3)-(3.4) gives the exact nested endpoint

`b!=0:  b^2 ||D-q p^T/b||_F^2 > 5E/32`,                          (3.5)

`b=0:   ||q||^2 ||p||^2 > 5E/32`.                                (3.6)

So failure of the partner L1 disjointness criterion cannot leave an amorphous four-coordinate hub: unless a literal two-hub wedge already carries `E/8`, it forces either a physical edge times Schur-Frobenius packet or a physical two-star product at fixed scale.

## 4. Genuine integrated-Fourier payment of the two-hub alternatives

Suppose (A) holds. Regard the two original coordinates in `H` as literal physical hubs and the residual column-coordinate bank as leaves. By symmetry of the full quadratic coefficient matrix, the leaf-to-hub coupling matrix is

`C=N[H,*]^T`,

so from (2.2)

`det(C^T C)=D_H`.                                                  (4.1)

Let `K` be any vertex cover of the exact off-diagonal curvature graph inside that physical leaf bank. Define the leverage quantities of the puncture theorem

`p_j=c_j^T (C^T C)^(-1)c_j`,
`Theta=sum_(j in K) p_j`,
`q=max_(j notin K) p_j`,
`zeta=1-Theta-2q`.                                                 (4.2)

If `zeta>0`, account01/B09's completed puncture theorem, whose underlying estimate is the account02/B09 Fourier theorem, applies to the full quadratic form after conditioning only disjoint original coordinates. By (1.2) and `D_H>=theta E`,

`boxed{
 integral_R |phi_Q(t)|dt
 <= 4 pi sqrt(e) (zeta D_H)^(-1/4)
 <= 4 pi sqrt(e) (zeta theta E)^(-1/4).
}`                                                                  (4.3)

Consequently

`boxed{
 ||p_Q||infinity
 <=2 sqrt(e)(zeta theta E)^(-1/4).
}`                                                                  (4.4)

The density on this branch is continuous and vanishes at infinity.

The same statement holds in alternative (B), using the two physical coordinates in `L` as hubs and transposing the residual cross block.

At the canonical `theta=1/8`,

`integral |phi_Q| <=4 pi sqrt(e) (8/(zeta E))^(1/4),`              (4.5)

`||p_Q||infinity <=2 sqrt(e) (8/(zeta E))^(1/4).`                 (4.6)

This is a new genuine unweighted integrated-Fourier exit from the account02/B02 four-anchor failure branch. The only extra hypothesis is precisely the already-proved B09 leaf-curvature certificate; no new law regularity is inserted.

## 5. Application to the live D' edge/E2 collar

In the designated partner's Section 6, after both third-volume marginal gates fail and the joint-star compiler lands on its edge/E2 side, one has

`a^2 E > Z3/12`,                                                   (5.1)

where `Z3=E3(B)` is the actual third exterior volume of the original physical cross block.

If either cross-disjointness parameter is at least `1/16`, the partner theorem itself gives the direct L1 estimate and this run is not needed. Suppose instead

`delta_r<1/16`, `delta_c<1/16`.                                   (5.2)

Apply Sections 2-3 with `eta=1/16`, `theta=1/8`.

### 5.1 Two-hub wedge exit

If `D_H>=E/8` (or symmetrically `D_L>=E/8`), then

`D_H > Z3/(96 a^2)`.                                              (5.3)

Whenever the corresponding B09 puncture certificate `zeta>0` holds, (4.3) becomes

`boxed{
 integral |phi_Q|
 < 4 pi sqrt(e) [zeta Z3/(96a^2)]^(-1/4).
}`                                                                  (5.4)

This is an actual equation-level splice of the designated account02/B02 edge/E2 result into a second completed Fourier compiler.

### 5.2 Nested physical resource when both hub wedges are small

Otherwise some `(h,l)` has `K_hl>5E/32`. Combining with (5.1) eliminates the intermediate `E` completely:

if `b!=0`,

`boxed{
 a^2 b^2 ||D-q p^T/b||_F^2 > 5 Z3/384;
}`                                                                  (5.5)

if `b=0`,

`boxed{
 a^2 ||q||_2^2 ||p||_2^2 > 5 Z3/384.
}`                                                                  (5.6)

These are homogeneous third-order physical resources: both sides scale as the sixth power of the quadratic coefficient scale. In particular there is no reciprocal selected 2x2 minor and no dimension factor.

Equations (5.5)-(5.6) are the first unpaid subbranches after this run. They are much narrower than the preceding four-anchor compound hub: (5.5) is two actual physical edges followed by one aggregate Schur-Frobenius direction, while (5.6) is one outer physical edge followed by two transverse physical stars with a zero inner edge.

## 6. Why this does not silently use a false perturbation or Schur identification

The outer designated-partner theorem deliberately keeps two different residual matrices: `S=N-cr^T/a` in `J=a^2E2(S)` and the raw residual cross block `N` in `E=E2(N)`. The present four-anchor argument is applied only to the partner's exact failure certificate for the raw `N`; it never identifies `E2(N)` with a TRUE symmetric pair-Schur residual.

Likewise, (3.2) is merely the determinant identity for the raw physical matrix `N`. No assertion is made that replacing `N` by its inner Schur complement is a small random perturbation. The Schur-Frobenius quantity in (3.5) is only a deterministic resource to be consumed by a future source-valid transducer.

The L1 payment in Section 4 acts directly on the full original quadratic form through the completed two-hub theorem and retains the entire physical hub core and outside couplings. Thus it is unaffected by the current correction `QFORM-UNIFORM-MATRIX-PERTURBATION-CONTINUITY-FALSE-v1`.

## 7. First unpaid implication

The first unpaid interface is now

`QFORM-NESTED-EDGE-FROBENIUS-OR-OPPOSITE-TWOSTAR-L1-v1`:

> Starting from the exact actual-coordinate resources (5.5) or (5.6), produce a direct integrated-Fourier or linear small-ball transducer that retains all same-bank curvature. In the `b!=0` branch the target currency is two physical edges times one Schur-Frobenius packet. In the `b=0` branch it is one outer edge times two opposite-bank stars. Alternatively, show that the failure of such a transducer forces one of the already-paid D', D5, ridge, grouped-square, grouped-bilinear, two-hub, or finite-core exits.

The two-hub wedge subbranch still has the B09 cover-failure collar when no vertex cover satisfies `zeta>0`; that is already identified by B09 as a cross-volume/ridge/dense-curvature routing problem rather than an integrated-Fourier failure.

## 8. Global status

No target-valid counterexample to the stronger global criterion

`integral_R |E exp(it X^T A X)|dt <= C`

was found. It remains `OPEN_NOT_REFUTED`.

The full universal density conjecture remains OPEN. The full continuous-density statement remains OPEN. Continuity is proved on the new Section 4 L1 branches.

Independent end-to-end review of the new trichotomy and splice is not yet claimed.

MODEL: GPT-5.6 Sol. THINKING LEVEL: UNKNOWN / not exposed. Provider reasoning-token and provider-thinking-time counters: NOT_EXPOSED.
