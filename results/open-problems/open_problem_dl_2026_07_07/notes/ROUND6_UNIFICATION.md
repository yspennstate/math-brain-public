# Round 6 (07-08 overnight workflow): the unification, the new tools, the dead routes
# Status: synthesis of the 7-agent max-effort round (6 done, A2 died on login).
# Verdict: NOT SOLVED. But the open part UNIFIED into one statement.

## THE ONE OPEN STATEMENT (global value/gradient co-monotonicity, "GCM")
A structure that cancels the tangential gradient must cancel the value-correlation.
Proved LOCALLY (at data points: empty-base lemma freezes signs to y_i; positivity
identity makes grad_S w_1(x_i) = Lambda * P_{x_i} sum_j c_j x_j with c_j >= 0, exact).
UNPROVEN in the global form each sector needs. It appears as:
  (JF)      point-multiplicity theater: high-incidence points must carry proportionately
            LOWER per-cap value => sum_i |w_1(x_i)| = O(Phi_disj) though sum_i J_i unbounded.
  (R1*)     harmonic-curvature theater: general level->=2 bulk correlation <= C * (pure
            level-2 value). Extremal (pure-curvature) case now CLOSED (see (*) below).
  (MERGE-R2) coherent-merge theater: cross-cluster static rigidity, merged super-profile
            TV <= C*L* for >>sqrt(d) adversarially-aligned sub-groups on one axis.
Prove GCM globally and JF, R1*, MERGE-R2 fall together; only R3 polylog bookkeeping left.
Equivalent form: a Rademacher/chaining bound at per-cap l2-radius O(Lambda) against the
pole-dictionary entropy, beating the deterministic l1 optimum by sqrt(d/(32 T log(m'n))).

## NEW RIGOROUS TOOLS from the round (referee-verified; NOT yet in the paper)
1. (*) Level-2 spread/nuclear identity (A4): sum_i y_i f_2(x_i) <= (1/2) Lip_S(f_2) ||H||_*,
   H = sum_i y_i x_i x_i^T. Exact, deterministic, LLN-free. With rank-(m'+1) structure of
   W and ||H||_F = sqrt(n)(1+o(1)): pure-curvature nets (g = s^2) closed LOG-FREE at
   c0 <= 1/64. The ONLY fully-closed instance of GCM. NOTE: it is a VALUE bound from a
   GRADIENT budget (spread(W) = tangential-gradient budget; ||H||_* = value side).
2. Aggregate-Lipschitz pile-up scale (A3+referee): sup_x ||grad_S w_1|| =
   Theta(Lambda sqrt(min(m', 1/tau0^2))), attained at half-space-perturbed subset
   centroids, NOT at data points (there the tangential gradient plateaus/vanishes).
   Corollary: C_L = Lambda/L* -> 0; ANY per-point multiplicity throttle route is DEAD.
   (Supersedes SUBSET_LIPSCHITZ.md's "flat 4 Lambda".)
3. Empty-base positivity identity (A1): exact, verified 1e-14. Relocates simplex-frame
   evasion to non-data points where it cannot touch the l1 sum.
4. Theorem A (A1, referee line-by-line): RIP window N_c <= c* d/log(en), empty base:
   ||grad_S w_1(x_i)||^2 >= (1/12) Lambda^2 J_rise, so J_rise <= 48/C_L^2. Rigorous but
   silent exactly where needed (dangerous points have N_c ~ (d/log)^2 >> d).
5. R3 unconditional coverage (A5): reduction spine is Op-FREE down to d >= C log n
   (capmass, stratiso, deep peel, disjoint, single-pole, S1 all survive); deterministic
   slice reaches d <= 512 T log(m'n); elementary covering floor Lip >= c eps n^{1/(d-1)}
   /log^C closes the extreme bottom for ALL widths. Sliver = pure (R')+R1 instance.

## DEAD ROUTES (rigorous refutations - do not retry)
- Per-point multiplicity throttles (J_i <= O(1)): killed by C_L -> 0 (tool 2).
- Bound total incidence M: M >> n is legal (S2 design has M ~ Phi_det >> n).
- Lemma R+ unrestricted nonneg-cone anti-concentration: FALSE numerically
  (min_{c>=0} Rayleigh -> 0 once N/d >~ 4). Any closure MUST use nu-incoherence.
- R2 count route K <= c sqrt(m): FALSE (K = Theta(m) super-poles, 6/6 configs);
  subadditivity is Omega(sqrt(m))-lossy even on the closed disjoint case.
- Christoffel/trace-LLN average-gradient for R1: loose by sqrt(d/m'); extremal
  adversary (poles at top eigenvectors of H) is leverage-invisible.
- Aggregate-gradient lemma (round 5's candidate): per-pair overlap bound evaded by
  data-dependent adversary; constant 2 numerically false (~3.5).

## WHY (JF) IS BELIEVED TRUE (but unproved)
Every legal counterexample attempt fails: designs beating Phi_disj on raw value are
certified ILLEGAL (coherence 1.1-3x over, or aggregate ||grad||/L* 2.2-2.7). rho*
saturates ~1.08 flat to d = 32000 under the strong certifier. Overlap <=> co-rising
is geometric, not design-specific.

## ANGLES NOT YET TRIED (for the next round - keep frames SEPARATE across agents)
A. Per-LEVEL tensor duality: generalize (*) to level l via nuclear/injective tensor
   duality. sum_i y_i f_l(x_i) = <W_l, H_l>, ||W_l||_nuc <= sqrt(m') ||beta_l||_2 (rank m'),
   E ||H_l||_inj = E sup_u sum_i y_i Gtilde_l(<u,x_i>) = single-direction level-l width -
   provable by the PAPER'S OWN ridge-multiplier machinery (fixed profile => NO profile
   entropy; direction factor via the log-free ellipsoid Dudley <= C sqrt(n) * C_l).
   Energy ellipsoid sum_l lambda_l ||f_l||^2 <= L^2 is free. THE CRUX: the level-cutoff
   sum. A ramp of width tau0 has content to l* ~ 1/tau0; naive C_l = poly(l) gives
   sum_{l<=l*} l/sqrt(d) ~ sqrt(d)/log = THE WALL AGAIN. Decisive question: does C_l
   DECAY (Gegenbauer oscillation / stationary phase: the empirical measure of <u,x_i>
   is smooth at scale 1/sqrt(d) while Gtilde_l oscillates at scale 1/l => cancellation
   for l << sqrt(d)?) - numerically checkable TODAY, then provable.
B. Bednorz-Latala Bernoulli-process theorem (never mentioned in 6 rounds): sup of a
   Bernoulli process E sup_{t in T} sum y_i t_i is CHARACTERIZED by decompositions
   T subset T1 + T2 with sup_{T1} ||t||_1 + gamma_2(T2). (R') IS the assertion that the
   evaluation class decomposes with l1-part ~ Phi_disj. The S1 reduction already
   extracts an aimed core; the question is gamma_2 of the REMAINDER. This is the
   theorem-shape MADE for this problem - work out what the remainder is after the
   S1/ledger extraction and compute its gamma_2 against the pole-dictionary.
C. Local->global transport: value at x_i = integral of the aggregate gradient along
   rays into the caps; sum_i |w_1(x_i)| = integral of (occupancy-weighted aggregate
   slope) over a co-area in the POLE-SUBSET direction. The positivity identity is the
   local generator; the subset-centroid Lipschitz law (tool 2) prices the rays.
   Make the layer-cake global instead of per-point.

## PAPER IMPACT (as of round 6)
None required: the paper states conj:M as a conjecture and thm:conditional as
conditional; rem:detslice and lem:deeppeel already record the deterministic slice and
deep peel. The (*) theorem (tool 1) is publishable-grade but paper is already
referee-flagged as dense - hold for a follow-up note or v2 unless asked.
