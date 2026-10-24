Model requested: GPT-6 maximum. Applied model/effort metadata: **UNVERIFIED**; this runtime exposes no authenticated selector receipt.

# PROB10-10 idea before code — exact Richardson evaluation of exponential strip certificates

Frozen source target: nearest-neighbor **undirected** FPP on `Z^2` with iid `Exp(1)` physical-edge weights. The canonical source-facing checkpoint remains

`Delta_12 = 2 mu(e1) - mu(1,1) > 0`,

with retained rigorous axis lower bound `mu(e1) >= b = 0.3002823`; hence it is enough for this checkpoint to prove `mu(1,1) < 0.6005646`. Full ADH strict convexity would still remain open.

The preceding incomplete asynchronous-carry idea (`20260920T1236Z__idea-finite-state-asynchronous-carry.md`) removes the per-block synchronization loss by carrying the whole antidiagonal arrival profile and proves a conservative finite-state Bellman architecture with an explicit `O(1/N)` finite-to-infinite correction. Its remaining proof burden is a rigorous finite transition/expectation certificate. This note proposes a different exactification that exploits the **specific Exp(1) law**, rather than generic interval quadrature.

## Exact exponential block evaluator

For a finite graph `G=(V,E)`, a source `o`, a terminal set `A`, and iid `Exp(1)` edge weights, let `q_G=E T_G(o,A)`. Couple FPP to Richardson infection growth. Before `A` is hit, let `S` be the infected vertex set and let

`b(S)=#{e={x,y} in E: x in S, y notin S}`,

`m_S(v)=#{x in S: {x,v} in E}` for `v notin S`.

Because exponentials are memoryless, conditional on the current infected set, all live boundary-edge residual clocks are independent `Exp(1)`. Therefore the next infection time is `Exp(b(S))`, and the next infected vertex is `v` with probability `m_S(v)/b(S)`. If `u(S)` is the expected remaining time to hit `A`, then

`u(S)=0` when `S cap A != empty`,

and otherwise

`u(S)=1/b(S) + sum_{v notin S} [m_S(v)/b(S)] u(S union {v}).`

The recursion is triangular in `|S|`; for a finite graph it determines `u` uniquely. With rate-one exponentials all coefficients are rational, so `q_G=u({o})` is an **exact rational number**. There is no exponential-tail truncation and no numerical integration error.

## Monotone certificate consequence

If `H` is any connected subgraph of a finite strip block `G` containing the source and at least one terminal, then pointwise `T_G(o,A)<=T_H(o,A)`, so

`q_G <= q_H`.

Thus a tractable edge-deleted subgraph whose exact Richardson recursion yields `q_H/L < 0.6005646` would be a rigorous finite block certificate. Combined with the already-proved moving-centered diagonal-block compiler, it would imply `mu(1,1)<0.6005646`, hence a positive `Delta_12`. The finite-to-infinite error in that compiler is explicit: for `N` iid fresh `s=x+y` bands, if `xi` is the selected terminal transverse offset with `E xi=0` and `v=E xi^2`, then the final fresh zig-zag correction gives

`E T(0,(NL,NL))/(NL) <= q_G/L + sqrt(v)/(L sqrt(N))`;

letting `N->infty` leaves exactly `mu(1,1)<=q_G/L`.

The new exactification does **not** by itself cross the threshold: the full width-40 blocks seen numerically are far too large for direct subset-state enumeration. Its purpose is to remove the previous analytic tail/integration obligation and isolate the remaining obstruction as state complexity / certificate design.

## Negation-first tests before any proof claim

1. Execute the exact Richardson recursion on tiny rotated strip blocks and compare exact rational values against independent simulation. This tests the memoryless recursion itself.
2. Re-run the asynchronous boundary-carry screen at width `W=40`, with independent replicas rather than a single correlated trajectory, and compare undirected versus a directed-within-band control. If the undirected mean is not below `0.6005646`, abandon this lane.
3. Treat every Monte Carlo value only as a falsification/sizing screen. No sampled estimate changes `c_*`.

## Three materially different live approaches

1. **Asynchronous carry + conservative upward projection.** Keeps dependence exactly across fresh bands; if a finite Bellman supersolution is certified with `lambda/L<0.6005646`, it proves the axis/diagonal strict triangle.
2. **Exact Richardson / edge-deleted finite block certificate (this note).** Uses exponential memorylessness to replace tail quadrature by exact rational recursion; remaining issue is finding a tractable subgraph/state aggregation with enough speed.
3. **P20 true-geodesic Busemann residual/co-calibration route.** The newest P20 work forces linearly many U-backtracks on the actual axis geodesic and, under flatness, forces almost all to have tiny diagonal residual. Its unpaid step is to rule out positive-density co-calibration; it is geometrically different from strip optimization.

The first-moment SAW route remains retired for the diagonal because the monotone-path barrier already proved it cannot reach the current checkpoint at the present axis cap.