Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — NO MOVEMENT in the fixed Tang periodic-tree curvature metric: UNBOUNDED_ABOVE -> UNBOUNDED_ABOVE; supported unchanged count 4 -> 5. STUCK2 thinking-only run. Section-B moves actually tried: B11 DUALIZE; B21 ASK WHO ELSE HAS THIS SHAPE; B27 SWAP THE QUANTIFIERS.** The exposed task-control interface still has no model selector or reasoning-effort selector, so the requested GPT-6/maximum setting remains prompt text only and is not claimed as runtime fact.

Problem/source: Pengfei Tang, *A note on some critical thresholds of Bernoulli percolation*, arXiv:2012.01135v2 / Electron. J. Probab. 28 (2023), PDF **Question 4.11**: for a transitive graph or a periodic rooted tree, is the Bernoulli bond-percolation probability `theta(p)` concave on `(p_c,1)`? The current arXiv HTML auto-numbering renders the same concavity question as Question 4.12; I preserve the owner's/source-PDF locator Question 4.11.

Run ID: `20260916T2336Z_tang_stuck2_dual_reliability`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Current mathematical status: periodic-tree universal assertion **REFUTED mathematically / P26 closure audit still missing**; transitive-graph-only variant **OPEN**.  
Frozen metric: greatest rigorous lower bound for `theta''(p)` at a certified admissible parameter in the fixed periodic-tree candidate family.  
Metric before / after: `UNBOUNDED_ABOVE -> UNBOUNDED_ABOVE`.

No new theorem-sized claim or finite certificate is introduced in this STUCK2 run. In accordance with the owner's stuck policy, I do not manufacture another checker merely to prove that the already-saturated metric remained saturated.

# 1. Continuity, ownership, and required repository recovery

I continued from the newest own immutable state

`runs/R09/20260916T2232Z_tang_c2c4_recovery.md`

rather than restarting. Its retained state is:

1. a source-admissible finite-stem periodic-tree family refutes Tang's universal periodic-tree assertion;
2. the frozen curvature metric is **unbounded above** in that fixed family;
3. a strongly-connected finite-type directed-cover witness also has positive curvature, so the failure is not only a reducible stem pathology;
4. the structural finite-stem theorem explains why Tang's broad periodic-tree class is vulnerable to a finite root prefix;
5. the transitive exact probes `C3*C3`, simple `C2*C3`, and simple `C2*C4` are all strictly concave on their entire supercritical intervals;
6. the newest `C2*C4` proof has now received an independent exact R08 audit, but R08 is still only one distinct auditor track;
7. no P26 end-to-end Tang-Q4.11 audit was recovered.

Before the present strategy analysis I reread/recovered or queried the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, current `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, canonical claim `operations/claims/TANG-2020-Q4.11.md`, the newest own R09 report, newest R08 audit-bearing report, newest R10 report, and targeted P26/Tang audit searches. I also searched the repository by Tang's arXiv identifier, exact concavity wording, and the excluded I0055 alias.

The large intake JSONL files cannot be rendered row-for-row through the connector before truncation. I used exact-ID/source/ownership searches and do not claim a fictitious byte-for-byte visible reread of all approximately 780 intake rows.

The canonical Tang claim remains R09-owned but still literally says `PENDING_ADMISSION, not READY`; attacking workers do not rewrite the coordinator-owned claim file. `POSTED.md` does not exclude Tang Question 4.11. No conflicting Tang owner surfaced. The intake alias I0055 / Lyons--Peres Question 5.16 remains excluded from this assignment: Tang's Theorem 1.6 answers that different modified first-moment question.

# 2. Fresh source and literature check — dated 2026-09-17 Asia/Jerusalem / 2026-09-16 UTC

Primary source rechecked:

- https://arxiv.org/abs/2012.01135 , current v2;
- source model is Bernoulli **bond** percolation;
- Tang's current HTML states that every periodic tree is a directed cover of a finite directed graph and, after the explicit concave examples in Example 4.11, asks the concavity question;
- the current HTML labels the question `Question 4.12`, while the source PDF / campaign locator is `Question 4.11`.

Fresh bounded searches included:

1. exact Tang title + `concavity` + periodic tree / transitive graph;
2. arXiv `2012.01135` + later resolution / citing papers;
3. Pengfei Tang percolation work 2024--2026;
4. percolation-density concavity on transitive graphs;
5. branching-process survival-probability shape;
6. reliability-polynomial convexity / inflection-point literature;
7. free-product percolation and finite factor groups;
8. nonunimodular transitive percolation / grandmother-grandfather graph literature.

No later primary source resolving Tang's exact concavity question surfaced. Tang's visible 2026 work concerns negative correlation / spanning-subgraph questions rather than this concavity problem. Zhongyang Li's 2025 paper citing Tang concerns critical site cutsets, not this question. This is a bounded dated negative search, **not** a novelty certificate.

Two pieces of nearby literature matter to the strategy:

- Iva Kozakova, *Critical Percolation of Free Product of Groups*, Int. J. Algebra Comput. 18 (2008), 683--704, arXiv:math/0611668: the free-product critical probability reduces to finite-factor cluster-size data and is polynomial for finite factors. This supports the finite-factor compiler but does not address curvature of `theta`.
- Jonathan Hermon and Tom Hutchcroft, *Supercritical percolation on nonamenable graphs: isoperimetry, analyticity, and exponential decay of the cluster size distribution*, Invent. Math. 224 (2021): on nonamenable transitive graphs the supercritical percolation density is analytic. This legitimizes a pointwise `theta''` search in that class but gives no sign.

Network-reliability literature explicitly studies inflection and generalized convexity properties of finite reliability polynomials. Thus a finite factor's reliability shape is not automatically one-signed. That makes a broader finite-Cayley-factor search more plausible than continuing only the cycle family, but it is not itself a Tang solution.

# 3. Why this run is STUCK2

The fixed metric was already `UNBOUNDED_ABOVE` and therefore is mathematically saturated: there is no larger finite value to report. It remained unchanged in the STUCK1 run and in the completed `C2*C4` recovery. The newest supported count before this run was 4; this invocation takes it to 5.

The periodic-tree disjunct of Tang's literal universal question is already answered negatively. The remaining mathematical research question is the separate transitive-graph-only variant. The remaining portfolio-closure obligation for the periodic-tree result is external certification, specifically a P26 audit.

This is therefore the second mandatory thinking-only stuck episode, not another adjacent-lemma run.

## (a) Exact statement that blocks

For the transitive-only variant, the blocker is the sign problem

\[
\boxed{\text{either }\forall G\text{ transitive},\quad \theta_G''(p)\le 0\text{ on }(p_c(G),1),
\quad\text{or exhibit }(G,p)\text{ with }\theta_G''(p)>0.}
\]

When a chosen graph is not known a priori to have a twice differentiable supercritical branch, the equivalent midpoint concavity inequality must be used instead. For nonamenable transitive graphs the Hermon--Hutchcroft analyticity result removes that regularity issue but not the sign issue.

The separate closure blocker for the already-refuted periodic-tree disjunct is

`P26 end-to-end Tang-Q4.11 periodic-tree audit = PASS`.

No such P26 PASS is currently recovered.

## (b) Routes tried and the precise failure of each

1. **Finite stem over a binary tail:** succeeds for periodic trees and gives unbounded positive curvature, but the stem singles out the root and destroys vertex transitivity.
2. **Strongly-connected finite-type directed cover:** succeeds as a stronger periodic-tree counterexample, but strong connectivity of the finite type graph is not vertex transitivity of the infinite tree.
3. **Structural finite-stem instability:** explains the periodic-tree failure generally; the mechanism is intrinsically a one-time rooted prefix.
4. **Free product `C3*C3`:** exact physical branch; strictly concave, so the first global symmetrization points opposite to the desired counterexample.
5. **Simple free product `C2*C3`:** local factor asymmetry while retaining global transitivity; still strictly concave.
6. **Simple free product `C2*C4`:** the STUCK1 recovery; exact factor PGF, exact physical branch, and an exact global sign proof again give strict concavity.
7. **Generic finite-type recursion:** branch selection and differentiation close for independent descendant/block systems but do not cover generic transitive graphs with overlapping cycles.
8. **First-order percolation inequalities:** Russo/sharpness/transitivity control growth but not the second variation of the total pivotal mass.

The newest R08 report independently reconstructs the `C2*C4` algebra and records

`R08-AUDIT-R09-TANG-Q411-C2C4-05 = PASS`.

That improves confidence in the special case but does not create a second distinct auditor for the source-level periodic-tree closure, because the earlier Tang audits also came from R08.

## (c) What a proof needs that no tried route contains

A transitive counterexample needs all of:

1. an explicitly vertex-transitive infinite graph;
2. the **physical** percolation branch above the true `p_c`, not an algebraic fixed point chosen by convenience;
3. exact or certified second-order control proving a midpoint violation or `theta''(p)>0`;
4. a mechanism that mimics the positive-curvature series delay of the rooted stem without leaving a distinguished root defect.

A universal transitive concavity theorem would instead need a second-order structural inequality. In differentiable form, it must control the derivative of total pivotal mass. First-order sharpness and FKG do not supply that sign.

The tractable free-product class has one additional missing ingredient: a criterion on finite factor cluster PGFs that forces or forbids positive curvature after the physical fixed point is composed.

## (d) Simplest special case still unproved after `C2*C4`

Continuing from cycles to the first genuinely non-cycle finite Cayley factor, a natural next concrete graph is

\[
G_{K_4}=\operatorname{Cay}\!\left(C_2*(C_2\times C_2),\;\{a\}\cup((C_2\times C_2)\setminus\{e\})\right).
\]

The `C_2` factor is one edge and the `C_2\times C_2` factor with all three nonidentity generators has Cayley graph `K_4`. Hence this is a simple connected vertex-transitive free-product Cayley graph with an exact finite factor containing six bond variables. It is the smallest new factor-shape test after the solved cycle cases. **No curvature sign is claimed here.**

## (e) Nearest solved problem and what its proof uses that the blocker lacks

Kozakova's free-product reduction and the completed R09 `C2*C3`, `C3*C3`, `C2*C4` calculations are the nearest solved mechanisms. They have a tree of finite factor cosets, so entering one factor exposes finitely many vertices and the continuations through the other factor are independent. This yields a finite extinction fixed-point system.

A generic transitive graph lacks this independent finite-block decomposition. Overlapping cycles create history dependence and destroy the small fixed-point state space. Conversely, remaining inside free products preserves exact solvability but may be too restrictive if a hidden positivity principle forces extinction convexity there.

# 4. B11 — DUALIZE: concavity of survival becomes convexity of extinction

For a finite-type/block exploration write the physical extinction vector as

\[
q(p)=F(p,q(p)).
\]

Let `J=D_qF` on the physical supercritical branch. In every exact block example already solved by R09, the stable extinction branch has spectral radius `rho(J)<1`, so formally and rigorously on an analytic branch

\[
q'=(I-J)^{-1}F_p,
\]

and

\[
q''=(I-J)^{-1}\left(F_{pp}+2F_{pq}q'+F_{qq}[q',q']\right).
\]

Because `J` is entrywise nonnegative,

\[
(I-J)^{-1}=\sum_{n\ge0}J^n
\]

is entrywise nonnegative. This isolates the real sign obstruction: one should not repeatedly solve a high-degree `theta` formula and differentiate it; one should search for a factor system where the **second-order forcing vector** on the right becomes sign-indefinite strongly enough to make the root extinction probability concave.

Since `theta=1-Q`, where `Q` is the root extinction probability, a transitive counterexample is exactly a point with

\[
Q''(p)<0.
\]

For a two-factor free product with extinction coordinates `(u,v)`, the root extinction is the product `Q=uv`. The solved cycle examples all give `Q''>0` on the supercritical interval. The dual formulation explains what an exact search must target.

This is a strategy reduction, not a new source theorem.

# 5. B21 — ASK WHO ELSE HAS THIS SHAPE

Three neighboring literatures now point to a sharper search space:

1. **free-product percolation** (Kozakova): finite factors reduce the threshold to polynomial cluster data;
2. **network reliability:** finite connectivity polynomials can have inflection/shape changes, so richer finite factors are not forced to behave like cycles merely because their coefficients are nonnegative;
3. **supercritical analyticity on nonamenable transitive graphs** (Hermon--Hutchcroft): if a candidate free product or another nonamenable transitive graph is found, a local second-derivative certificate is a legitimate source-level refutation route.

The literature search did not locate a theorem saying survival probability on all free products of finite groups is concave. It also did not locate a Tang-Q4.11 resolution. Therefore the finite-factor curvature criterion is a genuine unresolved intermediate route, not a cited theorem being rediscovered.

# 6. B27 — SWAP THE QUANTIFIERS

The recent search asked, one graph at a time,

`for this transitive graph, is theta concave?`

The more useful restricted existential is

\[
\boxed{\exists\text{ finite Cayley factors }H,K\text{ and }p>p_c(H*K)\text{ such that }Q_{H*K}''(p)<0?}
\]

If YES, then `theta''>0` and Tang's transitive half is refuted by an exact vertex-transitive graph. If NO for a rigorously characterized class of factor PGFs, the result would be a real PARTIAL theorem explaining why all current tractable transitive examples are concave and would tell the next worker to leave independent-block geometries entirely.

This quantifier swap is better than continuing `C2*C_m` serially: it searches the finite **factor reliability shape**, not just factor size.

# 7. Exactly one STUCK2 recovery choice

I choose exactly one Section-I recovery:

**REDUCE THE OBSTRUCTION TO A FINITE COMPUTATION AND RUN IT.**

If this Tang slot receives one final research invocation before the six-unchanged CLOSABLE retirement point, use the dual sensitivity compiler above to perform an **exact**, bounded search over small finite Cayley factors rather than another cycle-by-cycle derivation. The first explicit case is `C2*K4` in the notation above.

The finite algorithm is:

1. enumerate every edge subset of each finite factor and compute the exact cluster PGF `F_H(p,t)` and `F_K(p,t)`;
2. certify the threshold from the two-type mean product;
3. select the physical extinction fixed point as the minimal fixed point in `[0,1]^2`, with an exact isolation interval;
4. evaluate the implicit first/second derivative system above using exact rational-polynomial/Sturm or interval certificates;
5. certify `Q''<0` on a rational parameter interval if a candidate exists;
6. if no candidate appears in the bounded family, record the exact family searched and rotate rather than adding another unmotivated special case.

This is the final high-value recovery because the next unchanged invocation would bring the supported count to 6, at which point the controlling policy retires a CLOSABLE target from active research. Even a new transitive PARTIAL theorem cannot move the already-saturated periodic-tree metric, so no seventh Tang research run should follow an unchanged sixth run.

Planned Section-B methods for that final recovery, distinct from this run: **B8 GO THE OTHER WAY AND DISCRETIZE; B16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE; B17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.**

# 8. Audit and package state

Distinct auditor tracks currently recovered for the source-matching periodic-tree refutation: **one (R08)**.

R08 audit IDs include:

- `R08-AUDIT-R09-TANG-Q411-PERIODIC-01 = PASS`;
- `R08-AUDIT-R09-TANG-Q411-STRONG-CONNECTED-02 = PASS`;
- `R08-AUDIT-R09-TANG-Q411-CAYLEY-03 = PASS` on a later transitive probe;
- newest `R08-AUDIT-R09-TANG-Q411-C2C4-05 = PASS` on the complete `C2*C4` special case.

Repeated R08 passes count as **one** independent auditor. Fresh repository search still finds no `P26-AUDIT-R09` / Tang-Q4.11 end-to-end PASS. Therefore the owner's closure gate is not satisfied and no `paper_...` folder is created.

R10 is not audit-ready. Its newest report is a six-run handoff for I0070: an author-side full-source proof candidate is preserved, but `0/2` required external closure audits are recovered and no source-matching paper package is present. I therefore do not invent an R09 audit of R10.

# 9. Model / reasoning control and denied-task escalation

The requested model fix is still not available in this worker interface. The exposed task-control schema provides title, prompt, schedule, enabled state and timing mode. It exposes **no model selector, no reasoning-effort selector, and no authenticated runtime telemetry**. Therefore I cannot truthfully set or verify GPT-6/maximum here.

What would change this:

1. the product/API must expose model and reasoning-effort fields for native tasks; and
2. the runtime report must expose authenticated execution metadata rather than relying on prompt text.

The repository records earlier `You cannot modify this task` failures for P26/P01/P03 in one context, while a later authorized owner-side context successfully updated P26. This establishes that the modification denial is context/ownership-specific. The legitimate workaround is the native task's owning workspace/interface or platform support/ownership repair. A duplicate schedule, permission bypass, or repository edit pretending to be a native task change is not legitimate.

No scheduler modification is attempted in this run because the current deployment expressly forbids worker-side scheduler changes.

# 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R09
  run_id: 20260916T2336Z_tang_stuck2_dual_reliability
  source: "Pengfei Tang, A note on some critical thresholds of Bernoulli percolation, arXiv:2012.01135v2 / EJP 28 (2023), PDF Question 4.11"
  target: "decide concavity of theta(p) on (p_c,1); periodic-tree disjunct first"
  metric: "greatest rigorous lower bound for theta''(p) at a certified admissible parameter in the fixed periodic-tree candidate family"
  before: UNBOUNDED_ABOVE
  after: UNBOUNDED_ABOVE
  movement: false
  supported_unchanged_count_before: 4
  supported_unchanged_count_after: 5
  stuck_episode: 2
  status:
    periodic_tree_source_disjunct: "REFUTED mathematically; P26 closure audit pending"
    transitive_graph_only_variant: OPEN
  methods_this_run: [11, 21, 27]
  new_theorem_claims: []
  new_exact_artifacts: []
  exact_evidence_retained:
    - "runs/R09/20260916T173216Z_tang_q411_stem_counterexample.md"
    - "runs/R09/20260916T1832Z_tang_q411_strong_counterexample.md"
    - "runs/R09/20260916T2232Z_tang_c2c4_recovery.md"
  audit_ids:
    - "R08-AUDIT-R09-TANG-Q411-PERIODIC-01=PASS"
    - "R08-AUDIT-R09-TANG-Q411-STRONG-CONNECTED-02=PASS"
    - "R08-AUDIT-R09-TANG-Q411-C2C4-05=PASS"
  distinct_auditor_count_for_source_closure: 1
  missing_closure_evidence:
    - "P26 end-to-end Tang Q4.11 periodic-tree PASS"
  recovery_choice: "reduce the transitive free-product obstruction to an exact finite Cayley-factor computation"
  first_recovery_case: "C2 * (C2 x C2), with K4 factor generated by all three nonidentity elements"
  next_methods: [8, 16, 17]
  six_run_gate: "one more unchanged invocation reaches mandatory CLOSABLE retirement/handoff"
```

# 11. Final disposition

The periodic-tree mathematics is not stuck: it is already a negative answer, with an unbounded curvature witness family. What is stuck is (i) an already-saturated metric, (ii) the external P26 closure audit, and (iii) the optional stronger transitive-only question.

This STUCK2 run therefore stops serial special-case proof production and identifies one final exact recovery: search finite Cayley-factor reliability shapes through the dual extinction Hessian. If that final recovery does not alter the frozen metric—which is already `UNBOUNDED_ABOVE`—the six-run rule requires R09 to leave Tang active research and preserve the result for audit/closure rather than run a seventh Tang attack.

No email, Drive operation, public posting, purchase, permission change, workflow execution, scheduler mutation, shared-root edit, claim-file edit, or peer-file edit is made in this run.