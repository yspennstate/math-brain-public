# B09 r40 line coverage delta

Pinned source: `paper.tex` blob `98e45d53d106db9a205051a4dd4917fc39dc2e3a`.

| Lines | Clause | Status | Impact |
|---|---|---|---|
| 315 | complex-measure total variation | UNCHECKED | paper proof audited; Lean theorem still absent |
| 315-319 | measurability of x -> ||nu_x||_2^2 | UNCHECKED | nested integration API identified; needs compiled bridge |
| 319 | approximate-identity norm limit | UNCHECKED | probability-Jensen contraction + a.e. bump convergence + Fatou route identified |
| 321-329 | scaled Plancherel and Jensen | UNCHECKED | mathematical step audited; full Lean theorem absent |
| 331 | kappa_epsilon normalization | UNCHECKED | reflected-convolution mass-one route identified |
| 331-335 | Fubini / norm limit / DCT | UNCHECKED | remaining formal task is weighted integrability/Fubini splice |

No fresh Lean compilation is claimed. Rendered PDF remains UNCHECKED.
