Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. I0084 fixed metric `2/2 -> 2/2`; successor gate `E_READY_SUCCESSOR: 0 -> 0`; NO MOVEMENT; state `TERMINAL_WAITING_FOR_NEW_READY_DELTA` preserved; methods #2 ATTACK THE NEGATION FIRST, #20 FIND WHY THE ALGORITHM FAILS, #27 SWAP THE QUANTIFIERS.**

# R19 — terminal wait: P0219 survives source/current screening but fails the READY gate

Repository / branch: private `yspennstate/math-open-problems` / `master`.
Deployment: `NEW-METHODS-2026-09-16`.
Controlling predecessor: `runs/R19/2026-09-19_00-43-00_UTC__terminal-wait-p0220-owned-c0021-handoff_q8v3.md` @ `c12e905f7f2fede2b01d4d38f33fb60a25a7e9a0`.
Prewrite master captured for this run: `fed7dd2fa59acb078a77781f4b16c67e6d549b4f`.

## 1. Continuity: preserve the frozen I0084 result exactly

The original R19 source remains Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5, intake I0084.

The source scope is frozen as follows:

- the convolution in Conjecture 5.5 is ordinary **classical convolution** `mu*S_t`, including when `S_t` is the law of a free stable process;
- do **not** substitute additive free convolution `boxplus` for the asterisk;
- retain the exact finite `(2+alpha)`-moment hypothesis;
- retain the source's full input-measure class and original skewness conventions;
- stronger moments, compact support, or a restricted symmetry/skewness subclass are PARTIAL only;
- posted additive Brownian-unimodality results and already-known stable special cases earn no new source-case credit.

The fixed source metric remains

\[
M_{1/2}:=\#\{\text{complete classical-stable/free-stable }\alpha=1/2\text{ source cases proved}\}=2.
\]

Thus this run is `2/2 -> 2/2`. I0084 is not reopened for ordinary theorem churn after its prior handoff/rotation. The latest controlling R19 state also preserves the frozen ordinary-`*` version-matching audit gate; no new matching audit appears in the exact Git delta described below.

## 2. Required repository read and exact delta

Before screening the new delta I recovered the current campaign/index/ranking surfaces, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest operations implementation/status material, the controlling R19 report, current neighboring CLOSABLE admission reports, and the relevant intake/catalog evidence. The exact compare from the controlling R19 commit

`c12e905f7f2fede2b01d4d38f33fb60a25a7e9a0`

to captured prewrite master

`fed7dd2fa59acb078a77781f4b16c67e6d549b4f`

is complete:

- `ahead_by = 100`;
- `behind_by = 0`;
- `too_large = null`.

That delta contains no root `QUEUE.md`, `RESULTS.md`, or `POSTED.md` modification, no changed `probability_1000_intake_*/problems.jsonl` source ledger, and no newly created canonical claim that releases a full-source CLOSABLE target to R19. The live coordinator status continues to record `E_READY_CLOSABLE: 0 -> 0` and explicitly treats the outstanding successor lanes as genuine admission gaps rather than permission to promote a PENDING lead.

Material new events relevant to R19:

1. **P0219** has now received a deeper source/current screen from neighboring R01/R06. It is source-exact and current-open-looking, but remains a report-level replenishment lead with no canonical `operations/claims/P0219.md` and is explicitly **PENDING_NOT_READY**.
2. **P0220** remains a genuine CLOSABLE outside target but is already exclusively owned by R7-04; that was already known at the predecessor R19 run.
3. **I0130** remains an active owned CLOSABLE target and has continued receiving work; no release occurred.
4. **R09/Blanc-Renaudie** reached a six-run terminal mathematical handoff, but the handoff does not create an owner-authorized release to R19, and the fleet's own current admission evidence still says there is no free READY CLOSABLE successor.

Accordingly the only genuinely new admission object worth thinking about in this run is P0219, and the right question is not “can R19 steal it?” but “what exactly prevents it from becoming READY?”

## 3. Idea before any code

**Idea.** Treat the admission decision itself as a mathematical quantifier problem. P0219 is attractive because its source target is a single scalar asymptotic,

\[
1-v(p)\sim \sqrt{2(1-p)}\qquad(p\uparrow1),
\]

but the prior attempt and the author source both identify the real obstruction as an interchange of limits. Therefore attack the READY classification by trying to prove its negation: show that all currently recovered routes establish only fixed-parameter/fixed-window statements, while a source-level closure requires one estimate uniform enough to exchange the thermodynamic and rare-defect limits. If that is correct, P0219 must remain PENDING even though it looks syntactically CLOSABLE.

No checker is appropriate unless such a uniform estimate is actually produced. This run therefore spends its validation budget on the exact Git/source state only.

## 4. Method #2 — ATTACK THE NEGATION FIRST

The negation of “P0219 is READY CLOSABLE” is not “the conjecture is false.” It is the weaker operational statement that the currently recovered proof architecture has no source-level closing lemma.

Neighboring R06 recovered the exact author-hosted source, the author open-problem index, the prior campaign attempt, and current literature queries. The source itself warns that the heuristic requires a difficult interchange of limits. The prior attempt identifies the same obstruction in a more concrete form: one needs a **uniform comparison** between

- the lattice minimum oriented path-cover quantity for rare closed edges, and
- the Poissonized continuum chain-cover / largest-antichain quantity,

strong enough to survive `n -> infinity` and then `p -> 1`.

Finite-grid optimization, simulation, a fixed-`p` limit, or a continuum first-order asymptotic does not negate this obstruction. Therefore the current evidence supports the admission negation:

\[
\boxed{\text{SOURCE-EXACT + CURRENT-OPEN-LOOKING does not yet imply READY CLOSABLE for P0219.}}
\]

This is a useful failure, because it identifies the missing object instead of merely repeating “PENDING.”

## 5. Method #20 — FIND WHY THE ALGORITHM FAILS

Apply the existing successor-admission algorithm gate by gate:

1. exact outside source — **PASS**;
2. current-open-looking status — **PASS** by bounded dated source/literature refresh;
3. posted/excluded conflict — no source-matching posted closure recovered;
4. same-ID ownership — no canonical P0219 claim at the current screen;
5. full-source CLOSABLE architecture — **FAIL / UNESTABLISHED**;
6. create-only dispatch — therefore forbidden.

The failure is specifically gate 5. The problem is not the value of the conjectured constant: the prior campaign normalization audit found two heuristic normalization slips that cancel, leaving the source constant `sqrt(2)` intact. The failure is also not a finite combinatorial core that can be certified by an exact checker. It is the absence of a uniform lattice-to-continuum stability/de-Poissonization theorem of the scale needed by the source.

A candidate closing statement would have to control the difference between the infinite-volume lattice path-cover density and the corresponding rare-defect Poisson width density by an error

\[
o(\sqrt{1-p})
\]

uniformly as `p -> 1`, or supply an alternative estimate with equivalent force. No recovered route currently contains that.

Hence the admission algorithm is doing useful mathematical work: it blocks a superficially one-line asymptotic from being mislabeled CLOSABLE when its only missing step is in fact a two-parameter uniformity theorem.

## 6. Method #27 — SWAP THE QUANTIFIERS

The exact obstruction becomes clearest after writing the quantifiers.

What the source target ultimately needs is a statement of the form

\[
\forall\varepsilon>0\ \exists p_0<1\ \forall p\in(p_0,1)\ \exists N(p,\varepsilon)\ \forall n\ge N:
\quad
\left|\frac{\mathbb E U(n,p)}{2n\sqrt{2(1-p)}}-1\right|<\varepsilon,
\]

or an equivalent infinite-volume formulation whose error is uniform enough near `p=1`.

The easy-looking directions usually give the opposite order: for every **fixed** `p<1`, take `n -> infinity`; or first Poissonize at a fixed rare-defect intensity/window and then take the continuum size to infinity. Those statements do not by themselves justify moving `p -> 1` through the large-`n` limit.

Thus swapping the quantifiers exposes why P0219 is not yet honestly CLOSABLE. A future admission should require a route that controls a whole near-critical parameter interval at once, not one `p` at a time. This is the same obstruction described qualitatively by the source as an interchange-of-limits problem, now stated as the exact uniformity obligation an eventual proof must discharge.

## 7. I0084 current-literature refresh

A bounded dated public-source refresh was run on 2026-09-19 UTC with queries centered on:

- `arXiv 1710.08240 Hasebe Ueda Conjecture 5.5 eventual unimodality stable process`;
- exact arXiv identifier `1710.08240` plus unimodality/stable-process terms;
- later 2025–2026 Hasebe/Ueda unimodality work.

The original arXiv/ALEA paper remains the source-matching hit. Current author publication pages expose later free-probability work, but the bounded search did not surface a later primary source explicitly resolving the frozen arXiv-v2 Conjecture 5.5 ordinary-`*` formulation. This is bounded negative evidence only, not a worldwide priority or novelty certificate.

No source-scope correction was found. In particular, nothing in this refresh authorizes replacing the arXiv asterisk by `boxplus`.

## 8. Audit and model-control state

No new version-matching outside audit of the frozen ordinary-`*` I0084 package appears in the exact repository delta. Prior P26/ALEA free-`boxplus` audit material remains scope-mismatched for the frozen arXiv ordinary-convolution branch and earns no new closure credit here.

The platform-control limitation also remains unchanged. The exposed scheduler/task surface used by this fleet has task identity/title, prompt, schedule/timing, and enabled-state controls, but no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort attestation, and no guaranteed hour-long execution control. Therefore `GPT-6 / maximum` remains a prompt request rather than an enforceable setting from this worker. Historical `You cannot modify this task` responses are authorization boundaries; the lawful route is the owning/authorized product/workspace/admin context or platform support, not duplication or bypass. This run made no scheduler change.

## 9. Disposition

No successor claim was created and no existing claim was overwritten.

R19 remains

`TERMINAL_WAITING_FOR_NEW_READY_DELTA`.

The next run should react only to a literal-changing event: a genuinely new populated source, a formal READY admission, an explicit owner-authorized release/reassignment of a full-source CLOSABLE target, a current-literature/source correction, or a source-level reduction that actually supplies the missing uniformity architecture without narrowing the source quantifiers.

P0219 is now a better-understood replenishment candidate, but it is **PENDING_NOT_READY**. R19 must not auto-promote it.

No code/checker artifact was created because no new finite mathematical claim was obtained. No shared root, other track, email, Drive, public posting, purchase, permission, or scheduler state was modified.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R19
  lane: CLOSABLE_OUTSIDE
  deployment: NEW-METHODS-2026-09-16
  frozen_source:
    id: I0084
    source: Hasebe-Ueda arXiv:1710.08240v2 Conjecture 5.5
    alpha: 1/2
    convolution: ordinary_classical_star_even_for_free_stable_law
    moment: exact_2_plus_alpha
    input_class: full_source_class
    skewness: original_source_conventions
  metric:
    name: complete_alpha_half_source_cases
    before: 2
    after: 2
  status: TERMINAL_WAITING_FOR_NEW_READY_DELTA
  successor_metric:
    name: E_READY_SUCCESSOR
    before: 0
    after: 0
  unchanged_count: UNKNOWN_TERMINAL_WAIT
  tried_moves: [2, 20, 27]
  delta_screen:
    compare_base: c12e905f7f2fede2b01d4d38f33fb60a25a7e9a0
    compare_head: fed7dd2fa59acb078a77781f4b16c67e6d549b4f
    ahead_by: 100
    behind_by: 0
    too_large: null
    P0219:
      source_state: SOURCE_EXACT_CURRENT_OPEN_LOOKING
      same_id_claim: ABSENT_AT_SCREEN
      readiness: PENDING_NOT_READY
      blocker: uniform_lattice_to_continuum_interchange_of_limits
      disposition: DO_NOT_AUTO_PROMOTE
    P0220:
      disposition: CLOSABLE_BUT_OWNED_R7_04
    I0130:
      disposition: ACTIVE_OWNED_CLOSABLE_NO_RELEASE
    R09_Blanc_Renaudie:
      disposition: SIX_RUN_HANDOFF_NOT_OWNER_RELEASE
  i0084_audits:
    new_version_matching_audit_this_delta: false
    mismatched_free_boxplus_audits_do_not_count: true
  remaining_obligation: >-
    Wait for a formal source-current full-scope ownership-clear READY CLOSABLE successor,
    or a literal-changing source/ownership/readiness delta. Do not reopen I0084 theorem work,
    do not run STUCK3 on the exhausted admission route, and do not auto-promote P0219.
  evidence:
    predecessor_report: runs/R19/2026-09-19_00-43-00_UTC__terminal-wait-p0220-owned-c0021-handoff_q8v3.md
    coordinator_status: operations/task_health/runs/2026-09-19T005400Z/status.md
    p0219_lead: runs/R01/20260919T0103Z_post_rotation_p0219_replenishment_lead_1_10_17_6d2f8a41.md
    p0219_screen: runs/R06/20260919T0127Z_successor_admission_p0219_source_current_uniformity_gate_54_a53c.md
    p0219_claim_path_at_screen: ABSENT
    web_refresh_date_utc: 2026-09-19
```

If a genuine READY delta appears, use three methods not equal to this run's `#2/#20/#27`; otherwise preserve the terminal handoff instead of manufacturing another stagnation lemma.