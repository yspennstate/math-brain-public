# B05 / A023 — shared star--point-defect payment

Run: `20261013T084137Z-fleet01-B05-star-defect-shared-a023`  
Primary packet: **A023 (Amortized rarity budget)**  
Stable gap: `B05_RARE_REFUNDS`  
Claim version: `B05_A023_SHARED_STAR_DEFECT_v1`  
Status: **AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW**  
Full FEI: **OPEN**

## Result

The preceding complete theorem for quadratic controls required a disjoint
retained core.  This run removes that hypothesis for a first unbounded,
restriction-stable shared-variable family.

Let

\[
P_{m,R,\varepsilon}(x,y)
=(-1)^{x(\varepsilon+\sum_{j\in R}y_j)}
\left(1-2\mathbf1_{\{y=0\}}\right),
\]

where `m >= 1`, `emptyset != R subseteq [m]`, and `eps in {0,1}`.  For any
arbitrary Boolean `h` on a disjoint terminal block, put `F=Ph`.  Every finite
adaptive/pruned restriction tree on the `P` block satisfies

\[
\boxed{
U(F)-\sum_\ell w_\ell U(F_\ell)
\le2\le4I_{\{x,y\}}(F).
}
\]

The terminal packet `U(h)` is retained exactly once.  The bound is independent
of defect dimension, star weight, affine phase, restriction order/depth, and
terminal-core complexity.  For the base class,

\[
U(P)\le4I(P),\qquad H(P)\le10I(P).
\]

This is a proper class extension beyond disjoint products: the selector phase
and point defect share all `y` variables.

## Method

The full squared Fourier law has only four exceptional atoms and a uniform
tail.  Exact formulas for both affine phases reduce the problem to `(m,r)`.
All `m <= 9` rows are certified by exact Walsh arithmetic and positive-series
rational intervals for logarithms.  For `m >= 10`, the uniform tail has mass
below `4*2^{-m}` and costs at most `8(m-1)2^{-m}`; four scalar logarithmic
envelopes finish the dimension-free tail.

The finite certificate reports

- `90` parameter rows and `90` direct Walsh reconstructions;
- `33,322` assertions;
- maximum certified finite `U` upper endpoint `1.912217876358139`;
- maximum certified one-node `Delta_x U` upper endpoint
  `1.073327087360621`;
- analytic tail envelopes below `1.082`.

## Failed stronger route retained

Small exhaustive and targeted searches suggested the more general orbit
inequality `Delta_x U <= 2` whenever the two children differ by a character.
The entropy part is easy, but the needed upper-mass logarithm comparison was
not proved pointwise; a three-bit orbit has a positive pointwise defect.
That unproved inequality is not used here.

## Exact remaining obstacle

The proof relies on the one-defect law: four exceptional atoms plus a uniform
tail.  Multiple coherent defects create intersecting principal filters, while
a general shared core has no uniform tail.  The next step is to replace the
single tail estimate by a nonreused displacement-filter refund for two defects,
or to produce a falsifier showing that root source influence must be augmented
by a retained data-core packet.  A directional payment by only the actually
queried influences is not claimed.

Independent A087/A094 review is required before adoption.
