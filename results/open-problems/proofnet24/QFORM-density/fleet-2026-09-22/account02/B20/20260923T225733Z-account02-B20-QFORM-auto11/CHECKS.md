# Deterministic checks — account02/B20 `20260923T225733Z-account02-B20-QFORM-auto11`

All checks below are deterministic arithmetic / linear algebra regressions for `REPORT.md`; they are not probabilistic evidence for the conjecture.

## Constants

- `S0 = 1/(480*sqrt(7626)) = 2.3856699607287348e-5`.
- `C2(3/4) = 16*exp(1/4)*(3/2)^(-1/4) = 18.563967027280146`.
- `C2(3/4)*S0^(-1/4) = 265.6245415480431 < 265.625`.
- `(3+122*sqrt(10))*2^(-20) = 0.0003707865472226546`.
- Adding the cross-collar error gives `0.0003707865472226546+1/64 = 0.015995786547222654`.
- Weyl remainder: `1-0.015995786547222654 = 0.9840042134527773`.
- Partner triple gate: `102*(2^(-60))^(-1/3) = 106954752` (up to floating representation in a numerical evaluation).
- Pinned D5 gate at `Z5=1/1024`: `5*sqrt(2e)*(1/1024)^(-1/10) = 10*sqrt(2e) = 23.316439815971243`.
- Physical coloop incident-volume floor: `(3/4)*S0^2 = 4.2685658711425824e-10`.

## Rank-two leverage identities

For a fixed `2 x m` full-row-rank matrix `M`, let `G=MM^T`, column `m_j`, and `ell_j=m_j^T G^(-1)m_j`. The report uses

`sum_(k!=j) det([m_j,m_k])^2 = ell_j det G`,

and

`det(G-m_jm_j^T)=det G (1-ell_j)`.

A fixed-seed `2 x 9` numerical regression produced

- `det G = 87.61332403069989`,
- maximum absolute error in the incident-minor identity `2.13e-14`,
- maximum absolute error in the determinant-lemma identity `5.68e-14`.

These identities also follow exactly from Cauchy--Binet and the matrix determinant lemma, respectively; the numerical check only guards transcription/arithmetic.
