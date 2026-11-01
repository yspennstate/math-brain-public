Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `n_all: 8 -> 8`; status `PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY`; methods #13 FIND WHAT ONLY INCREASES, #19 MAKE IT AN ALGORITHM, #24 FIND THE EXTREMAL OBJECT.**

# R20 — finite interface algebra for triangular cacti; all three-cycle cores close, and a four-cycle obstruction to the strongest mod-3 route

## 0. Continuity, ownership, and the fixed metric

I did **not** reopen the stale scheduler-title target Bandeira / Randomstrasse Conjecture 26 / I0100. That track was already handed off after its six-unchanged-run rule; its historical exact localized-Paley frontier remains frozen at `p_max=1213`, and finite certificates there never proved the source asymptotic. I also did not return to the subsequently handed-off KNSV target.

The current canonical R20 claim is still

`operations/claims/BMO-2025-PUSHING-DELTA.md`,

owned exclusively by R20 and marked `CLAIMED / READY / CLOSABLE OUTSIDE`. The source is Julien Bensmail, Clara Marcille and Mano Orenga, *Pushing Vertices to Make Graphs Irregular*, DMTCS 27:3 (2025), article 7, DOI `10.46298/dmtcs.14963`, Conjecture 2.6:

\[
P^\ell(G)\le \Delta(G)
\]

for every nice finite simple graph `G` (no connected component `K_2`). For a pushing scheme `rho`,

\[
\sigma(v)=(1+\rho(v))d(v)+\sum_{u\sim v}\rho(u),
\]

and the scheme is proper when adjacent vertices have distinct `sigma` values.

The fixed all-graphs metric remains

\[
n_{\rm all}=\max\{n:\text{every nice simple graph of order at most }n\text{ is exactly certified}\}.
\]

The supported value is still `n_all=8`. The preceding R20 reports established, at self-check status, the source-valid structural results `P^l<=2` for every connected unicyclic graph and for every connected cactus with exactly two cycles. The most recent report was

`runs/R20/2026-09-18T21-39-02Z_bmo_bicyclic_cactus_transparency_7c2e91.md`,

whose next assigned moves were exactly #13, #19 and #24. This run continues from that state rather than restarting.

At run start I reread the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the canonical BMO claim, and the newest R20 report. Repository search recovered no competing source-matching BMO owner or later fleet closure. No shared root and no other track's file is edited here.

## 1. Current source and later-literature check

Checked 18 September 2026 UTC / 19 September locally.

Primary source:

- Julien Bensmail, Clara Marcille, Mano Orenga, *Pushing Vertices to Make Graphs Irregular*, DMTCS 27:3 (2025), article 7, DOI `10.46298/dmtcs.14963`, `https://dmtcs.episciences.org/16418`.
- The current PDF still states Conjecture 2.6 exactly as `P^l(G)<=Delta(G)` for every nice graph.
- In its conclusion the source explicitly singles out cacti. It says the authors tried modulo methods toward the optimal cactus result `P^l(G)<=2`, believed they had a functional proof, but the proof depended so heavily on exhaustive computer checks that they did not present a formal proof; they ask for a readable direct proof.

Current follow-up:

- Dieter Rautenbach, Laurin Schwartze, Florian Werner, *Coloring by Pushing Vertices*, Ars Combinatoria 167 (2026), 147--157, DOI `10.61091/ars167-10`, published online 17 June 2026.
- Its abstract still describes the Bensmail--Marcille--Orenga `Delta` bound as conjectural and proves it for cubic graphs and regular bipartite graphs.

Fresh bounded queries for the exact source title/DOI, `Conjecture 2.6`, `pushing scheme cactus`, the three original authors, and the 2026 follow-up found the source, the follow-up, mirrors/indexes and unrelated cactus-labelling work, but no later source-matching general proof or readable optimal cactus proof. This is dated bounded negative evidence only, not a global novelty certificate.

## 2. Idea before code

Before writing the checker I committed

`artifacts/R20/2026-09-18T22-04-40Z_bmo_three_cycle_state_idea_before_code.md`

at commit

`1a3ad6b1c6614a07936ca9f05da5e60bd988bd5c`,

and read it back at that exact commit. The note proposes a finite interface algebra over `F_3`, asks whether a triangle branch becomes more flexible as it is moved away from the root, and asks where the strongest all-core-edges-modulo-3 architecture first fails. No validation code preceded the note.

## 3. Rooted interface states

The preceding report used the edge-residue language

\[
w_{uv}=1+\rho(u)+\rho(v)\pmod3,
\qquad
\sigma(v)\equiv\sum_{e\ni v}w_e\pmod3.
\]

For a rooted cactus core `H` with root `a`, define its interface relation

\[
\mathcal R(H)\subseteq \mathbf F_3^3
\]

as follows. A triple `(r,s,t)` belongs to `R(H)` when there is a push assignment on the vertices of `H` such that

1. `rho(a)=r`;
2. `t` is the contribution at `a` from edges of `H` itself;
3. after an unspecified parent contribution is added, the desired final residue at `a` is `s`;
4. every edge internal to `H` is proper modulo `3`, using `s` as the final root residue.

The point of retaining both `s` and `t` is that a component can be composed before the parent contribution is known. When `H` is the whole core, there is no parent contribution, so it closes exactly when its relation contains a **diagonal state**

\[
(r,s,t)\quad\text{with }s=t.
\]

Let

\[
\mathsf U=\{(r,s,0):r,s\in\mathbf F_3\}
\]

be the empty rooted collection.

There are three exact composition operations.

### Bridge operation `B`

If `R` is the child relation and a new root is joined to the child root by one bridge, define `B(R)` by the following exact rule. Let the new root push be `r`, desired final color `s`, and bridge residue `w`; then the child push is

\[
x=w-1-r.
\]

If `(x,c,q) in R`, the child final color after the bridge is attached must satisfy

\[
c=w+q,
\]

and bridge properness requires `c != s`. The new root contribution is `w`. These conditions define `B(R)` exactly.

### Root merge `M`

If two rooted collections are identified at the same root, then

\[
(r,s,t_1)\in R,\quad(r,s,t_2)\in S
\]

compose to

\[
(r,s,t_1+t_2)\in M(R,S).
\]

Both children use the same final root color `s`.

### Triangle operation `T`

Create a triangle with root `a` and nonroot vertices `b,c`, and attach rooted states `R,S` at `b,c`. If the pushes are `r,x,y`, the three triangle-edge residues are

\[
w_{ab}=1+r+x,\quad w_{bc}=1+x+y,\quad w_{ca}=1+y+r.
\]

The triangle contribution at the root is

\[
t=w_{ab}+w_{ca}.
\]

A state is admitted exactly when the child relations can supply final colors for `b,c` so that the three final triangle colors are pairwise distinct.

All arithmetic in this section is in `F_3`.

## 4. #13 FIND WHAT ONLY INCREASES: a leaf triangle saturates after three bridges

The leaf triangle relation is

\[
R_0=T(\mathsf U,\mathsf U)
 =\{(r,r-1,t):r,t\in\mathbf F_3\},
\]

which is exactly the triangle-syndrome lemma from the preceding run.

Define

\[
R_k=B^k(R_0).
\]

Then there is a sharp four-state stabilization:

\[
\boxed{
\begin{aligned}
R_0&=\{(r,s,t):s=r-1\},\\
R_1&=\{(r,s,t):t\ne s+r-1\},\\
R_2&=\{(r,s,t):t\ne 1-r\},\\
R_3&=\mathbf F_3^3,
\end{aligned}}
\]

and therefore `R_k=F_3^3` for every `k>=3`.

### Proof

For `R_1`, let the bridge residue be `t`, so the child push is

\[
x=t-1-r.
\]

The triangle state requires the child final color to be `x-1`. Its internal triangle contribution can be chosen arbitrarily, hence the only bridge condition is

\[
x-1\ne s.
\]

Substituting for `x` gives exactly

\[
t\ne s+r-1.
\]

For `R_2`, let the second bridge have residue `t`, child push `x=t-1-r`, child final color `c`, and child-side contribution `q=c-t`. The `R_1` condition is

\[
q\ne c+x-1.
\]

After cancellation this becomes

\[
t\ne1-r,
\]

independent of `c`; one can then choose `c!=s` to make the new bridge proper.

For `R_3`, the `R_2` condition forbids only one child contribution, while the new bridge properness forbids only one child final color. Equivalently, for fixed `(r,s,t)` there are at most two forbidden choices among three possible child final colors, so at least one remains. Thus every triple occurs. Since `B(F_3^3)=F_3^3`, saturation is permanent. QED.

The state-set sizes are therefore

\[
9,18,18,27.
\]

This is the useful monovariant here: **a triangular leaf branch becomes completely interface-transparent after three bridge steps**.

Two merge identities follow immediately:

\[
M(R_0,R_k)=R_0\qquad(k=0,1,2,3),
\]

because `R_0` already supplies every contribution once its syndrome `s=r-1` is met; and

\[
M(R_i,R_j)=\mathbf F_3^3\qquad(i,j\ge1),
\]

because for every fixed `(r,s)`, both contribution sets have size at least two, and the sum of two two-element subsets of `F_3` is all of `F_3`.

## 5. #19 MAKE IT AN ALGORITHM: exact central-triangle composition table

Now put two branch types `R_i,R_j` on two vertices of a central triangle and root the core at the third vertex. Surprisingly, the complete `4 x 4` table collapses to only three relations.

Define

\[
A=\{(r,s,1-r-s):r,s\in\mathbf F_3\},
\]

and

\[
C=\{(r,s,s+r-1):r,s\in\mathbf F_3\}.
\]

Then

\[
\boxed{
T(R_i,R_j)=
\begin{cases}
A,&(i,j)=(0,0),\\
C,&(i,j)=(2,2),\\
\mathbf F_3^3,&\text{for all other 14 ordered pairs.}
\end{cases}}
\]

This is not merely a computer table; it has the following direct proof.

### Proof of the table

Let the root push be `r`, the two other triangle pushes be `x,y`, and set

\[
z=x+y,\qquad d=x-y.
\]

The triangle-only residues at the nonroot vertices are

\[
c_b=r-1-d,\qquad c_c=r-1+d,
\]

while the triangle contribution at the root is

\[
t=-1-r+z.
\]

If the final root residue is `s`, triangle properness means the other two final residues are, in some order,

\[
s+\varepsilon,\qquad s-\varepsilon,
\qquad \varepsilon\in\{1,-1\}.
\]

Substituting the explicit formulas for `R_0,R_1,R_2,R_3`, the branch conditions reduce to:

- `R_0` at `b`: it fixes `x=s+epsilon+1`, hence fixes `d` once `z,epsilon` are fixed;
- `R_0` at `c`: similarly fixes `y=s-epsilon+1`;
- `R_1` at `b`: it forbids exactly `d=z-r-1`;
- `R_1` at `c`: it forbids exactly `d=r-z+1`;
- `R_2` at `b`: it requires `z != s-r+epsilon`;
- `R_2` at `c`: it requires `z != s-r-epsilon`;
- `R_3`: no condition.

For `(R_0,R_0)`, the two exact equations force

\[
z=-s-1,
\]

hence

\[
t=-1-r+z=1-r-s,
\]

which is exactly `A`.

For `(R_2,R_2)`, the two forbidden values are `s-r+1` and `s-r-1`, so the only possible third residue is

\[
z=s-r.
\]

Hence

\[
t=-1-r+z=s+r-1,
\]

which is exactly `C`.

It remains to prove that every other ordered pair gives every target triple `(r,s,t)`. Fix such a target; equivalently, fix

\[
z=t+1+r.
\]

If neither branch is `R_0`, then any `R_2` branch forbids one choice of `epsilon`; unless both branches are `R_2` (the exceptional case already handled), one can choose `epsilon` satisfying all `R_2` requirements. The remaining `R_1` constraints forbid at most two values of `d`, leaving at least one of the three residues available. `R_3` imposes nothing.

If exactly one branch is `R_0`, then that branch fixes `d` for each of the two choices of `epsilon`, and the two resulting values of `d` are distinct. An `R_1` branch forbids only one `d`, so one choice of `epsilon` survives; an `R_2` branch forbids only one `epsilon`, so again one survives; and `R_3` imposes nothing. Thus every `z`, hence every `t`, is attainable.

These cases exhaust the 14 nonspecial ordered pairs. QED.

Each of the three possible output relations has a diagonal state:

- `A`: `s=t` iff `s=r-1`, giving three diagonal states;
- `C`: `s=t` iff `r=1`, giving three diagonal states;
- `F_3^3`: nine diagonal states.

## 6. Theorem: every connected triangular cactus with at most three cycles has `P^l<=2`

### Theorem 6.1 — SELF_CHECK_ONLY

Let `G` be a connected cactus all of whose cycle blocks are triangles, and suppose `G` has at most three cycles. Then

\[
\boxed{P^\ell(G)\le2.}
\]

For exactly three cycle blocks the proof is as follows; the one- and two-cycle cases were already covered by the preceding R20 results and also follow from the same state algebra.

First remove ordinary tree appendages. The previous tree-transparency lemma restores them afterwards without changing the core root residues; pendant edges are automatically proper over the integers because their positive edge label is a strict summand of the nonleaf endpoint sum.

The minimal block tree connecting three triangle blocks has only two possible reduced shapes.

### Y topology

The three triangles lie on three arms meeting at one articulation/bridge-tree branching vertex. Let `a,b,c in {0,1,2,3}` be the three bridge distances, truncated at `3` because `R_k=R_3` thereafter. The root relation is

\[
M(M(R_a,R_b),R_c).
\]

If any one of `a,b,c` is zero, `R_0` absorbs every merge and the result is `R_0`. If none is zero, merging the first two branches gives `F_3^3`, and the final merge remains `F_3^3`. Both relations have a diagonal state. Thus the whole core closes.

### Path topology

One triangle lies between the other two, and the two leaf triangles attach through bridge paths to two distinct vertices of the central triangle. Root at the third central-triangle vertex. With truncated distances `a,b in {0,1,2,3}`, the root relation is

\[
T(R_a,R_b).
\]

By the table in Section 5 this is `A`, `C`, or `F_3^3`, each of which has a diagonal state. Thus this core also closes.

Taking representatives `rho(v) in {0,1,2}`, all core edges are distinguished modulo `3`, hence over the integers; restoring ordinary tree appendages preserves properness. Therefore `P^l(G)<=2`. QED.

This theorem does **not** settle every three-cycle cactus: if a path-topology cactus has a nontriangle central cycle and both leaf cycles are triangles, that remaining case is not covered by the central-triangle table. If a nontriangle cycle is a leaf block, the previous transparency lemma strips it and reduces to the already solved two-cycle case. I therefore state the theorem only for triangular cacti, rather than silently extending it to all three-cycle cacti.

## 7. #24 FIND THE EXTREMAL OBJECT: the first strong-mod-3 failure occurs at four triangular cycles

Among all exact three-triangle core types above, the smallest diagonal-state count is

\[
\boxed{3}.
\]

It is attained, for example, by the all-direct Y core `M(M(R_0,R_0),R_0)=R_0`, and by the central-triangle special types `A` and `C`. Thus no three-cycle triangular core can kill the strong modulo-3 architecture.

At four triangle blocks, however, there is an exact obstruction.

Start with a central triangle having two `R_2` branches. Section 5 gives

\[
T(R_2,R_2)=C.
\]

Two bridge steps transform `C` as follows:

\[
B(C)=\{(r,s,1-r):r,s\in\mathbf F_3\},
\]

and

\[
B^2(C)=\{(r,s,t):s\ne r-1\}.
\]

The first identity follows directly from the defining equation of `C`: if the new bridge has residue `t`, the child push is `x=t-1-r`, while `C` requires `q=c+x-1` and `c=t+q`; cancellation forces `t=1-r`. For the second bridge, the child final color is forced to `r-1`, so bridge properness is exactly `s!=r-1`.

Now merge this branch with a direct leaf triangle `R_0`, which requires exactly the opposite syndrome `s=r-1`. Hence

\[
\boxed{M(R_0,B^2(T(R_2,R_2)))=\varnothing.}
\]

Equivalently, the explicit rooted expression

\[
M\bigl(F, B^2(T(B^2(F),B^2(F)))\bigr)
\]

has **no** assignment in which every edge of its four-triangle bridge/cycle core is distinguished modulo `3`.

This proves that, by number of triangle blocks, four is the first possible failure of the strongest all-core-edges-mod-3 certificate: all <=3 triangular-cycle cores close, while this four-cycle core does not.

Crucially, this is **not a counterexample** to the pushing theorem or to `P^l<=2` for cacti.

The exact constructed graph has 15 vertices, 18 edges and four triangle cycles. Its edges are

```text
(0,1) (0,2) (0,3) (1,2)
(3,4)
(4,5) (4,10) (5,10)
(5,6) (6,7)
(7,8) (7,9) (8,9)
(10,11) (11,12)
(12,13) (12,14) (13,14)
```

so the four triangles are `(0,1,2)`, `(4,5,10)`, `(7,8,9)`, `(12,13,14)` and the remaining edges form bridge paths.

An exact integer proper `{0,1,2}` pushing witness is

\[
(\rho(0),\ldots,\rho(14))=
(0,0,2,0,0,0,1,1,0,1,0,2,0,0,2).
\]

The resulting integer sums are

\[
(5,4,6,2,3,4,5,8,4,5,5,6,7,4,6),
\]

and are unequal across every edge. Four edges nevertheless have equal sums modulo `3`:

\[
(0,3),\ (6,7),\ (7,9),\ (12,13).
\]

Thus the graph pinpoints exactly why the strongest modulo-3 proof architecture is too rigid: an integer proper scheme can deliberately tolerate equal residues when the actual sums differ by a nonzero multiple of three. This gives a concrete explanation for why a purely residue-proper induction can stall even though the cactus itself still has a two-push witness.

## 8. Exact validation

Only after the idea and derivations above were written did I build the exact checker

`artifacts/R20/bmo_three_cycle_state_exact.py`

at commit

`f4fa4ecfd026fbff36c2f292f375c388aad2c6c5`,

and archive its executed output as

`artifacts/R20/bmo_three_cycle_state_exact.out`

at commit

`261c6683865afb15a220647c36fab59b71734905`.

Both were read back at those exact commits.

The checker uses only finite integer/residue arithmetic. It verifies:

- `|R_0|,|R_1|,|R_2|,|R_3| = 9,18,18,27`;
- the exact formulas for `R_0,R_1,R_2` and saturation `R_3=F_3^3`;
- all sixteen central-triangle compositions, with only `(0,0)->A` and `(2,2)->C` exceptional;
- all 64 truncated Y-topology triples and all 16 path-topology pairs, each with a diagonal state;
- minimum diagonal count `3` in both reduced three-cycle topologies;
- the exact empty four-cycle relation;
- the explicit 15-vertex graph and its cyclomatic number four;
- the displayed `{0,1,2}` integer witness, including integer properness on every edge;
- the fact that the same witness has four modulo-3 edge conflicts.

The archived output ends `VERDICT=PASS`. This is a self-check, not an independent audit.

## 9. What moved and what did not

The fixed source metric does **not** move:

\[
\boxed{n_{\rm all}:8\to8.}
\]

The run nevertheless makes structural progress:

1. a leaf triangle branch becomes completely transparent after three bridge steps;
2. the complete three-cycle triangular-cactus interface algebra collapses to three relations;
3. every triangular cactus with at most three cycle blocks has `P^l<=2`;
4. a concrete four-cycle triangular cactus is the first obstruction to the stronger requirement that every core edge be distinguished modulo three;
5. that same graph has an exact integer two-push witness, proving the obstruction belongs to the proof architecture rather than the source statement.

This is the **third consecutive BMO run with no movement of the fixed all-graphs metric** (`unchanged_count_on_BMO_target=3`). Under Section I, the next R20 invocation must therefore be a **thinking-only stuck run**, not another theorem/checker run. The precise blocker to record there is now sharper than before:

\[
\boxed{
\text{How can one induct on cactus blocks while allowing controlled edges with }
\sigma(u)\equiv\sigma(v)\pmod3
\text{ but }\sigma(u)\ne\sigma(v)\text{ over }\mathbf Z?
}
\]

The natural next recovery choice is to **prove the simplest unproved special case** rather than extend the failed strong-residue rule: path-topology three-cycle cacti whose two leaf cycles are triangles and whose central cycle has length at least four, or equivalently develop one local integer-lift repair state that survives the 15-vertex obstruction. The next nonrepeating Section-B moves recorded for that thinking run are **#15 BREAK THE SYMMETRY ON PURPOSE, #20 FIND WHY THE ALGORITHM FAILS, #29 ADD THE POINTS AT INFINITY**.

## 10. Honest status and closure boundary

Current source status: **PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY / current-open-looking**.

No claim here proves or refutes BMO Conjecture 2.6. No claim here proves the full cactus statement. No finite all-graphs order beyond eight is claimed. No numerical heuristic is promoted to an exact certificate. No P26 audit or second outside-track audit exists for the new theorem.

Source closure still requires the full source-level argument or a source-valid exact counterexample, a current prior-art search, and two independent audits from other tasks under the controlling protocol.

## 11. Model / scheduler-control status

The actual model visible to this run is **GPT-5.6 Sol**. The reasoning level is not authenticated by the runtime surface, so I report it as **UNVERIFIED** and do not claim GPT-6/maximum.

The repository's current implementation manifest still records that the exposed task-control interface has no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution control. The requested GPT-6/maximum setting is therefore prompt text only on this surface. The historical P26 attempt that returned `You cannot modify this task` is an authorization boundary; the lawful workaround is an owner/admin-authorized product or backend surface that exposes the required controls, not a permission bypass or duplicate schedule. No scheduler, permission, email, Drive, or public-posting change was attempted in this run.

## ledger_delta

```yaml
ledger_delta:
  worker: R20
  source:
    canonical_claim: operations/claims/BMO-2025-PUSHING-DELTA.md
    authors: Julien Bensmail; Clara Marcille; Mano Orenga
    title: Pushing Vertices to Make Graphs Irregular
    venue: DMTCS 27:3 (2025), article 7
    doi: 10.46298/dmtcs.14963
    target: Conjecture 2.6, P^l(G) <= Delta(G) for every nice graph
    source_adjacent_question: readable proof of optimal P^l(G) <= 2 for nice cacti
    current_status_check: 2026-09-18 UTC; general conjecture still stated as conjectural in the 2026 Rautenbach-Schwartze-Werner follow-up; bounded search found no later source-matching general/cactus proof
  metric:
    name: n_all
    before: 8
    after: 8
    movement: false
    unchanged_count_on_BMO_target: 3
  status: PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY
  methods_tried: [13, 19, 24]
  new_claims:
    - SELF_CHECK_ONLY: triangular leaf-interface states stabilize after three bridges: sizes 9,18,18,27 and R_3 = F_3^3
    - SELF_CHECK_ONLY: exact 4x4 central-triangle state table has only A, C, and F_3^3
    - SELF_CHECK_ONLY: every connected triangular cactus with at most three cycle blocks has P^l <= 2
    - SELF_CHECK_ONLY: a specific four-triangle 15-vertex cactus has empty strong-mod-3 root relation, so four cycles are the first obstruction by cycle count to this stronger certificate architecture
    - EXACT FINITE WITNESS: that same four-cycle cactus has a proper integer {0,1,2} pushing scheme; therefore the mod-3 obstruction is not a source counterexample
  remaining_obligation: prove or refute BMO Conjecture 2.6 for every nice graph; source-adjacent cactus question remains unresolved, with the next stuck run required to address controlled integer lifts beyond strict residue separation
  evidence:
    idea_before_code:
      path: artifacts/R20/2026-09-18T22-04-40Z_bmo_three_cycle_state_idea_before_code.md
      commit: 1a3ad6b1c6614a07936ca9f05da5e60bd988bd5c
    checker:
      path: artifacts/R20/bmo_three_cycle_state_exact.py
      commit: f4fa4ecfd026fbff36c2f292f375c388aad2c6c5
    output:
      path: artifacts/R20/bmo_three_cycle_state_exact.out
      commit: 261c6683865afb15a220647c36fab59b71734905
  audits:
    p26: NONE
    second_other_track: NONE
  next_run:
    mode: REQUIRED_SECTION_I_THINKING_ONLY
    recovery_choice: prove the simplest unproved special case / identify an integer-lift interface that survives the four-cycle residue obstruction
    methods: [15, 20, 29]
```
