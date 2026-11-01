# REFEREE VERDICTS (session 20) — APPLIED:
# CORRECT: Route 2 (comb-robust, NO factor 2: int|H| <= full cap-mass, ratio 1.002);
#   radial identity (exact); Lemma D (deep mult = 1); Lemma M with the LINEAR constant
#   (the VALUE bound binds: K <= 2B/h_0 + O(1/C_L^2); the quadratic gradient branch is
#   valid but non-binding; substantial-value hypothesis v_0 >= h_0/2 required;
#   small-value pile-ups reach ~1/nu but are capture-harmless); y-independent split.
# FIXED: Route 1's "single-ramp extremal" WITHDRAWN (bang-bang combs are extremal,
#   median ratio 1.04 but up to ~1000x; harmless — per-ridge bound survives verbatim).
# GAP (repair prescribed): Lemma S fails on the VERY-SHALLOW strip [tau_0, sqrt(nu)]
#   (aligned tangential-cancelling simplex frames are pole-LEGAL there, mult up to
#   2B/h_0); repair = incidence/pole-budget accounting: such clusters cost ~2B/h_0
#   poles each => <= m' h_0/(2B) clusters x B capture = Phi_disj/(2T) — Phi_disj-scale,
#   not per-point J_max. W_det's l1 must be re-derived this way.
# WITHDRAWN (fatal): "poly(m'n) covering for W_rad" — covering entropy is
#   Theta(k* log n) up to ~n (CHECK 5: ratios 6.7 -> 1673); chaining is HOPELESS on
#   W_rad; (R') is the value-ball-intersection/label-average gain, NOT a covering
#   statement. (S1) REDUCES to (R'); it does not close it.
# GLOBAL CHECK REQUIRED (fix 5): the sector slice nu <~ C_L^2 c_0^4 must overlap the
#   deterministic slice — the whole-program consistency check, outside (S1) proper.
# (S1): the three-sector reduction, general -> aimed, carrying Lip_S
# Status: agent-derived (session 19); MY re-derivation of Lemma M's general-Gram form
# added below; referee IN FLIGHT. Scripts: s1_sectors.py, s1_mid.py (agent scratchpad).

## Delivered (pending referee)
ROUTE 1 (profile extremizers): layer-cake C_g(T) = int (T'/Lambda) Lambda H_g dtau,
H_g(tau) = sum_i y_i 1{s_gi >= tau}: bang-bang optimum; claimed single-ramp form
(combs flagged â€” referee to determine; sector lemmas need only full-slope-at-risers).
ROUTE 2 (per-ridge general = aimed): one-sign cap-mass: sup_u |sum y_i (s - t)_+| <=
A/t â€” per-ridge, general configs gain nothing over aimed. CLEAN.
RADIAL IDENTITY (star): ||sum sigma_g u_g||^2 = R^2 + ||tangential||^2, R = sum sigma s_g;
same-or-mixed signs >= K(1 - (K-1)nu): a pile-up hiding from Lipschitz (small tangential)
must show large radial imbalance R â€” which the value ball controls. THE LEVER.
LEMMA S (shallow, s <= s_1 = sqrt(2nu)): tangential coherences <= 3nu => SIGN-ROBUST
||sum eps P u||^2 >= K/2 for K <= 1/(6nu) => K <= J_max = 8(L*/Lambda)^2. (Numerics:
min-over-signs 0.70-0.95; crossing at J_max.)
LEMMA D (deep, s >= s_2 = sqrt((1+2nu)/2)): pairwise coherence >= 2s_2^2 - 1 = 2nu > nu
=> K <= 1 (2 at boundary).
LEMMA M (mid â€” NEW, the crux): combined gradient+value throttle. Agent's form:
worst-cancellation frame Gram c(I - 11^T/K): sigma^T M sigma = c(K - Q^2/K); value
|Q| v_0 <= B; eliminate => K <= 8/C_L^2 + 2B/h_0 =: K_comb, DIMENSION-INDEPENDENT.
Defeats the simplex evasion: aligned signs (gradient-evading) are value-illegal;
balanced signs (value-legal) restore the sqrt(K) gradient.
MY GENERAL-GRAM RE-DERIVATION (for the referee): M_gh = coh - s^2 (off-diag),
sigma^T M sigma = K - s^2 Q^2 + E, |E| <= K^2 nu => tangential^2 >= K - s^2 Q^2 - K^2 nu
=> K <= 8/C_L^2 + 2 s^2 Q^2 for K <= 1/(2nu) => K_comb ~ 8/C_L^2 + 2(B/h_0-ish)^2 â€”
still dimension-independent (what matters); the agent's linear form may need the
specific frame; numerics show saturation at 48 (vs 79 linear, ~3000 quadratic) flat
across d = 2k..1M â€” the truth is at-or-below the linear form.
ASSEMBLY: W_det (shallow-rising + deep) is DETERMINISTIC l1 <= n J_max h_0 =
J_max Phi_disj <= eps n/16 at c_0 <~ 0.025 (the sqrt(J_max) rescaling of c* = 1/32).
W_rad (mid + faint + plateaus): ||.||_inf <= 2B, ||.||_2 <= C B sqrt(n), per-point
substantial multiplicity <= K_comb: its width = (R') â€” THE one remaining input.
The "poly(m'n) covering numbers" claim for W_rad is OPTIMISTIC as stated (aimed-block
counts C(n,k) with k up to 1/nu are e^{sqrt(d/log) log n}) â€” referee to restate honestly.

## What remains after (S1)
(R') on W_rad: E_y sup <= C(h_0 sqrt(m'n) + B sqrt(n log(m'n))) â€” now over a class with
ramp structure + O(1) substantial multiplicity + carried Lip_S. Plus the standing scoped
residuals: sub-tau_0 sector; coherent sqrt(n) <~ d <~ n window; the sliver.

## Numerics (seed 20260708)
T1 shallow sign-robust âœ“; T2 deep = 1 âœ“; T3 mid saturation 4,8,32,48,48 across
d = 2k..1M (dimension-independent; FD would allow 167) âœ“; T4 no cross-sector legal
attack beats C Phi_disj (illegal ones violate incoherence 2-3.5x / Lip / value) âœ“;
W_det affordable at c_0 <~ 0.025 âœ“.

