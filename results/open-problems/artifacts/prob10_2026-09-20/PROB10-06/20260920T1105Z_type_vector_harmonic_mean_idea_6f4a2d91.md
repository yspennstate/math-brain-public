# PROB10-06 idea before code — type-vector harmonic-mean reciprocal recursion

Runtime metadata available to this worker: model family **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is unavailable, so reasoning level is **UNVERIFIED**. GPT-6/maximum was requested in prompt text only and is not claimed.

Parent source remains the Lyons–Pemantle–Peres speed-monotonicity conjecture on supercritical Galton–Watson trees **without leaves**: `P(nu=0)=0`, `m=E nu>1`. In outward child-bias `beta`, larger `beta` pushes away from the root and the conjecture asks increasing speed for `beta>1/m`. I use reciprocal parent-bias `lambda=1/beta`, so larger `lambda` pushes toward the root and the target sign is decreasing speed on `0<=lambda<m`.

The required immutable R02 handoff is already preserved at `runs/R02/20260920T0005Z_owner_refocus_handoff_I0095_to_PROB10-06_4d8c2a71.md`; historical intake `P0066` remains attempted-unsolved. This run keeps the delimited no-leaf adjacent family `P(nu=2)=1-p, P(nu=3)=p` and does not overwrite P01's minimum-one nonadjacent route, NM13-05's `{3,4}` route, or P03's terminal-critical/coupling routes.

Immediate own checkpoint: `runs/prob10_2026-09-20/PROB10-06/20260920T1112Z_reciprocal_jensen_cross_lambda2_71pct_7f3c2a91.md`. It proves, among other things, all `p` through `lambda=1.85527`, `p>=3/4` through `lambda=2.07`, and `p>=71/100` through `lambda=2.0021`, using the scalar inverse-escape bound `E(1/B)<=1/[1-lambda E(1/nu)]` plus reciprocal Jensen.

## Attack A (new primary route): keep the reciprocal moment vector by child type

Write `Z=1/B`. The escape recursion `B=S/(lambda+S)` becomes

`Z = 1 + lambda H_n(Z_1,...,Z_n)`,

where

`H_n(z_1,...,z_n) := 1/(1/z_1+...+1/z_n)`.

The harmonic-sum map `H_n` is coordinatewise increasing and jointly concave on `(0,infinity)^n` (equivalently, the harmonic mean is concave). For the `{2,3}` law define conditional reciprocal means

`x_k := E[Z | nu=k]`, `k=2,3`.

Condition first on the child offspring types `R_i in {2,3}` and then use Jensen:

`x_k <= T_k(x_2,x_3)`,

`T_k(y_2,y_3) := 1 + lambda E[ H_k(y_{R_1},...,y_{R_k}) ]`.

This retains the heterogeneity that the scalar Cauchy bound discards.

For a parameter corner `(L,P)` with `lambda<=L` and `p>=P`, start from the old scalar supersolution

`D=1-L(3-P)/6`, `M=1/D`,
`y_2^(0)=1+L M/2`, `y_3^(0)=1+L M/3`.

Because `E[y_R^(0)]=M` and `H_k(z)<=k^{-2} sum_i z_i`, one has `T_{L,P}(y^(0))<=y^(0)`. Since `T` is monotone, the exact rational iterates

`y^(r+1)=T_{L,P}(y^(r))`

form a decreasing chain of supersolutions. Also `y_2^(r)>=y_3^(r)`, and for such vectors `T_{lambda,p}` increases with `lambda` and decreases with `p`; therefore every corner iterate is a valid supersolution on the whole rectangle `lambda<=L, p>=P`.

Consequently

`E[1/B | nu=k] <= y_k^(r)`, hence `E[B | nu=k] >= d_k^(r):=1/y_k^(r)`.

Feed these sharper type-dependent denominators into the reciprocal-Jensen kernels already proved in the preceding run. This should improve both the annealed `U=-B'` contraction and the Aidekon score bound, while preserving an explicit finite-depth truncation rate from the same `rho<1` estimate.

Targeted source-level gains to test after the proof is written:

1. extend `p>=3/4` beyond the current `lambda=2.07`, with a tentative analytic target near `lambda=2.14`;
2. lower the mixture threshold for a genuine crossing of `lambda=2`, tentatively from `p>=0.71` to about `p>=0.68` while keeping an endpoint strictly above `2`.

These are only targets until exact rational certification succeeds.

## Attack B (different route): exploit the exact harmonic-mean deficit

For two children,

`H_2(z_1,z_2)=(z_1+z_2)/4 - (z_1-z_2)^2/[4(z_1+z_2)]`.

Thus the scalar Cauchy/Jensen step loses an explicit nonnegative variance term. I will test whether offspring-type randomness alone gives a quantitative lower bound on this deficit. Conditioning on child types shows that the type-vector Jensen bound in Attack A already captures the deterministic between-type part. Any further strict gain would require a **within-type** lower variance bound for `Z|nu=k`. Such a bound cannot be assumed and vanishes at the deterministic endpoint `p=1`; if no source-valid positive lower variance can be proved, this route is blocked exactly at that missing ingredient.

## Attack C (different route): terminal-critical splice rather than stronger low/intermediate estimates

P03-A's current corrected theorem `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0906Z__sharp-von-bahr-esseen-restores-all-mean-third-moment-terminal-theorem.md` proves existence of a terminal interval below `lambda=m` under `E nu^3<infinity`. For `{2,3}` this applies. I will check whether its constants can be made explicit enough, without taking over that owner, to overlap the intermediate interval above and thereby close the **entire bias interval for a restricted random two-point family**. The obstruction to be recorded if this fails is quantitative: the P03 theorem presently gives existence after several `delta_0` shrinkages with constants `C_i` not numerically instantiated. A splice is rigorous only after those constants are exposed; existence of some terminal neighborhood cannot be used as if it overlapped `lambda=2.14`.

No finite-tree simulation will be counted as a proof, and no restricted-family gain will be called source-wide closure.