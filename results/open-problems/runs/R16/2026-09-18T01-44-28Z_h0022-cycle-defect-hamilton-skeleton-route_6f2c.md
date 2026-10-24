Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime provides no authenticated model-family selector, reasoning-effort selector, or applied-effort receipt, so this report does not claim otherwise. **NO METRIC MOVEMENT: H0022 sharp-density `A_cyc(1+eps): UNMEASURED -> UNMEASURED`; supported substantive unchanged count `0 -> 1`. Fresh Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #24 FIND THE EXTREMAL OBJECT.**

# R16 HARD OUTSIDE — H0022 first substantive run: cycle-defect spread obstruction and Hamilton-skeleton route

Date: 2026-09-18.
Track: R16.
Active source: Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (2026), Section 1.6, Conjecture 1.5.
Canonical claim: `operations/claims/H0022.md`.

Frozen metric: `A_cyc(c)`, the smallest coefficient `A` for which R16 has a complete proof that `G(n,c log n/n)` is whp universal for every `n`-vertex cycle factor whose cycles all have length at least `A log n/loglog n`, retaining every restriction. Unknown slices are `UNMEASURED`, not infinity. Source target: `A_cyc(1+eps) <= 1+eps` for every fixed `eps>0`.

Source status after this run: **OPEN / PARTIAL METHOD PROGRESS / NO NEW SOURCE COEFFICIENT CERTIFIED**.

## 1. Continuity, repository read, and current-source refresh

I continued from the R16 H0021 handoff

`runs/R16/2026-09-18T00-46-50Z_h0021-spread-capacity-handoff-h0022_91e4.md`

rather than reopening H0021, I0036, or the stale native Beck--Fiala title. Before research I reread the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the current NEW-METHODS owner directive, the active H0022 claim, the newest own R16 state, and the newest neighboring H0023/P20 final report.

The neighboring H0023 handoff matters: its fixed-permutation path-hypergraph route had very good mean regularity but exposed two genuine barriers at the sharp depth `k ~ log n/loglog n`: quenched clustering around actual graph edges and perfect completion for growing uniformity. H0022 must not silently assume that unresolved fixed-endpoint problem.

Fresh searches on 2026-09-18 for the exact arXiv id, title/authors, `Conjecture 1.5`, later versions, `cycle factor girth`, `growing uniformity perfect matching`, `spread Hamilton cycles`, and related terms still locate arXiv:2608.06358v1 (6 August 2026) as the current primary source and no later source-matching resolution. This is bounded negative evidence only.

The source statement remains exactly:

> for every fixed `eps>0` and every integer `ell >= (1+eps) log n/loglog n`, whp `G(n,(1+eps)log n/n)` is universal for all `n`-vertex cycle factors of girth at least `ell`.

The source proves instead a large-constant result: for sufficiently large absolute `C`, `G(n,C log n/n)` is whp universal for all cycle factors of girth at least `100 log n/loglog n` (the proof constants can be taken below 100 in the paper's more general formulation). The paper itself says that the sharp `1+eps` coefficient is open and that the reduction to cycle factors proceeds by deleting long bare paths to obtain a linear forest and then using linking systems.

## 2. #2 ATTACK THE NEGATION FIRST — the shortest equal-cycle factor is the correct stress family, but first moment does not refute the conjecture

Let

`p = c log n/n`, `c>1`,

and let

`k = A log n/loglog n`, `A>0`,

with `k | n`, `r=n/k`. Let `X_k` count `C_k`-factors. The exact number of labelled `C_k`-factors in `K_n` is

`N_k = n! / ((2k)^r r!)`,

hence

`E X_k = N_k p^n`.

Stirling gives

`log E X_k = (1 - 1/A + o(1)) n loglog n + O_c(n)`.

Thus:

- if `A<1` by a fixed amount, `E X_k -> 0` superexponentially on the `n loglog n` scale, recovering the source's elementary lower obstruction;
- if `A>1` by a fixed amount, `E X_k` is enormous, so the equal-shortest-cycle family produces no first-moment counterexample above the conjectured constant 1.

The same calculation can be done for an arbitrary cycle-type partition `lambda=(l_1,...,l_r)` with multiplicities `m_s`:

`N_lambda = n! / (2^r prod_i l_i prod_s m_s!)`.

Since `prod_s m_s! <= r! <= r^r` and `prod_i l_i <= (n/r)^r`,

`N_lambda >= n!/(2n)^r`.

When every `l_i >= k`, we have `r<=n/k`, so the equal-shortest family is the leading first-moment bottleneck on the `n loglog n` scale. I do not claim exact finite-n extremality among all partitions, only this asymptotic leading-order statement.

There is also no local minimum-degree counterexample at `c>1`: by a direct union bound,

`P(delta(G)<2) <= n[(1-p)^(n-1) + (n-1)p(1-p)^(n-2)] = n^{1-c+o(1)} log n = o(1)`.

So any negation of Conjecture 1.5 above coefficient 1 would have to be a genuinely global packing obstruction, not an isolated-vertex/degree-one obstruction.

## 3. #18 SAY IT IN ANOTHER LANGUAGE — the one-shot spread obstruction is exactly the cyclomatic defect

The cleanest reformulation is as a spread-capacity calculation on component factors.

### Proposition 3.1 (component-defect spread lower bound)

Let `H` be a connected graph with `v` vertices and `e` edges, let `v | n`, and let `F_H` be the family of all `H`-factors of `K_n`. If a probability measure `nu` supported on `F_H` is `q`-spread in the edge-set sense, then

`q^e >= (n/v) / N_H`,

where

`N_H = (n)_v / |Aut(H)|`

is the number of labelled copies of `H` in `K_n`.

**Proof.** Every sampled `H`-factor has exactly `n/v` components. Summing `P(J is a component)` over all labelled copies `J` of `H` gives exactly `n/v`, so some `J` has probability at least `(n/v)/N_H`. If `J` is a component, then all `e` edges of `J` lie in the sampled factor. By `q`-spreadness that probability is at most `q^e`. QED.

This is an elementary density/spread obstruction and is very likely folklore in the modern Kahn--Kalai/spread language; I make **no novelty claim** for Proposition 3.1.

For `H=C_k`, `|Aut(C_k)|=2k`, so every `q`-spread law on `C_k`-factors satisfies the exact inequality

`q^k >= 2n/(n)_k`,

hence for `k=o(sqrt n)`,

`q >= (1+o(1)) n^{-1+1/k}`.

At `k=A log n/loglog n`,

`q >= (1+o(1)) (log n)^(1/A)/n`.

The source's quantitative FKNP theorem (its Theorem 2.15) says that a direct hit from a `q`-spread family of minimal edge-size `L` is guaranteed at `p>96 q log L`. Here `L=n`, so a **direct one-shot application to the full `C_k`-factor family cannot reach** `p=Theta(log n/n)` for any fixed `A`: its spread lower bound forces a sufficient density of order at least

`(log n)^(1+1/A)/n`.

This is a proof-architecture obstruction, not a lower bound on the actual cycle-factor threshold.

### Why deleting one edge per cycle is exactly the right topological move

For comparison take `H=P_k`, the path on `k` vertices and `k-1` edges. Proposition 3.1 gives

`q^(k-1) >= 2n/[k (n)_k]`,

so the unavoidable scale becomes

`q >= (1+o(1))/n`.

Thus removing **one edge per cycle** eliminates precisely the extra factor `n^{1/k}=(log n)^{1/A+o(1)}` in the spread obstruction. In density language, the cycle has `e=v` while the path has `e=v-1`: the single cyclomatic defect is exactly what makes the unfragmented factor family too concentrated for one-shot FKNP.

This gives a conceptual explanation for the source paper's successful high-constant strategy of deleting long paths and working with linear forests. The new target should not be `better q-spread on whole cycle factors`; that is impossible at the required scale. It should be `optimal spread after cutting the cyclic defect`, followed by a sharp closure mechanism.

## 4. An exact positive benchmark: complete-space Hamilton skeletons produce an optimally spread closure matching

The spread obstruction above suggests cutting one edge from every target cycle. There is an exact complete-graph model showing what the ideal closure distribution should look like.

Assume again `n=rk`, `k>=3`. Choose uniformly an undirected Hamilton cycle `H` of `K_n` and independently choose one of the `k` offsets. Cut `H` into `r` consecutive `k`-vertex path blocks. Let `R(H)` be the `r` chords joining the two endpoints of each block.

### Lemma 4.1 (uniform closure matching)

`R(H)` is exactly uniform over all `r`-edge matchings of `K_n`.

**Proof.** Its law is invariant under the full vertex permutation group, which acts transitively on `r`-matchings. Every `r`-matching occurs: orient its edges, partition the remaining `r(k-2)` vertices among the pairs, order each block, and concatenate the blocks into a Hamilton cycle. Hence all `r`-matchings have the same positive probability. QED.

For a fixed matching `S` of size `s`, the exact containment probability under the uniform `r`-matching law is

`P(S subset R) = 2^s (r)_s/(n)_(2s)`.

Consequently

`P(S subset R) <= [2r/(n-2r)^2]^s`,

so this closure law is `q_0`-spread with

`q_0 = 2r/(n-2r)^2 = (2+o(1))/(nk)`.

This is optimal up to `1+o(1)` because any probability law on `r`-edge subsets of `E(K_n)` has the elementary capacity lower bound `q >= r/binom(n,2) = (2+o(1))/(nk)`.

This exact calculation is the strongest positive information of the run: **after cutting one edge per shortest cycle, the ideal complete-space closure law has precisely the optimal spread scale `Theta(1/(nk))`.** No extra `(log n)^{1/A}` penalty remains.

Again, the complete-space symmetry calculation itself is elementary and I do not claim it as publication-novel. Its value is that it specifies the exact quenched statement a sharp random-graph proof should try to preserve.

## 5. #24 FIND THE EXTREMAL OBJECT — equal shortest cycles and the Hamilton-skeleton entropy balance recover the constant 1

The equal `C_k`-factor is now the canonical extremal object for the route.

Split the target random graph into two independent layers

`G = G_1 union G_2`,

with, say, `p_1=(1+eps/2) log n/n` and `p_2=(eps/2+o(1)) log n/n`, using the exact union relation if desired. The first layer is already above the Hamiltonicity threshold.

Glebov--Krivelevich (SIAM J. Discrete Math. 27 (2013), 27--42) prove that in this range the number of Hamilton cycles is

`n! p_1^n (1+o(1))^n = exp((1+o(1)) n loglog n)`

whp.

A **single** Hamilton skeleton is hopeless for the equal factor: for a fixed Hamilton cycle there are only `k` offsets into consecutive `k`-vertex blocks, and each offset requires `r=n/k` independent closure chords from `G_2`. Hence, conditionally on that skeleton,

`P(some offset closes) <= k p_2^r = exp(-(1/A+o(1)) n loglog n)`.

So `one Hamilton cycle + sprinkle` fails decisively.

But the *number* of Hamilton skeletons has entropy `exp((1+o(1))n loglog n)`, while the closure cost is `exp(-(1/A+o(1))n loglog n)`. Their exponents balance at

`A=1`.

This reproduces the conjectured constant for an entirely different reason than the raw factor first moment and points to a sharp route:

> **Hamilton-skeleton entropy + optimally spread closure matchings.**

The total Hamilton-cycle count alone is not enough: all those cycles could, in principle, induce closure matchings in a badly clustered way. What is missing is a **quenched cyclic-spacing spread theorem**.

A useful precise target is the following. For typical

`G_1 ~ G(n,(1+eta)log n/n)`,

find a probability measure on Hamilton cycles of `G_1` such that, after choosing the target block lengths and a random cyclic offset/order, the induced set `R` of one closure edge per block satisfies

`P(S subset R | G_1) <= [C/(nk)]^|S|`

for every matching `S`, uniformly over all target parts at least `k`, with `C=C(eta)`.

The complete graph has this with `C=2+o(1)` by Lemma 4.1. Glebov--Krivelevich give the correct *total* number of sparse Hamilton cycles, but their counting theorem by itself does not give this local cyclic-position equidistribution.

## 6. The hypergraph view isolates the same sharp scale

For the equal-factor stress case, let `H_k(G)` be the `k`-uniform hypergraph on `V(G)` whose hyperedges are vertex sets spanning a `k`-cycle. A `C_k`-factor is a perfect matching in this hypergraph.

For a fixed vertex `v`, the expected number of present `k`-cycles through `v` is

`D_k = ((n-1)_(k-1)/2) p^k = n^{A-1+o(1)}`.

For two fixed vertices `u,v`, the unconditional expected codegree is exactly

`((k-1)/(n-1)) D_k`.

However, conditioning on the graph edge `uv` being present, cycles that use that edge alone contribute conditional mean

`(n-2)_(k-2) p^(k-1) = (2+o(1)) D_k/(np) = Theta(D_k/log n)`.

Thus the same quenched local clustering seen in neighboring H0023 appears here: the mean hypergraph looks extremely regular, while actual graph edges create codegree clusters of relative size `Theta(1/log n)`. Growing-uniformity Pippenger--Spencer technology does exist for `k=O(log n)` (e.g. Guo--Patton--Warnke, Combinatorica 43 (2023), 853--884), but it is a near-perfect/edge-colouring tool, not a certified perfect-completion theorem for this correlated cycle hypergraph. I therefore do not invoke it as if it solved the factor problem.

## 7. Universality has fewer targets than H0023, but a naive per-type union is still quantitatively impossible

An unlabeled cycle factor is determined by an integer partition of `n` into parts at least `k`. Hence the number of target isomorphism types is at most the ordinary partition number `p(n)=exp(O(sqrt n))`, drastically smaller than the `m!` endpoint permutations in H0023.

It is also still at least `exp(Omega(sqrt n))` when `k=o(sqrt n)`. A simple construction: choose `Theta(sqrt n)` distinct integers in `[sqrt n,2sqrt n]` with total of all chosen candidates below `n/3`. Among their `2^{Theta(sqrt n)}` subsets, pigeonhole gives `exp(Omega(sqrt n))` distinct subsets with the same sum; appending the one remaining part `n-s` gives that many distinct admissible partitions, all parts much larger than `k`.

This matters because even **ideal** residual closure spread does not make a per-type union bound cheap enough. The best possible residual scale is `q=Theta(1/(nk))`. The optimal-convergence form of the Park--Pham/FKNP hitting theorem has required density of order

`q log(L/delta)`

to make the miss probability at most `delta`. To union over `exp(Omega(sqrt n))` types by brute force would require `log(1/delta)=Omega(sqrt n)`, hence density at least

`Omega(q sqrt n) = Omega(1/(k sqrt n))`,

which is asymptotically much larger than the available `Theta(log n/n)` budget because

`[1/(k sqrt n)] / [log n/n] = sqrt n/(k log n) -> infinity`.

Therefore a sharp proof needs **simultaneous structure**, not `prove each cycle type separately with a q-spread hit theorem and union bound`. This is a second architecture obstruction, distinct from the whole-factor cyclomatic spread obstruction.

The natural stronger target is to group many length partitions under one common first-layer object — for example, a length-flexible path-factor family or a quenched Hamilton-skeleton measure — and prove a deterministic/random-host property that serves all partitions at once.

## 8. What survived the three attacks

### #2 ATTACK THE NEGATION FIRST

No source counterexample emerged. The equal-shortest factor `C_k^{n/k}` is the sharp stress family: it reproduces the `A=1` first-moment boundary, while minimum degree and other obvious local obstructions disappear at every fixed `c>1`.

### #18 SAY IT IN ANOTHER LANGUAGE

The problem is cleaner after cutting the cyclomatic defect. Whole cycle factors have an unavoidable `q >= n^{-1+1/k}` concentration; one-cut path factors have only the optimal `1/n` component obstruction, and their closure edges ideally form an optimally spread `r`-matching at scale `1/(nk)`.

### #24 FIND THE EXTREMAL OBJECT

Equal shortest cycles remain the extremal test. One frozen Hamilton cycle is exponentially inadequate, but the full Hamilton-cycle entropy in a sharp random graph has exactly the right exponent to beat closure cost when `A>1`. The missing theorem is local cyclic-spacing spread, not total Hamilton-cycle abundance.

## 9. Nearest literature and explicit prior-art boundary

Searches included the source paper and its cited cycle-factor literature, Glebov--Krivelevich on counting Hamilton cycles near the threshold, Frankston--Kahn--Narayanan--Park / Park--Pham / optimal convergence versions of the spread theorem, Spiro on smoother spread, Kelly--Müyesser--Pokrovskiy on optimal spread in dense Dirac hosts, Guo--Patton--Warnke on growing-uniformity Pippenger--Spencer, and searches for sparse-random Hamilton-cycle spread/equidistribution.

What these sources supply:

- the current H0022 source already fragments cycle factors to linear forests at a large constant;
- Glebov--Krivelevich supply the correct total Hamilton-cycle entropy at the connectivity/Hamiltonicity scale;
- modern spread theory supplies the correct threshold conversion once an optimal spread law is in hand;
- dense Dirac-host work constructs optimally spread Hamilton embeddings, but its linear minimum-degree hypothesis does not cover `G(n,Theta(log n/n))`;
- large-uniformity Pippenger--Spencer results handle `O(log n)` uniformity in near-perfect/colouring settings, not the correlated perfect-completion statement needed here.

I did **not** locate a theorem giving the required quenched cyclic-spacing spread for Hamilton cycles of a sparse `G(n,p)` at `p=(1+eta)log n/n`. That absence is bounded-search evidence, not a novelty certificate.

The component-defect lower bound and complete-graph closure law are elementary enough that they should be treated as folklore/route lemmas unless a later novelty search proves otherwise.

## 10. Metric, status, and next run

No complete uniform sharp-density coefficient was proved in this run, so the frozen source metric does not move:

`A_cyc(1+eps): UNMEASURED -> UNMEASURED`.

Supported substantive unchanged count:

`0 -> 1`.

H0022 remains **OPEN / PARTIAL**. This is not a stuck episode.

The next nonrepeating H0022 triple is:

- **#1 CHANGE THE CATEGORY:** use the bipartite/permutation representation of a 2-factor and the induced cycle-type support problem;
- **#9 RANDOMIZE:** randomize over Hamilton/path skeletons rather than committing to one skeleton;
- **#25 COUNT THE SAME THING TWICE:** count `(skeleton, closure matching)` incidences locally, seeking the quenched `Theta(1/(nk))` cyclic-spacing spread bound.

The concrete next blocking statement is:

`for typical G_1 at p_1=(1+eta)log n/n, construct a Hamilton/path-skeleton measure whose residual closure sets have q=O_eta(1/(nk)) spread uniformly over admissible length types, or produce a finite/asymptotic obstruction to such a measure.`

If this can be obtained, the remaining universality issue is **simultaneous length-type coverage**, for which a naive per-type FKNP union is now ruled out quantitatively above; the proof must group types or establish a common deterministic good-host property.

## 11. Native Beck--Fiala source refresh

The scheduler/native title remains stale as an active research target, and I did not count published/preprint improvements as R16 research progress.

- Bansal--Jiang, arXiv:2508.03961v2, proves the conjectured `O(sqrt t)` order for `t >= log^2 n` and gives a weaker polylogarithmic-loss bound below that regime.
- Guo--Fang--Lu, arXiv:2609.11189v1 (submitted 10 September 2026), now claims the stronger real Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduces

  `disc(A) < 3 sqrt(2 pi t)`

  for every integer `t>=1`, with no restriction on `n`.
- Karingula--Lovett, ECCC TR26-188 (17 September 2026), gives a separately authored elementary Komlos proof with constant `36`, which independently implies the complete Boolean bound

  `disc(A) <= 36 sqrt t`

  for all `t,n`.

These are extremely recent preprint/technical-report claims rather than mature refereed consensus, but there are now two independent current proofs of a stronger statement than Beck--Fiala. R16 therefore continues its already-authorized HARD successor rather than pretending that a restricted Bansal--Jiang regime is the full answer or restarting the stale title.

## 12. Model / scheduler control status

The limitation is unchanged and is directly visible in the current task-control schema: the exposed controls include task identity, title/prompt, schedule or relative start, timing mode, and enablement; there is **no model-family field and no reasoning-effort field**, and there is no authenticated applied-model receipt. Therefore GPT-6/maximum can be requested only in prompt text here. Enforcing it would require an authorized product/workspace scheduler or API that exposes those selectors plus runtime telemetry.

The historical P26 `You cannot modify this task` event is not treated as a current global failure: current repository reconciliation records a later successful P26 update from an authorized P/C context. If a task still returns that permission error, the compliant remedy is the owning workspace/account context or platform support, not duplication or permission bypass.

No scheduler state, shared root ledger, peer research file, email, Drive content, public post, purchase, permission, or workflow was changed.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R16
  source_id: H0022
  source_status: OPEN
  research_status: PARTIAL
  metric_name: A_cyc(c)
  metric_slice: A_cyc(1+eps)
  before: UNMEASURED
  after: UNMEASURED
  substantive_unchanged_before: 0
  substantive_unchanged_after: 1
  methods:
    - 2
    - 18
    - 24
  new_durable_items:
    - whole C_k-factor q-spread lower bound q >= (1+o(1)) n^(-1+1/k)
    - one-cut path-factor component obstruction drops to q >= (1+o(1))/n
    - exact complete-space closure law: uniform Hamilton skeleton + offset gives uniform r-matching
    - exact uniform-r-matching spread q <= 2r/(n-2r)^2 = (2+o(1))/(nk)
    - one frozen Hamilton skeleton fails for equal C_k-factor at sharp density
    - Hamilton-skeleton entropy versus closure cost balances exactly at A=1
    - naive per-type optimal-spread hitting plus union bound cannot cover exp(Omega(sqrt n)) admissible types at target density
  next_methods:
    - 1
    - 9
    - 25
  next_blocker: >-
    Establish or refute a quenched O_eta(1/(nk))-spread law for residual
    closure matchings generated by Hamilton/path skeletons in typical
    G(n,(1+eta)log n/n), uniformly over admissible cycle-length types;
    then replace the impossible per-type union bound by simultaneous structure.
```
