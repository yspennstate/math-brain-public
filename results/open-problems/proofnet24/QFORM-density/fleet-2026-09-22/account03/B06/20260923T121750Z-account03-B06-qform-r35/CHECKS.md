# r35 finite checks

These computations are sanity checks only; the proof in REPORT.md is symbolic.

Constants in the live collar c>63/64:

- exact-null translated-square bound: `2^(11/4)*(64/63)^(1/4) = 6.753709002199243`;
- same-sign nonzero translated-square bound: `2^(15/4)*(64/63)^(1/4) = 13.507418004398486`;
- opposite-sign two-sheet bound: `2^(13/4)*(64/63)^(1/4) = 9.551186867231433`;
- Claude ruled one-sheet constant: `pi*sqrt(2) = 4.442882938158366`;
- account04/B18 follow-on constants: `2*sqrt(13.508)=7.3506462300943305`, `2*sqrt(9.552)=6.181262007066194`.

For `rho=1/sqrt(2)`,

`epsilon(rho)=(rho^2+rho*sqrt(rho^2+4))/2 = 1`,

so `rho<1/sqrt(2)` is exactly the positive spectral-margin range of the Weyl repair.

A 1000-sample random numerical check over coupling vectors with `rho<1/sqrt(2)` compared the eigenvalues of

`Delta=[[theta^2,theta*zeta,theta],[theta*zeta,zeta^2,zeta],[theta,zeta,0]]`

against the exact formula

`{0,(rho^2-rho*sqrt(rho^2+4))/2,(rho^2+rho*sqrt(rho^2+4))/2}`.

Maximum absolute eigenvalue discrepancy: `7.771561172376096e-16`.

The same samples checked both the positive-pivot base `spec={-1,1,1+delta}` and the opposite-sign base `spec={-(1+eta),1,1}`. The observed ratio

`min_j |lambda_j(B0+Delta)| / (1-epsilon(rho))`

was always at least `1.0009797224645218`; the proof only uses Weyl's exact lower bound `>=1`.
