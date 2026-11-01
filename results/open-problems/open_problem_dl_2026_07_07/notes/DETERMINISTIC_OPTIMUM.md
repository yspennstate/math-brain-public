# The deterministic incidence-capture optimum: solved exactly
# Status: REFEREED — the mass bound is TRUE, Op-FREE AND LOG-FREE, with the referee's
# complete proof replacing the (insufficient) P4-ellipsoid sketch:
#   IDENTITY (exact convex duality): sup_u sum_i (<u,x_i> - tau_0)_+ =
#     max_{S subset [n]} ( ||sum_{i in S} x_i|| - tau_0 |S| );
#   SUB-GAUSSIAN RIP: ||z_S||^2 <= N(1 + C_0(sqrt(L_N) + L_N)), L_N =
#     (N log(en/N) + 4 log n)/d, whp uniformly over all subsets (net + union);
#   TWO-REGION OPTIMIZATION => Phi <= (3 + 2C_0)/(4 tau_0) for tau_0 >=
#     sqrt(12 C_0 log(en)/d). Achievability (1 - o(1))/(4 tau_0) via random-block aiming
#     (E||z_S||^2 = k EXACTLY; the coherence-ceiling worry was a worst-case artifact).
# REFEREE FIXES APPLIED: (1) tau_0 typo — the operative value is sqrt(2 log(m'n)/d)
#   (the header's 2 sqrt(8 log/d) was 4x too large; crossover law only closes with the
#   operative value); (2) proof route corrected as above; (3) the "0.99-1.02" constant
#   was a weak-adversary underestimate — strong adversary gives sup-mass * 4 tau_0 ~
#   1.4-1.6 (absolute, Op-free, log-free; -> 1 as tau_0 sqrt(d/log) -> infinity);
#   (4) honest slice: d <= 0.17 T log(m'n)/c_0^2 (A ~ 0.37) — 2-3x thinner than first
#   stated, NONEMPTY at the band top (overlaps d >= eps^{-2} log^C n for c_0^2 <~
#   eps^2 log n); the log-lossy alternative WOULD close it — the decisive numerics
#   (Op swept 12-28x: flat; log n swept 60%: flat) are what keep it open;
#   (5) deep-sector disjointness needs s > sqrt((1+nu)/2) for nu > 0 (exact threshold).
# Ledger: 3 passes on the mass bound (derivation-shape + referee's complete proof +
# my audit of the duality identity and optimization). Paper-ready.

## The theorem
Phi_det := max over admissible configs of sum_i min(B, Lambda D_i)  =  Lambda m'/(4 tau_0),
D_i = total depth received by point i. CLOSED FORM, Op-FREE, TIGHT (achieved by m'
aimed caps of k* = 1/(4 tau_0^2) points each, pairwise nu-incoherent, freely
overlapping, UNSATURATED — the value bound is INACTIVE at the optimum).
Crossover law: Phi_det/target = sqrt(d/(32 T log(m'n))), target = Lambda sqrt(n m').

## Consequences
1. DETERMINISTIC (M) — new unconditional slice: on the Op event, with NO label
   randomness, E_y sup <= Lambda m'/(4 tau_0) <= eps n/8 iff d <= T log(m'n)/(2 c_0^2).
   Combined with Claims 1-7: the BAND LEMMA HOLDS UNCONDITIONALLY on
   d in [eps^{-2} log^C n, c T log(m'n)] — nonempty at the top of the band; thin;
   its value = a sharp certificate of where deterministic tools stop.
2. TRIANGLE REFINEMENT: the clip is INACTIVE at the deterministic optimum (sat = 0
   in all regimes) — determinism fails at large d NOT because it discards the clip
   but because occupancy alone is too weak; the clip can only bite through the
   randomness channel. And the old "l1 vacuous at n-scale" was an artifact of the
   unachievable occupancy depth-profile (inner products > 1); the achievable profile
   is aiming-limited and Op-free.
3. SINGLE-CAP MASS BOUND (the one non-elementary step, TO BE WRITTEN): sup_u
   sum_i (<u,x_i> - tau_0)_+ <= C/tau_0 — Op-free (occupancy alone gives only
   Op/(2 tau_0)); provable by the P4 ellipsoid method (sum sigma_j(X)^2 = n);
   numerics: mass * 4 tau_0 in [0.99, 1.02] across d = 200..8000.
4. THE RESIDUAL (= G2, exact form): E_y sup <y, w_lo> <= eps n/16 for anchored
   shallow ridges, nu-incoherent poles, |w| <= B, at DIAGONAL RADIUS Lambda sqrt(m')
   (per-cap l2 = Lambda/2 — O(1)! l1/l2 = sqrt(k*)) — against pole entropy
   sqrt(m' d log): needs a genuine Talagrand/multi-scale gain (per-pole increments
   <= Lambda — moving one pole perturbs only its caps). Auxiliary proved facts:
   (a) the DEEP sector s > 1/sqrt2 is UNCONDITIONALLY DISJOINT for incoherent poles
   (x in two caps => <u_g,u_h> >= 2s^2 - 1 > nu) — its l1 closes at target with no
   randomness; only the shallow band tau_0 < s <= 1/sqrt2 is live. (b) at d >= n the
   height ceiling makes it the "easier" instance — but even that is not closed by any
   single-scale bound (the reduced-radius arithmetic proves single-scale insufficiency).

## Numerics (dic_confirm.py, dic_opt2.py in agent scratchpad; < 30 s each)
Single-cap constant ratio 0.99-1.02 (4 regimes, d 200..8000). Crossover law measured
vs predicted: 0.18/0.18, 0.40/0.39, 0.81/0.80, 1.47/1.46, 2.38/2.35, 4.13/4.12
across d = 120..60000 (500x), Op 1.3..31 (Op-independence confirmed), sat = 0
everywhere. Per-cap l2 = 0.50 flat, l1 = 1/(4 tau_0) growing.
