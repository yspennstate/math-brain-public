# account01/B17 final addendum — arbitrary Gaussian locations and iid non-Lindeberg saturation

Run `20260924T074031Z-account01-B17-QFORM-auto11`. This supersedes the mathematical scope of the earlier same-run handoff without deleting it. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED; unrestricted continuity remains separate. Execution `WITHOUT_VERIFIED_BRAIN`.

Canonical strongest mathematics is source-pinned at `yspennstate/math-open-problems@735df7bcc07eec7f35b87f0d70ec6766ca29ea41`, file `proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260924T074031Z-account01-B17-QFORM-auto11/ADDENDUM_GLOBAL_GAUSSIAN_LOCATION.md`. Checker `CHECK_GLOBAL.py` / `CHECK_GLOBAL_OUTPUT.json` records `QFORM_B17_GLOBAL_GAUSSIAN_LOCATION_CHECK_PASS`.

## Stronger theorem

For `G~N(0,sI_3)`, any independent random vector `M` in `R^3`, and any symmetric reflection `B` with spectrum `{1,1,-1}`,

`||p_{(G+M)^T B(G+M)}||_infinity <= 1/(2sqrt(2)s)`.

At `s=1/12` this is exactly `3sqrt(2)`.

Proof after conditioning on `M=m`: rotate only the isotropic Gaussian limit to `J=diag(1,1,-1)`, write `Q=U-V`. Noncentral chi-square Poissonization gives, conditionally on independent Poisson indices `(K,L)`,

`U~Gamma(1+K,2s)`, `V~Gamma(1/2+L,2s)`.

Gamma additivity writes `U-V=Q0+W`, with `Q0=Gamma(1,2s)-Gamma(1/2,2s)` independent of `W`. Therefore each component density is `p_Q0` convolved with a probability law, so its `L^infinity` norm is at most `||p_Q0||_infinity`. The centered base law has global mode at zero and exact height `1/(2sqrt(2)s)`. Mixing over Poisson indices and arbitrary `M` preserves the bound.

This closes the off-axis/two-sheet Gaussian-location gap identified by the latest completed account02/B17 result `math-open-problems@5b85a3d5f95ea478f2534589aaf8729a4e1a29d6`. It does not use the refuted generic two-sheet X-ray shortcut.

## Strongest stress family from this run

Use the exact dense Parseval core

`R0=(1/2)[[1,1,1],[1,-1,1],[1,1,-1],[1,-1,-1]]`,

`B=[[0,0,1],[0,1,0],[1,0,0]]`,

and `A_m=R_m B R_m^T` with `m` copies of `R0/sqrt(m)`. Every physical entry is nonzero and `spec_nonzero(A_m)={1,1,-1}`.

Give **all `4m` physical coordinates iid** cap-one three-interval laws: central length `1-lambda/m`, total satellite mass `lambda/m`, satellite centers `+-a sqrt(m)`. Then the latent limit is `G+M` with `G~N(0,I_3/12)` and arbitrary full-dimensional compound-Poisson location `M=a sum_j S_j r_j`. Pinned Theorem F at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` gives the common physical-frame `|t|^-3/2` envelope, so complete output densities converge uniformly.

Hence

`3sqrt(2)e^(-4lambda)I_0(lambda)^4 <= lim ||p_m||_infinity <=3sqrt(2)`.

For any fixed `D>0`, choose `a=sqrt(D/lambda)`. Then every physical marginal has limiting variance `1/12+D`, the vector Lindeberg defect tends to `3D`, but the lower witness tends to `3sqrt(2)` as `lambda->0`.

Concrete iid example: `lambda=10^-4`, `D=1`, `a=100` gives marginal variance limit `13/12`, vector Lindeberg defect `3`, and

`4.240944012619882 <= lim ||p_m||_infinity <=4.242640687119286`.

Even stronger diagonal sequence: `lambda_m=m^-1/4`, `a_m=m^1/4` makes all physical marginals iid, their variance excess and the vector Lindeberg sum diverge like `m^1/4`, yet `||p_{X^TA_mX}||_infinity ->3sqrt(2)`.

Sharp-proof constraint: near-`3sqrt(2)` concentration does not force bounded moments, Lindeberg, near-minimal variance, connected supports, sparse matrices, or a sign-aligned macroscopic jump structure. The full theorem is still open; remaining witness stress should move beyond Gaussian-plus-independent-location limits, e.g. shared macroscopic rows that alter covariance/shape rather than merely adding a location mixture, or additional active spectrum surviving aggregation.
