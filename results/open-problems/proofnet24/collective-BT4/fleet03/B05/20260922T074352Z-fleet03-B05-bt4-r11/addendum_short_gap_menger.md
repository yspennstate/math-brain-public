# Addendum — the `p+++` short gap forces a K-side Menger port

Parent candidate: `BT4-SHORTEST-CROSS-PARITY-TRAP-v1`  
Addendum candidate: `BT4-P3-KSIDE-MENGER-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

This addendum pushes the parent parity obstruction one step further by using the special aligned heavy-triangle geometry that the parent theorem did not yet exploit.

## 1. Source-bound inherited facts

From the aligned long-support heavy-triangle branch:

- `a3=p+++` on light support `A`;
- the clean mixed cycle is

  `K0 = p -> x -> b -> B[b,q] -> q -> a3 -> A[a3,p] -> p`;

- therefore the only vertices of `A` outside `K0` are exactly

  `{p+,p++}`.

From assigned partner fleet04/B06 `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1`: between `A` and `B` in either ordered direction there are three pairwise vertex-disjoint directed Menger paths before the `R2/H2` split. After trimming, their internal vertices avoid `A union B`; an internal packed hit is therefore on the heavy triangle `H`, and otherwise the internal vertices lie in the acyclic remainder `R`.

## 2. New theorem — short-gap Menger pigeonhole

### Statement

In the exact clean-pair state above:

1. among any three pairwise vertex-disjoint directed `A->B` paths, after trimming from last `A` hit to first later `B` hit, at least one path has its `A` source on `K0 intersect A`;
2. among any three pairwise vertex-disjoint directed `B->A` paths, after trimming, at least one path has its `A` terminal on `K0 intersect A`.

Consequently, in each direction, either one obtains explicit `H` mediation or one obtains an `R`-internal connector with its `A` port on the used `K0` support segment. Thus the shortest-cross parity wall cannot persist with every new port confined to the two-vertex complementary `A` gap.

### Proof

The three trimmed `A->B` paths are vertex-disjoint, so their three source vertices on `A` are distinct. But

`V(A) \ V(K0) = {p+,p++}`

has only two vertices. Hence at least one source lies in `V(K0) intersect V(A)`. Its trimmed interior either meets `H`, giving explicit third-support mediation, or avoids `H`, in which case every internal vertex lies in `R` and the path is the claimed K-side remainder connector.

For three trimmed `B->A` paths, the three terminal vertices on `A` are distinct. Again only two vertices of `A` lie outside `K0`, so at least one terminal lies on `K0 intersect A`. The same `H`-mediation versus `R`-internal dichotomy applies. QED.

This uses the exact `a3=p+++` geometry. It is not an average-degree or generic linkage argument.

## 3. Interaction with opposite-connector intersections

Suppose the no-`H` branch supplies

`P* : c -> ... -> e` (`A->B`), with `c in K0 intersect A`,

`Q* : f -> ... -> d` (`B->A`), with `d in K0 intersect A`,

and both interiors in `R`.

If `P*` and `Q*` intersect internally in `R`, the assigned partner's opposite-intersection theorem immediately emits a same-support bypass or a bounded short-support event. Hence in the all-long/no-bypass residual they may be taken internally disjoint.

Packed endpoint collisions remain a separate explicit branch. In the distinct-port residual assume

`c,d notin {p,a3}`, `c!=d`,

and the `B` ports `e,f` are distinct from `b,q` and from each other.

## 4. Exact remaining 2x2 order condition with the forced K-side ports

The old connectors are

`F0 : p -> x -> b`,
`G0 : q -> a3`.

Use `P*` as the second forward connector and `Q*` as the second reverse connector.

Since both new `A` ports lie on the directed support segment `A[a3,p]`, the `A` endpoint types alternate **iff**

`c` occurs before `d` while traversing `A[a3,p]` from `a3` toward `p`.

Indeed, in that case the cyclic order is

`p(F0), a3(G0), c(P*), d(Q*)`,

and the unique disjoint pairing on `A` is the transposed pairing

`F0 with Q*`, `P* with G0`.

If `d` occurs before `c`, the two reverse-target ports are consecutive by type and no two-cycle splice using this quartet is possible.

When `c` occurs before `d`, the same transposed pairing is legal on `B` exactly when the cyclic order of the four `B` ports is

`b(F0), f(Q*), e(P*), q(G0)`

(up to cyclic rotation). In that case the two explicit replacement cycles are

`Z0 = F0 + B[b,f] + Q* + A[d,p]`,

`Z1 = P* + B[e,q] + G0 + A[a3,c]`.

Their connector interiors and support segments are pairwise vertex-disjoint, so `Z0,Z1` are genuinely vertex-disjoint. They replace `A,B` while retaining `H`, and the existing minimum-packing tax applies.

Thus the generic cyclic-order wall has been reduced, in this exact branch, to two concrete one-dimensional order tests: the order of `(c,d)` along `A[a3,p]`, and the order of `(b,f,e,q)` around `B`.

## 5. Correction to the parent next-step wording

The parent report said that a side-switched connector should be combined with rank-two opposite linkage to obtain a legal reconstruction. Source-side switching alone is **not sufficient**. The exact conditions in Section 4 are required. This addendum narrows rather than silently assumes that splice.

What is now proved is stronger and safer:

- the `A`-side K-port is forced by three-linkage plus the two-vertex `p+++` gap;
- internal collision is already productive by the partner theorem;
- in the clean distinct-port residual, only the two explicit cyclic inequalities above remain for this quartet.

## 6. First unpaid implication after the addendum

`BT4-KSIDE-ORDER-CLOSE-v1`:

> In the aligned four-remainder heavy-triangle long-support state, choose the K-side Menger connectors `P*,Q*` supplied above. Prove that either `c` precedes `d` on `A[a3,p]` and `b,f,e,q` have the compatible cyclic order, giving the explicit two-cycle replacement and tax; or the opposite order forces a packed-endpoint collision, another `R`-intersection bypass, `H` mediation, SIX, or the bounded short-support exit.

The remaining debt is therefore not generic rank, not arbitrary connector intersection, and not mere existence of a side-switched source. It is an exact ordered-port wall on one known `A` segment and the corresponding `B` pairing order.

Global debts remain separate: SIX/H5 closure, bounded F2/F3 states, and the support-carried seven-remainder branch. No full BT4 proof is claimed.

No computation or authenticated brain use occurred; no scheduler mutation or prohibited external action occurred.
