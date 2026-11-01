# Round 039 log

## Goal

Use the optimized fixed-rational decorated-strip checker to test height
\(12\) for the remaining \(T_3\Box\mathbb Z\) case.

## Additional optimization

Added transition caching to the depth-one ladder routines in
`scripts/decorated_strip_float_scan.py` and
`scripts/decorated_strip_fixedp_certificate.py`.  A ladder transition depends
only on:

- the current frontier state,
- the next height row,
- whether the next root site is seeded.

It does not depend on the full seed mask.  Caching this transition across seed
masks preserves exactness and substantially reduces the repeated local DSU
work.  The fixed-rational checker still reproduces the height-nine certificate
at \(p=7429/25000\).

## Height-twelve scan

For the side-depth-one decorated strip with height \(12\), the floating scanner
gives
\[
  \rho_{\rm lower}(p=0.2935)=0.501033137927,
\]
while
\[
  \rho_{\rm lower}(p=0.2930)=0.499793285995.
\]
Thus the observed height-twelve crossing is between \(0.2930\) and \(0.2935\).

## Exact certificate

The fixed-rational checker certifies
\[
  p=\frac{5863}{20000}=0.29315.
\]
The run used matrix size \(2^{12}-1=4095\), one-column edge count \(34\), and
certificate scale \(10^9\).  It returned
\[
  \rho_{\rm lower}=0.500165129611,
  \qquad
  \min_A \frac{2(Mv)_A}{v_A}=1.00032076793,
\]
with positive integer margin.  Hence \(\rho(M(p))>1/2\) exactly.

## New consequence

Yamamoto's criterion now gives
\[
  p_c(T_3\Box\mathbb Z)<\frac{5863}{20000}=0.29315.
\]
The corresponding SAW/operator-side target is
\[
  \gamma_{\rm SAW,2}(T_3\Box\mathbb Z)
  <
  \frac{20000}{5863}
  \approx3.411222923418.
\]
The best exact finite-length SAW bound remains
\[
  \|C_{15}\|_{2\to2}^{1/15}\le3.647511532644,
\]
so this still does not close the case, but it improves the height-eleven target
by about \(0.01160\).
