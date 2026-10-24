# Deterministic/numerical sanity checks for sparse-kernel deletion

The proof in `REPORT.md` is algebraic. These checks are only diagnostics.

A fixed-seed test generated 3,000 random examples with ambient dimensions 5, 7, 9; kernel support size 3; and kernel dimensions 1 or 2. For each example an orthonormal supported kernel basis `W` was generated, the best Cauchy--Binet coordinate set `L` was selected, a random symmetric complement matrix `C` was sampled, and `A=P^T C P` was formed.

Observed:
- maximum `||A W||_F`: `5.95e-16`;
- maximum `||P||^2 / binom(3,d)`: `0.94849`;
- minimum tested margin in `s_3(C) - s_3(A)/binom(3,d)`: `3.80e-4`.

Sharpness matrix

`A_*=[[2/3,-1/3,-1/3,0],[-1/3,2/3,-1/3,0],[-1/3,-1/3,2/3,0],[0,0,0,1]]`

has numerical spectrum `{0,1,1,1}` (zero observed as `2.78e-17`). Deleting any one of its first three coordinates leaves spectrum `{1/3,1,1}`, so the factor-three spectral loss in the theorem cannot be improved in general by merely choosing a coordinate from the support of the null vector.
