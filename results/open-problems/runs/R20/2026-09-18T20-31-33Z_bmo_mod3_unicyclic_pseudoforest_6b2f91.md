Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `n_all: 8 -> 8`; status `PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY`; methods #11 DUALIZE, #18 SAY IT IN ANOTHER LANGUAGE, #25 COUNT THE SAME THING TWICE.**

# R20 — modulo-3 lifting and an optimal pseudoforest theorem for BMO Conjecture 2.6

## 0. Continuity and ownership

I did **not** reopen the stale scheduler-title target Bandeira / Randomstrasse Conjecture 26 / I0100. Its finite localized-theta frontier remains historical and frozen at `p_max=1213`; finite prime certificates never proved the asymptotic source conjecture. I also did not return to the handed-off KNSV successor.

The current canonical R20 claim is

`operations/claims/BMO-2025-PUSHING-DELTA.md`,

owned exclusively by R20 and marked `CLAIMED / READY / CLOSABLE OUTSIDE`. The target is Julien Bensmail, Clara Marcille and Mano Orenga, *Pushing Vertices to Make Graphs Irregular*, DMTCS 27:3 (2025), Conjecture 2.6:

\[
P^\ell(G)\le \Delta(G)\qquad\text{for every nice finite simple graph }G.
\]

The fixed metric remains

\[
n_{\rm all}=\max\{n:\text{every nice simple graph of order at most }n\text{ is exactly certified}\},
\]

whose newest R20 value is `8` from the complete exact order-eight census in

`runs/R20/2026-09-18T19-01-21Z_bmo_pushing_n8_admission_91e4c7.md`.

Before new mathematics I reread the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the canonical BMO claim, the newest R20 BMO report, and current neighboring ownership/admission reports. No shared root and no other track's file is edited in this run.

## 1. Current-source and later-literature check — 18 September 2026

Original primary source:

- Bensmail--Marcille--Orenga, DMTCS 27:3 (2025), article 7, DOI `10.46298/dmtcs.14963`.
- Current source page: `https://dmtcs.episciences.org/16418`.
- Conjecture 2.6 states exactly `P^l(G) <= Delta(G)` for every nice graph.

The paper's conclusion is particularly relevant to this run. The authors single out **cacti**, say they tried modulo methods to prove the optimal bound `P^l(G)<=2`, report that their functional approach relied so heavily on exhaustive computer checks that they did not provide a formal proof, and explicitly ask for a readable, more direct proof of the optimal cactus result.

Current follow-up recovered:

- Dieter Rautenbach, Laurin Schwartze, Florian Werner, *Coloring by Pushing Vertices*, Ars Combinatoria 167 (2026), pp. 147--157, DOI `10.61091/ars167-10`, published online **17 June 2026**.
- It still presents the general `Delta` statement as the Bensmail--Marcille--Orenga conjecture and proves it for **cubic graphs** and **regular bipartite graphs**.

Dated bounded searches using the exact conjecture wording, title, authors, `proper pushing scheme`, `cactus`, `unicyclic`, and `pseudoforest` found the original source, the 2026 follow-up and mirrors/indexing pages, but no later source-matching general proof, counterexample, or written unicyclic/pseudoforest theorem. This is bounded negative evidence only, not a novelty certificate. Before publication or closure, repeat the current-primary/citing/later-author search.

A separate prior-art search for the linear-algebra ingredient found Monfared--Mallik, *An Analog of Matrix Tree Theorem for Signless Laplacians*, Linear Algebra Appl. 560 (2019), 43--55: the fact `det Q=4` for an odd-unicyclic graph is classical. **No novelty is claimed for that determinant fact.** The proof below rederives the needed special case directly.

## 2. Idea before code

Before writing any new checker I committed

`artifacts/R20/2026-09-18T20-28-20Z_pushing_mod3_unicyclic_idea_before_code.md`

at commit

`c2b643c5e68e0f28c71279773c1537538cd76819`.

The research route was therefore fixed before validation code.

## 3. #18 SAY IT IN ANOTHER LANGUAGE: pushing is a signless-Laplacian lifting problem

Let `A` be the adjacency matrix, `D` the diagonal degree matrix, `Q=D+A` the signless Laplacian, and `d` the degree vector. For a pushing vector `rho`, the defining formula is exactly

\[
\boxed{\sigma=d+Q\rho.}
\]

Reduce modulo `3`. The following elementary lifting lemma is the key language change.

### Lemma 3.1 (modulo-3 lifting)

Let `G` be any finite simple graph. If there is a proper vertex coloring

\[
c:V(G)\to\mathbb F_3
\]

such that

\[
c-d\in \operatorname{im}_{\mathbb F_3} Q,
\]

then `G` has a proper pushing scheme with every push count in `{0,1,2}`. In particular,

\[
P^\ell(G)\le2.
\]

#### Proof

Choose `rho in F_3^V` with `Q rho=c-d`, and replace each coordinate by its representative in `{0,1,2}`. For the resulting integer pushing vector,

\[
\sigma=d+Q\rho\equiv c\pmod3.
\]

If adjacent vertices had equal integer sums, their residues modulo `3` would agree, contradicting properness of `c`. Thus the pushing scheme is proper. QED.

A useful immediate corollary is: if `Q` is invertible over `F_3` and `G` is 3-colorable, then `P^l(G)<=2`. More generally, the obstruction is the **cokernel of `Q mod 3`**, not the integer search box.

## 4. #11 DUALIZE: the cokernel equations are explicit on a unicyclic graph

The principal theorem of this run is the following restricted but complete source-valid result.

### Theorem 4.1

If `G` is a connected unicyclic graph, then

\[
\boxed{P^\ell(G)\le2.}
\]

The constant `2` is best possible for the class because odd cycles satisfy `P^l(C_{2k+1})=2` in Bensmail--Marcille--Orenga Theorem 3.4.

This theorem is **SELF_CHECK_ONLY** pending independent audit. It is not a proof of Conjecture 2.6.

### Proof

Let `C=v_0v_1...v_{ell-1}v_0` be the unique cycle. Work throughout over `F_3`.

#### Case 1: `ell` is odd

A pendant-vertex elimination preserves `det Q` for a unicyclic graph. Indeed, if `x` is a leaf adjacent to `y`, order `x` first. Then

\[
Q(G)=\begin{pmatrix}1&e_y^T\\ e_y&Q(G-x)+E_{yy}\end{pmatrix},
\]

so the Schur complement of the leading `1` is exactly `Q(G-x)`. Repeating strips every tree attached to the cycle and gives

\[
\det Q(G)=\det Q(C_\ell).
\]

For a cycle, write `Q(C_ell)=BB^T`, where `B` is the unsigned vertex-edge incidence matrix. When `ell` is odd, the two permutation terms in `det B` have the same sign, so `|det B|=2`; hence

\[
\det Q(C_\ell)=4.
\]

Thus `det Q(G)=4`, which is nonzero modulo `3`. Therefore `Q` is invertible over `F_3`.

A unicyclic graph is 3-colorable. Choose any proper `c:V->F_3`. Since `Q` is invertible, solve

\[
Q\rho=c-d.
\]

Lemma 3.1 gives a proper pushing scheme with `rho(v) in {0,1,2}`.

#### Case 2: `ell` is even

Now `G` is bipartite. Let `A cup B` be its bipartition, choose `v_0 in A`, put

\[
s_v=\begin{cases}1,&v\in A,\\-1,&v\in B,\end{cases}
\qquad S=\operatorname{diag}(s_v),
\]

and let `L=D-A` be the ordinary Laplacian. Bipartiteness gives

\[
\boxed{Q=SLS.}
\]

Consequently `Q rho=c-d` is equivalent, after setting `x=S rho`, to

\[
Lx=S(c-d).
\]

Because `L` is symmetric,

\[
\operatorname{im}L=(\ker L)^\perp.
\]

So it remains to choose a proper 3-coloring `c` for which `S(c-d)` is orthogonal to `ker L`.

Strip all pendant vertices from an equation `Lz=0`. At a leaf `w` with parent `u`, the leaf equation says `z_w=z_u`, and after substitution the restriction solves the Laplacian equation on the smaller graph. Therefore every kernel vector is constant on each tree attached to the cycle. On the cycle the equations are

\[
2z_i-z_{i-1}-z_{i+1}=0,
\]

so the first differences are constant and

\[
z_i=a+bi.
\]

Periodicity imposes `ell b=0` in `F_3`. Hence:

- if `3` does not divide `ell`, `ker L=span{1}`;
- if `3` divides `ell`, then `ell` is a multiple of `6` and
  \[
  \ker L=\operatorname{span}\{\mathbf1,h\},
  \]
  where `h(v)=i mod 3` on the entire tree attached to `v_i`.

For either basis vector `g in {1,h}` that exists, we have

\[
\langle g,Sd\rangle=0.
\]

For `g=1`, this is immediate by summing `s_u+s_v=0` edge by edge. For `g=h`, every attached-tree edge contributes zero because `h` is constant there, while the cycle-edge contributions alternate and sum to zero around the even cycle.

Start from the bipartite coloring

\[
c_0(v)=0\ (v\in A),\qquad c_0(v)=1\ (v\in B).
\]

Let `T` be an independent set, and recolor exactly the vertices of `T` to color `2`; call the resulting coloring `c_T`. Since `T` is independent, `c_T` is still proper. For every `g in ker L` of the displayed basis type,

\[
\langle g,S(c_T-d)\rangle
=-\sum_{v\in B}g(v)+2\sum_{v\in T}g(v).
\]

Thus it is enough to choose `T` so that

\[
\boxed{\sum_{v\in T}g(v)=-\sum_{v\in B}g(v)\quad\text{in }\mathbb F_3}
\]

for all basis vectors `g`.

##### Subcase 2a: `3` does not divide `ell`

Only `g=1` occurs. We need

\[
|T|\equiv-|B|\pmod3.
\]

The cycle side `A cap V(C)` contains at least two vertices because `ell>=4`. It is independent. Choosing `0`, `1`, or `2` of those vertices realizes every residue modulo `3`.

##### Subcase 2b: `3` divides `ell` and `ell>=12`

We must realize the pair

\[
\left(|T|,\sum_{v\in T}h(v)\right)
=-\left(|B|,\sum_{v\in B}h(v)\right)
\in\mathbb F_3^2.
\]

Among the independent cycle side `A cap V(C)` there are at least two vertices of each `h`-value `0,1,2`. Their subset sums realize every element of `F_3^2`:

- `(0,0)` is the empty set;
- `(1,b)` is one vertex of `h`-value `b`;
- `(2,0)` is two vertices of value `0`, while `(2,1)` and `(2,2)` are one value-`0` vertex plus one value-`1` or value-`2` vertex;
- `(0,1)` is three vertices with values `0,0,1`, and `(0,2)` uses `0,0,2`.

Hence the required `T` exists.

##### Subcase 2c: `ell=6`

If `G=C_6`, then `|B|=3` and the three `h`-values on `B` sum to `0`, so the target pair is `(0,0)` and `T=emptyset` works.

Otherwise some cycle vertex has a neighbor `x` off the cycle. Rotate the indexing and, if necessary, swap the bipartition sides so that this root is `v_0 in A`. Then `h(x)=0`. The following nine independent sets realize all of `F_3^2`, where the recorded pair is `( |T|, sum_T h )` modulo `3`:

\[
\begin{array}{c|c}
(0,0)&\varnothing\\
(1,0)&\{v_0\}\\
(1,1)&\{v_1\}\\
(1,2)&\{v_2\}\\
(2,0)&\{v_0,v_3\}\\
(2,1)&\{v_1,v_3\}\\
(2,2)&\{v_0,v_2\}\\
(0,1)&\{v_1,v_3,x\}\\
(0,2)&\{v_1,v_4,x\}.
\end{array}
\]

So again the required target pair can be reached.

In all even-cycle subcases, `S(c_T-d)` is orthogonal to `ker L`; therefore it belongs to `im L`. Choose `x` with

\[
Lx=S(c_T-d),
\]

set `rho=Sx` in `F_3`, and take representatives in `{0,1,2}`. Then

\[
d+Q\rho\equiv c_T\pmod3,
\]

which is proper. Lemma 3.1 finishes the proof. QED.

## 5. #25 COUNT THE SAME THING TWICE: the determinant and the finite obstruction both collapse

The proof uses two exact double-count / dual descriptions rather than a larger graph census:

1. `Q=BB^T` turns the odd-cycle signless determinant into the square of an incidence determinant. The two cycle permutation terms give `|det B|=2` for odd length, hence `det Q=4`.
2. In the even case, solving `Lx=r` is dual to checking only the kernel moments `r perp ker L`; the entire potential obstruction is reduced to one or two residue sums, which are then realized by independent subsets of the cycle side.

This is the mechanism that was missing from the order-eight census: it proves an infinite class without extending `n_all` by brute force.

## 6. Corollary: every nice pseudoforest has pushing number at most 2

A pseudoforest has at most one cycle in each connected component. Bensmail--Marcille--Orenga Theorem 3.6 already gives `P^l<=1` for every nice tree. Theorem 4.1 gives `P^l<=2` for every unicyclic component. Components are independent for pushing constraints. Therefore:

### Corollary 6.1

If `G` is a nice pseudoforest, then

\[
\boxed{P^\ell(G)\le2.}
\]

The bound is optimal because odd cycles are pseudoforests and need two pushes in the source's Theorem 3.4.

This supplies a completely written modulo proof for the full pseudoforest subclass of the cactus direction raised by the source. It does **not** settle arbitrary cacti with multiple cycles in one component.

## 7. Exact finite validation

Only after the idea and proof route were fixed did I add

`artifacts/R20/pushing_unicyclic_mod3_sanity.py`

at commit

`c5a6c26d91792d0b885592a8274fd749f8cdcf0c`.

It is explicitly a finite sanity checker, not the proof. It checks exactly:

- the nine `C6 + one off-cycle neighbor` independent-set residues cover all of `F_3^2`;
- every connected unicyclic graph in NetworkX's complete graph atlas through order seven has an exact pushing vector in `{0,1,2}`;
- every odd-cycle atlas instance has exact integer `det Q=4`;
- every even-cycle atlas instance has the kernel nullity predicted by the proof.

The executed output is archived as

`artifacts/R20/pushing_unicyclic_mod3_sanity.out`

at commit

`1158d6825855b1c05fb2762abfefffaa9b523050`:

```text
c6_plus_leaf_independent_set_residues= [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
c6_plus_leaf_covers_all_F3_squared=True
connected_unicyclic_atlas_counts= {3: 1, 4: 2, 5: 5, 6: 13, 7: 33}
connected_unicyclic_atlas_total= 54
exact_012_witnesses_found= 54
odd_cycle_detQ_not_4= []
even_cycle_kernel_prediction_failures= []
proper_012_failures= []
VERDICT=PASS
```

No floating point, SDP, heuristic acceptance, or numerical tolerance is involved in these finite checks.

## 8. Honest status, metric and what remains

The fixed metric does **not** move:

\[
\boxed{n_{\rm all}:8\longrightarrow8.}
\]

The reason is definitional: `n_all` concerns **all** nice graphs by order, while Theorem 4.1 proves an infinite structural subclass. It would be dishonest to count the subclass theorem as order-nine coverage.

The source-level conjecture remains PARTIAL. No P26 audit and no second independent other-track audit are claimed. The theorem and corollary above are `SELF_CHECK_ONLY` until another worker checks the proof independently. No paper folder is created because the universal source conjecture is not closed.

The strongest remaining source-adjacent obligation suggested by this route is the authors' cactus question:

\[
\boxed{P^\ell(G)\le2\quad\text{for every nice cactus }G.}
\]

The present proof settles exactly the case with at most one cycle per connected component. The obstacle to gluing multiple cycle blocks is now concrete: one must control the `Q mod 3` cokernel syndrome across articulation vertices rather than solve each cycle independently.

## 9. Next genuinely different methods

Do not extend the all-graphs census next. The next nonrepeating Section-B moves are:

- **#6 DEFORM TO A POINT YOU CAN SOLVE:** add cactus cycle blocks one at a time to the now-solved pseudoforest case and identify the first syndrome that fails to glue;
- **#12 FIND WHAT IS CONSERVED:** derive the exact block-tree conservation law for `ker(Q mod 3)` / the syndrome `z^T(c-d)` across articulation vertices;
- **#30 ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME:** first solve two-cycle cacti completely, split by the two cycle lengths modulo `6`, before attempting arbitrary block trees.

A genuine next success is either a readable two-cycle gluing lemma that inducts over cactus blocks, or an exact cactus counterexample to modulo-3 properness. A larger unrelated finite census is not the priority.

## 10. Structured ledger delta

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
    unchanged_count_on_BMO_target: 1
  methods_tried: [11, 18, 25]
  new_claims:
    - "SELF_CHECK_ONLY: every connected unicyclic graph has P^l <= 2"
    - "SELF_CHECK_ONLY: every nice pseudoforest has P^l <= 2"
    - "modulo-3 lifting lemma: c-d in im(Q mod 3) for a proper c implies a 2-pushing scheme"
  status: "PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY"
  remaining_obligation: "prove or refute BMO Conjecture 2.6 for all nice finite simple graphs; nearest source-raised subclass is optimal P^l<=2 for all cacti"
  exact_evidence:
    idea_commit: c2b643c5e68e0f28c71279773c1537538cd76819
    checker_commit: c5a6c26d91792d0b885592a8274fd749f8cdcf0c
    output_commit: 1158d6825855b1c05fb2762abfefffaa9b523050
    checker_verdict: PASS
  audits:
    self_check: true
    p26: null
    second_other_track: null
  next_moves: [6, 12, 30]
```

## 11. Scheduler/model-control truth

The requested `GPT-6 / maximum` setting is still **not enforceable from the exposed worker/scheduler surface**. The repository's operative implementation record says the scheduler exposes title/prompt/schedule/timing/enabled controls but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed one-hour runtime setting. Thus the actual reasoning level remains `UNVERIFIED`, and I do not claim GPT-6.

The historical P26 ID `6aa7b43682948191b697d72fec69d539` returned `You cannot modify this task` in one authorization context; repository records also distinguish later authorized-context successes from that denial. The lawful workaround is an owner/admin-authorized product/backend surface that actually exposes the needed control. No permission bypass, duplicate task, scheduler change, email, Drive action, or public posting was attempted here.

**NO I0100 REOPENING. NO BMO UNIVERSAL CLOSURE CLAIM. FIXED METRIC STAYS `n_all=8`. NEW MATHEMATICAL RESULT: SELF-CHECKED OPTIMAL `P^l<=2` FOR CONNECTED UNICYCLIC GRAPHS, HENCE FOR NICE PSEUDOFORESTS.**
