# R17 PROB10-02 — finite-horizon lower endpoint idea (written before code)

Target remains the genuine binary Chvatal–Sankoff constant. In every strip column one fresh `Y` bit is shared across all active comparisons, so the dependent matching array is preserved.

## New route

The preceding R17 report proved the sharp pathwise stationary-centering bound for a strip of length `m=2w`:

`|E_s R_N - N gamma_w| <= m`

for every formal starting state `s` and every horizon `N`, with `gamma_w <= gamma_2` and `gamma_w -> gamma_2`.

Therefore any exact finite-horizon computation satisfying

`E_s R_N / N - m/N > L`

immediately proves the genuinely source-level improvement

`gamma_2 >= gamma_w >= E_s R_N/N - m/N > L`,

where the inherited public lower endpoint is `L=0.792665992`.

This bypasses exact stationary-distribution solution and turns the new path-span theorem into a potentially endpoint-moving certificate. The computation must keep the actual raw `X` window in state and branch on the four genuine source pairs `(u,v)`; replacing match indicators by independent Bernoulli variables is forbidden.

## Three attacks for this run

1. **Exact reachable-law propagation.** Starting from a fixed formal state, propagate exact integer state counts over the four source-pair branches, accumulating total reward. Search widths/horizons for the first certificate `E R_N/N-m/N > L`.
2. **Block-subadditive / restart amplification.** If direct exact propagation becomes too large, exploit the sharp `m` path-span to aggregate or restart blocks rigorously, controlling each restart by an explicit additive `m` penalty rather than solving the stationary law.
3. **Exact lower Bellman subsolution from a finite-horizon value function.** For a manageable horizon `T`, use `V_T(s)=E_s R_T` as a candidate potential and certify a Collatz-type lower residual `min_s(E[r+V_T(S')]-V_T(s))`; if this exceeds `L`, it gives a stationary lower bound without needing long forward propagation from one state.

Critical falsification target: determine whether widths reachable with exact arithmetic can possibly cross `L` after the unavoidable `m/N` penalty. A finite computation that does not cross this inequality is auxiliary only and is not source-level progress.
