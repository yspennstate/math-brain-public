# Round 027 log

Date: 2026-06-08

## Focus

Made the depth-one decorated-strip computation sparse enough to handle the
ten-height strip.

## Sparse transfer

The dense implementation stored the full closure tensor and then built a dense
matrix.  For height \(10\), that is unnecessary.  The revised computation stores
only the non-zero output masks for each seed mask, and applies the transfer
matrix to a vector by:

- first evaluating the expected value after the column closure for each seed;
- then summing over horizontal seed subsets of the current mask.

This avoids forming the \(1023\times1023\) dense matrix.  The frontier state
profile for height \(10\) remains manageable: the largest seed class reached
about \(50{,}448\) frontier states.

## Exact certificate

For the ten-height window \(\{-4,\ldots,5\}\), the one-column ladder has
\(28\) edges.  At
\[
  p=591/2000=0.2955,
\]
exact integer arithmetic verifies
\[
  \min_A\frac{2(M(p)v)_A}{v_A}>1.00016.
\]
Therefore
\[
  p_c(T_3\square\mathbb Z)<591/2000.
\]

The default command
`python scripts\decorated_strip_bound.py`
now verifies this height-ten certificate.

## Interpretation

The SAW operator target is now
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<2000/591\approx3.38409.
\]
This is a larger improvement than the final nine-height sharpening.  The next
decorated-strip target is to locate the height-ten crossing more sharply, then
try to compress the frontier state further for height \(11\).
