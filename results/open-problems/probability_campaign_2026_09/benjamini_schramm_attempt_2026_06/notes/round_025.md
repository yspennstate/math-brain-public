# Round 025 log

Date: 2026-06-08

## Focus

Sharpened the nine-height decorated-strip certificate from Round 024.  The
height-transfer computation showed that the spectral-radius crossing is below
\(0.298\), so I tested rational parameters closer to the crossing.

## Exact certificate

The value
\[
  p=119/400=0.2975
\]
certifies easily.  Pushing further, the same nine-height transfer matrix at
\[
  p=743/2500=0.2972
\]
still has a positive integer Perron-Frobenius certificate:
\[
  \min_A\frac{2(M(p)v)_A}{v_A}>1.00018.
\]
Thus \(\rho(M(p))>1/2\), and Yamamoto's criterion gives
\[
  p_c(T_3\square\mathbb Z)<743/2500.
\]

The default command
`python scripts\decorated_strip_bound.py`
now verifies this sharper rational bound.

## Interpretation

The current SAW operator target after this round is
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<2500/743\approx3.36474.
\]
This is still below the best finite-length SAW certificate \(3.647512\), but it
is a meaningful improvement over the previous \(500/149\approx3.35570\) target.

I also began prototyping a sparse matrix-vector formulation for larger height
windows.  The naive frontier state space for height \(10\) is still too large
without further compression, so the next implementation target is a better
canonical state or symmetry reduction rather than just sparse storage.
