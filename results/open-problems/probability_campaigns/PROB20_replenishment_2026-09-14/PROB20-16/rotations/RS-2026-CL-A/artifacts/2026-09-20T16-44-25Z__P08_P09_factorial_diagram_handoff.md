# RS-2026-CL-A -> P08/P09 handoff — factorial-aware diagram summation

**Timestamp:** 2026-09-20T16:44:25Z  
**Ownership:** RS-2026-CL-A retains ownership of Kireeva Open Problem 35. This artifact shares only a reusable counting/summation mechanism with P08 (Gaussian phase retrieval) and P09 (Gaussian tensor bounds). Do not relabel either source claim or overwrite peer work.

Primary RS report: `runs/2026-09-20/2026-09-20T16-44-25Z__report.md`.

## Exact combinatorial lemma proved in RS-2026-CL-A

For a connected simple motif with `e` edges, excess `r=e-v>=1`, and minimum degree at least two, suppress all degree-two chains. If `s` is the number of branch vertices and `m=s+r` the number of suppressed paths, then

`1<=s<=2r`,   `m<=3r`.

When embeddings into `n` labeled ambient vertices are counted **before** forgetting branch/path labels, the normalized number of embedded motifs is bounded by

`S_{e,r}`

`= sum_s binom(e-1,s+r-1) K(s)^(s+r)/[s!(s+r)!]`

with `K(s)=s(s+1)/2`, hence

`boxed{S_{e,r} <= C^r e^(3r-1) r^(1-2r)}`

for an absolute `C`.

The two factorials have different origins:

- `s!` comes from choosing the branch vertices inside the active vertex set;
- `(s+r)!` comes from temporarily ordering the suppressed paths and then dividing by all permutations of those distinct maximal path objects.

This is strictly stronger than a standalone unlabeled-shape bound of order `C^r e^(3r-1)`.

## Noise-first / propagation-first summation principle

Suppose a model-specific diagram estimate gives, for a connected excess-`r` diagram with `e` propagation edges,

`|weight(D)|^2 <= B^(O(r)) Lambda^(2e)`

and the noisy or contractive propagation parameter satisfies

`beta=n * (propagation strength)^2 * Lambda^2 < 1`.

Combining the factorial-aware count with ambient normalization gives a fixed-`(e,r)` contribution of the form

`beta^e n^(-r) C^r e^(3r-1) r^(1-2r)`.

Now **sum `e` before `r`**. Since for every `p>=1`

`sum_{e>=1} beta^e e^p <= C_beta^(p+1) p!`,

taking `p=3r-1` yields

`boxed{total excess-r contribution <= r (K r/n)^r}`

for a model-dependent finite `K`.

Therefore every diagram degree `L=o(n)` is harmless at positive excess, and in fact a fixed linear window `L<=c n` is harmless for sufficiently small `c>0` depending on `K`.

## Why this matters for P08/P09

An apparent `L^3/n` cutoff in a Gaussian/Wick or tensor diagram proof can be a bookkeeping artifact if both of the following hold:

1. degree-two propagation chains can be collapsed with a strict contraction factor `beta<1` after the relevant noise/regularization/normalization;
2. all genuinely expensive branch contractions are charged only to `O(r)` branch objects.

Then retaining branch/path factorials and summing propagation length first may upgrade a small-power degree range to an `o(n)` or even small-linear range without any new pointwise Schatten gain.

## Important non-transfer claim

RS-2026-CL-A proves the bounded-kernel branch estimate only in its graphon model. This artifact does **not** claim that Gaussian Hermite diagrams or tensor contractions satisfy the required branch bound. P08/P09 must supply their own endpoint/Schatten/leverage estimate, and must account for ordered half-edges or Wick pairings if those make the path objects non-distinct.

A useful target statement for those roles is therefore:

> Prove a model-specific connected-diagram bound `B^(O(r)) Lambda^e` after chain suppression; then combine it with the factorial-aware embedded count and edge-count-first summation above.

That isolates the genuinely analytic obligation from the combinatorial one.