# The aimed-set ledger: solved; the residual = a spherical-code question
# Status: agent-derived; Tier 0 + Tier 1 + coherence identity + value-death rigorous
# (elementary, audited in-session); the two named residual steps OPEN.
#
# !! SESSION-18 AMENDMENT (mine, critical): THE SHALLOW CLASS AS STATED IS MISSING THE
# AGGREGATE-GRADIENT CONSTRAINT. Candidate counterexample to unamended (R'): RANDOM
# aimed designs (m' random k-subsets of the majority class, k = 1/(4 tau_0^2)) are
# LEDGER-LEGAL in the window [d_slice, C n^{2/3} log] (systematic overlap-coherence
# 2k/n <= nu there; max fluctuation within budget for t* <= 1/2; value at shared
# points ~ eps/11 <= B; anchor exact) and capture ~ Phi_det/2 >> budget. They violate
# ONLY the aggregate Lipschitz of the true nets: co-rising annuli multiplicity J ~
# 1/(128 c_0^2) forces |grad| ~ sqrt(J) Lambda >> L* at subset-aligned sphere points —
# a constraint the true class HAS (Lip_S(f) <= L*) and the ledger forgot. The earlier
# sweeps didn't see it because n^{2/3} log < slice at their parameters (window EMPTY).
# FIX: amend (R')'s class with the aggregate-gradient constraint (carried through the
# deep-peel); then pile-up caps co-rising multiplicity at (L*/Lambda)^2 = O(1)
# POINTWISE ON THE SPHERE — which may render the spherical-code question tractable.
# Agent in flight on: the amended class, the pile-up throttle theorem, and the
# verify-attack-then-exclude protocol.

## The ledger (exact optimization over aimed designs)
Variables: aimed sets S_g (|S_g| = k_g, same-sign), poles u_g = normalized sums, depths
~ k_g^{-1/2}, per-point per-ridge value v(k) = min(h_0, Lambda(k^{-1/2} - tau_0)_+),
multiplicities J_i. Constraints: m' ridges; coverage sum k_g = M = sum J_i, support <= n;
INCOHERENCE via the exact identity <u_g,u_h> = (r_gh + Xi_gh)/sqrt((k_g+Xi_gg)(k_h+Xi_hh))
=> systematic overlap r_gh/sqrt(k_g k_h) budgeted by nu minus a per-pair fluctuation
xi ~ N(0, 1/d); VALUE sum over covering ridges <= B; ANCHOR k < 1/tau_0^2.
SOLUTION (uniform relaxation): W*(nu*) = max_k min( m' k v(k), n(1 + m' nu*) v(k), nB );
Theta = W*/Phi_disj. At nu* = 0: Theta = 1 EXACTLY (disjoint optimal).

## Rigorous tiers
TIER 0 (unconditional, counting only): ceiling regime k <= 1/delta*^2 <= C(c_0) T:
m' caps of ceiling size cannot over-cover: W_ceil <= h_0 m' k_ceil <= C Phi_disj.
NO incoherence, NO d-condition, NO gap.
TIER 1 (second moment, RIP event): sum J_i^2 <= M(1 + m'nu)/(1 - lambda) => M <=
n(1 + m'nu)/(1-lambda) => W <= C Phi_disj for m'nu = O(1), i.e. d >= d_pair ~
2(n/T)^2 log(m'n). Below d_pair the second moment permits sqrt(1 + m'nu) inflation —
THE HONEST GAP of the rigorous route: [d_slice, d_pair].
TIER 2 (fluctuation floor, heuristic): even disjoint aimed poles carry coherence
phi ~ 2 sqrt(log m'/d); the residual budget nu_eff = nu - phi is tiny; closure moves
down to d_fluct ~ (n/T)^2 (log T)^2/log m'.
OBSERVED (decisive): Theta ~ 1 UNIFORMLY down to the slice; J_ach = 1.00 at nominal
budgets m'nu up to 64; overlap gain 0.0% above the slice; flat in n up to 8192.

## The mechanism (named): THE BUDGET IS UN-SPENDABLE
- Forced depth: vacuous at the anchor (local throttling impossible).
- Value-death of J-fold cores (proved): m' Lambda tau_0 <= B fails => mega-cores illegal.
- THE OPERATIVE ONE: designs at the pairwise optimum have AVERAGE coherence = budget;
  per-pair noise N(0,1/d) puts HALF the pairs over => joint feasibility fragments the
  design. A spherical-code obstruction (PSD unit-diagonal entrywise-<=nu AIMED Gram),
  invisible to second moments.

## MY additions (session analysis, for the next attack)
- ENTROPY COUNTING: fixing all ~M J/(nu k) overlapping pairs' fluctuations costs
  ~ c per pair in probability; the aimed-set selection entropy is m' k log(en/k):
  fragmentation provable by first moment when m'^2-ish pair-costs exceed selection
  entropy — needs care (half-budget pairs are nearly free: P(xi <= nu/2) ~
  1 - (m'n)^{-c}; the binding pairs are the SATURATING ones).
- ANCHORING x INFLATION: J-multiplicit designs need k = M/m' <= 1/tau_0^2 (depth above
  anchor) => J <= m' /(n tau_0^2) = d/(2 T log(m'n)) — at d ~ slice this is ~1/(64 c_0^2)
  = O(1)!! Anchoring alone caps J near the slice; the gap region is where BOTH
  J-entropy and anchoring are loose: mid-range d.
- c* = 1/32 exact (Phi_disj = n h_0 saturates at c_0 = 1/32; throttle C only rescales
  c_0 by sqrt(C) — affordable).

## The residual, final form (two named steps)
(S1) GENERAL -> AIMED reduction: the shallow-class maximizer is near an aimed design
     (profile-decoupling given poles + the value ball selects aimed poles).
(S2) JOINT FEASIBILITY (the spherical-code bound): aimed nu-incoherent legal designs
     have J_ach = O(1) (equivalently M <= Cn), closing [d_slice, d_pair].
Numerics decisive for both. Character: finite combinatorial geometry, NOT chaining.

## Numerics (seed 20260708; ledger.py, decisive2.py, largen3.py, ledger_solve.py,
## peak.py in agent scratchpad)
Sweep table in the session record: gain 0.0% and J_ach = 1.00 for all (n, T, d) above
the slice (n up to 8192, m'nu up to 63.9); W_ov/Phi_disj <= 1.02 above slice (1.24 at
d = 512 < slice — inside the deterministic regime, fine); analytic tiers loose
(pair 2.0-5.6, fluct 1.2-2.4); RPRIME_CORRECTED table reproduced exactly.
