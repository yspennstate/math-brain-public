# Verification note

The canonical checker is `check_cell_local_mux.py` at its hardened version and the canonical recorded output is `VERIFICATION.txt`.

The verification paragraph in the initially committed `REPORT.md` was written from the pre-hardened near-zero floating mesh. The hardening excludes `rho<10^-3` from the **floating sanity mesh only** to avoid subtractive cancellation in the numerical evaluation of `K`; the analytic proof covers the entire interval. Canonical observed values are:

- affine formula trials: 20,000;
- maximum affine-formula discrepancy: `5.783568068906675e-15`;
- K-envelope mesh points: 19,980 (`rho` from `0.001` through `0.99995`);
- maximum sampled `K / [rho^2/(1-rho^2)]`: `0.9999991665555377`.

No theorem statement, exact rational reserve, or analytic inequality changed.
