# Two untried approaches, second pass, 2026-10-11

Remaining gap from ATTEMPT.md: a matching iid weak-moment upper rate
in almost-sure southwest-rectangle discrepancy, or a sharper lower bound.
The previous rare-tail argument misses all n^2 tail variables and proves
only the necessary exponent bound 2eps/(2+eps) for eps<2/3.

1. **Quantitative Hermitized comparison, rather than eigenvalue rank bounds.**
   Compare the truncated and original shifted matrices through singular
   values, where rank interlacing and Hoffman–Wielandt DO apply. Use a
   regularized logarithm, optimize its cutoff against the moment tail,
   and explicitly expose the small-singular-value term. Seek a neighbour
   theorem (Gaussian smoothed analysis, a Wegner bound, or weak-moment
   singular-value local law) that pays that term. This can produce a
   rigorous transfer theorem even if a matching spectral rate remains out
   of reach. It was not carried out in the first attempt.

2. **Fill the spectral edge from a finite-(4+eta)-moment bulk local law.**
   Use Götze–Naumov–Tikhomirov's local circular law and Götze–Jalowy's
   edge-excluded discrepancy theorem, then bound the missing annulus and
   the exterior by a shrinking cutoff. A full-domain rate would be a
   stronger special case than the all-moments input. The principal risk:
   a theorem uniform only for fixed distance from the edge cannot be
   applied at distance n^(-c) without explicit control of constants.

I pursue approach 1 first: it directly targets eps-dependence and admits
exact deterministic checks. Approach 2 is retained as an independent
alternative, not assumed solved by applying a fixed-parameter theorem
to a moving parameter.

Brain gap queries (read-only): “circular law weak moments quantitative
Hermitization upper bound Götze Tikhomirov”; “small singular values
Gaussian perturbation Wegner estimate logarithmic integrability”.
The first returned source/rate cards and neighbouring sparse covariance
local-law cards, but no matching upper theorem. Every returned card is
treated as a lead, not a verdict.
