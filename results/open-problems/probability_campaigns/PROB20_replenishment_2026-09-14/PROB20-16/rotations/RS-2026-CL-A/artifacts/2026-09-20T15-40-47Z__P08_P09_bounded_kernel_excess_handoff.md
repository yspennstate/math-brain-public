# P08/P09 handoff from RS-2026-CL-A — bounded-kernel excess contraction

**Timestamp:** 2026-09-20T15:40:47Z  
**Ownership:** RS-2026-CL-A retains ownership of the Kireeva low-degree source claim. This file shares only reusable analytic lemmas with P08 (Gaussian phase retrieval) and P09 (Gaussian tensor bounds). Do not relabel either role's source problem or overwrite peer reports.

Primary RS report: `runs/2026-09-20/2026-09-20T15-40-47Z__report.md`.

## Exact proved kernel-chain lemma

Let `(S,mu)` be a probability space and let `T` be the self-adjoint integral operator with bounded symmetric kernel `W`. Put

`Lambda=||T||_op>0`,    `M=||W||_infty`,

and

`B=max{1,M/Lambda,(M/Lambda)^2}`.

If `W^{(ell)}` is the kernel of `T^ell`, then for every `ell>=1`,

`|W^{(ell)}(x,y)| <= B Lambda^ell`                         (1)

for a.e. `(x,y)`.

For `ell=1` this is the `L_infty` bound. For `ell>=2`, with `W_x(z)=W(x,z)` and `W_y(z)=W(z,y)`,

`W^{(ell)}(x,y)=<W_x,T^{ell-2}W_y>`,

so

`|W^{(ell)}(x,y)| <= M^2 Lambda^{ell-2} <= B Lambda^ell`.

## Excess suppression consequence

Suppose a connected contraction diagram is graph-like, every degree-one vertex vanishes by centering, and a connected non-cycle diagram has `e` propagator edges and excess

`r=e-v>=1`.

Suppress all maximal degree-two chains. The residual branch multigraph has at most `2r` vertices and `3r` edges. If the diagram permits the same path integration as above, then

`|diagram(F)| <= B^{3r} Lambda^e`.                         (2)

Thus long propagation chains pay only the spectral factor `Lambda^length`; endpoint/dimension losses are charged only to `O(r)` branch objects.

## Why this may matter for P08/P09

For Gaussian/Wick and tensor contraction expansions, a recurrent source of dimension loss is bounding every edge or chaos level separately. The RS proof shows a different accounting principle:

1. identify degree-two propagation chains;
2. collapse each chain using the operator norm;
3. pay leverage / endpoint / Schatten losses only at the residual branch kernel;
4. enumerate by excess, not total degree.

The companion RS enumeration also improved the generic graph-shape count to

`N_{e,r} <= C^r e^{3r-1}`,

which is the natural cubic-kernel scale after degree-two suppression.

## What is *not* transferred as a theorem

No Gaussian phase-retrieval or tensor conjecture is claimed solved here. To use (2), P08/P09 still need a model-specific analogue of the endpoint estimate in (1), for example a uniform `L2 -> L_infty`, leverage, or Schatten branch-contraction bound. Hermite functions are unbounded pointwise, so the Boolean/graphon `L_infty` step cannot simply be copied.

A useful target inequality is therefore:

`|chain_ell(a,b)| <= C_end Lambda^ell`

with `C_end` independent of `ell`, followed by a branch estimate growing only exponentially in excess. If obtained, the same suppression/counting scheme can replace total-degree dimension losses by excess-dependent losses.
