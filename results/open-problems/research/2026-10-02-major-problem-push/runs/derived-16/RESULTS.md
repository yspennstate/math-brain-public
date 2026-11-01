# Derived-16 research result: exact boundary of colored binary averaging for ML10

## Verdict

This checkpoint does **not** solve the Möbius-ladder case of Sidorenko's
conjecture.  It proves a restricted two-state quartic lemma and, more
importantly for the research program, gives an exact actual-host obstruction
to the stronger coefficientwise averaging strategy.

## Completed mathematics

For any entrywise-nonnegative symmetric `2 x 2` base matrix A and arbitrary
real symmetric `2 x 2` perturbation B, the ML10 colored density with B on a
chosen square and A on the other eleven edges is nonnegative.  Exact
enumeration writes the quartic as three nonnegative fourth-power terms plus
`w^2(Cu^2+Euv+Dv^2)`.  The polynomial `4CD-E^2` has 66 nonzero monomials,
every coefficient positive (minimum 24, maximum 16,008), proving the final
quadratic is PSD.  An independent left-label elimination reproduces all six
coefficient polynomials and the complete determinant certificate.

The natural extension “every even colored coefficient is nonnegative” is
false.  On the explicitly given strictly positive mean-one sixteen-state
Boolean convolution kernel, the sixth coefficient is

`-809116997184077332220240713482240 / 1524^15`.

Three independent exact computations agree: literal even-subset full
transfers, Walsh translation blocks, and a direct 3,932,160-term Kirchhoff
Fourier-flow sum.  The total averaging difference is positive and the full
density is about 70.6086, so this is a proof-method obstruction, **not** a
Sidorenko counterexample.

The C4 transfer/reflection/Walsh formulas were independently checked.
Individual character contributions can be negative for an admissible q=4
host, ruling out termwise character positivity.  q=32 and q=64 searches
found no global C4 counterexample, but are numerical evidence only.

## Audit and status

Root reran five exact programs; all exited zero.  The independent C6 checker
enumerated the literal graph rather than importing the author's transfer
words, and the two-state checker used a separate variable-elimination order.
Current primary sources were checked through 3 October 2026.  Historical
novelty and external peer review remain unverified.

Unrestricted ML10 Sidorenko, global colored C4 positivity, total binary
averaging monotonicity, full Boolean FEI, the full forest negative-dependence
conjecture, and Kaplansky/direct finiteness remain open in this campaign.

