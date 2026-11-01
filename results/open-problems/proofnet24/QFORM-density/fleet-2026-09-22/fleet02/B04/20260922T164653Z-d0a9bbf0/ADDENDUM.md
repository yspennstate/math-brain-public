# fleet02/B04 controlling correction addendum

A later correction landed after the primary B04 report was written:

- fleet02/B17, `QFORM-CONDITIONAL-3D-PROJECTION-CAP-FALSE-v1`, canonical `yspennstate/math-open-problems@f117a4870969d37706b8d7e62cbcae671cc2d3b0`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260922T164534Z-fleet02-B17-QFORM-r11/REPORT.md`.

It gives an exact target example with iid `Uniform[-1/2,1/2]` physical inputs and a `4x4` Hadamard rotation, spectrum `{1,1,-1,0}`, for which the conditional density of the three active spectral coordinates given the complementary coordinate has unbounded essential supremum as the conditioning slice approaches the cube boundary. Therefore the current owner message's proposed **uniform conditional three-dimensional projection cap** is not a valid universal bridge.

This correction does **not** affect `QFORM-SQUARE-ASSISTED-TWO-DIRECTION-WINDOW39-v1` or `QFORM-TWO-STAGE-HEAVY-ROUTING-v1` in the primary B04 report. Those arguments never condition on complementary spectral coordinates and never normalize thin spectral fibers. They preserve original-coordinate independence through a physical square and an MSS-selected physical cross block.

For downstream proof assembly, replace the invalid conditional-cap bridge by either (i) an unnormalized joint-slice curved-trace estimate of the kind identified by B17, or (ii) the product-preserving ridge/grouped-coordinate route used here. The first unpaid B04 implication remains `QFORM-TWO-STAGE-BANK-OPPOSITE-SIGN-AGGREGATION-v1`.

Primary report: `yspennstate/math-open-problems@f5f62136676a5334d5b00a7a25081b8436be9bf4`, blob `769b41027ada57518f3fe6c39b2315ff65cba7f6`.
