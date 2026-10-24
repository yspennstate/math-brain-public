# The single-cluster theorem: ridge band-nets cannot fit random labels
# Status: derived + numerics-checked by the (M)-agent; MY LINE AUDIT PASSED (P1-P5);
# independent referee PENDING. Gaps G1-G3 = the remaining content of (M).

Notation: BAND_CLAIMS.md conventions. Single-cluster f: all units share one pole u_0:
f(x) = <v,x> + c + sum_k alpha_k relu(<u_0,x> - t_k), t_k in [0,1), rigidity, Lip_S(f)
<= L*, sup|f| <= 2+2L*. v = beta u_0 + v_perp; s_i = <u_0,x_i>; A(s) = sum_{t_k<s}
alpha_k; P-tilde(s) = c + beta s + sum_k alpha_k relu(s-t_k); B(s) = beta + A(s).

## P1 — STATIC PROFILE RIGIDITY (exact constant; the F30 key)
For single-cluster f, at every generic s in (-1,1):
   |beta + A(s)| sqrt(1-s^2) <= Lip_S(f)   AND   ||v_perp|| <= Lip_S(f).
Proof (three lines): at generic x with <u_0,x> = s the ambient gradient is z = B(s)u_0 +
v_perp; x = s u_0 + sqrt(1-s^2) w; ||P_{x-perp} z||^2 = ||z||^2 - <z,x>^2 = B^2 +
||v_perp||^2 - (Bs + sqrt(1-s^2)<v_perp,w>)^2. For d >= 3 choose w perp v_perp (S^{d-3}
nonempty; the whole level set is kink-free so no continuity issue): <z,x> = Bs, giving
Lip^2 >= B(s)^2 (1-s^2) + ||v_perp||^2. QED. Exact and tight (numerics ratio 0.9999,
0% violations, 2000 adversarial nets); d = 2 genuinely excluded (matches paper's prop:d2).

## P2 — Bounded variation
TV(P-tilde) = int |B| <= int L*/sqrt(1-s^2) = pi L*. Any number of stacked units in one
direction: profile TV <= pi L*, m-FREE.

## P3 — Occupancy tail (deterministic in y)
Split at s_0 = 1/2: P>_(s) := P-tilde(s) - P-tilde(clamp(s, -s_0, s_0)):
   sum_i |P_>(s_i)| <= L* Op sqrt(1-s_0^2)/s_0 (+ mirror side) <= 4 L* Op.
Proof: Fubini + occupancy N(tau) <= Op/tau^2: int_{s_0}^1 Op/(tau^2 sqrt(1-tau^2)) dtau
= Op sqrt(1-s_0^2)/s_0.

## P4 — Ridge multiplier bound (one free pole + free Lipschitz profile)
P = {x -> P(<u_0,x>)}: all u_0 in S^{d-1}, all Lambda_0-Lipschitz profiles (Lambda_0 =
2L*/sqrt 3), |P| <= B' = 2+3L*:
   E_y sup_P sum_i y_i P(<u_0,x_i>) <= C (1+L*) sqrt(n).
Proof: empirical-l2 entropy = direction + profile: direction = ellipsoid cover of
{X u_0} (rank min(n,d), radius sqrt(Op)); KEY IDENTITY sum_j sigma_j(X)^2 = n gives
Op min(n,d) <= 2 C_1 n IN BOTH REGIMES => Dudley direction term <= C L* sqrt(n) — the
sqrt(nd) one fears appears only for SHARP thresholds (VC = d halfspaces); Lipschitz
kills it. Profile term: 1-D sup-norm entropy C(Lambda_0 sqrt(n)/u + log(B' sqrt n/u))
=> C(1+L*) sqrt n. (Alt check: fixed profile + Talagrand contraction collapses to
||sum y_i x_i|| ~ sqrt n, flat in d — numerics confirm /sqrt(nd) DECREASING.)

## P5 — SINGLE-CLUSTER THEOREM
Band, d >= eps^{-2} log^C n, whp over x:
   E_y sup over single-cluster class of sum_i y_i clip(f(x_i)) <= C(1+L*) sqrt n +
   4 L* Op-bar <= eps n/4,
hence (Claim 7 assembly verbatim) NO single-cluster band net fits eps below the noise
floor. m-FREE: arbitrarily many stacked, sign-alternating, nested-threshold units in one
direction cannot fit. All d >= eps^{-2} log^C n including d >= n.
Proof: clip 1-Lipschitz: sum y clip(f) <= sum y clip(<v_perp,x> + P_<=) + sum|P_>|;
tail P3; Talagrand contraction removes the clip; subadditivity: affine (||v_perp|| <= L*
by P1; E||sum y x|| <= sqrt n) + ridge (P4). Affordability: L* sqrt n = c_0 eps
sqrt(Tn) <= eps n/16 for n >= C T; C sqrt n <= eps n/16 for eps^2 n >= C; 4 L* Op-bar
<= eps n/8 under d >= eps^{-2} log^C n.

## P6 — within-rho single cluster (conditional on rho-smallness)
Poles within rho of u_0: g = P(<u_0,.>) + shells + tilt; shells sum_i |R| <= rho Op
sum_k |alpha_k|/(t_k - rho)^2; tilt Phi = <D(s), x>, ||D|| <= rho sum|alpha|:
E_y sup <= rho sum|alpha| (sqrt n + C sqrt(Op log n)). Both <= eps n/32 for rho <=
c min(eps sqrt n/sum|alpha|, tau_min).

## P7 — General reduction (Steps 1-2 rigorous)
Greedy rho-clustering; g_lo = sum_c g_c; SHELL ERROR CLOSES UNCONDITIONALLY:
sum_i sum_c |shell_c(x_i)| <= eps n/32 for rho <= eps n tau_min^2/(C m L* Op).
Remaining: profiles + tilts.

## GAPS — the remaining content of (M)
(G1) CROSS-CLUSTER STATIC RIGIDITY: TV(P_c) <= C L* for rho-separated clusters. The P1
probe picks up sum_{c' != c} A_{c'}(<u_{c'},x>)<u_{c'},w>; need probe points with fixed
other-cluster activity — provable for near-orthogonal separated centers via gradient-
cloud (Claim 5); OPEN for clustered/coherent centers. THE irreducible core.
(G2) CLIP-AWARE JOINT CHAINING: E_y sup sum_i y_i clip(a + sum_c P_c(<u_c,x_i>)) <=
eps n/8 WITHOUT the naive factor #clusters (subadditivity pays m' C(1+L*) sqrt n —
fatal for large m'). The clip must cap value-overlap. For m' <= c eps sqrt n/(1+L*),
subadditivity suffices (clean corollary once G1 holds).
(G3) CROSS-CLUSTER TILT (rho > 0 only): sum_c tilts <= eps n/32 jointly with shells;
tension rho small (tilt) vs rho large (shells); union over m' directions must not pay
sqrt(m') or sqrt(d).

## The d >= n intermediate target (banked)
Single-cluster (DONE) + shallow-slab charging => (M) at d >= n modulo (G1): at Op = O(1),
G1's partial sums give height ceiling |P_c| <= 2 C L* t* = C' c_0^2 eps on the shallow
region — every cluster profile uniformly eps/1000-small; remaining = joint chaining of
tiny slab profiles = strictly easier (G2) instance. Sharpest next objective.

## Numerics (seed 20260707, scripts in agent scratchpad, each < 5 min)
P1 ratio 0.9999 max, 0% violations (2000 nets, exact analytic tangential gradient — FD
undershoots 1.8x); TV/(pi L*) <= 0.577; affine flat in d (|X^T y| = sqrt n to 2 digits,
d up to 4096); free-ramp sup/sqrt(nd) DECREASING (0.056 -> 0.013); full single-cluster
adversary E_y sup = 32-58 vs target 128 at n = 2048, ratios 0.25-0.45, /sqrt(nd) falling
monotonically — decisively sqrt(n)-scale, not sqrt(nd).
