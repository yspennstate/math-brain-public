# Affine addendum — countable rational-grid reduction survives arbitrary conditioning leakage

This addendum strengthens `QFORM-COUNTABLE-EXTREME-WITNESS-v1` to the affine quadratic forms that arise after conditioning outside coordinates.

For

`P_(A,b,c)(x)=x^T A x+2 b^T x+c`,

let `C_aff` be the supremum of

`P{P_(A,b,c)(X) in I}/|I|`

over every finite dimension, every independent cap-one product law, every real symmetric `A` with `s_3(A)>=1`, arbitrary real `b,c`, and every nondegenerate interval `I`.

Let `C_aff,grid` be the same supremum restricted to:

- `A` rational symmetric with `s_3(A)>1`;
- `b` and `c` rational;
- rational intervals;
- product indicators of compact finite rational-grid interval unions of measure one in every coordinate.

Then

`boxed: C_aff = C_aff,grid.`

## Proof

The easy inequality is inclusion. For the reverse, take an arbitrary datum with ratio `R` and fix `epsilon>0`.

1. Choose `s>1` close to one and replace `(A,b,c,I)` by `(sA,sb,sc,sI)`. The event is unchanged, the interval length is multiplied by `s`, and `s_3(sA)>=s`; hence the ratio is divided only by `s` and can be kept above `R-epsilon/4`.
2. Apply fleet04/B14 finite-mixture localization to the product law and select one compact rational-grid product-indicator component whose slab probability is within an arbitrarily small additive loss of the original one.
3. On its compact support `K`, choose `L` with `||x||<=L`. Approximate `(sA,sb,sc)` by rational `(B,d,e)` so that

   `||B-sA||_op L^2 + 2||d-sb||_2 L + |e-sc| < eta`

   and simultaneously `||B-sA||_op<(s-1)/2`. Then

   `sup_(x in K) |P_(B,d,e)(x)-P_(sA,sb,sc)(x)|<eta`

   while `s_3(B)>(s+1)/2>1`.
4. Enlarge `sI` by `eta` on each side and then by an arbitrarily small extra amount to a rational interval `J`. The old event is contained in the new rational event; choosing all approximation parameters sufficiently small keeps the slab ratio above `R-epsilon`.

Thus every affine slab ratio is approximable from below by the countable rational-grid class, proving equality of the suprema.

## Relevance

This is the form needed after conditioning: arbitrary outside coordinates generate deterministic affine coefficients in the active original-coordinate block. No support radius, moment, centered law, connected support, or bounded fragment count is introduced. The approximation parameters may depend on the datum; no uniform mesh or radius is asserted.

As in the main report, this is an essential-density/small-ball reduction. Total-variation approximation alone does not transfer continuity.
