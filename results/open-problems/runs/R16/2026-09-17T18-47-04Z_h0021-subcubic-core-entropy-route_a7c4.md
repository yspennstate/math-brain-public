Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family or reasoning-effort telemetry, so GPT-6/maximum is not claimed. **NO MOVEMENT:** H0021 `Delta_near: 2 -> 2`; supported unchanged count on H0021 `0 -> 1`. Methods actually tried: **#2 ATTACK THE NEGATION FIRST, #4 PROVE SOMETHING WEAKER COMPLETELY, #19 MAKE IT AN ALGORITHM**.

# R16 HARD OUTSIDE — H0021 first substantive run: the subcubic core, a sharp structural scale, and an entropy-first route

Date: 2026-09-17 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Source target: H0021 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Conjecture 1.4.

Status after this run: **OPEN / PARTIAL / ACTIVE HARD OUTSIDE**. The source conjecture is not solved here. The fixed R16 metric does not move.

## 1. Continuity, exclusions, ownership, and current source status

I continued from the actual R16 handoff instead of restarting from the stale native Beck--Fiala title. Before doing mathematics I recovered/read the current campaign/index state, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R16 handoff report, the H0021 intake/queue references, and the create-only exclusive claim `operations/claims/H0021.md`. The claim records R16 as the active exclusive H0021 owner and freezes the metric below.

The newest R16 report handed off I0036 after both permitted hard recoveries and admitted H0021. Therefore I0036 is not reopened here.

A fresh 2026-09-17 primary-source search recovered arXiv:2608.06358v1 and no v2 or later source-matching proof of Conjecture 1.4. The source itself states

\[
G\!\left(n,(1+\varepsilon)\frac{\log n}{n}\right)
\quad\text{is conjectured whp to be }\mathcal T_{n,\Delta}\text{-universal}
\]

for every fixed `epsilon>0` and every integer `Delta>=2`. The same paper proves the conclusion with `C log n/n` for a sufficiently large absolute `C`, and its linking-system result at `psi=1` currently permits a constant below 2000 rather than `1+epsilon`. This remains the baseline, not an R16 result.

The source proof outline is especially relevant here: it works at the structural scale

\[
\alpha=\Theta\!\left(\frac{n\log\log n}{\log n}\right)
\]

and says the hard complementary tree class has `Omega(alpha)` leaves; the technically difficult regime is between `alpha` and `exp(Delta^5) alpha` leaves. For `Delta=3`, the calculation below shows that this `n loglog n/log n` scale is intrinsic to the homeomorphism structure of subcubic trees, not merely an artefact of their general bounded-degree lemma.

I also refreshed the stale Beck--Fiala source comparison. Bansal--Jiang arXiv:2508.03961v2 proves the square-root order when `t>=log^2 n` and a weaker bound below it. A newer primary preprint, Guo--Fang--Lu, arXiv:2609.11189v1, submitted 10 September 2026, explicitly claims the full real Komlos constant `3 sqrt(2 pi)` and hence

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}
\]

for every integer `t>=1`, with no `n` restriction. It is a very recent preprint, so this report does not assert mature refereed consensus; it is nevertheless why the stale Beck--Fiala title is not used to restart old work.

## 2. Frozen metric

The H0021 claim defines

`Delta_near`

as the largest integer `D>=2` for which R16 has a complete source-matching proof that for every fixed `epsilon>0`, whp

\[
G\!\left(n,(1+\varepsilon)\frac{\log n}{n}\right)
\]

contains every `n`-vertex tree of maximum degree at most `D`.

The admitted baseline is

\[
\Delta_{\rm near}=2,
\]

because `T_{n,2}` consists of the spanning path and the Hamilton-path threshold lies below `(1+epsilon) log n/n` for every fixed positive `epsilon`.

After this run,

\[
\boxed{\Delta_{\rm near}=2.}
\]

The first source-valid unresolved milestone remains `Delta_near>=3`. Since this is the first substantive H0021 run after admission, the supported unchanged count is `0 -> 1`, not a fabricated continuation of the old I0036 streak.

## 3. #2 ATTACK THE NEGATION FIRST — what a degree-three counterexample would have to exploit

### 3.1 There is no fixed local-degree obstruction

Put

\[
p=(1+\varepsilon)\frac{\log n}{n}
\]

for fixed `epsilon>0`. For a fixed vertex `v` and fixed `j`,

\[
\Pr(d(v)=j)
={n-1\choose j}p^j(1-p)^{n-1-j}
\le \frac{(np)^j}{j!}\exp(-p(n-1-j)).
\]

For `j<=2`, the union bound over all vertices gives

\[
\Pr(\delta(G)\le2)
\le n^{ -\varepsilon+o(1)} O((\log n)^2)=o(1).
\]

More generally, the same calculation gives `delta(G)>=d` whp for every fixed `d`. Thus a failure of subcubic universality cannot come from a simple shortage of degree-three host vertices. Any counterexample mechanism would have to be global: saturation, simultaneous routing, or the inability to absorb the last `Theta(n loglog n/log n)` vertices.

### 3.2 An exact extremal family pins down the structural scale

There is, however, a clean obstruction to the most obvious *tree-structure* shortcut.

Take any tree core with `L>=3` leaves, no degree-two vertices and maximum degree three. Such a core has

\[
2L-2\quad\text{vertices},\qquad 2L-3\quad\text{edges}.
\]

For an integer `k>=2`, subdivide **every** core edge by exactly `k-2` degree-two vertices. The resulting subcubic tree has

\[
n=(2L-2)+(k-2)(2L-3)
  =2L(k-1)-3k+4,
\tag{3.1}
\]

while every maximal bare path has length exactly `k-1`. Hence it has **no** bare path of length `k`, even though

\[
L=\frac{n+3k-4}{2(k-1)}
  =\left(\frac12+o(1)\right)\frac nk.
\tag{3.2}
\]

For the natural near-threshold routing scale

\[
k\asymp\frac{\log n}{\log\log n},
\]

this is exactly `L=Theta(n loglog n/log n)`, the scale called `alpha` in the source. So a proof of `Delta=3` cannot merely say “few leaves force a bare path of the linking depth.” Uniformly subdivided cubic cores are a concrete family living precisely in the middle regime.

The finite checker described below constructs this family for 36 `(L,k)` cases and verifies (3.1) and the absence of a bare `k`-path exactly.

## 4. #4 PROVE SOMETHING WEAKER, COMPLETELY — exact subcubic core lemmas

The following statements are elementary and are likely folklore in some form. I am not claiming publication novelty. Their value here is that they identify exactly what extra structure `Delta=3` provides beyond the source's general bounded-degree decomposition.

### Proposition R16-H0021-CORE-1 (explicit bare-path packing)

Let `T` be an `n`-vertex tree with maximum degree at most three and exactly `L` leaves. For every integer `k>=1`, `T` contains at least

\[
\boxed{
P_k(T)\ge
\max\!\left\{0,
\left\lceil
\frac{n+3k+2-2(k+1)L}{k+1}
\right\rceil
\right\}
}
\tag{4.1}
\]

pairwise vertex-disjoint bare paths of length `k`.

#### Proof

Let `n_i` be the number of vertices of degree `i`. The tree degree identities give

\[
n_1=L,\qquad n_3=L-2,\qquad n_2=n-2L+2.
\tag{4.2}
\]

Suppress every degree-two vertex. The resulting core is a tree with

\[
E=2L-3
\tag{4.3}
\]

edges. For each core edge `e`, let `r_e` be the number of suppressed degree-two vertices on its corresponding maximal chain. Then

\[
\sum_e r_e=n_2.
\tag{4.4}
\]

Inside that chain, group consecutive degree-two vertices into disjoint blocks of `k+1` vertices. Each full block contains a bare path of exactly `k` edges, and blocks from different core edges are disjoint. Therefore

\[
P_k(T)\ge\sum_e\left\lfloor\frac{r_e}{k+1}\right\rfloor.
\]

Using `floor(x/(k+1)) >= (x-k)/(k+1)` and (4.2)--(4.4),

\[
\begin{aligned}
P_k(T)
&\ge \frac{n_2-kE}{k+1}\\
&=\frac{n-2L+2-k(2L-3)}{k+1}\\
&=\frac{n+3k+2-2(k+1)L}{k+1}.
\end{aligned}
\]

Since `P_k(T)` is a nonnegative integer, (4.1) follows. `QED`.

A useful source-scale corollary is immediate: if

\[
L\le\frac{n}{4(k+1)},
\]

then `T` contains at least `n/(2(k+1))` vertex-disjoint bare `k`-paths, so those paths cover at least `n/2` vertices. Thus, for subcubic trees, the path-rich branch can be certified by an exact linear-time count rather than the much looser general bounded-degree constants.

The uniformly subdivided cores from Section 3 show that the coefficient `n/k` itself is unavoidable: trees with about `n/(2k)` leaves may have no bare `k`-path at all.

### Proposition R16-H0021-CORE-2 (one third of all degree-two mass lies on disjoint maximal chains)

With the notation above, there is a collection of pairwise vertex-disjoint maximal bare chains whose internal degree-two vertices total at least

\[
\boxed{\frac{n-2L+2}{3}}.
\tag{4.5}
\]

#### Proof

The suppressed core is a tree of maximum degree at most three, hence its edges admit a proper three-colouring. Each colour class is a matching. Give a core edge `e` weight `r_e`. The three colour classes partition the total weight `sum_e r_e=n-2L+2`, so one class has weight at least one third of the total. Core edges in one colour class have disjoint endpoints; consequently their corresponding maximal bare chains are vertex-disjoint. `QED`.

This result suggests replacing a single fixed linking depth by a **variable-depth path-system problem**: in every low-leaf subcubic tree one can reserve a vertex-disjoint family of whole maximal chains carrying a constant fraction of the available degree-two mass. The equal-depth requirement, not the absence of disjoint path mass, is the bottleneck.

### Proposition R16-H0021-CORE-3 (homeomorphism entropy bound)

Let `N_{n,L}^{(3)}` be the number of isomorphism classes of `n`-vertex trees with maximum degree at most three and exactly `L>=2` leaves. Then

\[
\boxed{
N_{n,L}^{(3)}
\le 16^L {n-2\choose 2L-4}.
}
\tag{4.6}
\]

#### Proof

After suppressing degree-two vertices, the core has `2L-2` vertices and `2L-3` edges. The number of unlabelled core shapes is at most the number of rooted plane trees on `2L-2` vertices, which is the Catalan number `C_{2L-3}<4^{2L-3}<16^L`.

Fix a core. Reconstructing the original tree amounts to assigning to its `2L-3` edges nonnegative subdivision counts summing to

\[
n-(2L-2).
\]

The number of such weak compositions is exactly

\[
{n-(2L-2)+(2L-3)-1\choose (2L-3)-1}
={n-2\choose 2L-4}.
\]

Multiplying the two upper bounds proves (4.6). `QED`.

Consequently, if

\[
L\le A\frac nk
\]

for a fixed `A` and `k -> infinity`, then

\[
\log\sum_{j\le L}N_{n,j}^{(3)}
=O\!\left(\frac nk\log k\right).
\tag{4.7}
\]

At the source's natural depth `k=Theta(log n/loglog n)`, this is

\[
O\!\left(\frac{n(\log\log n)^2}{\log n}\right)=o(n).
\tag{4.8}
\]

So the genuinely difficult low-leaf subcubic trees form a **subexponential** family of homeomorphism types. This opens a route which is conceptually different from constructing one linking system that supports every permutation: condition out common host defects, obtain a sufficiently strong failure tail for one compressed tree type, then union-bound over the subexponential core/subdivision catalogue.

No such tail estimate is proved in this run; (4.6)--(4.8) only quantify exactly how strong it would need to be.

## 5. #19 MAKE IT AN ALGORITHM — a constructive decomposition and the point where naive absorption fails

### 5.1 Linear-time tree-side procedure

For a given subcubic `T` and target depth `k`, the proofs above are constructive:

1. suppress maximal degree-two chains and record each core-edge weight `r_e`;
2. output the explicit `k`-path blocks from Proposition CORE-1;
3. three-edge-colour the core (a rooted tree permits this greedily in linear time);
4. choose the colour class with largest total `r_e`, yielding the variable-depth chain reservoir of CORE-2;
5. retain the core plus subdivision vector as the canonical compressed description used in CORE-3.

Thus the tree side of the `Delta=3` problem has an honest `O(n)` preprocessing algorithm. It returns either many equal-depth paths or a heavy disjoint family of variable-depth maximal chains, together with a compressed core whose entropy is subexponential in the hard `L=Theta(n/k)` regime.

### 5.2 Why “embed the core, leave the leaves, then match” cannot work at the sharp density

There is a sharp obstruction to the most tempting completion algorithm. Suppose an embedding procedure fixes `L` leaf-parent images `P` and reserves `L` unused vertices `R`, and only then exposes fresh cross edges between `P` and `R`. Even in the favourable case of `L` distinct parents, this final graph is a fresh `G(L,L,p)`.

Take

\[
L=c\frac nk,
\qquad
k=\Theta\!\left(\frac{\log n}{\log\log n}\right),
\qquad
p=(1+\varepsilon)\frac{\log n}{n}.
\]

For each `r in R`, the probability that `r` is isolated from `P` is

\[
q=(1-p)^L
   =\exp(-(1+o(1))pL)
   =(\log n)^{-\Theta(1)}.
\]

The isolation events for distinct vertices of `R` use disjoint edge sets, so the number of isolated vertices is exactly binomial with mean

\[
Lq
=\frac{\Theta(n\log\log n)}{\log n}\,(\log n)^{-\Theta(1)}
\longrightarrow\infty.
\]

Hence this fresh fixed-parent/fixed-reservoir final matching fails whp. This is **not** a counterexample to H0021: a successful embedding algorithm may choose parent images and reservoirs adaptively, use paths rather than single edges, or maintain absorbing sets throughout the embedding. It does certify why the source needs matchmaking/rollback machinery precisely at the `n loglog n/log n` scale.

### 5.3 New route retained from this run

The most promising route I found is therefore **homeomorphism entropy + conditional tail**, not another attempt to optimise the source's large constant `C` directly.

For the low-leaf window `L<=A n/k`, CORE-3 shows only

\[
\exp\!\left(O\!\left(\frac nk\log k\right)\right)
\]

isomorphism types. A sufficient next theorem would be the following stronger fixed-type statement.

> Find a single high-probability host event `H_n`, independent of the tree type, such that for every subcubic `T` with `L(T)<=A n/k`,
> \[
> \Pr(T\not\subseteq G\mid H_n)
> \le
> \exp\!\left(-\omega\!\left(\frac nk\log k\right)\right).
> \tag{5.1}
> \]

Then (4.7) and a union bound give simultaneous universality over the whole low-leaf class. Conditioning is essential: unconditionally, the common event that `G` has an isolated vertex has only polynomially small probability at `(1+epsilon) log n/n`, so no per-tree exponentially small failure estimate can hold without first removing such common host obstructions.

This route avoids paying for a universal all-permutations linking system if one can obtain a strong tree-specific embedding tail after compression. Whether (5.1) is attainable is the central question for the next run.

## 6. Exact finite self-check

Only after the structural route was identified did I write an exact finite checker:

`artifacts/R16/2026-09-17T18-47-04Z_h0021_subcubic_core_checker.py`

creation commit:

`5aa0179397941b073d7b278614f441b1eee83514`

Executed output:

`artifacts/R16/2026-09-17T18-47-04Z_h0021_subcubic_core_checker.out`

creation commit:

`b4f9d2926a72fa96527415f54d5d534d8a455e19`

The checker uses exact graph combinatorics/integer comparisons. It exhaustively checks every unlabelled subcubic tree through `n=14` (552 such trees at `n=14`) for the explicit CORE-1 packing for all tested `k<=6`, verifies the one-third weighted matching bound, and checks 36 uniformly subdivided-core obstruction instances. The archived output is:

```
subcubic_unlabeled_counts_n2_to_n14 = {2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 6, 8: 11, 9: 18, 10: 37, 11: 66, 12: 135, 13: 265, 14: 552}
tree_k_pairs_checked = 6577
uniform_subdivision_obstruction_cases = 36
ALL_EXACT_CHECKS_PASS
```

This is a **self-check**, not an independent audit. The proofs of CORE-1--3 are on the page and do not depend on the computation.

## 7. Prior-art and nearest solved results

The fresh source/literature check used the exact H0021 paper, author/title queries, and later-result queries on 2026-09-17. No later proof of Conjecture 1.4 was recovered. This is a bounded search, not a worldwide novelty certificate.

Two older sharp-density results are important boundaries:

- Hefetz--Krivelevich--Szabo (2012) prove the sharp density for a **given** bounded-degree spanning tree when it has linearly many leaves or a linear bare path. Their theorem is not simultaneous universality over all subcubic trees.
- Montgomery (arXiv:1405.6560, 2014) proves the sharp density for combs and a broader family including bounded-degree trees with many disjoint very long bare paths. This is a baseline, not the `Delta=3` universality theorem sought here.

The 2026 source explicitly says that even the corresponding fixed-tree hitting-time question remains open for trees with few leaves and without a linear bare path. Thus the hard family isolated above is not being declared solved by prior fixed-tree results.

The combinatorial CORE-1--3 mechanisms themselves are elementary; no novelty claim is made for them. The research contribution of this run is the **route synthesis**: for `Delta=3`, suppressing degree-two vertices exposes an exact `n/k` hard scale, a subexponential low-leaf type entropy, and a concrete reason naive last-step leaf matching fails at the same scale.

## 8. Outcome and next methods

Metric outcome:

`Delta_near: 2 -> 2` — **no movement**.

What did move conceptually:

- the source's `alpha = Theta(n loglog n/log n)` bottleneck is now derived exactly from the subcubic homeomorphism core;
- an explicit uniformly subdivided cubic-core family shows the scale is real;
- all low-leaf subcubic types at that scale form a subexponential catalogue;
- the tree-side decomposition is constructive in linear time;
- a fresh fixed-parent/fixed-reservoir leaf matching is proved to fail whp at exactly that scale;
- the surviving route is a conditional fixed-type failure estimate strong enough to union-bound over the compressed catalogue, potentially bypassing a fully universal linking system.

The next H0021 triple must differ from `#2,#4,#19`. I record:

- **#3 PROVE SOMETHING STRONGER:** target the conditional tail (5.1), which is stronger than mere fixed-tree whp embedding but self-feeds through the entropy bound;
- **#11 DUALIZE:** rewrite the compressed-core embedding as a prescribed-length path-factor / flow problem and look for a Hall-type obstruction whose bad witnesses can be union-bounded uniformly;
- **#24 FIND THE EXTREMAL OBJECT:** focus first on uniformly subdivided cubic cores, which sit at `L~n/(2k)` with all maximal bare segments just below the natural linking depth.

This is unchanged run 1 on H0021, so no stuck recovery is triggered.

## 9. Model/scheduler-control status requested by the owner

The situation is still exactly the one recorded in the controlling repository policy. The exposed task-mutation surface supports title/prompt, schedule or relative start, timing mode and enablement, but **does not expose a model-family selector or a reasoning-effort selector**. GPT-6/maximum can therefore be requested in prompt text only; actual execution requires authenticated product/workspace telemetry to verify it.

The repository's current reconciliation also distinguishes the historical P26 permission failure from a later successful P26 update in another authorised context. For any task returning `You cannot modify this task`, the compliant workaround is to use the task's owning account/workspace context or platform support. Permission bypass and duplicate scheduling are not acceptable substitutes. No scheduler state was changed in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R16
  allocation: HARD_OUTSIDE
  target: H0021
  source: Cohen_Antonir_Lichev_Zhukovskii_arXiv_2608.06358v1_Conjecture_1.4
  metric: Delta_near
  before: 2
  after: 2
  movement: false
  supported_unchanged_count_before: 0
  supported_unchanged_count_after: 1
  status: OPEN_PARTIAL_ACTIVE
  methods: [2, 4, 19]
  new_complete_results:
    - subcubic_bare_path_packing_formula_CORE_1
    - one_third_degree2_mass_disjoint_maximal_chains_CORE_2
    - subcubic_homeomorphism_entropy_bound_CORE_3
  finite_obstruction:
    - uniformly_subdivided_cubic_cores_have_L_asymptotic_n_over_2k_and_no_bare_k_path
    - fresh_fixed_parent_fixed_reservoir_leaf_matching_fails_at_L_Theta_n_over_k
  next_route: conditional_fixed_type_tail_plus_homeomorphism_entropy
  next_methods: [3, 11, 24]
  exact_self_check: PASS
  closure: false
  audits_required: [P26, second_other_track]
```

No shared root ledger, peer file, email, Drive content, public post, purchase, permission, workflow, or scheduler state was changed.
