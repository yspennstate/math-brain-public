# POS3 fleet02/B11 — ordinal-sum reduction to the incomparability-connected core

**Outcome:** ESSENTIAL_STEP_APPLIED (target remains open).

## Scope

Target: every finite nonchain poset of width at most three has an incomparable pair `x,y` with

`1/3 <= Pr(x precedes y) <= 2/3`

under the uniform law on all linear extensions.

This run implements the assigned minimal-counterexample / ordinal-decomposition reduction. The named partner fleet03/B19 had no source-bound collective POS3 handoff in the traced authorized archive at the start snapshot, so I used the inherited I0122 strong-majority-block result as the complete compatible prior state and reconstructed the missing reduction directly.

## New theorem: exact ordinal factorization by incomparability components

Let `Inc(P)` be the graph on the elements of a finite poset `P` in which two vertices are adjacent exactly when they are incomparable. Let its connected components be `C_1,...,C_t`.

### Lemma 1 — distinct incomparability components are uniformly comparable

For any two distinct components `C,D`, exactly one of the following holds:

* every `c in C` satisfies `c<d` for every `d in D`, or
* every `d in D` satisfies `d<c` for every `c in C`.

**Proof.** Every cross-component pair is comparable, since an incomparable cross pair would be an edge joining the components. Fix `c in C`, `d in D`; suppose `c<d`. If `c'` is adjacent to `c` in `Inc(P)`, then `c'` and `d` are comparable. We cannot have `d<c'`, because then `c<d<c'`, contradicting `c || c'`. Hence `c'<d`. Propagating along an incomparability path shows every element of `C` lies below `d`.

Now fix any `c' in C`. If `d'` is adjacent to `d` in `Inc(P)`, then `c'` and `d'` are comparable. We cannot have `d'<c'`, because then `d'<c'<d`, contradicting `d || d'`. Hence `c'<d'`. Propagating along a path in `D` gives `C<D` pointwise. The case `d<c` is symmetric. ∎

The induced comparison relation on the components is therefore a total order. Relabel so

`C_1 < C_2 < ... < C_t`

pointwise. Thus

`P = C_1 ⊕ C_2 ⊕ ... ⊕ C_t`

is an ordinal sum.

### Lemma 2 — uniform linear extensions factor exactly

Every linear extension of `P` is uniquely a concatenation

`L_1 L_2 ... L_t`, with `L_i in L(C_i)`.

Consequently

`e(P) = product_i e(C_i)`.

Moreover, every incomparable pair lies inside one component, and for `x,y in C_i` with `x || y`,

`Pr_P(x precedes y) = Pr_{C_i}(x precedes y)`.

**Proof.** Lemma 1 forces every element of `C_i` before every element of `C_j` when `i<j`, while the order within each component may be any linear extension of that induced subposet. Hence concatenation is a bijection from the Cartesian product of component extension sets onto `L(P)`. Uniform counting then gives the displayed probability identity. ∎

Define

`b(P) = max_{x || y} min(Pr_P(x<y), 1-Pr_P(x<y))`.

For a nonchain poset, Lemma 2 yields the exact identity

`b(P) = max_{i: |C_i|>1} b(C_i)`.

### Corollary 3 — exact reduction of POS3

A finite poset `P` is a counterexample to the 1/3–2/3 assertion if and only if every nontrivial incomparability component `C_i` is itself a counterexample. Width does not increase on induced subposets. Therefore proving POS3 for width-at-most-three posets whose incomparability graph is connected proves POS3 in full.

In particular, any cardinality-minimal POS3 counterexample must have connected incomparability graph (equivalently, be ordinally indecomposable under nontrivial ordinal sum).

## Combination with inherited exact state

The inherited I0122 work proves that any source counterexample has a transitive strong-majority order and at least five maximal contiguous chain blocks in that order. The inherited finite frontier certifies all nonchains through 14 elements. Width two is already a known solved regime in the current source package.

Hence any size-minimal counterexample to the present width-three target must simultaneously satisfy:

1. width exactly three;
2. at least 15 elements;
3. connected incomparability graph / no nontrivial ordinal-sum decomposition;
4. at least five maximal contiguous chain blocks in its strong-majority order.

This is a strictly smaller unresolved core and is the reduction needed before attempting chain deletion/insertion: ordinal factors can now be removed without ever pretending that a biased induced extension law is uniform.

## Exact finite self-check

A standard-library exhaustive checker was run over every distinct transitively closed relation compatible with the natural order on `n<=6` (every finite poset admits such a labeling via a linear extension). After deduplication the counts by `n=1,...,6` were

`1, 2, 7, 40, 357, 4824`,

for `5231` relations total. For every relation the checker verified:

* the component comparison direction in Lemma 1 is uniform;
* `e(P)=product_i e(C_i)` by exact integer dynamic programming.

Output: `5231 checked; 0 failures`.

A separate exact probability check on all `407` deduplicated relations through `n<=5` verified

`b(P)=max_i b(C_i)`

with `0` failures. These are self-checks of the proof, not substitutes for it.

## What remains

The target is not solved. The next essential step should work entirely inside the connected-incomparability, width-exactly-three, at-least-five-majority-block core. A promising route is to combine a three-chain cover with the inherited reverse-boundary-event cover and prove that connectedness forces enough overlap among boundary-reversal events to contradict every reverse probability being `<1/3`. Any deletion/insertion recurrence must retain exact multiplicity weights rather than replace the induced law by a uniform one.

No benchmark data, held-out labels, solver answers, production keys, private transcripts, or unrelated material were used.
