# Least singular value of a coordinate-optimized Gaussian submatrix

`main.tex` (`main.pdf`) proves that for an `N x N` matrix `A` with i.i.d. standard real or complex
Gaussian entries and a fraction `alpha in (0,1)`, the minimum of the smallest singular value over all
`alpha N x alpha N` submatrices,

    M_N(alpha) = min_{|S|=|T|=alpha N} sigma_min(A[T,S]),

satisfies `-(1/N) log M_N(alpha) -> 2 H(alpha) / d_F` in probability, where `H` is the binary
entropy and `d_F` is 1 (real) or 2 (complex). This is the sharp large-deviation exponent; previously
only the surrounding bounds `H(alpha)/d_F` and `2H(alpha)/d_F` were known for the square two-sided
minimum. More generally, for `(alpha N + r) x alpha N` submatrices (r surplus rows, r fixed) the
exponent is `2H(alpha)/(d_F (r+1))`.

The upper bounds are first moments. The lower bounds are second moments on a marked-row
construction. The new analytic ingredients are a two-direction small-ball estimate (sharp up to a
logarithmic factor uniformly in the angle) and, for the surplus case, a second tail bound for the
overlap of two constructed normals through the fresh-row Haar direction.

Two consequences are recorded: the achievable exponent for support-optimized products of Gaussian
matrices improves to `2H(alpha)/d_F`, and for Rademacher entries the minimum vanishes outright for
all `alpha <= 1/2` (and is positive for `alpha > 0.9051...`), so the constant is not
distribution-free.

## Numerics
- `numerics/verify_key_lemma.py` — Monte Carlo for the two-direction estimate: the ratio
  `q_D(t)/p(t)^2` grows like `log(1/t)` at `D=2`, tends to 1 as `D` grows, and stays far below the
  crude `1/p(t)`.
- `numerics/verify_O1_finite_size.py` — exhaustive `M_N(alpha)` at `alpha=1/2` versus the
  first-moment scale; the measured exponent matches the prediction for `N = 8,10,12` and rises
  toward `2H(1/2)/d_F`.
- `numerics/verify_surplus_finite_size.py` — the same check with one surplus row (`r=1`), matching
  the first-moment scale in both fields and rising toward `2H(1/2)/(2 d_F)`.
- `numerics/t2_support_min_sv.py` — exhaustive `-(1/N) log M_N` at small `N`, real and complex.
