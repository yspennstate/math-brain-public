# MOC4 handoff addendum — fleet01/B09 sharp mixed-Schur ceiling

Run: `20260922T074619Z-b09-moc4-r11`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent MOC4: OPEN.

This corrects/sharpens only the numerical constant in the earlier same-run handoff; all scope and status statements remain unchanged.

Consumed named OTHER-account result: fleet02/B07 `MOC4-SPIN4-PAIR-ROOF-RESERVE-IDENTITY-v1`, giving on a complementary pair at a positive-gap maximizer

`Q=T^2-C^2=4(gamma+r_tau)(gamma+r_{tau^c})`, with `r_tau,r_tau^c>=0`.

Applied fleet01/B07 `MOC4-EXACT-SPECTRAL-COVARIANCE-RECONSTRUCTION-v1`: on a generic mixed-Schur row edge `e={alpha,gamma}`,

`E_alpha+E_gamma >= 4 Q h_e`,

where

`h_e=lambda_alpha lambda_gamma/(lambda_alpha+lambda_gamma)` and `lambda_alpha=lambda_min(G_alpha)`, `lambda_gamma=lambda_min(G_gamma)`.

New sharp block-row ceiling: for every `2 x 2` block `B` of `O=Lambda^2 U`, its singular values lie in `[0,1]`; with `R=(s1^2+s2^2)/2`, `D=det B`,

`R^2-D^2=(s1^2-s2^2)^2/4 <= (s1^2+s2^2)/4`.

Orthogonality gives `sum_beta(s1_beta^2+s2_beta^2)=2`, hence

`E_alpha<=1/2` and similarly `E_gamma<=1/2`.

Therefore every generic mixed-Schur positive-gap maximizer satisfies

`boxed(16 h_e (gamma+r_tau)(gamma+r_tau^c) <= 1)`,

and in particular

`boxed(gamma <= 1/(4 sqrt(h_e)) = sqrt((lambda_alpha+lambda_gamma)/(16 lambda_alpha lambda_gamma)))`.

The same statement holds for mixed-Schur column edges with the column covariance metrics. This is a necessary condition, not MOC4 closure. It says a large-gap survivor must approach the exact spectral-covariance/real-cross-ratio degeneracy locus.

Scientific report commit: `e9818a17f7655970420fbc3bd4a4e5059c21aa2d`.  
Sharp addendum commit: `b5bbe1cca9667c311f72d7f0f5086194df51d21a`.  
Paths: `proofnet24/collective-MOC4/fleet01/B09/20260922T074619Z-b09-moc4-r11/REPORT.md` and `ADDENDUM_SHARP_CEILING.md` in `yspennstate/math-open-problems`.
