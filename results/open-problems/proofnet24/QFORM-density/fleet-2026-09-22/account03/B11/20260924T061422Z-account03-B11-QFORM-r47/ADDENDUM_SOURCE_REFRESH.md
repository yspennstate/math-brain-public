# Source-order correction and r49 integration

After the main `REPORT.md` was committed and read back, the worker-owned `LATEST.json` was read as required by `MEMORY_PROTOCOL.md`. It showed that the true latest completed account03/B11 predecessor before this 06:14Z run was

- `20260924T041407Z-account03-B11-QFORM-r49`,
- canonical mathematics `yspennstate/math-open-problems@506a01e6b5026fd7f703ad5b7f2e6ad08b9277c3`,
- path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260924T041407Z-account03-B11-QFORM-r49/REPORT.md`.

The main report incorrectly called r48 the latest predecessor. This addendum corrects only that source-order statement; none of the mathematics in the new two-Jacobian theorem depends on the mistaken ordering.

## What r49 proved

R49 proved `QFORM-R48-CANCELLATION-XRAY-IMPOSSIBILITY-v1`: the nonlinear same-bank cancellation law used in r48 has infinite all-direction X-ray norm, whereas every genuine orthogonal three-dimensional projection of a cap-one product source has all two-dimensional orthogonal projection densities uniformly bounded. Hence the r48 nonlinear cancellation law is rigorously impossible as the true residual product projection. R49 also correctly retained the live correction that a generic X-ray cap alone does **not** imply the two-sheet QFORM bound.

## Relation to the present run

The present theorem is a distinct next step and is compatible with r49. In the exact r45 puncture normal form it proves the pointwise original-coordinate identity

`(J_2(W,Q))^2 = 4[kappa^2 W^2+c^2(V')^2]`

and, using the genuine two-dimensional product-projection density cap plus `kappa^2|c|=|det M|`, proves

`E[J_2(W,Q)^(-1)] <= sqrt(2*pi)/s`

and more generally the full family of negative moments below exponent two, uniformly through the puncture `q -> 1`.

Thus r49 and this run fit together as follows:

1. r49 rules out the exact nonlinear cancellation model by a global product-projection invariant;
2. this run identifies the puncture-specific coarea invariant that remains uniformly nondegenerate after **aggregate original-coordinate minors are summed before inversion**;
3. the still-missing theorem must combine those two facts with the original product factorization rather than using either X-ray control or the reciprocal-Jacobian expectation in isolation.

A more precise successor name is therefore

`QFORM-PUNCTURE-XRAY-TWOJACOBIAN-PRODUCT-COMPILER-v1`:

> on the minority-sign/two-sheet side of the exact r45 null-pivot normal form, combine (i) the r49 all-direction product-projection X-ray certificate, (ii) the exact full two-Jacobian identity from this run, and (iii) the original independent-coordinate factorization, to prove a universal linear interval bound. Do not infer the conclusion from X-ray control alone and do not replace the product law by an arbitrary capped joint density.

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. No continuity conclusion is added by this addendum.
