SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B14, 2026-09-24T05:36:25Z.
attacking: endpoint Beta localization — extend the newest fleet03/B14 same-sign overlap compiler to finite active submeasures, prove exact zero-tax outside localization, and show active square-carrier fragmentation has no positive mass homogeneity and therefore must be aggregated before the endpoint Beta payment.

# fleet02/B14 — endpoint Beta localization and active-fragment barrier

Run: `20260924T053625Z-fleet02-B14-QFORM-auto11`.
Status: **supporting localization theorem proved / exact-target fragment-first obstruction proved / newest partner applied / fixed Claude-source theorem applied / full unrestricted QFORM OPEN / continuity separate**.

## 1. First unpaid implication

`QFORM-WHOLE-SQUARE-CARRIER-OR-MASS-HOMOGENEOUS-EXIT-v1`.

Before paying a same-sign two-square Beta endpoint, keep both active square-carrier original marginals aggregated. Arbitrary positive localization is free on an independent environment, but not on either active square carrier. If a structural decomposition must fragment an active carrier, it has to switch *before* the Beta endpoint to a genuinely mass-homogeneous whole-law mechanism: an aggregate linear-slope receiver, projected crossing/volume estimate, ridge/hub/grouped-bank theorem, or a physical-triple/Schur certificate whose finite-measure scaling carries the fragment mass.

The remaining full-target debt is structural: derive one of those safe representations/exits from only `s_3(A)>=1` without bounded fragment count, bounded diameter, hidden moments, or reciprocal payment of an arbitrarily small physical pivot.

## 2. Newest designated partner used

The newest compatible fleet03/B14 run is

`yspennstate/math-open-problems@7c982b2537be11bbe3f63123e2870171bfb27717`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260924T043626Z-fleet03-B14-QFORM-auto11/`.

Its authoritative source-match addendum identifies the useful surviving theorem as `QFORM-OVERLAP-SAME-SIGN-SQUARE-COMPILER-v1`:

Let `W,U,Z` be mutually independent, let `W,U` have probability density caps `K_W,K_U`, let `a,d` be nonzero with the same sign, and let `Phi(U,Z), theta(Z), R(Z)` be arbitrary measurable functions. Then

`T=a(W+Phi(U,Z))^2+d(U+theta(Z))^2+R(Z)`

has an essentially bounded density satisfying

`||p_T||inf <= pi K_W K_U/sqrt(|a d|)`.

The same source explicitly permits the first square's center to depend on the transverse active variable `U` and on the environment `Z`. A same-sign random affine slope in `U` is absorbed by completing the `U` square. No support, moment, fragment, diameter, tail, smoothness or translation parameter enters.

The partner addendum also source-matches the ordinary definite physical-pair determinant bound to an earlier fleet theorem; I therefore do not relabel that older statement as new here. The extension below is about finite-measure localization and its sharp asymmetry between active carriers and outside environment.

## 3. Finite-measure extension: exact outside mass homogeneity

### Theorem `QFORM-SAME-SIGN-BETA-SUBMEASURE-COMPILER-v1`

Let `rho_W dw` and `rho_U du` be finite positive measures with Lebesgue densities satisfying

`0<=rho_W<=L_W`, `0<=rho_U<=L_U`.

Let `tau` be an arbitrary finite positive measure on an independent environment space, of total mass

`m_Z=tau(Zspace)`.

Assume the product measure `rho_W dw x rho_U du x tau(dz)`. Let `a,d` be nonzero and have the same sign. For arbitrary measurable `Phi(u,z)`, `theta(z)`, `R(z)`, push this product measure forward by

`T(w,u,z)=a(w+Phi(u,z))^2+d(u+theta(z))^2+R(z)`.

Then the output finite measure `eta` is absolutely continuous and

`boxed: ||p_eta||_(infinity,ess) <= pi L_W L_U m_Z / sqrt(|a d|).`

This estimate is independent of the masses of the active submeasures except through their pointwise caps. It is exactly linear in the *environment* mass.

### Proof

Reflect the output if needed, so take `a,d>0`.

Fix `(u,z)`. Translation does not change the pointwise cap of `rho_W`. Under

`w -> a(w+Phi(u,z))^2`,

the two inverse branches give, for `v>0`,

`p_(a(W+Phi)^2)(v)`

`= [rho_W(-Phi+sqrt(v/a))+rho_W(-Phi-sqrt(v/a))]/(2 sqrt(a v))`

`<= L_W/(sqrt(a) sqrt(v)).`

Now fix `z` and an output point `q`; put `s=q-R(z)`. After integrating out `W`,

`p_(eta_z)(q)`

`<= L_W/sqrt(a) * int rho_U(u) 1_{d(u+theta(z))^2<s}/sqrt(s-d(u+theta(z))^2) du.`

For `s<=0` the right side is zero. For `s>0`, use `rho_U<=L_U`, translate `u`, and evaluate the endpoint Beta integral exactly:

`int_{|v|<sqrt(s/d)} dv/sqrt(s-dv^2)=pi/sqrt(d)`.

Therefore, uniformly in `z,q`,

`p_(eta_z)(q) <= pi L_W L_U/sqrt(a d)`.

Integrating these finite conditional measures against `tau(dz)` gives

`p_eta(q) <= m_Z pi L_W L_U/sqrt(a d)`

for almost every `q`. This proves the theorem.

No normalization of a spatial fragment was used. Arbitrary translations, remote fragments, unbounded supports, and conditioning-generated affine centers are retained literally.

## 4. Exact zero-tax localization theorem for the outside environment

Let the outside measure be any countable positive decomposition

`tau=sum_j tau_j`, `m_j=tau_j(Zspace)`, `sum_j m_j=m_Z`.

Apply the theorem to each output submeasure `eta_j`. Since the active caps `L_W,L_U` are unchanged,

`||p_(eta_j)||inf <= pi L_W L_U m_j/sqrt(|a d|)`.

The total output measure is `eta=sum_j eta_j`; therefore

`||p_eta||inf <= sum_j ||p_(eta_j)||inf`

`<= pi L_W L_U/sqrt(|ad|) * sum_j m_j`

`= pi L_W L_U m_Z/sqrt(|ad|)`.

So arbitrary finite or countable localization of the independent environment is **exactly zero-tax**, even if the pieces are arbitrarily distant, have unbounded combined support, possess no densities at all, and induce arbitrary piece-dependent translations through `Phi,theta,R`.

This is the localization/mixture principle compatible with the full rough-law target in this chamber.

## 5. Active square-carrier mass homogeneity is impossible

The preceding linear mass factor is special to the outside environment. It cannot hold for a same-sign active square carrier.

### Proposition `QFORM-SAME-SIGN-BETA-ACTIVE-MASS-HOMOGENEITY-IMPOSSIBLE-v1`

For every `0<m<=1`, let

`rho_W(w)=1_[-1/2,1/2](w)`,

`rho_U(u)=1_[-m/2,m/2](u)`.

The `U` submeasure has mass `m` and cap one. Push the product finite measure forward by

`S=W^2+U^2`.

For every

`0<s<m^2/4`,

the full circle `w^2+u^2=s` lies in the rectangle. Polar coarea gives

`p_S(s)=int delta(s-w^2-u^2) dw du=pi`.

Hence

`boxed: ||p_S||inf >= pi for every m>0.`

Consequently there are no universal constants `C<infinity`, `gamma>0` such that every active cap-one square-carrier submeasure of mass `m` obeys an endpoint bound `C m^gamma` in this class.

The obstruction is not translation, support diameter, or tails. It is the exact endpoint geometry of two same-sign square singularities: the shrinking active mass is concentrated into a smaller radial window while the density height remains fixed.

## 6. Stronger obstruction: every fixed finite L^p norm can vanish

The same endpoint cannot be repaired by replacing the active `L^infinity` cap with an `L^p` collision-energy norm.

For `R>=2`, let

`f_R(u)=1_[-1/(2R),1/(2R)](u)+R^(-1)1_[2,R+1](u)`.

Then `f_R` is a probability density, `0<=f_R<=1`, and for every fixed finite `p>1`,

`||f_R||_p^p=1/R+(R-1)/R^p -> 0`.

Let `W` be independent Uniform`[-1/2,1/2]` and `U_R~f_R`. For

`0<s<1/(4R^2)`,

the circle `w^2+u^2=s` lies entirely inside the central height-one tooth and does not meet the remote tail. Therefore

`boxed: p_(W^2+U_R^2)(s)=pi.`

Thus no estimate depending on a positive power of `||f_U||_p`, for any fixed finite `p>1`, can replace the active cap-one endpoint uniformly over the target's laws. In particular, the `L^2` collision-energy improvement that is valid for a **linear slope bank** cannot be transplanted to an active quadratic square carrier.

For `p=2`,

`||f_R||_2^2=(2R-1)/R^2 -> 0`,

while the output density retains height `pi` near zero.

This precisely distinguishes two localization interfaces now available to B14 work:

- linear slope/Fourier interfaces can gain mass homogeneity from `L^2` convolution contraction;
- the same-sign quadratic Beta endpoint is an `L^infinity` endpoint on each active carrier and has no positive active-mass exponent.

## 7. Exact-target fragment-first barrier

Apply the newest fleet03/B14 theorem to the three-coordinate matrix

`A_* = [[2,1,0],[1,2,0],[0,0,-1]]`.

Its spectrum is

`spec(A_*)={3,1,-1}`,

so it lies exactly inside the owner target. For independent cap-one `W,U,Y`,

`Q=2W^2+2WU+2U^2-Y^2`

`=2(W+U/2)^2+(3/2)U^2-Y^2`.

The two active square coefficients have the same sign, with

`a=2`, `d=3/2`, `sqrt(ad)=sqrt(3)`.

Hence the partner's whole-law theorem gives

`boxed: ||p_Q||inf <= pi/sqrt(3) = 1.8137993642342178...`

for arbitrary cap-one `U`, including arbitrarily fragmented and unbounded support.

Now take

`E_N=union_{j=1}^N [4^j,4^j+1/N]`,

`f_(U_N)=1_(E_N)`.

This is a cap-one probability density. The whole-law certificate remains `pi/sqrt(3)`, independent of `N` and the exponentially growing gaps.

Change only the bookkeeping: split the active `U_N` law into its `N` tooth submeasures. Each tooth has mass `1/N`, but its **unnormalized cap is still one**. The finite-measure Beta compiler therefore gives the full

`pi/sqrt(3)`

certificate on every tooth. Summing those fragmentwise certificates yields

`boxed: N pi/sqrt(3).`

The underlying probability law did not change. Thus fragment-first endpoint payment can lose a factor `N`.

There is also a countably fragmented unbounded-support version. Put

`m_j=6/(pi^2 j^2)`,

`E=union_{j>=1}[4^j,4^j+m_j]`,

`f_U=1_E`.

Because `sum_j m_j=1`, this is a cap-one probability density with unbounded support. The whole same-sign theorem still gives `pi/sqrt(3)`. But each tooth submeasure again has cap one, so separate endpoint payment has certificate sum

`sum_j pi/sqrt(3)=infinity`.

This is a proof-interface obstruction, not a lower bound on the actual output density and not a QFORM counterexample.

## 8. Required fixed source applied to the same obstruction

The fixed required source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was freshly read through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Its completed Theorem A states: for a three-dimensional symmetric matrix all of whose eigenvalues have absolute value at least `sigma`, with arbitrary linear terms and independent cap-one coordinates,

`||p_Q||inf <= 6 sqrt(pi)/sigma`.

For the **same** matrix `A_*`, `sigma=1`. Therefore for every finite comb `U_N` and the countably fragmented unbounded comb above,

`boxed: ||p_Q||inf <= 6 sqrt(pi) = 10.634723105433096...`.

This independent completed-source inequality stays uniformly finite while the artificial fragment-first Beta certificate grows like `N` or diverges. The source theorem therefore confirms that the obstruction is to the localization proof interface, not to the conjecture.

On this exact chamber the newest partner is much sharper:

`||p_Q||inf <= min(pi/sqrt(3),6sqrt(pi)) = pi/sqrt(3)`.

## 9. Source-match audit

Before assigning a novelty label, I searched the current math repository for same-sign/subprobability/Beta localization terminology. The search found related finite-measure bilinear and Fourier compilers and older B14 Beta-named reports, but no exact source match for the active-carrier no-positive-mass-exponent statement above. A search miss is not a novelty proof, so the status here is only **supporting extension proved**, not a novelty claim.

The newest fleet03/B14 addendum is also respected: the definite physical-pair determinant bound is older fleet mathematics; the partner run's genuinely relevant interface is the arbitrary-overlap same-sign compiler.

## 10. Safe localization order

The result gives a sharp order-of-operations rule.

1. Aggregate each active square-carrier marginal at its original cap-one scale.
2. Pay the same-sign Beta endpoint only after that aggregation.
3. Arbitrarily localize/fragment/translate an independent environment afterwards; its finite-measure mass enters linearly and summation is zero-tax.
4. If the matrix reduction demands localization of an active square carrier itself, do **not** pay the Beta endpoint piecewise. Switch first to a mass-homogeneous mechanism that aggregates the carrier through a slope, volume, ridge, grouped bank, or another whole-law receiver.

This retains arbitrary translations, fragmented/unbounded supports, conditioning-generated affine terms and the absence of moments. No fixed-fragment or bounded-diameter shortcut is introduced.

## 11. Status

The full arbitrary-dimension QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This report proves essential boundedness only in the stated same-sign overlap chamber and a sharp localization obstruction for that proof interface. Full-target continuity remains separate and open.
