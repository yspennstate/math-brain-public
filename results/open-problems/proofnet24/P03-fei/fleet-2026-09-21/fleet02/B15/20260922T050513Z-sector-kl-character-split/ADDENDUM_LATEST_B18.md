# Addendum — compatibility with the fresh fleet04/B18 unequal-MUX interface

After the main B15 report was committed, the completed fleet04/B18 handoff `20260922T045533Z-mux-joint-credit-collapse` became available on fresh master and was read in full. It proves for the unequal-data one-bit MUX that the selector information credit vanishes exactly on

\[
t=1/2,\qquad q_0=1/2\ \text{or}\ q_1=1/2,
\]

and reduces either zero-credit line to the one-dimensional potential inequality

\[
\Gamma(1/4+s/2)\le C-2+\Gamma(s)/2.
\]

This is **exactly incompatible** with trying to use the present sector-KL payment on that remaining line: B18's zero-credit theorem says the selector child spectra are disjoint there, so every information-sector lower bound is necessarily zero. The new B15 theorem instead treats the complementary geometry where both cofactors are balanced and one is a character; then the two child spectra share the character mode, while the nonshared sector has posterior `1/2` and mass `2d(1-d)`, producing the indispensable `d log(1/d)` KL payment.

Thus the two results separate the selector problem cleanly:

- **shared-character / rare-disagreement geometry:** preserve posterior KL; the B15 sector theorem closes the local step for every center `C>=6.387646448685102...`, hence for `C^dagger`;
- **disjoint-support MUX zero-credit geometry:** no information credit exists to spend; one must prove B18's source-potential inequality (or refute the candidate) by potential arithmetic/AND descendants, not by another KL lower bound.

This prevents double-counting and prevents wasting the next B15 run on an information-credit mechanism that is provably null on B18's remaining zero-credit frontier. Full FEI remains OPEN.
