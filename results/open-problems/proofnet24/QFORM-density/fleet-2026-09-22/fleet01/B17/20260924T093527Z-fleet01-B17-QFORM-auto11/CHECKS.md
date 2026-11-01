# Checks — fleet01/B17 two-macro witness

The symbolic calculations used in `REPORT.md` were rerun in the current execution environment with SymPy using the same identities committed in `CHECK.py`.

Result:

`PASS_QFORM_B17_TWO_MACRO_MINORITY_WITNESS`

Verified exactly:

- `B^2=I` for `B=I-2nn^T`, `n=(1,2,4)/sqrt(21)`.
- `V^T V=I` for the tetrahedral `4 x 3` frame.
- all four overlaps `Vn` are nonzero.
- compensated diffuse block is exactly the rational matrix displayed in (2.2), with no zero entry.
- `S^2=I-P/2` and `(P/2)+S^2=I`, hence the compensated synthesis is Parseval.
- uncompensated diffuse block is exactly the rational matrix displayed in (3.2), with no zero entry.
- the uncompensated active eigenvalues are exactly `{1,1,-3/2}`.
- the degree-nine Taylor lower certificate equals the displayed positive Bernstein polynomial on `0<=a<=3`.
- small-`q` expansion: `1-3 q^2/160-q^3/224+3 q^4/10240+O(q^5)` for the two-row compensated peak ratio.
- general `k` fragmentation expansion: `1-3 q^2/(80 k)+O(q^3)`.
- exact `q=1/2` compensated limit:
  `C2 = 4.220606561842082557450058370217359849235...`.
- gap:
  `3 sqrt(2)-C2 = 0.022034125277202588955007802411734386474...`.
- partner-average factor:
  `E exp[-3(U1+U2)^2/2] = 0.8087886651129561639478631204165...`.
- fleet02/B17 quantitative partner bound after averaging:
  `3.986610240755808324043573782483862164174...`.

External proof dependencies checked at source:

1. Fresnel--Brascamp--Lieb Theorem F: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`. Its actual hypotheses were checked on both finite physical eigenframes; no arbitrary-joint or post-rotation-independence shortcut is used.
2. Partner fleet02/B17 random-location Gaussian barrier and quantitative noncentral estimate: `yspennstate/math-open-problems@97d91254e56ad2f8c79b121a0ce8bf66472a11d9:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260924T074629Z-fleet02-B17-QFORM-auto11/REPORT.md`.

Full unrestricted QFORM remains open. Continuity remains separate.
