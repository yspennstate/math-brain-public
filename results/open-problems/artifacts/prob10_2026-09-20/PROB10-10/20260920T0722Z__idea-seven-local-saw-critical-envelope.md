# PROB10-10 mathematical idea before code — seven-local SAW critical-envelope optimization

Frozen model: nearest-neighbor undirected FPP on Z^2 with iid Exp(1) physical edge weights. Canonical parent remains `operations/claims/PROB10-10.md`; the full-source metric is `c_*` for `Delta_12=2 mu(e1)-mu(1,1)`, currently `c_*=0`. The newest source-valid restricted cone available before this attack is P04's seven-column carry-lane theorem, `|y| >= (851/500)x = 1.702x`, using the canonical six-local-SAW endpoint counter and axis upper bound `mu(e1)<=a_7=0.6049757734885347...`.

This run does not resume the retired R08 independent-detour/fixed-corner route. It keeps the dependence-controlled block theorem as a consumed input and changes the oblique counting side.

## Attack A — B16/B24: seven-local self-avoidance plus direct extremal Perron optimization

A globally self-avoiding path has every consecutive seven-step window self-avoiding. Hence the seven-local shift is still a rigorous finite-memory superset of all possible positive-weight geodesics, but is strictly smaller than the six-local shift. For tilted step weights `A,A^{-1},B,B^{-1}`, let `r_7(A,B)` denote the Perron radius of the seven-local transfer matrix. If an exact Collatz vector certifies `M z <= r z`, then for every endpoint `(an,bn)` the path count obeys `N_l <= K r^l A^{-an} B^{-bn}`.

Instead of freezing the preceding Chernoff parameter, use the critical envelope obtained by taking `s downarrow r-1`:

`L_*(rho) = [log A + rho log B]/(r-1)`.

Combined with `mu(e1)<=a_7`, this yields a reflected strict-triangle defect whenever `L_*(rho)>a_7`. The critical slope is

`rho_*(A,B,r) = ((r-1)a_7-log A)/log B`.

The finite computation should therefore optimize this source-relevant quantity directly, not merely reduce `r`. A successful candidate will be promoted only after an exact rational Collatz inequality and an exact rational finite-scale Chernoff/Taylor certificate.

## Attack B — B11: dual cut/barrier certificate

Try to lower-bound the oblique time constant by a weighted family of dual cutsets crossing every path. This would remove path entropy entirely. The obstacle to test is whether a deterministic or finite-state random barrier can be chosen so that its minimum Exp(1) crossing cost has a positive density after accounting for shared edges. If the dual optimization collapses to a zero-density cheapest cut, record that obstruction rather than inventing a conditional theorem.

## Attack C — B5/B18: Busemann interpolation between axis and an oblique support

Use an axis reconstructed Busemann cocycle and a second support cocycle, interpolate their residual metrics, and ask whether a quantitative policy-disagreement density can be forced from the explicit outer-cone residual barrier already proved by P20. The exact missing lemma is a lower bound on the density of edges where the two support policies cannot simultaneously have zero residual. If only qualitative disagreement is available, do not promote it to a strict-triangle constant.

## Negation test for Attack A

Two failure modes will be tested before any theorem claim: (i) seven-local memory may fail to improve the optimized critical slope after its larger state-space Perron cost is accounted for; (ii) the floating Perron vector may have too little slack to rationalize. The global-SAW inclusion itself has a direct all-length proof: every seven-edge subpath of a global SAW visits eight distinct vertices.

Only after a candidate moves the rigorous cone boundary will code/checker archival follow.