Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO MOVEMENT:** `epsilon_bridge: 1/14,469,504 -> 1/14,469,504`; supported unchanged count `3 -> 4`; this is the post-`STUCK_RECOVERY_1` attack, not a second recovery report. Methods actually tried: **#7 TAKE THE LIMIT, #9 RANDOMIZE, #19 MAKE IT AN ALGORITHM**.

# R16 HARD OUTSIDE — I0036 / Schramm Problem 2.1: randomized switching still fails if it is rank-oblivious; geometry-dependent switching survives

Date: 2026-09-17 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`. Source-level status: **PARTIAL / OPEN**. This report does not improve the frozen bridge exponent and does not claim the SAW scaling limit. It records a new exact finite obstruction to the specific Fomin-style recovery selected in the preceding stuck report, and it narrows the surviving algorithmic route.

## 1. Continuity, repository state, ownership, and source status

I continued from the immutable R16 report

`runs/R16/2026-09-17T14-57-00Z_i0036-stuck-recovery-1-fomin-switching-obstruction_f3c2.md`,

which had reached the first hard-target recovery after three supported unchanged runs. That report selected one recovery route — port Fomin-style loop-erased switching to the critical two-defect SAW sector — and prescribed the nonrepeating methods `#7,#9,#19` used here.

Before research I recovered/read the current campaign and operational state required by the owner:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the current owner policy it points to;
- exclusive claim `operations/claims/I0036.md`;
- the newest R16 report and the preceding R16 recurrence, renewal, transfer/Fourier, and `n->0` defect reports;
- the neighboring retired R11 planar-SAW history and the current R12/R13 discrepancy material.

The large intake ledgers were queried through the repository search surface rather than rendered byte-for-byte in one response. No missing intake text is being silently reconstructed.

I0036 remains **R16 exclusive / ADMITTED_ACTIVE / HARD_OUTSIDE**. Its source is Oded Schramm, ICM 2006 Problem 2.1: prove that the small-mesh scaling limit of the infinite half-plane fixed-lattice self-avoiding walk exists and is `SLE_{8/3}`. The fresh 2026-09-17 literature check again found Krachun--Panagiotis, *Annals of Probability* 54(3), 1109--1125 (published 31 May 2026; DOI `10.1214/24-AOP1730`), as the directly relevant peer-reviewed quantitative fixed-lattice baseline: quantitative sub-ballisticity plus polynomial decay of the critical bridge partition function. I found no later source-matching proof of Schramm Problem 2.1 in the bounded search. A bounded negative search is not a worldwide openness or novelty certificate.

The nearest switching baseline remains Sergey Fomin, *Loop-erased walks and total positivity*, arXiv:math/0004083: Fomin obtains total-nonnegativity statements for planar **walk** matrices using loop-erased switching. The central issue here is that critical SAW weights are on already self-avoiding paths, and erasing loops after a switch loses reconstruction information.

## 2. Frozen metric

The fixed R16 metric remains

`epsilon_bridge` = the largest explicit `epsilon>0` for which R16 has a complete proof, in the Krachun--Panagiotis critical honeycomb normalization, of

\[
B_T\le C_\varepsilon T^{-\varepsilon}\qquad\text{for every integer }T\ge1
\]

with explicit finite `C_epsilon`.

Before:

\[
\varepsilon_{\rm bridge}=\frac1{14,469,504}.
\]

After:

\[
\boxed{\varepsilon_{\rm bridge}=\frac1{14,469,504}.}
\]

There is **no movement**. The supported consecutive unchanged count is now `4`. The preceding run already consumed `STUCK_RECOVERY_1`; this run is the substantive test of that selected recovery route. If the protocol is followed literally, the **next** R16 invocation must be `STUCK_RECOVERY_2 / thinking-only`, the second and final permitted recovery on I0036, rather than another ordinary lemma run.

## 3. The recovery route being tested

For a finite planar domain with cyclic boundary terminals `a,b,c,d`, write

\[
S_{uv}(x)=\sum_{\gamma:u\to v\,\mathrm{SAW}}x^{|\gamma|}.
\]

The preceding recovery isolated the source-relevant gluing target

\[
S_{ac}(x_c)S_{bd}(x_c)
\le C_0\left(S_{ab}(x_c)S_{cd}(x_c)+S_{ad}(x_c)S_{bc}(x_c)\right),
\tag{3.1}
\]

ideally with `C_0=1`, where

\[
x_c=\frac1{\sqrt{2+\sqrt2}}.
\]

A same-total-length tail-switch injection was already refuted exactly on a seven-vertex planar subcubic core. The surviving idea was to switch at an intersection and then chronologically erase loops. Since `x_c<1`, every erased edge makes the target **heavier** relative to the source, so the only serious accounting issue is many-to-one reconstruction multiplicity.

This run asks whether randomizing the switch location can make that multiplicity scale-stable.

## 4. #19 MAKE IT AN ALGORITHM — exact algorithm class

Given an ordered source pair

\[
P:a\to c,\qquad Q:b\to d
\]

of SAWs, list their common vertices in the order in which they occur along `P`:

\[
v_0,\ldots,v_{m-1}.
\]

At a selected `v_k`, swap tails to obtain two walks

\[
P[a,v_k]\,Q[v_k,d],\qquad Q[b,v_k]\,P[v_k,c],
\]

then apply chronological loop erasure separately. The result is an adjacent-connectivity pair

\[
A:a\to d,\qquad B:b\to c
\]

of SAWs, with total output length no larger than the total input length.

The first natural randomized class is **rank-only / geometry-oblivious**:

> when there are `m` common vertices, choose the `k`-th common vertex with probability `p_{m,k}`, depending only on `(m,k)` and not on the actual paths or surrounding geometry.

This class contains first-intersection, last-intersection, uniform-intersection, and every fixed mixture of positional rules.

For an output pair `(A,B)`, normalize by its critical weight. The transport load of its fiber is

\[
L(A,B)=\sum_{(P,Q,k)\mapsto(A,B)}p_{m,k}\,x_c^{|P|+|Q|-|A|-|B|}.
\tag{4.1}
\]

A capacity-one transport proof of the stronger one-pair inequality `S_{ac}S_{bd}\le S_{ad}S_{bc}` would require `L(A,B)\le1` for every output pair.

## 5. #9 RANDOMIZE — exact no-go for every rank-only randomization

Use exactly the preceding seven-vertex planar subcubic core

\[
01,04,12,23,25,36,45,56
\]

with pendant terminals

\[
a\!\sim0,\qquad b\!\sim4,\qquad c\!\sim6,\qquad d\!\sim3.
\]

There are four `a-c` SAWs and four `b-d` SAWs, hence sixteen source pairs. Put

\[
z=x_c^2=\frac{2-\sqrt2}{2}.
\]

Two particular output fibers are

\[
T_1=((a,0,1,2,3,d),(b,4,5,2,3,6,c)),
\]

and

\[
T_2=((a,0,4,5,2,3,d),(b,4,5,6,c)).
\]

Exact enumeration gives the following complete signatures `(m,k,delta)` for contributions to these fibers, where `delta` is the number of erased edges:

\[
T_1:\quad (2,0,0),(2,1,0),(4,0,2),(4,1,2),
\tag{5.1}
\]

\[
T_2:\quad (2,0,0),(2,1,0),(4,2,2),(4,3,2).
\tag{5.2}
\]

Let

\[
A=p_{4,0}+p_{4,1}.
\]

Because `p_{2,0}+p_{2,1}=1` and `p_{4,0}+p_{4,1}+p_{4,2}+p_{4,3}=1`, (5.1)--(5.2) imply **for every rank-only randomized rule**

\[
L(T_1)=1+zA,
\qquad
L(T_2)=1+z(1-A).
\]

Therefore

\[
\boxed{
\max\{L(T_1),L(T_2)\}
\ge1+\frac z2
=\frac{6-\sqrt2}{4}
>1.
}
\tag{5.3}
\]

Numerically the unavoidable factor is about `1.1464466`, but (5.3) is exact. Thus randomizing the intersection position does **not** repair the Fomin-style route if the distribution is allowed to see only the number of intersections and their rank along one path.

This is stronger than the preceding observation that first-, last-, and uniform-intersection rules fail: it eliminates the entire positional-randomization simplex at once.

## 6. The obstruction is sharp in the important sense: geometry dependence can repair this witness

The same finite graph does **not** rule out geometry-dependent switching. In fact, exact enumeration gives a deterministic source-pair-dependent choice of switch vertex for all sixteen source pairs such that every output fiber has critical relative load at most one.

For the checker’s deterministic DFS ordering of the sixteen source pairs, one such switch-vertex list is

`[0,0,2,3, 0,0,2,5, 2,3,4,4, 0,5,4,4]`.

The resulting fiber profiles in erased-edge counts are exactly

- twelve fibers with profile `(0,)`, load `1`;
- one fiber with profile `(2,)`, load `z<1`;
- one fiber with profile `(2,2,2)`, load `3z<1`.

The last inequality is exact because

\[
3z<1
\iff 4<3\sqrt2
\iff 16<18.
\]

So the right conclusion is **not** “loop-erased switching fails.” The exact conclusion is:

> a scale-stable switching proof must choose its switch using genuine path/domain geometry; intersection count and rank alone are insufficient.

That is useful because Fomin’s walk-level mechanism is inherently geometric: it singles out intersections relative to a loop-erased trajectory, not an oblivious positional statistic.

## 7. #7 TAKE THE LIMIT — why a fixed local overload is fatal under scale iteration

Equation (5.3) also gives a clean limit obstruction to a product-form local proof architecture. Suppose the same rank-only local switcher is applied independently across `r` separated copies of this local switching problem. In each copy one of the two target fibers has load at least

\[
\lambda_*:=\frac{6-\sqrt2}{4}>1.
\]

Choosing a maximally loaded target fiber in each factor gives tensor-product load at least

\[
\lambda_*^r\longrightarrow\infty.
\]

This statement is intentionally scoped: it rules out **independent/product iteration of the rank-only local rule** as a route to a scale-uniform annulus constant. It does not rule out a globally coupled or geometry-adaptive algorithm on an actual planar domain.

The analogy with the preceding `n<1` quasi-FKG obstruction is exact at the proof-architecture level: a fixed multiplicative defect bigger than one cannot simply be paid at every scale.

## 8. Exact certificate

The finite claims above were checked with integer-exact path enumeration; no floating point is used. The checker is

`artifacts/R16/2026-09-17T15-47-43Z_i0036_rank_only_switching_no_go.py`

and its archived executed output is

`artifacts/R16/2026-09-17T15-47-43Z_i0036_rank_only_switching_no_go.out`.

It verifies the four-by-four source path count, the two complete fiber signatures (5.1)--(5.2), the exact rank-only lower bound, and the geometry-dependent selector’s fiber profiles. It ends

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent audit of I0036.

## 9. What survives, and what the second recovery must test

The recovery route has now split cleanly:

1. **dead:** first/last/uniform intersection and, by (5.3), every random rule that depends only on `(number of intersections, positional rank)`;
2. **still alive:** source-pair/domain-dependent switching, where the choice sees the alternating geometry of the two paths;
3. **still necessary:** a reconstruction or mass-transport argument showing that such geometry-aware choices have uniformly bounded critical fiber load on arbitrary honeycomb domains;
4. **still source-relevant:** if that transport can be made stable under annular composition, it is a plausible route to the missing multi-crossing estimate; it would still require a separate compactness/SLE-identification argument afterward.

The simplest remaining special case is therefore stronger and more precise than in the preceding report:

\[
\boxed{
\text{Construct a geometry-dependent switch selector }\sigma(P,Q)
\text{ such that every critical output fiber has load }\le C
}
\tag{9.1}
\]

with `C` universal over finite simply connected honeycomb domains, ideally `C=1`. The seven-vertex witness proves that geometry dependence is genuinely necessary and also proves that it can succeed locally.

All thirty section-B labels have now appeared somewhere in the I0036 history; the predecessor explicitly identified `#7,#9,#19` as the final unused triple. Thus a literally never-before-used label does not exist for the next recovery. The next run must still avoid repeating the immediately preceding triple and must use genuinely new mathematical routes. For `STUCK_RECOVERY_2`, I recommend **#11 DUALIZE, #14 FIND THE GROUP ACTING, #25 COUNT THE SAME THING TWICE** applied to (9.1): formulate switch selection as a finite transport/flow duality, exploit planar alternating-path components rather than mere intersection rank, and look for a double-counting certificate that bounds every target fiber without reconstructing erased loops one by one.

If that second recovery also fails to produce movement and a later third stuck episode is reached, the hard-two-recovery rule requires an I0036 handoff and rotation to a source-checked eligible HARD outside target. Do not run a third I0036 recovery.

## 10. Stale Beck--Fiala title: fresh source check, no restart

The native title still says Beck--Fiala, but repository continuity has already transferred R16 to I0036 after the earlier source-status correction and I0043 handoff.

Fresh 2026-09-17 comparison:

- Bansal--Jiang, arXiv:2508.03961v2, state the conjectured `O(sqrt(t))` order for `t>=log^2 n`, with a weaker polylogarithmic sparse-regime bound and efficient algorithms. That paper alone does not settle all `t,n`.
- Guo--Fang--Lu, arXiv:2609.11189v1, submitted **10 September 2026**, explicitly claim the dimension-free Boolean Komlós bound `3 sqrt(2 pi)` and deduce
  \[
  \operatorname{disc}(A)<3\sqrt{2\pi t}
  \]
  for every integer `t>=1`, with no restriction on `n`.

This is a very recent preprint claim. The current repository search surfaced `R12-AUDIT-R13-KOMLOS-01=PASS` as one independent OTHER-track audit of that external theorem package, and the R13 reports found in the same bounded search explicitly say that no P26 R13 Komlós audit had been located at those report times. I therefore do **not** upgrade the fleet to protocol closure here. The correct operational description is: **fresh primary-preprint full-resolution claim, one verified OTHER-track audit surfaced in this run, mature external consensus and protocol closure not asserted**.

No Beck--Fiala research was restarted.

## 11. Model/scheduler control and P26 permission issue

The control limitation is unchanged. The exposed scheduler mutation schema permits task title/prompt, schedule or relative start, timing mode, and enablement. It has **no model-family selector and no reasoning-effort selector**. Therefore GPT-6/maximum is request text only; actual enforcement would require an authorized product/workspace scheduler or API that exposes those selectors plus authenticated runtime telemetry.

The repository’s current deployment record says the earlier P26 `You cannot modify this task` result was context-specific: a later P/C-authorized context successfully updated P26, while another context denied all R-series edits. A denial is not repaired by duplicating the task or bypassing permissions. The compliant workaround is to use the owning account/workspace context or platform support and verify the accepted native edit there.

No scheduler state, shared-root ledger, peer-track file, email, Drive content, public post, purchase, permission, workflow, or additional task was changed in this run.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R16
  lane: HARD_OUTSIDE
  canonical_target: I0036
  source: "Schramm ICM 2006 Problem 2.1; fixed-lattice half-plane SAW scaling limit to SLE_8/3"
  ownership: "operations/claims/I0036.md; R16 exclusive"
  status: PARTIAL_OPEN
  metric: epsilon_bridge
  before: "1/14469504"
  after: "1/14469504"
  movement: false
  supported_unchanged_count_before: 3
  supported_unchanged_count_after: 4
  stuck_recoveries_used_before: 1
  stuck_recoveries_used_after: 1
  run_role: "post-STUCK_RECOVERY_1 attack"
  next_protocol_action_if_no_intervening_movement: "STUCK_RECOVERY_2 thinking-only"
  methods: [7, 9, 19]
  new_exact_finite_claim: "Every rank-only randomized switch-and-loop-erase rule on the seven-vertex witness has a target fiber of load at least (6-sqrt(2))/4>1; a geometry-dependent selector achieves max load <=1 on the same witness."
  claim_scope: "algorithmic finite obstruction/repair only; not Schramm Problem 2.1 and not a proof of the four-terminal inequality in general"
  checker: "artifacts/R16/2026-09-17T15-47-43Z_i0036_rank_only_switching_no_go.py"
  checker_output: "artifacts/R16/2026-09-17T15-47-43Z_i0036_rank_only_switching_no_go.out"
  checker_status: "ALL_EXACT_CHECKS_PASS; self-check"
  beck_fiala_refresh: "Bansal-Jiang partial-by-regime baseline; Guo-Fang-Lu 2026-09-10 v1 claims full Boolean Komlos/Beck-Fiala bound; one R12 outside audit surfaced; P26 closure not verified here"
  shared_root_edits: false
  peer_file_edits: false
  scheduler_edits: false
  email_or_drive: false
```
