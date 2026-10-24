# POS3 account03/B10 — pinned majority-rank atom from bounded-width balancing

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent status:** **OPEN / NOT PROVED**  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## Exact state consumed

The current owner allocation supersedes this slot's former benchmark role and assigns account03/B10 to apply bounded-width/high-variance results to the width-three 1/3–2/3 target.

I consumed two exact other-account results:

- account02/B11, report blob `b71c5087c4982769946c31f1ec76242bf297fe17`: incomparability components are ordinal-sum factors, so a cardinality-minimal counterexample may be assumed incomparability-connected. Together with inherited state, the unresolved core has width exactly three, at least 15 elements, and at least five maximal contiguous blocks in the strong-majority order.
- account01/B10, report blob `3a0d4e63665646adc853bb48192eba0f81629a15`: exact three-chain ideal-state encoding, insertion-flux formula, and heavy-slice normal form. In a counterexample, every relevant strong-majority insertion gap carries more than one third of all extensions.

The named partner account04/B11 had no source-bound collective-POS3 artifact in the shared handoff/archive snapshot available during this run, so no partner result is fabricated.

The external input used below is Aires–Kahn, *Variance vs. range for linear extensions, and balancing extensions in posets of bounded width*, arXiv:2510.26134. I use its bounded-width local lemma: if `P={x} ⊔ D ⊔ U`, `D` is an ideal, `U` a filter, `A=max(D)`, `B=min(U)`, `|A|,|B|<=w`, and `Pr(a<x<b)>=epsilon` for every `a in A,b in B`, then `Pr(A<x<B)>=epsilon^(w^2)`.

## Strong-majority cuts are ideal/filter cuts

Assume `P` is a width-at-most-three counterexample. The inherited I0122 result gives a transitive strong-majority total order `L_*` extending `P`.

Fix `x` and define

`D_x={y: y precedes x in L_*}`,  `U_x={y: x precedes y in L_*}`.

Since `L_*` extends `P`, `D_x` is an ideal and `U_x` a filter. Put `A_x=max(D_x)` and `B_x=min(U_x)`. Both are antichains, hence have size at most three.

For every `a in A_x`, either `a<x` in `P`, so `Pr(a<x)=1`, or `a||x`, so the strong-majority orientation gives `Pr(a<x)>2/3`. Similarly every `b in B_x` satisfies `Pr(x<b)>2/3` (or equals one). Therefore

`Pr(a<x<b) >= Pr(a<x)+Pr(x<b)-1 > 1/3`

for every `a in A_x,b in B_x`.

## Pinned majority-rank atom lemma

**Lemma.** Let `P` be a width-at-most-three poset with no balanced incomparable pair, and let `L_*` be its transitive strong-majority order. For every `x`, if `r_*(x)` is the position of `x` in `L_*`, then for a uniformly random linear extension `L`,

`Pr(position_L(x)=r_*(x)) >= 3^(-9) = 1/19683`.

**Proof.** Suppose first that `D_x,U_x` are both nonempty. Apply the Aires–Kahn lemma with `w=3` and `epsilon=1/3`. The preceding inequalities verify the hypotheses, giving

`Pr(A_x<x<B_x) >= (1/3)^9 = 1/19683`.

On `A_x<x`, every `d in D_x` precedes `x`: extend `d` upward inside the finite ideal `D_x` to some maximal `a in A_x`, then `d<=a<x`. Likewise `x<B_x` forces `x<u` for every `u in U_x`. Hence exactly the `|D_x|` elements preceding `x` in `L_*` occur before `x`; equivalently `x` has rank `r_*(x)`.

If `D_x` is empty, `x` is first in `L_*`. For every `b in B_x`, `Pr(x<b)>2/3`. The Shepp/XYZ inequality used in the Aires–Kahn argument gives

`Pr(x<B_x) >= product_{b in B_x} Pr(x<b) > (2/3)^|B_x| >= (2/3)^3=8/27`,

which is stronger than `1/19683` and forces `x` first. The case `U_x` empty is symmetric. ∎

Thus if `q(x)=max_k Pr(position_L(x)=k)` is below `1/19683` for even one element of a width-at-most-three poset, the poset already has a balanced pair. More strongly, in a counterexample the guaranteed atom is pinned to the rank prescribed by the *common* strong-majority order for every `x`.

## Exact transfer to the three-chain flux system

Fix a chain partition `C_1 ⊔ C_2 ⊔ C_3=P` and use account01/B10's exact path notation. Let `x=c_{a,r}` and let `b,c` be the other chain indices. Define the refined flux

`W_x(s,t)=sum A(u)B(u+e_a)`

over legal ideal states immediately before adding `x` with `u_a=r-1,u_b=s,u_c=t`.

Then `W_x(s,t)` counts exactly the extensions having `J_b(x)=s` and `J_c(x)=t`. Let

`g_b(x)=#{y in C_b: y precedes x in L_*}`,  `g_c(x)=#{y in C_c: y precedes x in L_*}`.

Because `L_*` extends each chain, `x` has its `L_*` rank iff `(J_b,J_c)=(g_b,g_c)`. Writing `E=e(P)`, the lemma gives the new **central-cell constraint**

`W_x(g_b(x),g_c(x)) >= E/19683`                                      (1)

for every `x` in a hypothetical counterexample.

Account01/B10 already gives the marginal heavy-slice constraints: whenever `x` has an incomparable element in `C_b`,

`sum_t W_x(g_b(x),t) > E/3`,

and analogously for `C_c`. Equation (1) is a genuine strengthening: large row and column sums alone do not force mass at their intersection.

## Updated unresolved core

Any cardinality-minimal width-three counterexample must now simultaneously have:

1. width exactly three;
2. at least 15 elements;
3. connected incomparability graph;
4. at least five maximal contiguous blocks in the common strong-majority order;
5. every relevant strong-majority insertion-gap marginal greater than `E/3`;
6. for every element, the joint majority-gap cell in the two other chain coordinates at least `E/19683`.

This does **not** close POS3. The sharpened next implication is to show that signed flux-conservation across consecutive boundaries of the one common strong-majority order is incompatible with the simultaneous `>E/3` heavy marginals and `>=E/19683` pinned central atoms, under connected width three and at least five majority blocks; or construct a genuine poset realizing the full system and extract the missing invariant.

The account03/B19 exact 9-element certificate already refutes the stronger shortcut that connectedness alone forces some relevant insertion distribution to have every slice at most `E/3`, so that shortcut is not revived.

No benchmark answer, held-out label, key, FEI proof material, credentials, scheduler identifier, machine path, email, Drive action, paid model/API/Codex call, remote workflow or public release was used. No novelty or priority claim is made.
