# Route log: rank-one weighted `K_{2,3}`

## Route A: exact Rayleigh-template factorization — successful

Constructed the 32-term spoke polynomial from 54 backbone forests and used
arm permutations plus endpoint exchange to reduce ten Rayleigh differences
to three templates.  Shifting by the natural one-vertex partition functions
turned every decisive discriminant into a binary form.  Four exact principal
minor certificates close the proof.

## Route B: boundary-first degeneration analysis — successful and necessary

The endpoint--internal leading coefficient is proportional to `x^2 y^2`, so
the generic discriminant argument alone leaves two axes untreated.  Direct
factorization on each axis produced positive multiples of `x^2` or `y^2`.
This removes a real logical gap that a generic-parameter calculation would
miss.

## Route C: coefficientwise positivity — partially failed, then repaired

The internal--internal discriminant form has a mixed coefficient with both
signs, so coefficientwise positivity of the form fails.  The repaired route
computes its `2 x 2` determinant.  That determinant factors into three linear
positive factors and the coefficient-positive polynomial `S(a,b,c)`.

## Route D: exact rational reconstruction/stress testing — independent audit

A separately written checker reconstructs the polynomial and tests all ten
pairs at exact rational parameter/shift profiles.  This is an audit channel,
not the proof itself; the symbolic determinant identities are the proof.

## Next obstruction

For six arbitrary backbone weights there is no common arm multiplier, so the
rank-one determinant factors need not survive.  The most informative next
step is to perturb a single edge off rank one and analyze the first signed
coefficient/determinant obstruction, rather than launching an undirected
six-parameter expansion.

