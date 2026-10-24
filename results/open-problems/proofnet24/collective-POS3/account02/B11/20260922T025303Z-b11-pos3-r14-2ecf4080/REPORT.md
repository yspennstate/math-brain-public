# POS3 account02/B11 — parallel-prime reduction and bi-connected hard core

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent POS3 status:** `OPEN / NOT PROVED`  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`  
**Run:** `20260922T025303Z-b11-pos3-r14-2ecf4080`

## 1. Fresh control and source-bound state

Fresh owner control was resolved from `yspennstate/math-research-brain` main before substantive work. OWNER CONTROL remains revision `2026-09-22.2`; `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` is active; the later stop on new installation/benchmark work remains in force. This slot remains POS3 and no benchmark work was resumed.

The current lead result actually consumed is account04/B10 run
`20260922T011127Z-account04-B10-POS3-r11`, report blob
`1e5a9682e4f90f38484a86e7199428de0b0160f8`. It proves the arbitrary-size
`>1/81` pinned-majority-rank atom in any width-at-most-three no-balanced
candidate, equivalently `81 W_x(g_b(x),g_c(x)) > e(P)` for every element.

The named OTHER-account partner result actually consumed is account03/B19 run
`20260922T020106Z-account03-B19-pos3-r11-a3f7`, handoff blob
`a84d3eccdc76b869801d7a902fceec105ec876f3`. It proves a weighted
boundary-rank-gap conservation law after exact chain deletion and supplies a
349-extension example in which deleting a chain leaves a two-chain remainder
whose *weighted* projection law has no balanced pair, although the parent
poset is rescued by pairs meeting the deleted chain.

The previous account02/B11 route had spent three substantive runs on
autonomous-chain contraction/inflation. In accordance with the collective
method-switch rule, this run changes mechanism: instead of refining the
one-step migration inequality again, it studies the **parallel decomposition
seen by the comparability graph**. This is complementary to the earlier
ordinal decomposition seen by the incomparability graph.

## 2. Conditional end-to-end route and first missing implication

Assume POS3 is false and choose a cardinality-minimal counterexample `P`.

The earlier B11 ordinal-decomposition theorem gives connected
incomparability graph. Width two is already solved, so `width(P)=3`. The lead
adds the `>1/81` pinned-rank atom and the inherited strong-majority block
constraints.

The new theorem below proves something stronger than a merely minimal
reduction:

> **Every** width-at-most-three counterexample, minimal or not, must have
> connected comparability graph.

Thus a cardinality-minimal counterexample is simultaneously indecomposable
under ordinal sum and parallel sum. The genuinely unresolved core is now a
width-exactly-three poset whose comparability **and** incomparability graphs
are connected. Existing module work further says that any remaining proper
autonomous subset must be a chain; the autonomous-chain migration lemma
remains unpaid.

The first structural implication attacked here is therefore:
`Comp(P)` disconnected `=>` POS3 holds under the actual uniform
linear-extension law. It is proved exactly below.

## 3. Uniform shuffle factorization for comparability components

Let `Comp(P)` be the undirected comparability graph of a finite poset `P`.
Suppose its connected components have vertex sets

`V_1,...,V_t`,

and let `P_i=P[V_i]`, `n_i=|V_i|`, `e_i=e(P_i)`.

Because vertices in distinct comparability components have no comparability
edge, **every pair from distinct components is incomparable in `P`**.
Therefore

`P = P_1 || ... || P_t`

is the parallel sum of its induced component posets.

### Lemma 3.1 — exact extension factorization

If `n=sum_i n_i`, then

`e(P) = multinomial(n; n_1,...,n_t) * product_i e(P_i)`.

Moreover a uniform random linear extension of `P` can be sampled exactly by:

1. independently choosing a uniform linear extension `sigma_i` of each `P_i`;
2. choosing uniformly one component-label word with exactly `n_i` copies of
   label `i`;
3. replacing the occurrences of label `i`, in order, by the entries of
   `sigma_i`.

#### Proof

Every linear extension of the parallel sum uniquely determines the internal
word `sigma_i` seen on each component and the component-label shuffle.
Conversely every such tuple is valid, because there are no order relations
between distinct components. Hence this is a bijection

`L(P) <-> (product_i L(P_i)) x Sh(n_1,...,n_t)`,

where the shuffle set has multinomial cardinality. Uniformity on the
Cartesian product gives the sampling statement. `□`

### Corollary 3.2 — internal probabilities are exactly preserved

For `x,y in V_i`,

`Pr_P(x<y) = Pr_{P_i}(x<y)`.

More generally, for any index set `S`, deleting all letters belonging to
components outside `S` from a uniform extension of `P` leaves a **uniform**
linear extension of the parallel sum `||_{i in S} P_i`.

#### Proof

For the first statement, the event depends only on `sigma_i`, which is
uniform and independent of the shuffle. For the second, fix any extension of
the selected parallel sum. The number of ways to choose the omitted internal
extensions and reinsert all omitted component labels depends only on the
component sizes and extension counts, not on the selected extension.
Therefore all selected extensions have equal numbers of global completions.
`□`

This exact marginal statement is important: it uses the genuine uniform law
on `L(P)`. It is not the biased chain-deletion projection used elsewhere in
the campaign.

## 4. Width is additive across comparability components

### Lemma 4.1

For a parallel sum,

`width(P_1 || ... || P_t) = sum_i width(P_i)`.

#### Proof

The union of a maximum antichain from each component is an antichain because
all cross-component pairs are incomparable, giving the lower bound.
Conversely any antichain intersects `V_i` in an antichain of `P_i`, so its
size is at most the sum of the component widths. `□`

## 5. Main theorem — disconnected comparability graph is impossible in POS3 counterexamples

### Theorem 5.1 — parallel-prime reduction

Let `P` be a finite nonchain poset of width at most three. If `Comp(P)` is
disconnected, then `P` has an incomparable pair `x,y` with

`1/3 <= Pr_P(x<y) <= 2/3`.

Consequently **every** counterexample to POS3 has connected comparability
graph.

#### Proof

Let `P_1,...,P_t`, `t>=2`, be the comparability components. By Lemma 4.1,

`sum_i width(P_i) = width(P) <= 3`.

Every nonempty component has width at least one, hence every component has
width at most two.

If some `P_i` is a nonchain, the already-solved width-two theorem gives an
incomparable balanced pair `x,y` inside `P_i`. Corollary 3.2 preserves its
probability exactly in `P`.

It remains to consider the case that every `P_i` is a chain. Select any two
components, say `P_i` and `P_j`. Their parallel sum

`R=P_i || P_j`

is a nonchain of width exactly two, so the width-two theorem gives a balanced
incomparable pair in `R`. By the multi-component marginal part of Corollary
3.2, the relative order distribution on `V_i union V_j` induced from a
uniform extension of `P` is exactly the uniform extension law of `R`.
Therefore the same pair is balanced in `P`.

Both cases contradict counterexample status. `□`

No minimality, finite-size bound, or nonuniform quotient law enters this
argument.

## 6. Combined minimal-counterexample hard core

Combine Theorem 5.1 with the earlier account02/B11 ordinal-factorization
reduction and current collective inputs. If POS3 is false, a
cardinality-minimal counterexample `P` may be taken to satisfy simultaneously:

1. `width(P)=3`;
2. `|P|>=15` from the inherited exact finite frontier through order 14;
3. the incomparability graph is connected;
4. the comparability graph is connected;
5. the common strong-majority order has the inherited at-least-five maximal
   contiguous chain blocks;
6. every element has its strong-majority rank with probability `>1/81`
   by the lead result;
7. all proper autonomous nonchains are excluded by the existing module
   reduction, so any remaining proper autonomous subset is a chain.

Thus the unresolved object is **series- and parallel-indecomposable**. This
does not yet imply full module-primality, because proper autonomous chains are
still possible.

Two immediate graph consequences, useful for the remaining chain-module
branch, are:

- no element is comparable with every other element (that would isolate it in
  the incomparability graph);
- no element is incomparable with every other element (that would isolate it
  in the comparability graph).

For a proper autonomous chain `M`, using the standard partition of the
outside into `D<M`, `I||M`, and `M<U`, the two graph connectivities force

`I != empty` and `D union U != empty`.

So any surviving chain module is active in both complementary graph senses.

## 7. One-step chain deletion stays inside the bi-connected hard class

Let `M={c_1<...<c_m}`, `m>=2`, be a proper autonomous chain in the
minimal hard core, let `x=c_m`, and put `P^-=P-x`.

The previous B11 run proved that `width(P^-)=3` and that the
incomparability graph of `P^-` remains connected. The new parallel-prime
view gives the complementary statement.

### Lemma 7.1

`Comp(P^-)` is connected.

#### Proof

All members of an autonomous chain have the same set of comparable vertices
outside `M`, while the members of `M` are pairwise comparable. Thus in
`Comp(P)` the vertices of `M` form a clique of true twins with respect to
the outside neighborhood.

Since `m>=2`, the vertex `c_{m-1}` survives. Any path in `Comp(P)` that uses
`x` can replace `x` by `c_{m-1}`: every outside neighbor of `x` is also an
outside neighbor of `c_{m-1}`, and every other member of `M` is adjacent to
`c_{m-1}`. Hence deleting `x` cannot disconnect the graph. `□`

Therefore the unresolved **one-step autonomous inflation** problem can be
posed entirely inside the same bi-connected width-three class at both
successive sizes. Proving the earlier migration OR-lemma would eliminate
proper autonomous chains without escaping to a series- or
parallel-decomposable smaller object.

## 8. Named partner result applied: why this theorem cannot be misused after chain deletion

The account03/B19 handoff is an exact boundary test for Theorem 5.1. In its
349-extension example, deletion of `C=(2<5<8)` leaves

`Q=(0<3<6) || (1<4<7)`,

so `Comp(Q)` is disconnected and `Q` is a width-two parallel sum. Under the
**uniform** law on `L(Q)`, Theorem 5.1/width two of course supplies balanced
pairs.

But B19's exact projected law is

`mu_C(tau)=W_C(tau)/e(P)`,

not the uniform law on `L(Q)`. Under that weighted law all six incomparable
pair numerators in `Q` are outside the balanced interval. The parent is
instead rescued by pairs `(2,3)` and `(5,6)` meeting the deleted chain.

Hence the new parallel-prime theorem is fully compatible with the partner's
obstruction and gives a precise rule for future induction:

> Parallel decomposition can be collapsed only when the relevant marginal is
> proven uniform (as in Lemma 3.1/Corollary 3.2). It cannot be imported into a
> chain-deletion remainder merely because that remainder is a parallel sum.

This is a direct application of the named partner result, not a citation-only
mention.

## 9. Exact finite self-check

A standard-library checker enumerated every naturally labelled transitively
closed poset on `2<=n<=6`. For every nonchain of width at most three with
disconnected comparability graph it independently verified:

- the multinomial extension-count factorization;
- exact preservation of every internal incomparable-pair probability;
- existence of a balanced pair in the full poset.

Counts were:

- `n=2`: 1 checked;
- `n=3`: 4 checked;
- `n=4`: 21 checked;
- `n=5`: 135 checked;
- `n=6`: 902 checked.

Total: **1,063** disconnected-comparability width-at-most-three cases, with
zero failures. Across `n=2,...,6` the enumerator saw 5,230 naturally labelled
transitively closed relations.

Terminal marker:

`POS3_PARALLEL_DECOMPOSITION_CHECK_PASS`

SHA-256:
- checker: `0e9dc5fe59c1700e2091ae3a0cd93bdb701ddc139ff75b4c9e56134954851ad8`;
- output: `3dbe6786dabcba605b3ae3979b13fa56c30f5a201611486ed1005eea9362626e`.

This finite computation is a self-check only; Theorem 5.1 is the arbitrary-size
proof and the finite census is not used as closure.

## 10. Status and next mathematical obligation

**Paid this run:** the hard POS3 core is now parallel-indecomposable as well
as ordinally indecomposable; comparability connectivity is proved for every
counterexample, and one-step deletion of a surviving autonomous chain
preserves that connectivity.

**Not paid:** POS3 itself, the autonomous-chain migration OR-lemma, and the
module-prime heavy-slice/central-cell alignment problem remain open.

The clean next structural obligation is one of two genuinely unresolved
branches:

1. prove the one-step autonomous inflation OR-lemma **within the bi-connected
   width-three class**, thereby eliminating all proper autonomous chains; or
2. on the module-prime branch, combine the lead's `>1/81` pinned rank atom
   with the partner's compressed weighted boundary and exact deletion-interface
   charge to force a balanced chain-involving pair.

The next B11 run should not revert to a fourth unchanged binomial-corridor
calculation; it should use the new bi-connected constraint in a separator or
two-graph argument.

## 11. Provenance / safety

No benchmark work, benchmark gold, held-out labels, credentials, scheduler
identifiers, machine paths, raw private transcripts, email, Drive, public
posting, paid model/API/Codex call, remote workflow, permission change, or
brain mutation was used. Old benchmark artifacts remain untouched.

The bounded repository search for an exact pre-existing phrase matching
`connected comparability graph` returned no hit, but this is **not** treated
as a novelty or priority claim.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort:
`maximum actually supported`. Configured/known reasoning effort:
`UNKNOWN / NOT_EXPOSED`. Provider reasoning-token and thinking-time counters:
`null / NOT_EXPOSED`.
