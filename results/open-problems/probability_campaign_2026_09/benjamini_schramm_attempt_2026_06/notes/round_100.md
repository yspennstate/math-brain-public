# Round 100 log

## Goal

Give the far-leg square tail a direct percolation interpretation.

## Result

Added `lem:far-leg-cluster-interpretation`.

For two independent Bernoulli-\(p\) configurations and clusters \(C_i(z)\),
\[
  \bar\chi_p |K|\mathcal R_p^{>R}(K)
  =
  \sum_z
  \mathbb E_p^{\otimes2}
  \bigl[
    |(K\setminus B(z,R))\cap C_1(z)|
    |(K\setminus B(z,R))\cap C_2(z)|
  \bigr].
\]

## Interpretation

The remaining far-leg tightness estimate is a normalized same-root overlap
tail for two independent clusters.  This should make future
backscattering/separator arguments easier to state in probabilistic language.
