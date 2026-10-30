SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B05, 2026-09-23T03:59:43Z.
attacking: a rough-input interval form of the ruled one-sheet theorem, then the exact reciprocal-shear geometry of the two-sheet side.

# fleet02/B05 r21 — rough one-sheet intervals, reciprocal shear, and a near-null scalar/dependent-pair interpolation

**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN`.

No full-solution claim is made. Independent end-to-end review of the new theorem has not yet occurred.

## 1. Fresh controls and source pins


Required newest external source actually consumed:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

I use its ruled one-sheet parametrization and its completed diffuse-leverage Theorem F at actual inequalities below. The rough interval formulation in Section 2 is a direct measure-level upgrade of its one-sheet calculation, not a claim that the one-sheet case was previously unpaid.

Other proof dependencies actually read:

- exact-rank-three scalar-pivot theorem: `math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`;
- exact null scalar/dependent-pair kernel: `math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260922T232932Z-fleet02-B16-QFORM-auto11/REPORT.md`;
- designated partner fleet03/B05 r20: `math-open-problems@929322485c85c8a08367589be2b8e2e73839c65f`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260923T014000Z-fleet03-B05-QFORM-r20/REPORT.md`.

Live corrections retained: no post-rotation independence, no generic three-dimensional joint-density coarea lemma, no X-ray-only two-sheet replacement, and no conditional-cap-for-independence substitution.

## 2. Rough-input one-sheet interval theorem

Let `X=(X_1,...,X_n)` have independent densities bounded by one, let `R^T R=I_3`, put `Y=R^T X`, and let `rho` denote its three-dimensional density. For `lambda_1,lambda_2,mu>=1`, define

`q(y)=lambda_1 y_1^2+lambda_2 y_2^2-mu y_3^2`.

### Theorem 2.1 — `QFORM-RULED-ROUGH-INTERVAL-v1`

For every Borel interval `J subset [0,infinity)`,

`P(q(Y) in J) <= C_+(lambda_1,lambda_2,mu)|J| <= pi sqrt(2)|J|`,

where

`C_+=(lambda_1lambda_2mu)^(-1/2) integral_0^{2pi} [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2)dtheta`.

No continuity of `rho` or pre-existing pointwise output density is assumed.

### Proof

Put `D=diag(sqrt(lambda_1),sqrt(lambda_2),sqrt(mu))`, `z=Dy`, `e_theta=(cos theta,sin theta,0)` and `e_theta^perp=(-sin theta,cos theta,0)`. For `s>0`,

`z=sqrt(s)e_theta+t(e_theta^perp+e_3)`

parametrizes the one-sheet level. In the moving basis `(e_theta,e_theta^perp,e_3)`, the derivative columns with respect to `(s,theta,t)` are

`(1/(2sqrt(s)),0,0)`, `(-t,sqrt(s),0)`, `(0,1,1)`,

so the absolute Jacobian is exactly `1/2`. Therefore Tonelli and change of variables yield, for intervals away from zero,

`P(q(Y) in J)=(2sqrt(lambda_1lambda_2mu))^(-1) integral_J ds integral_0^{2pi}dtheta integral_R rho(D^(-1)[sqrt(s)e_theta+t(e_theta^perp+e_3)])dt`.

The line direction in the original `y` coordinates is

`d_theta=D^(-1)(e_theta^perp+e_3)`

with

`|d_theta|^2=sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu`.

The inner `t` integral is `|d_theta|^(-1)` times an arclength line integral of `rho`, hence a value of a two-dimensional orthogonal marginal density. The sharp product-projection input used in the required newest source bounds that marginal by `2`. This gives the displayed `C_+` after `(s,theta)` integration.

Moreover

`lambda_1lambda_2mu |d_theta|^2=lambda_2mu sin^2(theta)+lambda_1mu cos^2(theta)+lambda_1lambda_2>=2`,

so the integrand in `C_+` is at most `1/sqrt(2)` pointwise and `C_+<=pi sqrt(2)`. The cone has Lebesgue measure zero under the three-dimensional projection law, so there is no atom at zero; monotone convergence includes intervals meeting zero. QED.

This turns the ruled calculation into the exact rough-input interval theorem requested by the card while preserving the curved geometry and avoiding pointwise regularity assumptions.

## 3. Exact two-sheet reciprocal-shear identity

The useful new coordinate description of the negative side is the following. For `u>0`, `sigma in {+1,-1}`, set

`n_{theta,sigma}=e_theta+sigma e_3`,
`m_{theta,sigma}=-e_theta+sigma e_3`,

and for `T>sqrt(u)/2`,

`y_sigma(u,theta,T)=D^(-1)[T n_{theta,sigma}+(u/(4T))m_{theta,sigma}]`.

Then `q(y_sigma)=-u` exactly: in `z` coordinates the positive radius is `T-u/(4T)` and the signed third coordinate is `sigma(T+u/(4T))`.

Starting from the ordinary hyperbolic coordinates

`z=sqrt(u)sinh(v)e_theta+sigma sqrt(u)cosh(v)e_3`,

whose volume Jacobian is `sqrt(u)sinh(v)/2`, and setting `T=sqrt(u)e^v/2`, gives `dv=dT/T` and hence the exact Jacobian

`[2sqrt(lambda_1lambda_2mu)]^(-1)[1-u/(4T^2)]`.

Thus, for every interval `J subset (0,infinity)`,

`P(q(Y) in -J)`

`=(2sqrt(lambda_1lambda_2mu))^(-1) sum_sigma integral_0^{2pi}dtheta integral_{T>0} integral_{u in J, u<4T^2}`

` rho(y_sigma(u,theta,T))[1-u/(4T^2)] du dT`.

In particular, for a.e. `u>0`,

`p_q(-u)=(2sqrt(lambda_1lambda_2mu))^(-1) sum_sigma integral_0^{2pi} integral_{sqrt(u)/2}^infinity rho(y_sigma(u,theta,T))[1-u/(4T^2)]dT dtheta`.     (3.1)

Equation (3.1) is the exact unpaid curved transform. It is not an unrestricted fiber supremum. At `u=0` the reciprocal displacement vanishes and the curves collapse to null rays; for `u>0` they are the reciprocal shears

`T n + (u/(4T))m`.

This shows precisely why the one-sheet X-ray argument cannot simply be copied. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction gives an arbitrary-joint thin-shell counterexample to that replacement. Product-projection provenance is the remaining resource.

## 4. Source-bound reduction before the new interpolation theorem

Let the exact-rank-three active frame have rows `r_i`, leverage `c_i=||r_i||^2`, and physical diagonal `a_i=r_i^T Lambda r_i`.

The required newest source Theorem F applies directly if every `c_i<=1/2`, giving

`||p_Q||_infinity<=12`.                                              (4.1)

So both sides of (3.1) are already paid in the diffuse-leverage regime.

If some heavy row has `c_i>1/2` and `|a_i|>=delta`, the source-pinned exact-rank-three scalar-pivot theorem gives

`||p_Q||_infinity<=128(c_i|a_i||det Lambda|)^(-1/4)
                  <=128(2/delta)^(1/4)`.                              (4.2)

Hence with `delta=1/16`, every still-unpaid exact-rank-three state may be restricted to heavy rows satisfying `|a_i|<1/16`. There are at most five heavy rows because `sum_i c_i=3`. Each such near-null heavy row nevertheless has a strong cross arm:

`||A_{i,-i}||_2^2=(A^2)_ii-a_i^2=r_i^T Lambda^2r_i-a_i^2
                  >=c_i-a_i^2>127/256`.                              (4.3)

So the obstacle is not missing cross mass. It is retaining the selector/product structure while spending that arm together with a third curvature.

The designated partner fleet03/B05 r20 applies whenever those resources can be routed into its three disjoint coefficient banks with affine smoothing side: if `||r||||c||||D||_HS>=eta`, then

`||p_Q||_infinity<=K_3 eta^(-1/3)`.                                  (4.4)

Thus a survivor after (4.1)--(4.4) must either fail that three-resource routing or contain the partner's precise obstruction, same-side quadratic curvature on the smoothing banks.

## 5. New theorem: uniform interpolation away from the exact null scalar pivot

The latest shared synthesis records that the exact null-coloop endpoint is already paid by fleet02/B16. The following theorem extends its analytic kernel to **arbitrary nonzero scalar pivot** without a perturbative moment argument. It is uniform as the pivot tends to zero.

### Theorem 5.1 — `QFORM-NEARNULL-SCALAR-DEPENDENT-PAIR-v1`

Let `X` be a real random variable with probability density `f<=1`. Let `(C,D)` be independent of `X` and have an arbitrary joint probability density `g` with `||g||_infinity<=M`; `C,D` need not be independent. Consider

`Q=aX^2+2 beta X C+alpha C^2+2 delta C D+gamma D^2`,                  (5.1)

with `beta!=0`, `gamma!=0`, and the symmetric coefficient matrix

`B=[[a,beta,0],[beta,alpha,delta],[0,delta,gamma]]`                  (5.2)

invertible. Then `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity <=31 M^(2/3)|beta^2 gamma det B|^(-1/6).`   (5.3)

The estimate is uniform in the scalar pivot `a`, including the limit `a->0`. For `a=0` the already-completed fleet02/B16 null-scalar theorem is stronger and implies (5.3); below I prove the new `a!=0` case.

### Step 1: shear only inside the dependent pair

Because `gamma!=0`, replace `D` by `D+(delta/gamma)C`. This linear map has determinant one, so the joint pair density cap remains `M`, and independence of `X` from the whole pair is unchanged. Thus it suffices to study

`Q=aX^2+2 beta X C+kappa C^2+gamma D^2`,                              (5.4)

where `kappa=alpha-delta^2/gamma`. Put

`Delta=a kappa-beta^2`.

Then `det B=gamma Delta`, so `Delta!=0`.

### Step 2: the exact conditional root kernel

For a.e. target `t`, one-dimensional change of variables in the genuinely independent scalar `X` gives

`p_Q(t)=integral g(c,d) K_t(c,d) dc dd`,                             (5.5)

where

`K_t(c,d)=sum_{x:Q(x,c,d)=t} f(x)/(2|a x+beta c|)`                   (5.6)

and critical roots are irrelevant on a null set.

If `K_t(c,d)>s`, at least one of the at most two roots satisfies

`f(x)>s|w|`,  where `w=a x+beta c`.                                  (5.7)

Since `f<=1`, every such root has `|w|<1/s`.

### Step 3: parameterize the superlevel set without discarding the selector

For a qualifying root use `(x,w)` as coordinates and write

`c=(w-a x)/beta`.

The part of (5.4) not containing `gamma d^2` is

`P(x,w)=a x^2+2 beta x c+kappa c^2
       =w^2/a+A(x-w/a)^2`,                                          (5.8)

where

`A=a Delta/beta^2`.                                                   (5.9)

For each sign of `d`, the level equation `gamma d^2=t-P(x,w)` defines a map `(x,w)->(c,d)`. A direct implicit differentiation gives

`|det partial(c,d)/partial(x,w)|=|w|/(|beta gamma d|)`.              (5.10)

Indeed `c_x=-a/beta`, `c_w=1/beta`, `2gamma d d_x=-P_x`, `2gamma d d_w=-P_w`, while the elementary identity

`a P_w+P_x=2w`                                                        (5.11)

makes all other terms cancel.

Summing the two possible signs of `d` and using the area formula, the Lebesgue measure of `{K_t>s}` is at most

`2/(|beta|sqrt(|gamma|)) integral_{|w|<1/s} |w| I(w) dw`,            (5.12)

where

`I(w)=integral_{E_w}|t-w^2/a-Au^2|^(-1/2)du`,                        (5.13)

`u=x-w/a`, and by probability normalization of `f`,

`|E_w|<=1/(s|w|)`.                                                    (5.14)

This is the decisive difference from replacing `f` by its pointwise cap. The root-location selector remains present through (5.14).

### Step 4: one-dimensional curved trace estimate

For every nonzero `A,v` and every measurable `E` of length `L`,

`integral_E |v-Au^2|^(-1/2)du
 <=4 |A|^(-1/4)|v|^(-1/4)L^(1/2)`.                                  (5.15)

Proof. Scale `u=sqrt(|v|/|A|)y`. It is enough to show that for either kernel

`k_+(y)=|1-y^2|^(-1/2)`, `k_-(y)=(1+y^2)^(-1/2)`,

and every set of length `L'`, `int_E k<=4sqrt(L')`. Both kernels satisfy the distribution estimate

`|{k>r}|<=4/r` for `0<r<1`, and `|{k>r}|<=4/r^2` for `r>=1`.

Layer cake gives exactly the asserted `4sqrt(L')`: if `L'<=4`, split at `r=2/sqrt(L')`; if `L'>4`, the bound is `8+4log(L'/4)<=4sqrt(L')`. Scaling back proves (5.15). QED.

Applying (5.15) and (5.14) in (5.12) yields

`|{K_t>s}| <=8 |beta|^(-1)|gamma|^(-1/2)|A|^(-1/4)s^(-1/2)
              integral_{|w|<1/s}|w|^(1/2)|t-w^2/a|^(-1/4)dw`.       (5.16)

The remaining integral is uniformly controlled. With `z=sw` and `tau=a t s^2`,

`integral_{|w|<1/s}|w|^(1/2)|t-w^2/a|^(-1/4)dw
 =|a|^(1/4)s^(-1) J(tau)`,                                          (5.17)

where

`J(tau)=integral_{-1}^1 |z|^(1/2)|tau-z^2|^(-1/4)dz
      =integral_0^1 y^(-1/4)|tau-y|^(-1/4)dy <=4`.                   (5.18)

For `tau<=0`, bound by `int_0^1 y^(-1/2)dy=2`; for `tau>=1`, bound by the beta integral `B(3/4,3/4)<2`; for `0<tau<1`, split at `tau`, obtaining less than `B(3/4,3/4)+2<4`.

Combining (5.9), (5.16)--(5.18),

`|{K_t>s}|
 <=32 H s^(-3/2)`,                                                   (5.19)

where

`H=|beta|^(-1/2)|gamma|^(-1/2)|Delta|^(-1/4)
  =|beta^2 gamma det B|^(-1/4)`.                                    (5.20)

Crucially, the factor `|a|^(1/4)` in (5.17) cancels the `|a|^(-1/4)` coming from `|A|^(-1/4)`. This is why the estimate survives the near-null limit.

### Step 5: average against the dependent-pair density

Using both `g<=M` and `integral g=1`,

`integral_{K_t>s} g <= min(1,32 M H s^(-3/2))`.                      (5.21)

Layer cake gives

`p_Q(t)<= integral_0^infinity min(1,32 M H s^(-3/2))ds
       =3(32 M H)^(2/3)
       <31 M^(2/3)|beta^2 gamma det B|^(-1/6)`.                      (5.22)

This is uniform in `t`, proving (5.3). Standard one-dimensional change of variables plus Tonelli supplies the a.e. density; the uniform estimate then gives absolute continuity. QED.

### Why this is compatible with the live dependence corrections

The proof never treats `C,D` as independent. It never conditions on a nonlinear shear and then promotes a conditional cap to independence. The only genuine independence is the original scalar `X` versus the entire pair `(C,D)`. The pair shear in Step 1 has determinant one and is used only because arbitrary dependence inside the pair is already allowed. Most importantly, the selector `f(x)` is not dropped in Step 2: its probability normalization is exactly what produces the finite-length set (5.14). Dropping it would recover the false unrestricted two-sheet/fiber mechanism.

## 6. Quantitative near-null coloop consequence

Suppose an exact-rank-three frame has an ORIGINAL leverage-one coordinate, so the corresponding scalar is independent of the remaining two-dimensional projection. The weighted product-projection result used in the completed B16 proof gives the dependent pair density cap `M<=e`.

Choose an orthonormal basis in the dependent pair so the cross vector from the scalar is `(beta,0)`. This rotation is inside the already-dependent pair and preserves its density cap. If the scalar pivot satisfies `|a|<=1/16`, the spectral hypothesis `s_min(B)>=1` gives

`beta^2=||B e_1||^2-a^2 >=1-a^2 >=255/256`.                         (6.1)

If in addition the transverse pair curvature in this aligned basis satisfies `|gamma|>=1/2`, then `|det B|>=1`, and Theorem 5.1 gives the fully numerical target-level bound

`||p_Q||_infinity
 <=31 e^(2/3) (512/255)^(1/6)
 <68`.                                                               (6.2)

This includes arbitrarily small **nonzero** scalar pivots and therefore genuinely extends the already-paid exact-null endpoint in this transverse-curvature branch.

If `|gamma|<1/2`, the unit lower singular-value bound applied to the cross-orthogonal pair direction gives

`delta^2+gamma^2=||B e_3||^2>=1`, hence `|delta|>sqrt(3)/2`.           (6.3)

Thus the coloop near-null debt is reduced to a concrete mixed-transverse branch: the direct transverse square is small but the pair cross-curvature is large. This is a sharper obstruction than the previous phrase "near-null nonzero coloop".

## 7. Relation to the reciprocal-shear and partner mechanisms

Theorem 5.1 may be viewed as a product-sensitive substitute for an impossible generic bound on the two-sheet transform (3.1): it retains one genuine original scalar and uses the probability-normalized root selector before paying the curved quadratic trace. In the complementary multi-bank situation, fleet03/B05 r20 pays three affine arms by the whole product `||r||||c||||D||_HS` before reciprocal inversion. These are compatible mechanisms:

- Theorem 5.1 pays one independent scalar plus an arbitrarily dependent projected pair when the transverse curvature `gamma` is present.
- Partner r20 pays three disjoint coefficient resources when the smoothing side is affine, even with a diffuse bilinear core.
- What neither currently pays is the simultaneous combination of a near-null/mixed-transverse scalar-pair geometry with arbitrary same-side quadratic curvature across the smoothing banks.

## 8. First unpaid implication

`QFORM-TWOSHEET-MIXED-TRANSVERSE-OR-THREEARM-CURVATURE-v1`:

In the high-leverage near-null survivor after (4.1)--(4.3), prove one of the following without losing original-coordinate product provenance:

1. extract a leverage-one/near-coloop scalar-pair state in which the aligned transverse coefficient `|gamma|` is quantitatively nontrivial, then apply Theorem 5.1;
2. if `gamma` is small, spend the forced large mixed pair curvature (e.g. (6.3) in the exact-coloop state) by a corresponding curved trace estimate; or
3. route the strong cross arm and remaining curvature into the partner r20 three-resource packet while allowing the presently unpaid same-side quadratic curvature.

The exact negative-level formula (3.1) should remain the geometric receiver. A proof must average the reciprocal-shear traces or retain a root selector/product factor; it must not replace them by unrestricted fiber suprema or generic X-ray caps.

## 9. Status summary

- full arbitrary-dimensional QFORM: **OPEN / NOT PROVED / NOT DISPROVED**;
- one-sheet rough interval formulation: **proved here, source-compatible**;
- exact reciprocal-shear two-sheet identity: **proved here**;
- near-null scalar/dependent-pair interpolation with `beta gamma det B !=0`: **proved here**;
- exact-null endpoint: previously proved by fleet02/B16 and only used as the `a=0` boundary;
- diffuse leverage: paid by newest-source Theorem F;
- affine three-arm diffuse-core branch: paid by designated partner fleet03/B05 r20;
- mixed-transverse / same-side-curvature two-sheet branch: **OPEN**;
- independent review of this report: **PENDING**.
