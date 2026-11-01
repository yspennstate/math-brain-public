Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate. Methods #10 DERANDOMIZE, #20 FIND WHY THE ALGORITHM FAILS, #28 REPLACE FOR ALL WITH FOR TYPICAL.**

# R15 CLOSABLE OUTSIDE — disjoint-support tensorization and the first necessary overlap for Talagrand 10.9

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

All new deductions below are **SELF_CHECK_ONLY** unless explicitly identified as prior art. No source closure, novelty certificate, or independent audit is claimed.

## 1. Continuity, exact Brownian source, and why I0076 is not reopened

I continued from the current repository state and reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the current coordinator report `operations/task_health/runs/2026-09-18T095900Z/status.md`;
- the controlling six-run handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- the immediately preceding R15 report `runs/R15/20260918_0957Z_successor_admission_f0111_ifra_oneatom_w55c.md`;
- the neighboring R20 F0111 handoff `runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md`;
- the I-intake location `probability_1000_intake_I_20260914/problems.jsonl` and current source/ownership searches.

I also reread the primary Burdzy--Scheutzow PDF, including the source page itself rather than relying on a secondary statement. Definition 2.1 says that `X` is FBM if there are random times `S_n -> -infinity` a.s. such that every future increment process from `S_n` is standard Brownian motion; BBM is the time-reversed notion; 2BM means that at one random origin the two centered half-paths are independent **standard Brownian motions**. Problem 7.2 assumes only FBM + BBM and the existence of a random time `T` at which the two complete centered half-paths are independent. There is no stopping-time hypothesis on `T`, and neither seam half is separately assumed Brownian.

Primary source checked 2026-09-18: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958 / PTRF 160 (2014), Definition 2.1 and Problem 7.2, `https://arxiv.org/pdf/1302.6958`. The rendered PDF pages containing both Definition 2.1 and Problem 7.2 were inspected. The University of Washington publication page likewise still identifies the paper as PTRF 160 (2014), 95--126. A bounded dated search for the exact title/problem wording and later/citing work located no accessible paper explicitly claiming to settle exact Problem 7.2; that is negative search evidence only.

The six-run handoff remains controlling. The source-Theorem-6.1 candidate was eliminated because it has no source-required independent real seam. The later alternating Brownian-prefix/BES candidate reached FBM, BBM and exact seam independence, but the excursion/Palm argument proved it is actually 2BM. Hence there is **no surviving frozen counterexample candidate**. The marked Brownian-cell / sparse copied-continuous-block idea is still only an architecture, not a candidate whose third or fourth source obligation may be counted.

Accordingly I did not manufacture movement in the original source metric. The historical carried value remains `2/4`, status `OPEN / PARTIAL / RETIRED-HANDOFF`, and I0076 is not reopened.

The strict successor metric remains

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run`.

Before: `0`. After: `0`.

The current coordinator still records newly certified READY reserve entries as zero. `operations/claims/F0111.md` remains absent on current `master`. No successor claim is created.

With no lawful fresh CLOSABLE assignment, I continue F0111 only as **successor-screening mathematics**, not as an R15 assignment.

## 2. Screening source retained: Talagrand Problem 10.9

Source: Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Definition 10.1 and Problem 10.9.

For a finite up-class `A` on a coordinate set `S`, let `zeta_t` be the product law with

`P_t(i in X)=1-exp(-t_i)`

and define the hazard

`F_A(t)=-log(1-zeta_t(A)).`

Talagrand's `A in C_gamma` condition says that for every base point `q>=0` there must be a multilinear polynomial

`P(t)=sum_{empty != I subset S} beta_I t_I`, `beta_I>=0`,

such that

`F_A(t)<=P(t)` for every `t>=0`

and

`P(gamma q)<=gamma F_A(q)`.

Problem 10.9 asks whether one universal `gamma>0` works for every cardinality threshold

`A_{n,k}={X subset [n]: |X|>=k}`.

Primary source checked 2026-09-18 at `https://michel.talagrand.net/preprints/small.pdf`; the PDF page containing Problem 10.9 was inspected directly. The same page immediately begins Proposition 11.2, where Talagrand exploits **disjoint supports** to obtain independence of block events in a different conjectural route. Thus the disjoint-support independence mechanism used below is source-adjacent prior art, not something I claim to have invented.

The preceding R15 report established two facts used below:

1. **KNOWN / prior-art transfer:** for every finite nontrivial up-class and `0<=lambda<=1`,

   `F_A(lambda q)<=lambda F_A(q)`,                                                (2.1)

   via the IFRA first-passage theorem for coherent systems (Brown--Chaganty 1983; Shanthikumar--Shaked 1987).

2. **SELF_CHECK_ONLY one-atom no-go:** if `u=gamma q` and one atom `w delta_t` satisfies

   `w t_I<=u_I` for every nonempty `I`,

   then

   `w F_A(t)<=F_A(u)<=gamma F_A(q)`.                                              (2.2)

The weak-dual certificate carried from the earlier R15 reports says that a positive measure `mu` could refute `C_gamma` only if it obeys every monomial-moment budget

`int t_I dmu(t) <= (gamma q)_I`                                                   (2.3)

while nevertheless giving

`int F_A(t) dmu(t) > gamma F_A(q)`.                                               (2.4)

This run attacks the first genuinely multi-atom possibility.

## 3. Method #10 — DERANDOMIZE: disjoint-support dual witnesses tensorize and cannot refute

For `B subset S`, define the trace up-class

`A|_B = {Y subset B : Y, viewed as a subset of S, belongs to A}`.

If a hazard vector `t` is supported inside `B`, then outside coordinates are absent almost surely, so exactly

`F_A(t)=F_{A|_B}(t_B)`.                                                           (3.1)

### Theorem R15-F0111-DISJOINT

Let `A` be a finite nontrivial up-class, let `0<gamma<=1`, put `u=gamma q`, and let

`mu = sum_{a=1}^r w_a delta_{t^(a)}`

be a finite positive measure satisfying all weak-dual budgets (2.3). Suppose the coordinate supports

`B_a={i:t_i^(a)>0}`

are pairwise disjoint. Then

`sum_a w_a F_A(t^(a)) <= F_A(u) <= gamma F_A(q)`.                                 (3.2)

Consequently no weak-dual refutation can be built from atoms with pairwise disjoint coordinate supports.

#### Proof

Fix an atom `a`. For every nonempty `I subset B_a`, all other atoms vanish on at least one coordinate of `I`, because the supports are pairwise disjoint. Thus the global constraint (2.3) reduces on this block to

`w_a t_I^(a) <= u_I` for every nonempty `I subset B_a`.                           (3.3)

Apply the preceding one-atom theorem to the trace up-class `A|_{B_a}`, with base vector `u_{B_a}` and `gamma=1`. Using (3.1),

`w_a F_A(t^(a)) <= F_{A|_{B_a}}(u_{B_a}).`                                       (3.4)

Now sample `X` from the product law with hazard vector `u`. Define

`E_a={X intersect B_a belongs to A|_{B_a}}`.

Because `A` is increasing, `E_a subset {X in A}`: if `X intersect B_a` is already an element of `A`, then adding coordinates outside `B_a` cannot leave `A`.

The blocks `B_a` are disjoint, so the events `E_a` are independent. Therefore

`P_u(X notin A) <= P_u(intersection_a E_a^c)
                 = product_a P_u(E_a^c).`

Taking `-log` gives

`F_A(u) >= sum_a F_{A|_{B_a}}(u_{B_a}).`                                         (3.5)

Summing (3.4) and using (3.5) proves

`sum_a w_a F_A(t^(a)) <= F_A(u).`

Finally (2.1) with `u=gamma q` gives `F_A(u)<=gamma F_A(q)`. QED.

### Why this is stronger than the previous one-atom screen

The preceding report eliminated support size one. The theorem above eliminates **arbitrarily many atoms at once** whenever their coordinate supports do not interact. Thus merely randomizing or mixing many independent-coordinate one-atom attempts cannot create a negative witness.

The only place where a multi-atom dual witness can gain anything beyond the one-atom theorem is through **overlap of coordinate supports**.

### Connected-component reduction

Form the support-intersection graph `G_mu`: its vertices are the atoms and two atoms are adjacent iff their coordinate supports intersect.

If `G_mu` is disconnected, its connected components use pairwise disjoint coordinate unions. Applying the preceding block argument componentwise shows the following exact reduction:

> If a feasible dual measure `mu` refutes (2.4), then at least one connected component of `G_mu`, restricted to its own coordinate union, already refutes the corresponding trace problem.

For Talagrand's threshold family, a trace on a coordinate union `U` is again the same cardinality threshold `{Y subset U: |Y|>=k}` (or the empty event when `|U|<k`). Therefore any **minimal-support** weak-dual counterexample to Problem 10.9 may be assumed to have connected support-intersection graph. Combining with the one-atom theorem, it must have at least two atoms and at least one genuine overlap.

This is the useful derandomization: disconnected atom clouds do not create synergy and can be discarded component by component.

## 4. Method #20 — FIND WHY THE ALGORITHM FAILS: FKG reverses the needed inequality on overlapping blocks

The proof above identifies exactly where the naive tensorization algorithm stops.

For two blocks `B_1,B_2`, define `E_1,E_2` as above. If the blocks are disjoint, independence gives

`-log P(E_1^c intersect E_2^c)
 = -log P(E_1^c)-log P(E_2^c)`.                                                   (4.1)

This equality is what pays for summing the two local one-atom bounds.

When the blocks overlap, `E_1` and `E_2` are increasing events in a product measure, so `E_1^c,E_2^c` are decreasing. Harris--FKG gives

`P(E_1^c intersect E_2^c) >= P(E_1^c)P(E_2^c)`,

hence

`-log P(E_1^c intersect E_2^c)
 <= -log P(E_1^c)-log P(E_2^c)`.                                                  (4.2)

That is the **opposite direction** from the additive lower bound needed by the disjoint-support proof.

The global event `{X in A}` still contains `E_1 union E_2`, so its hazard dominates the union hazard, but (4.2) shows that positive correlation can create an exact deficit against the sum of the local hazards. A successful two-atom negative witness would have to exploit precisely this overlap/correlation deficit while simultaneously satisfying all mixed monomial budgets.

This is a sharper obstruction than the statement “two atoms interact”: the missing quantity is the FKG overlap deficit

`Delta(E_1,E_2)
 = log( P(E_1^c intersect E_2^c) /
        (P(E_1^c)P(E_2^c)) ) >= 0`.                                               (4.3)

Any attempt to extend the one-atom argument to two atoms must either control (4.3) from the moment budgets or construct a family where it overwhelms the base-point budget.

## 5. Method #28 — REPLACE FOR ALL WITH FOR TYPICAL: sparse random supports are asymptotically doomed

The disjoint-support theorem gives an exact probabilistic screening rule before any coefficient optimization is done.

Take `r` atom supports independently and uniformly from the `m`-subsets of `[n]`. If `rm<=n`, the exact probability that all supports are pairwise disjoint is

`prod_{j=0}^{r-1} [ C(n-jm,m) / C(n,m) ].`                                       (5.1)

For a pair of independently uniform `m`-sets,

`P(B_1 intersect B_2 != empty)
 = 1 - C(n-m,m)/C(n,m)
 <= m^2/n`,                                                                       (5.2)

where the last inequality is the union bound over the `m` points of `B_1`. Hence

`P(some pair overlaps) <= C(r,2) m^2/n`.                                         (5.3)

Conditional on pairwise disjointness, Theorem R15-F0111-DISJOINT rules out a weak-dual refutation **for every choice of atom values and weights satisfying the budgets**. Therefore any random sparse-support search of this form has success probability at most the right side of (5.3), regardless of how the coefficients are tuned after the supports are revealed.

In particular, for fixed `r` and `m=o(sqrt(n))`, a typical random sparse-support candidate is asymptotically unable to refute Talagrand's condition. A serious negative search must deliberately engineer an overlap-connected support pattern rather than spray sparse atoms independently across coordinates.

No simulation is used in this conclusion. Equations (5.1)--(5.3) are exact/combinatorial or elementary union bounds.

## 6. Prior-art and current-literature audit

Dated 2026-09-18 searches included exact combinations of:

- `Talagrand C_gamma positive polynomial up-class disjoint support`;
- `Problem 10.9 Are Many Small Sets Explicitly Small`;
- `card X C_gamma Talagrand threshold`;
- later work citing Talagrand's threshold questions.

The bounded search recovered Talagrand's STOC paper, DeMarco--Kahn (2015), Frankston--Kahn--Park (2022), Park--Pham/Kahn--Kalai threshold work, and Warnke (2024), but no accessible source explicitly stating a resolution of the exact heterogeneous-`q`, positive-multilinear-majorant Problem 10.9. This is **not** a worldwide openness certificate.

The most relevant source-adjacent prior art is Talagrand's own Proposition 11.2 immediately after Problem 10.9: for a different part of his framework he treats a family with disjoint supports and uses independence of the resulting block events. Accordingly, the independence mechanism in Theorem R15-F0111-DISJOINT is plainly folklore/source-adjacent. The exact weak-dual tensorization, overlap-graph reduction, and sparse-random-support corollary were not located in the bounded search; their publication novelty is **UNVERIFIED**.

I therefore do not call F0111 solved, refuted, CLOSABLE, or owned by R15. Its disposition remains

`OPEN-looking / screening only / HARD-leaning / NOT CLOSABLE-ready / NOT CLAIMED`.

## 7. Validation discipline

I wrote the idea and proof before considering code. No numerical path samples, Monte Carlo, or floating optimization are used as evidence for Brownian laws or for the Talagrand theorem above.

No exact-arithmetic checker was created: the new load-bearing statements are symbolic analytic/combinatorial arguments written on the page, not a finite enumeration. Creating a checker for unchanged `E_ready=0` would be ceremonial and contrary to the 90/10 instruction.

No independent audit was requested because there is no source closure claim. Every new theorem in Sections 3--5 remains `SELF_CHECK_ONLY` pending any later use in a closure package or paper.

## 8. Model / scheduler-control boundary

The actually running model is GPT-5.6 Sol. Authenticated reasoning-effort telemetry is unavailable, so the reasoning level is UNVERIFIED. This is not GPT-6 maximum.

The exposed scheduler/task API still offers prompt/title, schedule or relative start, timing mode, and enabled state. It still exposes **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long runtime control**. Therefore GPT-6 / maximum remains prompt-only from this surface.

The historical P26 ID recorded in the operations manifest once returned `You cannot modify this task`; later repository evidence records a successful update from an authorized context. The lawful workaround is therefore the owning/authorized product or admin context, or platform support that exposes and attests the model/reasoning controls. Duplication or permission bypass is not a legitimate workaround.

No scheduler, permission, email, Drive, public-posting, purchase, or workflow action was taken.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  allocation: CLOSABLE_OUTSIDE
  repository: yspennstate/math-open-problems
  branch: master
  predecessor:
    source: "Burdzy-Scheutzow, Forward Brownian Motion, Problem 7.2 / I0076"
    source_hypothesis_preserved: "FBM + BBM + independence of complete centered half-paths at arbitrary random T; no stopping-time strengthening"
    historical_metric_name: source_matching_obligations_for_one_frozen_counterexample
    historical_metric_before: "2/4"
    historical_metric_after: "2/4"
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    surviving_frozen_candidate: false
    active_research_this_run: false
  successor_gate:
    metric_name: E_ready
    metric_before: 0
    metric_after: 0
    movement: none
    unchanged_count: UNKNOWN
    claim_created: false
  tried_moves: [10, 20, 28]
  screening:
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9 / F0111"
    disposition: "OPEN-looking / screening only / HARD-leaning / NOT CLOSABLE-ready / NOT CLAIMED"
    exact_results:
      - "SELF_CHECK_ONLY: any feasible weak-dual measure with pairwise disjoint atom supports obeys integral F_A dmu <= F_A(gamma q) <= gamma F_A(q), for every finite nontrivial up-class A"
      - "SELF_CHECK_ONLY: any minimal-support weak-dual counterexample can be reduced to an overlap-connected atom-support graph; support size one is already impossible"
      - "SELF_CHECK_ONLY: the tensorization algorithm fails at overlap because Harris-FKG gives the reverse inequality for the union-hazard versus the sum of local hazards"
      - "SELF_CHECK_ONLY: r independent uniform m-supports can only refute on the overlap event, whose probability is at most C(r,2)m^2/n"
    prior_art:
      - "Talagrand Proposition 11.2 uses disjoint-support independence in an adjacent part of the source; mechanism is not claimed novel"
      - "Brown-Chaganty / Shanthikumar-Shaked IFRA radial inequality carried from the preceding report"
    remaining_obligation: >-
      A source closure still requires one universal gamma and q-adaptive positive multilinear
      majorants for every threshold n,k,q, or an exact counterexample. The weak-dual negative
      route is now forced into an overlap-connected multi-atom configuration; the first unresolved
      case is genuinely overlapping two-atom support.
  evidence:
    - "runs/R15/20260918_0957Z_successor_admission_f0111_ifra_oneatom_w55c.md"
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md"
    - "operations/task_health/runs/2026-09-18T095900Z/status.md"
    - "Burdzy-Scheutzow arXiv:1302.6958, Definition 2.1 and Problem 7.2"
    - "Talagrand STOC 2010, Definition 10.1, Problem 10.9, Proposition 11.2"
  finite_checker_needed: false
  audit_ids: []
  closure_claim: false
  next_methods: [14, 22, 29]
```

## 10. Next cursor

If no strict CLOSABLE successor is admitted before the next invocation, do **not** return to I0076 and do **not** repeat disjoint-support or one-atom arguments. The first unresolved negative object is an **overlap-connected two-atom dual measure**. Fresh methods reserved for that screen are **#14 FIND THE GROUP ACTING**, **#22 READ THE FAILURES**, and **#29 ADD THE POINTS AT INFINITY**: quotient the two-atom overlap pattern by coordinate permutations, read the exact places where Talagrand's disjoint-block stability argument loses independence, and compactify ratios of shared/private hazards to identify boundary extremizers before any finite computation.

**NO I0076 REOPENING. NO F0111 CLAIM. R15 remains `SUCCESSOR_ADMISSION_REQUIRED`.**