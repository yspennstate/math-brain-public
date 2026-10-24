# BT4-MONOTONE-QUADRANT-RANK-WALL-v1

**Status:** ESSENTIAL_STEP_APPLIED; full BT4 remains OPEN.

## Target and assignment

BT4 asks whether every finite loopless simple digraph with minimum outdegree at least 7 contains four vertex-disjoint directed cycles (digons allowed). This run follows the account03/B05 assignment: prove the disjointness-preserving exchange promised by the current two-partition/linkage candidate, without replacing a minimum-degree hypothesis by an average-degree statement. Assigned partner: account04/B06.

## Named partner result consumed

I apply account04/B06's source-bound result `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1` from `20260922T070806Z-b06-bt4-coll11`. Its useful output is that, in the current 3-vertex-strong minimal-counterexample normal form, connector intersection can be converted to a same-support bypass or bounded-support exit, while a direct cross can be freshened after deleting its endpoints. Consequently the genuinely unpaid long/no-bypass/no-third-support residual is a packed-port cyclic-order/endpoint-compatibility problem rather than merely a linkage-rank problem.

## New lemma: monotone same-quadrant rank is not enough

Let A and B be directed cycles. Let

- `F_i : alpha_i -> ... -> beta_i` and `F_k : alpha_k -> ... -> beta_k` be A-to-B connectors,
- `G_0 : gamma_0 -> ... -> delta_0` and `G_1 : gamma_1 -> ... -> delta_1` be B-to-A connectors,

with pairwise internally vertex-disjoint connector interiors, all interiors disjoint from A union B, and all four packed endpoints distinct. Suppose the forward ports occur in the same cyclic order relative to the fixed reverse anchor:

- on A: `alpha_i, alpha_k, delta_0`,
- on B: `beta_i, beta_k, gamma_0`.

Here `X(x,y)` denotes the open directed arc of directed cycle X from x to y.

**Lemma.** No choice of the fresh reverse endpoints `(gamma_1,delta_1)` permits these four connectors to be spliced, using directed subarcs of A and B, into two vertex-disjoint mixed A-B cycles.

### Proof

Any mixed cycle pairing `F_j` with `G_l` uses the directed support arcs

`B[beta_j,gamma_l]` and `A[delta_l,alpha_j]`.

First inspect A. If `delta_1` is not in `A(alpha_i,alpha_k)`, then neither pairing of `{F_i,F_k}` with `{G_0,G_1}` yields two disjoint A-support arcs: one of the two required directed arcs contains an endpoint or a nontrivial subarc of the other. Thus A is already blocking.

If instead `delta_1` lies in `A(alpha_i,alpha_k)`, then the only disjoint A pairing is

`F_i <-> G_0` and `F_k <-> G_1`.

Indeed `A[delta_0,alpha_i]` is disjoint from `A[delta_1,alpha_k]`, whereas the crossed pairing forces overlap.

Now inspect B. If `gamma_1` is not in `B(beta_i,beta_k)`, B is blocking for the same directed-arc reason. If `gamma_1` lies in `B(beta_i,beta_k)`, then the only disjoint B pairing is the opposite one,

`F_i <-> G_1` and `F_k <-> G_0`,

because `B[beta_i,gamma_1]` is disjoint from `B[beta_k,gamma_0]`, while `B[beta_i,gamma_0]` overlaps the other required arc under the first pairing.

Thus whenever A admits two disjoint support pieces it forces one pairing, while whenever B admits two disjoint support pieces it forces the opposite pairing. No globally consistent pairing exists. QED.

## Positive inversion criterion

The obstruction identifies exactly what additional structure would pay the exchange. Suppose instead that the forward pair is inverted between the supports:

- on A: `alpha_i, alpha_k, delta_0`,
- on B: `beta_k, beta_i, gamma_0`.

If a second reverse connector has

- `delta_1 in A(alpha_i,alpha_k)`, and
- `gamma_1 in B(beta_k,beta_i)`,

then the common pairing

`F_i <-> G_0`, `F_k <-> G_1`

uses disjoint directed arcs on both A and B. Together with pairwise disjoint connector interiors, this gives two genuinely vertex-disjoint mixed replacement cycles.

So the missing global implication is not 'raise Menger rank once more'. It is: force an **order inversion/side switch** together with a reverse endpoint in the matched inversion gaps, or force one of the already recognized structural exits (connector collision, third-support mediation, same-support bypass, bounded/short support, or the SIX/fan branch).

## Application to the partner state

The partner result collapses intersection/rank defects to a pure port-order residual in the long/no-bypass branch. The lemma above shows that a naive third-linkage repair is false at that level: even arbitrarily clean extra reverse linkage cannot close a two-cycle exchange against a forward pair whose ports remain monotone in the same quadrant. This is a source-valid counterexample to that *local implication*, not to BT4 itself.

Conversely, the positive inversion criterion supplies an exact disjointness-preserving splice once the global degree/minimality machinery produces an inverted forward pair and a matched-gap reverse connector. This narrows the next obligation to a concrete cyclic-order forcing statement.

## First missing implication after this run

`BT4-INVERSION-OR-EXIT-v1`: in the partner's long/no-bypass/no-third-support residual, prove from minimum outdegree 7, minimal packing, and the existing exact-seven/arc-domination structure that either

1. an inverted forward pair and matched-gap reverse connector occur, closing the two-cycle exchange by the criterion above; or
2. one of collision, H-mediation, same-support bypass, short/bounded support, or SIX/fan closure occurs.

No claim is made that a prescribed direct connector is automatically part of a particular 3-Menger-path family, and no claim is made that the lemma controls arbitrary unbounded reverse-linkage rank. Full BT4 is not proved.

## Provenance / execution posture

Brain status: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`. No scheduler, notification, email, Drive, public workflow, paid remote compute, credential, or cross-account native action was performed. Configured model/reasoning metadata not exposed by the platform remains `UNVERIFIED`.