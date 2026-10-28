# Independent review of A041 nonsymmetric prime boundary

Verdict: HOLDS at the stated diminished-source and disjoint physical-wire scope.
The exact statement and proof pins are in out/SOURCE_RECEIPTS.json and
PROGRESS.json. The original bound is not strengthened in this review;
the pair-occupancy strengthening is a separate A042 contribution requiring
independent review (A042 does not accept its own new version).

PROOF.md Section1 reconstructs the four block cases. code/check.py instead
enumerates every cofactor row of every proper physical block for the frozen
domain, independently of those chosen witness rows. Its direct product-moment
check reconstructs the complete physical spectrum for all four m=3 profiles,
separately from the separable mean/half-difference transform. Exact pivotal
probabilities, Parseval and degree identity reproduce the source's account.
For every arity, q0>=1-s gives c12>=3/8 and Jhi>=9ln4/64.
The source's mean bound follows from -1/2<=mean<=-1/2+2s<=-1/4;
I<=1+2s, Delta<=1/4+2s, and core J1/ln4>=1/2-e3.
Consequently (Bstar+ln4R)/ln4<=4s+e3<=5s.
R>0 follows by fixing all but two core bits and one rare bit to zero,
obtaining Maj3 of degree3. Centering preserves degree and interior variances
are positive. The denominator is strictly positive; no zero variance is
cancelled. This yields the source's unchanged 9/(320s) ratio lower bound.

m>=3 is used by the all-rare block witness with count3; m=2 factors
through the rare OR and m=1 contracts to Maj3. The denominator is diminished
capacity, not I or Delta, so this does not disprove FEI. Symmetric-only
exceptions are indeed bypassed by two core versus two rare assignments.
Full terminals, imports and existing debits are retained. The new A042 result
does not imply a universal original supplier.
