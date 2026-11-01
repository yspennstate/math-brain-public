# R15 idea note — smooth the last K-floor and isolate a boundary coefficient

Date: 2026-09-20 UTC

Status: **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. This is retained F0111 screening only. It does not reopen Burdzy–Scheutzow Problem 7.2 / I0076.

Immediate predecessor: `runs/R15/20260920_0822Z_successor_screen_f0111_adaptive_ray_r103z.md`.

Methods for this run: **#6 deform to a solvable point, #11 dualize, #24 find the extremal object**. The preceding triple was #5/#13/#30.

## New route before repository validation code

The previous run reduced the remaining dimension-30 two-level F0111 mechanism (`N=|K|=12,13`) to a two-scalar necessary inequality, but its exact K-block entropy term is still written with a floor `m_K=floor((U_K-N)/(c_K-1))`. That creates many artificial scalar subcells as `c_K -> 1`.

Remove the floor before doing any interval work. For `f(v)=v log v`, convexity on `[1,c]` gives the secant inequality

`f(v) <= ((v-1)/(c-1)) c log c`.

Thus if `1 <= v_j <= c_K` and `sum_j v_j=U_K=N+eta_K`, then

`sum_j v_j log v_j <= eta_K c_K log(c_K)/(c_K-1)`.

After dividing by `S`, this yields a smooth K moment roof

`K_sec = (U_K-N)/S * c_K log(c_K)/(c_K-1)`.

It is weaker than the exact capped-convex extreme point but has no floor and is sharp to first order as the K-excess tends to zero. Hence every survivor must satisfy the single smooth inequality

`Gamma_sec(delta,s) := log S - Ebar_K - K_sec - H_J^* <= 0`,

with the same adaptive ray and J extremizer from r103z.

The next question is not another matrix estimate: determine the sign of this smooth two-variable function. A first analytic attack should deform to `s=0`, compute `lim Gamma_sec/s` uniformly on the limiting feasible d-intervals, and use the resulting positive boundary margin to reduce any eventual exact interval certificate to a compact strip bounded away from zero.

No repository checker has been written for this route at the time of this note.