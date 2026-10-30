# Late partner application — forced leakage versus the new clean-bank endpoint

Run: `20260922T212423Z-fleet02-B05-QFORM-r17`
Status: **ESSENTIAL_STEP_APPLIED; full QFORM OPEN**.

After the immutable main report was written, a fresh path-scoped source check found the newer completed named-partner result fleet03/B05 run `20260922T203915Z-fleet03-B05-QFORM-r17`, canonical mathematics

`yspennstate/math-open-problems@a48f196ab8489a9a83edc4d1c03630f9788c6978`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260922T203915Z-fleet03-B05-QFORM-r17/REPORT.md`.

This supersedes r16 as the newest completed named-partner source, while r16 remains a dependency for the pair-log inequality used in the main report.

## 1. Partner result actually applied

The partner proves `QFORM-LEAKAGE-FREE-TRIBANK-EXTRACTION-FALSE-v1`. For the rank-three projection `P_n=R_n R_n^T`, with rows of `R_n` equal to

`(1/sqrt(n), sqrt(2/n) cos(2pi k/n), sqrt(2/n) sin(2pi k/n))`,

the nonzero spectrum is exactly `{1,1,1}`. Every original-coordinate bank that is scalar-sufficient — after conditioning outside original coordinates, the conditional polynomial depends on the bank only through one scalar linear form — must be a singleton. Hence every leakage-free three-scalar core is a physical principal triple and has

`sigma_min <= trace/3 = 3/n`.

Thus no uniform clean scalar-bank extraction exists, even though the same diffuse family is uniformly paid by the completed ridge-window theorem.

The partner also gives the exact projection compression identity

`E E^T = M-M^2`,

where `M=U^T P U` is a compressed core and `E=U^T P W` is its coupling to an orthogonal complement. Therefore a compressed eigenvalue `mu` in `[s,1/2]` forces leakage singular value at least `sqrt(s/2)`.

## 2. Interaction with the new B05 theorem

The main report proved `QFORM-DISJOINT-BANK-INDEFINITE-PAIR-COAREA-v1`: a whole physical bank may be compressed before inversion when it enters the paid part only through one scalar `L=b dot Y`; after Ball normalization this gives a dimension-free pair-coarea estimate and, on the target-valid star family, the explicit bound `<13.455`.

The partner's full-spark projection is a source-valid obstruction to making that clean-bank endpoint exhaustive. On `P_n`, every nontrivial multi-coordinate scalar aggregate necessarily leaves another active direction in the same bank. Hence the correct synthesis is: clean scalar-sufficient bank is paid by the new aggregate pair theorem; genuinely nonreducing compression carries quantitative leakage currency; the remaining proof debt is to spend the core and that leakage jointly in original product coordinates, without conditioning on a rotated residual coordinate from the same bank.

This is an actual application of the newer named-partner result: it rules out the stronger universalization of the main theorem and identifies a quantitative resource that any extension must retain.

## 3. Sharpened first unpaid implication

`QFORM-COMPRESSED-CORE-PLUS-PRODUCT-LEAKAGE-COAREA-v1`:

Given a density-normalized compressed core on disjoint physical banks and nonzero same-bank leakage, prove a dimension-free small-interval/coarea inequality that consumes the two jointly while keeping the original product law. For projection endpoints, use `EE^T=M-M^2`; for general symmetric `A`, use `EE^T=U^T A^2 U-M^2` as the total leakage identity and convert it into original-coordinate ridge/cross-bank resources. The clean-bank case is already paid by this run's theorem.

No arbitrary-joint coarea, post-rotation independence, worst conditional density, or unrestricted fiber supremum is permitted. Full QFORM remains open.
