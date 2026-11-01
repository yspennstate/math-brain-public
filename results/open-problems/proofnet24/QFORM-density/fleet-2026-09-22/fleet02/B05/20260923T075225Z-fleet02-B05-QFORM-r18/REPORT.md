SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B05, 2026-09-23T07:52:25Z.
attacking: make the ruled one-sheet estimate rigorous for rough product inputs at interval level, then identify and narrow the exact convex/two-sheet curved-trace factor.

# fleet02/B05 QFORM r18 — rough one-sheet interval theorem and reciprocal-shear formulation of the two-sheet debt

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea bound.  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval used; repository transport is not native learned-memory ingestion).  
**Status:** `PROVED_SUPPORTING_THEOREM / PRECISE_MISSING_FACTOR_SHARPENED / FULL_QFORM_OPEN`.  
**Continuity:** not asserted by the new theorem; the conclusion is an interval/Lipschitz bound and hence an essential density bound on the paid side.

## 1. First unpaid implication

The ruled one-sheet calculation is already geometrically correct, but rough inputs require care: the X-ray of a merely L1 projection density is only an essentially bounded two-dimensional marginal, so evaluating it on the one-dimensional curve of offsets picked by a fixed level can silently sample an exceptional representative. The correct rough statement is therefore an interval theorem, obtained by smoothing the 3D projection density while preserving every line X-ray cap and then passing back in L1.

After that repair, the first genuinely unpaid exact-rank-three geometric implication is:

`QFORM-TWOSHEET-ROUGH-NULL-SHEAR-HEAVY-v1` — for a 3D orthogonal projection of an original-coordinate product law, control the negative-level reciprocal-shear transform in Section 4 in the high-leverage class that escapes Fresnel-Brascamp-Lieb and the completed B05 packet receivers. A straight-line X-ray supremum is not enough.

## 2. Source inputs actually used

1. Required newest-Claude source at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`. Its Theorem C gives the ruled one-sheet parametrisation and the product-projection line-X-ray cap 2. The same source states that the two-sheet/convex side is the unresolved geometric side.

2. The same pinned package, `RESULTS.md` / `FOURIER_ROUTE_REPORT.md`, proves Theorem F: for an exact rank-three spectral frame with every row leverage <=1/2, all signatures are paid with density <=12. I apply this below to remove the entire diffuse curved-trace class from the two-sheet obligation.

3. Latest designated partner fleet03/B05, run `20260923T063932Z-fleet03-B05-QFORM-r22`, canonical math commit `2d50abfc12e46bb37e72db66f5a6f0e23aca5c1a`. Its ratio-packet theorem gives `||p_Q||inf <= 8*2^(3/4)*sqrt(5) (mu*kappa*m)^(-1/4)` and its exact double-zero receiver gives `||p_Q||inf <14.7240 [mu*m*(eta_R/|c|)^2]^(-1/3)`. These are applied quantitatively in Section 6.

4. Fleet01/B05 r26 at `b0299facc04ea0c03276dddb1a12c027aed5a946` supplies the ratio packet with mass `m>=3/20` used for the explicit partner thresholds.

All live corrections were retained: no arbitrary-joint 3D coarea inequality, no post-rotation independence, no unrestricted fiber supremum, no conditional-cap-as-independence, and no small-matrix-as-small-random-error step is used.

## 3. New theorem: a rough-input interval theorem on the ruled one-sheet side

### Theorem 3.1 — `QFORM-RULED-ONESHEET-ROUGH-INTERVAL-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by 1. Let `R` be an `n x 3` matrix with orthonormal columns and put `Y=R^T X`. Fix `lambda_1,lambda_2,mu >=1` and

`Q=lambda_1 Y_1^2+lambda_2 Y_2^2-mu Y_3^2`.

Then for every Borel set `E subset [0,infinity)`, without any continuity or smoothness assumption on the input laws,

`P(Q in E) <= K(lambda_1,lambda_2,mu) |E|`,

where

`K = (lambda_1 lambda_2 mu)^(-1/2) int_0^(2pi) [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2) dtheta`

and `K <= pi sqrt(2)`.

Consequently the restriction of the law of `Q` to the one-sheet half-line has an essentially bounded density at most `pi sqrt(2)`. The same statement holds after reversing all signs, with the one-sheet half-line reversed accordingly.

### Proof

Let `rho` be the density of `Y`. The completed product-projection theorem used in the newest-Claude Theorem C says that for every line direction `d` in `R^3`, the line X-ray `X_d rho` is the density of a two-dimensional orthogonal projection of the original product law and has essential supremum at most 2.

For a rough `rho`, that is only an a.e. statement on the two-dimensional offset plane; a fixed level-set ruling can in principle sample an exceptional representative. Smooth first. Let `eta_eps` be a standard nonnegative probability mollifier and set `rho_eps=rho*eta_eps`.

For every line direction, projection commutes with convolution, so `X_d rho_eps = (X_d rho) * (Pi_(d^perp) eta_eps)`. Hence `X_d rho_eps` is continuous and bounded everywhere by 2. Also `rho_eps -> rho` in `L1(R^3)`.

Put `D=diag(sqrt(lambda_1),sqrt(lambda_2),sqrt(mu))` and write `z=D y`. In isotropic Lorentz coordinates define, for `s>0`,

`e_theta=(cos theta,sin theta,0)`, `e_theta^perp=(-sin theta,cos theta,0)`, `v_theta=e_theta^perp+e_3`,

`F(s,theta,t)=sqrt(s) e_theta+t v_theta`.

Then `F_1^2+F_2^2-F_3^2=s` and a direct determinant calculation gives

`|det(d_s F,d_theta F,d_t F)|=1/2`.  (3.1)

For smooth `rho_eps`, the density on `s>0` is therefore

`p_eps(s)= [2 sqrt(lambda_1 lambda_2 mu)]^(-1) int_0^(2pi) int_R rho_eps(D^(-1)F(s,theta,t)) dt dtheta`.  (3.2)

For fixed `(s,theta)`, the inner curve is a straight line in `y` with direction `d_theta=D^(-1) v_theta`. The parameter `t` is not arclength, hence

`int_R rho_eps(y_0+t d_theta) dt = |d_theta|^(-1) int_line rho_eps dH^1 <= 2 |d_theta|^(-1)`.  (3.3)

Substituting (3.3) into (3.2) gives `p_eps(s)<=K` for every `s>0`, with the displayed `K`.

To bound `K`, put `a=1/lambda_1`, `b=1/lambda_2`, `c=1/mu`; all lie in `(0,1]`. The integrand including the outside determinant factor is

`sqrt(a b c) / sqrt(a sin^2 theta+b cos^2 theta+c)`.  (3.4)

For fixed theta, (3.4) is increasing in each of `a,b,c`: for example

`d/da log(3.4)= [b cos^2 theta+c]/[2a(a sin^2 theta+b cos^2 theta+c)] >0`,

and the `b,c` derivatives are analogous. Hence the maximum occurs at `a=b=c=1`, where the integrand is `1/sqrt(2)`. Therefore

`K<=2pi/sqrt(2)=pi sqrt(2)`.  (3.5)

Now let `E subset [0,infinity)` be Borel. For the smoothed law, `P_eps(Q in E)<=K |E|`. Since `rho_eps -> rho` in L1,

`|P_eps(Q in E)-P(Q in E)| <= ||rho_eps-rho||_1 ->0`.

Passing to the limit proves the theorem. QED.

### Why this is a genuine rough-input upgrade

The proof never evaluates an a.e.-defined marginal density on a prescribed curve. Smoothing preserves the full X-ray cap in every direction and L1 convergence returns directly to interval probabilities. Thus arbitrary fragmented and unbounded input supports are allowed, and continuity of the output density is not assumed.

## 4. Exact rough interval formula on the two-sheet side

The same change-of-variables calculation shows precisely what breaks when the level set is not ruled. It is enough to display the canonical Lorentz form `q(y)=y_1^2+y_2^2-y_3^2`.

For `s>0`, `u>=sqrt(s)` and `theta in [0,2pi)`, define

`G_+(s,theta,u)=((u-s/u)/2 e_theta, +(u+s/u)/2)`,
`G_-(s,theta,u)=((u-s/u)/2 e_theta, -(u+s/u)/2)`.

Then `q(G_pm)=-s`. The maps parametrise the two connected sheets, except for the measure-zero axis. Direct differentiation gives

`|det(d_s G_pm,d_theta G_pm,d_u G_pm)| =(1-s/u^2)/4`.  (4.1)

Therefore for every nonnegative `rho in L1(R^3)` and every `0<a<b`, with no smoothness or trace assumption,

`int_{-b<=q(y)<=-a} rho(y) dy = (1/4) sum_(pm) int_a^b int_0^(2pi) int_(sqrt(s))^infinity rho(G_pm(s,theta,u)) (1-s/u^2) du dtheta ds`.  (4.2)

Equation (4.2) is the correct rough-input interval object. Define

`T_-(rho;a,b) = [4(b-a)]^(-1) sum_(pm) int_a^b int_0^(2pi) int_(sqrt(s))^infinity rho(G_pm(s,theta,u)) (1-s/u^2) du dtheta ds`.  (4.3)

A universal bound on `T_-` for the 3D projection densities arising from product cap-one sources is exactly the canonical two-sheet essential-density theorem.

### Reciprocal-shear geometry

Put `n_theta=e_theta+e_3`, `m_theta=-e_theta+e_3`. They are orthogonal Euclidean directions and are null for the Lorentz quadratic form. Then

`G_+(s,theta,u)= (u/2)n_theta + (s/(2u))m_theta`.  (4.4)

Thus the missing integral is a reciprocal transverse shear of a null line: the transverse offset is not fixed, but drifts like `s/u`. The product-projection X-ray theorem controls a straight line with constant transverse offset; it does not control (4.4), where the offset changes along the curve. The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` is therefore hit at the correct location: bounded straight-line X-ray norm alone cannot bound (4.3). No unrestricted fiber supremum can repair this.

## 5. The convex side has the same rough-trace obstruction

For the definite canonical form `q_+(y)=|y|^2`, ordinary spherical coordinates give the exact rough interval identity

`int_{a<=|y|^2<=b} rho(y)dy = (1/2) int_a^b sqrt(s) int_(S^2) rho(sqrt(s) omega) d sigma(omega) ds`.  (5.1)

Hence the definite exact-rank-three problem asks for a universal bound on the averaged spherical trace in (5.1) for product-projection densities. An L-infinity bound on the 3D density alone cannot do this: the shell counterexample in the correction stream concentrates unit mass in an arbitrarily thin distant spherical shell. Thus the convex and two-sheet debts are the same kind of issue: curved trace stability supplied by product provenance, not merely a bound on `rho` or on its flat marginals.

## 6. Applying completed results to remove real pieces of the curved-trace obligation

### 6.1 Newest-Claude Theorem F removes the entire diffuse class

Let `R` be the exact-rank-three spectral frame and let `ell_i=||row_i(R)||_2^2`. Theorem F in the required source proves that if `max_i ell_i <=1/2`, then for every signature of the rank-three quadratic form

`||p_Q||inf<=12`.  (6.1)

Therefore both rough curved-trace operators (4.3) and (5.1) are already uniformly paid in the diffuse-leverage class. A genuinely unpaid convex/two-sheet instance must have a heavy original coordinate `max_i ell_i>1/2`.  (6.2)

This is a real structural reduction of the new coarea obligation.

### 6.2 Latest designated partner fleet03/B05 removes two quantitative packet branches

Inside the ratio-packet normal form already reached by the B05 chain, fleet01/B05 r26 supplies a packet with `m>=3/20`.

The latest partner theorem gives

`||p_Q||inf <=30.0848247447 (mu*kappa*m)^(-1/4)`.  (6.3)

Thus on the concrete subbranch `mu>=1`, `kappa>=1/4`, (6.3) yields

`||p_Q||inf <68.37`.  (6.4)

At the exact double-zero endpoint, partner r22 gives

`||p_Q||inf <14.7240 [mu*m*(eta_R/|c|)^2]^(-1/3)`.  (6.5)

Hence on `mu>=1`, `m>=3/20`, `eta_R/|c|>=1/4`, one gets

`||p_Q||inf <69.83`.  (6.6)

The same partner report records the dominant-slope exit `<81.91` when `mu>=1` and the exact-slope atom has mass at least `1/4`.

Accordingly, after the diffuse Theorem-F exit, the two-sheet packet survivor is forced toward the genuinely singular configuration already isolated by the partner: high leverage, small pair scale, no positive-mass exact slope atom, and vanishing normalized residual coupling. The rough reciprocal-shear operator (4.3) is the geometric form of what still has to be controlled there.

## 7. What changed in the proof map

1. The one-sheet theorem is now an interval statement valid for arbitrary rough product densities, with the same source constant `pi sqrt(2)` on that half-line. No pointwise representative or continuity assumption is hidden.

2. The two-sheet debt is not another X-ray estimate. It is the reciprocal-shear transform (4.3), or equivalently a product-projection stability estimate for a null line under the transverse drift `s/u`.

3. The convex debt is the analogous averaged spherical trace (5.1). Both are automatically paid by the newest-Claude Theorem F whenever every spectral-row leverage is at most `1/2`.

4. The designated partner then removes substantial heavy-packet subbranches quantitatively. What remains is a high-leverage, near-null, nonatomic, vanishing-coupling curved-trace problem. This is narrower than the previous generic phrase `two-sheet coarea`.

## 8. Independent review and target status

The new rough interval theorem and transform identities are proved here but have not received a new independent review. The full QFORM conjecture remains OPEN: no claim is made for the surviving heavy convex/two-sheet class, for arbitrary higher-rank full matrices, or for continuity of the full output density.
