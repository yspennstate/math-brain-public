# account03/B08 handoff — optimized full-range diffuse branch

Run: `20260922T142426Z-account03-B08-qform-diffuse-v3`  
Programme: `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
Canonical proof: `yspennstate/math-open-problems@f6bc73f719d1e9dbcaeb06df49913bb84dd274b6:proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T142426Z-account03-B08-qform-diffuse-v3/REPORT.md`  
Status: supporting theorem; full conjecture OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.

## New theorem
If `U` spans the entire range of `A=U Lambda U^T`, at least three eigenvalues satisfy `|lambda|>=1`, and

`max_i ||u_i||^2 <= epsilon < epsilon_*=(39-6sqrt(30))/98≈0.0626188423`,

put `delta=1/2-epsilon-sqrt(2epsilon)`. For every

`max(1,2epsilon/delta) <= q <3/2`,

all admissible independent coordinate laws satisfy

`||p_{X^TAX}||_infinity <= 3e/[sqrt(2q) delta (3-2q)]`,

and the density is continuous and vanishes at infinity. Extra nonzero eigenvalues may be arbitrarily small or large and of either sign.

Explicitly, full-range leverage `<=1/16` is covered by `q=149/100`, with a universal constant `<2814`.

## Mechanism
MSS partitions the original coordinate frame into two pieces with Gram lower bound `delta I`. The actual full cross block then has three singular values at least `delta`, and its range leverage is at most `epsilon/delta`. Apply the completed regularized determinant/cross-block theorem at fractional exponent `q`; the condition `3>2q` is exactly what yields the threshold `epsilon_*`.

Completed source theorem applied: `math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

The designated partner `account04/B08` has no completed current-QFORM handoff in the fresh shared directory, so no theorem is falsely attributed to that worker.

## Remaining debt
Full-range delocalization is stronger than delocalization of only the three large eigenvectors. The next missing implication is to handle a highly localized arbitrary spectral remainder without losing original-coordinate product structure: either produce a controlled actual cross block or pair the selected diffuse subspace with localized-coordinate smoothing.
