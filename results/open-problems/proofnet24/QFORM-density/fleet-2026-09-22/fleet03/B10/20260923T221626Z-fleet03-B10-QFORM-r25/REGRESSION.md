# fleet03/B10 r25 deterministic algebra checks

Run: `20260923T221626Z-fleet03-B10-QFORM-r25`.

These are diagnostic checks only; the proof is symbolic in `REPORT.md`.

Using NumPy with fixed seed `240923`, 2000 trials were generated. In each trial an `n=12` orthonormal coefficient frame `[a,p_1,p_2]` was drawn by QR, `rho` was drawn in `(10^-6,1/64)`, `t=sqrt(rho)a`, `c=1-rho`, and a symmetric invertible `3x3` matrix `M` with eigenvalue magnitudes in `[1,4]` was drawn by orthogonal conjugation. Random leaf and hub values and a random level were then used to check the exact hub-discriminant cancellation

`B^2-4AC = 4c[(m.P)^2-alpha P^T N P+alpha s]`

for

`A=alpha c`, `B=2sqrt(c)(alpha T+m.P)`,
`C=alpha T^2+2T(m.P)+P^T N P-s`,

and to check the exact bank-absorption identity

`sqrt(c) H + T = (sqrt(c) H+T_S)+T_{S^c}`

inside the spectral aggregate.

Maximum absolute discrepancy over 2000 trials:

- discriminant identity: `5.684341886080802e-14`;
- bank-absorption spectral identity: `8.881784197001252e-16`.

No stochastic histogram or numerical density estimate is used as evidence for the theorem.