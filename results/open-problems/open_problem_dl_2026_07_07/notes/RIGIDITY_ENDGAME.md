# Rigidity endgame: stratified isolation + multi-scale merge — delivered
# Status: REFEREED (combined pass). VERDICTS + FIXES APPLIED:
# - CLAIM 1 (stratified isolation): CORRECT — "real theorem, reproduces to machine
#   precision; the crown jewel holds." Fixes applied: (a) Lemma A stated in the safe form
#   P(|<a,w>| >= t) <= 2 exp(-(d-2) t^2/4) for all t, d >= 6 (effective dimension d-2;
#   the bare exp(-(D-1)t^2/2) needs a polynomial prefactor); the union arithmetic and the
#   deterministic-witness logic survive with room (witness needs only P(good) > 0).
#   (b) tau_0 numeric caveat: the stated tau_0 formula is vacuous (>1) for d <= ~400 at
#   m' = 100; the reported d=256 run must have used log(m') — the lemma is asymptotic and
#   correct; reconcile constants before publication (referee re-ran d in {512,1024,2048}:
#   0 cross-activations, residual 1.3e-15, ratio 0.995).
# - CLAIM 2: correct modulo constant bookkeeping. CLAIM 3: correct in the stratified
#   regime; THE SUB-tau_0 AFFINE FALLBACK IS BROKEN (BAND_CLAIMS Claim 6's bridge was
#   withdrawn, and at d >= n the penalty form gives rank([X 1]) = n — useless). The
#   affine bound ||v|| <= C L* is UNCONDITIONAL ONLY in the fully-stratified regime
#   (all thresholds >= tau_0); sub-tau_0 units are an explicit open sub-lemma.
# - THEOREM 5: near-orthogonal branch sound MODULO the unwritten P4-LIFT (see below);
#   the claim "coherent blocks don't exist at d >= n" is WRONG (they can exist; they
#   were to be bypassed via the coherence-reversal — which rode on Claim P, now REFUTED).
#   Honest scope: Theorem 5 is (conditionally) about near-orthogonal nets; coherent
#   blocks route through MERGING (Claim 2, proved) into near-orthogonal super-ridges.
# - THE P4-LIFT (the referee-identified actual content, unwritten): E_y sup over m'
#   near-orthogonal-pole ridges with per-ridge TV <= C L* of sum_g <y, T_g(evals)> <=
#   C sqrt(m') L* sqrt(n) — Pythagoras replacing subadditivity. Uses TV + rigidity
#   (ALLOWED — different route from the refuted Claim P). This + merging = (M)'s
#   remaining core, and is exactly the final-core agent's incidence-capture target.

## UNCONDITIONAL (fully rigorous):
CLAIM 1 — STRATIFIED ISOLATION LEMMA (the F30/G1 synthesis, now a theorem):
d >= 6, tau_0 := 2 sqrt(8 log(m'n)/d), nu := tau_0/(2 t*). If every threshold >= tau_0
and every pole pair has |<u_c,u_{c'}>| <= nu, then for EVERY cluster and every generic
s in (tau_0, t*]:   |beta_c + A_c(s)| sqrt(1-s^2) <= L*   — EXACT constant, NO m'
restriction. Probe: x = s u_c + sqrt(1-s^2) w, tau = sqrt(1-s^2) u_c - s w, w RANDOM on
u_c-perp cap v_perp-perp (one exact orthogonality); spherical tail (Lemma A) + union:
whp all |<u_{c'},w>| < tau_0/2 => all cross arguments |s_{c'}| < tau_0 => A_{c'} = 0
IDENTICALLY; genericity a.s.; one witness certifies the deterministic inequality.
Numerics: d=256, m'=300 (>> sqrt d), 3600 probes: 0 cross-activations, isolation
residual 9e-16, worst ratio 0.968 <= 1.
COROLLARY 1.1: near-orthogonal regime TV(P_c) <= (1 + pi/2) L* — better than polylog.
CLAIM 2 (merged-group TV): group radius rho <= nu/2: TV(T_g) <= 4L* +
3 rho sum ||alpha_c||_1 / sqrt(1-t*^2).
CLAIM 3 (between-group difference, clean case): |A_g - A_g'| sin(theta/2) <= 2L* + Sh
with ZERO contamination when other groups are near-orthogonal to both; affine term
killed via a sub-tau_0 reference probe (|<v,b>| <= L*).
THEOREM 5, near-orthogonal regime: the FULL G1-replacement — mesoscopic part =
sum of merged bounded-TV ridges + shells + tilts <= eps n/32 — UNCONDITIONAL when
blocks are singletons (d >~ m' log; includes ALL of d >= n).

## CONDITIONAL / residual:
- Coherent blocks: TV <= C L* log(1/rho) under the Claim-4 contraction q < 1 (holds for
  up to ~sqrt(d)/polylog same-scale coherent groups). IRREDUCIBLE CORE: blocks with
  >> sqrt d mutually-coherent adversarially-aligned sub-groups.
- G3 scale tension: rho small (shells/tilts) vs rho >= 1/polylog (coherent TV): joint
  window nonempty only for d <~ T^{3/2} polylog; EMPTY for d >= n — but there coherent
  blocks don't exist (near-orthogonal regime), so the tension is vacuous exactly where
  it would bite. Genuinely unresolved: sqrt n <~ d <~ n with coherent blocks.
- d in {3,4,5}: constants need d >= 6 (immaterial).

## STRATEGIC CONSEQUENCE (main thread): the ReLU critical path is now CLAIM P ALONE
Lemma R (G2) consumes only the value bound + rank <= m — NO TV bounds. So for
ReLU-(M): contraction (clip off) -> affine probe ||v|| <= C L* (DELIVERED here:
sub-tau_0 reference probes / Claim 3 device) -> peel g_hi (Claim 3 of BAND_CLAIMS) ->
Lemma R -> CLAIM P -> content-zone arithmetic. Rigidity's TV machinery remains
load-bearing ONLY for: (a) the general-activation transfer (profile Lipschitz/TV feeds
the P4-general dictionary), (b) belt-and-braces alternate assembly. The coherent-block
core does NOT block ReLU-(M) via Lemma R (coherent = rank-collapse = easier Claim P).
Sub-tau_0 thresholds: units with t_k < tau_0 — handle inside Lemma R (rank argument is
threshold-blind; the value bound is global) — check at assembly: YES, Lemma R never
used thresholds. So the stratification is needed only for the affine probe (which needs
SOME inactive region — supplied by t >= tau_0 units... for sub-tau_0 units the
inactive region {all <u_c,x> < min t_k} may be empty!! Residual check for the
assembly: the affine bound for nets with near-zero thresholds — route via BAND_CLAIMS
Claim 6 (penalty form, unbounded v, y^T P y ~ d) instead — CHECK at assembly time).

## Numerics (seed 20260708, stratified_isolation.py in agent scratchpad)
Task 1: 0 violations at m' = 300, d = 256; estimator caution: naive Lip sampling
undershoots 4x (use certified probes). Task 2b: near-orthogonal 3rd group contamination
EXACTLY 0; coherent 3rd group 0.499 (bounded) — clean/fallback dichotomy confirmed.
