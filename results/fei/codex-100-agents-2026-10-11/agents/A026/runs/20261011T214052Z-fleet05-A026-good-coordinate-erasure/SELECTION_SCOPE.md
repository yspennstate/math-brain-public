# Selection scope

The universal target stays OPEN. All statements use physical coordinates and bit entropy.

Closed locally, pending independent review: every nonconstant Boolean function whose nonzero Fourier support has affine F2 dimension at most four has a relevant coordinate with B_i <= (7/2) I_i. Arbitrary disjoint products of such factors inherit the same selection constant. The physical restriction class is hereditary. The proof and exact integer exhaustive certificate are in GOOD_COORDINATE_TARGET.tex and out/.

Rule: choose a nonconstant factor. Form the direction space of its support. If a relevant unit coordinate vector is outside it, query that coordinate at zero actual entropy decrement. Otherwise there are at most four relevant variables; choose a coordinate minimizing the exact amplitude proxy/influence ratio, whose integer certificate is <=7/2. This is an existential rule; no all-coordinate bound is asserted.

The finite constant is sharp for the amplitude proxy through four variables, not asserted sharp for B_i or FEI. The resulting entropy bound is H <= (7/2+2/ln 2) I on the stated class. FEI for bounded-size gates and many parity/composition classes was already known; the contribution here is a directly executable physical selection certificate and its stated hereditary scope, without a literature-priority claim.

Frozen stress family: symmetric thresholds at explicitly listed n=8,16,32,64. A threshold at n=32,t=24 gives an exact all-coordinate failure of proxy K=4. This is a different statement from failure of actual B_i selection and does not duplicate the recovered K=4 erasure counterexample as a new result.

First unsupported universal step: show a dimension-independent bound for the minimum true B_i/I_i when no zero-erasure coordinate exists and the affine support dimension is unbounded. The stronger amplitude proxy may be too expensive; its unrestricted finiteness is also unproved here. Next mathematical action: derive its asymptotics for symmetric thresholds with t=n/2+c sqrt(n), retaining exact binomial expressions, to determine whether to discard that proxy before more searches.

Reviewers requested by packet: A087 and A094. Suggested scope of review: scalar bound, certificate domain/symmetry, direction-space reduction, heredity, tensor invariance, then exact mismatch identity and influence telescope.
