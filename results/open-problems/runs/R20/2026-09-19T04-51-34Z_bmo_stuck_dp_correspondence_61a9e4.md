Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `n_all: 9 -> 9`; status `PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / STUCK_RECOVERY_1_AFTER_N9_RESET`; methods #6 DEFORM TO A SOLVABLE POINT, #12 FIND WHAT IS CONSERVED, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R20 — stuck recovery: the short-theta obstruction is a correspondence-coloring problem

## 0. Continuity, ownership, and why this is a thinking-only run

I continued from the newest complete R20 report

`runs/R20/2026-09-19T04-06-53Z_bmo_branch_cycle_brooks_7d3a91.md`

rather than restarting from the stale scheduler title. The current exclusive R20 research claim remains

`operations/claims/BMO-2025-PUSHING-DELTA.md`,

marked `CLAIMED / READY / CLOSABLE OUTSIDE`.

The stale scheduler-era source `I0100` (Bandeira, Randomstrasse 2025, Conjecture 26) remains historical/frozen in the later R20 continuity. I did not reopen it, did not change its finite Paley frontier, and make no new claim here about any Paley prime or the Paley asymptotic. P04/I0101 two-localization, R12/I0102 degree-four SOS and C28's Paley-ETF line remain distinct.

The active outside source is Julien Bensmail, Clara Marcille and Mano Orenga, *Pushing Vertices to Make Graphs Irregular*, DMTCS 27:3 (2025), article 7, DOI `10.46298/dmtcs.14963`, Conjecture 2.6:

\[
P^\ell(G)\le \Delta(G)
\]

for every nice finite simple graph `G`.

The fixed fleet metric is

\[
n_{\rm all}=\max\{n:\text{every nice simple graph of order at most }n\text{ has an exact witness with }\max\rho\le\Delta\}.
\]

Its supported value is `n_all=9`. The three runs after the `8 -> 9` movement left this fixed metric unchanged, so Section I requires this invocation to be a **thinking-only stuck run**. I therefore add no new checker and make no new theorem/counterexample claim in this report.

At run start I reread the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the BMO claim, the newest complete R20 report, and the visible neighboring Paley records needed to avoid collision. No shared root and no other track's file is edited here.

## 1. Fresh source / current-literature check — 19 September 2026

Primary source page: `https://dmtcs.episciences.org/16418`.

The current DMTCS PDF still states Conjecture 2.6 exactly as `P^ell(G) <= Delta(G)` for nice graphs. Its conclusion explicitly identifies maximum degree three as a first natural gap and separately asks for a readable optimal cactus proof after saying the authors' own modulo approach relied too heavily on exhaustive checking to present legibly.

Current follow-up located this run: Dieter Rautenbach, Laurin Schwartze and Florian Werner, *Coloring by Pushing Vertices*, *Ars Combinatoria* 167 (2026), 147--157, DOI `10.61091/ars167-10`, published online 17 June 2026. Its abstract still presents the general `Delta` bound as conjectural and proves it for cubic graphs and regular bipartite graphs.

Fresh bounded queries on 19 September 2026 included the exact DMTCS title, exact conjecture phrase, the 2026 follow-up title, `pushing vertices subcubic`, `proper pushing scheme correspondence coloring`, and current citing/follow-up combinations. They located the source, the published 2026 follow-up, mirrors/indexes and graph-coloring literature, but no later source-matching general proof and no located theorem matching the current nonregular subcubic subclasses. This is bounded negative evidence only, not a novelty certificate.

A second literature direction became directly relevant: DP-coloring / correspondence coloring. Bernshteyn--Kostochka--Pron, *On DP-coloring of graphs and multigraphs*, Siberian Math. J. 58 (2017), 28--36, characterizes connected multigraphs that are not degree-DP-colorable; Kim--Ozeki, *A note on a Brooks' type theorem for DP-coloring*, J. Graph Theory 91 (2019), 148--161, gives the detailed obstruction structure. In the standard terminology, the exceptional blocks are multiples of complete graphs or cycles. This is established literature, not an R20 novelty claim.

## 2. Section-I stuck protocol

### (a) Exact blocking statement

The immediate frontier from the previous report is the 2-core `C` of a connected nice subcubic graph in which the degree-three core vertices

\[
B=\{v\in V(C):d_C(v)=3\}
\]

induce a 2-regular graph `D=C[B]`. Every branch vertex has exactly one remaining core incidence, so suppressing the degree-two vertices on those remaining branch-to-branch paths gives a perfect matching `M` on `B`.

For each `b in B`, write the branch push as

\[
\rho(b)=3-\varepsilon_b,\qquad \varepsilon_b\in\{0,1\},
\]

and let `p_b in {0,1,2,3}` be the push on the first degree-two vertex of its matching chain. If `b^-` and `b^+` are the two neighbors of `b` in `D`, then the exact branch sum is

\[
\boxed{
\sigma(b)=18+p_b-3\varepsilon_b-\varepsilon_{b^-}-\varepsilon_{b^+}.
}
\tag{2.1}
\]

The chain-transfer lemma from the preceding report gives the exact matching-chain constraints:

\[
\boxed{
\begin{array}{ll}
k=1:&p_u=p_v,\\[2mm]
k=2:&p_u-p_v\ne \varepsilon_u-\varepsilon_v,\\[2mm]
k\ge3:&\text{every ordered pair }(p_u,p_v)\in\{0,1,2,3\}^2\text{ is realizable.}
\end{array}}
\tag{2.2}
\]

Thus the precise blocker is now:

> choose `epsilon_b in {0,1}` and ports `p_b in {0,1,2,3}` satisfying (2.2) and, for every direct branch edge `uv in E(D)`,
> \[
> \boxed{
> p_u-3\varepsilon_u-\varepsilon_{u^-}-\varepsilon_{u^+}
> \ne
> p_v-3\varepsilon_v-\varepsilon_{v^-}-\varepsilon_{v^+}.
> }
> \tag{2.3}
> \]

The previous ordinary-Brooks proof handles this when no `k=1` matching pair is itself a direct edge of `D`. The unresolved short-theta case is exactly when a `k=1` matching path `u-x-v` occurs in parallel with the direct branch edge `uv`; then (2.2) forces `p_u=p_v`, so the old all-branch-push-3 quotient creates a loop.

No theorem is claimed from the reformulation (2.1)--(2.3) in this run.

### (b) Routes tried so far and why each stops

1. **Complete exact graph census.** Exact witnesses now cover every nice simple graph through order nine, moving `n_all` to 9. This is finite evidence only and cannot prove the universal conjecture.

2. **Signless-Laplacian / modular lifting.** `sigma=d+Q rho` yields useful sufficient criteria when `Q` is invertible modulo a suitable prime or has a very small controllable cokernel. General graphs have uncontrolled modular nullspaces, so the criterion is not universal.

3. **Polynomial / Combinatorial-Nullstellensatz dual.** The degree budget is not the obstruction: raw term selections can keep all variable exponents at most `Delta`. The missing ingredient is a noncancellation theorem for the target coefficient.

4. **Pure mod-3 cactus interfaces.** These give complete arguments for unicyclic/bicyclic families and several triangular families, but a four-triangle example showed that insisting every edge be separated modulo 3 is strictly stronger than integer properness. The projection loses exact height inside a residue class.

5. **Exact-sum / range interface for cacti.** This correctly identifies the information missing from the mod-3 state, but no finite compositional compression of the exact forbidden-sum sets was obtained.

6. **Mod-5 deformation for a central cycle with two leaf triangles.** The extra two residues solve that infinite family, but no block-gluing principle was obtained for arbitrary cactus depth.

7. **Explicit subcubic chain words.** They prove the conjecture when the degree-three vertices of the 2-core are independent. Direct degree-three edges are outside that first construction.

8. **Matching-core extension.** An asymmetric `{2,3}` branch-push rule plus an auxiliary orientation extends the proof to the case where the degree-three core graph has maximum degree at most one. The method stops when direct branch edges form cycles.

9. **Ordinary Brooks quotient for 2-regular branch graphs.** Exact port transfer reduces long chains to four-state endpoint constraints and handles the `K5` Brooks exception by one push-2 defect. Its only stated hypothesis excludes a direct branch edge in parallel with a `k=1` matching chain, because contracting that equality chain turns the direct edge into a loop. This is the sharp current obstruction.

### (c) What a proof now has to contain that the preceding routes lack

The missing step is not another chain word. It must combine:

- the exact affine offsets in (2.1), so a short-theta direct edge can remain proper even when its two ports are equal;
- the equality/one-forbidden-pair/free trichotomy (2.2) for matching chains;
- a global existence theorem for edge-specific forbidden port correspondences, because once some branch pushes are 2 and others 3, different direct edges compare differently shifted copies of the same four port values;
- a controlled treatment of the small exceptional quotient structures where a generic Brooks-type theorem can fail.

The first three items are exactly the language of **correspondence coloring (DP-coloring)**. That language was absent from the earlier ordinary Brooks reduction.

### (d) Simplest special case still unproved structurally on the page

The smallest genuinely new structural family is a 2-regular branch graph with at least one matched pair `u,v` joined both by a direct branch edge and by a one-internal-vertex matching path `u-x-v`, with the remainder of the branch cycle arbitrary. Finite members of this family below order ten are already covered by `n_all=9`, but no uniform written proof currently covers all lengths.

A particularly useful quotient test after the correspondence reduction is the doubled-cycle obstruction family: a 4-regular quotient whose underlying block is `C_m^2` (two parallel constraint edges between consecutive quotient vertices). This is one of the standard degree-DP exceptional shapes and is therefore the first family that a generic DP-Brooks invocation cannot simply discard.

### (e) Nearest solved problem and what it supplies

The closest exact theorem is the degree-DP-coloring characterization of Bernshteyn--Kostochka--Pron, refined structurally by Kim--Ozeki. For a connected multigraph and a correspondence cover with at least `d(v)` available colors at each vertex, failure is confined to GDP-tree structure: blocks that are multiples of complete graphs or cycles.

That theorem supplies exactly what the current R20 route lacks: a **Brooks theorem with edge-dependent color identifications**, rather than the ordinary equality constraint used in the previous quotient proof.

What it does **not** supply automatically is the final BMO result, because the quotient can itself have one of the GDP exceptional blocks and because our edge correspondences arise from restricted integer translations, not arbitrary independent matchings. Those exceptional structures must be checked from the BMO algebra, not waved away by the general theorem.

## 3. #6 — DEFORM TO A POINT YOU CAN SOLVE

Start from the all-3 branch assignment and allow binary defects

\[
\rho(b)=3-\varepsilon_b.
\]

For a short-theta pair `u,v`, the `k=1` chain forces a common port `p`. Let `a` and `b` be their other neighbors on the branch cycle. Subtracting (2.1) gives

\[
\sigma(u)-\sigma(v)
=2(\varepsilon_v-\varepsilon_u)+(\varepsilon_b-\varepsilon_a).
\tag{3.1}
\]

Hence if `epsilon_u != epsilon_v`, the right-hand side lies in `{1,2,3}` or `{-1,-2,-3}` regardless of the outer two binary values. So a single asymmetric defect across the matched short-theta pair makes the direct edge automatically safe **without using the port at all**.

The short-theta pairs are edges of the suppressed perfect matching, hence pairwise vertex-disjoint. Therefore one can orient each such pair and assign opposite binary defect values locally without a direct conflict between these requirements.

This is the key new route observation of the thinking run. It is **not promoted to a theorem** here because the resulting shifted constraints on all neighboring edges still require a global port-coloring argument.

## 4. #12 — FIND WHAT IS CONSERVED

The conserved datum on a `k=1` matching chain is the common port value. Contract every such pair to one quotient vertex `q`; call its four allowed colors `p_q=0,1,2,3`.

After choosing the binary defects, each non-loop direct branch edge `uv` forbids exactly the pairs satisfying

\[
p_{q(u)}+c_u=p_{q(v)}+c_v,
\qquad
c_w=-3\varepsilon_w-\varepsilon_{w^-}-\varepsilon_{w^+}.
\tag{4.1}
\]

For fixed `uv`, (4.1) is a **partial matching** between the four colors at its two quotient vertices. A `k=2` matching chain likewise forbids the partial matching

\[
p_u-p_v=\varepsilon_u-\varepsilon_v.
\tag{4.2}
\]

A partial matching can be enlarged to a perfect matching; solving the stronger completed correspondence cover also solves the original BMO constraints. Thus the quotient problem sits naturally inside a 4-fold DP-cover.

There is also a useful degree fact. After contracting `k=1` chains:

- a singleton branch quotient has two direct-cycle incidences and at most one `k=2` matching constraint, hence degree at most 3;
- a non-short-theta contracted `k=1` pair has four direct-cycle incidences, hence degree at most 4;
- a contracted **short-theta** pair loses its internal direct edge after (3.1) certifies that loop automatically, leaving only its two external direct-cycle incidences, hence degree at most 2.

Therefore every quotient component containing a short-theta defect has a vertex with strict color slack: four available colors but degree at most two there. The degree-DP obstruction theorem strongly suggests that such a component cannot be minimally uncolorable.

Again, this paragraph records the route and the exact algebra only. I am not declaring the resulting global BMO theorem proved until the correspondence-cover construction, multiedge accounting and exception handling are written end to end in a later non-stuck run.

## 5. #23 — DO WHAT THE PROPOSER DID NOT EXPECT

The earlier proof tried to retain an **ordinary** four-color quotient, where every constraint meant `p_u != p_v`. The natural reaction to shifted constraints would be to fight those shifts and recover an ordinary coloring.

The opposite move is better: allow the constraints to become *more general* and solve the stronger problem of arbitrary edge-specific correspondences. This lands directly in DP-coloring, where a Brooks-type obstruction theorem already exists.

If this port is valid, the only components not dispatched abstractly are the degree-tight GDP exceptions. In the present maximum-degree-four setting, the potentially relevant 4-regular blocks are multiples of complete graphs or cycles. The old R20 all-3 quotient already contains an explicit repair for the `K5` ordinary-Brooks exception. The remaining high-value check is therefore the cycle-multiple side, together with any small multigraph degeneracies such as `K_2` with four parallel constraints.

There is an additional favorable structural feature specific to R20: if a connected quotient component contains any short-theta defect, then it contains a vertex of quotient degree at most two, so it has list slack and is not degree-tight. Conversely, a fully 4-regular quotient component contains only non-short-theta `k=1` contractions, allowing all branch defects in that component to remain zero; its parallel direct-edge correspondences then collapse back toward the ordinary-equality cover. This looks like the bridge between the general DP theorem and the earlier Brooks proof.

This is the strongest route found in the present thinking-only run. It is a candidate proof architecture, not a theorem claim.

## 6. Exactly one Section-I recovery action chosen

**Chosen action: port the technique from the nearest solved problem.**

The next non-stuck R20 run should port the Bernshteyn--Kostochka--Pron / Kim--Ozeki degree-DP-coloring theorem into the branch-port quotient and attempt an end-to-end proof of the entire 2-regular branch-graph case, including the previously excluded short-theta pairs.

The proof obligations for that run are now concrete:

1. define the quotient multigraph and its 4-fold correspondence cover formally from (2.1)--(2.2);
2. choose opposite binary defects on every short-theta matched pair and prove every resulting quotient loop is automatically safe by (3.1);
3. check degree counting with multiplicity and verify every forbidden relation is a matching that can be completed to a legitimate DP-cover;
4. invoke the precise degree-DP theorem only in the scope its hypotheses permit;
5. reduce any remaining GDP-tree/degree-tight exceptions to explicit BMO-specific structures;
6. reuse, rather than re-prove, the previous exact `K5` one-defect argument where its hypotheses match;
7. handle the cycle-multiple exception directly from the translation structure of the BMO correspondences;
8. only after the full written proof exists, add a small exact checker for the genuinely finite exceptional templates.

The next three **previously unused on this BMO target** Section-B moves are **#14 FIND THE GROUP ACTING, #26 HUNT THE SPORADIC CASE, #8 GO THE OTHER WAY AND DISCRETIZE**. In particular, #14 should look for gauge transformations of the four local port colors that normalize translation correspondences along a quotient spanning tree; #26 should isolate the exact GDP exceptional blocks; #8 should reduce only those exceptions to finite translation templates, not restart an all-graph census.

## 7. No checker and no new mathematical status claim

This invocation intentionally creates no validation artifact or checker. Section I required a thinking-only stuck run, and the outcome is a new route with a much sharper obstruction description.

No new theorem, counterexample, closure, refutation, audit, or novelty certification is claimed. All previous self-check theorems retain their exact prior status. The fixed metric stays

\[
\boxed{n_{\rm all}=9}.
\]

The post-reset unchanged count is now `4`.

## 8. Scheduler/model-control status

The exposed automation control surface still provides prompt/title/schedule/timing/enabled fields, but **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed one-hour execution control**. Therefore the requested `GPT-6 / maximum` remains prompt text only; this completed run is reported as `GPT-5.6 Sol / UNVERIFIED`, not as GPT-6.

The historical P26 `You cannot modify this task` response was authorization-context-specific: repository records also preserve a later authorized context in which the P26 update succeeded. The legitimate way to guarantee a chosen model/reasoning level would be an owner/admin product or backend surface that actually exposes those fields. This R20 run makes no scheduler or permission change.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R20
  lane: CLOSABLE OUTSIDE
  source: "Bensmail--Marcille--Orenga, DMTCS 27:3 (2025), Conjecture 2.6"
  ownership: "R20 exclusive; operations/claims/BMO-2025-PUSHING-DELTA.md"
  stale_predecessor: "I0100 Paley one-localization historical/frozen; not reopened"
  metric: n_all
  before: 9
  after: 9
  movement: "none"
  unchanged_count_after_n9_reset: 4
  status: "PARTIAL / CLAIMED / READY / CLOSABLE OUTSIDE / STUCK_RECOVERY_1_AFTER_N9_RESET"
  tried_moves: [6, 12, 23]
  route_result: "candidate correspondence-coloring/DP-coloring reduction for the short-theta obstruction; no theorem claimed"
  exact_blocker: "solve affine four-port constraints (2.1)--(2.3), including k=1 short-theta pairs, without losing the max-push-3 bound"
  recovery_action: "port the degree-DP-coloring obstruction theorem to the branch-port quotient"
  simplest_unproved_case: "2-regular branch core with at least one direct-edge + k=1 matching short-theta pair; cycle-multiple quotient is the first generic DP exception"
  remaining_obligation: "full Conjecture 2.6; immediate goal is a written proof of the complete 2-regular branch-graph subcubic case"
  next_moves: [14, 26, 8]
  evidence:
    - "runs/R20/2026-09-19T04-06-53Z_bmo_branch_cycle_brooks_7d3a91.md"
    - "operations/claims/BMO-2025-PUSHING-DELTA.md"
    - "DMTCS DOI 10.46298/dmtcs.14963, checked 2026-09-19"
    - "Rautenbach--Schwartze--Werner, Ars Combinatoria 167 (2026), DOI 10.61091/ars167-10"
    - "Bernshteyn--Kostochka--Pron, Siberian Math. J. 58 (2017), 28--36"
    - "Kim--Ozeki, J. Graph Theory 91 (2019), 148--161"
  audits: []
```
