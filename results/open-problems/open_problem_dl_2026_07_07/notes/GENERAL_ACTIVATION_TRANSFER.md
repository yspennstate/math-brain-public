# REFEREE VERDICT (3rd pass): essentially correct, NO FATAL GAPS. Single-pole theorem
# for every Lipschitz activation = genuine, unconditional, numerically tight (ratio
# 1.00000000 exact-Lip, 0/96). Fixes: (1) ANCHORING IS A SPLIT NOT A SHIFT:
# g = g(tau_0) [-> c] + g^hi (:= g(max(s,tau_0)) - g(tau_0), anchored above tau_0)
# + g^{lo,0} (:= g(min(s,tau_0)) - g(tau_0), the sub-tau_0 residual); max/min are
# 1-Lipschitz so both parts inherit Lip(g). (2) The transferable assembly is the DP
# chain (cluster-counting), NOT lem:valuemass (unit-counting — does not transfer,
# correctly). (3) sec:scope updated in the paper (9001691). Paper now carries
# thm:singleclusterpsi (32pp).
# General-activation transfer: the band machinery for every Lipschitz activation
# Status: derived + audited by me (this session); numerics-checked (seed 20260708);
# independent referee PENDING. Complete for the single-pole theorem + stratified
# isolation + FD/DP + deterministic slice; the reduction lands on the SAME residual (R').

By the F1 worst-activation reduction the general-psi (worst case over Lipschitz psi)
conjecture is EQUIVALENT to the arbitrary-profile ridge-sum statement. So throughout we
treat
    f(x) = <v,x> + c + sum_{g<=m'} g_g(<u_g,x>),   g_g arbitrary Lipschitz profiles,
on model (S), with Lip_S(f) <= L*, sup_S|f| <= B. A single-ridge-direction psi-net is
DIRECTLY such an f with m'=1 (all same-direction units collapse to one profile
g = sum_j a_j psi(b_j <u_0,.> + c_j)); NO canonical form / kink-merge is needed. Write
v = beta_g u_g + v_perp^{(g)}. The kink structure and per-unit rigidity |alpha_k|<=2L* of
the ReLU proof are REPLACED throughout by (profile variation, profile-derivative
rigidity). Every band lemma below is re-derived from its ReLU proof with that single
substitution; each proof is checked to use only {slope bound, value bound, anchoring,
pole geometry} and NEVER "is a psi-net" or the kink count.

## T1. STATIC RIGIDITY TRANSFER

### T1a. PROFILE-DERIVATIVE RIGIDITY (single pole; = P1 / lem:staticrig verbatim)
Let f(x) = <v,x> + c + g(<u_0,x>), g Lipschitz, d>=3, v = beta u_0 + v_perp. g is
differentiable a.e. (Rademacher on R). For every Lebesgue point s of g' in (-1,1):
    (beta + g'(s))^2 (1-s^2) + ||v_perp||^2  <=  Lip_S(f)^2 ;
in particular |beta + g'(s)| sqrt(1-s^2) <= Lip_S(f) AND ||v_perp|| <= Lip_S(f).
Proof (three lines, IDENTICAL to lem:staticrig). Fix a Lebesgue point s of g'. On the whole
level set {<u_0,x> = s}, f(x) = <v_perp,x> + g(s) restricted, and x -> g(<u_0,x>) is
differentiable at every such x (composition of g, differentiable at s, with the submersion
<u_0,.>), with ambient gradient z = (beta + g'(s)) u_0 + v_perp, CONSTANT on the level set.
Write x = s u_0 + sqrt(1-s^2) w, w perp u_0 unit; ||P_{x^perp}z||^2 = ||z||^2 - <z,x>^2 with
<z,x> = (beta+g'(s)) s + sqrt(1-s^2) <v_perp,w>. Since d>=3 choose w perp v_perp: <z,x> =
(beta+g'(s))s, giving Lip^2 >= ||P_{x^perp}z||^2 = (beta+g'(s))^2(1-s^2) + ||v_perp||^2. QED.
The ReLU proof used ONLY the level-set gradient formula z = B(s)u_0 + v_perp; the general
profile supplies exactly the same formula with the partial-sum A(s) replaced by g'(s). The
d=3 requirement and d=2 exclusion are inherited unchanged.

Consequences (P2 transfers): writing P(s) := c + beta s + g(s) so f = P(<u_0,.>) + <v_perp,.>,
P is absolutely continuous with P' = beta + g', so
    TV(P) = int_{-1}^1 |beta + g'| <= L int_{-1}^1 (1-s^2)^{-1/2} ds = pi L,   ||v_perp|| <= L,
HOWEVER MANY units compose g. (For Lipschitz g, TV(g) = int|g'| exactly; no kink structure.)
Numerics: R = max_s|beta+g'|sqrt(1-s^2)/Lip = 1.000000 (tight, v_perp=0) and <=1 with 0/2000
violations on random tanh and GELU stacks (seed 20260708).

### T1b. STRATIFIED ISOLATION (multi-pole; = lem:stratiso verbatim)
Normalize each g_g so it is 0 (constant) below its ANCHOR a_g := inf{s: g_g(s) != 0}
(subtract g_g's value at the anchor into c). The STRATIFIED general class = {all anchors
a_g >= tau_0}, i.e. every profile is flat on (-1, tau_0]; this is the general-profile
analogue of "all ReLU thresholds >= tau_0" (a ramp is 0 below its threshold in value AND
slope). Let d>=6, tau_0 = 2 sqrt(8 log(m'n)/d), poles pairwise |<u_c,u_c'>| <= tau_0/(2t*),
thresholds/supports in [tau_0, t*]. Then for every cluster c and a.e. s in (tau_0, t*]:
    |beta_c + g_c'(s)| sqrt(1-s^2)  <=  Lip_S(f).
Proof (IDENTICAL to lem:stratiso). Probe x = s u_c + sqrt(1-s^2) w, w uniform on the sphere
of u_c^perp âˆ© (v_perp^{(c)})^perp (dim >= d-3). The tangential gradient along tau =
sqrt(1-s^2) u_c - s w is
    <grad f(x), tau> = (beta_c + g_c'(s)) sqrt(1-s^2) + sum_{c'!=c} g_{c'}'(s_{c'}) <u_{c'},tau>,
the <v_perp^{(c)}, w> term vanishing by the choice of w. The random-probe bound
|<u_{c'},w>| < tau_0/2 (spherical marginal + union over the m'-1 OTHER POLES) forces
|s_{c'}| < t*Â·(tau_0/2t*) + tau_0/2 = tau_0 <= a_{c'}, so g_{c'} is CONSTANT near s_{c'} and
g_{c'}'(s_{c'}) = 0: ALL cross-terms vanish. (The random-probe argument never used kinks;
only that other clusters deactivate below their support minimum.) Two clean improvements
over ReLU: (i) genericity for c'!=c is AUTOMATIC â€” s_{c'} sits in g_{c'}'s flat region, a
differentiability point for free; (ii) only s need be a Lebesgue point of g_c. QED.
This gives CLUSTER-TOTAL profile-derivative rigidity: the total g_c is slope-bounded;
INDIVIDUAL profiles within a cluster need NOT be (the rem:rigidfail / G1 counterexample
transfers verbatim as two general profiles +h, -h ramping to N along near-coincident poles).
Sub-tau_0 residual: identical to ReLU â€” isolation says nothing below the anchor; the
sub-tau_0 units are the SAME open sub-lemma.

## T2. THE SINGLE-POLE THEOREM FOR EVERY LIPSCHITZ ACTIVATION (complete, unconditional)

THEOREM (general-activation single-pole; = thm:singlecluster verbatim). There are absolute
c,C>0 such that in model (S) with exact +-1 labels, for all d>=3 and eps^2 n >= C, with
probability >= 1 - 2e^{-d} - e^{-eps^2 n/128}: EVERY single-ridge-direction network
    f(x) = <v,x> + c' + g(<u_0,x>),   u_0 in S^{d-1},  g ANY Lipschitz profile
    (produced from arbitrarily many units of ANY Lipschitz activation, arbitrary weights),
that fits eps below the noise floor has
    Lip_S(f)  >=  c eps min(sqrt n, d).
At d>=n the threshold is c eps sqrt n = the conjectured rate at the overparameterized
endpoint. No log, no width bound, no bound on the number of units.

Proof-transfer (every step activation-free or T1a). Put L = Lip_S(f), P(s) = c'+beta s+g(s).
* VALUE BOUND (lem:B0). ACTIVATION-FREE: its proof uses only diam(S)<=2<=4, Lipschitzness,
  and that fitting makes at least one (f(x_i)-y_i)^2 <= 1 (so |f(x_i)|<=2, then
  |f(x)|<=2+L*diam). No activation, no representation. Gives sup_S|f| <= B_0 = 2+2L (single
  pole), hence |P| = |f - <v_perp,.>| <= sup|f| + ||v_perp|| <= 2+3L =: B'.
* FITTING IDENTITY (lem:fitident). ACTIVATION-FREE (pure algebra on values+labels): fitting
  forces sum_i y_i clip(f(x_i)) >= eps n/2, deterministically.
* TAIL (P3). Split at s_0 = 1/2, P = P_<= + P_>, P_<=(s) = P(clamp(s,-s_0,s_0)). For |s|>s_0,
  |P_>(s)| = |int_{clamp}^s (beta+g')| <= L int (1-tau^2)^{-1/2} dtau by T1a â€” SAME slope bound
  on BOTH sides (the general profile needs no "affine below threshold": profile-derivative
  rigidity bounds |P'| = |beta+g'| everywhere). Layer-cake + occupancy N(tau)<=Op/tau^2
  (geometric) on directions +-u_0:  sum_i |P_>(s_i)| <= 2 L Op int_{s_0}^1 dtau/(tau^2
  sqrt(1-tau^2)) = 2 sqrt3 L Op <= 4 L Op, deterministically in y.
* RIDGE MULTIPLIER (P4). ALREADY stated for ALL Lambda_0-Lipschitz profiles â€” it NEVER used
  kinks. Class R = {x -> Q(<u,x>): u in S^{d-1}, Q is Lambda_0-Lipschitz, |Q| <= B'},
  Lambda_0 = 2L/sqrt3. P_<= qualifies (slope |beta+g'| <= L/sqrt(1-s_0^2) = Lambda_0 on
  [-s_0,s_0] by T1a; |P_<=| <= B'). Then E_y sup_R sum_i y_i Q(<u,x_i>) <= C(1+L) sqrt n:
  empirical-l2 entropy = direction (image-ellipsoid cover of {Xu}, rank min(n,d), radius
  sqrt(Op); Frobenius identity sum_j sigma_j^2 = n gives Op min(n,d) <= 2C_1 n in BOTH
  regimes => direction term C L sqrt n) + profile (1-D sup-norm Lipschitz entropy
  C(Lambda_0 sqrt n/u + log(B' sqrt n/u)) => C(1+L)sqrt n). The Lipschitz profile kills the
  sqrt(nd) that SHARP thresholds pay. Numerics: tanh-ridge sup /sqrt(nd) falls 0.46->0.022,
  /sqrt(n) stays O(1) â€” sqrt(n)-scale confirmed.
* ASSEMBLY (P5). clip 1-Lipschitz => sum_i y_i clip(f) <= sum_i y_i clip(<v_perp,x_i> +
  P_<=(s_i)) + sum_i |P_>(s_i)|; contraction removes clip; subadditivity splits affine
  (||v_perp||<=L by T1a, E||sum y_i x_i|| <= sqrt n) from ridge (P4):
      E_y sup sum_i y_i clip(f(x_i)) <= C(1+L) sqrt n + 4 L Op.
  With L <= c eps min(sqrt n,d): C(1+L)sqrt n <= eps n/8 (eps^2 n>=C) and 4 L Op <= eps n/8
  (both regimes). McDiarmid (differences 2) => sup <= 3 eps n/8 whp; 3/8 + ... < 1/2
  contradicts fitting. QED.

The canonicalization step is the only structural difference and it DISAPPEARS: a
single-direction psi-net is a profile ridge with no merging to do; g is just Lipschitz.

## T3. FD / DP / DISJOINT TRANSFER (activation-free given T1)

* FORCED DEPTH (lem:forceddepth / FD). PURE POLE GEOMETRY: K poles pairwise nu-incoherent,
  x with <u_g,x> >= sigma all g => K sigma <= ||sum u_g|| <= sqrt(K(1+(K-1)nu)) => sigma <=
  sqrt(1/K + nu). No profiles, no activation. Transfers trivially.
* DEEP PEEL (lem:deeppeel / DP). Uses only: cluster-total SLOPE bound Lambda (from T1b
  isolation), ANCHORING at tau_0 (stratified class), and CAP-MASS (lem:capmass: sup_{||u||<=1}
  sum_i (<u,x_i>-tau_0)_+ <= A/tau_0, purely geometric). Height-split each cluster-total at
  h_0 = Lambda delta*, delta* = 32 A Lambda m'/(eps n). An anchored slope-<=Lambda profile
  reaching height > h_0 needs argument > tau_0 + delta*, and there its high part <=
  Lambda(s-tau_0-delta*)_+; cap-mass at tau_0+delta* + sum over m' clusters =>
  sum_i |w_2(x_i)| <= m' Lambda A/delta* = eps n/32, deterministic in y, when delta*>=tau_0.
  NOTHING here is a kink property. Transfers verbatim.
* DISJOINT-CAP CASE. Height ceiling only: pairwise-disjoint data caps => |w_1(x_i)| <= h_0
  pointwise => l1 <= h_0 n <= eps n/32. Activation-free. CLOSED.
* Negative results N1-N3 (no disjointness lemma; deterministic surrogates vacuous above the
  slice; Rademacher width additive over Minkowski sums) are geometric / structural and carry
  over unchanged (they concern poles + caps + value balls, not activation).

## T4. THE MERGE / SHELL STRUCTURE â€” the one place kinks were used, and its resolution

The ReLU shell bound (P6/P7) wrote a within-rho stack as one center ridge + shells + tilt
with sum_i|R| <= rho sum_k|alpha_k| and ||tilt|| <= rho sum_k|alpha_k| â€” the per-unit
coefficients, controlled by per-unit rigidity |alpha_k|<=2L*. For general profiles the shell
error is sum_g [g_g(<u_g,x>) - g_g(<u_c,x>)] <= rho sum_g Lip(g_g): PER-PROFILE Lipschitz
bounds. These are NOT available â€” by T1b only the cluster TOTAL is slope-bounded, and the
G1 counterexample (rem:rigidfail, transferred) makes sum_g Lip(g_g) arbitrarily large while
the total stays L*-Lipschitz. So the merge/shell step is exactly where the ReLU proof used
kinks, and naive per-profile control FAILS â€” correctly, because this is precisely the
coherent-cluster degeneracy that is OPEN for ReLU too.

RESOLUTION (order the argument correctly; the difficulty is the SAME (R'), no worse):

(i) UNIT-FREE AUDIT. Every proven lemma counts POLES/CLUSTERS, never units/kinks:
    - single-pole thm (T2), P1, P2, TV, tail: "any m_0", "however many units" â€” m-FREE;
    - occupancy, cap-mass, forced-depth: geometric, no units;
    - stratified isolation (T1b): union over the m'-1 OTHER POLES â€” counts clusters;
    - deep-peel (T3): "sum over the m' ridges" â€” counts clusters;
    - residual (R') / Conjecture M: sup over m'-cluster configs, bound counts m'.
  NOWHERE does the number of psi-units (or PL kinks) enter a bound that must be small.

(ii) PL-APPROXIMATION IS FREE. Given the general net, replace each profile g_g by the
  piecewise-linear interpolant g_g^PL of g_g on a COMMON uniform grid of spacing h, chosen so
  ||g_g - g_g^PL||_infty <= eta := eps/(64 m'). Then f^PL = <v,x>+c+sum_g g_g^PL(<u_g,x>) is a
  ReLU ridge-sum with the SAME m' directions and MANY kinks (m Lip/eta per profile) â€” which,
  by (i), cost NOTHING. Correlation transfer (clip 1-Lipschitz, always valid, no Lipschitz
  needed): |sum_i y_i clip(f(x_i)) - sum_i y_i clip(f^PL(x_i))| <= n m' eta <= eps n/64. So it
  suffices to bound the correlation of the ReLU ridge-sum f^PL.
  The COMMON grid is the crucial choice: PL-interpolation is linear in the function, so the
  cluster-total-along-center G_c^PL = sum_{g in c} g_g^PL = PLinterp(G_c) is the interpolant
  of the L*-slope-bounded cluster total G_c; PL-interpolation is slope-non-increasing, so
  the CLUSTER-TOTAL slope bound (all that T1b/T3/P4 use) TRANSFERS to f^PL, while INDIVIDUAL
  g_g^PL slopes are â€” correctly â€” not controlled and not needed. Value bound: |f^PL| <= B+1.
  Anchoring: preserved up to h (shift tau_0 by h). So f^PL sits in the ReLU stratified band
  class for the purposes of every proven lemma.

(iii) WHAT DOES NOT TRANSFER, AND WHY IT DOES NOT MATTER. f^PL still has the SAME within-
  cluster shell structure (its PL profiles on near-coincident poles), whose bound would need
  sum_g TV(g_g^PL) ~ sum_g TV(g_g) â€” uncontrolled, for f^PL exactly as for f. This is not a
  defect of the transfer: the coherent-cluster shell/tilt problem is NOT part of the proven
  machinery in EITHER case. It lives entirely inside the open residual (R') / (M)'s core
  (G1 cross-cluster rigidity, G3 cross-cluster tilt). The transfer's job is to land on that
  SAME residual, which it does.

## T5. ASSEMBLED REDUCTION MAP (general activations)

Every object below is the ReLU object with (kink structure, per-unit rigidity) replaced by
(profile variation, profile-derivative rigidity T1); the activation enters ONLY through the
Lipschitz-profile abstraction.

1. SINGLE-POLE THEOREM (T2): COMPLETE, UNCONDITIONAL, every Lipschitz activation, all d>=3.
   Lip_S(f) >= c eps min(sqrt n, d). [= the general-activation conjecture at every m' that
   is a single ridge direction, incl. arbitrarily many same-direction units.]
2. STRATIFIED ISOLATION (T1b): cluster-total profile-derivative rigidity for the stratified
   general class (profiles anchored above tau_0, incoherent poles). COMPLETE.
3. DETERMINISTIC SLICE (rem:detslice): Conjecture M holds WITH NO LABEL RANDOMNESS on
   d <= c T log(m'n)/c_0^2 â€” its proof uses only cap-mass (geometric) + cluster-total slope
   + value bounds (T1). Transfers. COMPLETE. The sharp "no deterministic argument goes
   further" (excess sqrt(d/(32 T log(m'n))) above the slice) transfers identically.
4. DEEP PEEL + DISJOINT CASE (T3): remove the deep sector unconditionally above the slice;
   close the disjoint shallow case. COMPLETE, activation-free given (2).
5. THE (M)-REDUCTION. General-activation (M) reduces, by (2)-(4) + the merge (T4), to
       (R')  E_y sup over the shallow class of <y, w_1>  <=  C( h_0 sqrt(m'n) + B sqrt(n log(m'n)) ),
   whose class ("merged ridges, slope <= Lambda, height <= h_0, ANCHORED, incoherent poles,
   |w| <= B") is stated PURELY in profile terms and ALREADY admits arbitrary Lipschitz
   profiles. Hence (R') for general activations IS the ReLU (R') â€” literally the same
   statement (the ridge-multiplier P4's 1-D Lipschitz-profile entropy already covers every
   Lipschitz profile). Plus the SAME two scoped residuals: the sub-tau_0 sector and the
   coherent sqrt(n) <~ d <~ n window.

CONCLUSION (the structural theorem). THE FULL BLN CONJECTURE FOR EVERY LIPSCHITZ ACTIVATION
IS REDUCED TO (R') PLUS THE SAME SCOPED RESIDUALS AS THE ReLU CASE. The activation plays no
role beyond the profile abstraction: once one collapses same-direction units to a Lipschitz
profile and uses profile-derivative rigidity in place of kink rigidity, ReLU and general-psi
are the identical problem. When (R') lands for ReLU, it lands for every Lipschitz activation
simultaneously; the log-free law at all widths m <= n/2, d >= eps^{-2} log^C n, holds for
every Lipschitz activation the moment it holds for ReLU. (This subsumes the F21 small-width /
high-d general-activation results and the F1 reduction into one clean statement.)

## Numerics (seed 20260708, scratchpad genact_numerics.py, < 5 min)
(1) Profile-derivative rigidity on smooth single-pole nets (tanh AND GELU stacks, J up to 12,
    d in [3,40]): R = max_s |beta+g'(s)| sqrt(1-s^2)/Lip_S(f) = 1.000000 (machine-precision
    tight) for adversarial v_perp=0; max 0.999999 general; 0/2000 violations. Exactly the
    ReLU P1 signature (0.9999, 0%) with kinks removed.
(2) tanh single-pole ridge multiplier, n=512: sup /sqrt(n) = 1.84, 1.75, 1.10, 0.71 and
    sup /sqrt(nd) = 0.46, 0.22, 0.069, 0.022 for d = 16, 64, 256, 1024 â€” /sqrt(nd) falls
    monotonically, /sqrt(n) bounded: decisively sqrt(n)-scale, matching P4 for smooth psi.
```
d       16     64    256   1024
/sqrt n 1.84  1.75  1.10  0.71
/sqrtnd 0.46  0.22  0.069 0.022
```

