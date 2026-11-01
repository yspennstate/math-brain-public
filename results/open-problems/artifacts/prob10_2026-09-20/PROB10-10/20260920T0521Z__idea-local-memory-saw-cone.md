# PROB10-10 idea before code — finite-memory self-avoiding superset

Runtime model available to this run: **GPT-5.6 Sol; reasoning level UNVERIFIED — not GPT-6 maximum, and no stronger runtime claim is made.**

Frozen model: nearest-neighbor **undirected** FPP on `Z^2` with iid `Exp(1)` physical-edge weights, with time constant norm `mu` in the usual `T(0,nv)/n -> mu(v)` normalization.

## Consumed newest state

The canonical source remains Auffinger–Damron–Hanson Question 4. The newest owner report before this run is `runs/prob10_2026-09-20/PROB10-10/20260920T0416Z__cone-tilt-15over8-extension.md`. The newer neighboring P04 report `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T04-47-14Z__ladder8-cone1814-transfer.md` supersedes its restricted-cone baseline by proving `mu(e1) <= A8 = 0.6303807261851404...` and a reflected strict-triangle defect for `|y| >= (907/500)x`. P20's newest `2026-09-20T05-09-30Z__axis-busemann-cone-and-policy-separation.md` gives a Busemann residual formulation but leaves the canonical axis/diagonal gap `c_*` at zero.

Thus the source-level restricted-direction baseline for this run is **slope 907/500 = 1.814**, while the canonical axis/diagonal milestone remains `c_*=0`.

## New mechanism

Do **not** keep the old non-backtracking path-count transfer unchanged. Instead count self-avoiding competitors through a strictly smaller finite-memory superset.

A globally self-avoiding path has the property that every block of four consecutive steps is itself self-avoiding. Let `S4` be the finite set of four-step direction words whose five visited vertices are all distinct. A direction sequence is `4-local-SAW` if every consecutive four-step word belongs to `S4`. Every genuine self-avoiding path is `4-local-SAW`, but the converse need not hold. Therefore an exact weighted transfer matrix on `S4` gives an upper bound on the number of genuine self-avoiding competitors, without assuming independence between blocks and without excluding any geodesic.

Give directions `(E,W,N,S)` multiplicative tilt weights `(A,A^{-1},B,B^{-1})`. For `s,t in S4`, allow a transition exactly when the last three directions of `s` followed by the last direction of `t` form a word in `S4`; weight the transition by the new direction weight. If a positive vector `z` and rational `r` satisfy `Mz <= r z`, then the weighted count of length-`m` local-SAWs is at most `K r^m` with explicit startup constant `K`. For an endpoint displacement `(an,bn)`, every path has the same tilt product `A^{an}B^{bn}`, hence the number of genuine self-avoiding paths of length `m` is at most `K r^m A^{-an}B^{-bn}`.

Combining this with the exact `Gamma(m,1)` lower-tail Chernoff bound for the sum of `m` iid exponentials should improve the oblique lower bound while keeping the P04 length-8 axis upper bound. The exact target is to certify at least

`rho0 = 361/200 = 1.805`, `c = 63039/100000`,

so that `mu(a,b) >= c a` whenever `b/a >= rho0`. Since P04 gives `mu(e1)<=A8<c`, this would imply

`mu(a,b)+mu(a,-b)-mu(2a,0) >= 2(c-A8)a > 0`

throughout the larger cone `|b|/a >= 1.805`.

The finite-to-infinite obligation is not optional: derive an explicit `C<infinity` and `beta<1` such that

`P(T(0,n(a,b)) <= c a n) <= C beta^(a n)`

uniformly over the cone, and combine it with the length-8 axis block to obtain a finite expected reflected-triangle residual error at scales with `an` divisible by four.

## Negation test to perform

The critical claims to try to falsify before promotion are:

1. every genuine self-avoiding path maps to the finite-memory automaton (prove directly and exhaustively check short words);
2. a positive exact Collatz certificate `Mz<=rz` exists with `r<1+s` for rational tilt parameters;
3. the resulting exact Chernoff base at `rho0=361/200` is strictly below one, preferably below a simple rational `beta_hat<1`;
4. startup lengths `m<4` are covered by the same global constant `K` rather than silently discarded.

## Three materially different attacks compared this run

1. **Finite-memory self-avoiding superset (primary, new):** replace the non-backtracking automaton by the four-step local self-avoidance automaton. This is a dependence-safe combinatorial strengthening of the lower-bound compiler.
2. **Busemann policy disagreement (P20 route):** potentially closer to global curvature, but the current result has no quantitative lower bound on the frequency/energy of policy disagreement that survives unrestricted bypasses. Use it only if a new quantitative density estimate appears; do not relabel its conditional interface as strict convexity.
3. **Longer axis ladder / block optimization (P04 route):** improves the axis support but is already independently owned by P04 and becomes computationally expensive. This run consumes the proved length-8 value and does not duplicate its infection recursion. The nonduplicating opportunity is to improve the oblique path-count side instead.

A successful run remains **PARTIAL**: even slope 1.805 leaves a large unproved angular sector including the axis/diagonal pair.