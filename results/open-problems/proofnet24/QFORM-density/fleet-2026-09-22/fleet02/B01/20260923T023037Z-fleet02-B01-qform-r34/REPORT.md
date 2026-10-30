# QFORM B01 r34 — double-coloop rank-two volume is a two-hub packet

Status: **ESSENTIAL_STEP_APPLIED / supporting N3 estimates + target-valid stress / full QFORM OPEN**.

Run: `20260923T023037Z-fleet02-B01-qform-r34`.  
Assignment: fleet02/B01, Oscillatory replacement.  
Execution context: `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred; native learned-memory receiver use was not established).

## 1. Exact target and source pins

The only target is the full bounded-density quadratic-form conjecture: independent real `X_i` with densities at most one, real symmetric `A` with at least three eigenvalues of modulus at least one, and a universal finite bound for the essential supremum of the density of `X^T A X` (or a target-valid counterexample). No moment, support, Gaussian/log-concavity, spectral-basis independence, or post-rotation product assumption is used.

This run preserves the source-backed refutation of law-uniform pointwise scalar quadratic-phase decay. Every estimate below is distributional or frequency-averaged.

Inputs actually used at equation level:

1. Newest required Claude package, fixed source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, especially Theorem H (hub coordinates).
2. Own earlier two-slope distributional theorem, canonical `yspennstate/math-open-problems@c396b6e553f98ca1cd735ae10eb0e6ec24a96cc4`, `.../fleet02/B01/20260922T223353Z-fleet02-B01-qform-r29/REPORT.md`.
3. Sharp two-dimensional product-marginal transfer used in own r22, canonical `yspennstate/math-open-problems@08e91d2cd50db663646e7c25983c421ccaa78c7c`, `.../fleet02/B01/20260922T150052Z-fleet02-B01-qform-r22/REPORT.md`: for rank-two `T`, `||p_{TX}||_infinity <= 2/sqrt(det(TT^T))`.
4. Newest completed designated partner fleet03/B01 auto11, canonical mathematics `yspennstate/math-open-problems@f651c96b5c87b1b0df9a5701b9b47293d08dc94c` (main report creation commit `1d5a022d1461c7be5cd26b1bd7a8fc53abc7f458`), which proves the rank-two volume half-Riesz certificate quoted in Section 5 below.

## 2. New aggregate exact-null two-hub theorem

### Theorem `QFORM-AGGREGATE-NULL-TWO-HUB-v1`

Let `i != j` be ORIGINAL coordinates with

`A_ii=A_jj=A_ij=0`.

Let `K` be all remaining coordinates and form the `2 x |K|` physical coupling matrix

`B = [ A_{iK} ; A_{jK} ]`.

Assume `rank B=2`, and put

`Gamma = sqrt(det(B B^T)) > 0`.

Then for every independent input law with one-dimensional density caps at most one, with the entire outside quadratic form and every outside coupling retained,

`boxed: ||p_{X^T A X}||_infinity <= 2 sqrt(2) Gamma^(-1/2)`

or equivalently

`||p_Q||_infinity <= 2 sqrt(2) det(BB^T)^(-1/4)`.

No continuity claim is needed here.

### Proof

Write the two hub coordinates as `X,Y` and the outside vector as `Z`. Exact nullity of the physical `2 x 2` hub block gives

`Q = 2 X U + 2 Y V + R`,

where

`(U,V)^T = B Z`

and `R` is an arbitrary measurable function of `Z` coming from the entire outside quadratic form. Thus `(U,V,R)` is independent of `(X,Y)`. The sharp rank-two product-marginal theorem gives the joint slope density bound

`||p_(U,V)||_infinity <= 2/Gamma`.

The r29 two-slope theorem says that if `X,Y` have density caps one and the joint slope cap is `M`, then

`||p_(2XU+2YV+R)||_infinity <= 2 sqrt(M)`.

Substitution of `M=2/Gamma` proves the result.

This is a genuine many-coordinate improvement over r29's fixed `2 x 2` transverse minor certificate: the determinant is paid only after the full slope vectors have been aggregated.

## 3. Newest-Claude two-hub Fourier corollary, with arbitrary hub block

Theorem H of the required `e5f71d...` report gives a complementary endpoint in which the physical hub block need not be null.

### Corollary `QFORM-TWO-HUB-DIFFUSE-LEAF-v1`

Split ORIGINAL coordinates as `H union I union J`, with `|H|=2`. Suppose `A_II` is diagonal. Let

`C=A[I,H]`, `G=C^T C`,

assume `G` is invertible, and assume every leaf row `c_l` obeys

`c_l^T G^(-1)c_l <= 1/2`.

Then `A_HH,A_HJ,A_IJ,A_JJ` and all affine terms may be arbitrary, and

`boxed: |phi_Q(t)| <= min(1, 4 pi^2 det(G)^(-1/2)|t|^(-2))`,

`boxed: ||p_Q||_infinity <= 4 det(G)^(-1/4)`.

Here `phi_Q` is integrable, so this branch has a bounded continuous density.

Indeed, Theorem H with two hubs and Fresnel rank `r=0` gives the displayed `|t|^-2` bound. If `K=4 pi^2 det(G)^(-1/2)`, then

`int_R min(1,K/t^2) dt = 4 sqrt(K)`,

and Fourier inversion yields

`(2 pi)^(-1) 4 sqrt(K)=4 det(G)^(-1/4)`.

This is the required newest-report result applied to an actual density inequality, not a summary. It also shows why the r29 nonzero-mutual-edge obstruction does not forbid progress: the mechanism has changed. Hub integration can tolerate an arbitrary physical `A_HH` provided a diffuse diagonal leaf packet is available.

## 4. Exact strict-N3 double-coloop family

Fix `0 <= eps <= 1/2` and `m>=2`. In `R^2`, with standard basis `e1,e2`, define the `(1+2m) x 2` left frame `U` by rows

- `u0=sqrt(1-eps)e1`,
- `m` copies of `sqrt(eps/m)e1`,
- `m` copies of `m^(-1/2)e2`,

and the right frame `V` by rows

- `v0=sqrt(1-eps)e2`,
- `m` copies of `m^(-1/2)e1`,
- `m` copies of `sqrt(eps/m)e2`.

Then exactly

`U^T U = V^T V = I_2`.

Put `M=UV^T` and

`A_(m,eps) = [[0,M],[M^T,0]]`.

Because the two singular values of `M` are exactly one, the nonzero spectrum of `A_(m,eps)` is exactly

`{1,1,-1,-1}`.

Thus this family satisfies the full target spectral hypothesis with room to spare.

Every physical diagonal vanishes. The largest entry of `M` has squared magnitude `(1-eps)/m`, hence every physical `2 x 2` principal determinant has magnitude at most `(1-eps)/m`. Therefore for every fixed strict-N3 threshold `tau>0`, choosing `m>1/tau` makes every physical diagonal and every physical `2 x 2` principal determinant smaller than `tau` in modulus.

### The rank-two volume picture

For a rank-two SVD `M=U Sigma V^T`, squared two-minor sampling factors:

`det(M_{S,T})^2 / e_2(M^T M) = det(U_S)^2 det(V_T)^2`.

Since the columns of `U,V` are orthonormal, the natural row and column two-volume marginals are precisely the row leverages

`alpha_i=||u_i||^2`, `beta_j=||v_j||^2`.

Here `Z_2=e_2(M^T M)=1`, while

`alpha_0=beta_0=1-eps -> 1`.

So this is an exact target-valid **double-coloop** stress for the rank-two volume-marginal route.

### Uniform target density bound from the newest hub theorem

Take the two heavy physical coordinates `u0,v0` as `H`. Let `I` consist of the `m` right `e1` leaves and the `m` left `e2` leaves; let all other coordinates be `J`. Then

`A_II=0`,

`G=(1-eps) I_2`,

and every normalized leaf leverage equals `1/m<=1/2`.

Section 3 therefore gives, for **all** independent cap-one input laws,

`boxed: ||p_{X^T A_(m,eps) X}||_infinity <= 4(1-eps)^(-1/2) <= 4 sqrt(2).`

The original-coordinate product structure is untouched.

### Stronger bound from the aggregate exact-null gate

The same heavy pair has an exactly null physical `2 x 2` block. Its two full outside slope vectors have disjoint supports and squared norms both `1-eps`. Hence

`B B^T = (1-eps) I_2`, `Gamma=1-eps`.

Theorem 2 gives the stronger distributional estimate

`boxed: ||p_{X^T A_(m,eps) X}||_infinity <= 2 sqrt(2)(1-eps)^(-1/2) <= 4.`

At `eps=0` the rank-two volume marginals are exactly one on one row of each side, so any theorem requiring `h<1` is unavailable, while the two-hub density bound remains uniform.

## 5. Designated partner applied at equation level

The newest completed fleet03/B01 result states: for a rank-two cross block with `Z_2=e_2(M^T M)` and maximum constrained-side natural two-volume marginal `h<1`, put `q=max(1,2h)<2`; then

`H_(1/2)(R) := sup_s E |R-s|^(-1/2)`

obeys

`H_(1/2)(R) <= [4 sqrt(2e) q^(-1/4)/(2-q)] Z_2^(-1/8)`.

Apply it to the exact family above. In **either orientation** the constrained-side maximum is

`h=1-eps`,

and `Z_2=1`. For `0<eps<=1/2`, `q=2(1-eps)` and the partner certificate evaluates to

`H_(1/2)(Q_cross) <= 2 sqrt(2e) [2(1-eps)]^(-1/4) eps^(-1)`.

Thus that particular rank-two fractional-volume certificate deteriorates like `eps^(-1)` and becomes unavailable at the exact double-coloop endpoint `eps=0`. This is **not** a lower bound and does not assert that the true fractional potential diverges. It is a concrete certificate-level obstruction: the same target family has the uniform density bounds `<=4 sqrt(2)` from the required newest hub theorem and `<=4` from the aggregate null-hub theorem.

The correct move at simultaneous high row/column volume leverage is therefore not to keep paying `1/(1-h)`; it is to test for a genuine physical two-hub packet before inversion.

## 6. What changed in the proof map

This run pays a previously explicit endpoint of the rank-two high-leverage branch:

- **exact null physical hub pair, arbitrary outside curvature:** paid by `QFORM-AGGREGATE-NULL-TWO-HUB-v1` through the full slope Gram determinant;
- **arbitrary physical two-hub block, diffuse leaf packet with diagonal self-curvature:** paid by the newest Claude Theorem H, with `||p_Q||_infinity <=4 det(G)^(-1/4)`;
- **double-coloop rank-two volume family:** shown explicitly to be strict N3 and uniformly controlled even though the newest partner `h<1` fractional certificate degenerates in both orientations.

The phase-aligned fragmented-support refutation of scalar law-uniform pointwise Fresnel decay remains untouched; both successful mechanisms average before inversion.

## 7. First unpaid implication

The remaining local interface exposed here is

`QFORM-DOUBLE-HUB-NONDIAGONAL-LEAF-v1`:

from strict N3 and a rank-two cross-bank state with row and column two-volume marginals both close to one, quantitatively route to either

1. a two-physical-hub packet whose leaf curvature can be handled **without** assuming `A_II` diagonal and without requiring the physical hub block to be exactly zero, or
2. an already-paid volume/ridge/mixed-hub/physical-block branch.

Equivalently, one must bridge the rectangle between the exact-null aggregate slope theorem (arbitrary outside curvature) and Theorem H (arbitrary hub block but diagonal/low-rank leaf curvature). A naive continuation of either hypothesis is not justified.

This is a supporting step only. N3 and the unrestricted conjecture remain **OPEN / NOT PROVED / NOT DISPROVED**, and no full-proof candidate with two independent end-to-end reviews exists.
