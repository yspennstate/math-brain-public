# Round 024 log

Date: 2026-06-08

## Focus

Improved the decorated-strip \(p_c\) comparison by replacing the direct
edge-subset enumeration with an exact transfer along the height direction.

## Height-transfer method

For the depth-one decorated strip, one column is a two-lane ladder: the geodesic
fiber, one side fiber, vertical edges in both fibers, and rungs between them.
Instead of enumerating all \(2^{3h-2}\) edge configurations, the transfer keeps
only:

- the two frontier components at the current height;
- whether each component is connected to the seed set;
- the mask of geodesic heights already contained in each frontier component;
- the finalized output mask.

This computes the same exact closure counts by open-edge number, but makes the
nine-height window practical.

## New exact certificate

With heights \(\{-4,\ldots,4\}\), the one-column ladder has \(25\) edges and
the transfer matrix acts on \(2^9-1=511\) non-empty masks.  At
\[
  p=149/500,
\]
exact integer arithmetic certifies a positive vector \(v\) with
\[
  \min_A \frac{2(M(p)v)_A}{v_A} > 1.00344.
\]
Therefore \(\rho(M(p))>1/2\), and Yamamoto's criterion gives
\[
  p_c(T_3\square\mathbb Z)<149/500.
\]

This improves the previous decorated-strip bound \(303/1000\).  The computation
is reproducible with the default command
`python scripts\decorated_strip_bound.py`.

## Interpretation

The SAW operator target after this round is
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<500/149\approx3.35570.
\]
The best current finite-length SAW certificate is \(3.647512\), so the case
still remains open for this route.  The next natural \(p_c\)-side experiment is
a larger height window using the same transfer, or a transfer that allows
deeper finite side trees without returning to full edge enumeration.
