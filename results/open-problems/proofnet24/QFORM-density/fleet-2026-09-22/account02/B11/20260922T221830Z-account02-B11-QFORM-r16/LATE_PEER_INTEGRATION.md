# Late peer integration — account01/B11 finite-spike reduction

This addendum is immutable and does not alter the proofs or constants in `REPORT.md`.

After the primary r16 report was committed, fresh main exposed the completed account01/B11 run `20260922T221310Z-account01-B11-QFORM-r11`. I read its canonical proof at

`yspennstate/math-open-problems@59a472456800fb0a6a40579e996f9c9d8eb5ff48`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260922T221310Z-account01-B11-QFORM-r11/REPORT.md`.

That result consumes B11's preceding transverse wedge partition and proves three facts in the heavy-null two-bank chamber:

1. every exact graph-bank endpoint (`delta_B=0`) is already uniformly paid, with bound `<29.448/s`;
2. when `delta_B>0` and all regression residuals obey `e_i^2<=delta_B/4`, the diffuse-deletion theorem pays the bank with exact determinant cancellation;
3. otherwise each bank has at most three static longitudinal spikes, and deleting the spike sets from both banks leaves transverse covariance at least `I_2/16` on each side and cross-wedge mass at least `3/32`.

This is compatible with the current r16 theorem. The r16 hub-Fresnel compiler pays the complete orthogonal one-hub/one-square model even when every fixed pair/ridge certificate degenerates. The account01 result shows that in the more general two-bank geometry, exact graph endpoints and no-spike positive-regression states should no longer be listed as unpaid.

The sharpened first missing interface is therefore:

**`QFORM-FINITE-SPIKE-HUB-WEDGE-ROBUSTNESS-v1`.** In the heavy-null two-bank geometry after the account01 reduction, jointly exploit (i) at most three longitudinal spike coordinates per bank, (ii) the surviving two-bank transverse covariance `>=I_2/16` and wedge mass `>=3/32`, and (iii) the product-preserving hub/Fresnel mechanism of this run, while retaining the actual within-bank dense/self curvature. Prove a dimension-free density bound or force an already completed physical-pair/ridge/volume-sampling certificate. Small regression residuals or dense coefficients may not be discarded perturbatively, and the residual banks may not be replaced by arbitrary joint densities.

Conditioning the finite spike variables is legitimate and produces affine translations, which the r16 hub-Fresnel estimate tolerates. What is not yet proved is that the remaining core has a uniformly nondegenerate combined hub/Fresnel Gram after that conditioning; account01 explicitly warns that the least-squares regression changes when spikes are deleted. That changing-Gram step is the precise new bridge rather than a vague perturbation problem.

Full QFORM remains OPEN / NOT PROVED. No full-solution or continuity claim is added here.
