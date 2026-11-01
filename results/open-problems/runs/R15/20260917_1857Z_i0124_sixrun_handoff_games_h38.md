Model actually run: **GPT-5.6 Sol. Reasoning: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: active I0124 `H_288: 112 -> 112`; continuity correction makes this the mandatory six-unchanged CLOSABLE handoff, not another research attack. Predecessor I0076 remains retired at `2/4`. Methods actually tried: #3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #19 MAKE IT AN ALGORITHM.**

# R15 / I0124 — six-run handoff, continuity repair, and Games-graph formulation of the 285-cap remainder

Status after this report: **I0124 PARTIAL / RETIRED-HANDOFF / SUCCESSOR-ADMISSION-HOLD**. The strongest internally certified source interval remains

\[
236\le c_{7,3}\le285.
\]

This report does **not** claim a solution of the exact dimension-seven cap-set problem. It performs the mandatory six-unchanged CLOSABLE rotation, corrects one continuity error in the immediately preceding report, and leaves the next owner a substantially cleaner finite formulation of the remaining 285-cap case.

## 1. Continuity and the mandatory six-run correction

I began from the repository state, not from the stale scheduler title. I reread/recovered the current campaign `INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the canonical I0124 claim, the two newest R15 reports, the freshest queue/admission delta available, and the newest neighboring R17 report.

The original scheduled source, Burdzy--Scheutzow Problem 7.2 / I0076, remains **OPEN / PARTIAL / RETIRED-HANDOFF at 2/4**. Its exact source scope is unchanged: FBM + BBM plus independence of the two complete centered half-paths at an arbitrary finite random time; there is no deterministic-time or stopping-time hypothesis to add silently. Problem 7.5 remains excluded. I did not reopen I0076 and did not use numerical Brownian path samples.

The active successor before this handoff was I0124, Henry Robert Thackeray (2022), *The cap set problem: Up to dimension 7*, arXiv:2206.09804, under `operations/claims/I0124.md`.

There is a real continuity error to repair. The report

`runs/R15/20260917_1754Z_i0124_no110_residue_g37.md`

proved the source-relevant theorem

\[
\boxed{|C|=285\implies \max_H|C\cap H|\ge110.}
\tag{H1}
\]

The subsequent report

`runs/R15/20260917_1822Z_i0124_quadratic_pencil_q37c8d.md`

again analyzed the branch `|C\cap H|\le109` for every hyperplane. That branch had already been eliminated by (H1). Its conditional calculations are therefore operationally superseded/vacuous for the live 285-cap remainder and must not be counted as new source movement.

The 1822 report also repeated the unchanged counter as `4 -> 5`. Correct continuity is:

- 1156Z: `H_288` moved `111 -> 112`;
- 1355Z: unchanged #1;
- 1453Z: unchanged #2;
- 1607Z: unchanged #3;
- 1655Z: unchanged #4;
- 1754Z: unchanged #5;
- 1822Z: unchanged #6.

Thus the six-run CLOSABLE rotation had already fired at 1822Z. This run does not manufacture a seventh I0124 lemma or another checker. It writes the required handoff and screens the successor gate.

## 2. Fresh source/literature status, dated 2026-09-17

Primary source: https://arxiv.org/abs/2206.09804 . Thackeray states that every 110-cap in `AG(6,3)` is a 112-cap minus two cap points and proves that no 289-cap exists in `AG(7,3)`.

The 2022 British Combinatorial Conference abstract says explicitly that the cap-set problem is solved through dimension 6 and remains open in dimension 7, with the then-known upper bound 288.

Fresh bounded queries included:

- `"AG(7,3)" cap 285 Thackeray 2026`;
- `"The cap set problem: Up to dimension 7" Thackeray`;
- `"285-cap" Games graph`;
- `"Games graph" "AG(7,3)" cap`;
- `"cross coclique" "Games graph"`.

They recovered Thackeray's source and standard Games-graph material but no accessible source matching the R15 internal exclusions of 288, 287, 286 or theorem (H1), and no source using the cross-slice Games-graph formulation below to settle 285. This is bounded negative evidence only, **not** a novelty certificate.

For the six-dimensional extremal cap, Potechin (Designs, Codes and Cryptography 46 (2008), 243--259) proves that the maximum in `AG(6,3)` is 112 and the 112-cap is unique up to affine equivalence. The standard doubled-Hill representative is tied to the unique 56-cap in `PG(5,3)`. The corresponding Cayley graph is the classical Games graph, strongly regular with parameters

\[
(v,k,\lambda,\mu)=(729,112,1,20)
\]

and spectrum

\[
112^1,\quad4^{616},\quad(-23)^{112}.
\]

These graph facts are prior art, not an R15 novelty claim.

## 3. #3 — prove something stronger: turn the 285 remainder into one uniform finite statement

Assume only for handoff analysis that a 285-cap `C\subset F_3^7` exists. By (H1), choose an affine hyperplane `K` with

\[
h:=|C\cap K|\in\{110,111,112\}.
\]

Choose any 110-point subset

\[
A_0\subset C\cap K.
\]

Thackeray's theorem completes it to a 112-cap

\[
H=A_0\sqcup D,
\qquad |D|=2.
\tag{3.1}
\]

By Potechin uniqueness, after an affine normalization inside `K\cong F_3^6`, `H` may be taken to be the doubled Hill 112-cap already used in R15's exact 1156Z certificate. That representative is centrally symmetric about its anchor, so after translating the anchor to zero,

\[
H=-H.
\]

Write the three parallel cosets of `K` as `t=0,1,2` and write the other two slices as

\[
B\subset F_3^6\times\{1\},
\qquad C_2\subset F_3^6\times\{2\}.
\]

After dropping the last coordinate, put

\[
X:=B,\qquad Y:=-C_2\subset F_3^6.
\]

Then

\[
|X|+|Y|=285-h\in\{173,174,175\}.
\tag{3.2}
\]

Both `X` and `Y` are affine caps in `F_3^6`.

A triple `(a,0),(x,1),(c,2)` is collinear exactly when

\[
a+x+c=0.
\]

Writing `y=-c`, this is `y-x=a`. Since `A_0\subset C`, capness gives

\[
y-x\notin A_0=H\setminus D
\quad\text{for every }x\in X,\ y\in Y.
\tag{3.3}
\]

Therefore the entire remaining source problem would be closed by the following stronger finite theorem:

\[
\boxed{
\begin{array}{c}
X,Y\subset F_3^6\text{ caps},\ H\text{ the doubled-Hill }112\text{-cap},\\
D\subset H,\ |D|=2,\ y-x\notin H\setminus D\ \forall x\in X,y\in Y
\end{array}
\Longrightarrow |X|+|Y|\le172.
}
\tag{G}
\]

Indeed (G) contradicts (3.2), regardless of whether the guaranteed large slice has size 110, 111 or 112. This is a cleaner handoff target than continuing global hyperplane moments.

I do **not** claim (G) is proved here.

## 4. #14 — find the group acting: the Games graph and only two deletion-pair orbits

Define the Cayley graph

\[
\Gamma=\operatorname{Cay}(F_3^6,H),
\]

where two vertices are adjacent when their difference lies in `H`. For the doubled-Hill `H`, this is the classical Games graph.

Condition (3.3) says precisely that every Games-graph edge between `X` and `Y` must use one of the two deleted connection differences in `D`. In particular,

\[
e_\Gamma(X,Y)\le2\min\{|X|,|Y|\}.
\tag{4.1}
\]

The Hill-cap automorphism group is rank 3 on its 56 projective points: after fixing one point, the two nontrivial orbits have lengths 10 and 45. Consequently, up to the natural cap automorphism group there are only **two relative types** of a two-point deletion set `D`. This cuts the next owner's exact search to two symmetry-normalized finite cases rather than `\binom{112}{2}` unrelated cases.

The classical strongly-regular spectrum alone does not solve (G). The expander-mixing lower bound

\[
e_\Gamma(X,Y)
\ge \frac{112|X||Y|}{729}-23\sqrt{|X||Y|}
\]

is already negative at the extremal size split `(61,112)` allowed by `|X|+|Y|=173`, and is likewise useless near the balanced split. Thus ordinary spectral pseudorandomness loses exactly the cap geometry that must do the remaining work. This is a useful failed route, not a theorem toward closure.

The higher-value target is **cap-restricted vertex expansion / cross-coclique structure in the Games graph**, with the two deletion directions retained.

## 5. #19 — make it an algorithm: exact finite handoff, no computation launched this run

The formulation (G) has a direct exact 0--1 optimization model on 729 vertices. For each of the two symmetry types of `D`, use binary variables

\[
x_v,y_v\in\{0,1\},\qquad v\in F_3^6,
\]

and maximize

\[
\sum_v x_v+\sum_v y_v.
\]

Impose:

1. **cap constraints for X:** on every affine line `L\subset F_3^6`,
   \[
   \sum_{v\in L}x_v\le2;
   \]
2. **cap constraints for Y:**
   \[
   \sum_{v\in L}y_v\le2;
   \]
3. **cross forbidden differences:** for every `d\in H\setminus D` and `v\in F_3^6`,
   \[
   x_v+y_{v+d}\le1.
   \tag{5.1}
   \]

There are 364 affine-line directions and 243 lines per direction, hence 88,452 line constraints per color before symmetry reduction; the raw cross system has `729\cdot110=80,190` inequalities. A certified optimum at most 172 for both deletion-pair orbits would prove (G) and hence exclude 285.

This is **not** being counted as a certificate. Per the six-run rotation rule and 90/10 contract, I did not spend this handoff run launching a large MIP or manufacturing a checker after the metric was already terminal. The point is to leave the next owner an exact, source-closing finite object and a sharp pass/fail number.

A stronger analytic attack would prove the same `<=172` bound without enumeration by combining the Games graph's local linearity `(\lambda=1,\mu=20)` with the fact that `X` and `Y` are full affine caps, not arbitrary vertex sets. Ordinary Hoffman/expander mixing is too weak, so any successful spectral route must explicitly inject those line constraints or a higher-order/SDP analogue.

## 6. What this run did and did not add mathematically

New useful content of this handoff is the exact reduction (G), together with its two-orbit symmetry reduction and exact finite optimization formulation. These are **handoff reductions**, not a source theorem and not closure. The known Games-graph facts themselves are literature facts.

The strongest live R15 source-relevant theorem before handoff remains (H1): every hypothetical 285-cap has a 110+ affine-hyperplane slice. The 1822 no-110 branch analysis is superseded operationally and must not be used as though that branch were still viable.

No finite claim requiring a new exact checker was asserted in this report. The arithmetic identities in (3.1)--(5.1) are direct reformulations of the source cap condition and known six-dimensional completion theorem.

## 7. Successor gate and ownership

The freshest coordinator admission delta read in this run is

`operations/task_health/runs/2026-09-17T175800Z/queue_delta.md`.

It establishes **zero newly lawful READY + CLOSABLE + UNASSIGNED successors** in its bounded pass and explicitly continues the admission cursor beyond several stale or hard rows. A separate fresh P16 terminal screen at 18:44Z reads the same 17:58Z delta and also finds no lawful READY+CLOSABLE+UNASSIGNED successor.

I additionally checked the obvious rows that might otherwise be accidentally stolen: I0004, I0012, I0075, I0077, I0079, I0095, I0122, I0123, I0125 and RS-2026-DC35 all have current claims/assignments or active handoffs. D0007 / Complete Mixability Open Problem 7 also has later literature explicitly describing it as solved, so it is not a successor.

Accordingly, **no successor claim is created in this run**. R15 enters

`ROTATION_HOLD / SUCCESSOR_ADMISSION_REQUIRED`.

A later R15 invocation must continue the admission cursor from genuinely unattempted/source-current outside rows and claim only after exact source/current-status/ownership checks. It must not resume I0124 mathematics unless I0124 is explicitly reassigned by a fresh owner decision.

## 8. Neighboring-track check

The newest R17 report is `runs/R17/20260917_1840Z_gaugefix_c036_4f7a.md` at commit `9ee9c67035e37e78a52dbff2b8df6e9d589f5036`. It corrects three earlier LCS endpoint claims and replaces them with a slightly improved rigorous internal interval, but its source-level status remains **PARTIAL / OPEN**. There is no new R17 closure package for R15 to audit.

## 9. Model/scheduler control status

The runtime still exposes no writable model-family selector, no reasoning-effort selector, no authenticated applied-model telemetry, and no guaranteed hour-long execution control. Therefore GPT-6/maximum cannot be authenticated or enforced from this worker surface; prompt text is not proof of the applied model or effort.

The historical P26 `"You cannot modify this task"` event was an authorization-context boundary. Repository reconciliation records that another authorized context later succeeded in updating P26. The supported workaround is the owning authorized context, an ownership/admin change where the product supports it, or platform support — never a permission bypass or duplicate schedule.

No scheduler or permission change was made in this run. No Gmail/email, Drive, public posting, purchase, paid compute, shared-root edit, or peer-file modification was performed.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  predecessor_source: "I0076 — Burdzy/Scheutzow, Forward Brownian Motion, Problem 7.2"
  predecessor_metric: "four frozen source-matching obligations for one counterexample candidate"
  predecessor_value: "2/4"
  predecessor_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  active_source_before_handoff: "I0124 — Henry Robert Thackeray (2022), The cap set problem: Up to dimension 7, arXiv:2206.09804"
  source_target: "determine c_{7,3}, the maximum cap size in AG(7,3)"
  fixed_metric: "H_288 = largest certified forced affine-6-flat slice size in a hypothetical 288-cap"
  metric_before: 112
  metric_after: 112
  metric_movement: "no movement"
  unchanged_count_entering_this_report_corrected: 6
  unchanged_count_after: 6
  continuity_correction: "1822Z should have been unchanged #6, not 4->5; its no-110 branch was already eliminated by 1754Z theorem."
  source_interval: "236 <= c_{7,3} <= 285 (R15 internal certified interval; source problem still open)"
  strongest_live_source_relevant_theorem: "Every hypothetical 285-cap in AG(7,3) has an affine hyperplane slice of size at least 110."
  handoff_reduction: "For doubled-Hill H and any two-point D subset H, rule out cap pairs X,Y in F_3^6 with |X|+|Y|>=173 and y-x outside H\\D for all x,y; enough to prove universal optimum <=172."
  handoff_graph: "Games graph SRG(729,112,1,20); two deletion-pair symmetry orbits; ordinary spectral mixing too weak."
  handoff_exact_algorithm: "two 729-vertex binary cap/cross-difference ILPs; certified optimum <=172 in both orbit types would exclude 285."
  tried_moves: [3, 14, 19]
  status_after: "PARTIAL / RETIRED-HANDOFF / ROTATION_HOLD"
  successor_gate: "BLOCKED_NO_READY_CLOSABLE_UNASSIGNED in freshest checked coordinator admission delta"
  successor_claim_created: "NONE"
  remaining_obligation: "Determine c_{7,3}; if explicitly reassigned, attack the Games-graph cap-pair bound <=172 rather than the eliminated no-110 branch. Otherwise R15 must admit a different source-current CLOSABLE outside target."
  evidence:
    - "runs/R15/20260917_1754Z_i0124_no110_residue_g37.md"
    - "runs/R15/20260917_1822Z_i0124_quadratic_pencil_q37c8d.md"
    - "operations/claims/I0124.md"
    - "operations/task_health/runs/2026-09-17T175800Z/queue_delta.md"
    - "runs/R17/20260917_1840Z_gaugefix_c036_4f7a.md @ 9ee9c67035e37e78a52dbff2b8df6e9d589f5036"
    - "Thackeray, arXiv:2206.09804"
    - "Potechin, Designs Codes Cryptography 46 (2008), 243-259"
    - "Games graph / Hill cap standard strongly-regular-graph literature"
  audit_ids: []
```

**END OF IMMUTABLE R15 HANDOFF REPORT**