# PROB10-02 / R17 second idea-before-code — stationary cylinder-cocycle upper dual

This note supersedes the *method choice* in the earlier `20260920T1120Z_r17_forced_clear_smdp_idea_7d31.md` without deleting it. The forced-clear/bounded-imbalance proposal was checked against canonical ownership before code: its imbalance coordinate confines the alignment path to a fixed diagonal strip, so it collapses to the finite-width model already owned by P13 and already identified with Chia--Bundschuh's correlated finite-width model. P13 has now exactly certified widths through 6. Therefore R17 does not duplicate that route.

A second possible pivot, run-length/geometric regeneration, was also checked before code. P05 already owns exactly that renewal route and has an M-state source-valid certificate. R17 will not duplicate it.

The new nonduplicating route is a stationary *pathwise upper dual* directly on the iid-letter environment.

## A. Cylinder gradient dual

Let the two-sided environment be `omega=(X,Y)` with independent fair binary sequences and commuting shifts `T_X,T_Y`. The LCS grid is directed last passage with horizontal and vertical displacement reward 0 and a diagonal `(1,1)` step reward

`m(omega)=1{X_1=Y_1}`.

For a bounded cylinder potential `phi` and constants `c_X,c_Y`, impose the pointwise inequalities

`c_X + phi(T_X omega)-phi(omega) >= 0`,

`c_Y + phi(T_Y omega)-phi(omega) >= 0`,

`c_X+c_Y + phi(T_X T_Y omega)-phi(omega) >= m(omega)`.

Summing along *any* monotone LCS path from `(0,0)` to `(n,n)` makes the potential telescope and counts exactly `n` X-displacements and `n` Y-displacements. Hence

`LCS_n(omega) <= n(c_X+c_Y)+osc(phi)`

pathwise and therefore

`gamma_2 <= c_X+c_Y`.

For a cylinder of `k` visible X bits and `k` visible Y bits, all three inequalities reduce to a finite rational LP on `4^k` potential values, checked over all one-bit extensions. By X/Y symmetry one may average a certificate with its transpose and take `c_X=c_Y=c` without worsening `2c`.

This is not a finite-n simulation: a feasible rational LP point is already an arbitrary-length source-valid upper certificate with explicit error `osc(phi)/n`.

## B. Closed edge-cocycle relaxation

A scalar cylinder gradient may be too restrictive. The second attack is to introduce finite-state edge increments `B_X,B_Y` on the de Bruijn extension graph, impose exact plaquette closedness

`B_X(omega)+B_Y(T_X omega)=B_Y(omega)+B_X(T_Y omega)`

and zero-mean/gauge constraints, and dominate the three local LCS moves by deterministic slopes plus these increments. This searches finite stationary cocycles before insisting they have a short scalar potential representation. If closedness forces exactness on the finite extension graph, that is an exact obstruction; if not, it is a strictly richer dual.

## C. Finite-memory approximation / obstruction

Try to construct a `k -> k+1` lift and a quantitative truncation theorem. Desired form: if `U_k` is the optimum cylinder dual, prove `gamma_2 <= U_k <= gamma_2+epsilon_k` with an explicit `epsilon_k -> 0`. A candidate proof route is to start from finite-box dynamic-programming values, average translated local increments, and quantify only boundary defects. If a bounded cylinder corrector cannot approximate the unrestricted stationary cocycle, identify the exact cohomological obstruction rather than silently claiming convergence.

The immediate computation will only occur after these ideas are frozen here. It will (i) solve small cylinder LPs numerically to discover structure, (ii) rationalize a candidate and verify every local inequality exactly, and (iii) test the edge-cocycle closure and the first truncation identities. Source endpoint movement is claimed only if the resulting exact upper is below the newest P02 `U_new`; otherwise it is separate mechanism progress. Status remains OPEN/PARTIAL.