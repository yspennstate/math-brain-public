# r46 checks

Current-run arithmetic / algebra checks (supporting only; symbolic proofs are in REPORT.md).

- Exact permutation threshold: `233/256 = 0.91015625 < 1`.
- Four-coordinate Case A constant: `45.345244000098106 < 46`.
- Four-coordinate Case B constant: `92.32198486920356 < 93`.
- Partner/new three-hub subbranch: `3 sqrt(2) 256^(1/3) = 26.939089159424952 < 26.940`.
- 1000 random symmetric block-matrix sanity checks of
  `det M_{jk}=det K[{j,k}]/det H`
  had maximum normalized discrepancy `9.12e-14`.
- 1000 random full-row-rank cases of
  `det(B_j B_j^T)=det(E_J E_J^T)||P_{ker E_J}(K[j,J]/det H)||^2`
  had maximum normalized discrepancy `9.05e-10`; the larger floating error is from explicit projection through occasionally ill-conditioned random two-row Gram matrices.

These numerical checks do not establish the theorems. The proofs use exact Schur-complement, determinant-one row-operation, Gram-factorization, permutation-expansion, and layer-cake identities.
