# fleet01/B06 r48 — degenerate two-hub curved receivers

**Run:** `20260924T060138Z-fleet01-B06-QFORM-r48`  
**Assignment:** curved fiber integration  
**Status:** new supporting analytic theorems; full unrestricted QFORM remains OPEN; global continuity remains OPEN  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval/publication occurred, but no native learned-memory receiver use was verified)

## 0. Target, corrections, and source pins

The target is unchanged: for every `n`, independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has an essentially bounded density by one universal finite constant, or give a valid counterexample. No support, moment, log-concavity, sign, compactness, connectedness, or diagonal-basis assumption is introduced.

Fresh control was read from `yspennstate/math-research-brain` main, including `AGENTS.md`, `scheduled_tasks/README.md`, `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/fleet01/B06.json`. The live state still marks the full theorem and full continuity conclusion OPEN. The pointwise van-der-Corput shortcut, arbitrary-joint coarea shortcut, post-rotation independence, and unrestricted fiber-sup mechanism are not used.

Immediate predecessor: fleet01/B06 r47, canonical mathematics `yspennstate/math-open-problems@f9c285a20c529904887122c7def9ca3a2afb484b`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260924T043511Z-fleet01-B06-QFORM-r47/REPORT.md`. Its concentrated conditional Pluecker-pair branch yields a literal two-hub carrier-plane lower bound `||r_h wedge r_j||^2>7/64`, but did not yet pay the cases where the literal physical pair is singular or zero.

Designated partner result actually applied below: fleet02/B06, theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical source `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. In dimension `k`, if `V` has orthonormal columns and `Z` has independent cap-one coordinates, the density of `V^T Z` is at most `e^{k/2}`. Consequently, for a rank-`k` linear map `M` with nonzero singular values `sigma_1,...,sigma_k`, the density of `MZ+a` is at most `e^{k/2}/prod sigma_i`. This is a product-weighted affine-fiber theorem, not an independence-after-rotation claim.

A second current partner endpoint is fleet02/B06 r13, canonical mathematics `yspennstate/math-open-problems@bc7c60dbcb335ba3b18748816a62b026dc8ef4ab`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/fleet02-B06-20260924T052646Z-auto11-r13/REPORT.md`. Its invertible-pair branch gives, in the stated two-hub/one-tail-cross normal form, `||p_Q||_infinity <=15.0823111681 [sigma_min(P_h)||R_h||_2]^(-1/4)` for an indefinite physical pair. The new results below are complementary exact-degeneracy receivers; they do not replace that near-singular invertible estimate.

## 1. The missing curved endpoint

The basic obstruction is a literal pair of original coordinates whose physical `2x2` quadratic block is singular. Throwing away the pair loses curvature, while rotating the whole ambient input destroys independence. The correct operation is local: rotate only the two-dimensional geometric parametrization, but keep the original product factors in the integral.

### Theorem 1 — `QFORM-PARABOLIC-PRODUCT-FIBER-v1`

Let `X,Y` be independent real variables with probability densities `f,g<=1`. Let `v,w` be an orthonormal basis of `R^2`, let `theta !=0`, `beta !=0`, and consider

`F(X,Y)=theta (v dot (X,Y))^2 + 2 beta (w dot (X,Y)) + c`.

Then `F` has an essentially bounded density and

`||p_F||_infinity <= 2^(7/4) / sqrt(|theta beta|).`        (1.1)

The same bound holds after arbitrary translations of the two original input coordinates.

#### Proof

Write `(u,z)` for coordinates in the orthonormal basis `(v,w)`. If `v=(c0,s0)` and `w=(-s0,c0)`, then

`x=c0 u-s0 z`, `y=s0 u+c0 z`.

For fixed level `t`, because the phase is affine in `z`,

`z(u)=(t-c-theta u^2)/(2 beta)`.

The change of variables `(u,z)->(u,F)` has Jacobian `2|beta|`. Therefore, for almost every `t`,

`p_F(t)= [1/(2|beta|)] int_R f(x(u))g(y(u)) du`.          (1.2)

This is the exact curved fiber; no fiber supremum is taken.

Differentiate along the parabola:

`z'(u)=-theta u/beta`,
`x'(u)=c0+s0 theta u/beta`,
`y'(u)=s0-c0 theta u/beta`.

Hence

`|x'(u)|^2+|y'(u)|^2 = 1+(theta u/beta)^2`.               (1.3)

Fix `U>0`. On `|u|<=U`, the integrand is at most one, contributing at most `2U`.

On `|u|>U`, partition the parameter line into `E_x={|x'|>=|y'|}` and `E_y={|y'|>|x'|}`. On the selected set,

`max(|x'|,|y'|) >= |theta|U/(sqrt(2)|beta|)=:L`.          (1.4)

On `E_x`, use `g<=1` and the one-dimensional area formula. The map `u->x(u)` is quadratic (or linear in the degenerate orientation), hence has multiplicity at most two. Therefore

`int_{E_x cap {|u|>U}} f(x(u))g(y(u))du
 <= L^(-1) int f(x(u))|x'(u)|du
 <= 2/L`.

The same argument on `E_y` gives another `2/L`. Consequently

`int f(x(u))g(y(u))du
 <= 2U + 4sqrt(2)|beta|/(|theta|U)`.                      (1.5)

Choose `U^2=2sqrt(2)|beta|/|theta|`. Then the right side is

`2^(11/4) sqrt(|beta|/|theta|)`.

Substitution into (1.2) proves (1.1). Every translation simply replaces `f(x),g(y)` by translated cap-one densities, so the estimate is translation-uniform. QED.

### Why this is the desired weighted replacement

The proof retains the entire parabola. The central part is paid by its parameter length; the tails are paid by whichever **original coordinate map** has the larger tangent derivative. Product structure enters through `f<=1`, `g<=1`, and `int f=int g=1`. This is precisely the operation that is unavailable for an arbitrary joint cap-one density concentrated in a thin curved tube.

## 2. Random transverse slope: rank-one physical pair plus arbitrary same-bank curvature

The preceding theorem can be averaged against the true product law of all remaining coordinates.

### Theorem 2 — `QFORM-RANK1-PHYSICAL-PAIR-TRANSVERSE-SLOPE-v1`

Let `H=(X_1,X_2)` be two original independent cap-one coordinates and let `Z` be a disjoint bank of original independent cap-one coordinates. Let

`Q = H^T B H + 2 H^T M Z + 2 a^T H + G(Z)`,             (2.1)

where `B` is real symmetric of rank one, its nonzero eigenvalue is `theta!=0`, `M` is arbitrary, and `G` is an arbitrary measurable function for which (2.1) is defined (in the QFORM application `G` is the complete remaining quadratic-plus-affine term).

Let `w` be a unit vector spanning `ker B`, and put

`n=M^T w`.

If `n!=0`, then `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity
 <= 2^(13/4) e^(1/4) (|theta| ||n||_2)^(-1/2)`           (2.2)

with numerical front constant

`2^(13/4)e^(1/4)=12.215777290955165...`.

No restriction is imposed on the same-bank function `G`; in particular it may contain arbitrary quadratic curvature and may be strongly dependent on the scalar `n dot Z`.

#### Proof

Diagonalize only the deterministic `2x2` matrix:

`B=theta vv^T`, `w perp v`.

Condition on `Z=z`. Decompose the conditional linear coefficient as

`Mz+a = alpha(z)v + beta(z)w`,
`beta(z)=n dot z + beta_0`.

Complete the square only in the `v` direction. This translates the two original coordinates by a deterministic vector depending on `z`; conditionally they remain independent, and each translated marginal still has density cap one. All terms created by the completion are absorbed into the level shift and into `G(z)`. Therefore Theorem 1 applies conditionally:

`||p_{Q|Z=z}||_infinity
 <= 2^(7/4)|theta|^(-1/2)|beta(z)|^(-1/2)`.              (2.3)

Now apply the designated fleet02/B06 weighted affine-fiber theorem at `k=1` to the normalized direction `n/||n||`. It gives the actual inequality

`||p_{n dot Z + beta_0}||_infinity <= sqrt(e)/||n||`.     (2.4)

For any real random variable `T` whose density is bounded by `L`, the bathtub/rearrangement bound gives

`E|T|^(-1/2)
 <= L int_{-1/(2L)}^{1/(2L)} |t|^(-1/2)dt
 = 2sqrt(2L)`.                                           (2.5)

Apply (2.5) with `L=sqrt(e)/||n||` and average (2.3):

`||p_Q||_infinity
 <=2^(7/4)|theta|^(-1/2) * 2sqrt(2)e^(1/4)||n||^(-1/2)`,

which is exactly (2.2). QED.

This theorem is an endpoint receiver: it remains finite when the physical pair determinant is exactly zero, provided the null direction has genuine transverse linear coupling to the product bank.

## 3. Pure bilinear endpoint: zero physical pair

When the literal physical pair vanishes identically, the remaining two-hub geometry is linear rather than parabolic, and the entire rank-two cross block can be aggregated.

### Theorem 3 — `QFORM-ZERO-PAIR-RANK2-CROSS-v1`

In (2.1), assume `B=0` and `rank M=2`. Let `sigma_1>=sigma_2>0` be the singular values of `M`. Then

`boxed: ||p_Q||_infinity
 <= sqrt(2 pi e) (sigma_1 sigma_2)^(-1/2)`                (3.1)

with numerical front constant

`sqrt(2 pi e)=4.132731354122493...`.

Again `G(Z)` is arbitrary and lives on the same coordinates as `MZ`.

#### Proof

Condition on `Z=z` and put `y=Mz+a in R^2`. Then

`Q|Z=z = 2 y_1 X_1 + 2 y_2 X_2 + constant`.

The convolution of the two scaled one-dimensional cap-one laws satisfies

`||p_{Q|Z=z}||_infinity
 <= 1/[2 max(|y_1|,|y_2|)]
 <= 1/[sqrt(2)||y||_2]`.                                 (3.2)

Take an SVD `M=U Sigma V^T`, where `V` has two orthonormal columns. The designated fleet02/B06 weighted affine-fiber theorem, now used at `k=2`, gives

`||p_{MZ+a}||_infinity <= e/(sigma_1 sigma_2)=:L`.        (3.3)

For any probability density on `R^2` bounded by `L`, radial rearrangement against `|y|^{-1}` gives

`E ||Y||^(-1)
 <= L int_{|y|<=1/sqrt(pi L)} |y|^(-1)dy
 = 2 sqrt(pi L)`.                                        (3.4)

Average (3.2), insert (3.3)-(3.4), and obtain (3.1). QED.

This is a genuine bounded-density theorem for a rank-two bilinear crossing with arbitrary same-bank remainder. It does not come from the borderline pointwise rank-two Fourier decay.

## 4. Exact carrier geometry for the r47 two-hub plane

Return to the r45-r47 rank-three carrier notation

`A=D+R Lambda R^T`, `R^T R=I_3`,

and let `H={h,j}` be two literal original coordinates. Write `R_H` for the `2x3` row block and `T=H^c`. Define

`eta = ||r_h wedge r_j|| = sigma_1(R_H)sigma_2(R_H)`,
`G_T = R_T^T R_T = I-R_H^T R_H`,
`tau = lambda_min(G_T) = 1-sigma_1(R_H)^2`,
`s = sigma_min(Lambda)`.

The physical cross block is

`M=A_{H,T}=R_H Lambda R_T^T`.                             (4.1)

The exact Gram identity is

`MM^T = R_H Lambda G_T Lambda R_H^T`.                    (4.2)

If `tau>0`, then

`Lambda G_T Lambda >= tau Lambda^2 >= tau s^2 I`,

so

`MM^T >= tau s^2 R_H R_H^T`.                             (4.3)

Hence, denoting the nonzero singular values of `M` by `m_1>=m_2`,

`m_k >= s sqrt(tau) sigma_k(R_H)`,

and therefore

`boxed: m_1 m_2 >= s^2 tau eta.`                         (4.4)

Moreover, for every unit vector `w in R^2`,

`||M^T w|| >= m_2
 >= s sqrt(tau) sigma_2(R_H)
 >= s sqrt(tau) eta`,                                    (4.5)

because `sigma_1(R_H)<=1` and `eta=sigma_1 sigma_2`.

These identities are deterministic and do not rotate the input law.

## 5. Paying the exact degenerate-pair endpoints in r47

Suppose r47's concentrated conditional pair law has produced

`eta^2=||r_h wedge r_j||^2 > 7/64`.                      (5.1)

Thus `eta>sqrt(7)/8`.

### Rank-zero physical block

If the literal physical block `A_{H,H}=0`, Theorem 3 and (4.4) give

`boxed: ||p_Q||_infinity
 <= sqrt(2 pi e) [s^2 tau eta]^(-1/2).`                  (5.2)

For example, at `s>=1` and `tau>=1/8`, the numerical bound from (5.1) is `<20.327`.

### Rank-one physical block

If `A_{H,H}` has rank one with nonzero eigenvalue `theta`, let `w` be its unit null direction. Then Theorem 2 and (4.5) give

`boxed: ||p_Q||_infinity
 <= 2^(13/4)e^(1/4)
    [|theta| s sqrt(tau) eta]^(-1/2).`                   (5.3)

At the concrete scale gates `s>=1`, `tau>=1/8`, `|theta|>=1/8`, and (5.1), this is `<101.044`.

Thus the r47 two-hub-plane branch no longer fails merely because the physical pair is **exactly** singular. The zero pair is paid by the complete rank-two cross block; the rank-one pair is paid by parabolic curvature in its active direction and the product-averaged transverse slope in its null direction.

## 6. Actual use of the current fleet02/B06 invertible-pair result

For completeness, on the neighboring invertible **indefinite** pair branch, the current fleet02/B06 r13 theorem applies to the literal physical pair `P=A_{H,H}` and its Schur cross row. In its exact notation,

`boxed: ||p_Q||_infinity
 <= 15.0823111681 [sigma_min(P)||R_H^{cross}||_2]^(-1/4).` (6.1)

The new Theorems 2-3 are not obtained by setting `sigma_min(P)=0` in (6.1); that would diverge. They are separate endpoint estimates that exploit the exact rank loss before any reciprocal determinant is paid.

For definite invertible physical pairs, the standard two-dimensional elliptic coarea bound gives the separate direct exit `pi/sqrt(det P)`. Therefore the remaining difficult transition is **near-singular but nonzero** indefinite curvature together with arbitrary same-bank tail curvature, not the exact rank-one/rank-zero endpoints.

## 7. What remains

The full conjecture is not proved. This run removes a concrete endpoint from `QFORM-TWOHUB-PLANE-OR-ANCHOR-DEGENERACY-RECEIVER-v1` but leaves these debts:

1. `tau=1-sigma_1(R_H)^2` may be small: the two literal hubs can be an almost-coloop carrier pair, so the residual cross bank loses a direction.
2. In the rank-one physical branch the surviving eigenvalue `|theta|` may be small.
3. A near-singular but still indefinite pair can carry a logarithmic conditional singularity; exact rank-one parabolic smoothing does not automatically extend to it because arbitrary same-bank quadratic curvature can align the moving critical value.
4. The rank-three carrier `Lambda` arising in a local decomposition need not itself have `s>=1`; (5.2)-(5.3) are therefore stated with the exact scale `s` rather than silently identifying it with the target spectral threshold.

The next focused implication is

`QFORM-TWOHUB-NEARCOLOOP-OR-NEARSINGULAR-TRANSITION-v1`:

starting from the r47 carrier-plane mass, prove that small `tau` or small nonzero physical-pair eigenvalue forces either a literal three-hub localized block, the fleet02/B06 r13 P1 mixed-layer receiver, or another aggregate original-product cross packet at target scale, without taking a largest-minor reciprocal or a fiber supremum.

## 8. Continuity and claim status

Theorems 1-3 establish **essential boundedness** in their stated branches. No global continuity claim is made here; the full `QFORM-CONTINUOUS-REPRESENTATIVE` claim remains OPEN. The full arbitrary-dimensional theorem remains OPEN / NOT PROVED / NOT DISPROVED.
