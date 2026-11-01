# Correction to REPORT.md

The construction in REPORT.md is mathematically intended in the standard spectral coordinates of `Lambda=diag(1,1,-1)`. One displayed definition in (2.11) used the already-rotated coefficient matrix `B` a second time. The correct definition is

`A = R Lambda R^T`,

not `A = R B R^T`, when the rows of `R` are the vectors `sqrt(c)e`, `sqrt(a)e`, and `w_k=sqrt(2/m)(cos(theta_k)p+sin(theta_k)q)` written in the original standard spectral basis.

Equivalently, if one first rotates coefficient coordinates to the orthonormal basis `(e,p,q)`, then the row-coordinate matrix is

`R' = R [e p q]`

and the same physical matrix is

`A = R' B R'^T`,

where

`B = [[0,1,0],[1,0,0],[0,0,1]] = [e p q]^T Lambda [e p q]`.

All subsequent formulas in REPORT.md — the spectrum `{1,1,-1}`, the physical entries, `Q=2TC+D^2`, the strict-N3 bounds, the Pluecker calculation, the mixed-hub application, and the Fresnel coefficient — use this corrected interpretation and are unchanged.

This correction preserves the original REPORT.md as an immutable false-start record; consumers should read REPORT.md together with this file.
