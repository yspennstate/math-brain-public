# Notation clarification for REPORT.md

In Theorem 4.1 and its proof, `B0=U Sigma V^T` is taken in singular-value form: after the deterministic choice of left/right singular frames `U,V`, `Sigma=diag(s1,s2)` with `s1>=s2>=beta L>0`. Thus every occurrence of `Sigma^2` in equations (4.20), (4.21), (4.36) means the positive matrix `Sigma Sigma^T=diag(s1^2,s2^2)`.

Equivalently, without choosing diagonal singular coordinates, replace each `Sigma^2` there by `Sigma Sigma^T`; the proof uses only `Sigma Sigma^T >= beta^2 L^2 I_2`. No random input is rotated, and no statement or constant in REPORT.md changes.
