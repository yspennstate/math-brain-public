# account02/B14 — translation-frame localization and the saturated-fragment barrier

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: new supporting theorem + exact-target obstruction to a proof interface. The unrestricted conjecture remains OPEN. Continuity is separate.

## 1. Exact target and scope

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities `f_i<=1`, and let

`P(x)=x^T A x+b^T x+c`

with `A` real symmetric. The owner target asks for one universal `C` whenever at least three eigenvalues of `A` have modulus at least one. No moment, support, connectedness, log-concavity, identical-law or post-rotation independence assumption is available.

This note studies only localization/mixture steps that preserve the original-coordinate product structure and arbitrary affine terms.

## 2. Affine-uniform core constant

For a product probability density `g(z)=prod_i g_i(z_i)` and fixed symmetric `A`, define

`Lambda_A(g)=sup_{ell,gamma,I} |I|^{-1} P_g(z^T A z+ell^T z+gamma in I)`,

where `I` ranges over bounded open intervals and the supremum is over all deterministic affine coefficients. This is the right quantity for translation localization because coordinate translations leave the quadratic matrix unchanged and only alter affine data.

## 3. QFORM-TRANSLATION-FRAME-COMPILER-v1

For each coordinate `i`, suppose

`f_i=sum_{j in J_i} rho_{ij}`

as a finite or countable sum of nonnegative subdensities. For every `(i,j)` suppose there are a translation `a_{ij}`, a probability density `g_{ij}`, and a number `c_{ij}>=0` such that

`rho_{ij}(z+a_{ij}) <= c_{ij} g_{ij}(z)` a.e.

Put `D_i=sum_j c_{ij}`. Assume that for every multi-index `alpha=(j_1,...,j_n)` the product core

`g_alpha(z)=prod_i g_{i,j_i}(z_i)`

has the same affine-uniform certificate

`Lambda_A(g_alpha) <= C`.

Then

`Lambda_A(prod_i f_i) <= C prod_i D_i`.                                                (3.1)

This is completely translation-uniform and permits arbitrary countable remote fragments and unbounded supports. It has no moment or diameter term.

### Proof

Expand the product law into positive cells `rho_alpha(x)=prod_i rho_{i,j_i}(x_i)`. For one cell set `a_alpha=(a_{1,j_1},...,a_{n,j_n})` and substitute `x=z+a_alpha`. Then

`P(z+a_alpha)=z^T A z+(b+2A a_alpha)^T z + c+b^T a_alpha+a_alpha^T A a_alpha`.

Meanwhile

`rho_alpha(z+a_alpha) <= (prod_i c_{i,j_i}) g_alpha(z)`.

The affine-uniform core bound therefore gives

`int 1_{P(x) in I} rho_alpha(x) dx <= C |I| prod_i c_{i,j_i}`.

Sum by Tonelli/monotone convergence. The multi-index sum factorises:

`sum_alpha prod_i c_{i,j_i}=prod_i sum_j c_{ij}=prod_i D_i`.

This proves (3.1).

The same proof applies to positive finite mixing measures and to subprobability laws: the coefficient is exactly linear in the domination mass.

## 4. Exact zero-loss characterization

Let `m_{ij}=int rho_{ij}`. Integrating the domination inequality gives

`m_{ij} <= c_{ij}`.

Hence always

`D_i >= sum_j m_{ij}=1`.                                                            (4.1)

Consequently the compiler has zero localization tax in coordinate `i` iff `D_i=1`. Because every summand satisfies `c_{ij}>=m_{ij}`, equality forces `c_{ij}=m_{ij}` for every positive-mass piece. In that case

`rho_{ij}(z+a_{ij})/m_{ij} <= g_{ij}(z)`

and both sides are probability densities, so equality holds a.e. Therefore:

**zero-loss positive translate domination is possible iff every normalized fragment is itself exactly a translate of the probability core used for that fragment.**

If one insists on one common core `g_i` for all fragments of a coordinate, zero loss occurs iff all normalized fragments are translates of that same shape. This recovers ordinary convolution/random-centre mixtures as an exact special case, and shows precisely how much stronger general positive domination is allowed to be before it starts paying a tax.

## 5. QFORM-PEAK-MASS-DOMINATION-TRADEOFF-v1

Suppose additionally `||g_{ij}||_infinity<=M`. Taking essential suprema in the pointwise domination gives

`c_{ij} >= ||rho_{ij}||_infinity/M`.                                                (5.1)

Together with `c_{ij}>=m_{ij}`,

`c_{ij} >= max(m_{ij}, ||rho_{ij}||_infinity/M)`.                                  (5.2)

Thus a narrow cap-saturated fragment of mass `m` and peak one has inflation

`c/m >= max(1,1/(M m))`.

In particular, if the downstream core theorem is available only for cap-one probability cores (`M=1`), a saturated fragment `rho=1_E` of any positive mass forces `c>=1`. The coefficient no longer carries the fragment mass. This is exactly the failure mode that a mass-homogeneous localization theorem must avoid.

The tradeoff is sharp at the level of peak versus mass. Allowing a core cap `M` can reduce the coefficient only until `c=max(m,1/M)`; in particular `M c>=1` for a saturated fragment. A zero-loss coefficient `c=m` requires `M>=1/m`.

## 6. Exact comb obstruction

Let

`E_N = union_{j=1}^N [4^j,4^j+1/N]`,
`f_N=1_{E_N}`.

This is a legal cap-one probability density with arbitrarily remote fragments. Split it into its saturated teeth

`rho_j=1_[4^j,4^j+1/N]`, `m_j=1/N`.

For any family of cap-one probability cores `g_j` and arbitrary translations satisfying

`rho_j(.+a_j) <= c_j g_j`,

(5.1) gives `c_j>=1`, hence

`D=sum_j c_j >= N`.                                                                 (6.1)

This lower bound is exact: a cap-one unit-interval core can dominate any one tooth with coefficient one after translation. If one allows core cap `M`, then

`D >= max(1,N/M)`, hence `M D >= N`.                                                 (6.2)

So separated-fragment location is not the source of the loss: arbitrary translations are already free. The obstruction is peak-to-mass concentration created by fragment-first positive domination.

For three independent coordinates all having density `f_N`, cellwise product localization has

`prod_i D_i >= N^3`                                                                  (6.3)

if all three active marginals are split tooth-by-tooth before a cap-one affine-uniform core theorem is paid. Splitting only one active marginal already incurs the factor `N`.

This is a proof-interface obstruction, not a lower bound on the true quadratic-form density.

## 7. The obstruction remains inside the newest partner reduction class

Newest compatible designated partner account03/B14 proved `QFORM-SMOOTH-CONNECTED-SUPPORT-ZERO-LOSS-v1` at

`math-open-problems@46f817e053914df4ed718042194c1ff39f425e46`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260923T223632Z-account03-B14-QFORM-auto11/REPORT.md`.

That theorem says the optimal interval-density constant is unchanged when every marginal is restricted to `C_c^infinity` densities with one finite interval as support, positive throughout the interior and strictly below one. The support diameter and interior density floor are not uniform.

The peak-mass barrier survives this reduction quantitatively. Fix `N` and `eta>0`. Around each tooth choose a smooth compact bump `u_j` with disjoint supports, `0<=u_j<=1-eta`, and with a nonempty inner interval `K_j` on which `u_j=1-eta`. Choose the bumps so `u=sum_j u_j` has mass `<1` but arbitrarily close to one. Because the convex hull of the remote teeth is arbitrarily long, choose a smooth probability bump `q` supported on that hull, positive throughout its interior, with `||q||_infinity` so small that, with `alpha=1-int u`,

`h=u+alpha q`

satisfies `0<h<1` on the interior, `int h=1`, and has one connected compact support. Thus `h` lies in the partner's zero-loss reduced class, while on every `K_j`,

`h >= 1-eta`.

If a subsequent proof re-localizes these `N` plateau pieces `rho_j=h 1_{K_j}` separately and positively dominates each by any cap-one probability core after arbitrary translation, (5.1) forces

`c_j >= 1-eta`,

so

`sum_j c_j >= N(1-eta)`.                                                            (7.1)

Therefore connected support and smoothness do not cure fragment-first positive domination. The partner theorem is safe only as a whole-law closure reduction: the analytic estimate after that reduction must remain uniform as the support diameter grows and the artificial bridge floor tends to zero.

## 8. Required source theorem applied to the same obstruction

The fixed required Claude source was read at

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` in `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its proved Theorem A states that in dimension three, if every eigenvalue of the quadratic matrix has modulus at least `sigma`, then, with arbitrary linear terms,

`||p_Q||_infinity <= 6 sqrt(pi)/sigma`.

Apply it to the exact-target family

`Q_N=X_1^2+X_2^2+X_3^2`, `A=I_3`,

with the three independent marginals equal either to `f_N` above or to any of the smooth connected cap-one densities `h` constructed in Section 7. Then

`||p_{Q_N}||_infinity <= 6 sqrt(pi) = 10.634723105433...`                        (8.1)

uniformly in `N`, all fragment locations, all support diameters and all bridge floors.

Compare (8.1) with (6.3)/(7.1): the true source-valid whole-law certificate is constant while any route that first isolates every narrow high plateau and then transfers a cap-one core theorem by positive domination loses at least one factor of order `N` per fragmented active marginal. Therefore `QFORM-SATURATED-FRAGMENT-DOMINATION-BARRIER-v1` is a genuine proof-order obstruction and not a QFORM counterexample.

## 9. Consequence for the full proof

The safe localization order is now exact:

1. It is legitimate, with zero constant loss, to use account03/B14's whole-law smooth connected-support reduction.
2. It is legitimate to translate arbitrary positive pieces once a protected affine-uniform core certificate has been paid; (3.1) gives the exact coefficient.
3. Zero-loss fragment mixing requires full mass homogeneity `c_j=m_j`; for saturated narrow fragments this is impossible with cap-one probability cores unless the core itself concentrates at scale `1/m_j`.
4. Therefore the remaining full-target estimate must be paid on the whole active marginal (or through an aggregate signed/phase-sensitive mechanism) before narrow high peaks are normalized or positively dominated separately.

A proof that depends on bounded support diameter, a fixed fragment count, a uniform bridge floor, or normalized active fragments is not a valid closure of the owner target.

## 10. First unpaid implication

`QFORM-WHOLE-ACTIVE-CERTIFICATE-BEFORE-PEAK-DOMINATION-v1`:

On the smooth connected-support strict-subcap class supplied by account03/B14, prove a whole-active affine-uniform estimate for every remaining no-pivot/near-degenerate configuration, uniform as support diameters tend to infinity and bridge floors tend to zero; or produce an aggregate localization functional whose submeasure coefficient carries a full power of the fragment mass despite peak near one. The translation variable itself is no longer the debt: the exact debt is concentration before aggregation.

Execution classification for the scheduled worker remains `WITHOUT_VERIFIED_BRAIN`; repository transport is not native receiver-memory ingestion.
