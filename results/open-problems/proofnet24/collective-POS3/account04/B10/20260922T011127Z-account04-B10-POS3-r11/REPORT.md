# POS3 account04/B10 — 1/81 pinned-majority-rank atom

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose order probability under the uniform linear-extension law lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14` (unchanged).  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

This is an arbitrary-size width-three argument. It does not replace the source target by a finite census or by a width-two subcase.

## 1. Source-bound state consumed

The current collective allocation supersedes the former benchmark/installation duty for this slot. I used only the following essential state.

1. **Inherited I0122 state.** `operations/claims/I0122.md`, blob `b9dac0d3f56b5119e495fc70f71769100124fc58`, preserves the all-posets finite frontier `n_bal=14` and the universal source target. The later I0122 retirement handoff preserves the transitive strong-majority order reduction and the fact that a hypothetical counterexample has at least five maximal contiguous chain blocks in that order.

2. **OTHER-account result actually applied:** account03/B10, run `account03-B10-20260922T001407Z-pos3-r11`, report blob `388ac28e375df4e7a49f72ffbf540f362e03696e`. It combines the common strong-majority order with Aires–Kahn Theorem 2.6 to prove that every element of a width-at-most-three counterexample has a rank atom pinned to its strong-majority position of at least `1/19683`. In the exact three-chain flux coordinates, this is a lower bound on the central majority-gap cell.

3. **OTHER-account path/flux normal form:** account01/B10, report blob `3a0d4e63665646adc853bb48192eba0f81629a15`. For a fixed three-chain cover, uniform linear extensions are exactly unit-weight paths through the ideal-state lattice; for each element the two other chain-prefix counts give a refined cell `W_x(s,t)`. In a counterexample every relevant one-chain majority-gap marginal exceeds `E/3`.

4. **OTHER-account falsification boundary:** account03/B19, report blob `106c46c118f9863c6fc7867d2ae536dd0786818e`. Connectedness alone does not force a light insertion-slice vector; the unresolved step must use the alignment of heavy slices with the one common strong-majority order.

The designated partner account01/B11 had no completed source-bound collective-POS3 report on `master` in the bounded fresh path check for this run, so I did not wait or fabricate uptake.

External result used below: Max Aires and Jeff Kahn, *Variance vs. range for linear extensions, and balancing extensions in posets of bounded width*, arXiv:2510.26134 (2025), especially their Theorem 2.1 (the multivariate Shepp/XYZ inequality). In probability notation, for a uniform linear extension and fixed `x`,

`Pr(x precedes every y in Y) >= product_{y in Y} Pr(x precedes y)`,

and dually with all elements of `Y` preceding `x`. The same statement applies after conditioning on a consistent collection of order comparisons, since this is the uniform law on the linear extensions of the augmented poset.

## 2. Conditional end-to-end route and the first missing implication

Assume for contradiction that a finite width-at-most-three poset `P` has no balanced incomparable pair. The inherited I0122 argument orients every incomparable pair in its probability-`>2/3` direction and every comparable pair by the poset order. The resulting tournament is transitive, hence gives a total order `L_*` extending `P`.

Fix a three-chain cover. Account01/B10 shows that, at every relevant element/other-chain pair, the insertion-gap marginal selected by `L_*` has mass `>1/3`. Account03/B10 goes one step further and proves that the **joint** cell in the two other chain coordinates is nonzero with the quantitative bound `>=1/19683`.

The first missing implication I attack here is the sharp width-three specialization of that joint-cell step:

> **Candidate implication.** Does the fact that only two chains can contain elements incomparable with a fixed `x` improve the generic width-three `3^{-9}` central-cell bound by removing the order relations that are already forced?

Yes. The correct exponent is at most four, giving `>1/81`.

## 3. A two-sided multivariate XYZ product lemma

### Lemma 3.1

Let `P` be any finite poset, `x in P`, and let `A,B` be finite sets disjoint from `x`. Suppose that for every `a in A` and `b in B`,

`Pr(a < x < b) >= epsilon`.

Then

`Pr(A < x < B) >= epsilon^(|A||B|)`.

Here `A<x<B` means every element of `A` precedes `x` and `x` precedes every element of `B` in the random linear extension.

### Proof

Fix `a in A`. Condition on `a<x`. This conditioning is the uniform linear-extension law of the poset obtained by adjoining the relation `a<x`, so the multivariate XYZ inequality applies there. Hence

`Pr(a<x<B)`

`= Pr(a<x) Pr(x<B | a<x)`

`>= Pr(a<x) product_{b in B} Pr(x<b | a<x)`

`= [product_{b in B} Pr(a<x<b)] / Pr(a<x)^(|B|-1)`

`>= epsilon^|B|`,

because `Pr(a<x)<=1`.

Now condition on `x<B`. In that augmented poset apply the dual multivariate XYZ inequality to the events `a<x`, `a in A`. Writing `q=Pr(x<B)`,

`Pr(A<x<B)`

`= q Pr(A<x | x<B)`

`>= q product_{a in A} Pr(a<x | x<B)`

`= [product_{a in A} Pr(a<x<B)] / q^(|A|-1)`

`>= epsilon^(|A||B|)`,

again because `q<=1`. This proves the claim. `□`

This is the exact product inequality implicitly coarsened to `epsilon^(w^2)` when only the width bounds on the two boundary antichains are retained.

## 4. Width three removes all but two uncertain extrema on each side

Fix `x` and let

`D_x = {y : y precedes x in L_*}`,

`U_x = {y : x precedes y in L_*}`.

Because `L_*` extends `P`, `D_x` is an ideal and `U_x` is a filter. Put

`A=max(D_x)`, `B=min(U_x)`.

As in account03/B10, the event `A<x<B` forces every element of `D_x` before `x` and every element of `U_x` after `x`; equivalently it pins `x` to its `L_*` rank.

Remove from `A` every element already comparable below `x`, and remove from `B` every element already comparable above `x`. Call the remaining sets

`A_0={a in A : a || x}`,

`B_0={b in B : b || x}`.

The removed relations are forced in every linear extension, so

`{A<x<B} = {A_0<x<B_0}`.

Now use width three. `A_0` is an antichain, and no member of `A_0` can lie in the same chain of a fixed three-chain cover as `x`. Therefore it contains at most one element from each of the two other chains:

`|A_0| <= 2`.

Similarly

`|B_0| <= 2`.

For every `a in A_0`, the strong-majority order places `a` before `x`, so

`Pr(a<x)>2/3`.

For every `b in B_0`, it places `x` before `b`, so

`Pr(x<b)>2/3`.

Consequently inclusion-exclusion gives, for every `(a,b) in A_0 x B_0`,

`Pr(a<x<b) >= Pr(a<x)+Pr(x<b)-1 > 1/3`.

Apply Lemma 3.1. If both `A_0` and `B_0` are nonempty,

`Pr(A_0<x<B_0) > (1/3)^(|A_0||B_0|) >= 1/81`.

If one of the two sets is empty, only a one-sided condition remains. The multivariate XYZ inequality directly gives at least the product of at most two probabilities each `>2/3`, hence a bound `>4/9`, which is stronger. If both are empty, the rank is forced with probability one.

We have proved the following arbitrary-size exception lemma.

### Theorem 4.1 — `1/81` pinned-majority-rank atom

If a finite width-at-most-three poset `P` has no balanced incomparable pair, then for every `x in P`, with `r_*(x)` the position of `x` in the common transitive strong-majority order `L_*`,

`Pr(rank_L(x)=r_*(x)) > 1/81`.

Equivalently, if for even one element `x`

`q(x):=max_k Pr(rank_L(x)=k) <= 1/81`,

then `P` already has a `1/3–2/3` balanced incomparable pair.

This improves the previously posted `1/19683` pinned atom by a factor of `243` at the probability threshold.

## 5. Exact transfer to the account01/B10 three-chain flux system

Let `x=c_{a,r}` and let the other two chains be indexed by `b,c`. Let

`g_b(x)=#{y in C_b : y precedes x in L_*}`,

`g_c(x)=#{y in C_c : y precedes x in L_*}`.

With account01/B10's refined flux cell

`W_x(s,t)=sum A(u) B(u+e_a)`

over legal ideal states immediately before adding `x` with the two other coordinates equal to `(s,t)`, one has

`W_x(s,t) = #{linear extensions L : J_b(x)=s, J_c(x)=t}`.

Since the own-chain prefix before `x` is fixed, `rank_L(x)=r_*(x)` iff

`(J_b(x),J_c(x))=(g_b(x),g_c(x))`.

Therefore every hypothetical counterexample satisfies the exact integer inequality

`81 W_x(g_b(x),g_c(x)) > E`,

where `E=e(P)`.

This is the strengthened central-cell constraint to combine with the already-proved marginal constraints

`sum_t W_x(g_b(x),t) > E/3`,

`sum_s W_x(s,g_c(x)) > E/3`

whenever the corresponding other-chain incomparability interval is nonempty.

## 6. What this pays and what remains unpaid

**Paid now:** the first missing exception implication in the bounded-width alignment route is substantially sharpened. In a no-balanced width-three candidate the common-majority central cell cannot merely have tiny positive mass: it must contain more than `1/81` of all extensions for **every element**.

**Not paid:** this does not by itself contradict the simultaneous `>E/3` row/column heavy marginals, connected incomparability, or the inherited at-least-five-block condition. POS3 remains open and `n_bal` remains 14.

The most direct next step is now quantitative: test or prove a signed-flux / consecutive-boundary conservation inequality that cannot coexist with

- `>E/3` in every relevant majority-gap row/column, and
- `>E/81` in every corresponding central cell,

all pinned to the same transitive `L_*`.

This is a materially tighter feasible region than the prior `E/19683` central-cell constraint and is source-valid at arbitrary finite size.

## 7. Computation and provenance

No computation was used to prove Theorem 4.1; there is therefore no code/output artifact to report for the mathematical claim. The proof is symbolic and uses only the source-bound results identified above plus the multivariate XYZ inequality. No search miss is treated as novelty evidence.

No benchmark gold, held-out labels, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive action, paid model/API/Codex call, remote workflow, public posting, permission change, or production-brain mutation was used.
