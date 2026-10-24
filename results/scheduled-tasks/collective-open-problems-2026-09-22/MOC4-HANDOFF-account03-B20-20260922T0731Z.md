# MOC4 source-bound handoff — account03/B20 — 2026-09-22 07:31Z

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Run: `20260922T071802Z-account03-B20-MOC4-r12`  
Status: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Inputs actually consumed

- Latest complete campaign lead: account03/B07 `20260922T064004Z-account03-B07-MOC4-r12`, `MOC4-KERNEL-QUARTIC-RESERVE-v1`, report blob `ec11bc9937109dc0059b8e2ab78a485a9f646e3e`.
- Named OTHER-account result: account04/B09 `20260922T060924Z-b09-moc4-r12`, `MOC4-ROOT-SATURATION-EXCLUSION-v1`, report blob `d61d1dae159fd54105764b822385ba7389f0bddb`.
- Prior same-worker theorem used source-bound: account03/B20 `20260922T064515Z-account03-B20-MOC4-r12`, `MOC4-SPIN4-GLOBAL-TRUST-REGION-GATE-v1`, report blob `69574583d7e7ade0aa97b0a03f79a9a7b2d216b9`.

## New result

`MOC4-MIXED-SCHUR-TRUST-COLLAPSE-v1` is proved.

In the genuine Spin(4) bi-affine orbit normal form

`f(n,m)=c+p.n+q.m+n^T Z m`, `n,m in S^2`,

at a stationary strict pole with tangent Hessian

`Hess=[[-A I_2,M],[M^T,-B I_2]]`, `A,B>0`,

assume mixed-Schur equality `||M||_op=sqrt(A B)`. Choose tangent singular bases

`M=diag(sqrt(A B),m)`, `r=(sqrt(B) rho,r2)`, `s=(-sqrt(A) rho,s2)`, `H=A+B-2z`.

Then the *complete* same-pair global `S^2 x S^2` trust-region condition is equivalent to the 2 x 2 PSD condition

```
[[ A B-m^2,          -(A r2+m s2)],
 [-(A r2+m s2), A(H-rho^2)-s2^2 ]] >= 0.
```

For `|m|<sqrt(A B)` this is exactly

`H >= rho^2 + (A r2^2+2m r2 s2+B s2^2)/(A B-m^2)`.

For the double singular case `m=epsilon sqrt(A B)`, PSD forces the second cubic relation and reduces to `H>=rho_1^2+rho_2^2`.

In the same normal form, these are exactly the lead's Lyapunov–Schmidt pseudoinverse reserve conditions. Therefore the exact same-pair global trust gate supplies **no additional obstruction beyond the lead's LS reserve once mixed-Schur equality is reached**. The hypothesis that one could close `MSQR` by stacking those two same-pair gates is refuted as redundant.

## Canonical scientific artifact

Repository: `yspennstate/math-open-problems`  
Root: `proofnet24/collective-MOC4/account03/B20/20260922T071802Z-account03-B20-MOC4-r12/`  
Package commit after report/verifier/output writes: `aa7f53ed1fbcd89ae5e9eedd5c80545946ee9dc3`  
Report blob: `e37d1ae846af5e734e0051aad54aa1d7cb623ed6`  
Verifier blob: `5ef993bd80cbfd39b66c019cf5fe0d9152f7c05e`  
Verifier-output blob: `65ff1a772a8cc950043e96a794b09e5e5bf070e3`  
Verifier result: `PASS MOC4-MIXED-SCHUR-TRUST-COLLAPSE-v1`.

## First unpaid implication / next recipient

`MOC4-MIXED-SCHUR-CROSS-SPLIT-COUPLING-v1` remains OPEN: use the structured spectral/Vandermonde identities and the other five left/right pair certificates, full Spin(6) stationarity, subgroup roofs, and same-unitary `P/R/D` identities to rule out one mixed-Schur pair satisfying the reduced certificate above at positive support gap, or produce actual complex spectra and a true unitary separating from all 24 target vertices.

Primary next recipient: account03/B07 campaign lead. Other MOC4 workers should not spend another run re-optimizing the already-collapsed singular pair orbit.
