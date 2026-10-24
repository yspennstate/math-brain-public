# RC reduces to one graph inequality, and that inequality has an interpretation

Author: session 6c4d55a4, 2026-08-20. Third of three notes; see
`the_fibre_is_an_ising_partition_function.md` for the closed form and
`rc_on_the_ising_reformulation.md` for the families. Nothing here bears on the sharp Rademacher
conjecture directly.

## The statement

**CONJECTURE (cut-inflation).** Let `G` be a connected graph on `V` vertices with `E` edges, and let
`b = 1` if `G` is bipartite, `0` otherwise. Then

    Z(G) := < prod_{uv in E} (1 - x_u x_v / 3) >   <=   (4/3)^{E - V + b},

the average being uniform over `x in {+-1}^V`. **Equality exactly on trees.**

## Why it is the right object: Z is an inflation factor

Write `F(G) = SUM_x 2^{cut(x)}`. Then `Z = (2/3)^E F / 2^V`. Now let

    I(G) := 2^V (3/2)^E

be the value `F` would take **if the edge-cut indicators were independent** — each edge cut with
probability 1/2, contributing `(1/2)(2) + (1/2)(1) = 3/2` per edge. Then

    **Z = F / I   exactly.**

So `Z` is precisely the factor by which dependence among the cut indicators inflates
`E[2^{cut}]` over independence, and the conjecture says that inflation never exceeds
`(4/3)^{E-V+b}`.

On a tree the indicators genuinely are independent — `F = I`, `Z = 1`, and `E - V + b = 0`, so the
bound holds with equality. That is not a coincidence to be explained away; it is the content.

## Evidence

**Exhaustive, exact rational arithmetic:** every connected graph on up to 7 vertices —
**1,893,730 graphs — zero violations.** Worst ratio `Z / (4/3)^{E-V+b} = 1.000000000` exactly,
attained at the path on 3 vertices, i.e. at a tree.

**Targeted families**, chosen as the likely extremes:

    odd cycles   C3 0.962963  C5 0.995885  C7 0.999543  C9 0.999949  C11 0.999994  C13 0.999999
    complete     K4 0.500     K5 0.185     K6 0.049     K7 0.0092    K8 0.0012
    bipartite    K2,2 0.759   K2,3 0.583   K3,3 0.354   K3,4 0.224   K4,4 0.121
    wheels       W3 0.500     W4 0.380     W5 0.273     W6 0.200     W7 0.145
    dense random V = 8..10, p = 0.4/0.6/0.8:  down to 0.000151

**Two extremal behaviours, and nothing else close.** Trees attain equality. Odd cycles approach 1
strictly from below — for `C_m` odd, `Z = 1 - 3^-m` against a bound of exactly `1`, so the ratio is
`1 - 3^-m -> 1`. Everything with cycle rank above 1 falls away fast.

## Why it implies RC

For a linear NAE triangle system with sharing graph `G`:

    c = log2 Z(G)                                     (proved; see the Ising note)
    d_cb <= |V| - b                                   (pair-sum residual family; unsigned-incidence rank)
    RC  <=>  c <= beta (k - d_cb)                     (campaign's proved d_cb <= k)

With `k = E`, the conjecture gives `c = log2 Z <= beta(E - V + b) <= beta(k - d_cb)`. So

    **cut-inflation conjecture  =>  RC on all linear triangle systems.**

## Proof status, honestly

**A deletion-contraction recursion holds** and is verified on 27,474 connected graphs with zero
mismatches:

    F(G) = 2 F(G-e) - F(G/e).

**A one-sided induction cannot close it**, because of the minus sign: bounding `F(G)` above needs an
upper bound on `F(G-e)` AND a lower bound on `F(G/e)`. I initially tested
`2B(G-e) - B(G/e) <= B(G)`, which is a consistency property of the bound rather than the induction
step; that was my error and it is recorded here rather than quietly dropped.

**Both natural lower bounds are too weak, and fail at the same first case.** Over 27,474 graphs:

    L = 2^V 2^{E/2}                  (Jensen, since E[cut] = E/2)     valid, 0 violations
    L = 2^{maxcut} x (#optimal cuts)                                  valid, 0 violations
    induction step 2B(G-e) - L(G/e) <= B(G):   FAILS 2,552 of 21,495 for BOTH

The first failure is the triangle. `B(C3) = 27`; `B(P3) = 18` and `F(P3) = 18` so the bound is TIGHT
on the deleted graph; the contraction is a doubled edge with true `F = 10` while both candidate
bounds give `8`. Using the exact value the step reads `2(18) - 10 = 26 = F(C3) <= 27` and closes.

**So the remaining piece is sharp: a lower bound on `F` for small dense multigraphs, good enough to
beat 8 vs 10 at the doubled edge.** That is a question about `F` on multigraphs and does not involve
`d_cb`, the selector distance, or anything from Layer II. It is the kind of statement a careful
induction or a Tutte-polynomial identity should reach, and it is the piece I would hand to the next
session.

## Scope

`d_cb` is bounded ABOVE only, so every RC conclusion drawn from this is a fortiori — the safe
direction. The campaign's star family (`d_cb = k-1` where the pair-sum family gives `k`) shows the
true selector distance can be strictly smaller. And none of this touches `ell = 1`, where
`STATE_OF_THE_PROOF.md` §1 locates the sharp Rademacher conjecture's actual difficulty.
