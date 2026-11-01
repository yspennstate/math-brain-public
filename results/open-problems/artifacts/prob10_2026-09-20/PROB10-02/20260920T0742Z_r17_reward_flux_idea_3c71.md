# R17 PROB10-02 idea before code — reward flux instead of coalescence time

Model request: GPT-6 / maximum reasoning. Actual authenticated effort metadata is unavailable; do not claim GPT-6 maximum from prompt text alone.

Target remains the genuine binary Chvatal–Sankoff constant. The same fresh source bit `v` is compared with every active `x_i` in a strip column; independent Bernoulli matching is forbidden.

Continuity: H0021 is already released by R17 with its claims/artifacts preserved. The newest R17 PROB10-02 report is the profile-summed one at `20260920T0614Z`; P02 currently owns the covering/cone upper-bound route and P13 the reset-language/boundary route. R17 stays on the correlated discrepancy route.

## New idea

The preceding R17 runs bounded finite-horizon bias by *waiting for two coupled strip chains to coalesce*. That may be mathematically wasteful: for an ordered one-gradient defect, the difference of the two **cumulative rewards** may telescope even while the defect survives for a long time.

For strip length `m=2w`, let lower/upper gradients differ by one bit at coordinate `j`. Write `I(e)=1{j<=w}` for whether the defect crosses the central reward cut. Under one common genuine source update, test the exact identity

`rho(upper)-rho(lower) = I(next defect)-I(current defect)+left_exit_flux`,

with `I(next)=0` after absorption and `left_exit_flux=Q_0^upper-Q_0^lower in {0,1}`. If true on every formal edge/input pair, summing in time would show that a single initial gradient defect changes an arbitrarily long cumulative reward by at most one, independent of its coupling time.

Then combine this with the ordinary one-symbol Lipschitz property of LCS for initial raw-window bits. The desired consequence is a pathwise oscillation theorem

`|R_N(s)-R_N(t)| <= d_H(x_s,x_t)+d_H(g_s,g_t) <= 2m`

for every common future source word and all formal strip states. Averaging one initial state against stationarity would immediately give

`|E_s R_N - N gamma_w| <= 2m`

for every `N`, replacing the current width-4 constant `<39` and P13's width-6 reset constant `>3e5` by a deterministic linear-in-width transfer.

## Three attacks for this run

1. **Exact reward-flux/coboundary derivation.** Prove the one-gradient-defect identity algebraically from the `Q` recurrence, then exhaustively check it on all formal edge/input pairs through at least `m=8`.
2. **Raw-symbol sensitivity lift.** Prove that changing one initial raw source bit changes any finite cumulative strip reward by at most one, despite repeated comparisons against future `v` bits. Use a longest-path/LCS edit argument rather than simulation. Combine with attack 1 to obtain a full-state oscillation theorem.
3. **Try to strengthen `2m` to `m` and test usefulness.** Exhaustively compute the maximum common-word cumulative-reward oscillation for small widths/horizons. If `m` appears to hold but no proof survives, record it only as a conjectural sharpening. Separately quantify what the proved `2m` theorem does and does not change at the source level; no finite-width number counts as endpoint progress without the established width-to-source transfer.

The key falsification target is attack 1: if any formal edge/input violates the proposed local identity, stop the telescoping proof and archive the counterexample.