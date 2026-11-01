# Round 026 log

Date: 2026-06-08

## Focus

Sharpened the same nine-height decorated-strip certificate and bracketed the
limit of this particular transfer matrix.

## Exact certificate

The rational value
\[
  p=29717/100000=0.29717
\]
certifies with exact integer arithmetic.  Pushing slightly lower, the value
\[
  p=7429/25000=0.29716
\]
also certifies:
\[
  \min_A\frac{2(M(p)v)_A}{v_A}>1.00004.
\]
Therefore
\[
  p_c(T_3\square\mathbb Z)<7429/25000.
\]

The value
\[
  p=14857/50000=0.29714
\]
has floating-point spectral radius below \(1/2\), and the same exact
certificate check correctly fails.  Thus the nine-height depth-one strip is
essentially exhausted; further \(p_c\)-side progress needs a larger strip or a
new state-space compression.

## Interpretation

The current SAW operator target is now
\[
  \gamma_{\rm SAW,2}(T_3\square\mathbb Z)<25000/7429\approx3.36519.
\]
This is a small numerical improvement over \(2500/743\approx3.36474\), but the
main value of the round is bracketing the present transfer method's limit.
