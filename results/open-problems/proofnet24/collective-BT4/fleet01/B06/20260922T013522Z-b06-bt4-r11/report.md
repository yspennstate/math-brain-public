# BT4 fleet01/B06 — fixed-pair witness staticization and exit-return collars

Run: `20260922T013522Z-b06-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Target and exact inherited state

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Digons are allowed in the target statement. The current source boundary remains Bessy--Muis--Sereni--Steiner--Wiederrecht, arXiv:2608.12948 (2026-08-13), which explicitly leaves the genuine directed conjecture unresolved for every `k>=4` and proves only the one-reversed-arc relaxation at the `2k-1` threshold.

I consumed the campaign lead's newest complete version, **fleet02/B04 `20260922T011943Z-b04-bt4-r11`**, report blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`. I also use the compatible OTHER-account result **fleet03/B04 `BT4-MENGER-COLLAR-v1`**, report blob `a11cd981b4d76eaeb6dd02b4820d16a740ee0057`, and the support-correct segment-bypass theorem from fleet03/B05 `BT4-TCEX-v2.1-linkage` (linkage blob `f1545c2e4a546d17150bb20bbc59650a29eb2672`). The previous fleet01/B06 support-transfer report is commit `119633c34a37481842cbc84e728e057c56c9cd11`, blob `0af4b6dbda55cf1126d73d0688744bb2ba4496d9`.

The inherited counterexample normal form is an oriented exact-outdegree-seven spanning counterexample `D` with a globally minimum-total three-cycle packing `(A,B,C)`, acyclic remainder `R`, chordless packed cycles, arc domination and 3-vertex-strongness. For every fixed packed pair, the strengthened Lichiardopol--Pór--Sereni `k=2` theorem gives either a residual vertex of degree at most one (a six-or-more pair fan) or at least three residual vertices of degree exactly two (five-pair-fan witnesses). This dichotomy is universal for every disjoint cycle pair and therefore survives neutral exchanges.

The lead's current conditional proof has three remaining closures: six-fan closure, cross-linkage closure, and exclusion of a long neutral orbit in a persistent no-six state. This run attacks the last item by observing that the first off-pivot witness step is actually static for a fixed untouched pair, and then derives an exact rerouting collar for the resulting cycle-supported branch.

## 1. Fixed-pair witness sets do not regenerate under a light pivot

Fix two packed cycles `A,C` and define the induced residual digraph

`H_AC := D - (V(A) union V(C))`

and its degree-two witness set

`W_AC := {v in V(H_AC): d^+_{H_AC}(v)=2}`.

In a persistent no-six state the strengthened `k=2` theorem gives

`|W_AC| >= 3`.                                                     (1)

Now let `x` be a sink of the current remainder with no-six fan pattern `(3,2,2)`, where `A` is heavy and `B,C` are light. Suppose `b in B` is a direct light return port. Then

`N^+(x) intersect B = {b^+,b^{++}}`.

Perform the neutral light pivot

`B* = b -> x -> b^{++} -> ... -> b`,

so

`R* = (R \ {x}) union {b^+}`.

The key point is literal, not asymptotic: **the graph `H_AC` has not changed at all**. The pair `A,C` is identical before and after the pivot and the ambient digraph `D` is fixed. Hence

`W_AC(before pivot) = W_AC(after pivot)`                         (2)

as an exact vertex set with the same residual outdegrees. Only the support partition inside `H_AC=B union R=B* union R*` changes, and it changes only on the two vertices `x,b^+`.

Thus the lead's off-pivot witnesses are not dynamically created by reapplying the degree theorem. They were already present for the same fixed pair before the pivot. This removes one source of apparent neutral-orbit complexity.

## 2. Sharpened support dichotomy after the pivot

The sink `x` has pair fan

`a_A(x)+a_C(x)=3+2=5`,

so `x in W_AC`; after the pivot it is a cycle-supported five-witness on `B*`.

There are now two exact cases.

### Case T — the freed vertex is itself a witness

Assume `b^+ in W_AC`. Then after the pivot `b^+ in R*` is an **R-supported five-witness** for the unchanged pair `{A,C}`.

It has a genuinely nonterminal residual structure. In the old chordless cycle `B`, the only outarc of `b^+` back to `B` is the successor arc `b^+->b^{++}`. In the new support cycle `B*`, the only additional possible new support vertex is `x`, but `x->b^+` is one of the sink fan arcs and `D` is oriented, so `b^+->x` is absent. Since `b^+` has residual degree exactly two in `H_AC`, its second residual outarc must therefore go to a vertex

`r in R*`.

Consequently the pivot has transferred a cycle-supported degree-two witness into the remainder with the exact form

`b^+ -> b^{++} in B*`,   `b^+ -> r in R*`.                       (3)

In particular `b^+` is not a sink of `R*`.

### Case S — the freed vertex is not a witness

Assume `b^+ notin W_AC`. Since `x in W_AC` and `|W_AC|>=3`, there are at least two distinct vertices

`z_1,z_2 in W_AC \ {x,b^+}`.                                    (4)

By (2), each `z_i` has exactly the same support type before and after the pivot: if it was in the remainder it stays in the remainder, and if it was on `B` it stays on `B*`.

Combining T and S gives the useful post-pivot dichotomy:

> **Pivot support dichotomy.** In a persistent no-six state, after a light pivot for the pair `{A,C}`, either there is an R-supported five-witness for `{A,C}`, or at least three distinct five-witnesses for `{A,C}` are cycle-supported on the same complementary cycle `B*`.

Indeed, if there is no R-supported witness, all vertices of the size-at-least-three set `W_AC` lie on `B*`. Since `B*` is chordless, every such cycle-supported five-witness has residual outdegree exactly two consisting of its support-cycle successor and one unique `R*` exit. This is exactly the support-correct three-five-witness branch needed by the fleet03/B05 linkage machinery; no fake remainder witness is introduced.

This is sharper than merely saying that one off-pivot witness exists: the first pivot already forces either a real R-supported input to the path-fan machinery or a full three-witness cycle-supported saturation configuration.

## 3. Applying the OTHER-account Menger collar to the transferred R witness

Take any R-supported five-witness `z` produced by the preceding dichotomy. Its five arcs into `A union C` make it heavy on at least one of `A,C`; call that cycle `T` and write

`m = |N^+(z) intersect T| >= 3`.

Apply fleet03/B04 `BT4-MENGER-COLLAR-v1` in the current 3-vertex-strong minimum packing. There are three directed `T`-to-`z` paths, pairwise vertex-disjoint except at `z`, with distinct starts on `T`. Trim each to its last `T` vertex.

If one trimmed path internally meets another packed cycle, we have a genuine cross-packed transition, already one of the lead's explicit closure inputs. Otherwise all three interiors lie in `R*`. The corrected path-fan inequality gives every length `L_i >= m-1`.

The latest lead report proves that **every equality `L_i=m-1` is actionable**, including the saturated case: it gives a size-neutral globally minimum packing exchange with acyclic exchanged remainder. Therefore, if this R-supported branch avoids both a cross transition and an equality exchange, all three paths satisfy

`L_i >= m`,

and disjointness gives the sharper hard-branch bound

`|R*| >= 1 + sum_i (L_i-1) >= 3m-2 >= 7`.                        (5)

Thus the transferred-witness branch has an exact trichotomy:

1. cross-packed transition;
2. equality exchange;
3. three strict pure-R collars and `|R|=|R*|>=3m-2>=7`.

This applies in particular to the concrete transferred vertex `b^+` from Case T.

## 4. Exit-return collar for every cycle-supported five-witness

The alternative branch has at least three cycle-supported five-witnesses on one complementary packed cycle, say `B` (renaming `B*` back to `B`). Let `w` be any such witness for the fixed pair `{A,C}`.

Because `B` is chordless and `w` has residual degree exactly two after deleting `A,C`, its residual arcs are exactly

`w -> w^+`,   `w -> r_w` with `r_w in R`.                         (6)

Follow the unique exit `r_w` along arcs inside the finite DAG `R` until a sink `s` is reached. In the global no-six branch every remainder sink has fan pattern `(3,2,2)`, so in particular it has at least two outneighbors on **every** packed cycle, including `B`. Choose one such outneighbor `v in B`. This gives a directed path

`P_w: w -> r_w -> ... -> s -> v`                                (7)

whose internal vertices all lie in `R`.

Let `d_B(w,v)` be the positive forward cyclic distance from `w` to `v` on `B`, taking the value `|B|` when `v=w`. Global minimum of the three-packing gives the exact detour inequality

`|P_w| >= d_B(w,v)`.                                              (8)

For `v!=w`, replace the forward `B` segment from `w` to `v` by `P_w`; the resulting directed cycle has size `|B|+|P_w|-d_B(w,v)`, so a strict inequality in the wrong direction would shorten the global packing. For `v=w`, `P_w` itself is a replacement cycle and gives `|P_w|>=|B|`. Equality in (8) is again a neutral one-cycle exchange with an acyclic exchanged remainder.

Call

`e(P_w)=|P_w|-d_B(w,v) >= 0`                                     (9)

the **collar excess**.

### Heavy-witness crossing costs excess

Suppose `v!=w`, and the forward segment bypassed by `P_w` contains another cycle-supported five-witness `q`. Let `S` be the internal vertex set of that forward segment, so

`d_B(w,v)=|S|+1`.

Let `T in {A,C}` be a heavy target of `q`, with fan

`m_q=|N^+(q) intersect T|>=3`.

If some vertex of `T` sends an arc to `q`, fleet03/B05's support-correct segment-bypass theorem applies to the same path `P_w` and the proper segment `S`. It gives

`|P_w| >= m_q + |S| - 1 = d_B(w,v) + (m_q-2)`.

Equivalently,

`e(P_w) >= m_q-2 >= 1`.                                         (10)

Hence a **tight** exit-return collar (`e=0`) can bypass another heavy five-witness only if that witness satisfies reverse avoidance from its heavy target cycle. More generally, every crossed witness receiving from its heavy target consumes at least `m_q-2` units of collar excess.

This connects the unique-exit saturation branch directly to the named OTHER-account segment-linkage theorem without assuming an `R` bypass around a preselected single vertex.

## 5. G2 double-port incidence amplification

There is an additional exact count when the original no-six sink `x` has return ports from both light cycles. Write its fan labels as

`H=3`, `B=2`, `C=2`.

For each pair define the five-witness sets

`W_HB, W_HC, W_BC`.

Persistent no-six gives each set size at least three. The sink satisfies

`x in W_HB intersect W_HC`,   `x notin W_BC`.

No vertex can belong to all three witness sets. If a vertex had pair fans

`h+b=5`, `h+c=5`, `b+c=5`,

then adding gives `2(h+b+c)=15`, impossible over the integers. Therefore every vertex has witness-incidence at most two, while the three sets have at least nine incidences in total. It follows that

`|W_HB union W_HC union W_BC| >= 5`.                              (11)

If equality holds in (11), at least four of the five vertices are double-pair witnesses.

There is also an exact local classification. If

`v in W_HB intersect W_HC`,

then `b=c=t`, `h=5-t`, and exact outdegree seven gives the number `r` of outarcs from `v` into the remainder as

`r=7-(h+b+c)=2-t`.

Thus exactly three profiles are possible:

- `(h,b,c;r)=(5,0,0;2)`;
- `(4,1,1;1)`;
- `(3,2,2;0)`.

Chordlessness sharpens the support information: a packed-cycle vertex has exactly one outneighbor on its own support cycle. Hence the `(5,0,0)` and `(3,2,2)` profiles cannot be cycle-supported at all; they are R-supported, with the last profile a remainder sink. The only cycle-supported double-pair profile is `(4,1,1;1)`, and it must lie on one of the two 1-fan light cycles, where it has a unique R exit. The cyclically permuted statements hold for the other two double intersections.

So the G2 branch cannot hide all witness multiplicity in an unstructured support set: there are at least five distinct five-witnesses overall, and every double-pair witness is either an R object with one of the exact exit counts above or a light-cycle object with one unique R exit.

## Compact conditional end-to-end argument after this run

Assume a minimum BT4 counterexample and pass to the inherited exact-seven/global-minimum normal form. The universal pair-deletion theorem splits every state into SIX or persistent NO-SIX.

- SIX remains the separate six-fan/two-cycle-splice closure.
- In NO-SIX, every remainder sink is `(3,2,2)` and admits a neutral light pivot.
- For the untouched pair across that pivot, the witness set is **fixed**, not regenerated. The pivot support dichotomy above immediately yields either an R-supported five-witness or at least three cycle-supported five-witnesses on one complementary support cycle.
- An R-supported witness feeds the fleet03/B04 Menger collar: cross transition, equality exchange, or the strict quantitative branch `|R|>=3m-2>=7`.
- Three cycle-supported witnesses each have a unique R exit and hence an exit-return collar. Any collar crossing another heavy witness either pays the exact excess `m-2` or forces reverse avoidance by the fleet03/B05 segment theorem.
- In G2 there are at least five distinct pair witnesses and double-pair witnesses have only the three exact profiles above.

Thus the first unpaid implication is now the following narrower **static linkage statement**, rather than an abstract long neutral orbit:

> In a persistent no-six minimum packing, given either (i) an R-supported five-witness in the strict three-collar branch `|R|>=7`, or (ii) at least three cycle-supported five-witnesses on one support cycle with their unique exit-return collars and the excess rule (10), construct a legal two-cycle splice / strict packing reduction, or force a six-fan. In G2 one may additionally use the five-vertex incidence lower bound and the exact double-witness profiles.

No proof of this final static linkage statement is claimed here. But the first neutral-pivot step no longer requires chasing a newly generated witness around an unspecified orbit: its pair-deficit system is fixed, its support change is two-vertex exact, and the two resulting support branches now carry explicit directed collars.

## Failure checks and nonclaims

- Every cycle used is genuinely directed; no near-directed relaxation is substituted.
- The witness set invariance is only asserted for a fixed untouched pair `A,C`; a later exchange changing `A` or `C` changes the induced pair-deletion graph and must be recomputed.
- The `|R|>=3m-2` bound is only for the branch where all three Menger channels have R interiors and none attains equality.
- Exit-return collars may share R vertices; no disjointness of the three witness collars is assumed.
- Collar inequality (10) uses the fleet03/B05 segment theorem only when the bypassed segment actually contains the marked heavy witness and its heavy target cycle sends into it.
- The G2 incidence count is a structural amplification, not a target-level closure.
- No target-level BT4 proof, novelty claim, finite-order surrogate, edge-disjoint substitute, or verified-brain claim is made.

## Honest outcome

`ESSENTIAL_STEP_APPLIED`.

The lead's first no-six dynamic obstruction is tightened to a static support dichotomy, with a real R-supported transfer branch or a three-cycle-supported-witness branch. The latter now has canonical exit-return collars and an exact collar-excess charge when a collar bypasses another heavy witness. Full BT4 remains open.
