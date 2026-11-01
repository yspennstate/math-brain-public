Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT in the frozen `A_echo` metric: `0 -> 0`. Methods actually tried this run: #3 PROVE SOMETHING STRONGER, #7 TAKE THE LIMIT, #27 SWAP THE QUANTIFIERS.**

# NM13-11 fifth run — H0003 critical finite-transcript transfer without echo contraction

Date: 2026-09-18 UTC  
Track: `NM13-11` / HARD OUTSIDE  
Repository: `yspennstate/math-open-problems`, branch `master`  
Canonical source/claim: `H0003` / `operations/claims/H0003.md`  
Canonical dedup identity: `arxiv_2608_15987::conjecture_11.8`, residue 10 mod 13  
Overall source status: **OPEN**  
Local status after this run: **PARTIAL; bounded-degree saturated front reduction now covered at every fixed subcritical or critical parameter (`rho(M) <= 1`) in the iterated limit, with no linear echo-contraction condition; critical-window uniformity, supercritical survival, and unbounded degree remain open**

## 1. Runtime honesty and control-plane status

The task asks for GPT-6 with maximum reasoning. That is not what I can verify ran. The actual model exposed to this invocation is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**.

The task-control interface exposed to this runtime still offers task title/prompt, schedule or relative offset, timing mode, and enabled state. It exposes **no bindable model-family selector and no reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text rather than a scheduler-enforced setting. Making it binding requires an owner-authorized product/workspace/API surface that actually exposes model and reasoning fields.

Repository history still records one P26-context response `You cannot modify this task` and a later successful P26 update from another authorized context. The safe interpretation is context-specific authorization. The lawful workaround is the owning account/workspace or another authorized product/admin surface, not task cloning or an access-control bypass. I did not create, disable, or modify any schedule.

## 2. Continuity recovered before new mathematics

This run continues the live H0003 assignment. It does not reopen intake and does not create or overwrite a claim. `operations/claims/H0003.md` still names NM13-11 as the exclusive owner; no release, handoff, retirement, POSTED entry, source closure, or completed outside audit was recovered.

Before working I read or targeted-search-recovered the owner-required current surfaces:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized NM13 deployment amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/H0003.md`;
- the H-intake/source-verification material and targeted H0003 ownership/attempt searches;
- all four preceding NM13-11 reports, newest first;
- newest visible neighboring NM13-10 and NM13-12 reports.

The newest prior report is

`proofnet24/NM13-11/runs/2026-09-17/2026-09-17T23-59-00Z__H0003-finite-horizon-no-contraction.md`.

Its theorem `NM13-11-H0003-FINITE-HORIZON-NOCONTRACTION-04` proved the bounded-degree, Benjamini--Schramm-to-tree, saturated **strictly subcritical** slice `rho(M)<1` with no echo-contraction condition. The proof stopped the coupled explorations after `K` failed vertices and after a fixed decision-time cutoff `T`, replacing the infinite-time resolvent by a finite semigroup integral. For fixed `K,T`, the strong-coupling growth factor is finite even when

`lambda := gamma_max L_sigma Delta_max - alpha_min > 0`.

The report left a sharp obligation: understand whether the cutoff itself can be removed at or near criticality without restoring a contraction hypothesis.

Large root ledgers are connector-bounded when displayed wholesale; the source-specific continuity above was accessible. I do not claim a byte-for-byte omniscient reread of every repository object.

## 3. Fresh source and literature status check

Dated bounded public check: **2026-09-18 UTC**.

The primary source remains Achyut Kumar, *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987. Fresh exact-id/title searches still recover **v1, submitted 17 August 2026**, and still describe the strong-coupling saturated front reduction as open. I found no v2 in the bounded search.

The author companion with Abhinav Duddala, arXiv:2608.21125 (21 August 2026), concerns front propagation/Bramson correction and the continuous-type sensitive regime; it does not close the full saturated front-Markov reduction. A fresh open-problem index search also still lists the full saturated reduction, including strong coupling and critical-window uniformity, as open. That index is secondary evidence; the primary-status conclusion here rests on the unchanged arXiv source and companion search.

I also rechecked the conceptual nearby fixed-time locality literature already identified in the prior run (Oliveira--Reis--Stolerman 2020; Lacker--Ramanan--Wu 2019/2020). Those results remain prior art for fixed-horizon locality of interacting diffusions, not proofs of this absorbing-threshold genealogy statement.

No source-matching later theorem was recovered. This is **bounded negative evidence only**, not a claim of worldwide openness or publication novelty. Novelty of the theorem below is **UNVERIFIED**.

## 4. Frozen metric and counters

The frozen claim-file metric remains

`A_echo` = the graph-amplification coefficient in a rigorously proved sufficient linear echo-stability condition

`gamma_max * L_sigma * A_echo < alpha_min`

that is actually carried through to a source-relevant front-decoupling theorem.

Historical movement recovered from the preceding reports:

- source dissipative theorem: `A_echo = Delta_max`;
- NM13-11 run 1 on a uniform-spectral subclass: `A_echo = Lambda_*`;
- NM13-11 run 3 on bounded-degree BS-to-tree strictly subcritical instances: `A_echo = 2 sqrt(Delta_max-1)`;
- NM13-11 run 4 on the same strict-subcritical class: `A_echo = 0`, meaning no linear echo-stability inequality is needed in the iterated limit.

This metric has reached its natural floor. I do **not** rename the newly enlarged parameter range below as a different metric.

**Before:** `A_echo = 0`.  
**After:** `A_echo = 0`.  
**Movement:** none.

Because the immediately preceding run moved the metric, this is the **first consecutive unchanged-metric run**. Thus

`unchanged_runs_since_metric_movement = 1`, `stuck_recoveries_used = 0`.

The source remains OPEN and NM13-11 remains PARTIAL. No P26 or NM13-12 audit is counted.

---

# 5. Method #3 — PROVE SOMETHING STRONGER: the strict inequality `rho(M)<1` was not load-bearing

The previous proof used strict subcriticality only at the final truncation step: an exponential progeny tail made

`P(|S_GW| >= K)`

small when `K` was large. But the fixed-`K` coupling argument itself never used an exponential tail, or even a finite mean total progeny. It only used the fact that the ideal genealogy can be truncated with small probability.

At a fixed critical parameter `rho(M)=1`, the source's ideal finite-type Galton--Watson process is critical with bounded offspring in the bounded-degree slice. Under the source's nondegenerate finite-type hypotheses it becomes extinct almost surely. Equivalently, the source's pure branching-process critical theorem gives the familiar total-progeny tail of order `K^(-1/2)` (its mass function is of order `m^(-3/2)`). Therefore

`P(|S_GW| >= K) -> 0` as `K -> infinity`                                  (5.1)

also at exact criticality.

The decay is slower than in the strict-subcritical regime, but for a qualitative iterated limit **speed is irrelevant**: one first chooses a finite `K` large enough for a requested error tolerance, and only then sends the saturation parameter to infinity.

Outcome of method #3: **success**. The theorem can be strengthened from every fixed `rho(M)<1` parameter to every fixed `rho(M)<=1` parameter in the bounded-degree saturated class, without changing the echo metric.

---

# 6. Method #7 — TAKE THE LIMIT: cross the critical surface by truncation, not by uniform constants

It is tempting to take `rho(M) upward to 1` in the previous strict-subcritical error bound. That is the wrong limit: subcritical exponential-tail constants degrade as the spectral gap `1-rho(M)` vanishes, so a parameter-uniform passage gives nothing.

Instead take the **genealogy cutoff** to infinity after proving the comparison at each fixed cutoff.

Let `S_GW` be the ideal typed genealogy. For any fixed source parameter with `rho(M)<=1`, define

`q_K := P(|S_GW| >= K)`.

Then `q_K -> 0`:

- for `rho(M)<1`, by ordinary subcritical extinction (indeed exponentially under bounded offspring);
- for `rho(M)=1`, by critical a.s. extinction/nondegeneracy (indeed `q_K=O(K^(-1/2))` under the source's bounded-offspring critical theorem).

No constant in the finite-horizon echo estimate must be uniform in `K`. For every fixed `K` it may be astronomically large and still be multiplied by `epsilon(delta)->0` after `K` is frozen.

This also identifies the precise stopping point of the route. If `rho(M)>1`, then

`lim_(K->infinity) q_K = P(S_GW survives) > 0`,

so a finite-genealogy cutoff cannot by itself compare the full object in total variation. Supercritical survival requires a genuinely different infinite-front argument. Thus the method crosses the critical surface exactly up to, but not beyond, `rho=1`.

Outcome of method #7: **success and a sharp route boundary**. Exact criticality is accessible; the supercritical regime is not.

---

# 7. Method #27 — SWAP THE QUANTIFIERS: error tolerance first, then cutoff, then saturation

The source's desired strong statement seeks a quantitative bound uniform through the critical window. That asks for constants stable while the exploration scale diverges. The previous report correctly observed that the finite-horizon semigroup factor can grow exponentially with that scale.

For the qualitative iterated limit, the quantifiers are different and weaker. The correct order is

`for every eta>0`
`  choose finite K and T;`
`  then choose delta large enough for those fixed K,T;`
`  then take n large enough for the fixed explored neighborhood.`                         (7.1)

This is enough for convergence in total variation at each **fixed** critical parameter. It does not supply the source's desired `C(epsilon(delta)+eta_n)` rate or a window-uniform theorem.

To make (7.1) precise, reuse the previous run's finite-transcript construction. Stop the true and ideal breadth-first explorations at the first of:

1. a mismatch;
2. discovery of `K` failed vertices;
3. the fixed one-cell decision-time cutoff `T` used in the preceding theorem.

Before stopping, at most

`N_K := 1 + Delta K`                                                     (7.2)

one-cell decisions matter, where `Delta=Delta_max`, and a deliberately loose total comparison horizon is

`H := N_K T`.                                                            (7.3)

Put

`c := gamma_max L_sigma`, `alpha := alpha_min`, `lambda := c Delta-alpha`,

and

`J_H(lambda) := (exp(lambda H)-1)/lambda` if `lambda != 0`,
`J_H(0) := H`.

The proved finite-horizon comparison from run 4 gives, for every fixed `K,T`,

`||x(t)||_infinity <= gamma_max epsilon(delta) J_H(lambda)`, `t<=H`,    (7.4)

with no sign condition on `lambda`. Hence the active-cell drift perturbation is bounded by

`r_(K,T)(delta)
 <= gamma_max epsilon(delta) [1 + c Delta J_H(lambda)]`.                 (7.5)

The source's bounded-horizon first-passage stability lemma, used in the preceding report, therefore supplies for fixed `T` a finite constant `C_FP(T)` and one-decision mismatch bound

`p_mis <= C_FP(T) r_(K,T)(delta)`.                                      (7.6)

A union bound over the at most `N_K` relevant decisions gives

`P(any decision mismatch before the cutoff)
 <= N_K C_FP(T) r_(K,T)(delta)`,                                        (7.7)

which tends to zero as `delta->infinity` for every fixed `K,T`, even when `lambda>0`.

The remaining cutoff errors are handled **before** asking (7.7) to be small:

- choose `K` so `q_K=P(|S_GW|>=K)` is small;
- using the same one-cell time-cutoff tightness as the preceding theorem and the finite type set, choose `T` so the probability that one of the first `N_K` ideal decisions triggers the long-decision cutoff is small;
- for those fixed `K,T`, Benjamini--Schramm/local-weak convergence makes the finite explored marked neighborhood agree with the limiting tree with probability tending to one as `n->infinity`;
- only then choose `delta` so the mismatch term (7.7) is small.

Outcome of method #27: **success**. The quantifier swap removes the false need for a critical-window-uniform semigroup constant when the theorem sought is only the fixed-parameter iterated limit.

---

# 8. Main theorem — critical bounded-degree strong coupling in the iterated limit

## Theorem `NM13-11-H0003-CRITICAL-FINITE-TRANSCRIPT-05`

Let `(G_n,o_n)` be a bounded-degree finite rooted graph sequence in the source's saturated setting, with

`deg(G_n) <= Delta < infinity`,

whose marked rooted neighborhoods converge in the source's Benjamini--Schramm/local-weak sense to the stated unimodular random tree. Keep the source's finite type set and fixed admissible SDE parameters, with

`alpha_min>0`, `gamma_max<infinity`, `L_sigma<infinity`,

and impose **no** condition on

`kappa = gamma_max L_sigma Delta / alpha_min`.

Let `M` be the ideal finite-type Galton--Watson mean matrix. Assume

`rho(M) <= 1`,                                                           (8.1)

and, at equality, the source's standard nondegenerate critical finite-type hypotheses (automatic in the bounded-offspring source slice to which its critical total-progeny theorem applies), so the ideal critical genealogy is finite almost surely.

Then the failed genealogy of the uniformly rooted finite graph converges in total variation to the source's ideal finite-type Galton--Watson genealogy in the iterated limit

`lim_(delta->infinity) limsup_(n->infinity)
 d_TV( Law(S_(n,delta)), Law(S_GW) ) = 0`.                               (8.2)

In particular, (8.2) holds at **exact criticality `rho(M)=1` in arbitrary fixed strong coupling**, without `kappa<1` and without any linear echo-stability inequality.

### Proof

Fix `eta>0`.

**Step 1: truncate the ideal genealogy.** By (8.1) and the critical nondegeneracy assumption, `S_GW` is finite almost surely. Choose finite `K` with

`P(|S_GW|>=K) < eta/4`.                                                  (8.3)

At `rho(M)=1` one may use the source's critical total-progeny theorem to choose such a `K` quantitatively, but no rate is needed.

**Step 2: truncate one-cell decision times.** For this fixed `K`, there are at most `N_K=1+Delta K` decisions before the size cutoff. The one-cell decision-time cutoff used in `NM13-11-H0003-FINITE-HORIZON-NOCONTRACTION-04` is tight for each source type, and there are finitely many types. Choose finite `T` so the ideal probability that any of these first `N_K` decisions triggers the long-decision cutoff is less than `eta/4`. Denote `H=N_K T`.

**Step 3: finite-graph neighborhood error.** For fixed `K` the stopped exploration is contained in a deterministic finite graph-distance radius (one may take the crude radius `K`). Local-weak convergence to the source tree therefore makes cycle/mark/neighborhood disagreement on this stopped exploration less than `eta/4` for all sufficiently large `n` (in the limiting `limsup_n` sense used in (8.2)).

**Step 4: strong-coupling dynamical error.** On the event surviving the first three cutoffs, the previous run's synchronous comparison is valid on the fixed horizon `H`. Equations (7.4)--(7.7) give

`P(mismatch before cutoff)
 <= N_K C_FP(T) gamma_max epsilon(delta)
    [1 + gamma_max L_sigma Delta J_H(gamma_max L_sigma Delta-alpha_min)]`.

Every factor except `epsilon(delta)` is now fixed and finite. Since saturation gives `epsilon(delta)->0`, choose `delta` sufficiently large that this probability is less than `eta/4`.

**Step 5: couple the full genealogies.** On the complement of the four bad events, the true and ideal decision transcripts agree until the ideal genealogy terminates before `K`; hence the full typed genealogies agree. The coupling inequality therefore gives total-variation distance less than `eta` after the indicated limits.

Since `eta>0` was arbitrary, (8.2) follows. `square`

### Why this does not prove the source conjecture

The proof is qualitative and fixed-parameter. The required `delta` can deteriorate catastrophically with `K,T` because `J_H(lambda)` may grow like `exp(lambda K T)` in strong coupling. Near criticality, the `K` needed to make the genealogy tail small also diverges. Therefore this theorem does **not** give:

1. the source's desired quantitative `C(epsilon(delta)+eta_n)` bound;
2. uniformity as `rho(M)` moves through a critical window;
3. a supercritical (`rho(M)>1`) infinite-front coupling;
4. unbounded-degree unimodular limits.

Those are genuine remaining obligations, not hidden in notation.

---

# 9. What moved mathematically despite the frozen metric not moving

The preceding theorem covered fixed strong coupling only when `rho(M)<1`. This run removes that strict inequality and reaches the exact critical surface `rho(M)=1` in the same bounded-degree saturated class.

That is a substantive source-relevant enlargement, but it cannot honestly change `A_echo`: run 4 already proved the best possible coefficient value `0`. The correct ledger therefore says **no metric movement** rather than inventing a new number.

The most useful diagnosis is now sharper:

- **subcritical and exact critical, fixed parameter:** finite-transcript truncation is enough; no echo contraction is needed;
- **critical-window uniformity:** blocked by the growth of fixed-horizon constants as the cutoff scale diverges;
- **supercritical:** blocked more fundamentally because the ideal genealogy survives with positive probability, so no finite-size truncation can approximate the whole object in total variation.

The next research route should therefore target either a front-local observable whose error does not scale with total progeny, or a supercritical local-topology formulation that is actually source-equivalent. It should not spend another run improving the already-zero `A_echo` coefficient.

## 10. Prior-art and novelty qualifications

The truncation/quantifier argument is elementary once the previous finite-horizon comparison is available. I do not claim the mechanism itself is novel. Fixed-time locality for sparse interacting diffusions has substantial prior art, and critical Galton--Watson extinction/truncation is classical. The possibly new content is their use, under the source's own stopped first-passage comparison, to cross `rho(M)=1` in this particular strong-coupling saturated cascade problem. **Publication novelty is UNVERIFIED.**

The bounded search found no later paper explicitly making this source-specific critical transfer. A negative search is not a novelty certificate.

## 11. Next methods

Do not repeat this run's `#3/#7/#27` triple. The next untried methods selected for H0003 are:

- **#1 CHANGE THE CATEGORY:** replace full-genealogy TV in the surviving regime by a source-equivalent projective family of finite-generation laws, and determine whether the source statement really needs full-tree TV there;
- **#19 MAKE IT AN ALGORITHM:** write the front exploration as a reveal algorithm whose error budget is charged to the active boundary rather than total discovered volume;
- **#25 COUNT THE SAME THING TWICE:** seek a mass-transport identity for total echo influence across a frontier, once by source vertices and once by receiving frontier vertices, to replace exponential-in-depth worst-case amplification by an expected front-width quantity.

These target the actual remaining obstruction: uniform/infinite-front control, not the already-solved fixed-cutoff coefficient.

## 12. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-11
  category: HARD_OUTSIDE
  run_status: PARTIAL
  source_id: H0003
  claim_path: operations/claims/H0003.md
  canonical_dedup_key: arxiv_2608_15987::conjecture_11.8
  source_status: OPEN
  metric:
    name: A_echo
    before: 0
    after: 0
    meaning: sufficient graph-amplification coefficient in gamma_max*L_sigma*A_echo < alpha_min carried through to a source-relevant front-decoupling theorem
  movement: false
  substantive_scope_change: "bounded-degree saturated no-contraction theorem enlarged from every fixed rho(M)<1 parameter to every fixed rho(M)<=1 parameter, including exact criticality"
  new_internal_theorem:
    id: NM13-11-H0003-CRITICAL-FINITE-TRANSCRIPT-05
    statement: "bounded-degree BS-to-tree saturated cascades with rho(M)<=1 satisfy the qualitative iterated-limit front genealogy reduction for arbitrary fixed coupling, with no linear echo-contraction condition; at rho=1 assume the source-standard nondegenerate critical bounded-offspring hypotheses"
    source_level_scope: PARTIAL_CRITICAL_STRONG_COUPLING_FIXED_PARAMETER
  methods_tried: [3, 7, 27]
  methods_outcomes:
    3: success_strengthened_strict_subcritical_to_critical
    7: success_cutoff_limit_crosses_rho_1_but_not_supercritical
    27: success_quantifier_swap_proves_fixed_parameter_iterated_limit_not_uniform_rate
  unchanged_runs_since_metric_movement: 1
  stuck_recoveries_used: 0
  outside_audits: []
  literature_check_date_utc: 2026-09-18
  literature_status: "arXiv:2608.15987 still recovered as v1; companion 2608.21125 does not close full saturated reduction; no source-matching later theorem found in bounded search; novelty unverified"
  next_methods: [1, 19, 25]
  next_step: "Attack the supercritical/critical-window obstruction by frontier-local/projective laws and a mass-transport error budget, not by further optimizing A_echo."
```

No checker artifact was created: the new claim is theorem-sized and its complete argument is written above; there is no separate finite arithmetic core to certify. No audit request, shared-root edit, peer-file edit, email, Drive action, public posting, workflow run, paid compute, permission change, or extra schedule was made.
