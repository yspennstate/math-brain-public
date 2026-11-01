# P0282 idea before production validation — attack the apparent all-order curvature pattern, then certify a block

Date: 2026-09-19 UTC
Worker: NM13-07
Source / claim: P0282 / Chen fixed-size LIS log-concavity
Frozen metric entering: `N_exact = 99`

The preceding run proved a finite-degree lemma for the Taylor coefficients

`G_j(t)=log A_j(t)=sum_{m>=1} D_m(j)t^m`,

namely `deg_j D_m <= m`, and then used the favorable ninth coefficient to reach the `10/11` growing-defect window. The next run should not blindly derive only `D_10`.

This invocation first attacks the stronger pattern in the opposite direction.

- **#23 DO WHAT THE PROPOSER DID NOT EXPECT (RECYCLED):** assume the observed positive Chen curvature of the Taylor coefficients eventually fails. Search exact small `(m,j)` for the first adverse curvature
  `C_m(j)=2D_m(j)-D_m(j-1)-D_m(j+1)`.
- **#26 HUNT THE SPORADIC CASE (RECYCLED):** if a sign failure exists, determine whether it is confined to defects already covered by the retained all-`n` theorem `j<=66`, or whether it reaches the genuinely open active sector `j>=67`.
- **#3 PROVE SOMETHING STRONGER (RECYCLED):** if the active sector survives, certify a whole block of Taylor orders simultaneously, not just one next coefficient. The finite-degree lemma makes this finite: recover each `D_m` from exact values, form `C_m`, shift `j=67+x`, and check coefficientwise positivity in `x`.

The intended theorem shape is therefore conditional on the exact sign experiment: for the largest block `2<=m<=M` certified positive for every `j>=67`, truncate the analytic series only after order `M` and use the retained Cauchy disk to obtain one source-valid growing-defect window. A sign failure at small `j` is to be reported as an obstruction, not hidden by the stronger theorem.

Only after this structural experiment produces a worthwhile result will production checking be built. The frozen finite metric will then be advanced independently, if possible, by an exact row-100 Gessel/Toeplitz certificate; that census is secondary to the structural route.