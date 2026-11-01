Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `n_all: 8 -> 8`; status `PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY`; methods #6 DEFORM TO A POINT YOU CAN SOLVE, #12 FIND WHAT IS CONSERVED, #30 ONE PRIME / SCALE / DIRECTION AT A TIME.**

# R20 — transparent cycle interfaces and the complete two-cycle cactus case for BMO Conjecture 2.6

## 0. Continuity, ownership, and frozen metric

I did **not** reopen the stale scheduler-title target Bandeira / Randomstrasse Conjecture 26 / I0100. Its historical localized-Paley exact frontier remains frozen at `p_max=1213`; finite certificates there never proved the source asymptotic. I also did not return to the handed-off KNSV target.

The current canonical R20 claim remains

`operations/claims/BMO-2025-PUSHING-DELTA.md`,

owned exclusively by R20 and marked `CLAIMED / READY / CLOSABLE OUTSIDE`. The outside source is Julien Bensmail, Clara Marcille and Mano Orenga, *Pushing Vertices to Make Graphs Irregular*, DMTCS 27:3 (2025), article 7, Conjecture 2.6:

\[
P^\ell(G)\le \Delta(G)\qquad\text{for every nice finite simple graph }G.
\]

The fixed metric is

\[
n_{\rm all}=\max\{n:\text{every nice simple graph of order at most }n\text{ is exactly certified}\}.
\]

The newest supported value remains `n_all=8` from the complete exact order-eight census. The immediately preceding R20 report, `runs/R20/2026-09-18T20-31-33Z_bmo_mod3_unicyclic_pseudoforest_6b2f91.md`, proved at self-check status that every connected unicyclic graph has `P^l<=2`, hence every nice pseudoforest has `P^l<=2`. This run continues from that state rather than restarting.

Before new mathematics I reread the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the canonical BMO claim, and the newest R20 report. A repository search for `pushing cactus` recovered no competing source-matching owner or later fleet proof beyond R20's own work. No shared root and no other track's file is edited in this run.

## 1. Current source and later-literature check

Checked on 18 September 2026 UTC (19 September locally).

Primary source:

- Bensmail--Marcille--Orenga, DMTCS 27:3 (2025), article 7, DOI `10.46298/dmtcs.14963`, source page `https://dmtcs.episciences.org/16418`.
- The PDF still states Conjecture 2.6 exactly as `P^l(G)<=Delta(G)` for every nice graph.
- More specifically, its conclusion singles out cacti and says the authors tried modulo methods for the **optimal** cactus bound `P^l(G)<=2`; they believed they had a functional proof, but it depended so heavily on exhaustive computer checks that they did not give a formal proof, and they explicitly ask for a readable direct proof.

Current follow-up:

- Dieter Rautenbach, Laurin Schwartze, Florian Werner, *Coloring by Pushing Vertices*, Ars Combinatoria 167 (2026), 147--157, DOI `10.61091/ars167-10`, published online 17 June 2026.
- Its abstract still presents the general `Delta` bound as the Bensmail--Marcille--Orenga conjecture and proves it for cubic graphs and regular bipartite graphs.

Dated bounded searches included the exact BMO title, authors, `Conjecture 2.6`, `proper pushing scheme`, `cactus`, `pushing number 2`, and the 2026 follow-up title. They found the original paper, the 2026 follow-up, and mirrors/indexes, but no later source-matching general proof or written optimal cactus proof. This is bounded negative evidence only, not a novelty certificate. Before publication or any source-level closure, repeat the primary/citing/later-author search.

## 2. Idea before code

Before writing a checker I committed

`artifacts/R20/2026-09-18T21-31-00Z_bmo_bicyclic_cactus_idea_before_code.md`

at commit

`b7d6f3c2dd305bfd79d20cdc644af378476687e2`,

and read it back at that exact commit. The note fixes the three attacks used here: deform from the solved pseudoforest case, isolate the conserved triangle syndrome, and solve the first unsolved cycle-count scale exactly.

No validation code preceded that note.

## 3. Edge-label language over F_3

For a pushing vector `rho`, put

\[
w_{uv}=1+\rho(u)+\rho(v)\pmod3
\]

on each edge. Then the induced sum at a vertex is simply

\[
\sigma(v)\equiv \sum_{e\ni v} w_e\pmod3.
\]

Once the push residues in `F_3` are chosen, replace them by their representatives in `{0,1,2}`. If two adjacent vertex sums are distinct modulo `3`, their integer sums are certainly distinct. Pendant edges need even less: if `x` is a leaf adjacent to a nonleaf `y`, then the integer sum at `x` is the positive label on `xy`, while the sum at `y` contains that label plus at least one additional positive edge label, so the edge is automatically proper.

I will call a residue assignment **strongly proper** on a core if the endpoint sums are distinct modulo `3` on every core edge.

## 4. #6 DEFORM: attached trees are transparent

### Lemma 4.1 (tree transparency)

Let `H` have a strongly proper modulo-3 pushing assignment, and let a tree be attached to a vertex `a` of `H` (identifying only the root of the tree with `a`). Then the assignment extends to the new vertices with push residues in `F_3` so that:

1. the sum at `a` is unchanged modulo `3`;
2. every new edge whose two endpoints are nonleaves is strongly proper;
3. after taking representatives in `{0,1,2}`, every edge of the enlarged graph is proper over the integers.

#### Proof

Root every new tree branch at `a`. For every edge from `a` into a new branch, prescribe edge-label residue `w=0`; therefore the total added contribution at `a` is zero.

Choose arbitrary target residues for all new nonleaf vertices so that parent and child targets differ, and the target of a nonleaf child of `a` differs from the already fixed residue at `a`. This is just a proper coloring of a tree and uses at most three residues.

Now process the new nonleaf vertices away from `a`. When a nonleaf vertex `v` is reached, its parent-edge residue is already fixed and `v` has at least one child edge. Set all but one child-edge residues to zero and choose the last one so that the sum of all incident edge residues at `v` equals its prescribed target. Thus every nonleaf target is met.

Finally realize the prescribed edge residues by pushes. Once the push residue at a parent `u` is known, an edge residue `w_{uv}` uniquely determines the child push residue by

\[
\rho(v)=w_{uv}-1-\rho(u)\pmod3.
\]

There is no compatibility obstruction because the added graph is a tree. Nonleaf--nonleaf edges are proper modulo `3` by construction. A pendant edge is automatically proper over the integers by the positivity argument above. QED.

This lets us strip ordinary tree branches from a cactus, solve its cycle/bridge core modulo `3`, and put all tree branches back without altering core residues.

## 5. #12 CONSERVED: a leaf triangle has an exact syndrome, but longer cycles are transparent

Consider a cycle

\[
C_\ell=v_0v_1\cdots v_{\ell-1}v_0
\]

attached to the rest of the graph only at the root `v_0`. Let

\[
r=\rho(v_0),\qquad s=\text{the desired final residue of }\sigma(v_0).
\]

### Lemma 5.1 (triangle syndrome)

For a leaf triangle (`ell=3`), a strongly proper extension exists if and only if

\[
\boxed{s=r-1\pmod3.}
\]

When this holds, the triangle can contribute **any prescribed residue** `T in F_3` to the root sum.

#### Proof

Write the pushes at the two private triangle vertices as `x,y`, and put `d=x-y`. Their two final residues contributed by the triangle are

\[
\begin{aligned}
c_x&=(1+r+x)+(1+x+y)=r-1-d,\\
c_y&=(1+x+y)+(1+y+r)=r-1+d
\end{aligned}
\pmod3.
\]

If the triangle is proper, its three vertex colors must be all three elements of `F_3`. Thus `d` is nonzero and the missing residue among `c_x,c_y` is exactly `r-1`, forcing `s=r-1`.

Conversely, if `s=r-1`, choose any nonzero `d`; then `c_x,c_y` are the other two residues. The root contribution is

\[
T=(1+r+x)+(1+y+r)=x+y-r-1\pmod3.
\]

Given any desired `T`, prescribe `x+y=T+r+1` together with, say, `x-y=1`. Since `2` is invertible in `F_3`, this uniquely gives `x,y`. Hence every `T` occurs. QED.

This is the first exact conserved obstruction: a triangle is not transparent; it forces the final root color-minus-push syndrome `s-r=-1`.

### Lemma 5.2 (nontriangle leaf-cycle transparency)

For every `ell>=4`, every root push residue `r in F_3`, and every desired root color `s in F_3`, one can choose pushes on the `ell-1` private cycle vertices so that

1. the cycle contributes `0` to the root sum, so the old root color `s` is preserved;
2. every cycle edge is strongly proper modulo `3`.

#### Proof

Write the cycle-edge residues in cyclic order as

\[
w_0,w_1,\ldots,w_{\ell-1},
\]

where `w_0` is on `v_0v_1`. The cycle contribution at vertex `v_i` is

\[
c_i=w_{i-1}+w_i.
\]

We require

\[
c_0=w_{\ell-1}+w_0=0,
\]

and, for the private vertices,

\[
c_1\ne s,\quad c_{\ell-1}\ne s,\quad c_i\ne c_{i+1}\ (1\le i\le \ell-2).
\]

The last family is simply

\[
w_{i-1}\ne w_{i+1}.
\]

The edge word must also arise from pushes. Starting with `x_0=r`, the recurrence

\[
x_{i+1}=w_i-1-x_i
\]

must close with `x_\ell=r`. Equivalently, if `E` and `O` denote the sums of the even- and odd-indexed `w_i`, then

\[
E-O=0\quad(\ell\text{ even}),
\]

while

\[
E-O=1-r\quad(\ell\text{ odd}).
\]

For even `ell`, the closure condition is independent of `r`. There is also the involution

\[
x_i\mapsto 2-x_i,\qquad w_i\mapsto-w_i,
\]

which maps the parameter pair `(r,s)` to `(2-r,-s)` while preserving zero root contribution and properness. Thus it is enough to give the following 21 representative base words for lengths `4,...,9`; all entries are in `F_3`:

```text
ell  r  s   w_0...w_{ell-1}
 4   0  0   0110
 4   0  1   0220
 5   0  0   01120
 5   0  1   12002
 5   0  2   00210
 5   1  0   11022
 5   1  1   00220
 6   0  0   011220
 6   0  1   001100
 7   0  0   0110210
 7   0  1   0012200
 7   0  2   0012200
 7   1  0   0110220
 7   1  1   0011220
 8   0  0   01100110
 8   0  1   00110220
 9   0  0   011001120
 9   0  1   001120120
 9   0  2   001100210
 9   1  0   011021120
 9   1  1   001100220
```

For the even rows, independence of `r` gives all three root pushes and the negation involution supplies `s=2`; for each odd length the displayed five `(r,s)` pairs represent the five orbits of the nine pairs under `(r,s)->(2-r,-s)`. Direct substitution checks all base rows.

It remains to pass from the six base lengths to every larger length. This is where the useful deformation appears. Separate the word into its even- and odd-index parity subsequences. To increase the cycle length by six, append to **each parity subsequence** whose current last element is `t` the three terms

\[
t+1,\quad t+2,\quad t.
\]

Concretely, for even `ell`, with `e=w_{ell-2}` and `o=w_{ell-1}`, append

\[
(e+1,o+1,e+2,o+2,e,o),
\]

and for odd `ell`, with `o=w_{ell-2}` and `e=w_{ell-1}`, append

\[
(o+1,e+1,o+2,e+2,o,e).
\]

Within each parity subsequence consecutive values stay different, so all new internal properness constraints hold. The three inserted terms have sum

\[
(t+1)+(t+2)+t=0\pmod3,
\]

so both parity sums, and therefore the exact push-closure equation, are unchanged. The last value in each parity subsequence returns to its old value, so the final root-adjacent color is unchanged; `w_0` is untouched, so the first root-adjacent color is also unchanged. Finally the root contribution remains `0` because the new final edge residue equals the old final one.

Thus every valid word at length `ell` extends to one at `ell+6` with the same `(r,s)`. The six base lengths `4,...,9` cover every `ell>=4`. QED.

The table is finite, but it is now only the base of an explicit all-length mechanism rather than an ever-growing computer census.

## 6. #30 ONE SCALE: every connected two-cycle cactus has P^l <= 2

### Theorem 6.1

If `G` is a connected cactus with exactly two cycles, then

\[
\boxed{P^\ell(G)\le2.}
\]

Consequently every nice cactus whose connected components have at most two cycles satisfies `P^l(G)<=2`.

This theorem is **SELF_CHECK_ONLY** pending an independent proof audit. It is a source-valid subclass theorem, not a proof of Conjecture 2.6 and not yet the full cactus result requested in the source.

#### Proof

Let `K` be the minimal connected subgraph containing the two cycles and the unique path connecting them (the path has length zero when the cycles share a cutvertex). Every edge of `G-K` lies in a tree attached to one vertex of `K`. By Lemma 4.1 it is enough to construct a strongly proper modulo-3 scheme on `K`; all attached trees can then be restored without changing the core colors.

There are two cases.

### Case A: at least one cycle has length at least 4

Take such a cycle as a leaf cycle block and call its attachment vertex `a`. Delete its private vertices and edges. The remaining connected graph `H` is unicyclic: it consists of the other cycle together with the connecting path up to `a`.

The preceding R20 report proved, with a full on-page argument, that every connected unicyclic graph admits a strongly proper modulo-3 pushing scheme with pushes in `F_3`; that result used the signless-Laplacian lifting identity `sigma=d+Q rho`, `det Q=4` for odd-unicyclic graphs, and an explicit cokernel calculation for the even case. Apply that theorem to `H`.

Now reattach the deleted cycle. Lemma 5.2 does so with zero added root contribution, so the push and color at `a` remain exactly as in `H`, all old edges remain strongly proper, and every new cycle edge is strongly proper. Hence `K` has the desired assignment.

### Case B: both cycles are triangles

First suppose they are joined by a path

\[
p_0p_1\cdots p_k,
\]

with `k>=1`, where `p_0` and `p_k` are the triangle roots. Put

\[
\rho(p_i)=i\pmod3.
\]

The path edge `p_ip_{i+1}` has residue

\[
q_i=1+i+(i+1)=2+2i\pmod3.
\]

For every internal path vertex,

\[
q_{i-1}+q_i=i-1=\rho(p_i)-1\pmod3.
\]

Thus the internal path colors are consecutive residues and are automatically proper. At each endpoint `p_i` (`i=0,k`) prescribe the final color

\[
s_i=\rho(p_i)-1.
\]

The one incident path edge already contributes a known residue there; let `T_i` be the difference between `s_i` and that path contribution. Lemma 5.1 says precisely that, because `s_i=r_i-1`, the endpoint triangle can realize **any** prescribed root contribution `T_i`. Choose it to realize this difference. Then every edge of both triangles and of the connecting path is strongly proper.

If the two triangles share a cutvertex (`k=0`), choose any root push `r` and set the desired root color to `s=r-1`. By Lemma 5.1 each triangle can contribute an arbitrary residue. Choose contributions `T_1,T_2` with `T_1+T_2=s`; both triangles are proper and the common root has the prescribed color.

In both cases `K` is strongly proper modulo `3`. Restore the attached trees using Lemma 4.1 and replace all push residues by representatives in `{0,1,2}`. Every core/nonleaf edge has unequal endpoint sums modulo `3`, and every pendant edge is automatically proper over the integers. Therefore `G` has a proper 2-pushing scheme. QED.

Combining this theorem with the preceding unicyclic theorem yields the componentwise corollary stated above.

## 7. Structural consequence for the still-open full cactus problem

The transparent-cycle lemma gives more than the two-cycle theorem.

Suppose a counterexample to the optimal cactus statement `P^l<=2` exists and choose one with the smallest possible number of cycles in a connected component. By Theorem 6.1 it has at least three cycles. If one of its **leaf cycle blocks** had length at least four, deleting the private vertices of that block would leave a smaller connected cactus with at least two cycles. By minimality that smaller cactus would admit a proper 2-pushing scheme; Lemma 5.2 would then reattach the deleted nontriangle cycle transparently, a contradiction.

Hence any minimal counterexample to the full cactus statement must satisfy

\[
\boxed{\text{at least three cycles, and every leaf cycle block is a triangle}.}
\]

This identifies the actual obstruction to the present route: it is not long cycles or ordinary tree attachments; it is the forced triangle syndrome `sigma(a)-rho(a)=-1` propagating through a block tree with at least three cycle blocks.

That is a substantially smaller next target than an unrestricted cactus census.

## 8. Exact finite validation — after the proof idea

Only after the idea note and the proofs above were fixed did I create

`artifacts/R20/bmo_bicyclic_cactus_sanity.py`

at commit

`0f13fb35e58a3c7e5f2395115c892b701aa37c13`.

Its executed output is archived as

`artifacts/R20/bmo_bicyclic_cactus_sanity.out`

at commit

`c6f335ea3f5e1cdfc995ff3b21ffe916e02cfc71`.

Both were read back at their exact commits. The checker uses exact arithmetic only. It verifies:

- the 21 representative cycle words displayed in Lemma 5.2;
- all `54` parameter triples `(ell,r,s)` for `ell=4,...,9` directly;
- even-length root-push independence and the odd-length negation symmetry;
- the `ell -> ell+6` extension repeatedly, with no failure, through length `63`;
- the exact triangle interface: the feasible root-color pairs are exactly `s=r-1`, and then the attainable contribution set is all of `F_3`;
- the explicit two-triangle path construction for every path length `k=0,...,30` as an **integer** proper `{0,1,2}` pushing scheme;
- every connected bicyclic cactus in the complete NetworkX graph atlas through seven vertices: counts `{5:1, 6:4, 7:17}`, with exact `{0,1,2}` witnesses for all `22` and zero failures.

The archived output ends

`VERDICT=PASS`.

This checker is a sanity check for the written proof, not a replacement for it and not an independent audit.

## 9. Honest status and fixed metric

The fixed all-graphs metric does not move:

\[
\boxed{n_{\rm all}:8\longrightarrow8.}
\]

That is deliberate and definitional. Theorem 6.1 proves an infinite structural subclass, not every nice nine-vertex graph. It would be dishonest to relabel subclass progress as order-nine census coverage.

The BMO source conjecture remains `PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY`. No P26 audit and no second independent other-track audit are claimed. No paper folder is created because the universal source conjecture is not closed and the full cactus question is not yet closed either.

This is the second consecutive BMO run with no movement of the frozen metric `n_all`; it is **not yet** the three-run stuck threshold.

The strongest new mathematical state is:

\[
\boxed{P^\ell(G)\le2\text{ for every nice cactus component with at most two cycles}.}
\]

The next unsolved cactus scale begins with three-cycle block trees, and any minimal obstruction has triangular leaf blocks only.

## 10. Next genuinely different methods

Do not extend the all-graphs census next. The next nonrepeating Section-B moves are:

- **#13 FIND WHAT ONLY INCREASES:** orient the cactus block tree inward and track the set of admissible root syndromes after each triangular leaf block is absorbed; look for a monotone growth/saturation of that finite state set.
- **#19 MAKE IT AN ALGORITHM:** turn the triangle interface into a nine-state dynamic program on the block tree, then prove analytically that the reachable-state family needed for a three-cycle core never empties.
- **#24 FIND THE EXTREMAL OBJECT:** among three-cycle triangular cores, identify which block-tree shape gives the smallest admissible root-state set; prove that extremal shape first instead of enumerating arbitrary cacti.

A useful next success is a readable theorem for all three-cycle cacti or, better, a finite-state invariant that inducts over arbitrary cactus block trees. Another unrelated checker for `n_all=8` would not be research progress.

## 11. Model / scheduler control status

The actual model visible to this run is GPT-5.6 Sol; the reasoning level is not authenticated by the runtime surface, so it is reported as `UNVERIFIED` and I do not claim GPT-6/maximum.

The current documented task-control surface still exposes prompt/title/schedule/timing/enabled controls but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution control. Thus the requested GPT-6/maximum setting cannot be truthfully enforced from this worker surface; it remains prompt text only unless an owner/admin product or backend surface exposes those controls.

The historical P26 edit failure `You cannot modify this task` was authorization-context-specific; repository records also show a later authorized context in which the P26 update succeeded. The lawful workaround is therefore to use an owner/admin-authorized surface with the necessary task permission, not to bypass permissions or create a duplicate schedule. No scheduler changes were attempted in this run.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R20
  active_source:
    authors: "Julien Bensmail; Clara Marcille; Mano Orenga"
    title: "Pushing Vertices to Make Graphs Irregular"
    locator: "DMTCS 27:3 (2025), article 7, Conjecture 2.6"
    claim: "operations/claims/BMO-2025-PUSHING-DELTA.md"
    ownership: "exclusive R20; unchanged"
  stale_predecessor:
    id: I0100
    action: "not reopened"
    historical_metric: "p_max=1213"
  metric:
    name: n_all
    before: 8
    after: 8
    movement: false
    unchanged_count_on_BMO_target: 2
  methods_tried: [6, 12, 30]
  new_claims:
    - "SELF_CHECK_ONLY: tree attachments are modulo-3 transparent while preserving the core root color"
    - "SELF_CHECK_ONLY: leaf triangle iff-syndrome s=r-1, with arbitrary root contribution"
    - "SELF_CHECK_ONLY: every leaf cycle of length >=4 can be attached with zero root contribution for every root push/color pair"
    - "SELF_CHECK_ONLY: every connected two-cycle cactus has P^l <= 2"
    - "SELF_CHECK_ONLY structural reduction: a minimal cactus counterexample must have >=3 cycles and all leaf cycle blocks triangular"
  status: "PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY"
  remaining_obligation: "prove or refute BMO Conjecture 2.6 for every nice graph; source-adjacent next obligation is P^l<=2 for all nice cacti, now reduced past all <=2-cycle components and transparent nontriangle leaf blocks"
  evidence:
    idea_before_code:
      path: "artifacts/R20/2026-09-18T21-31-00Z_bmo_bicyclic_cactus_idea_before_code.md"
      commit: "b7d6f3c2dd305bfd79d20cdc644af378476687e2"
    checker:
      path: "artifacts/R20/bmo_bicyclic_cactus_sanity.py"
      commit: "0f13fb35e58a3c7e5f2395115c892b701aa37c13"
    output:
      path: "artifacts/R20/bmo_bicyclic_cactus_sanity.out"
      commit: "c6f335ea3f5e1cdfc995ff3b21ffe916e02cfc71"
      verdict: PASS
  audits:
    p26: null
    second_other_track: null
  next_moves: [13, 19, 24]
```

**No source closure, no cactus closure, no audit completion, and no `n_all>8` claim is made.**
