# PROB10-04 idea before code — global-max flip sets and the first genuinely extensive radius-3 obstruction

Model fixed throughout: classical iid proper random 3-SAT, `m=floor(alpha n)`, three distinct variables per clause, independent uniform signs.

Source metric remains the verified explicit bracket `[3.52,4.4898]`, width `0.9698`. Nothing below is counted as endpoint movement until it is inserted rigorously into the current best first-moment/configuration bound.

## New route

Instead of another clause-local weight, choose, for every satisfiable formula, a satisfying assignment `sigma` of **maximum Hamming weight**. This is a legitimate canonical representative of the whole solution set, stronger than taking a maximum only inside one connected component. Every finite-radius improving flip pattern is therefore forbidden.

Relative to `sigma`, let a clause be *critical for v* if the literal on `v` is its unique true literal. A variable is *flippable* if it has no critical clause.

The first potentially extensive obstruction occurs at Hamming radius 3, not radius 2. A typical radius-3 pattern is one one-variable `y` flipped `1->0` followed by two zero-variables flipped `0->1`. If `y` is flippable and the unique blocker of a zero `x` contains the false literal `not y`, then `y` is a potential *rescuer* of `x`. In the naive picture, two such leaves at one center `y` would give an augmenting path and hence a capacity-one condition on rescuer incidences.

Before using that condition in a count, attack its negation: it is **not deterministically valid**. New blockers can be created after earlier flips. The smallest counterexample found in the negation search has four variables and four clauses (written as signed literals, `-i` meaning `not x_i`):

```
(-0,-1,-3)
(+0,-2,-3)
(+1,-2,-3)
(-1,-2,+3)
```

For `sigma=(1,1,0,0)`, variables `2` and `3` each have exactly one critical blocker, variable `1` is flippable, and both unique blockers contain `not x_1`. The satisfying component containing `sigma` has maximum Hamming weight `2`, attained by `sigma`; flipping `1` down and then either `2` or `3` up stays satisfying, but flipping both leaves up makes clause `(+1,-2,-3)` false. Thus the naive implication “two rescued leaves at one flippable center force a weight-improving path” is false.

## Exact clause-level reformulation

For any satisfying assignment `sigma`, and any clause `C`, let `T_C` be the variables whose literals are true under `sigma` and `F_C` the variables whose literals are false under `sigma`. For a flip set `S`, the endpoint assignment `sigma^S` satisfies `C` iff

`(T_C \ S) union (F_C intersect S)`

is nonempty. Equivalently,

`T_C subset S  =>  F_C intersect S != empty`.

This identity is exact and exposes why the naive rescue-star argument fails: a clause with all three literals initially true can become false after all three corresponding variables are flipped, even though no variable was critical initially.

For a path, every prefix `S_j` of the flip order must satisfy the same implication. Hence radius-3 augmentation is a finite signed-hypergraph accessibility problem, not merely an occupancy problem on unique blockers.

## Scale separation to exploit

The old radius-1 condition (each zero blocked) is already the “single-flip / positively-prime” condition used in the 4.4898 upper-bound line. Radius-2 mutual-rescue patterns require two specified blocker incidences and occur only at `O(1)` scale in the naive conditioned model. Radius-3 one-down/two-up patterns create `Theta(n)` potential rescuer incidences and therefore are the first finite-radius correction capable of changing a first-moment exponent.

This suggests a precise next analytic object: extend the Diaz–Kirousis–Mitsche–Perez-Gimenez configuration polytope by a finite set of radius-3 accessibility types, rather than trying to divide a solution count by an ad hoc cluster-ball size.

## Exact missing lemma for source progress

A useful source-level advance would follow from a uniform exponential counting lemma of the following form.

For every admissible typical degree/configuration tuple in the 4.4898 proof, refine the tuple by the radius-3 signed-hypergraph incidence types above. Let `N_1(x)` be the old single-flip count contribution and `N_3(x)` the number of assignments that are also free of every Hamming-weight-improving feasible flip path of length at most 3. Prove, uniformly over the source polytope near its maximizing set, that

`N_3(x) <= exp(-eta n + o(n)) N_1(x)`

for some explicit `eta>0`, while preserving all typicity/unbalancing reductions. Then rerun the finite-dimensional maximization and check whether the resulting exponent is already negative below `alpha=4.4898`.

The crucial point is uniformity near the actual maximizing type. A Poisson heuristic for rescue-star collisions is not enough, and the false deterministic capacity-one shortcut above must not be used.

## Three approaches compared this run

1. **Full-component quotient second moment.** Exact same-component cancellation remains valid, but no usable lower bound on `E Q` plus cross-component second moment was obtained; this route still owes the same nonlocal kernel.
2. **Global-max / radius-3 accessibility.** New progress: exact flip-set clause identity, an explicit counterexample killing the naive star-capacity lemma, and a source-compatible missing exponential-penalty lemma.
3. **Whitening/core compression.** Maneva–Sinclair's `4.453` core result is not an UNSAT bound; using it would require a new theorem that coreless whitening histories admit a uniformly cheaper representative count. No such theorem was obtained here.

No source endpoint is changed by this idea note.