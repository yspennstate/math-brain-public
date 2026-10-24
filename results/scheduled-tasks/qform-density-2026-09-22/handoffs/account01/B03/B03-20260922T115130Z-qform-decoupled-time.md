# account01/B03 handoff — mixed-minor decoupled time estimate

Run: `B03-20260922T115130Z-qform-decoupled-time`  
Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`  
Classification: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics: `yspennstate/math-open-problems@f2f04d1933c12fd58c9abf12dcb8bcf2877b172c`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/B03-20260922T115130Z-qform-decoupled-time/REPORT.md`, blob `e7242beb6f35026b45b970af870a02eca3010cbe`.

Named partner applied: account02/B03 report `yspennstate/math-open-problems@b4736d3226c5ffb46bda90b98c1a7b0ac28454b3:proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260922T114427Z-b03-qform-a11/REPORT.md` (blob `363519157d63781d00966b0ff1dd1733d3681a49`). Its exact `(U_i,V_i)` dependence correction and its proof that scalar one-copy symmetrization cannot recover linear small-ball scaling are used directly.

New theorem `QFORM-MIXED-MINOR-L2-v1`: if disjoint coordinate sets `I,J` have equal size `m>=3` and `C=A[I,J]` is invertible, then

`|phi_Q(t)| <= min(1, pi^(m/2)|det C|^(-1/2)|t|^(-m/2))`

and hence

`||p_Q||_infinity <= [m/(m-2)] |det C|^(-1/m)`.

For `m=3`, `||p_Q||_infinity <= 3 |det A[I,J]|^(-1/3)`. The proof conditions all other coordinates, absorbs arbitrary principal-block quadratics into unimodular `L^2` amplitudes, and applies Cauchy + change of variables + Plancherel. No condition is imposed on `A[I,I]` or `A[J,J]`.

Fresh account02/B09 correction `QFORM-CROSSMINOR-ALONE-FALSE` was consumed. It refutes a `2x2` cross-minor-only claim; the present proof is compatible because `m=2` gives only the nonintegrable borderline `|t|^-1` estimate and no density conclusion.

First unpaid implication: `QFORM-AGGREGATED-MIXED-MINOR-L1` — replace single-minor selection by determinant-weighted/BL aggregation over many triples so Cauchy-Binet mass yields a dimension-free `L^1_t` estimate in flat rank-three frames, while preserving the original product law and handling extra spectral directions.
