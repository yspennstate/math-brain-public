# Adversarial audit: finite critical-grid entrance can change the macroscopic law

## Verdict and scope

The proposed negative-correlation example is valid and robust. More strongly, in the entire strict mixed-sign cone for a two-input Gram matrix with `rho<0`, the eventual endpoint selector is explicit. For the nested grids `gamma_big=1` and `gamma_small=0.1`, the coarse-grid surviving endpoints include all fine-grid surviving endpoints, with strict inclusion on an open positive-intensity set. This monotonicity converts a separation under the natural coupling into a separation of the **marginal output path laws**, provided one proves the local residual-coupled entrance lemma below. It does not imply full global uniqueness, or arbitrary-gamma monotonicity.

The earlier `MACRO_COMPACTNESS.md` pays output tightness and uniform small-endpoint control, while `BOUNDARY_GRID.md` pays any fixed number of entrance steps. The bridge needed here is much narrower than a global selector: only a short random interval on which the residual remains in one open cone.

## Exact selector and an important nonmonotonicity

Let `G=[[1,rho],[rho,1]]` with `rho=-k`, `0<k<1`. Freeze `r1<0<r2` and take `z>0`. Write `a=-z r1>0`, `b=z r2>0`. The sector velocities per boundary time are

| sector | velocity |
|---|---|
| `--` | `(0,0)` |
| `+-` | `(-a,ka)` |
| `-+` | `(-kb,b)` |
| `++` | `(-(a+kb),ka+b)` |

Thus `--` is dead, `-+` is invariant and escaping, and every `++` orbit reaches `-+`. For a `+-` mark `(x,y)`, `x>0>y`, set `Nx=ceil(x/(gamma a))`. The exact frozen Euler selector escapes iff

`y+gamma*k*a*Nx > 0`,

with equality dead under the strict-positive gate convention. Equivalently, if `tx=x/a` and `ty=-y/(ka)`, escape iff `gamma ceil(tx/gamma)>ty`. On generic marks, this is the same as `ceil(ty/gamma)<=ceil(tx/gamma)`. The continuous Filippov selector escapes iff `y+kx>0` and dies iff `y+kx<0`. Consequently Euler may escape by overshooting the dead corner in one step.

At `rho=-1/2,z=1,r=(-1,1),(x,y)=(.14,-.12)`, continuous flow dies after hitting `(0,-.05)`. `gamma=1` gives `(-.86,.38)` and escape; `gamma=.1` gives `(.04,-.07)` then `(-.06,-.02)` and death. All margins are strict, so small perturbations preserve the result. The escape set for this mark is `gamma in (.24,infinity) union (.12,.14)`: `gamma=.13` escapes although `gamma=.2` dies. **Do not claim generic monotonicity in gamma.**

For the particular nested pair `1=10*0.1`, the ceiling-to-next-grid-time at scale 1 is at least that at scale 0.1. Therefore an escaping positive-`z` `+-` mark at `.1` also escapes at 1. The same inclusion holds for `z<0`, after swapping the two coordinates and their signs: its only nonzero eventual output ray is the first coordinate. For `z>0`, the only nonzero eventual output ray is the second coordinate. All other initial sectors give the same classification at both grids. These assertions hold for every generic mark in the strict cone, not just the displayed box.

## Local residual-coupled lemma to prove

Fix `rho<0`, `gamma>0`, and an initial residual `r0` with `r01<0<r02`. For any subsequential macroscopic limit in `MACRO_COMPACTNESS.md`, there is an almost surely positive, possibly random time `delta` such that `r1(t)<0<r2(t)` on `[0,delta]`. For each retained Poisson atom, the frozen-`r0` grid orbit has a finite terminal step with strict sign margins, except on a null set of threshold equalities. Fixed-step convergence from `BOUNDARY_GRID.md` puts its finite-width counterpart into the same terminal sector. While the residual stays in the cone, these sectors are invariant: `--` gives zero updates exactly; positive-`z` `-+` moves further left/up; negative-`z` `+-` moves further right/down. The uniform `W/a -> z` bound in `MACRO_COMPACTNESS.md` preserves the weight sign. Thus each retained endpoint has, after a transient of `O(1)` boundary steps and hence `o(1)` physical time, either zero scaled path or

`q_z(t) = z G diag(0,1) integral_0^t r(s)ds` for escaping `z>0`,

`q_z(t) = z G diag(1,0) integral_0^t r(s)ds` for escaping `z<0`.

There are countably many atoms and their terminal-step counts are not uniformly bounded. Apply this first to finite cutoffs, then use the already-proved uniform `O(sum_small z^2)` output bound to remove them. It yields the exact local output/residual equation

`r(t)=r0-[C+diag(M1_gamma,M2_gamma)] integral_0^t r(s)ds`,

where `M2_gamma=sum_{z>0} z^2 1{frozen gamma orbit escapes}` and `M1_gamma=sum_{z<0} z^2 1{frozen gamma orbit escapes}`. Both sums are finite almost surely. In particular every subsequential limit has the same right derivative

`f'(0+)=[C+diag(M1_gamma,M2_gamma)] r0`.

This formulation is **local**. The residual may leave the cone later, and nothing here selects the subsequent face/corner history. It also does not assert convergence of pre-step tangent matrices in `L1`.

## Turning pathwise separation into a law statement

For `gamma=1` and `.1`, nested grids give `M2_1 >= M2_.1` and `M1_1 >= M1_.1` under the same primitive `(F,C,N)` on the whole strict residual cone. The robust target-mark box in `f01_entrance.md`, with `z` near 1 and projected mark near `(.14,-.12)`, has positive Poisson intensity. The initial residual `r0=y-F` lies near `(-1,1)` with positive probability for every fixed label vector, and it is independent of `N`. Hence `M2_1>M2_.1` with positive probability on this observable residual event. The second-coordinate initial output slopes satisfy

`f2_1'(0+) - f2_.1'(0+) = r02 (M2_1-M2_.1) >= 0`,

strictly with positive probability there. The common `C r0` term cancels. Because `r0=y-f(0)` is observable from the output path, any bounded strictly increasing function of `f2'(0+)`, multiplied by the indicator of a compact residual subcone, distinguishes the joint/output path distributions. The derivative is measurable as the limit of forward difference quotients. This fixes the usual flaw that positive-probability separation under a coupling alone does not imply distinct marginals.

The Poisson square sum is finite almost surely but generally has infinite expectation; avoid comparing raw expected slopes. Use a bounded monotone test such as `arctan`. No event excluding all other large atoms is needed because the nested-grid selector is monotone atom by atom.

## Checks against previous results and remaining attack points

1. The example is a corner-overshoot effect with no attracting sliding face. Importing the positive-correlation Schur slide is unnecessary and would obscure the mechanism.
2. The finite-grid theorem alone does not identify `M_gamma`: its fixed-step horizon must be combined with the macro compactness bounds and terminal-sector invariance. Explicitly show this bridge in any proof.
3. A local random interval is enough to identify the initial slope. A full network convergence or a globally unique selected inclusion is not needed for the step-size nonuniversality claim.
4. The `gamma=1` versus `.1` monotonicity uses exact grid nesting. It fails for general pairs; the same mark has `.13` escape and `.2` death.
5. Projected stable marks have a positive density because the fixed input matrix has rank 2. The chosen Poisson mark box and residual box therefore have positive probability. Conditioning on `C` is unnecessary for the slope-ordering proof.
