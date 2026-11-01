# B08 r37 deterministic sanity checks

These checks are diagnostics only; the proof is algebraic.

Python/NumPy, deterministic seed `260923`, used the first three columns of the normalized Sylvester Hadamard matrix of order 512, followed by a random orthogonal 3-by-3 column rotation.  This gives an exactly orthonormal physical three-frame with row leverage `3/512 < 1/48`.  For each of 1000 trials I chose a random physical half-cut until both restricted Gram matrices lay between `I/4` and `3I/4`, then chose random nonsingular signed diagonal `D`, `tau>0`, and an aligned coefficient `beta` varying over several orders of magnitude.

For

`C=U D U^T`, `b=tau*w+U*beta`, `M=[C[S,T],b_S]`,

the check compared the numerical product of the three singular values of `M` against the exact formula

`tau*|det D|*sqrt(det(W_S^T W_S)*det(U_T^T U_T))`.

Observed:

- accepted balanced cuts: `1000`
- identity violations: `0`
- maximum relative identity error: `1.45329225428863e-11`
- minimum observed ratio
  `(s1(M)s2(M)s3(M))/(tau|det D|/32)`: `5.062494978699489`

The theorem constant was separately evaluated as

`6*(1536/(47*sqrt(47)))^(1/3) = 10.097938622915146`.

The numerical check is not used as evidence for the universal theorem; it only guards the determinant bookkeeping and constants in the exact rank-two-child endpoint proved in `REPORT.md`.
