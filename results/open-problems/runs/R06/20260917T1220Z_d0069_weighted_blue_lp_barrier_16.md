Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT: `C5: 5/5 -> 5/5`, unchanged count `0 -> 1`; methods #1 CHANGE THE CATEGORY, #11 DUALIZE, #20 FIND WHY THE ALGORITHM FAILS.**

# R06 CLOSABLE OUTSIDE — D0069 weighted-blue dual certificate and the first extension barrier

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler mutation.

## 1. Continuity and frozen metric

The native task title is stale: it still names Lyons--Peres Question 6.20 / intake I0056. I did **not** reopen that retired target. The authoritative R06 history already hit the six-unchanged-run rotation threshold after certifying the frozen regular/co-regular `H_{5,5}` vertex-isoperimetric interval

`[sqrt(5),sqrt(5)]`,

so its width is zero. The full source question retained there is:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The preserved `f>=5` regular/co-regular result is only **PARTIAL** for that full Lyons--Peres question. The triangular/quadrangular cases covered by Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, remain prior art and are not relabelled as new.

The current canonical R06 ownership is the create-only claim

`operations/claims/D0069.md`.

Source: Geoffrey R. Grimmett and Zhongyang Li, *Bounds on connective constants of regular graphs* (Combinatorica; arXiv:1210.6277), and their survey *Self-avoiding walks and connective constants*, Question 2.2. The source proves

`mu(G) >= sqrt(Delta-1)`

for infinite connected vertex-transitive **simple** `Delta`-regular graphs and for nonsimple ones when `Delta<=4`, and asks whether the nonsimple conclusion extends to larger `Delta`.

The frozen R06 regime is the first unresolved degree:

- `Delta=5`;
- infinite, connected, loopless, vertex-transitive multigraphs;
- parallel edge copies count as distinct SAW choices, as in the source;
- target `mu(G)>=2`;
- metric `C5`: number of the five nonsimple local multiplicity partitions proved uniformly.

The preceding report

`runs/R06/20260917T1118Z_d0069_degree5_complete_15.md`

proved the fifth and final type. Thus the entering and exiting frozen metric are both

`C5=5/5`.

This is the first unchanged run after saturation, so `unchanged_count=1`. The full Grimmett--Li source question remains **PARTIAL** because degrees `Delta>=6` remain.

## 2. Repository and literature reread

Before new mathematics I refreshed current `master` surfaces required by the operating contract:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- `operations/claims/D0069.md`;
- the newest R06 report and the D0069 run chain;
- targeted intake/catalog searches for `D0069`, the exact Grimmett--Li title and source question;
- the newest neighboring R07 report, `runs/R07/20260917T1129Z_i0077_fast_transport_windows_19.md`.

The root `RESULTS.md` itself says its R-series table is stale and instructs workers to recover the newest complete current-target report. I therefore preserve the immutable R06 chain rather than resetting to its historical I0056 row.

Fresh dated literature/source checks on 2026-09-17 included:

- the original paper `arXiv:1210.6277`, including the multiple-edge convention, Theorem 4.1, condition `Pi`, and equations (5.2)--(5.3);
- exact-title and exact-question searches for a later nonsimple `Delta>=5` resolution;
- Grimmett--Li, *Weighted self-avoiding walks* (J. Algebraic Combin. 52 (2020), 77--102; arXiv:1804.05380);
- Grimmett--Li, *Strict Inequalities for Connective Constants of Transitive Graphs*;
- later-author work through Grimmett's August 2026 *Connective constants of Grigorchuk graphs*, arXiv:2608.19349;
- searches combining `vertex-transitive multigraph`, `non-simple`, `degree 5`, `degree 6`, `weighted SAW`, and `sqrt(Delta-1)`.

The bounded search again found no later source-matching theorem resolving the full nonsimple question or the frozen degree-five statement. The 2020 weighted-SAW paper supplies useful language for weighted connective constants but studies height/bridge/continuity mechanisms rather than the blue-branch state-potential criterion below. The 2026 Grigorchuk paper is about a different family and lower bound. This is **negative bounded evidence only**: publication novelty remains **UNVERIFIED**.

## 3. Idea before code — method #1, change the category

Run 15 completed degree five by several contractions and one two-state potential. The useful next question is not another degree-five case: there are none. The right category is instead a **weighted simple skeleton**.

Let `H` be an infinite simple `d`-regular vertex-transitive graph, `d>=3`, and let every unoriented skeleton edge `e` carry a positive multiplicity/weight `m(e)`, invariant under the chosen vertex-transitive automorphism group. Replacing `e` by `m(e)` parallel edge copies produces a multigraph. A skeleton SAW

`e_1,...,e_n`

has exactly

`prod_i m(e_i)`

edge-copy-distinct lifts. Hence multigraph SAW counting is exactly weighted SAW mass on `H`.

Fix a candidate lower bound `r>1` and its critical generating-function point

`z=1/r`.

The degree-five proof can therefore be asked in a general form:

> When does the source's unweighted blue-edge count force divergence of a weighted SAW generating function at `z`?

That question admits a clean dual certificate.

## 4. The weighted blue-branch exponential certificate

Let `S` be the finite set of oriented-edge orbits of `H` under the chosen vertex-transitive automorphism group. Finiteness follows because a fixed vertex has only `d` incident oriented edges. Let

`h:S -> (0,infinity)`

be any positive state potential.

At an extendable SAW prefix whose incoming oriented edge has state `a`, each nonbacktracking outgoing skeleton edge `e` has transformed critical weight

`q_a(e) = z m(e) h(state(e))/h(a)`.                         (4.1)

There are `d-1` such candidate edges. Sort their transformed weights increasingly. For `0<=b<=d-2`, define

`F_b`

to be a uniform lower bound, over every incoming state and every allowed local realization, for the sum of the lightest `b+1` transformed candidate weights.

### Theorem R06-D0069-WB1 — weighted blue-branch certificate

Assume `H` satisfies Grimmett--Li condition `Pi` and there is a number `theta>=0` such that

`F_b >= exp(theta*(b-(d-2)/2))`                              (4.2)

for every `b=0,...,d-2`.

Then the weighted connective constant of the multiplicity model satisfies

`mu_w(H,m) >= r`.                                             (4.3)

### Proof

Take an extendable `2n`-step skeleton SAW. Grimmett--Li's equations (5.2)--(5.3) give, with their artificial incoming mid-edge at the root,

`sum_{s=0}^{2n-1} b_s >= n(d-2)`,                            (4.4)

where `b_s` is the number of blue/extendable alternatives at position `s`. Since `b_0<=d-2`, after deleting the artificial-root position and writing `N=2n-1`,

`sum_{s=1}^{2n-1} [b_s-(d-2)/2] >= -(d-2)/2`.                (4.5)

At every genuine prefix, the chosen continuation plus its `b_s` blue alternatives give `1+b_s` extendable children. Their total transformed critical mass is at least the sum of the lightest `1+b_s` candidate weights, hence at least `F_{b_s}`. Therefore along every such path,

`prod_s F_{b_s}`
` >= exp(theta * sum_s [b_s-(d-2)/2])`
` >= exp(-theta*(d-2)/2)`.                                   (4.6)

For an extendable prefix `eta`, let `S(eta)` be the total transformed critical mass of its extendable children and normalize those child weights to transition probabilities

`p(eta->eta') = q(eta,eta')/S(eta)`.                          (4.7)

For paths of any fixed depth after one fixed extendable first edge,

`sum_paths prod q = E_p[prod S(eta_s)]`.                      (4.8)

Every realized path in this expectation obeys (4.6), so the transformed critical mass at all these even depths is bounded below by a positive constant independent of `n`.

Finally, the state potential telescopes:

`prod q = z^k (prod m(e_i)) * h(final_state)/h(initial_state)`. (4.9)

Because `S` is finite and `h` is strictly positive, the endpoint ratio is bounded above and below by positive constants. Thus the original weighted critical mass is also bounded below at infinitely many depths. Its generating function diverges at `z=1/r`, so its radius of convergence is at most `1/r`, proving `mu_w>=r`. QED.

This is a theorem-sized argument on the page, not a numerical heuristic.

## 5. Method #11 — dualize the branch profile: the criterion is optimal inside this proof architecture

The source blue count supplies only a lower bound on the average number of blue alternatives. Once the local geometry has been compressed to a state-independent profile `F_0,...,F_{d-2}`, the asymptotically worst possible logarithmic path mass is the finite linear program

`Gamma(F) = min sum_b p_b log F_b`,                           (5.1)

where

`p_b>=0`, `sum_b p_b=1`, and `sum_b b p_b >= c`,

with

`c=(d-2)/2`.                                                  (5.2)

The dual variable for the mean-blue constraint gives

`Gamma(F)>=0`

if and only if there exists `theta>=0` for which

`log F_b >= theta*(b-c)` for every b,                         (5.3)

which is exactly (4.2).

Indeed, the Lagrangian is

`sum p_b log F_b + theta(c-sum b p_b)`.

Minimizing over the simplex places all mass on the smallest value of

`log F_b - theta b`,

so the dual lower bound is

`theta c + min_b(log F_b-theta b)`.

This is nonnegative exactly when (5.3) holds for every b. Finite-dimensional LP strong duality applies.

Thus the exponential supporting-line condition is not just a convenient sufficient trick: **given only the source average-blue inequality and a state-independent local prefix-mass profile, it is the sharp certificate.** If it fails, this architecture needs more information than the scalar blue count.

As a consistency check, the ordinary simple unweighted theorem is recovered by taking

`m=1`, `h=1`, `r=sqrt(d-1)`,

so

`F_b=(b+1)/sqrt(d-1)`.

For

`theta=log(d-1)/(d-2)`,

(4.2) is precisely

`log(b+1) >= [b/(d-2)] log(d-1)`,

which is the chord inequality from concavity of `log` between `b=0` and `b=d-2`. This reproduces the source mechanism in dual form.

## 6. Why the completed degree-five proof fits this theorem exactly

The two residual quotient states in run 15 both reduced to a simple `d=4` skeleton at the target `r=2`, with the state potential chosen there. Their uniform local profile was

`F_0=1/2, F_1=1, F_2=2`.                                     (6.1)

For `d=4`, the center is `c=1`; taking

`theta=log 2`

gives exact equality

`F_b = exp(theta*(b-1))`, `b=0,1,2`.                         (6.2)

So run 15 was not an isolated ad hoc cancellation: it sat exactly on the optimal LP-dual supporting line. This explains why the argument was sharp enough to finish the last degree-five type.

The exact checker archived this run verifies the rational profile identity

`F_0 F_2 = F_1^2`

without floating point.

## 7. Method #20 — find why the same algorithm fails one degree later

The most useful stress test is not to claim a degree-six theorem. It is to identify the first exact obstruction to simply recycling the degree-five state potential.

Consider the degree-six local multiplicity pattern

`[3,1,1,1]`.

Its simple skeleton has `d=4`. The source target would be

`r=sqrt(5)`, hence `z=1/sqrt(5)`.

Try the most natural multiplicity-only two-state potential: state `T` for a triple edge and `S` for a singleton. Normalize

`h(S)=1`, `h(T)=x>0`.

After an **incoming singleton edge**, the three nonbacktracking outgoing edge types are

`T,S,S`,

with transformed critical weights

`3x/sqrt(5), 1/sqrt(5), 1/sqrt(5)`.                           (7.1)

The sum of the two lightest weights is therefore at most

`2/sqrt(5) < 1`.                                              (7.2)

More explicitly:

- if `3x>=1`, the two singleton weights are the lightest and their sum is exactly `2/sqrt(5)`;
- if `3x<1`, the two-lightest sum is `(1+3x)/sqrt(5) < 2/sqrt(5)`.

But for a `d=4` profile the blue-count center is `c=1`. Any LP-dual certificate (5.3), for any `theta`, necessarily requires at the central value `b=1`

`F_1 >= exp(theta*(1-1)) = 1`.                                (7.3)

Equations (7.2)--(7.3) are incompatible. Therefore:

### Corollary R06-D0069-WB2 — exact method barrier

No multiplicity-only two-state potential `h(T),h(S)>0` can prove the degree-six `[3,1,1,1]` target `mu>=sqrt(5)` using only:

1. the Grimmett--Li scalar average-blue count (5.3 in the source), and
2. a state-independent lower profile obtained by summing the lightest `1+b` transformed children.

This is a **barrier for this proof architecture**, not a counterexample to the Grimmett--Li conjectural extension and not evidence that the degree-six statement is false.

It identifies exactly what the next successful method must contain that the degree-five proof did not need: for example, a joint state/blue-count constraint forcing the heavy edge to participate often enough, a longer-memory potential, or a second conserved statistic beyond the scalar number of blue alternatives.

## 8. Exact finite/symbolic validation

Only after the theorem and obstruction were derived, I added a small exact checker:

`artifacts/R06/d0069_run16_blue_lp_barrier_check.py`

creation commit

`f71614b9cd856b7dcdd134e1c068d9d198033964`.

It was executed locally before archival. The exact output is

`artifacts/R06/d0069_run16_blue_lp_barrier_check.out`

creation commit

`f65fa608f285951ab28f8b4c987534a3865ef83e`.

Both were read back at their returned commits. The checker uses rational arithmetic for the saturated degree-five profile and exact SymPy algebraic inequalities for the `sqrt(5)` barrier. Its terminal line is

`MULTIPLICITY_ONLY_TWO_STATE_CERTIFICATE_BARRIER_PASS`.

This checker validates only the finite algebraic core. The weighted blue-branch theorem and LP duality are proved on this page.

## 9. Closure/audit discipline

The frozen degree-five subclass is mathematically proved on the R06 pages with exact finite self-checks, but **no independent D0069 closure audit has appeared on current master yet**. A fresh repository search for `D0069` plus `AUDIT/PASS` returned only R06's own reports and outgoing audits of other tracks.

Therefore the degree-five package is not called closure-complete. The required next validation remains:

- one P26 end-to-end audit of the full D0069 degree-five chain;
- one independent end-to-end audit by a distinct OTHER track;
- a publication-level prior-art check if the result is to be written up.

Repeated R06 self-checks do not count as either independent audit.

I read the newest visible neighboring R07 report (`I0077-R07-T20`) for continuity, but I did not spend this run manufacturing another peer-audit certificate; the owner rule puts new-method research before audit bookkeeping, and D0069 itself is still waiting for its required external auditors.

## 10. Model/scheduler control status

The requested model line is still not enforceable from the scheduler surface exposed here. The current automation interface exposes task title/prompt, schedule, timing mode and enabled state, but **no model-family selector and no reasoning-effort selector**; it also supplies no authenticated completed-run model telemetry and no guaranteed hour-long execution control. Thus `GPT-6 / maximum` remains prompt text only, while this report honestly records the actual visible runtime as `GPT-5.6 Sol / reasoning UNVERIFIED`.

The implementation manifest also preserves the historical P26 update attempt that returned:

`You cannot modify this task`.

Repository reconciliation later records successful P26 prompt work from another authorized context. The legitimate workaround for a protected task is therefore the owning/authorized admin context, ownership transfer where supported, or platform support. It is **not** duplication, permission bypass, or claiming an edit that the interface rejected.

This run made no scheduler changes.

## 11. Current status and next route

Frozen metric:

`C5: 5/5 -> 5/5` — **NO MOVEMENT**.

Unchanged count:

`0 -> 1`.

Mathematical status:

**PARTIAL for the full Grimmett--Li source / frozen Delta=5 subclass proved on page / exact self-check PASS / two independent closure audits pending / novelty UNVERIFIED.**

The new reusable result is `R06-D0069-WB1`, the weighted blue-branch LP-dual certificate. The new negative information is `R06-D0069-WB2`: the simplest multiplicity-only state-potential extension already fails exactly at the degree-six `[3,1,1,1]` pattern because its central two-child mass is `<1`.

The next three methods, if no independent audit has arrived by the next invocation, should be:

- #5 ADD A PARAMETER: introduce a joint penalty for edge type and blue count rather than only a scalar state potential;
- #15 BREAK THE SYMMETRY: distinguish the singleton edge orbits instead of collapsing all singleton exits into one state;
- #27 SWAP THE QUANTIFIERS: ask for a pathwise joint-state invariant sufficient for every blue pattern before optimizing over potentials.

Do not restart any of the five already proved degree-five partition cases.

```yaml
ledger_delta:
  run_id: 20260917T1220Z_d0069_weighted_blue_lp_barrier_16
  worker: R06
  lane: CLOSABLE_OUTSIDE
  source:
    id: D0069
    citation: "Grimmett--Li, Bounds on connective constants of regular graphs / survey Question 2.2"
    full_question: "does mu(G)>=sqrt(Delta-1) extend to nonsimple infinite connected loopless vertex-transitive Delta-regular multigraphs for Delta>4?"
    frozen_degree: 5
    frozen_graph_class: "infinite connected loopless vertex-transitive 5-regular multigraphs; parallel edge copies distinct"
  metric:
    name: C5
    before: "5/5"
    after: "5/5"
    movement: false
    unchanged_count_before: 0
    unchanged_count_after: 1
  status: "PARTIAL_FULL_SOURCE / DELTA5_PROVED_ON_PAGE / EXACT_SELF_CHECK_PASS / CLOSURE_AUDITS_PENDING / NOVELTY_UNVERIFIED"
  tried_moves: [1, 11, 20]
  new_claims:
    - "R06-D0069-WB1: weighted blue-branch exponential/LP-dual certificate"
    - "LP duality shows the exponential supporting-line criterion is optimal within the scalar average-blue + state-independent local-profile architecture"
    - "R06-D0069-WB2: at Delta=6, pattern [3,1,1,1] cannot be certified at r=sqrt(5) by any multiplicity-only two-state h-transform inside that architecture"
  evidence:
    - "runs/R06/20260917T1118Z_d0069_degree5_complete_15.md"
    - "artifacts/R06/d0069_run16_blue_lp_barrier_check.py @ f71614b9cd856b7dcdd134e1c068d9d198033964"
    - "artifacts/R06/d0069_run16_blue_lp_barrier_check.out @ f65fa608f285951ab28f8b4c987534a3865ef83e"
    - "Grimmett--Li arXiv:1210.6277, equations (5.2)--(5.3) and Theorem 4.1"
    - "Grimmett--Li, Weighted self-avoiding walks, arXiv:1804.05380 / J. Algebraic Combin. 52 (2020)"
    - "Grimmett, Connective constants of Grigorchuk graphs, arXiv:2608.19349"
  closure_audits_d0069: []
  remaining_obligation:
    - "P26 full D0069 degree-five audit"
    - "one distinct OTHER-track full D0069 degree-five audit"
    - "publication-level novelty/prior-art check if packaged"
  next_moves: [5, 15, 27]
  delivery: "private GitHub only"
```
