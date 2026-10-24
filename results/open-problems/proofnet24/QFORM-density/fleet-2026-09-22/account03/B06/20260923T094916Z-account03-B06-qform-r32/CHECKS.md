# account03/B06 r32 finite checks

These are sanity checks only; the proofs are symbolic in `REPORT.md`.

1. Symbolic determinant of the transverse coefficient matrix

`S=[[2ka,kb,k],[kb,beta,0],[k,0,0]]`

was simplified exactly to

`det(S)=-beta*k^2`.

2. For 1000 random tests in ambient dimension 7, with random linearly independent `u,v`, random nonzero `w` orthogonal to `span{u,v}`, random nonzero `k,beta`, and random in-plane coefficients `a,b`, the signed product of the three nonzero eigenvalues of

`B_h=C S C^T`, `C=[u v w]`,

was compared with

`-beta*k^2*det(Gram(u,v))*||w||^2`.

Maximum relative discrepancy (denominator `max(1,|target|)`) was

`2.891011114798241e-14`.

3. Front constants:

`3*4^(2/3)=7.559526299369239...`

`2*sqrt(3)*4^(1/3)=5.49891854799441...`

4. The layer-cake constant is exact: if `A>0`,

`integral_0^infinity min(1,A*s^(-3/2)) ds = 3*A^(2/3)`.

No Monte Carlo histogram or numerical density estimate is used as proof.
