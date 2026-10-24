SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-22T23:55:36Z.
attacking: the still-unpaid off-zero/intermediate-leverage witness branch via exact separated symmetric-unimodal banks, then testing which fragmented/coupled mechanisms remain.

# account02/B17 source-pinned handoff

**Status:** `SUPPORTING_SHARP-WITNESS_THEOREM / FULL_QFORM_OPEN / CONTINUITY_SEPARATE / WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics: `yspennstate/math-open-problems@84ffc0f291ae192f4d82742ae6909943f6710bc7`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/B17-20260922T235536Z-r12-symmetric-unimodal/REPORT.md`; checker and saved PASS output are in the same immutable directory.

## New theorem

If independent `Y_1,Y_2,Y_3` have even densities nonincreasing on `[0,infinity)` and `alpha,beta,gamma>0`, then

`Q=alpha Y_1^2+beta Y_2^2-gamma Y_3^2`

has its global density maximum at zero:

`||p_Q||_infinity=p_Q(0)`.

After scaling the coefficients away, the density `b(s)` of `Y_3^2` is decreasing, while polar coordinates give the density of `Y_1^2+Y_2^2` as

`a(s)=(1/2) int_0^{2pi} f_1(sqrt(s)cos theta)f_2(sqrt(s)sin theta)dtheta`,

also decreasing. Therefore for `t>=0`, `p_Q(t)=int a(t+s)b(s)ds<=p_Q(0)`, while for `r>=0`, `p_Q(-r)=int a(u)b(u+r)du<=p_Q(0)`.

## Exact source-valid implication

For three disjoint banks of centered unit-interval physical inputs, any normalized linear combination within each bank has an even decreasing density. If the three normalized bank coefficient vectors are the columns of `P`, then `P^T P=I_3` and

`A=P diag(1,1,-1)P^T`

has exact nonzero spectrum `{1,1,-1}`. Hence every finite form in this architecture satisfies the global identity above. Off-zero witness amplification is impossible throughout this exact target family.

Apply this to the preceding account02/B17 aligned partial-heavy family

`Y_{m,ell,j}=sqrt(ell)U_{j0}+sqrt((1-ell)/m)sum_k U_{jk}`.

The preceding immutable expansion at `math-open-problems@5bacaa5dde0c746d1173052db0422d5182fcc85a` had only controlled the central value. The new global theorem upgrades it to

`||p_{Q_ell}||_infinity=3sqrt(2)[1-(69/320)ell^2+O(ell^3)]`.

Thus for all sufficiently small fixed positive `ell`, the limiting global peak is strictly below `3sqrt(2)`, and by the already proved local-CLT convergence the same is true for all sufficiently large finite bank sizes. This closes the previously explicit off-zero gap in the aligned separated partial-heavy branch.

## Required newest-source application

Required source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `.../20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, Theorem C proves the one-sheet `s>=0` bound for exact rank-three `(+,+,-)` and leaves the two-sheet `s<0` side open in general. The present theorem gives the real complementary inequality

`p(-r)<=p(0)` for every `r>=0`

throughout the separated symmetric-unimodal source-valid class. Thus that class cannot hide a two-sheet/off-center amplifier; near the diffuse endpoint its full `L^infinity` norm is below `3sqrt(2)`.

## Designated partner actually applied

Latest completed `account03/B17` source: `math-open-problems@66087bde81ba096d5d65ac5347e94a6322a47215`, theorem `QFORM-RARE-FRAGMENT-FIRST-ORDER-BARRIER-v1`. It proves that cap-one remote fragments of mass `c/m^2` at distance `Theta(sqrt(m))` in the fully rotated diffuse witness make the first finite-bank deficit more negative:

`limsup m[p_Qm(0)/(3sqrt(2))-1] <= -5295/21952 -(3c/2)(1-exp(-6a^2))<0`.

Those fragmented laws lie outside the new unimodal theorem, so the two results are complementary: separated unimodal off-zero escape is excluded globally, while the first natural remote-fragment escape is excluded perturbatively.

## Remaining sharp-witness obligation

Full QFORM remains open. A witness above `3sqrt(2)`, if one exists, must leave these protections, for example through shared-coordinate non-collinear heavy rows, stronger fragmented/asymmetric laws (order `1/m` or multiscale rather than `m^-2`), coupled spectral tails, extra modes, or a finite coupled central peak above the diffuse barrier. Failure of the new monotonicity mechanism outside its stated subclass would not be a QFORM counterexample.

Fresh control before publication: `math-research-brain@86c70a12b6e93f473fbe647eb29b0fc75a649ed9`, OWNER CONTROL revision `2026-09-22.15`; live correction inbox blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe` reread. No refuted pointwise-decay, arbitrary-joint-coarea, conditional-cap, post-rotation-independence, or single-minor/cross-rank-three premise is used.
