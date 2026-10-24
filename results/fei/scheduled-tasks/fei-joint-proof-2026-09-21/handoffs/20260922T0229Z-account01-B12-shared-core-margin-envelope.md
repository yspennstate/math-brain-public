# FEI handoff — account01/B12 adaptive shared-core margin envelope

Source scientific report: `proofnet24/P03-fei/fleet-2026-09-21/account01/B12/20260922T0227Z-shared-core-margin-envelope/REPORT.md`, commit `e94cb507a4f4876fad5bb703dee1ec569c177314`, blob `1906afba53355f2d05b892b6dc54caec4e574b1f`.

Consumed exact peers: account03/B15 `20260922T002607Z-readonce-gamma-counterexample` (balanced-uniform identity `c_G=4(H/(I-1)-C0)`), and account04/B15 `20260922T020955Z-adaptive-depth-shared-core-ceiling` (history-dependent integer-depth shared-core ceiling).

Applied result for the old read-once centre `C0=6.4548`: every finite gate in the full adaptive-depth nine-host shared-core family has

`c_G < 0.26820485205151089460601760095672786588585655524`,

while the explicit finite source-valid `F7` has

`c_F7 > 0.2682037982017927393606421554420460054013187196154347074312`.

Thus the entire depth-only family has less than `1.0538497181552454e-6` remaining margin room. `F7` already requires more than `60.9911703004` times the present AND correction `0.0043974201`.

Implication: the read-once all-gate candidate remains refuted; changing only self-composition depths in this fixed shared host/core geometry is analytically exhausted. Any stronger falsifier from this line must change host/core geometry, the prime gadget, or move to a genuinely biased point. Full FEI remains OPEN / NOT PROVED.
