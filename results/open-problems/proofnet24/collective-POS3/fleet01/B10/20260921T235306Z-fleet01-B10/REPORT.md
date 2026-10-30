# POS3 fleet01/B10 — exact three-chain path flux and the heavy-slice normal form

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** width-at-most-three `1/3–2/3` balanced-pair conjecture  
**Assigned subproblem:** develop a three-chain lattice-path encoding that retains exact extension multiplicities, then derive the candidate balanced-pair inequality under the actual uniform law.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

No benchmark validation and no FEI audit were performed in this run. The later owner allocation superseded the stale benchmark prompt and assigned this slot to POS3.

## 1. Source-bound state consumed

I used the current collective POS3 target together with two exact prior results.

1. **Named other-account result consumed:** `fleet02/B11`, commit
   `8a4f5bf21872cbcfbc38433903f60a1f25faacdf`, file
   `proofnet24/collective-POS3/fleet02/B11/20260921T235736Z-b11-44e20585/REPORT.md`.
   It proves exact ordinal factorization by incomparability components. Hence a cardinality-minimal POS3 counterexample may be assumed to have connected incomparability graph. Combining the inherited frontier and majority-order facts, the unresolved core has width exactly three, at least 15 elements, connected incomparability graph, and at least five maximal contiguous chain blocks in the strong-majority order.

2. The same-account neighboring B19 report, commit
   `61e199cb10e0ef8a5ea86f03b0a1404b0c6f632e`, proves an exact chain insertion/deletion recurrence and, crucially, shows that deleting a chain induces a weighted rather than uniform law on extensions of the remainder. I use its lesson below but derive a different state-space representation in which the third-chain multiplicity is retained automatically.

I also used the inherited I0122 strong-majority fact: if no balanced pair exists, orient every incomparable pair in its probability-`>2/3` direction and every comparable pair by the poset order. The resulting tournament has no directed triangle and therefore is a transitive total order extending the poset.

## 2. Exact three-chain ideal-state encoding

Let `P` have width at most three. Fix a chain partition

`C_1 ⊔ C_2 ⊔ C_3 = P`,

allowing an empty chain when the width is smaller, and write

`C_r = (c_{r,1} < ... < c_{r,m_r})`.

For a state `u=(u_1,u_2,u_3)` with `0<=u_r<=m_r`, define

`I(u) = {c_{r,j}: 1<=j<=u_r, r=1,2,3}`.

Let

`Omega = {u : I(u) is an order ideal of P}`.

Every order ideal meets each `C_r` in a prefix, so `u -> I(u)` is a bijection from `Omega` to the ideal lattice `J(P)`.

Put a directed edge

`u -> u+e_r`

when both endpoints lie in `Omega`. This edge adds exactly the next unused element `c_{r,u_r+1}` of chain `C_r`.

### Theorem 2.1 — linear extensions are exactly the admissible 3D paths

There is a bijection

`L(P) <-> {directed paths in Omega from (0,0,0) to (m_1,m_2,m_3)}`.

**Proof.** A linear extension exposes a nested sequence of order ideals, one after each prefix. Recording the three chain-prefix lengths gives a directed path in `Omega`. Conversely, each path adds one currently legal next element at every step, hence spells a linear extension. The constructions are inverse. ∎

This is the point at which the full third-chain multiplicity is retained: each complete 3D path has weight exactly one, so the uniform law on linear extensions is literally the uniform law on complete admissible paths.

Define forward and backward path counts

`A(u) = # paths 0 -> u`,

`B(u) = # paths u -> m`,

where `m=(m_1,m_2,m_3)`. They satisfy the exact recurrences

`A(0)=1`,

`A(u)=sum_r A(u-e_r)` over legal predecessor states,

and

`B(m)=1`,

`B(u)=sum_r B(u+e_r)` over legal successor states.

Therefore

`E := e(P) = A(m) = B(0)`.

The state space has at most `(m_1+1)(m_2+1)(m_3+1)` points, so for a fixed chain cover all counts are obtained by an `O(m_1 m_2 m_3)` state dynamic program up to a constant factor.

## 3. Exact edge-flux formula for every cross-chain comparison

Fix

`x = c_{a,r}`

and another chain `C_b`. For `0<=t<=m_b`, define the `x`-edge flux through `C_b`-level `t` by

`W_{x,b}(t)`

`= sum A(u) B(u+e_a)`,

where the sum is over states `u in Omega` satisfying

`u_a=r-1`, `u_b=t`, and `u+e_a in Omega`.

Equivalently, the third coordinate and any remaining coordinate are summed out exactly.

### Theorem 3.1 — flux equals the exact insertion-slice count

Let `J_b(x)` be the number of elements of `C_b` that precede `x` in a uniformly random linear extension. Then

`W_{x,b}(t) = #{L in L(P): J_b(x)=t}`,

and consequently

`sum_t W_{x,b}(t)=E`.

**Proof.** Every extension has a unique edge at which `x` is added. Immediately before that edge, the `b`-coordinate is exactly `J_b(x)`. For a fixed edge `u->u+e_a`, the number of complete paths using it is `A(u)B(u+e_a)`. Summing over the edges with `u_b=t` proves the claim. ∎

Now let

`y = c_{b,s}`

be incomparable with `x`. At the instant `x` is added, `x` precedes `y` exactly when fewer than `s` elements of `C_b` have already appeared. Therefore

`#{L: x precedes y} = sum_{t=0}^{s-1} W_{x,b}(t)`

and

`Pr(x precedes y) = E^{-1} sum_{t<s} W_{x,b}(t)`.

Hence the requested width-three balance statement is, for this fixed chain partition, **exactly** the following path-flux statement:

> There exist distinct chains `a,b`, an element `x=c_{a,r}`, and an incomparable `y=c_{b,s}` such that
>
> `E/3 <= sum_{t<s} W_{x,b}(t) <= 2E/3`.

Every incomparable pair belongs to two distinct chains, so this is not merely sufficient: it is an exact reformulation of POS3 for the chosen chain partition.

## 4. Incomparability intervals and a proved anti-concentration certificate

Fix `x` and `C_b`. Because `C_b` is a chain, the elements of `C_b` incomparable with `x` form a contiguous interval. Write

`ell = #{c in C_b : c < x}`

and

`u = #{c in C_b : not (x < c)}`.

Then `J_b(x)` is supported on `ell,...,u`, and the incomparable elements are exactly

`c_{b,ell+1},...,c_{b,u}`.

Put

`F(s) = E^{-1} sum_{t<s} W_{x,b}(t) = Pr(x precedes c_{b,s})`.

Thus `F` is a nondecreasing cumulative flux with the exact boundary values

`F(ell)=0`, `F(u+1)=1`.

### Corollary 4.1 — one-chain anti-concentration certificate

If

`W_{x,b}(t) <= E/3`

for every `t=ell,...,u`, then some incomparable `c_{b,s}` is balanced with `x`.

**Proof.** Starting at `0` and ending at `1`, the cumulative sum cannot jump over the entire interval `[1/3,2/3]` if every increment is at most `1/3`. Any first crossing of `1/3` therefore lands at or below `2/3`, and its cut corresponds to an incomparable element. ∎

This gives a concrete sufficient certificate under the actual full extension law. In particular a hypothetical counterexample must exhibit a large insertion slice for every cross-chain incomparability interval.

## 5. Heavy-slice normal form for a hypothetical counterexample

Assume `P` has **no** balanced incomparable pair. Let `L_*` be its transitive strong-majority order from the inherited I0122 result.

For fixed `x` and `C_b`, let

`g_b(x) = #{c in C_b : c precedes x in L_*}`.

### Theorem 5.1 — every incomparable chain interval has a unique forbidden-band crossing

If `x` is incomparable with at least one element of `C_b`, then

`sum_{t<g_b(x)} W_{x,b}(t) < E/3`,

`sum_{t<=g_b(x)} W_{x,b}(t) > 2E/3`,

and therefore

`W_{x,b}(g_b(x)) > E/3`.

Equivalently,

`Pr(J_b(x)=g_b(x)) > 1/3`.

**Proof.** For each incomparable `c_{b,s}`, the counterexample assumption says `F(s)` lies outside `[1/3,2/3]`. Since `F` is nondecreasing, begins at `0` and ends at `1`, there is a unique index at which the cumulative value passes from `<1/3` to `>2/3`. The jump has mass greater than `1/3`.

Moreover, if `F(s)<1/3`, then `Pr(c_{b,s} precedes x)>2/3`, so the strong-majority order places `c_{b,s}` before `x`. If `F(s)>2/3`, it places `x` before `c_{b,s}`. Hence the crossing index is exactly the number `g_b(x)` of `C_b` elements preceding `x` in `L_*`. ∎

This is the main structural reduction of the run. A minimal width-three counterexample in the fleet02/B11 connected core must support these `>E/3` heavy edge-flux slices simultaneously throughout a three-chain path system.

The immediate next mathematical obligation can therefore be stated without any biased-law ambiguity:

> **Three-chain heavy-slice obstruction.** Rule out the simultaneous inequalities in Theorem 5.1 for a connected-incomparability, width-exactly-three ideal-state system `Omega`, or identify an additional structural invariant that forces at least one cumulative flux into `[E/3,2E/3]`.

This is narrower than “apply the width-two theorem after deleting the third chain”: all third-chain lift multiplicities remain visible in the `A(u)B(u+e_a)` edge weights.

## 6. Projection to two chains: the exact source of the bias

The same encoding gives a second useful description. Project a complete 3D path to the two-letter word obtained by deleting every `C_3` step. For an admissible projected `C_1/C_2` word `w`, let

`M(w) = # {full 3D paths whose projection is w}`.

Then

`E = sum_w M(w)`.

Any comparison between an element of `C_1` and an element of `C_2` depends only on `w`, so

`Pr_P(x precedes y)`

`= [sum_{w: x precedes y in w} M(w)] / [sum_w M(w)]`.

Thus the third chain converts the width-two path law into a **special positive-integer weighted path law**. This is the path version of the exact insertion/deletion bias found by B19. The weights are not generally constant, so a proof that silently replaces them by the uniform law is invalid.

## 7. Exact falsification of two tempting shortcuts

The companion standard-library checker is

`verify_three_chain_flux.py`,

with executed output archived in

`verify_three_chain_flux.out`.

It independently enumerates linear extensions and compares them with the ideal-state dynamic program.

### Example A — third-chain lift multiplicities are genuinely nonuniform in width three

Take three two-element chains

`A=(0<1)`, `B=(2<3)`, `C=(4<5)`

and add `0<2<4` (with transitive consequences). The poset has width exactly three and `15` linear extensions.

Projecting to `A/B` gives exact lift multiplicities

`AABB : 3`, `ABAB : 6`, `ABBA : 6`.

For `x=1` relative to `B`, the flux vector is exactly

`(W(0),W(1),W(2))=(3,6,6)`.

Thus

`Pr(1<3)=(3+6)/15=3/5`,

whereas treating the three projected words uniformly would give `2/3`. The actual third-chain multiplicity changes the comparison probability.

### Example B — insertion-slice flux is not automatically log-concave

Take the same three chains and add `0<3` and `1<3`. This also has width exactly three, with `45` extensions. For `x=4` relative to `A=(0,1)`, the exact insertion-slice counts are

`(19,14,12)`.

They violate log-concavity:

`14^2 = 196 < 19*12 = 228`.

So Stanley's log-concavity theorem for the **rank distribution** of an element cannot simply be transplanted to these chain-insertion slices. Any proof using such a step needs an additional argument.

The same example has

`Pr(0<4)=26/45`,

so it is not a counterexample to POS3; its role is only to kill the false log-concavity shortcut.

The executed checker ends with

`POS3_THREE_CHAIN_FLUX_CHECK_PASS`.

## 8. Combined unresolved core after the partner result

Combining fleet02/B11 with the present run, a cardinality-minimal POS3 counterexample would have all of the following properties simultaneously:

1. width exactly three;
2. at least 15 elements under the inherited exact finite frontier;
3. connected incomparability graph, hence no nontrivial ordinal-sum factor to discard;
4. at least five maximal contiguous chain blocks in its strong-majority order;
5. for every element `x` and every chain of a fixed three-chain partition containing an element incomparable with `x`, the strong-majority insertion gap carries more than one third of **all** full linear extensions;
6. every relevant cumulative edge-flux cut avoids `[E/3,2E/3]`.

Items 5–6 are expressed entirely in the true uniform law on `L(P)` and retain the third chain exactly.

## 9. What changed and what did not

**Full-problem change:** none. POS3 remains open; no width-three closure is claimed.

**Mechanism change:** yes. The assigned three-chain encoding is now exact, and the biased deletion/projection issue is no longer an informal warning: it is represented explicitly by integer path fluxes and lift multiplicities. A hypothetical counterexample has been reduced to a simultaneous heavy-slice system anchored at the strong-majority gaps.

**Refuted shortcuts:** (i) uniformizing the two-chain projection; (ii) assuming chain-insertion slice counts inherit rank log-concavity.

**Next high-value step:** combine the heavy-slice normal form with fleet02/B11 connectedness and the inherited at-least-five-majority-block structure. The most concrete target is to prove that these structural constraints force at least one `x,C_b` insertion slice vector to have no jump exceeding `E/3` across its incomparable interval, or otherwise force a cumulative prefix directly into `[E/3,2E/3]`.

No novelty or priority claim is made. No benchmark gold, held-out labels, credentials, scheduler identifiers, machine paths, unrelated private data, remote paid model calls, email, Drive action, public posting, or permission change was used.
