Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `n_all: 9 -> 9`; methods #3 PROVE SOMETHING STRONGER, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #19 MAKE IT AN ALGORITHM.**

# R20 — loop-free branch-cycle theorem for BMO Conjecture 2.6

## 1. Continuity, ownership, source gate, and exclusions

I continued from the newest complete R20 report

`runs/R20/2026-09-19T03-02-29Z_bmo_subcubic_core_matching_4e9b71.md`

rather than restarting from the stale scheduler title. The current exclusive R20 research claim is still

`operations/claims/BMO-2025-PUSHING-DELTA.md`,

marked `CLAIMED / READY / CLOSABLE OUTSIDE`.

The active outside source is Julien Bensmail, Clara Marcille and Mano Orenga, *Pushing Vertices to Make Graphs Irregular*, DMTCS 27:3 (2025), article 7, DOI `10.46298/dmtcs.14963`, Conjecture 2.6. For a nice finite simple graph `G`,

\[
P^\ell(G)\le \Delta(G)
\]

is conjectured, where

\[
\sigma_\rho(u)=d_G(u)(1+\rho(u))+\sum_{v\sim u}\rho(v)
\]

must distinguish the endpoints of every edge.

The older create-only `operations/claims/I0100.md` still exists as historical scheduler-era ownership metadata, but the later immutable R20 rotation/admission history records I0100 as frozen and the BMO claim as the active successor. I therefore did not reopen Paley one-localization, did not edit either claim, and made no new assertion here about the unresolved status of any Paley prime or of the Paley asymptotic. The latest own BMO reports explicitly preserve the old finite I0100 frontier separately.

I reread the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the BMO claim, the old I0100 claim, and the newest complete R20 report. I also rechecked the named neighboring Paley tracks sufficiently to avoid collision: P04/I0101 is the distinct two-localization target; the old R12/I0102 degree-four-SOS target is distinct and later R12 reports have rotated elsewhere; C28/I0103 remains a distinct Paley-ETF/RIP line. None is reassigned here.

### Fresh literature check — 19 September 2026

The DMTCS primary page still gives the 2025 source paper, and its PDF states Conjecture 2.6 exactly as `P^ell(G)<=Delta(G)` for nice graphs. Its conclusion specifically identifies maximum degree three as a first gap: the paper has `P^ell<=9` there, whereas the conjecture asks for `P^ell<=3`.

The current published follow-up located this run is Dieter Rautenbach, Laurin Schwartze and Florian Werner, *Coloring by Pushing Vertices*, *Ars Combinatoria* 167, 147--157, published online 17 June 2026. Its abstract still presents the general `P^ell(G)<=Delta(G)` statement as conjectural and proves it for cubic graphs and regular bipartite graphs.

Dated bounded queries included the exact source title and conjecture phrase, `proper pushing scheme subcubic 2-core`, `pushing vertices subcubic matching`, and `pushing vertices Brooks`. They found the source, the 2026 follow-up, mirrors/indexes and unrelated graph-push material, but no later source-matching general solution and no located theorem matching the subclass proved below. This is bounded negative evidence only, not a novelty certificate.

## 2. Idea before code and the three Section-B moves

Before adding validation code I wrote

`artifacts/R20/2026-09-19T03-49-00Z_bmo_deg2_branch_port_idea.md`

at creation commit

`39167b531e65137e672eb321c0c2e77d4df603c3`.

The previous theorem handled the case in which the degree-three vertices of the 2-core induce a matching. The next target was the opposite high-interaction boundary: every degree-three core vertex has **two** direct degree-three neighbors, so those direct branch edges form cycles.

### #3 — PROVE SOMETHING STRONGER: success

Instead of treating one direct-branch cycle length or one chain length, I derived an exact endpoint-transfer lemma valid for **every** subdivided branch-to-branch chain and boundary branch pushes in `{2,3}`. The lemma converts the core into a four-state port problem and makes arbitrary long chains transparent.

### #16 — COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE: success, with a genuine obstruction to the first ansatz

The transfer relation stabilizes immediately:

- one internal vertex forces equal endpoint ports;
- two internal vertices forbid exactly one affine difference;
- three or more internal vertices realize every ordered endpoint-port pair in `{0,1,2,3}^2`.

For the all-branch-push-3 construction, the resulting quotient has maximum degree four. The only loop-free Brooks obstruction is a `K5` component. This is not an obstruction to the BMO conjecture: a single push-2 defect repairs **every** possible `K5` lift. The exact checker verifies all `3^5=243` local pairings.

### #19 — MAKE IT AN ALGORITHM: success

The proof below is constructive. Build a constraint quotient, four-color it unless a component is `K5`, use an explicit one-defect formula in the `K5` case, complete every subdivided chain greedily, then reattach the pruned forest one leaf at a time.

## 3. Exact chain-transfer lemma

Let

\[
b_0,x_1,\ldots,x_k,b_1
\]

be a branch-to-branch chain in the 2-core, where the internal vertices have degree two. Put

\[
\rho(b_0)=\alpha,\qquad \rho(b_1)=\beta,
\]

with `alpha,beta in {2,3}`, and write

\[
w_0=\alpha,\quad w_i=\rho(x_i)\ (1\le i\le k),\quad w_{k+1}=\beta.
\]

For an internal vertex,

\[
s_i:=\sigma(x_i)=2(1+w_i)+w_{i-1}+w_{i+1}.
\]

The key identity is

\[
\boxed{s_i-s_{i+1}=w_{i-1}+w_i-w_{i+1}-w_{i+2}.}
\tag{3.1}
\]

Hence the chain is proper internally iff

\[
w_{i-1}+w_i\ne w_{i+1}+w_{i+2}\qquad(1\le i<k).
\tag{3.2}
\]

Call `a=w_1` and `b=w_k` the two endpoint ports.

### Lemma 3.1 — endpoint transfer

For `a,b in {0,1,2,3}`:

1. if `k=1`, the two endpoints see the same internal vertex, so necessarily `a=b`, and every such `a` is allowed;
2. if `k=2`, the chain is internally proper iff
   \[
   a-b\ne \beta-\alpha;
   \tag{3.3}
   \]
3. if `k>=3`, **every** ordered pair `(a,b)` is realizable by a word `w_1,...,w_k in {0,1,2,3}` satisfying (3.2).

#### Proof

The first item is definitional. For `k=2`, (3.1) gives

\[
s_1-s_2=\alpha+a-b-\beta,
\]

which is nonzero exactly under (3.3).

For `k=3`, only `w_2` is free. The two inequalities in (3.2) forbid at most two values of `w_2`, leaving a choice among four symbols.

For `k=4`, set `w_2=0`. The remaining free value `w_3` is excluded by at most the three inequalities in (3.2), so one of the four symbols remains.

For `k>=5`, set `w_2=0`. Choose `w_j` successively for `j=3,...,k-2`; when `w_j` is chosen, the newly closed condition with `i=j-2` forbids only one value. Finally choose `w_{k-1}`. The last three conditions, with `i=k-3,k-2,k-1`, forbid at most three values, so one of `{0,1,2,3}` remains. This constructs the required word. QED.

This is the key strengthening: once a chain has at least three internal vertices, its two endpoint ports are completely independent.

## 4. A uniform branch--chain gap

The next observation lets the proof manipulate branch pushes `2` and `3` without risking a collision with adjacent degree-two chain vertices.

Suppose a degree-three branch `b` has exactly two direct branch neighbors with pushes `r_1,r_2 in {2,3}`, has push `r in {2,3}`, and has chain port `p in {0,1,2,3}`. Then

\[
\sigma(b)=3(1+r)+r_1+r_2+p.
\tag{4.1}
\]

If the chain has at least two internal vertices and the next internal push is `q<=3`, then the first chain vertex has

\[
\sigma(x)=2(1+p)+r+q,
\]

and therefore

\[
\sigma(b)-\sigma(x)
=1+2r+r_1+r_2-p-q\ge3.
\tag{4.2}
\]

If the chain has one internal vertex and the branch push at the far end is `s in {2,3}`, the same calculation gives

\[
\sigma(b)-\sigma(x)
=1+2r+r_1+r_2-p-s\ge3.
\tag{4.3}
\]

Thus every branch--chain edge is automatically proper throughout the construction below.

## 5. New theorem — branch cycles, including the Brooks `K5` exception

> **Theorem 5.1 (R20, SELF_CHECK_ONLY).** Let `G` be a connected nice graph with `Delta(G)<=3`, let `C` be its nonempty 2-core, and let
> \[
> B=\{v\in V(C):d_C(v)=3\}.
> \]
> Assume `B` is nonempty and every `b in B` has exactly two neighbors in `B`; equivalently, the induced branch graph
> \[
> D=C[B]
> \]
> is 2-regular. Assume moreover that no maximal branch-to-branch chain having exactly one internal degree-two vertex joins two branch vertices that are already adjacent in `D`.
>
> Then `G` has a proper pushing scheme with all pushes in `{0,1,2,3}`. In particular,
> \[
> \boxed{P^\ell(G)\le3=\Delta(G).}
> \]

The excluded configuration is very specific: a direct branch edge together with a parallel two-edge route through one degree-two vertex. It is an obstruction to the quotient proof below, **not** a claimed counterexample to Conjecture 2.6.

### 5.1 The complementary branch chains form a perfect matching

Each branch has core degree three and exactly two direct neighbors in `B`, so it has exactly one remaining core incidence, entering a degree-two chain. Since `C` is connected and `B` is nonempty, every component of `C-B` is a path whose two ends meet branch vertices. No such path can return to the same branch, because that would require two non-`D` incidences at that branch. Consequently these maximal paths pair the branch vertices: they form a perfect matching `M` on `B` after suppression.

For `e=uv in M`, let `k_e>=1` be the number of internal degree-two vertices and let `p_u,p_v` denote its two endpoint ports.

### 5.2 The all-3 quotient

First give every branch push three. Then every branch `b` has

\[
\boxed{\sigma(b)=18+p_b.}
\tag{5.1}
\]

Construct a finite constraint graph `J` as follows.

- For each matching chain with `k_e=1`, identify its two branch endpoints. By Lemma 3.1 this is exactly the relation `p_u=p_v`.
- Keep every direct branch edge of `D` as an inequality edge in the quotient.
- For every matching chain with `k_e=2`, add an inequality edge between its endpoints. Since both boundary pushes are three, Lemma 3.1 says precisely `p_u!=p_v`.
- Chains with `k_e>=3` contribute no port constraint.
- Parallel inequality edges can be suppressed.

The hypothesis in Theorem 5.1 is exactly what prevents a direct `D` edge from turning into a loop after a `k=1` identification. Thus `J` is loop-free.

A singleton quotient vertex has degree at most three: two `D` incidences and, only when its matching chain has length two, one matching inequality. A quotient vertex formed by contracting a `k=1` matching pair has degree at most four, from the four direct `D` incidences of its two preimages. Therefore

\[
\Delta(J)\le4.
\tag{5.2}
\]

If a connected component of `J` is not `K_5`, then it is 4-colorable. Indeed, components of maximum degree at most three are greedily 4-colorable; for maximum degree four, Brooks' theorem gives four colors unless the component is `K_5` (odd-cycle exceptions need only three colors).

Take such a coloring with colors `{0,1,2,3}` and assign the resulting color as the port value `p_b` for every branch represented by that quotient vertex. Then:

- a `k=1` chain gets equal ports as required;
- a `k=2` chain gets unequal ports as required;
- every `k>=3` chain can be completed by Lemma 3.1;
- every direct branch edge has different ports at its endpoints, so (5.1) separates it;
- every branch--chain edge is proper by (4.2)--(4.3).

Hence every non-`K_5` component is solved.

### 5.3 Why a `K5` quotient has one exact shape

Suppose a component of `J` is `K_5`. Every vertex of that component has degree four. A singleton quotient vertex has degree at most three, so **all five quotient vertices must come from `k=1` matching-pair contractions**.

Thus there are exactly ten branch preimages. Each quotient vertex `q` consists of a pair `q_0,q_1` joined through one internal degree-two vertex, and the four `K_5` edges incident with `q` are split into two pairs according to whether their direct `D` edge meets `q_0` or `q_1`. There are three possible pairings of four neighbors at each quotient vertex, hence `3^5=243` local lifts, but the next argument handles all of them uniformly.

### 5.4 One push-2 defect repairs every `K5` lift

Choose a quotient vertex `A={a_0,a_1}`. Set

\[
\rho(a_0)=2,
\qquad
\rho(b)=3\quad\text{for every other branch }b.
\tag{5.3}
\]

Give the unique internal vertex on the `A` matching chain port value

\[
p_A=0.
\]

Let `S={s_0,s_1}` be the two quotient neighbors of `A` whose direct edges meet `a_0`, and let `T={t_0,t_1}` be the two whose direct edges meet `a_1`.

Relative to the common baseline `18`, the branch sums on direct `D` edges now have the following effective labels:

- `a_0`: `p_A-3=-3`;
- `a_1`: `p_A=0`;
- at each `s in S`, the prebranch incident with `a_0` has label `p_s-1`, while its paired prebranch has label `p_s`;
- all prebranches in the two `T` classes have labels `p_t`.

Assign the two `T` ports the values `2` and `3`. Assign the two `S` ports the values `0` and `1`, with the following only rule. Look at the `K_5` edge joining the two vertices of `S`. If exactly one endpoint of that edge is the prebranch whose label is shifted by `-1`, give **that** quotient vertex port `0`; if zero or both endpoints are shifted, either order of `0,1` is allowed.

Now inspect all types of direct edge.

- `A--S`: the labels are `-3` and one of `-1,0`.
- `A--T`: the labels are `0` and one of `2,3`.
- `S--T`: the `S` label lies in `{-1,0,1}` and the `T` label in `{2,3}`.
- `T--T`: the labels are `2` and `3`.
- `S--S`: with no shifted endpoint the labels are `0,1`; with two shifted endpoints they are `-1,0`; with exactly one shifted endpoint, the rule above makes them `-1,1`.

Every pair is distinct. Each `k=1` matching chain has only one internal vertex, so it has no internal chain edge to check, and the branch--chain edges remain proper by (4.3). Thus the one-defect construction solves every `K_5` lift.

Combining Sections 5.2--5.4 gives a proper `{0,1,2,3}`-valued pushing scheme on the whole 2-core.

### 5.5 Reattaching the deleted forest

For completeness, use the same leaf-extension lemma as in the preceding R20 theorem. If a graph `H` already has a proper pushing scheme with values in `{0,1,2,3}`, and a new leaf `w` is attached to a nonisolated vertex `u` with current degree at most two, keep all old pushes and put `rho(w)=x`.

Then

\[
\sigma_{H+uw}(u)=\sigma_H(u)+(1+\rho(u))+x.
\]

Each old neighbor of `u` forbids at most one value of `x`, so at most two of the four values `0,1,2,3` are forbidden. The new leaf edge is automatically safe because

\[
\sigma_{H+uw}(u)-\sigma_{H+uw}(w)=\sigma_H(u)>0.
\]

Attach the forest deleted in taking the 2-core in increasing distance from the core. Because `Delta(G)<=3`, immediately before each attachment the parent has current degree at most two. This extends the scheme to all of `G` and proves Theorem 5.1. QED.

## 6. What this says about the failed all-3 route

The proof identifies the first genuine obstruction to the simplest port algorithm, without confusing it with an obstruction to the conjecture.

Under the loop-free hypotheses, setting every branch push to three reduces the direct-edge problem to four-coloring `J`. The only possible chromatic obstruction is `K_5`; in that case the all-3 construction really is impossible, since the five quotient vertices would require five distinct port values from `{0,1,2,3}`. But one push-2 defect supplies the missing degree of freedom and solves every lift.

The remaining local obstruction for this proof is therefore sharper than before:

\[
\boxed{\text{a one-internal-vertex matching chain whose branch endpoints are already joined by a direct branch edge}.}
\]

Equivalently, after the `k=1` identification the quotient has a loop. This is the simplest special case the next recovery should understand. Mixed path components of `D=C[B]` (degrees one and two together) are a second remaining structural frontier.

## 7. Exact validation, after the idea

Only after the idea note was committed did I add

`artifacts/R20/bmo_branch_cycle_brooks_exact.py`

at creation commit

`d1085ac6ca88646a7e9a857836cd5b04a005a1a4`.

I executed the same script locally with exact integer arithmetic and archived its output at

`artifacts/R20/bmo_branch_cycle_brooks_exact.out`

commit

`3c206cafc63f131530a31fb528b02d978e7c35de`.

The archived output is

```text
chain_constructive_cases=6400
chain_lengths_checked=1..100
branch_chain_gap_cases=192
minimum_branch_minus_chain_sigma_gap=3
k5_local_pairing_configs_checked=243
k5_all3_ansatz_successes=0
k5_one_defect_failures=0
VERDICT=PASS
STATUS=SELF_CHECK_ONLY_PARTIAL_FOR_BMO_CONJECTURE_2_6
```

The checker verifies the constructive chain-transfer algorithm for both boundary pushes in `{2,3}`, every endpoint-port pair and all chain lengths through 100; the exact branch--chain gap; every one of the 243 `K_5` local pairings; and the impossibility of the all-3 four-port coloring on a `K_5` quotient. The infinite theorem itself rests on the written proof above; the computation is a self-check, not its substitute.

Both the checker and archived output were read back at their returned commit SHAs. No floating-point calculation or numerical SDP output is involved.

## 8. Fixed metric, status, and stuck trigger

The frozen fleet metric remains

\[
\boxed{n_{\rm all}=9}.
\]

This theorem gives a new infinite subclass but does not certify every nice graph on ten vertices, so it does not move the fixed all-graphs order metric.

The `8 -> 9` census run reset the stagnation count. The two subsequent R20 reports both had `9 -> 9`; this report is therefore **unchanged run 3** after that reset. Under Section I, the **next R20 invocation must be a thinking-only stuck run**: no new lemma/checker should be manufactured merely to keep the track active.

The exact statement blocking the current structural program is now the full source conjecture outside the covered subcubic classes, with the immediate subcubic obstruction concentrated at the short-theta loop described in Section 6 and at mixed path components of `D`.

The source-level status remains

`PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY`.

There is no P26 audit, no second outside audit, no closure claim, no refutation claim, and no novelty certification.

The next nonrepeating Section-B moves reserved for the required stuck/recovery run are **#6 DEFORM TO A SOLVABLE POINT, #12 FIND WHAT IS CONSERVED, #23 DO WHAT THE PROPOSER DID NOT EXPECT**. The recovery should compare the short-theta loop against the nearest solved cubic proof and decide whether to port that technique, solve this simplest remaining special case, or formally hand off if the obstruction cannot be moved.

## 9. Model/scheduler control status

The current operational manifest still records no binding scheduler model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution control. Accordingly this report does not claim GPT-6 or maximum reasoning. The historical P26 `You cannot modify this task` response was an authorization-context boundary; later authorized context succeeded. No scheduler, permission, email, Drive, public-posting or shared-root change was attempted here.

## ledger_delta

```yaml
ledger_delta:
  track: R20
  source: "Julien Bensmail, Clara Marcille, Mano Orenga, Pushing Vertices to Make Graphs Irregular, DMTCS 27:3 (2025), Conjecture 2.6"
  ownership: "R20 exclusive; operations/claims/BMO-2025-PUSHING-DELTA.md"
  stale_predecessor: "I0100 Paley one-localization remains historical/frozen in later R20 continuity; not reopened"
  metric: n_all
  before: 9
  after: 9
  movement: "NO MOVEMENT"
  unchanged_count_after_reset: 3
  status: "PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY"
  tried_moves: [3, 16, 19]
  new_result: "SELF_CHECK_ONLY theorem: subcubic graphs whose 2-core branch graph is 2-regular and has no direct-edge plus one-internal-vertex parallel branch chain satisfy P^ell<=3; K5 Brooks exception handled by one push-2 defect"
  remaining_obligation: "full Conjecture 2.6; immediate subcubic frontier is the short-theta quotient-loop case and mixed degree-1/degree-2 branch paths"
  evidence:
    idea_before_code: "39167b531e65137e672eb321c0c2e77d4df603c3"
    exact_checker: "d1085ac6ca88646a7e9a857836cd5b04a005a1a4"
    exact_output: "3c206cafc63f131530a31fb528b02d978e7c35de"
    exact_output_verdict: "PASS"
  audits: []
  next_protocol: "THINKING_ONLY_STUCK_RUN_REQUIRED"
  next_moves: [6, 12, 23]
```
