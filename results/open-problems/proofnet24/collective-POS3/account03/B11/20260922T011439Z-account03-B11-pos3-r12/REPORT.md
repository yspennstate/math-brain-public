# POS3 account03/B11 — Hasse blockers and delayed endpoint distinguishers

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

The later owner control `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` supersedes this slot's older benchmark assignment. This run therefore continues the assigned POS3 order-polytope/correlation route and performs no new benchmark work.

## 1. Exact inherited state and peer result consumed

The immediate predecessor for this slot is:

- `proofnet24/collective-POS3/account03/B11/20260922T003936Z-account03-B11-pos3-r11/REPORT.md`, blob `5b65cb3c68a668e553dc6465252bc6cb82b68b8d`.

It proves the order-polytope swap-defect identity. For an incomparable pair `x,y`,
\[
2p_{xy}-1=\frac{\operatorname{vol}(D^+_{xy})-\operatorname{vol}(D^-_{xy})}{\operatorname{vol}O(P)}.
\]
Writing
\[
P_y(x)=\{z:z<y,\ z\parallel x\},\qquad
S_x(y)=\{z:x<z,\ z\parallel y\},
\]
the positive defect is controlled by the canonical blockers
\[
M^-_{xy}=\operatorname{Max}P_y(x),\qquad
M^+_{xy}=\operatorname{Min}S_x(y).
\]
In width at most three each canonical side has size at most two. For every adjacent incomparable pair `x ≺_* y` in the inherited transitive strong-majority order of a hypothetical counterexample, the predecessor report proves
\[
|M^-_{xy}|+|M^+_{xy}|\ge 2.
\]
At the first majority-block boundary this yields exactly two successor blockers; at the last boundary exactly two predecessor blockers.

The named other-account partner result consumed in this run is:

- **account04/B19**, `proofnet24/collective-POS3/account04/B19/B19-20260922T001218Z-r44/REPORT.md`, blob `ce30dae79d698103f026d4d871033238489b1fb1`.

It proves that restriction of a uniform linear extension to an autonomous subset is uniform on the induced subposet. Consequently a cardinality-minimal POS3 counterexample has no proper autonomous nonchain; in particular an autonomous incomparable pair is balanced with probability exactly `1/2`.

The present run applies that exact autonomous-subset theorem to the endpoint blocker pair, rather than merely citing it.

## 2. Canonical swap blockers are Hasse neighbors

The earlier compression to maximal predecessor blockers and minimal successor blockers can be sharpened from an arbitrary-poset relation to a Hasse-diagram statement.

### Theorem 2.1 — Hasse-cover compression

Let `x,y` be incomparable in any finite poset `P`.

1. Every `m in M^-_{xy}` is a lower cover of `y`: `m \lessdot y`.
2. Every `s in M^+_{xy}` is an upper cover of `x`: `x \lessdot s`.

### Proof

Take `m in M^-_{xy}`. We know `m<y` and `m || x`. Suppose `m` does not cover `y`. Then some `z` satisfies
\[
m<z<y.
\]
The element `z` cannot satisfy `z<x`, because then `m<z<x`, contradicting `m || x`. It cannot satisfy `x<z`, because then `x<z<y`, contradicting `x || y`. Hence `z || x`, so `z in P_y(x)`. But `m<z`, contradicting maximality of `m` in `P_y(x)`. Therefore `m \lessdot y`.

The successor statement is dual. If `x<z<s` for a purported non-cover `s in M^+_{xy}`, then `z<y` would imply `x<y`, while `y<z` would imply `y<s`, contradicting `s || y`. Thus `z || y`, so `z in S_x(y)` lies below the minimal element `s`, a contradiction. ∎

This theorem uses no width hypothesis.

### Width-three consequence

For an adjacent strong-majority boundary in a hypothetical width-three counterexample, the prior double-blocker certificate is therefore not supported by remote comparabilities: it is supported by at least two **Hasse edges** incident with the boundary endpoints.

At the first majority-block boundary `x ≺_* y`, there are no predecessor blockers, so
\[
M^+_{xy}=\{s_1,s_2\},
\]
with
\[
x\lessdot s_1,\qquad x\lessdot s_2,
\]
and `s_1,s_2,y` pairwise incomparable. At the last boundary the dual statement holds with two distinct lower covers of the right endpoint.

## 3. The partner theorem forces a delayed distinguisher

Let a cardinality-minimal counterexample have maximal contiguous chain blocks
\[
B_1,B_2,\ldots,B_r
\]
in its transitive strong-majority order, with `r>=5` from the inherited state. Let `x` be the last element of `B_1` and `y` the first element of `B_2`. By the preceding section there are exactly two canonical successor blockers `s_1,s_2`.

### Theorem 3.1 — delayed endpoint distinguisher

The incomparable pair `{s_1,s_2}` is nonautonomous. Moreover **every** element that distinguishes `s_1` from `s_2` in its poset relation lies strictly after the entire second majority block `B_2`.

Equivalently, the first-boundary Hasse fork cannot be broken locally inside `B_1 union B_2`; its first possible non-module witness occurs only in `B_3 union ... union B_r`.

### Proof

The pair `{s_1,s_2}` is a proper nonchain. If it were autonomous, the account04/B19 theorem would make its induced two-point antichain uniform and hence balanced with probability `1/2` in `P`, contradicting that `P` is a counterexample. Therefore at least one outside element distinguishes the two blocker vertices.

We now locate every such distinguisher.

Any element `z` in `B_1` before `x` satisfies `z<x`, since `B_1` is a poset chain. Because `x<s_i`, transitivity gives `z<s_1` and `z<s_2`; such `z` cannot distinguish them. The endpoint `x` is below both blockers, while `y` is incomparable with both, so neither endpoint distinguishes them.

Now take `z in B_2` after `y`. Since `B_2` is a chain and `y` is its first element, `y<z`.

If `z<s_i`, then `y<z<s_i`, contradicting `y || s_i`.

If `s_i<z`, then `s_i` must occur before `z` in the strong-majority order. Since `x<s_i` and `x,y` are adjacent in that total order, `s_i` cannot occur before `y`. Thus it would occur between `y` and `z`; by contiguity it would belong to `B_2`, contradicting `s_i || y`.

Hence every `z in B_2` is incomparable with both `s_1` and `s_2`, so it cannot distinguish them. No element occurs between adjacent `x,y`. Therefore every distinguisher lies strictly after all of `B_2`. ∎

### Dual endpoint

Reversing the poset gives the exact dual statement: for the last majority-block boundary, the two canonical predecessor blockers are lower covers of the right endpoint, are nonautonomous, and every element distinguishing those two blockers lies strictly before the entire penultimate block.

### A useful local refinement

A distinguisher cannot be below one blocker and above the other, because that would make the two blockers comparable by transitivity. Thus it is comparable with exactly one blocker and incomparable with the other.

If a delayed distinguisher `z` satisfies `z<s_1`, then the cover relation `x\lessdot s_1` and the fact that `z` occurs after `x` force `z || x`; also `z || y`, because `y<z<s_1` would contradict `y || s_1` and `z<y` would contradict the strong-majority position. Consequently
\[
\{x,y,z\}
\]
is a three-element antichain. Width three is therefore saturated again whenever the delayed witness approaches a blocker from below.

This does not yet force a contradiction, but it converts the formerly local double-blocker condition into a spatial constraint across at least three majority blocks.

## 4. A stronger local endpoint-fork lemma is false

The preceding theorem suggests a tempting shortcut:

> Perhaps the first-boundary triple `{y,s_1,s_2}` must itself contain a balanced pair.

That claim is false, even for a width-three poset satisfying the exact first-boundary Hasse-fork geometry.

Take the seven-element poset with transitive closure generated by
\[
0<2,\ 0<3,\ 0<4,\ 0<5,\ 0<6,\ 
1<2,\ 1<5,\ 2<5,\ 4<5,\ 4<6.
\]

It has exactly `79` linear extensions, width `3`, and transitive majority order
\[
0\prec_*1\prec_*4\prec_*2\prec_*3\prec_*6\prec_*5.
\]
At the first boundary `x=0`, `y=1`, the canonical successor blockers are exactly
\[
s_1=3,\qquad s_2=4,
\]
and both are Hasse covers of `0`. Exact extension counts give
\[
p(0<1)=54/79>2/3,
\]
\[
p(1<3)=65/79>2/3,\qquad
p(1<4)=55/79>2/3,
\]
while
\[
p(3<4)=23/79<1/3.
\]
Thus none of the three incomparable pairs inside `{1,3,4}` is balanced.

The blocker pair is indeed nonautonomous. Vertices `5` and `6` distinguish it; for example `4<6` while `3 || 6`. Both distinguishers occur strictly after the second majority chain block, exactly as Theorem 3.1 predicts.

This seven-element poset is **not** a counterexample to POS3: for instance
\[
p(2<3)=42/79,
\]
which is balanced. Therefore the example refutes only the stronger local endpoint-fork shortcut, not the parent conjecture.

The important implication is that the next proof cannot stop at one Hasse fork. It must exploit the delayed witness together with subsequent majority-block boundaries, or show that iterating this forced nonautonomy eventually violates width three / module-primality / the heavy-slice constraints.

## 5. What the new step changes in the global proof search

Before this run, the order-polytope route had reduced a hypothetical minimal counterexample to a connected, module-prime width-three core in which every adjacent majority-block boundary has multiple canonical swap blockers.

This run sharpens that residual in two ways:

1. **Local support is Hasse-local.** Every canonical blocker is a cover neighbor of the relevant boundary endpoint.
2. **Module failure is block-nonlocal at the endpoints.** The first Hasse fork cannot be distinguished until after all of the second majority block; dually, the last fork cannot be distinguished until before all of the penultimate block.

So the exact successor obligation is now:

> Starting from the first two-cover Hasse fork, follow a delayed distinguisher in `B_3` or later and combine it with the next adjacent-boundary double-blocker certificate. Prove that repeated forced nonautonomy either creates a balanced pair, creates four mutually incomparable elements, creates a proper autonomous nonchain, or contradicts the inherited heavy-slice inequalities.

The seven-element adversary shows that no theorem confined to the first boundary triple can suffice.

A plausible next invariant is a **block-span potential**: assign each forced Hasse fork the earliest majority block containing a distinguisher of its blocker pair. Theorem 3.1 says the first span is at least two blocks, and the dual last span is similarly nonlocal. A proof would need to show that a width-three module-prime core cannot realize compatible spans across all `r-1` boundaries. This is a new, more precise target, not a claimed theorem.

## 6. Verification

The companion standard-library verifier `verify_pos3_hasse_delay.py` checks:

- the seven-element relation set and transitive closure;
- exactly `79` linear extensions and width `3`;
- the transitive majority order above;
- canonical blocker computation at the first boundary;
- on every incomparable ordered pair in this example, every maximal predecessor blocker is a lower cover and every minimal successor blocker is an upper cover;
- all exact probability numerators quoted above;
- nonautonomy of the sibling blockers and the delayed distinguisher `6`.

Recorded output ends with `POS3_HASSE_DELAY_CHECK_PASS`.

The finite script checks the adversary and regression properties only. Theorems 2.1 and 3.1 are established by the proofs above, not by enumeration.

## 7. Status

- Hasse-cover compression of canonical swap blockers: **PROVED**.
- First-boundary two-cover Hasse fork: **PROVED**, conditional on the inherited double-blocker/minimal-counterexample state.
- Delayed endpoint distinguisher from the account04/B19 autonomous-module theorem: **PROVED**.
- Dual delayed last-boundary statement: **PROVED**.
- Stronger claim that the first endpoint-fork triple itself must contain a balanced pair: **REFUTED** by an exact seven-element width-three example.
- Width-three `1/3–2/3` parent target: **OPEN / NOT PROVED**.
- Run outcome: `ESSENTIAL_STEP_APPLIED`.

No novelty or priority claim is made. No benchmark gold, FEI proof material, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, paid model/API/Codex execution, remote workflow, or public release was used.
