Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT in the frozen metric: `C5: 5/5 -> 5/5`, unchanged count `2 -> 3`; methods #13 FIND WHAT ONLY INCREASES, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R06 CLOSABLE OUTSIDE — D0069 degree-six eight-of-nine reduction

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler mutation.

## 1. Continuity, ownership, and the frozen metric

The stale scheduler title still names Lyons--Peres Question 6.20 / intake I0056. I did **not** reopen it. R06's immutable history already rotated I0056 after six unchanged runs. Its frozen regular/co-regular `H_{5,5}` vertex-isoperimetric constant was certified as the point interval `[sqrt(5),sqrt(5)]`, width zero. The full Lyons--Peres Question 6.20 remains broader, and the triangular/quadrangular cases remain Haslegrave--Panagiotis prior art (DOI `10.1002/rsa.20946`).

The canonical active R06 claim is `operations/claims/D0069.md`. It retains Grimmett--Li's question whether

\[
\mu(G)\ge \sqrt{\Delta-1}
\]

extends from simple infinite connected vertex-transitive regular graphs, and from nonsimple ones with `Delta<=4`, to nonsimple vertex-transitive regular multigraphs of larger degree.

The frozen R06 metric is still

\[
C_5=\#\{\text{the five nonsimple degree-5 local multiplicity types proved uniformly}\}.
\]

Run 15 completed all five, so the tracked quantity enters and leaves this run at

\[
\boxed{C_5=5/5}.
\]

I do not silently replace the owner's frozen metric by a new degree-six metric. Therefore this is honestly the third consecutive **NO MOVEMENT** run in `C5`, even though the mathematics below makes substantial source progress. Under Section I, the next R06 invocation must be a thinking/stuck run with no new theorem claim before further attack on D0069.

Before research I recovered current `master` evidence from `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest implementation record, `operations/claims/D0069.md`, the full R06 D0069 report chain through run 17, exact R06 artifacts, and the newest neighboring R07 report. Root `RESULTS.md` itself warns that its compact R-series rows can lag the immutable run chain, so the latter is the mathematical baseline.

## 2. Source and current-literature check

Primary source checked again: Geoffrey R. Grimmett and Zhongyang Li, *Bounds on connective constants of regular graphs*, Combinatorica 35 (2015), 279--294, DOI `10.1007/s00493-014-3044-0`, arXiv `1210.6277`. Their Theorem 4.1 gives `mu(G)>=sqrt(Delta-1)` for simple vertex-transitive regular graphs and for nonsimple graphs when `Delta<=4`, and immediately asks whether the nonsimple clause extends to larger degree. Their Theorem 4.3 gives the same lower bound under condition `Pi`; the proof of Theorem 4.1(a), once finite-side edge connectivity equals the degree, uses edge-Menger plus local compactness to produce the edge-disjoint infinite SAWs required by `Pi`.

Dated 2026-09-17 searches included the exact source title/question, `"sqrt(Delta-1)" non-simple connective constant multigraph`, degree-six vertex-transitive multigraph variants, later Grimmett/Li work, and recent papers citing the connective-constant programme. The nearest recent papers found were Benjamin Grant--Zhongyang Li, arXiv `2601.12571`, on local finite-gadget transformations of cubic quasi-transitive graphs, and Geoffrey Grimmett, arXiv `2608.19349`, on Grigorchuk graphs. Neither states the general nonsimple larger-degree theorem or the degree-six partition results below. This is bounded negative evidence only: **publication novelty remains UNVERIFIED**.

## 3. Degree-six bookkeeping: nine nonsimple source classes

For a 6-regular loopless multigraph, excluding the already-known simple type `[1,1,1,1,1,1]`, the nine local multiplicity partitions are

\[
[5,1],\ [4,2],\ [4,1,1],\ [3,3],\ [3,2,1],\ [3,1,1,1],\ [2,2,2],\ [2,2,1,1],\ [2,1,1,1,1].
\tag{3.1}
\]

Run 17 proved the source-matching `[3,1,1,1]` class. This run proves seven additional classes. Thus an **auxiliary, non-frozen diagnostic** is now

\[
\boxed{8/9\text{ nonsimple degree-six partitions covered},}
\]

with sole residual `[4,1,1]`. This `8/9` is not substituted for `C5` in the ledger.

## 4. Easy source-matching degree-six classes

### 4.1 Two-neighbour classes `[5,1]`, `[4,2]`, `[3,3]`

The simple skeleton is an infinite connected 2-regular vertex-transitive graph, hence a bi-infinite path. If the consecutive parallel multiplicities are `m,6-m,m,6-m,...`, then a vertex-self-avoiding walk can only continue monotonically after choosing a direction. Edge-copy choices therefore give

\[
\mu(G)=\sqrt{m(6-m)}.
\]

For `m=1,2,3` this yields respectively

\[
\sqrt5,\quad \sqrt8,\quad 3,
\]

all at least `sqrt(5)`.

### 4.2 `[2,2,2]`

The simple skeleton `H` is cubic and vertex-transitive, and every skeleton edge is doubled. Every `H`-SAW of length `n` has exactly `2^n` edge-copy lifts to `G`, and projection gives the converse. Thus

\[
\mu(G)=2\mu(H).
\]

The simple-graph Grimmett--Li theorem gives `mu(H)>=sqrt2`, hence

\[
\mu(G)\ge2\sqrt2>\sqrt5.
\]

### 4.3 `[2,1,1,1,1]`

Let `H` be the simple 5-regular vertex-transitive skeleton. The double classes form an invariant perfect matching `D`; the singleton classes form an invariant spanning 4-factor `S`.

For finite nonempty `A`, set

\[
a=|\delta_H(A)\cap D|,\qquad b=|\delta_H(A)\cap S|.
\]

Since `S` is 4-regular, `b` is even. Finite-side edge connectivity of the simple 5-regular transitive skeleton gives `a+b>=5`. The multigraph cut has

\[
|\delta_G(A)|=2a+b.
\]

If `a=0`, then evenness forces `b>=6`; if `a>=1`, then `2a+b=(a+b)+a>=6`. A singleton has multigraph boundary six, so

\[
\lambda_f(G)=6.
\]

The edge-Menger/local-compactness consequence used in Grimmett--Li Theorem 4.1(a) now gives six pairwise edge-disjoint infinite SAWs from every root, hence condition `Pi`; Theorem 4.3 yields

\[
\boxed{\mu(G)\ge\sqrt5.}
\tag{4.1}
\]

## 5. The alternating-factor class `[3,2,1]`

Let `H` be the simple cubic skeleton. The multiplicity-3, multiplicity-2 and multiplicity-1 edge classes `E_3,E_2,E_1` are invariant perfect matchings. Hence

\[
C:=E_3\cup E_2
\]

is an invariant spanning 2-factor whose components alternate multiplicities `3,2,3,2,...`.

If a `C`-component is a double ray, following it already gives connective growth `sqrt(6)>sqrt5`.

Assume instead that the `C`-components are finite cycles. Transitivity makes their common length `2L`. Simplicity of `H` rules out a 2-cycle, so `L>=2`. Whether the `E_1` edge at a vertex stays in its own `C`-component is an invariant property. If all did, `H` would split into finite connected components, contrary to connected infinitude. Thus every `E_1` edge joins distinct `C`-cycles.

Contract the cycles and choose an infinite simple ray of contracted components. An intermediate component is entered and exited at distinct ports. Put the source-critical value

\[
z=1/\sqrt5.
\]

There are exactly two simple `C`-arcs between the entry and exit ports. Let their edge-copy critical masses be `W_1,W_2`. Together they use every edge of the alternating cycle exactly once, hence

\[
W_1W_2=(6z^2)^L=(6/5)^L.
\]

Including the outgoing singleton edge, the total block transfer is

\[
M=z(W_1+W_2)
\ge 2z\sqrt{W_1W_2}
=\frac2{\sqrt5}(6/5)^{L/2}
\ge\frac{12}{5\sqrt5}>1.
\tag{5.1}
\]

The last inequality is exact: `144>125` after squaring positive quantities. Concatenating independently the two internal arcs along a simple block ray gives genuine `G`-SAWs and critical mass bounded below by a positive constant times `M^k`. Therefore the SAW generating function diverges at `z=1/sqrt5`, and

\[
\boxed{\mu(G)\ge\sqrt5.}
\tag{5.2}
\]

## 6. Main new theorem: the `[2,2,1,1]` class

### Theorem R06-D0069-T5

Let `G` be an infinite, connected, loopless, vertex-transitive 6-regular multigraph with local parallel-class partition `[2,2,1,1]`. Then

\[
\boxed{\mu(G)\ge\sqrt5.}
\]

### 6.1 Cut reduction

Let `H` be the simple 4-regular vertex-transitive skeleton. The two double classes form an invariant spanning 2-factor `D`; the two singleton classes form an invariant spanning 2-factor `S`.

For a finite nonempty vertex set `A`, define

\[
a=|\delta_H(A)\cap D|,\qquad b=|\delta_H(A)\cap S|.
\]

Both `a` and `b` are even because both factors have degree two. The multigraph boundary is

\[
|\delta_G(A)|=2a+b.
\tag{6.1}
\]

Finite-side edge connectivity of the simple 4-regular vertex-transitive skeleton gives

\[
a+b\ge4.
\tag{6.2}
\]

Under (6.2) and evenness, the only way (6.1) can be smaller than six is

\[
\boxed{(a,b)=(0,4).}
\tag{6.3}
\]

If no finite set realizes (6.3), then every finite nonempty multigraph cut has size at least six and a singleton cut has size six. Thus `lambda_f(G)=6`, and the same Menger/condition-`Pi` argument as above gives `mu(G)>=sqrt5`.

It remains to handle the exceptional cut profile instead of excluding it.

### 6.2 Negation-first classification of an exceptional cut

Assume some finite `A` has `(a,b)=(0,4)`, and choose such `A` with minimum cardinality.

Because `a=0`, `A` is a union of whole `D`-components. Every automorphism preserves `D`, so every translate `gA` has the same properties.

Suppose `A cap gA` is nonempty. Both `A cap gA` and `A union gA` are finite and `D`-closed. Edge-boundary submodularity in the singleton factor gives

\[
b(A\cap gA)+b(A\cup gA)\le8.
\tag{6.4}
\]

For a finite nonempty `D`-closed set, its `H`-boundary equals its `S`-boundary and is at least four by `lambda_f(H)=4`. Hence both terms in (6.4) are exactly four. Minimality of `A` forces `A cap gA=A`; since `|gA|=|A|`, this gives `gA=A`.

Thus translates of `A` are disjoint or equal: `A` is a block of imprimitivity. Its setwise stabilizer is transitive on `A`: for `u,v in A`, choose an automorphism taking `u` to `v`; its translate of `A` intersects `A`, hence equals `A`.

Every vertex has internal `D`-degree two. Let `t` be its internal `S`-degree; stabilizer transitivity makes `t` constant. Since the total `S`-degree is two and the `S`-boundary is four,

\[
|A|(2-t)=4.
\tag{6.5}
\]

We cannot have `t=2` because the boundary is nonzero. If `t=0`, then `|A|=2`, impossible because the simple graph `H[A]` could not give each vertex internal `D`-degree two. Therefore

\[
t=1,\qquad |A|=4.
\]

Every vertex of `H[A]` has total internal degree `2+1=3`, so

\[
\boxed{H[A]=K_4.}
\tag{6.6}
\]

Inside this `K4`, the `D`-edges form a 4-cycle and the `S`-edges form the complementary perfect matching; every port has exactly one external singleton edge. The translates of `A` partition `V(H)` into such blocks.

### 6.3 Critical transfer through the K4 blocks

Contract the `K4` blocks and choose an infinite simple ray in the connected locally finite block quotient. An intermediate block is entered and exited through distinct ports because each vertex has only one external `S` edge.

Again set `z=1/sqrt5`. Between two distinct ports of a `K4` there are exactly five internally vertex-simple paths: one of length one, two of length two, and two of length three. Sum all their edge-copy critical weights, and include the outgoing external singleton edge.

If entry and exit are the `S`-matched pair, the internal total is

\[
z+8z^2+8z^3,
\]

so the block transfer is

\[
M_{\rm match}=z^2+8z^3+8z^4
=\frac{13+8\sqrt5}{25}>1.
\tag{6.7}
\]

The exact comparison is `8sqrt5>12`, or after squaring, `320>144`.

If entry and exit are adjacent on the `D`-cycle, the internal total is

\[
2z+4z^2+10z^3,
\]

and

\[
M_{\rm adj}=2z^2+4z^3+10z^4
=\frac{20+4\sqrt5}{25}>1.
\tag{6.8}
\]

Here the exact comparison is `4sqrt5>5`, or `80>25` after squaring.

Let `M_*` be the smaller of these two transfer masses. Then `M_*>1`.

Along the simple block ray, independently choose any internally vertex-simple route in each visited block and each admissible edge copy. Since a block is never revisited, every concatenation is a genuine vertex-self-avoiding walk of `G`. Its total critical mass after `k` complete block traversals is at least

\[
c_0M_*^k
\]

for a fixed `c_0>0`. Hence the critical generating function diverges at `z=1/sqrt5`, proving

\[
\boxed{\mu(G)\ge\sqrt5.}
\]

This completes Theorem R06-D0069-T5.

## 7. What remains at degree six: exactly `[4,1,1]`

Combining Sections 4--6 with run 17 gives source-matching proofs for eight of the nine nonsimple degree-six partitions in (3.1). The sole residual class is

\[
\boxed{[4,1,1].}
\]

A useful negative result is that the scalar multiplicity-only weighted-blue architecture from run 16 cannot simply be retuned to finish it.

The multiplicity-4 classes form an invariant perfect matching in the cubic simple skeleton. Contracting that matching gives a 4-regular transitive quotient whose macrovertex is split into two two-edge ports. At `z=1/sqrt5`, a same-port singleton transition has critical lift weight

\[
a=z=1/\sqrt5,
\]

while switching ports uses one of four heavy matching-edge copies followed by the outgoing singleton, giving

\[
b=4z^2=4/5.
\]

The scalar degree-four blue-count method has extremal child masses

\[
F_0=a,\qquad F_2=a+2b.
\]

The extremal product is

\[
F_0F_2
=z(z+8/5)
=\frac{5+8\sqrt5}{25}<1,
\tag{7.1}
\]

because `8sqrt5<20`, equivalently `320<400`. Thus the old scalar certificate fails at the exact source threshold. This is a **method barrier, not a counterexample**. A successful proof needs information absent from that scalar summary: port/branch correlation, longer-memory state, or a different structural theorem.

## 8. Section-B outcomes

### #23 DO WHAT THE PROPOSER DID NOT EXPECT — succeeded

Instead of trying to prove that every finite cut is large, I assumed the unique bad `[2,2,1,1]` cut profile `(a,b)=(0,4)` exists and classified it. Minimality plus submodularity turns it into a four-vertex imprimitivity block, necessarily a `K4`, which is then directly summable at the source-critical point.

### #13 FIND WHAT ONLY INCREASES — succeeded

In the exceptional-block branch, the total critical SAW transfer across each new `K4` is at least `M_*>1`. Along a simple macro-ray the critical mass therefore multiplies by a factor strictly larger than one at every scale. The monotone quantity is transfer mass, not a sampled SAW count.

### #30 ONE SCALE / ONE DIRECTION AT A TIME — succeeded

I localized the source first to `Delta=6` and then to its exact local multiplicity partitions. This exposes that eight of nine nonsimple types are now source-matching consequences of explicit one-dimensional, finite-cut, alternating-cycle, or K4-block mechanisms. Only `[4,1,1]` survives.

Because the official `C5` metric has nevertheless remained unchanged for three consecutive runs, the next run must obey Section I and be a thinking/stuck report, not another theorem-producing continuation. Suggested fresh moves for that thinking run: **#6 DEFORM TO A SOLVABLE POINT, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #27 SWAP THE QUANTIFIERS**.

## 9. Exact finite validation

Only after the proofs were written did I add the exact finite-core checker

`artifacts/R06/d0069_run18_degree6_eight_of_nine_selfcheck.py`

at commit `3ae054f220f5aedb5f841c7ae3f9dc2b05d868ac`, with archived output

`artifacts/R06/d0069_run18_degree6_eight_of_nine_selfcheck.out`

at commit `a76da0228b0251253f001863a9cf2aac9b0d9a07`.

It verifies exactly:

- the nine nonsimple degree-six partitions and the eight covered ones;
- that `(a,b)=(0,4)` is the unique even `[2,2,1,1]` cut profile with `a+b>=4` but `2a+b<6`;
- the `[2,1,1,1,1]` cut inequality;
- the two K4 radical comparisons `320>144` and `80>25`;
- the `[3,2,1]` worst finite-cycle transfer comparison `144>125`;
- the `[4,1,1]` scalar-blue barrier comparison `320<400`;
- the elementary two-neighbour and `[2,2,2]` inequalities.

The archived output ends `SELF_CHECK_PASS`. These finite checks are labelled self-checks; all infinite graph arguments are on the page above.

## 10. Neighbor/audit discipline

The newest neighboring R07 report visible at the start of this run is still the exterior-parabolic-fan / unbounded-component theorem `I0077-R07-T22`, which R06 already independently audited in run 17. I did not manufacture a duplicate audit ID merely to fill the validation quota.

No independent D0069 source audit was found on current master in the bounded ownership/audit search. The degree-five package therefore still awaits P26 plus one distinct OTHER-track end-to-end audit. The degree-six progress in this report is likewise **PROVED-ON-PAGE / SELF-CHECK PASS / NOVELTY UNVERIFIED**, not closure-certified.

## 11. Model / scheduler control status

Still true in the operative implementation record: the exposed scheduler surface has title/prompt, schedule, timing mode and enabled state, but **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed hour-long execution control**. GPT-6 / maximum is prompt text only, so this report truthfully identifies the actual exposed runtime as GPT-5.6 Sol / reasoning UNVERIFIED.

The historical P26 update attempt returning `You cannot modify this task` is an authorization-context boundary. The legitimate remedy is the owning/authorized admin context or platform support. Enforcing GPT-6/maximum would require the product/backend to expose persistent model and reasoning fields plus authenticated runtime telemetry. This run did not attempt a permission bypass, duplicate task, or scheduler mutation.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R06
  owner: R06
  lane: CLOSABLE OUTSIDE
  source_id: D0069
  source: "Grimmett--Li, Question 2.2 / Bounds on connective constants of regular graphs"
  parent_question: "Does mu(G)>=sqrt(Delta-1) extend to nonsimple vertex-transitive regular multigraphs for Delta>4?"
  frozen_metric: C5
  metric_definition: "number of five nonsimple Delta=5 local multiplicity types proved uniformly"
  metric_before: "5/5"
  metric_after: "5/5"
  metric_movement: "NO MOVEMENT"
  unchanged_count_before: 2
  unchanged_count_after: 3
  status: PARTIAL
  full_source_closed: false
  new_source_progress:
    delta6_nonsimple_covered: "8/9"
    delta6_sole_remaining: "[4,1,1]"
    new_theorems:
      - "Delta=6 [2,2,1,1] => mu>=sqrt(5)"
      - "Delta=6 [5,1], [4,2], [3,3], [2,2,2], [2,1,1,1,1], [3,2,1] => mu>=sqrt(5)"
    prior_run_theorem_used: "Delta=6 [3,1,1,1] => mu>=sqrt(5)"
  tried_moves: [13, 23, 30]
  next_run_protocol: "SECTION_I_STUCK_THINKING_ONLY"
  next_suggested_moves: [6, 17, 27]
  exact_evidence:
    - "artifacts/R06/d0069_run18_degree6_eight_of_nine_selfcheck.py @ 3ae054f220f5aedb5f841c7ae3f9dc2b05d868ac"
    - "artifacts/R06/d0069_run18_degree6_eight_of_nine_selfcheck.out @ a76da0228b0251253f001863a9cf2aac9b0d9a07"
  self_check_status: PASS
  d0069_independent_audits: PENDING
  novelty: UNVERIFIED
  remaining_obligation:
    - "Next run: required Section-I thinking/stuck report because C5 has been unchanged three consecutive runs."
    - "Simplest remaining source case at Delta=6: [4,1,1]."
    - "Full source also contains all Delta>=7 cases."
    - "P26 + distinct OTHER-track audit still required for closure of the frozen Delta=5 package."
```
