SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T01:48:09Z.
attacking: test the double-wedge-diffuse -> third-volume splice against concentrated tail directions, then repair it by a volume-or-tail-hub dichotomy.

# account02/B06 — concentrated-tail adversary and repaired volume-or-tail-hub gate

Programme: QFORM-DENSITY-3EIG-20260922. Run: `b06-20260923T014809Z-5f81b9d02dd3`. Status: `CANDIDATE_REFUTED + ESSENTIAL_STEP_APPLIED`; full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Sources actually used

Fresh starting control: `yspennstate/math-research-brain@ee0f2c9ba46b94775d510902fb5941a829289bfc`, OWNER CONTROL revision `2026-09-22.15`. Required current continuation and correction boundary were read there.

Designated partner actually applied: account03/B06, run `20260923T004812Z-account03-B06-qform-r23`, source snapshot `yspennstate/math-open-problems@0c9a2e6a85863dc639c9551c09605ceafb5afb14`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T004812Z-account03-B06-qform-r23/REPORT.md`, blob `ec3a6f691bec67f77dbeedaa4a09bbe04742f904`. Its theorem `QFORM-BICOLOOP-STAR-AGGREGATION-SQUEEZE-v1` says that, in the inherited bicolooop chamber, either a determinant star pays the branch or the two exterior top-two singular directions are simultaneously diffuse. At its tau=1/16 collar the inherited nonanchor top-two leverage is <0.099 on both physical sides, while the nonzero higher-rank tail must still be paid.

Newest-Claude input actually applied: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` in `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. In particular, Theorem D uses third-volume sampling row marginals, and the physical-coordinate localized theorem gives `||p_Q||_infinity <= 6 sqrt(pi)/c` when an original 3x3 principal block has all eigenvalues of modulus at least c.

Current volume-stability receiver: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/`. For an original-coordinate cross block M and 1<=q<3/2, if every third-volume row marginal alpha_i<=q/2, then

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] E3(M)^(-1/6)`,

with arbitrary self blocks, outside couplings and affine terms retained.

I also consumed the newer exact-coloop interpolation `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1` at `yspennstate/math-open-problems@80f95e245b7f3418e8da36173ac4eb9d81fb58a7:proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260923T003846Z/REPORT.md`; therefore I do not duplicate the already-paid near-null exact-coloop branch.

## 2. False splice refuted

A tempting next statement after the partner's r23 squeeze is:

> once the two inherited top singular directions are diffuse off the anchors and a nonzero third singular direction is present, the third-volume marginal gate is automatically diffuse enough for Theorem D/D'.

This is false, even for an exact target matrix and even after conditioning away the heavy left anchor.

Take m=32 and define three orthonormal vectors in R^34, indexed by anchor 0, core coordinates 1,...,32 and tail coordinate 33:

`u1(0)=sqrt(49/50)`, `u1(k)=sigma_k/40` for 1<=k<=32, `u1(33)=0`,

where sixteen sigma_k are +1 and sixteen are -1;

`u2(0)=0`, `u2(k)=1/sqrt(32)` for 1<=k<=32, `u2(33)=0`;

`u3=e_33`.

Let V=U and

`H=U diag(1,1,1/100) V^T`.

Then H has singular values exactly 1,1,1/100. The anchor top-two leverage is

`L_0=49/50 > 6221/6450`,

and the partner's normalized exterior direction is exactly `p_k=u2(k)`, so

`max p_k^2=1/32<1/16`; the same holds on the right. Also

`h3/h2=1/100<3/200`, `h1 h2=1>(4/5)*1^2`.

Thus this is an exact realization of the partner's strongest double-diffuse tau=1/16 geometry (with gamma=1), not a largest-minor surrogate.

Now condition on the left anchor coordinate and retain every right coordinate. The active cross block is `M=H[{1,...,33},:]`. Its singular values are exactly

`1, sqrt(1/50), 1/100`.

The two leading left singular vectors are the normalized constant and sign vectors on the 32 core coordinates, so every core row has active top-two leverage

`1/32+1/32=1/16`.

But the third left singular vector is the isolated physical tail coordinate e_33. Since M has rank exactly three, third-volume sampling has only the three singular directions, and its row marginal is the range-projection diagonal:

`alpha_i=u1'(i)^2+u2'(i)^2+u3'(i)^2`.

Consequently

`alpha_k=1/16` on every core row, while `alpha_33=1`.

For q=4/3 the receiver requires alpha_i<=2/3, so the gate fails maximally at the tail coordinate even though the active top-two plane is perfectly diffuse. The third volume is positive and exact:

`E3(M^T M)=1*(1/50)*(1/10000)=1/500000`.

The obstruction is therefore not lack of aggregate curvature: it is concentration of the *new* curvature direction.

## 3. Repaired statement: volume-or-tail-hub

Let an arbitrary original-coordinate cross block M have singular values s_m and left singular vectors u_m. Assume E3(M)>0. The third-volume inclusion probabilities are

`p_m = s_m^2 e2({s_l^2:l!=m}) / E3(M)`,

so `0<=p_m<=1` and `sum_m p_m=3`. The row marginal is exactly

`alpha_i = sum_m p_m u_m(i)^2`.

Fix 1<=q<3/2 and suppose the leading-two physical leverage obeys

`u1(i)^2+u2(i)^2 <= ell` for every constrained row i.

Define the weighted tail leverage

`T_i=sum_{m>=3} p_m u_m(i)^2`.

Then

`alpha_i <= ell + T_i`.

Therefore exactly one of the following holds:

1. `T_i <= q/2-ell` for every row. Then every alpha_i<=q/2 and the current volume-stability theorem applies directly:

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] E3(M)^(-1/6)`.

2. Some physical row i satisfies

`T_i > q/2-ell`.

Since every p_m<=1, this also forces the ordinary tail-range leverage

`sum_{m>=3} u_m(i)^2 > q/2-ell`.

This is `QFORM-DOUBLE-DIFFUSE-VOLUME-OR-TAIL-HUB-v1`. It is a genuine repair of the false splice: failure of the third-volume receiver cannot remain amorphous once the leading two directions are diffuse; it produces a quantitatively heavy *tail* physical coordinate.

At q=4/3 and ell=1/16, a gate failure forces tail-range leverage >29/48. The adversary above saturates the qualitative mechanism with tail leverage 1.

For the partner r23 survivor this identifies the next necessary interface. One still has to transfer its inherited exterior collar to an actual conditioned cross block without silently re-orthonormalizing away a concentrated direction; after such a transfer, either the volume theorem pays the branch or a >constant tail hub is forced. The explicit family proves that the tail-hub alternative is real and cannot be deleted from an exhaustive proof.

## 4. It is not a QFORM counterexample

Embed H into the exact symmetric target

`A = [1] direct_sum [[0,H],[H^T,0]]`.

Its spectrum contains

`1, +1,-1,+1,-1,+1/100,-1/100`

(and zeros), so it satisfies the target spectral hypothesis strongly. The original scalar together with the left and right anchor coordinates gives the physical principal block

`diag(1, [[0,49/50],[49/50,0]])`,

whose eigenvalue magnitudes are `1,49/50,49/50`. Hence the pinned Claude localized theorem gives, for every independent cap-one input law,

`||p_Q||_infinity <= 6 sqrt(pi)/(49/50) < 10.852`.

Thus the construction refutes only the proposed diffuse-top-two -> diffuse-third-volume reduction, not the conjecture.

## 5. Exact check

`CHECK.py` and `CHECK_OUTPUT.txt` in this run verify all rational thresholds and the localized bound. Executed checker SHA-256: `49d8c344d5273bf2fd348517710ec1c192fd5f108ae65db091ec91b41caacc4c`. Output SHA-256: `3d5e3d87236448769c34c08869dd5d09d5413b0b5bdecab3feff596037c141d9`. Status: PASS.

## 6. First unpaid implication

`QFORM-TAIL-HUB-RECEIVER-v1`: starting from a product-preserving conditioned block for which the partner's double-diffuse top-two collar has been transferred, pay the alternative physical row with large tail-range leverage without discarding the leading rank-two curvature or arbitrary same-side quadratic terms. Candidate receivers are the mixed-Fresnel hub theorem or a new scalar/dependent-projection curved kernel. Any proof that simply asserts the tail is diffuse is now source-validly false.

Independent-review status: none requested or claimed for this supporting reduction. Full QFORM remains open.
