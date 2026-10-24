# Route log: arbitrary weighted `K_{2,3}`

## Route A: transverse rank-one deformation

Started by freeing one edge from the rank-one family.  Keeping the six
weights symbolic showed that no rank-one identity was actually needed in the
endpoint templates, so the calculation was promoted immediately to six
independent variables.

## Route B: three generic Rayleigh templates — successful

Column relabeling and endpoint exchange reduce ten parameter-labeled pairs to
three identities.  Natural one-vertex partition-function shifts make each
Rayleigh difference quadratic in an unused spoke.  Exact determinants close
the endpoint--endpoint and endpoint--internal templates, including both
degenerate axes.

## Route C: coefficientwise positivity — failed, repaired topologically

For the internal--internal discriminant, both diagonal entries have signed
coefficient expansions (31 negative terms among 166 in each generic
diagonal), and the mixed entry is also signed.  Coefficientwise positivity is
therefore false as a proof route.  Its determinant nevertheless factors into
three strictly positive AM--GM forms and a coefficient-positive polynomial.
The determinant prevents either diagonal from vanishing; connectedness of
the positive orthant and one exact positive basepoint determine the sign.

## Route D: counterexample search / independent reconstruction

The earlier 36-million-evaluation search supplied only motivation.  The
theorem rests on symbolic identities, not sampling.  A separately written
component-factor checker and audit reconstruct all three templates and test
exact rational profiles.

## Remaining boundary

The next graph-theoretic question is not another weighting of `K_{2,3}` but
whether this certificate survives subdivision or two-terminal composition.
No closure claim is made here.

