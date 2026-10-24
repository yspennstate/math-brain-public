Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO METRIC MOVEMENT:** H0021 `Delta_near: 2 -> 2`; supported H0021 unchanged count `2 -> 3`. Methods actually tried: **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #13 FIND WHAT ONLY INCREASES, #21 ASK WHO ELSE HAS THIS SHAPE**. This is the third consecutive unchanged H0021 run, so the **next** invocation must be `STUCK_RECOVERY_1 / thinking-only`; this report is the substantive third run, not the recovery itself.

# R16 HARD OUTSIDE — H0021: a subcubic linear-forest normal form and an exact scale obstruction to the frozen-Hamilton-cycle route

Date: 2026-09-17 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Active source: H0021 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Conjecture 1.4.

Source status after this run: **OPEN / PARTIAL / ACTIVE HARD OUTSIDE**. The source conjecture is not solved here. Frozen metric remains `Delta_near=2`.

## 1. Continuity, ownership, exclusions, and current-source check

I continued from the newest complete R16 report

`runs/R16/2026-09-17T19-47-43Z_h0021-sharp-almost-spanning-rollback-gap_c91e.md`

rather than restarting the stale Beck--Fiala title or reopening handed-off I0036.

Before mathematics I reread/recovered the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, canonical `operations/claims/H0021.md`, the newest R16 reports, the newest H0023/P20 neighboring reports, and the H-intake ledger. H0021 remains the exclusive R16 HARD claim; H0023 is a neighboring source problem whose P20 route has already rotated after six unchanged runs and is not a solved black box.

A fresh 2026-09-17 search of the exact title/authors/arXiv id and Conjecture 1.4 recovered arXiv:2608.06358v1 and no later source-matching proof. This is bounded negative evidence, not a worldwide openness certificate. The primary-source text still states

\[
G\!\left(n,(1+\varepsilon)\frac{\log n}{n}\right)
\quad\text{should whp be }\mathcal T_{n,\Delta}\text{-universal}
\]

for every fixed `epsilon>0` and integer `Delta>=2`. The same paper proves the result only at `C log n/n` for sufficiently large absolute `C`; in the difficult `psi=1` linking-system regime its current proof has depth constant 24 and allows `C<2000`, while Conjecture 1.6 proposes the sharp `(1+epsilon) log n/loglog n` depth.

The preceding R16 theorem remains valid and preserved: at every fixed `c>1`, whp `G(n,c log n/n)` is simultaneously universal for all fixed-`Delta` trees with a deficit `O(n loglog n/log n)`. The missing source obligation is still the final spanning absorption/completion window.

## 2. Frozen metric

`Delta_near` is the largest integer `D>=2` for which R16 has a complete source-matching proof that, for every fixed `epsilon>0`, whp

\[
G\!\left(n,(1+\varepsilon)\frac{\log n}{n}\right)
\]

contains every `n`-vertex tree of maximum degree at most `D`.

Before this run: `Delta_near=2`.

After this run:

\[
\boxed{\Delta_{\rm near}=2.}
\]

No source case is being relabelled as solved.

## 3. New structural lemma: every subcubic tree is a spanning linear forest plus a matching

The first move was to change the completion problem into a form where Hamiltonicity could conceivably supply almost all tree edges.

### Lemma R16-H0021-LFM

Let `T` be a tree with maximum degree at most three. Let `B` be its set of degree-three vertices and let `L` be its number of leaves. Then there is a matching `M subset E(T)` such that

1. every vertex in `B` is incident to an edge of `M`;
2. every edge of `M` has exactly one endpoint in `B`;
3. `|M|=|B|=L-2`;
4. `T-M` is a spanning linear forest with exactly `L-1` path components.

### Proof

If `B` is empty, take `M=emptyset`. Otherwise let `H` be the minimal connected subtree of `T` containing `B`. Choose a leaf `v` of `H`. At most one of the three branches incident to `v` contains another vertex of `B`; hence at least one incident edge `vu` enters a branch containing no degree-three vertex, and in particular `u notin B`.

Put `vu` into `M` and discard, for the purpose of the induction, `v` together with all `B`-free branches hanging from it. All remaining degree-three vertices lie in the unique remaining component, which is again subcubic. Repeating gives pairwise vertex-disjoint chosen edges, each with one endpoint in `B`, and saturates all of `B`. Thus `|M|=|B|`.

The degree identity for a subcubic tree gives `n_1=n_3+2`, so `|B|=L-2`. After deleting `M`, every former degree-three vertex has degree at most two and no other degree can exceed two; as a subgraph of a tree, `T-M` is therefore a linear forest. Removing `|M|` edges from a tree creates `|M|+1=L-1` components. QED.

This elementary lemma may well be folklore; no novelty claim is made. Its role is to give a particularly rigid spanning normal form for the first unresolved source degree `Delta=3`.

## 4. #5 ADD A PARAMETER — the tempting Hamilton-skeleton route and its scale

Write

\[
p=(1+\varepsilon)\frac{\log n}{n}.
\]

The normal form suggests: obtain a Hamilton cycle `C`, place each path component of `T-M` consecutively on `C`, and use non-cycle random edges for `M`. If `r=|M|+1` is the number of path components, then arbitrary cyclic block order and orientation provide about

\[
2^r(r-1)!
\]

placement instructions. For one fixed placement, the `|M|=r-1` required matching edges are distinct, so an independent chord graph `G(n,q)` supplies them with probability exactly `q^{r-1}`.

Hence the first-moment scale of this *unfrozen block-permutation family* is

\[
\log \mathbb E X
=(r-1)\big(\log(2rq)-1\big)+O(\log r).
\]

At the source hard scale

\[
r\asymp \frac{n\log\log n}{\log n},
\qquad q=A\frac{\log n}{n},
\]

we have `rq=Theta(loglog n)`, so this crude first moment is very large. That initially made the Hamilton-skeleton representation look competitive with a full arbitrary-permutation linking system.

The next calculation shows why this first moment is deceptive if the Hamilton cycle is frozen before the attachment problem is solved.

## 5. #13 FIND WHAT ONLY INCREASES — a rigorous isolation obstruction for a frozen Hamilton cycle

The right stress test is not a new adversarial tree but a **known solvable tree**: the comb. Let `k|n`, set `r=n/k`, and let `Comb_{n,k}` consist of a backbone path on `r` vertices, with one disjoint tooth path on `k-1` vertices attached to every backbone vertex. Montgomery proved that for every `k=k(n)` and every fixed `epsilon>0`,

\[
G\!\left(n,(1+\varepsilon)\frac{\log n}{n}\right)
\]

contains `Comb_{n,k}` whp. Thus any obstruction below is necessarily an obstruction to the **method**, not to H0021 or even to this family.

Fix any deterministic Hamilton cycle `C` on `[n]`, independently of a random chord graph

\[
H\sim G\!\left(n,q\right),
\qquad q\le A\frac{\log n}{n},
\]

where `A>0` is an arbitrary fixed constant. Give the algorithm `C` for free. Consider the following very generous frozen-cycle block architecture:

- map the comb backbone to any consecutive block of `r` vertices of `C`, in either orientation;
- partition the complementary cycle path into `r` consecutive slots, each of size `k-1`;
- permute the `r` tooth paths arbitrarily among these slots and orient every tooth arbitrarily;
- use edges of `H` for the tooth-to-backbone attachment edges (and even permit the two boundary cycle edges if they happen to help).

### Theorem R16-H0021-FROZEN-CYCLE-NOGO

Assume

\[
k\sim \beta\frac{\log n}{\log\log n}
\]

for any fixed `beta>0`. For every fixed `A>0`, with high probability over `H`, **no** embedding of `Comb_{n,k}` exists within the frozen-cycle block architecture above, simultaneously for every choice of the consecutive backbone block and its orientation.

### Proof

Fix one backbone interval. Let `W` be the set of possible host images of the first tooth vertex over all tooth slots and both tooth orientations. Each slot contributes only its two endpoints, hence

\[
|W|\le 2r.
\]

For a backbone host vertex `v`, if `N_H(v) cap W=emptyset`, then its tooth cannot be attached by any permutation or orientation of the tooth blocks. The corresponding isolation events are independent over the `r` distinct backbone vertices because they depend on disjoint sets of random edges. Their common probability satisfies

\[
s=(1-q)^{|W|}
\ge (1-q)^{2r}
=
\exp\big(-(2+o(1))qr\big).
\]

Since

\[
r=\frac nk
=\left(\frac1\beta+o(1)\right)
\frac{n\log\log n}{\log n},
\]

we have

\[
qr\le\left(\frac A\beta+o(1)\right)\log\log n
\]

and therefore

\[
s\ge (\log n)^{-2A/\beta+o(1)}.
\]

If `Z` denotes the number of isolated backbone vertices, then

\[
\mathbb EZ=rs
\ge n(\log n)^{-1-2A/\beta+o(1)}\log\log n
\longrightarrow\infty.
\]

Indeed `Z` is binomial for a fixed backbone interval. Thus

\[
\Pr(Z\le2)\le \exp(-\Omega(rs)).
\]

There are at most `2n` choices of a consecutive backbone interval together with its orientation. Because `rs=n/polylog(n)`, a union bound over these `2n` choices is still `o(1)`. Therefore every frozen backbone placement has at least three vertices with no chord to any possible tooth endpoint. Even granting the two boundary edges of `C`, at least one tooth is impossible to attach. QED.

The theorem is stronger than the earlier constant-layer warning: it gives the Hamilton cycle for free and lets the independent chord graph have **any fixed multiple** `A log n/n` of the connectivity density. The failure occurs because a fixed path slot exposes only two candidate root positions. At `k~log n/loglog n`, the effective parent-to-slot degree is only `Theta(loglog n)`, far below the `Theta(log r)=Theta(log n)` scale needed to eliminate isolated left vertices.

This is precisely why the enormous raw count `2^r r!` does not automatically turn into a usable local algorithm: once the backbone interval is frozen, each individual parent still sees only `r` slot choices, and a polynomial-in-`log n` isolated fraction survives.

## 6. #21 ASK WHO ELSE HAS THIS SHAPE — Montgomery's connectors say what the missing ingredient is

The nearest solved problem is exceptionally informative because it is the same comb family used in the obstruction. Montgomery, *Sharp threshold for embedding combs and other spanning trees in random graphs* (arXiv:1405.6560; later RSA), proves the sharp `(1+epsilon) log n/n` result for `Comb_{n,k}` for every `k`.

His proof does **not** freeze one Hamilton cycle and give each tooth only two possible attachment points. It constructs `(l,gamma)`-connectors: an `l`-vertex graph carrying two endpoint sets of linear size `gamma l` such that every allowed endpoint pair is joined by a Hamilton path through the connector. It then turns attachment into grouped bipartite matching and verifies Hall. In the larger-`k` regime the proof explicitly replaces individual vertices by `log^6 n`-scale connectors to boost the effective edge probability above the matching threshold.

That mechanism is exactly what the no-go theorem says is missing here: **port amplification**. A frozen path block has two admissible root positions; a connector has `Theta(l)` admissible positions. The former gives effective degree `Theta(loglog n)` in the hard regime; the latter can raise grouped compatibility to the matching threshold while preserving exact vertex coverage.

This suggests a materially different full-bound route for `Delta=3`:

1. use the linear-forest-plus-matching normal form only as the combinatorial skeleton;
2. do **not** choose the spanning path pieces as rigid intervals of a preselected Hamilton cycle;
3. replace suitable long degree-two stretches by flexible connectors with many admissible port locations;
4. solve the matching constraints of the quotient **tree** of path pieces, rather than an arbitrary endpoint permutation as in source Conjecture 1.6;
5. use deferred decisions so that connector construction and port matching share the sharp-density randomness instead of wasting a constant-factor layer.

The quotient constraint is weaker than an arbitrary-permutation linking system: only the fixed tree matching dictated by the target must be realized. What is not yet proved is a uniform multi-port connector statement strong enough when one path component carries several matching endpoints.

## 7. What actually failed and what survives

### Failed route A: fixed Hamilton cycle + independent chord matching

The comb theorem above rules this out even when the chord graph receives `A log n/n` for arbitrary fixed `A`. The problem is not lack of total candidate block permutations; it is local isolation after freezing the cycle geometry.

### Failed route B: an adjacent-block-swap monovariant on a frozen cycle

I tried to use adjacent block transpositions to monotonically reduce the number of unsatisfied matching edges. Adjacent swaps are genuinely local — blocks after the swapped pair return to the same boundary — but the comb obstruction exhibits an invariant bad set: a backbone vertex with no edge to the union of all possible tooth-slot endpoints cannot be repaired by *any* sequence of tooth permutations, orientations, or adjacent swaps. Thus the natural deficit potential has terminal local minima of macroscopic multiplicity.

### Surviving route

Port-amplified connectors are not hit by this obstruction because the allowed endpoint set itself changes from size two to a growing set. Montgomery's solved comb proof supplies a concrete model for this. A successful R16 continuation would need to generalize that flexibility from star-like comb attachment to the tree-indexed matching skeleton of an arbitrary subcubic tree, while keeping the total exposure at `(1+epsilon) log n/n`.

## 8. Stuck trigger

This run leaves `Delta_near` unchanged for the third consecutive H0021 invocation. Under the owner protocol, **the next H0021 invocation is `STUCK_RECOVERY_1 / thinking-only`**. It must contain the five-part stuck diagnosis and choose exactly one recovery action.

The recovery I recommend is: **port the nearest solved technique** — Montgomery's connector/Hall mechanism — to the subcubic matching-linear-forest normal form. The exact blocker to put at the top of that recovery is a multi-port version:

\[
\boxed{
\text{build, at sharp density, disjoint path-connectors whose admissible port sets support the fixed tree-indexed matching constraints.}
}
\]

The simplest special case should not be the full source conjecture. It should be the class in which every path component of `T-M` contains at most two `M`-endpoints; then ordinary two-ended connectors may suffice. If that class cannot be closed, the obstruction should be reduced to an exact finite matching/connector counterexample before considering a more general multi-port gadget.

Recommended nonrepeating recovery methods: **#6 DEFORM TO A POINT YOU CAN SOLVE, #10 DERANDOMIZE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE**. These differ from the present #5/#13/#21 triple.

## 9. Beck--Fiala stale-title refresh

The native title remains stale relative to R16's admitted successor. Bansal--Jiang, arXiv:2508.03961v2, proves the conjectured `O(sqrt(t))` order for `t>=log^2 n` and gives a weaker polylogarithmic bound below that regime; it does not by itself settle all `t,n`.

A newer primary preprint, Shengtao Guo, Ethan X. Fang, Junwei Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1 (submitted 10 September 2026), explicitly claims the dimension-free Komlós bound `3 sqrt(2 pi)` and deduces

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}
\]

for every integer `t>=1`, with no `n` restriction. I continue to label this **fresh primary-preprint full-resolution claim, not mature refereed consensus**. It remains a reason not to restart the stale Beck--Fiala title while H0021 is the active admitted R16 target.

## 10. Model/scheduler control and permissions

The exposed scheduler mutation surface still has prompt/title, schedule or relative start, timing mode, enablement and task identity, but **no model-family selector and no reasoning-effort selector**. Therefore GPT-6/maximum remains a request in prompt text only. Enforcing it would require an authorized product/workspace scheduler or API exposing those selectors plus authenticated runtime telemetry.

The policy file still records native modification probes returning `You cannot modify this task` for P26/P01/P03 in one authorization context. The compliant workaround is the owning workspace/context or platform support; do not duplicate the job, bypass permissions, or represent a repository edit as a scheduler repair.

No scheduler state, shared root ledger, peer file, email, Drive content, public post, purchase, permission, or workflow was changed in this run.

## 11. Prior-art qualification

Queries checked on 2026-09-17 included the exact H0021 title/authors/arXiv id and Conjecture 1.4; `subcubic tree matching linear forest`; `Hamilton cycle matching subcubic tree embedding`; fixed-tree/tree-factor literature; and Montgomery's comb/bare-path paper. The linear-forest-plus-matching lemma is elementary and is **not claimed novel**. The frozen-cycle no-go is an R16 method diagnosis, not a source result and not a novelty claim. Montgomery's comb theorem is an explicit baseline and demonstrates that the obstruction is to the rigid architecture, not to comb embeddability.

## 12. Structured `ledger_delta`

```yaml
ledger_delta:
  track: R16
  active_target: H0021
  source_status: OPEN
  research_status: PARTIAL
  metric: Delta_near
  before: 2
  after: 2
  movement: false
  supported_unchanged_count_before: 2
  supported_unchanged_count_after: 3
  stuck_triggered: true
  next_run_mode: STUCK_RECOVERY_1_THINKING_ONLY
  methods_this_run: [5, 13, 21]
  methods_next_recommended: [6, 10, 17]
  new_general_lemma:
    name: subcubic_matching_linear_forest_normal_form
    claim: every subcubic tree is a spanning linear forest plus a matching saturating all degree-3 vertices
    publication_novelty_claimed: false
  new_method_obstruction:
    name: frozen_hamilton_cycle_comb_isolation
    scope: fixed Hamilton cycle plus rigid consecutive comb blocks plus independent G(n,A log n/n) chord graph
    conclusion: fails whp at k asymptotic to beta log n/loglog n for every fixed A,beta>0
    source_counterexample_claimed: false
  selected_recovery_direction: port_Montgomery_connector_Hall_mechanism_to_tree_indexed_subcubic_skeleton
  beck_fiala_refresh:
    bansal_jiang_2508_03961v2: O_sqrt_t_only_for_t_ge_log2_n_with_weaker_small_t_bound
    guo_fang_lu_2609_11189v1: fresh_primary_preprint_claims_full_Komlos_and_3sqrt2pi_t_Beck_Fiala
  shared_roots_edited: false
  peer_files_edited: false
  scheduler_changed: false
  email_or_drive_used: false
```
