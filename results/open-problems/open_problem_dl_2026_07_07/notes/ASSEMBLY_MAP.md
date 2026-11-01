# Assembly map: what implies the FULL conjecture, piece by piece
# (log-free + every Lipschitz activation + every width; maintained by the main thread)

Target: whp, every width-m psi-net (any Lipschitz psi, arbitrary weights) fitting n iid
+-1 labels on S^{d-1} has Lip >= c sqrt(n/m). Sensible regime d >= C log n (else even
pairwise separations degenerate); m <= c^2 n/2 is the content zone (above it the sqrt-2
trivial floor closes it).

## Width/dimension regime chart (PL activations, log-free)
1. m >= c^2 n/2: CLOSED (trivial floor; in the paper).
2. m = 1: CLOSED for ALL activations (thm:genact; 3-pass verified).
3. Band m in [n/log^C n, n/2), d >= eps^{-2} log^C n: reduced to (M) (sec:band, 3-pass).
   (M)'s open core: clustered mesoscopic stacks. Attack: F30 (in flight).
4. BELOW the band, T = n/m >= log^C n: NOT covered by the with-log theorem (F24 correction).
   Structure: t* = 320 L* Op/(eps T) SHRINKS with T, so the mesoscopic window narrows.
   Sub-regimes:
   4a. If t* <= sqrt(C log n/d) (holds iff T >= C' Op^2 d/(eps^2 log n)): every mesoscopic
       unit is BULK (population mass >= 1/poly) => visible-sector machinery (Christoffel
       LLN / C1) suffices — NO clustering hell. PROVABLE with the C2/visible deliverable.
   4b. Else (moderate T below the band but t* above bulk scale): same (M)-shape problem
       with a narrower window; the band machinery (Claims 1-7) applies verbatim (nothing
       in Claims 1-7 uses T <= log^C except through t* < 1 nonvacuity d >= C n c0/sqrt(T),
       EASIER for larger T). So regime 4b = (M) on [0, t*(T)] — the SAME conjecture (M)
       with better constants. CONCLUSION: closing (M) closes ALL m <= n/2 for d >= 
       eps^{-2} log^C n; the band restriction in sec:band is cosmetic and should be
       LIFTED when (M) lands (check: Claim 3's l1-closure and Claim 4/5 never used
       T <= log^C; Claim 7's assembly neither; only the CONSISTENCY numerics did).
5. d >= C n (any m <= cd, any activation): pending F21 (in flight). With the F27 curve:
   also m <= 3 at d >= polylog, m = 4 at d >= n^{1/3}, m = 5 at d >= sqrt(n).
6. SLIVER C log n <= d <= eps^{-2} log^C n: open, unattacked. Note Op ~ n/d is HUGE here,
   occupancy weak; heat split fine. Lowest priority (polylog-wide window in d) but must
   be either closed or honestly excluded from the final statement ("for d >= log^C n").

## Activation chart
- PL/ReLU: all of the above applies directly (canonical form + rigidity).
- General Lipschitz psi: two routes:
  R1 (small width / high d): genact + F21 — activation-blind (projection floors). Covers
     m = 1 (all d), m <= 3 (d >= polylog), all m (d >= Cn) — PENDING F21.
  R2 (all widths, d >= polylog): the level-decomposition keystone. The energy ellipsoid
     sum_l lambda_l ||f_l||^2 <= L^2 is activation-free; level-rank <= m is activation-free
     (Daniely device); the CLIPPED keystone (F25c) is what must be proved. Its visible
     sector = C2 + Christoffel LLN (in flight); its invisible sector = the SAME clustered
     degeneracy as (M). KEY OPEN QUESTION for R2: does the (M)-machinery (occupancy,
     serving, shells, profile rigidity) transfer to general-psi ridge stacks? Claims 1, 2
     do verbatim (activation-free). Claim 3-4 need per-unit value/serving bounds: for a
     general profile g_k with ridge Lip contribution, the analogues hold with |g_k| replaced
     by its variation — TO BE CHECKED when (M) lands for ReLU. The worst-activation
     reduction (F1) says it suffices to treat arbitrary-profile ridge sums.

## Dependency graph (=> means "suffices for") — CORRECTED after the visible-sector referee
(M) => log-free PL, all m <= n/2, d >= eps^{-2} log^C n   [via 3 + 4b + 1]
C2 + Christoffel-LLN: DELIVERED (jet transport scoped k <= 3; trace-LLN <= 3nm fixed) —
  but these do NOT by themselves give the visible-sector CORRELATION bound (Theorem 3
  was FATALLY flawed and is withdrawn): the correlation needs sup-before-E_y deviation
  control of y^T M_U y over the jet family — the SAME wall as (M)'s core. The trace-LLN
  gives only E_y. So: visible + invisible sectors BOTH funnel into the clipped
  charging/chaining core. The jet family + trace-LLN are proved INFRASTRUCTURE, not a
  finished sector.
F21' => any-psi at m = 1 (margin n/sqrt(Lambda)), m = 2 (whole admissible range),
  m = 3 (d >= C Lambda^5); NOTHING at d >= Cn (linear-activation ceiling — F21's old
  claim withdrawn); high-d general-psi OPEN at every m.
(M)-for-general-profiles (open formulation) + heat split + F1 => any-psi all m, d >= polylog
Remaining after ALL in-flight pieces land clean:
  - (M) itself (clustered core) — the decisive battle, agent on it (F30 route)
  - (M) for general profiles — formulate after ReLU-(M)
  - the sliver in d — decide: attack or scope the theorem to d >= log^C n
Everything else is assembled.

## Verified generalization (session 12, checked line-by-line against BAND_CLAIMS)
Claims 1-7 use T <= log^C n NOWHERE essential: Claim 3's t* = 320 c0 Op/sqrt(T) has
nonvacuity sqrt(T) > 320 c0 Op — EASIER for large T; Claims 4, 5, 7 are T-free; the
dyadic-T union over [4, n/4] costs log n/n. Therefore (M), stated with t* = min(1,
320 L* Op/(eps T)) for ALL T in [4, n/4], implies the log-free PL law for ALL m <= n/2
at d >= eps^{-2} log^C n. The band framing is cosmetic. When (M) lands, state the
conditional theorem for all widths.

## General-profile (M) groundwork (for R2 / any activation; drafted, needs ReLU-(M) first)
Claims 1-2 are activation-free verbatim. The l1-closure for a general profile g: split by
SUPPORT depth (not threshold): g_out := g 1_{|s| > t*}: sum_i |g_out| <= sup|g| N(t*) <=
B_0 Op/t*^2 — weaker than ReLU (no per-kink rigidity => height not tied to depth):
t*_general ~ sqrt(L Op/(eps T)) vs ReLU's L Op/(eps T). The missing rigidity analogue:
STATIC profile-derivative bound |g_c'(s)| <= C L* off shells/other-caps (from tangential
gradients, F30) + value anchoring at bulk (|g_c(bulk)| <= C(1 + ...) needs cross-cluster
disentanglement — same clustered core). PLAN: once ReLU-(M) lands, rebuild its proof with
(profile variation, static derivative rigidity) replacing (alpha, kink rigidity); the
F1 worst-activation reduction then gives every Lipschitz activation.

## Session-15 update: (M) rewired through Lemma R; the endgame is TWO statements
G1-as-stated FALSE (counterexample) but repaired by merging; G2 rewired: the variance
budget was vacuous at d >= n, replaced by LEMMA R (value bound + rank <= m =>
<y, w> <= B sqrt(n) ||P_R y||; COMPLETE) + CLAIM P (projection capture <= C sqrt(m),
log-free-ish; m = 1 is P4, numerics flat at 2 sqrt m). Content-zone arithmetic closing
G2 given Claim P is COMPLETE (c_0 <= 1/(16 C_0 (sqrt2 + 2))). The affine part needs
||v|| <= C L* via inactive-region probes (stratified setting). SOFTENING: ADDITIVE
polylog in Claim P is affordable (+ B sqrt(n log) <= eps n/64); only MULTIPLICATIVE
sqrt-log is fatal; regime split d <= n/polylog (additive sqrt(d log) enough) vs d >= n
(flat sqrt m needed).
ENDGAME = (1) CLAIM P (agent in flight) + (2) STRATIFIED ISOLATION + multi-scale merge
(agent in flight; supplies the v-probe, the threshold stratification, and the
general-activation transfer scaffolding). Both land clean => (M) => log-free PL law,
all m <= n/2, d >= eps^{-2} log^C n. Then: general activations via the profile-transfer
rebuild of the same chain (F1 reduction; Lemma R is ALREADY activation-blind except the
ReLU feature span — general profiles = spans of {g(<u,.>)} with bounded-TV g: the rank
argument survives verbatim with the profile dictionary; Claim P's general-profile
version = capture over bounded-TV ridge spans — SAME object, P4's profile entropy
already covers arbitrary Lipschitz profiles!! Check when Claim P lands.)

## Standing discipline for the overnight run
Each landing piece: my line audit -> (if needed) referee agent -> apply fixes -> paper ->
compile -> push -> zip -> memory. Agents get output-discipline instructions (< 500 words
intermediate, < 4500 final). If quota dies: continue solo on (M)/F30. Do not relaunch S3.

## FINAL NIGHT MAP (session 20, 08:50 — the stable state after 6 formulations)
PROVED AND IN THE PAPER (32pp, 10 theorem-grade results, 3-pass each): the PL law all
widths up to one log; the n-free logarithm (n >~ md^2 log); any-activation floors
(m = 1 exact, m = 2 whole range, m = 3 at d >= C log); the single-direction theorem
for EVERY activation at c eps min(sqrt n, d); stratified isolation; the coherence-floor
counterexample; cap-mass (Op/log-free); forced depth; deep peel; the deterministic
slice + crossover; the corrected residual statement (Phi_disj, c* = 1/32).
PROVED IN NOTES (refereed): the sector throttles (deep disjoint; mid Lemma M linear
value-bound form, dimension-independent; shallow sign-robust on [sqrt(nu), s_1]);
per-ridge general = aimed (comb-robust); the radial identity; the general-activation
transfer (the whole chain is activation-free); the ledger + un-spendable budget; the
Christoffel trace-LLN; VBL; the projection-width characterization.
NEGATIVE RESULTS (all rigorous — the map's walls): the constraint triangle (clip/
rigidity/randomness each indispensable); Claim P false (aimed deep caps); per-cluster
TV rigidity false (1/rho tight); the subset-Lipschitz law false (tangential critical
points); W_rad chaining hopeless (entropy Theta(k* log n)); no disjointness lemma;
deterministic bounds capped at Phi_det (sharp crossover).
THE RESIDUAL (final form): (R') = the label-average/value-ball-intersection gain on
W_rad (strip [tau_0, sqrt nu] + mid-faint + plateaus; l1 is Phi_det-scale — only the
y-average can close it; the (S1) structure supplies ramps + O(1) substantial
multiplicity + carried Lip_S). PLUS: the sub-tau_0 sector (visible/Christoffel route
staged); the coherent sqrt(n) <~ d <~ n window; the log n <= d <= log^C n sliver.
CONSISTENCY: the deterministic slice and the sector regime OVERLAP (fix-5 arithmetic
checked); all numerics support (R') with constant ~1 (no legal attack beats
1.23 Phi_disj anywhere tested).
