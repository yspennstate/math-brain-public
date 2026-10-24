Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `n_all: 9 -> 9`; status `PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / SELF_CHECK_ONLY`; methods #14 FIND THE GROUP ACTING, #26 HUNT THE SPORADIC CASE, #8 DISCRETIZE.**

# R20 — complete branch-cycle theorem: short-theta pairs are absorbed by four-port correspondence slack

Repository / branch: `yspennstate/math-open-problems` / `master`.

## 0. Continuity, ownership, and stale scheduler title

I continued from the newest complete R20 report

`runs/R20/2026-09-19T04-51-34Z_bmo_stuck_dp_correspondence_61a9e4.md`

rather than restarting from the native scheduler title. The current exclusive R20 claim is

`operations/claims/BMO-2025-PUSHING-DELTA.md`,

marked `CLAIMED / READY / CLOSABLE OUTSIDE`.

The older `operations/claims/I0100.md` is still present, but the later immutable R20 history records I0100 (Bandeira, Randomstrasse Conjecture 26, Paley one-localization) as a terminal six-unchanged-run handoff for this worker. Its exact-certified frontier is frozen at `p_max=1213`, with retained prime set

`{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`.

The source asymptotic was not closed there. Under `NEW-METHODS-2026-09-16`, a closable target rotates after six unchanged runs; this run therefore does not reopen I0100 or modify its frozen metric. P04/I0101 two-localization, R12/I0102 degree-four SOS, and C28's Paley-ETF line remain distinct.

At run start I reread/recovered `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the BMO and I0100 claim records, the terminal I0100 handoff, the newest R20 report, and the prior branch-cycle theorem/checker record. No shared root or peer-track file is edited in this run.

## 1. Fresh source and literature check — 19 September 2026

Primary source: Julien Bensmail, Clara Marcille, Mano Orenga, *Pushing Vertices to Make Graphs Irregular*, DMTCS 27:3 (2025), article 7, DOI `10.46298/dmtcs.14963`.

The current primary PDF still states Conjecture 2.6 exactly as

\[
P^\ell(G)\le \Delta(G)
\]

for every nice graph. Its conclusion explicitly proposes maximum degree three as a first gap, and separately asks about 2-degenerate graphs and a readable optimal cactus proof.

Current later work located again this run: Dieter Rautenbach, Laurin Schwartze, Florian Werner, *Coloring by Pushing Vertices*, *Ars Combinatoria* 167 (2026), 147--157, DOI `10.61091/ars167-10`, published online 17 June 2026. It still presents the general `Delta` bound as conjectural and proves it for cubic graphs and regular bipartite graphs.

Fresh dated searches included the exact source title/conjecture phrase, `pushing vertices subcubic`, `proper pushing scheme 2-degenerate`, `proper pushing scheme correspondence coloring`, and the 2026 follow-up. I found the source, the published follow-up, mirrors/indexes, and the established DP-coloring literature, but no later source-matching general proof and no located theorem matching the subclass proved below. This is bounded negative evidence only, not a novelty certificate.

Relevant established correspondence-coloring references remain Anton Bernshteyn, Alexandr Kostochka, Sergei Pron, *On DP-coloring of graphs and multigraphs*, Siberian Math. J. 58 (2017), 28--36, and Seog-Jin Kim, Kenta Ozeki, *A note on a Brooks' type theorem for DP-coloring*, J. Graph Theory 91 (2019), 148--161. The proof below ultimately needs only the elementary greedy-with-slack lemma stated in Section 4, not the full classification theorem.

## 2. Prior exact ingredients retained

For a pushing scheme `rho`,

\[
\sigma_\rho(u)=d_G(u)(1+\rho(u))+\sum_{v\sim u}\rho(v).
\]

Let `C` be the 2-core of a connected nice subcubic graph and

\[
B=\{v\in V(C):d_C(v)=3\}.
\]

The preceding report proved the target when the induced branch graph `D=C[B]` is 2-regular **provided** no one-internal-vertex branch chain joins two vertices already adjacent in `D`. Its exact chain-transfer lemma is retained here.

For a branch-to-branch chain

\[
b_0,x_1,\ldots,x_k,b_1
\]

with boundary branch pushes `alpha,beta in {2,3}`, let `a=rho(x_1)` and `b=rho(x_k)` be the endpoint ports. Then:

\[
\boxed{
\begin{array}{ll}
k=1:& a=b,\\
k=2:& a-b\ne \beta-\alpha,\\
k\ge3:& \text{every }(a,b)\in\{0,1,2,3\}^2\text{ is realizable.}
\end{array}}
\tag{2.1}
\]

The same report proved a uniform branch--chain integer-sum gap of at least 3 for branch pushes in `{2,3}` and internal pushes in `{0,1,2,3}`. It also gave an explicit one-defect repair of every `K5` quotient lift; the existing exact checker enumerated all `3^5=243` local pairings and returned zero failures. Those finite checks are reused rather than manufactured again.

The only missing case was a **short-theta pair**: a matching chain `u-x-v` with one internal degree-two vertex occurring in parallel with the direct branch edge `uv in E(D)`.

## 3. Binary defect algebra

Assume throughout this report that `B` is nonempty and `D=C[B]` is 2-regular. Every branch vertex has exactly one remaining core incidence, so the maximal degree-two branch chains form a perfect matching `M` on `B` after suppression.

Write

\[
\rho(b)=3-\varepsilon_b,\qquad \varepsilon_b\in\{0,1\}.
\]

For every short-theta matching pair `uv`, choose exactly one endpoint to have defect one; for definiteness orient the pair and put

\[
\varepsilon_u=1,\qquad \varepsilon_v=0.
\tag{3.1}
\]

All vertices not belonging to a short-theta pair initially receive defect zero. These choices are compatible because the matching pairs are vertex-disjoint.

Let `p_b` denote the port at branch `b`. If `b^-` and `b^+` are the two direct neighbors of `b` in `D`, then

\[
\boxed{
\sigma(b)=18+p_b-3\varepsilon_b-\varepsilon_{b^-}-\varepsilon_{b^+}.
}
\tag{3.2}
\]

For a short-theta pair `u,v`, (2.1) forces the common port `p_u=p_v=p`. Let `a` and `b` be the other direct neighbors of `u` and `v`, respectively. Subtracting (3.2) gives

\[
\boxed{
\sigma(u)-\sigma(v)
=2(\varepsilon_v-\varepsilon_u)+(\varepsilon_b-\varepsilon_a).
}
\tag{3.3}
\]

Under (3.1), the right side belongs to `{-3,-2,-1}`. Hence the direct edge `uv` is automatically proper, independently of the common port and independently of all outer defect choices. This removes the quotient loop that blocked the preceding proof.

No other direct edge is declared automatically safe; those are handled by the finite four-port cover below.

## 4. Four-port correspondence cover and the elementary slack lemma

Contract every matching chain with `k=1` to one quotient vertex. Its two branch endpoints share one port by (2.1). Branches whose matching chain has `k>=2` remain singleton quotient vertices.

Give every quotient vertex the four-port list

\[
L(q)=\{0,1,2,3\}.
\]

For a branch `w`, define the exact offset

\[
c_w=-3\varepsilon_w-\sum_{z\in N_D(w)}\varepsilon_z.
\tag{4.1}
\]

For every direct branch edge `xy` whose endpoints are not the same contracted short-theta vertex, properness is exactly

\[
p_{q(x)}+c_x\ne p_{q(y)}+c_y.
\tag{4.2}
\]

For fixed `xy`, the forbidden pairs in `L(q(x)) x L(q(y))` form a **partial matching**, because (4.2) fails only when one port is a fixed integer translate of the other. Complete that partial matching arbitrarily to a perfect matching.

For every matching chain with `k=2`, (2.1) says

\[
p_u-p_v\ne \varepsilon_u-\varepsilon_v,
\tag{4.3}
\]

which is again the complement of a partial matching; complete it to a perfect matching. Chains with `k>=3` impose no endpoint-port constraint.

Let `H` be the resulting loopless quotient multigraph, with one constraint edge for each unresolved direct edge and each `k=2` matching-chain constraint. Parallel edges are retained. The completed forbidden matchings make `(H,L)` a four-fold correspondence cover. A DP-coloring of this stronger completed cover is sufficient for the original pushing constraints.

The only DP fact needed is elementary.

> **Lemma 4.1 (greedy correspondence slack).** Let `H` be a connected loopless multigraph with a four-element list at every vertex and one matching constraint for each edge. If `Delta(H)<=4` and some vertex has degree at most 3, then every such cover is colorable.

**Proof.** Root a spanning tree at a vertex `r` of degree at most 3. Order the other vertices from leaves toward the root so that each nonroot vertex still has an uncolored parent when it is colored. At that moment at most `d_H(v)-1<=3` incident edges lead to already colored vertices. Each such edge forbids at most one of the four colors, so an available color remains. Color `r` last; at most `d_H(r)<=3` colors are forbidden. Parallel edges cause no problem because the count is by incident edges. QED.

This lemma is the useful part of the DP viewpoint: **one strict degree slack vertex dispatches the whole connected component, for arbitrary edge correspondences.**

## 5. Degree structure of the quotient

The quotient degrees are exact.

1. A singleton branch quotient has its two direct `D` incidences and, only when its matching chain has `k=2`, one extra matching constraint. Hence its degree is at most 3.

2. A contracted short-theta `k=1` pair has one internal direct edge already certified by (3.3). Removing that internal edge leaves exactly the two outer direct incidences, hence quotient degree 2.

3. A contracted non-short-theta `k=1` pair has four external direct incidences and no matching constraint, hence quotient degree 4.

Therefore

\[
\Delta(H)\le4.
\tag{5.1}
\]

Every connected component containing either a singleton quotient or a short-theta quotient has a vertex of degree at most 3, so Lemma 4.1 colors the entire component.

It remains only to treat components all of whose quotient vertices have degree four.

## 6. Degree-tight components collapse back to ordinary Brooks coloring

Suppose a connected component `K` of `H` has degree four at every vertex. By Section 5, every vertex of `K` is a contracted **non-short-theta** `k=1` pair. Hence:

- no singleton branch occurs in `K`;
- no `k=2` matching constraint occurs in `K`;
- no short-theta pair occurs in `K`;
- every branch in `K` still has `epsilon=0`.

Thus every constraint in `K` comes from an ordinary direct branch edge and (4.2) reduces simply to

\[
p_q\ne p_{q'}.
\tag{6.1}
\]

Suppress parallel copies and let `S` be the underlying simple graph. It has maximum degree at most four. If `S` is not `K5`, ordinary Brooks coloring (or greedy coloring when the maximum degree is at most three) gives a proper four-coloring, which solves all constraints in `K`.

If `S=K5`, then degree four in `H` implies there are no parallel copies: `H` itself is exactly `K5`. This is the sole degree-tight sporadic obstruction to the all-defect-zero ordinary coloring.

The preceding R20 report already proved that every such `K5` lift is repaired by one branch defect. For completeness, the mechanism is short. Pick quotient vertex `A={a_0,a_1}`, set `epsilon_{a_0}=1` and all other defects zero, and use common port `p_A=0`. Split the four quotient neighbors of `A` into `S={s_1,s_2}` meeting `a_0` and `T={t_1,t_2}` meeting `a_1`. Give the two `T` ports `2,3` and the two `S` ports `0,1`, choosing which `S` gets which value so that the unique `S--S` edge is noncolliding. This is always possible: if the `S--S` edge uses the same shifted/unshifted side at both ends, distinct ports work; if it uses different sides, exactly one of the two assignments of `0,1` can collide.

Then the effective direct-edge labels relative to the common baseline 18 are:

- at `a_0`: `-3`;
- at `a_1`: `0`;
- on the `a_0`-side of an `S` pair: `p_s-1`, and on its other side: `p_s`;
- on every `T` prebranch: `p_t`.

Hence `A--S`, `A--T`, `S--T`, and `T--T` edges are separated by disjoint numerical ranges, while `S--S` was separated by the chosen orientation of the `0,1` assignment. The `k=1` matching chains remain valid because they require only a common port. The prior exact checker verified all `3^5=243` possible local pairings and returned zero failures.

Thus every degree-tight component is solved as well.

## 7. New theorem

> **Theorem 7.1 (R20, SELF_CHECK_ONLY).** Let `G` be a connected nice graph with `Delta(G)<=3`, let `C` be its nonempty 2-core, and let
> \[
> B=\{v\in V(C):d_C(v)=3\}.
> \]
> Assume `B` is nonempty and the induced branch graph `D=C[B]` is 2-regular. Then `G` has a proper pushing scheme with every push in `{0,1,2,3}`. Consequently
> \[
> \boxed{P^\ell(G)\le3=\Delta(G).}
> \]

**Proof.** Choose the binary defects on all short-theta pairs as in Section 3. Their internal direct edges are proper by (3.3). Build the four-port quotient cover from all remaining direct edges and `k=2` matching-chain constraints. Components with a strict degree-slack vertex are colorable by Lemma 4.1. Every degree-tight component reduces to ordinary four-coloring; Brooks handles all but `K5`, and the explicit one-defect repair handles `K5`.

Use the resulting quotient colors as endpoint ports. Complete every `k>=3` matching chain by the exact transfer lemma (2.1); `k=1,2` chains already satisfy their endpoint conditions. Every internal chain edge is proper by construction, and every branch--chain edge is proper by the retained integer gap lemma.

Finally reattach the forest removed in taking the 2-core, one leaf at a time, using the previously proved leaf-extension lemma: when a leaf is attached to a currently nonisolated vertex of degree at most two, its push can be chosen in `{0,1,2,3}` so that all affected old edges remain proper and the new leaf edge is automatically proper. This reconstructs `G` without exceeding push three. QED.

This removes the sole hypothesis from the preceding branch-cycle theorem. The short-theta configuration is not a counterexample and is no longer an unresolved structural case.

## 8. Section-B moves and what happened

### #14 — FIND THE GROUP ACTING: success

The four port values form a translation coordinate: every direct-edge bad relation is `p_y=p_x+delta` on the part of the four-element interval where the translate remains inside. This gauge view shows that the shifted branch defects do not require recovering a common ordinary coloring. They produce partial correspondences, which can be completed edgewise.

### #26 — HUNT THE SPORADIC CASE: success

Once strict-slack quotient components are removed, the only degree-tight ordinary Brooks exception is `K5`. The prior one-defect construction repairs every lift of it. The feared cycle-multiple DP exceptions never arise as new obstacles because every genuinely shifted/short-theta component already has strict degree slack and is dispatched by Lemma 4.1 before any degree-DP classification is needed.

### #8 — DISCRETIZE: success

The entire short-theta obstruction reduces to four port values, one binary branch defect, and an edge-matching cover of a quotient of maximum degree four. No numerical SDP, floating point, or growing finite census enters the proof.

## 9. Validation discipline

I did **not** add a new checker just to create another receipt. The new step is a written global proof; its finite ingredients were already exactly checked in the preceding run:

- all endpoint-transfer cases through long chain lengths;
- the branch--chain gap;
- all `3^5=243` `K5` lifts under the one-defect repair;
- archived result `VERDICT=PASS` in `artifacts/R20/bmo_branch_cycle_brooks_exact.out`.

The present new ingredient, Lemma 4.1, is a direct greedy proof for arbitrary matchings and has no finite enumeration core. This report remains `SELF_CHECK_ONLY`: no independent audit is claimed.

## 10. Fixed metric, status, and next frontier

The fleet metric does **not** move:

\[
\boxed{n_{\rm all}:9\to9.}
\]

The theorem is infinite structural progress, but it does not certify every nice graph of order ten. This is unchanged run **5** after the earlier `8 -> 9` reset. The six-unchanged-run closable rotation rule therefore has not yet fired, but one further unchanged run will trigger it unless the fixed metric moves.

The sharp next subcubic frontier is now **mixed branch graph** structure: `D=C[B]` has maximum degree two but contains both degree-one and degree-two branch vertices, so some branches expose two complementary chain ports while others expose one. The natural next target is to unify the already solved `Delta(D)<=1` and `D` 2-regular cases.

Reserved next nonrepeating methods:

- **#1 CHANGE THE CATEGORY:** suppress the 2-core to its cubic kernel and treat direct/subdivided kernel edges as a transition system rather than a graph-with-paths description;
- **#15 BREAK THE SYMMETRY ON PURPOSE:** put binary defects only at path endpoints or short parallel routes and use them as slack sources;
- **#27 SWAP THE QUANTIFIERS:** instead of choosing a global branch pattern then solving ports, prove that for every admissible chain state there exists an endpoint-port choice maintaining a finite interface invariant.

## 11. Scheduler/model/authorization boundary

The currently exposed task-management schema still offers task identity/title, prompt, schedule or relative-start timing, timing mode, and enabled state. It exposes **no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution control**. Thus `GPT-6 / maximum` remains a prompt request only; this run is reported as `GPT-5.6 Sol / reasoning UNVERIFIED` and not otherwise.

The historical P26 `You cannot modify this task` event was authorization-context-specific. Repository records preserve a later context in which the P26 update succeeded. The legitimate workaround is an owner/admin-authorized product or backend context that exposes the relevant task controls; it is not a permission bypass or task clone. No scheduler or permission change is attempted here.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R20
  lane: CLOSABLE_OUTSIDE
  active_source: "Bensmail--Marcille--Orenga, DMTCS 27:3 (2025), Conjecture 2.6"
  ownership: "R20 exclusive; operations/claims/BMO-2025-PUSHING-DELTA.md"
  stale_predecessor:
    id: I0100
    status: TERMINAL_SIX_UNCHANGED_HANDOFF_NOT_REOPENED
    p_max_exact_primal_dual: 1213
  metric:
    name: n_all
    before: 9
    after: 9
    movement: false
    unchanged_count_after_reset: 5
  status: PARTIAL_CLAIMED_READY_CLOSABLE_OUTSIDE_SELF_CHECK_ONLY
  tried_moves: [14,26,8]
  new_claim:
    id: R20-BMO-BRANCH-CYCLE-FULL-01
    statement: "For connected nice subcubic G whose nonempty 2-core branch graph C[B] is 2-regular, P^ell(G)<=3; no short-theta exclusion is needed."
    proof_status: SELF_CHECK_ONLY
  remaining_obligation: "Full BMO Conjecture 2.6 remains open; immediate structural frontier is mixed branch graph C[B] with direct-branch degrees 1 and 2."
  evidence:
    - "runs/R20/2026-09-19T05-52-13Z_bmo_full_branch_cycle_dp_slack_7f3b91.md"
    - "runs/R20/2026-09-19T04-51-34Z_bmo_stuck_dp_correspondence_61a9e4.md"
    - "runs/R20/2026-09-19T04-06-53Z_bmo_branch_cycle_brooks_7d3a91.md"
    - "artifacts/R20/bmo_branch_cycle_brooks_exact.out"
    - "operations/claims/BMO-2025-PUSHING-DELTA.md"
  audit_ids: []
  next_moves: [1,15,27]
```

No Gmail/email, Drive, public posting, purchase, permission change, scheduler change, shared-root edit, peer-track edit, or I0100 reopening was performed.
