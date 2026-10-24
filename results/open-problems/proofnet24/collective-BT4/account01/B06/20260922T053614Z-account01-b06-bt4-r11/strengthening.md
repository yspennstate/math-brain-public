# Strengthening — forced light triangle has a common remainder port or an x-free cross

This addendum strengthens the same-run report `BT4-HT-ALIGNED-CROSS-COLLAPSE-v1` (commit `4167305fb4988666f144b48f5d2dd15d749239d2`, blob `5f8b2a981f3baa66d904695ed517040a91f916c0`). Outcome remains `ESSENTIAL_STEP_APPLIED`; full BT4 remains open.

## Fresh compatible inputs

After the primary report, I consumed two newer compatible cage refinements.

1. account02/B06 `BT4-HT-ARCMAX-CAGE-COLLAPSE-v2`, handoff `b06-20260922T052855Z-account02-B06-arcmax-cage`, controlling scientific blob `96fa9bdb0033fc6e6c3c42092e8259f882f8cd26`. It exactifies the cage further: `h0,h1,h2,r2` are all exact five-witnesses for the light pair `{A,B}`.

2. Named OTHER-account account04/B05 `BT4-HT-XFREE-HALL-v1`, run `b05-20260922t051421z-r34`, handoff blob `1ac9d889a7aba352f13e6d43b19c376a679d7a3c`. It proves that if the missing `T0` three-hit witness `p` lies on light support `A`, then `h0` cannot be heavy on `A`; hence `h0` is heavy on the other light support `B`. It also gives x-free heavy-fan escapes with pairwise disjoint remainder interiors and the same-heavy Hall alternative.

These exact statements are used below, not their outcome labels.

## Setup inherited from the same-run theorem

The primary report proved that in the aligned exact-two-predecessor heavy-triangle cage the light support is forced to be a triangle:

`A = p -> u -> v -> p`,

where

`x->u,v`, `p->h0,r0,x`,

and `h1` is heavy on `A`. Since `|A|=3`, in fact

`h1->p,u,v`.

The controlling heavy-target no-inport theorem gives

`A not->h1`.

The old remainder is the exact chain cage

`R={x,r0,r1,r2}`,
`r0->r1->r2`, `r0,r1,r2 -> x`,

with the other exact cage arcs retained from the lead.

By account04/B05, `h0` is heavy on `B`. Therefore either `h2` is heavy on `B`, in which case the pair `(h0,h2)` is already the account04/B05 same-heavy Hall port object, or `h2` is heavy on `A`. This addendum attacks the latter case.

Assume from now on that `h2` is heavy on `A`. Since `A` is a triangle,

`h2->p,u,v`.

The controlling no-inport theorem also gives `A not->h2`.

## Lemma 1 — the two sink-fan vertices have one common R-outneighbor

Let

`U=N_R^+(u)`, `V=N_R^+(v)`.

Both sets are nonempty. Indeed, apply global NO-SIX to the pair `H union B`. Each of `u,v` has residual outdegree at least two in `D-(H union B)=D[A union R]`. Chordlessness of `A` gives exactly one outgoing arc inside `A`, its directed successor. Thus each has an outneighbor in `R`. Since `x->u,v`, orientation excludes `u->x` and `v->x`, so

`U,V subseteq {r0,r1,r2}`.

We show that every pair `r_i in U`, `r_j in V` must have `i=j`.

Fix `r_i in U`. The triangle

`W_u(i)=u -> r_i -> x -> u`

is genuine. Also

`C=p -> h0 -> h1 -> p`

is a genuine triangle. The three cycles `C,W_u(i),B` are pairwise vertex-disjoint and have the same total order as the original packing `(H,A,B)`, namely `6+|B|`. Hence their four-vertex remainder must be acyclic.

If `r_j in V` is not the removed `r_i`, then `v->r_j` remains in that exchanged remainder. The following off-diagonal pairs create an explicit directed cycle there:

- `(i,j)=(0,1)`: `v->r1->h2->v`;
- `(i,j)=(2,0)`: `v->r0->r1->h2->v`;
- `(i,j)=(2,1)`: `v->r1->h2->v`.

Thus these three ordered pairs are impossible.

Now swap `u` and `v`: use the neutral triangle

`W_v(j)=v -> r_j -> x -> v`

and the same triangle `C`. Its exchanged remainder is also acyclic. The symmetric explicit cycles exclude

- `(i,j)=(1,0)`: `u->r1->h2->u`;
- `(i,j)=(0,2)`: `u->r0->r1->h2->u`;
- `(i,j)=(1,2)`: `u->r1->h2->u`.

All six off-diagonal ordered pairs are excluded. Therefore every element of `U x V` lies on the diagonal. Since `U,V` are nonempty,

`U=V={r_k}`

for one `k in {0,1,2}`. QED.

This is a genuine support/disjointness statement: the two neutral sink-fan transfers cannot choose independent remainder heads in the same-heavy-`A` triangle state; both are forced through one common remainder port.

## Lemma 2 — the common port is heavy on the opposite light cycle B

For the common `r_k` of Lemma 1, `r_k` has at least three outneighbors on `B`.

- If `k=0`, exact cage geometry gives exactly three outneighbors of `r0` in `H union R`, hence four in `A union B`. But `p,u,v -> r0` (the first from the `T0` witness, the latter two from Lemma 1), so orientation excludes every arc from `r0` to `A`. Thus all four light targets of `r0` lie on `B`.

- If `k=1`, exact cage geometry gives exactly three outneighbors of `r1` in `H union R`, hence four in `A union B`. Since `u,v -> r1`, at most the single vertex `p` of `A` can be an `A`-target. Hence `r1` has at least three targets on `B`.

- If `k=2`, the exact-cage refinement gives `d^+_{H union R}(r2)=2`, so `r2` has five targets in `A union B`. Since `u,v -> r2`, at most `p` can be an `A`-target, and therefore `r2` has at least four targets on `B`.

Thus in every case `r_k` is a remainder-supported vertex with `m=|N^+(r_k) intersect B|>=3`. By the inherited one-vertex minimum-packing exchange lemma,

`B not-> r_k`.

## Lemma 3 — exact B-to-common-port routing classification

Take a shortest directed path from `B` to `r_k`; strong connectivity guarantees existence. If it meets `H` or `A` before reaching `r_k`, its initial segment gives a genuine cross-packed transition from `B` into another packed support, which is already a legal packed-port output.

Assume instead that all internal vertices lie in the old remainder `R`. The corrected path-fan lemma says that a `B`-to-`r_k` path of length `L` satisfies

`L >= m-1`,

where `m=|N^+(r_k) intersect B|`.

Using the exact old remainder chain:

### k=0

No old remainder vertex sends to `r0`, and `B not->r0`. Hence an R-internal `B`-to-`r0` path does not exist. A cross-packed transition is forced.

### k=1

The only possible R-internal shortest path is

`B -> r0 -> r1`,

of length two. Since `m>=3`, the path-fan bound forces `m=3` exactly. Therefore the no-cross alternative is an exact equality collar: `r1` has exactly three `B`-targets and one `A`-target, necessarily `r1->p`.

### k=2

A path `B->r1->r2` has length two, but here `m>=4`, so the path-fan bound forbids it. The only possible R-internal route is

`B -> r0 -> r1 -> r2`,

of length three. Again the path-fan bound forces `m=4` exactly. Thus the no-cross alternative is another exact equality collar, and `r2` has its unique `A`-target `r2->p`.

Consequently, in the same-heavy-`A` triangular branch, the common remainder port forces either a genuine `B`-to-`H/A` cross-packed transition or one of two completely pinned equality chains:

`B->r0->r1` with `m_B(r1)=3`,

or

`B->r0->r1->r2` with `m_B(r2)=4`.

No arbitrary R-routing remains.

## Updated aligned heavy-triangle frontier

The forced triangular aligned branch now splits as follows.

1. If `h2` is heavy on `B`, then `(h0,h2)` is the account04/B05 same-heavy Hall pair, with x-free disjoint-interior escape transitions and the fourth-witness return interface.

2. If `h2` is heavy on `A`, Lemmas 1--3 force a single common remainder port for `u,v`, then either an immediate cross-packed transition from `B` to `H/A`, or one exact path-fan equality chain through the old remainder.

Thus the new first unpaid local implication is narrower than the primary report's generic shared-sink problem: close the account04/B05 same-heavy Hall port object, the newly forced `B->H/A` cross, or the two exact equality chains by an actual two-cycle splice / strict lexicographic decrease / cyclic exchanged remainder / SIX / fourth cycle. The equality chains must be treated as neutral exchanges, not as contradictions by themselves.

No full BT4 proof is claimed.
