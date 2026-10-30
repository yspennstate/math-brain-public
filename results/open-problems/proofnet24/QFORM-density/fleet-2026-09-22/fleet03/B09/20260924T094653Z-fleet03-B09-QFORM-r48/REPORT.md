SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-24T09:46:53Z.
attacking: grouped rank-two Schur crossing as the third genuine smoothing resource for the near-singular indefinite-pair survivor.

# fleet03/B09 r48 — scalar pivot + grouped rank-two Schur crossing

Programme: `QFORM-DENSITY-3EIG-20260922`
Role: Bilinear block mechanism / quantitative inequalities and rigorous computations
Run: `20260924T094653Z-fleet03-B09-QFORM-r48`
Status: **NEW SUPPORTING THEOREM PENDING INDEPENDENT REVIEW; NEAR-SINGULAR INDEFINITE-PAIR SUBBRANCH PAID; FULL QFORM OPEN; FULL-TARGET CONTINUITY OPEN**
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN. Every random variable below is an ORIGINAL-coordinate variable or a deterministic analytic projection used only inside an integral. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation independence assumption is introduced. Arbitrary same-bank quadratic curvature, arbitrary affine terms produced by outside conditioning, all signs, and arbitrary additional spectrum are retained.

## 1. Source state and the exact debt


The immediate B09 predecessor is

`yspennstate/math-open-problems@fd800c8358502f8e947f77f47e06ac3e5fae1742`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260924T091232Z-fleet03-B09-QFORM-r47/REPORT.md`.

That run proved a determinant-uniform definite-pair/star receiver and showed that a star alone cannot regularize an indefinite pair. Its exact remaining debt was:

`QFORM-NEAR-SINGULAR-INDEFINITE-PAIR-THIRD-RESOURCE-COMPILER-v1`:

retain a third genuine original-coordinate smoothing resource jointly with the logarithmic/near-singular pair, without deleting the small Schur square.

The present run changes the mechanism. Instead of paying the near-singular indefinite pair first, it pivots one literal scalar coordinate and aggregates TWO crossing directions in the Schur remainder before any physical right-pair selection.

Two completed inputs are used.

1. Grouped exact-rank crossing characteristic-function estimate:

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For independent banks with an exact rank-r cross block of nonzero singular values `s_1,...,s_r`, projected density caps `M_X,M_Y`, and arbitrary measurable same-bank phases, it gives

`|phi(t)| <= min(1, (pi/|t|)^(r/2) (M_X M_Y)^(1/2) (s_1...s_r)^(-1/2))`.

2. Fractional-potential Fourier representation from the completed rank-two affine report:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For a real random variable `R` with characteristic function `phi_R`,

`E|R-w|^(-1/2) <= (2pi)^(-1/2) int_R |t|^(-1/2)|phi_R(t)| dt`

whenever the right side is finite. Its proof uses the Gaussian representation of `|x|^(-1/2)` and Gaussian Fourier inversion, so it does not assume a density in advance.

The live corrections were read before use. In particular, nothing below uses law-uniform pointwise quadratic-phase decay, an arbitrary-joint coarea cap, a conditional density cap after rotating independent coordinates, deletion of a small quadratic term on unbounded supports, or a claim that one physical minor has universal scale.

## 2. New lemma: grouped rank-r crossing half potential

Let `Y` and `Z` be disjoint banks of ORIGINAL coordinates, hence independent. Let

`R = F(Y) + 2 Y^T C Z + G(Z)`

where `F,G` may be arbitrary real measurable functions (quadratic-affine functions in the QFORM application). Assume `C` has exact rank `r>=2`, with nonzero singular values `sigma_1,...,sigma_r`, and put

`Delta_r = product_(j=1)^r sigma_j`.

### Lemma 2.1 — `QFORM-GROUPED-CROSS-HALFRIESZ-v1`

For cap-one product input laws,

`sup_w E|R-w|^(-1/2)
 <= [4r/(r-1)] Delta_r^(-1/(2r)).`                    (2.1)

If one of the two banks consists of exactly `r` literal original coordinates, the coefficient improves to

`[4r/(r-1)] 2^(-1/4) Delta_r^(-1/(2r)).`              (2.2)

If both banks consist of exactly `r` literal original coordinates, it improves to

`[4r/(r-1)] 2^(-1/2) Delta_r^(-1/(2r)).`              (2.3)

For the critical case `r=2`, (2.2) is

`boxed:
 sup_w E|R-w|^(-1/2)
 <= 2^(11/4) Delta_2^(-1/4).`                         (2.4)

### Proof

Take an SVD `C=U Sigma V^T` in the deterministic coefficient space. This is NOT a rotation of the random variables and no independence is asserted for the projected coordinates. Push the complex measure `exp(itF(Y))dP_Y` to `U^T Y` and `exp(itG(Z))dP_Z` to `V^T Z`. Their complex densities `a_t,b_t` satisfy pointwise

`|a_t|<=p_(U^T Y)`, `|b_t|<=p_(V^T Z)`.

The product-projection theorem gives, in dimension r,

`||p_(U^T Y)||_infinity <= 2^(r/2)`,
`||p_(V^T Z)||_infinity <= 2^(r/2)`,

hence the completed crossing estimate yields

`|phi_R(t)|
 <= min(1,K |t|^(-r/2)),`
`K=(2pi)^(r/2) Delta_r^(-1/2)`.                       (2.5)

Now set `T=K^(2/r)=2pi Delta_r^(-1/r)`. Direct integration gives

`int_R |t|^(-1/2) min(1,K|t|^(-r/2)) dt
 = [4r/(r-1)] sqrt(T)`.                                 (2.6)

Multiplying by `(2pi)^(-1/2)` proves (2.1).

If, say, `Y` itself has exactly r literal original coordinates, its joint density is the product of r cap-one densities and is at most one. The orthogonal map `U^T` has Jacobian one, so its projected density cap is `M_Y=1` instead of `2^(r/2)`. The crossing estimate then has

`K=pi^(r/2) 2^(r/4) Delta_r^(-1/2)`,

which changes the coefficient in (2.1) by `2^(-1/4)` and proves (2.2). When both banks are literal r-tuples, both projected caps are one, giving an additional `2^(-1/4)` and (2.3). QED.

The point of (2.4) is that rank two is NOT sufficient for an `L^1` characteristic function and therefore does not by itself give bounded density, but it is exactly sufficient for a finite inverse-half potential. A literal square can spend that half potential without any square-root small-ball decoupling.

## 3. Main theorem: one scalar pivot plus a grouped rank-two Schur crossing

Choose one literal original coordinate `h`, a disjoint literal pair `I={i_1,i_2}`, and a disjoint original-coordinate bank `J`. All remaining original coordinates may be conditioned arbitrarily.

Write `a=A_hh` and assume `a!=0`. Let `R0` be the set of all coordinates other than h and let

`S = A_[R0,R0] - A_[R0,h] A_[h,R0]/a`                 (3.1)

be the exact scalar Schur complement. Put

`C = S[I,J]`                                                (3.2)

and assume `rank(C)=2`. Let

`Delta_2 = sigma_1(C) sigma_2(C)
         = sqrt(det(C C^T)) >0`.                           (3.3)

### Theorem 3.1 — `QFORM-SCALARPIVOT-GROUPED-RANK2-HALFRIESZ-v1`

For every admissible independent cap-one input law, with arbitrary same-side curvature, arbitrary outside couplings, arbitrary affine terms, arbitrary signs, and arbitrary additional spectrum, the FULL ambient quadratic form has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= 2^(11/4) |a|^(-1/2) Delta_2^(-1/4)
 = 2^(11/4) (|a|^2 Delta_2)^(-1/4).`                    (3.4)

Consequently every interval `E` obeys

`boxed:
 P{Q in E}
 <= 2^(11/4) |a|^(-1/2) Delta_2^(-1/4) |E|.`           (3.5)

No continuity conclusion is claimed by this proof.

### Proof

Condition on every original coordinate outside `{h} union I union J`. This preserves independence and the cap-one property of the retained original coordinates. All outside couplings become deterministic affine terms.

The conditional polynomial can be written

`Q = a X_h^2 + 2 X_h ell(Y,Z) + R_0(Y,Z)`                (3.6)

with `Y=X_I in R^2`, `Z=X_J`, and `ell` affine-linear. Complete ONLY the literal coordinate `X_h`:

`Q = a (X_h + ell/a)^2 + R(Y,Z)`,                        (3.7)

where the quadratic matrix of `R` is exactly the Schur complement `S`; in particular its Y-Z cross block is C.

For fixed `(Y,Z)`, the translated variable `X_h+ell/a` has a density bounded by one. The pushforward of a cap-one scalar density by `x -> a x^2` has the pointwise density majorant

`|a|^(-1/2)|u|^(-1/2)`                                   (3.8)

on the appropriate half-line (reflection handles `a<0`). Therefore, after averaging the conditional densities,

`p_Q(t)
 <= |a|^(-1/2) E|t-R(Y,Z)|^(-1/2)`                      (3.9)

for almost every t.

All terms of `R` internal to Y can be absorbed in `F(Y)` and all terms internal to Z in `G(Z)`; affine terms are also allowed. Since Y consists of exactly two literal original coordinates and the grouped cross block C has rank two, Lemma 2.1, equation (2.4), gives

`E|t-R|^(-1/2)
 <= 2^(11/4) Delta_2^(-1/4)`                             (3.10)

uniformly in t and in every outside conditioning value. Substitution into (3.9) proves (3.4). Averaging over the conditioned outside variables preserves the same cap. Integrating that density over an interval gives (3.5). QED.

This is the desired no-square-root-loss endpoint: the rank-two crossing is used at its natural half-Riesz exponent and the physical scalar square converts that directly to an `O(|E|)` bound.

## 4. What it does to the r47 near-singular indefinite-pair debt

Suppose a physical pair `(h,i_1)` is indefinite but approaches singularity. Completing the WHOLE pair first can create a logarithmic two-variable singularity and forces one to track a third resource through the remainder. Theorem 3.1 instead completes only h. The tiny Schur coefficient on `i_1` remains inside the arbitrary same-side function `F(Y)` and costs nothing. If a second literal row `i_2` and a disjoint original bank J make the Schur cross `S[{i_1,i_2},J]` rank two with controlled `Delta_2`, those two grouped crossing directions are the missing third resource.

Thus the analytic near-singular interpolation is paid on this subbranch with no reciprocal factor in

`det A[{h,i_1},{h,i_1}]`

and no reciprocal factor in the small scalar Schur coefficient.

The theorem does NOT assert that the bare three-large-eigenvalue hypothesis always forces such an h,I,J with `|a|^2 Delta_2` bounded below. That structural routing remains open.

## 5. Target-valid stress family: grouped crossing removes physical-minor diffusion

Let m be even and `0<epsilon<=1`. Use original coordinates

`h, y_1, y_2, z_1,...,z_m`

and the symmetric matrix defined by

`A_hh=1`,
`A_(h,y1)=1`,
`A_(y1,y1)=1-epsilon`,

and

`A_(y1,z_j)=2 sqrt(2/m)` for `j<=m/2`,
`A_(y2,z_j)=2 sqrt(2/m)` for `j>m/2`,

with all other entries zero.

The physical pair `(h,y_1)` is indefinite and

`det A[{h,y_1},{h,y_1}] = -epsilon ->0`.                 (5.1)

After the scalar h-pivot, the residual y1 coefficient is exactly `-epsilon`, but the Schur cross block from the literal pair `(y_1,y_2)` to the whole z-bank is

`C = [ first-half row ; second-half row ]`

with

`C C^T = 4 I_2`, hence `Delta_2=4`.                      (5.2)

Theorem 3.1 therefore gives, uniformly in BOTH m and epsilon,

`boxed:
 ||p_Q||_infinity
 <= 2^(11/4) 4^(-1/4)
 = 2^(9/4)
 = 4.756828460010884... .`                               (5.3)

This is a genuine target family. Let `z_A,z_B` be the normalized sums of the first and second z-halves. The active compression is

`[[1,1,0,0,0],
  [1,1-epsilon,0,2,0],
  [0,0,0,0,2],
  [0,2,0,0,0],
  [0,0,2,0,0]]`.                                        (5.4)

The `(y_2,z_B)` block has exact eigenvalues `+2,-2`. The remaining `(h,y_1,z_A)` block has operator norm at least two because it sends `z_A` to `2y_1`; hence it contributes another eigenvalue of modulus at least two. Therefore the full matrix has at least three eigenvalues of modulus at least one for every m and epsilon.

Yet every physical 2x2 minor of C is either zero or

`|det C[:,{r,s}]| = 8/m`.                                (5.5)

Selecting a single physical right pair before aggregation therefore gives a half-potential/density certificate deteriorating like `m^(1/4)`, whereas (5.3) stays fixed. The checker records the exact comparison for m=4,16,64,256.

Representative active spectra are:

* epsilon=1:
  `(-2.1642479385,-2,0.7728655578,2,2.3913823806)`;
* epsilon=0.1:
  `(-2,-1.7497337161,0.8030660401,2,2.8466676761)`;
* epsilon=0.001:
  `(-2,-1.7096745612,0.8060337953,2,2.9026407659)`;
* epsilon=1e-8:
  `(-2,-1.7092753634,0.8060634332,2,2.9032119202)`.

Numerics are only regression checks; target validity and the theorem are proved analytically above.

## 6. Designated fleet04/B09 partner applied to an actual inequality

The designated partner report is

`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`.

It proves that an actual literal invertible original-coordinate `3x3` cross block K, with arbitrary dense same-side curvature and arbitrary outside/affine terms, gives a CONTINUOUS density with

`||p_Q||_infinity <= 3 |det K|^(-1/3)`.                  (6.1)

Apply it to

`K=diag(5,3,1)`,
`A_*=[[0,K],[K,0]]`.

Then

`spectrum(A_*)={-5,-3,-1,1,3,5}`,
`det K=15`,

so the actual target-valid inequality is

`boxed:
 ||p_(X^T A_* X)||_infinity
 <= 3*15^(-1/3)
 = 1.2164403991146802... ,`                               (6.2)

and

`P{X^T A_* X in E} <= 1.2164403991146802... |E|`.        (6.3)

This partner branch has a continuous density.

## 7. Verification

`CHECK.py` tests:

* the r=2 constants in Lemma 2.1;
* exact Schur algebra for the target-valid family;
* `Delta_2=4` for m=4,16,64,256;
* at least three eigenvalues of modulus at least one for epsilon in `{1,.1,1e-3,1e-8}`;
* maximum physical `2x2` cross minor `8/m`;
* fixed grouped bound versus `m^(1/4)` physical-pair deterioration;
* the designated partner spectrum and constant.

All assertions passed. These computations verify algebra and finite stress instances; they are not substitutes for the analytic proof.

## 8. Exact remaining B09 implication

The new receiver closes the analytic `near-singular indefinite pair + genuine grouped rank-two Schur crossing` subbranch. The next B09 structural debt is

`QFORM-SCALARPIVOT-RANK2-CURRENCY-FORCING-OR-ROUTING-v1`:

under the three-large-eigenvalue hypothesis, after product-preserving reductions, either force a literal scalar pivot h and a literal two-row/disjoint-bank Schur crossing with

`|A_hh|^2 * [sigma_1(C)sigma_2(C)] >= c`

for a universal `c>0`, OR route every small-currency survivor to an already-paid three-hub/cross-volume/ridge/finite-core mechanism. Zero/tiny outer scalar pivots remain a separate boundary.

The full unrestricted QFORM conjecture remains OPEN. Full-target continuity remains OPEN. The theorem proved in this report gives essential boundedness only in its stated branch.

No task identity, cadence, enabled/paused state, email/push notification setting, permission, public-release setting, paid API/model/Codex call, or cross-account authentication state is changed by this work.
