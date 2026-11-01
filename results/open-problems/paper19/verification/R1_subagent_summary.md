# R1 adversarial verification summary

Date: 2026-06-27.

Subagents used: exactly 5.

## Source theorem check

The source article proves the Gaussian row-submatrix theorem for
`F in {R,C}`:

`(1/m) log M_m^F -> -h(gamma)/d_F`

and, at the real critical phase-retrieval threshold `N=2m-1`,

`(1/m) log omega(A_m) -> -log 4`.

It also proves the real bounded-density lower side:

`P{M_m <= exp(-(h(gamma)+eps)m)} -> 0`.

It does not prove full non-Gaussian universality, nor an atomic whp dichotomy.

## Universality audit

Safe:
- Abstract first/second moment principle.
- Union-bound lower side from a one-matrix tail.
- Real bounded-density lower side using `P{s_min <= t} <= 2 K m^2 t`.

Conditional:
- Full continuous universality.
- Balan-Wang base `1/4` beyond Gaussian.

The missing input is pair correlation for exponentially small singular-value
events across overlapping row sets.

## Atomic audit

Safe:
- Expected number of singular Rademacher critical minors is exponential.
- Atomic laws obstruct direct extension of bounded-density estimates.

Safe additional theorem from the atomic reviewer:
- Every sign matrix in `{+/-1}^{N x m}` with `m>=2` and `N>=2m-1` has a singular
  `m x m` row submatrix.  Proof: partition rows by whether the first two columns
  agree or disagree; one class has at least `m` rows, and on those rows the two
  columns are equal or opposite.

Still not safe as a theorem:
- `beta=log(1/p*)` as a general singularity threshold.

These remain conjectural/conditional on a singular-minor second moment.

## Geometric audit

Fixed rectangular excess `m+r` stays on the exponential hard-edge scale with
exponent `d(r+1)`.

Proportional excess `ell/m -> beta > 1` does not: the hard-edge exponent grows
like `m`, so the minimum is at a constant Wishart-edge scale, not `exp(-cm)`.

For the `k`-th smallest singular value of `(m+r) x m` Gaussian matrices, the
hard-edge exponent is `d k(r+k)`.
