# R17 PROB10-02 — idea before code: centered-boundary/path tradeoff

Model request: GPT-6 maximum reasoning. No authenticated model/effort telemetry is exposed here; actual reasoning metadata therefore remains UNVERIFIED.

Target remains the genuine iid-uniform binary Chvatal–Sankoff constant. The same fresh Y-bit is compared with all active X-bits in each strip update; independent Bernoulli matching is not used.

Newest R17 dependency is `runs/prob10_2026-09-20/PROB10-02/20260920T0742Z_r17_reward_flux_span_3c71.md`. It proved a pathwise one-gradient-defect reward discrepancy at most 1 and a one-raw-symbol reward discrepancy at most 1, hence an arbitrary-state cumulative-reward span at most `2m` for strip length `m=2w`. It left the stronger `m`-span as small-width evidence only. P02 owns the covering/cone upper-bound route and P13 owns reset-language/boundary synchronization; this run stays on R17's correlated reward/history route.

The source interval is not changed by an auxiliary strip theorem. Before this run, `L=99083249/125000000=0.792665992` and the newest recovered repository-internal upper endpoint is P02's four-band endpoint `U_R`; the tracked source width is `U_R-L`.

## Attack A — centered boundary values plus path exposure

For a formal state `s=(x,g)`, let `V_0=0`, `V_k=sum_{i<=k}g_i`, and center the initial boundary at the reward cut `w=m/2`:

`A_k = V_k - V_w`.

For two gradients `g,h`,

`|A_k(g)-A_k(h)| <= |k-w|`,

because only gradient coordinates strictly between `k` and `w` survive centering. The raw-window part should not be paid independently by all `m` bits: in the unrolled strip-DP representation, a path entering from boundary index `k` can use only a complementary number of initial-window symbols before those symbols leave the moving strip. The desired deterministic inequality is therefore

`boundary discrepancy at k + initial-symbol discrepancy usable from k <= m`,

uniformly over every monotone path. If this path-count statement is correct, taking maxima over paths gives

`|R_N(s)-R_N(t)| <= m`

for every common future source word and every horizon `N`.

This would halve the previously proved finite-to-stationary transfer from `2m` to `m` without any mixing-time argument.

Critical falsification target before claiming anything: derive the exact set of initial raw symbols that a path starting at each boundary index can consume. The bookkeeping can fail if a path can enter on one side of the central cut and later collect raw symbols from both sides.

## Attack B — exact counterexample search for the proposed `m`-span

Before investing in a proof, search exactly at `m=6` for a common future word and two formal states with cumulative reward difference `>m`. Do not enumerate all `4096^2` pairs naively. Use the deterministic transducer and dynamic programming over reachable pair states while keeping only extremal accumulated discrepancies for each pair. Seed strategically with pairs that maximize centered boundary discrepancy and opposite raw words; then broaden if needed. Any counterexample kills Attack A and becomes the obstruction result for the run.

## Attack C — finite-horizon variational payoff if Attack A survives

If the `m`-span is proved, then for the unique recurrent strip class and any reference state `s`, the average-reward bias span is at most `m`, giving the one-state exact bracket

`E_s R_N/N - m/N <= gamma_w <= E_s R_N/N + m/N`.

Explore whether an exact sparse forward distribution for a width not previously feasible can turn this into an actual lower-endpoint improvement. A finite computation counts as source progress only if its proved bracket exceeds `0.792665992`; otherwise record it solely as an auxiliary feasibility result.

No code has been written for this run before this idea file.