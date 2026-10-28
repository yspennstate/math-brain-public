SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-23T04:04:56Z.
attacking: rough-input regularity bridge on positive annuli; apply the completed ruled one-sheet result to an annular/tent inequality and test whether minority-side singularity can be isolated without continuity or post-rotation independence.

# account02/B15 auto11 — ruled annular decomposition and a source-valid non-uniform annular-approximation obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Absolute continuity and regularity  
**Method:** complementary constructions / source-valid counterexamples  
**Partner:** account03/B15  
**Status:** `ESSENTIAL_STEP_APPLIED / ROUGH_RULED_BRIDGE_CHECKED / ANNULAR_UNIFORM_LIMIT_REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication

The full theorem is still OPEN. The most economical exact unpaid statement now comes from the completed assigned-partner result account03/B15 auto11,

`yspennstate/math-open-problems@a86bb095aac440bd79e2b2c26b23228ac952d2ab`.

For every probability law `mu` on `R`, with value `+infinity` when no bounded density exists,

`||p_mu||_infinity = sup_{r>0,y} mu({r<|z-y|<2r})/(2r)`.

Therefore QFORM is exactly equivalent, with no continuity premise and no constant loss, to

`P(r<|X^T A X-y|<2r) <= 2 C r`

for all admissible matrices and product sources, every `r>0`, and every center `y`.

This is the first unpaid implication. Continuity is not used to infer the height.

## 2. Independent check of the ruled one-sheet formula

The required Claude source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

especially `COUNTEREXAMPLE_SEARCH.md`, Theorem C. I checked the geometric constant directly.

Let

`q(y)=lambda_1 y_1^2+lambda_2 y_2^2-mu y_3^2`,

with `lambda_1,lambda_2,mu>0`. Put `z=(sqrt(lambda_1)y_1,sqrt(lambda_2)y_2,sqrt(mu)y_3)`. On the positive level `q=s>=0`, write

`F(theta,t)=sqrt(s) e_theta+t(e_theta^perp+e_3)`.

In the orthonormal basis `(e_theta,e_theta^perp,e_3)`,

`F_theta=(-t,sqrt(s),0)`, `F_t=(0,1,1)`,

so

`|F_theta x F_t|=sqrt(s+2t^2)=|grad(z_1^2+z_2^2-z_3^2)|/2`.

Hence the coarea element is exactly

`d sigma/|grad q| = (1/2)(lambda_1 lambda_2 mu)^(-1/2) dtheta dt`.

The corresponding line direction in the original three spectral coordinates has norm

`|v_theta|=[sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(1/2)`.

For a smooth product source, the arclength integral of its three-dimensional spectral projection density along that line is the density of a two-dimensional orthogonal marginal. The product-projection theorem used in the Claude source gives that marginal density at most `2`. Since `t` is not arclength, the fibre integral is at most `2/|v_theta|`. Therefore

`p_q(s) <= C_+(lambda_1,lambda_2,mu)`

for `s>=0`, where

`C_+ = (lambda_1 lambda_2 mu)^(-1/2)
       int_0^{2pi} [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2) dtheta`.

Equivalently the integrand is

`[lambda_2 mu sin^2(theta)+lambda_1 mu cos^2(theta)+lambda_1 lambda_2]^(-1/2)`.

If `lambda_1,lambda_2,mu>=kappa`, it is at most `(sqrt(2) kappa)^(-1)`, so

`C_+ <= pi sqrt(2)/kappa`.

For the target-normalised exact rank-three case `kappa>=1`, this is the advertised `pi sqrt(2)`.

The factor `1/|v_theta|` is essential: the ruling parameter is not arclength. The exact cancellation above confirms the source constant rather than merely repeating its statement.

## 3. Rough-input bridge, independently checked

The preceding line-density derivation is easiest for smooth positive inputs. It extends to arbitrary one-dimensional probability densities `0<=f_i<=1` without claiming output continuity.

For each original coordinate set

`f_i^(eta)=f_i*gamma_eta`.

Then `f_i^(eta)` remains a probability density, is smooth, and satisfies `||f_i^(eta)||_infinity<=1`. Moreover `||f_i^(eta)-f_i||_1 ->0`. In fixed finite dimension,

`||prod_i f_i^(eta)-prod_i f_i||_1 <= sum_i ||f_i^(eta)-f_i||_1 ->0`

by telescoping. Thus the joint product laws converge in total variation. A deterministic orthogonal projection or quadratic pushforward cannot increase total variation.

Apply the smooth ruled interval inequality to the padded laws. For every interval `I subset [0,infinity)`,

`P_eta(q in I) <= C_+ |I|`.

Total variation lets `eta downarrow0` in this inequality for the same measurable event, giving

`P(q in I) <= C_+ |I|`

for the original rough source. Hence the positive-side submeasure is absolutely continuous with essential density at most `C_+`. This limiting step proves essential boundedness of the submeasure; it does **not** prove that its rough density is continuous.

The same argument is stable under deterministic coordinate translations. Thus, after conditioning on outside ORIGINAL coordinates of an ambient form and completing the square in a physical invertible `3x3` block `B` of signature `(2,1)`, the three retained coordinates are still independent translated cap-one variables. If `kappa=min |eig(B)|`, the conditional majority-side submeasure has density at most `pi sqrt(2)/kappa`, uniformly in the conditioning.

## 4. Majority/minority annular decomposition

Let `W` denote the outside original coordinates and, after completing the square in the physical block, write

`Q = (X_S+h(W))^T B (X_S+h(W)) + c(W)`.

For signature `(2,1)`, define the conditional majority event

`M={Q>=c(W)}`

and positive output submeasures

`nu_+(E)=P(Q in E, M)`, `nu_-(E)=P(Q in E, M^c)`.

The ruled estimate gives, after averaging over `W`,

`nu_+(I) <= C_B |I|`, `C_B<=pi sqrt(2)/kappa`,

for every interval `I`. Consequently for every `r,y`,

`boxed{ nu_+({r<|z-y|<2r}) <= 2 C_B r. }`

This is the required application of a completed Claude result to a real positive inequality.

The partner annular theorem extends verbatim to finite positive submeasures by normalising their total mass. Therefore

`||p_{nu_-}||_infinity
 = sup_{r>0,y} nu_-({r<|z-y|<2r})/(2r)`

(with `+infinity` if no bounded density exists). Hence this physical-three-block branch is reduced exactly to the minority/two-sheet shell estimate

`boxed{ sup_{r,y} nu_-({r<|z-y|<2r})/(2r) <= C_- . }`

If this is proved, then

`||p_Q||_infinity <= C_B+C_-`.

This pinpoints the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction: a generic X-ray bound alone cannot pay `nu_-`. No continuity statement is involved.

A useful caution is that the annulus does not make a dangerous output level disappear merely because its kernel vanishes near its center. Every interval `J=(a,a+r)` is exactly the right component of the shell centered at `y=a-r`:

`J=(y+r,y+2r)`.

Thus the free center `y` can move any bad two-sheet interval into the annulus. The annular normal form is an exact positive reparameterisation of height, not by itself a cure for the minority geometry.

## 5. New source-valid obstruction: the exact annular approximate identity is not uniform over QFORM

I now combine the completed account03/B15 annular theorem with the completed account03/B15 phase-aligned target construction

`yspennstate/math-open-problems@a5094ce57d028af28c2c114f92ca26ac277d4cec`.

That source gives, for every large frequency `s`, a smooth compactly supported cap-one density `f_s` on `(1,10)` such that, for three iid coordinates and the fixed target matrix `A=I_3`, the output

`Q_s=X_{s,1}^2+X_{s,2}^2+X_{s,3}^2`

has a density `p_s in C_c^infinity((3,300))`,

`||p_s||_infinity<=1/2`,

and

`|hat p_s(s)|>=27/64`.

Let

`rho_r(u)=(1/(2r)) 1_{r<|u|<2r}`.

This is exactly the compact positive annular kernel in the partner height theorem, and

`hat rho_r(xi)=[sin(2r xi)-sin(r xi)]/(r xi)`.

Choose

`r_s=pi/s`.

Then `hat rho_{r_s}(s)=0`. Therefore

`|widehat{p_s-p_s*rho_{r_s}}(s)|=|hat p_s(s)|>=27/64`,

and the elementary bound `|hat h(s)|<=||h||_1` gives

`boxed{ ||p_s-p_s*rho_{pi/s}||_1 >=27/64. }`

Since `p_s` is supported in `(3,300)` and `p_s*rho_{pi/s}` is supported in `(3-2pi/s,300+2pi/s)`,

`boxed{
||p_s-p_s*rho_{pi/s}||_infinity
 >= 27/[64(297+4pi/s)]
 >= 27/[64(297+2pi)]
 > 1.39*10^(-3)
}`

for `s>=2`, while `r_s=pi/s ->0`.

Thus the exact annular approximate identity **does not converge uniformly in either `L^1` or `L^infinity` over the target class**, even with:

- the fixed perfectly conditioned matrix `A=I_3`;
- smooth compactly supported cap-one marginals;
- a fixed compact output support; and
- the common height bound `||p_s||_infinity<=1/2`.

This is a source-valid counterexample to a proof interface, not to QFORM. It strengthens the earlier no-uniform-continuity statement specifically at the new exact annular testing kernel: one cannot replace

`sup_{r>0,y} (p*rho_r)(y)`

by a target-uniform small-`r` approximation to `p(y)` and then appeal to qualitative continuity. Every scale has to be controlled directly.

The same obstruction holds for the partner's smooth Gaussian-annular kernel

`kappa_epsilon(u)=(u^2/epsilon^2) gamma_epsilon(u)`,

whose Fourier multiplier is

`(1-epsilon^2 xi^2) exp(-epsilon^2 xi^2/2)`.

At `epsilon_s=1/s` the multiplier vanishes at `xi=s`, so

`boxed{ ||p_s-p_s*kappa_{1/s}||_1 >=27/64. }`

Hence neither exact positive normal form supplies a target-uniform approximate-identity convergence rate.

## 6. Exact logical ledger: absolute continuity, height, continuity

For the full target, absolute continuity is already unconditional and does not pay the universal height. Let `F(x)=prod_i f_i(x)` and `q(x)=x^T A x`. Since the target has rank at least three, `A` is nonzero and the critical space `ker A` is Lebesgue-null. If `N subset R` is Lebesgue-null, coarea gives

`int_{q^{-1}(N)} F(x)|grad q(x)| dx=0`.

Outside `ker A`, `|grad q|=2|Ax|>0`, so `F dx(q^{-1}(N))=0`. Therefore `q_#(F dx)<<Lebesgue`.

So under the target hypotheses:

`target => absolute continuity` is proved,

whereas

`target => one universal essential L^infinity bound`

remains the central OPEN theorem. The canonical shared claim for a continuous representative also remains separate/open. The annular criterion can prove an essential bound without proving continuity; the rough ruled bridge above is a concrete example of such a bounded-submeasure conclusion.

Outside the target rank threshold, the logical distinctions are sharp: `X~Unif[0,1]` gives `X^2` absolutely continuous with unbounded density `1/(2sqrt(t))`; and iid `X,Y~Unif[0,1]` give `X^2+Y^2` a bounded density that jumps from `0` to `pi/4` at the origin, so essential boundedness by itself does not force a continuous representative. These controls are only logical separators; they are not counterexamples to the target.

## 7. Remaining mathematics

The new exact branch obligation is the minority/two-sheet annular estimate with original-product provenance retained. The generic X-ray-only route is already refuted, and the new annular normal form does not remove that obstruction because its center is free. A viable proof must exploit extra product-projection structure of the curved two-sheet trace, or bypass it with an aggregate original-coordinate Fourier/volume mechanism before taking an inverse local curvature cost.

Globally, even paying the minority side for one physical block would still require structural glue ensuring either a uniformly usable block or one of the already-paid diffuse/volume/hub branches. The bare three-large-eigenvalue hypothesis does not supply a uniformly conditioned single block.

No moment, support, log-concavity, identical-law, spectral-coordinate independence, or output-continuity hypothesis has been added.

## Sources actually consumed

- assigned partner annular normal form: `math-open-problems@a86bb095aac440bd79e2b2c26b23228ac952d2ab`;
- assigned partner phase-aligned regularity obstruction: `math-open-problems@a5094ce57d028af28c2c114f92ca26ac277d4cec`;
- required Claude source: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`;
- live corrections include `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`, conditional-cap/moment failures, no post-rotation independence, no uniform pointwise quadratic-phase decay, and no uniformly good single physical minor.
