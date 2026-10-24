# The first unresolved n=8 layer of uniform split reliability

This folder is the source-matching closure package for the finite claim `ROMERO-2025-SPLIT8`.

## What the outside source asks

Pablo Romero, *Characterization of locally most split reliable graphs*, Theoretical Computer Science 1047 (2025), 115327, DOI 10.1016/j.tcs.2025.115327, studies uniformly most split reliable two-terminal graphs in `T_{n,m}`. Romero proves nonexistence for `n>=7` and `n <= m <= binom(n-3,2)+3`, while the previously known results settle the trivial complete/near-complete classes and all classes through `n<=7`. Thus the first complete unresolved vertex layer is

`n=8,  m=14,15,...,26`.

The unrestricted all-`n` Brown--McMullin/Romero problem remains open beyond the finite layer proved here.

## What this package proves

For `n=8`:

- for `14 <= m <= 19`, no uniformly most split reliable graph exists in `T_{8,m}`;
- for `20 <= m <= 26`, Romero's balloon graph equipped with a diameter terminal pair is uniformly most split reliable in `T_{8,m}`.

Hence every class in the first unresolved `n=8` layer is decided exactly. This is a source-valid finite theorem but only PARTIAL for the unrestricted all-`n` source problem.

## Proof/certificate files

- `main.tex`: self-contained proof of the finite-layer theorem.
- `check_sparse.py`: exact integer certificate for the six nonexistence cases `m=14,...,19` using all-minors Matrix--Tree determinants.
- `check_sparse.out`: archived exact output.
- `check_dense.c`: exact exhaustive terminal-fixed orbit and split-coefficient checker for `m=20,...,26`.
- `check_dense.out`: archived exact output.

The checker sources are copied verbatim from the already-audited R06 artifacts, rather than rewritten at closure:

- `artifacts/R06/20260919T0520Z_romero_split8_n6_checker.py`;
- `artifacts/R06/20260919T0631Z_romero_split8_full_layer_checker.c`.

Suggested execution:

```text
python3 check_sparse.py
gcc -O3 -std=c11 -Wall -Wextra check_dense.c -o check_dense
./check_dense
```

## Independent audits

The package has two genuinely distinct OTHER-track full mathematical audits:

1. `P26-AUDIT-R06-ROMERO-SPLIT8-N8-FULL-LAYER-64 = PASS_FULL_MATHEMATICAL_PROOF`, in `proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_10-01-31__run-report.md`.
2. `R01-AUDIT-R06-ROMERO-SPLIT8-N8-01 = PASS_FULL_MATHEMATICAL_PROOF`, in `runs/R01/20260919T2000Z_romero_split8_second_audit_20_27_30_5c8e2a71.md`. R01 used independently written exact code and re-derived the sparse determinants, dense terminal-fixed orbit completeness, coefficient recurrence, and quantifier step.

Thus the finite `n=8` package is internally `PROVED / AUDIT-COMPLETE / PACKAGED` under the repository protocol. This is not a claim of journal peer review or of resolution of the unrestricted source problem.

## Prior-art scope

A dated 2026-09-19 check of Romero's current arXiv record (`arXiv:2503.15453`), exact-title/author searches, and later split-reliability searches did not locate a later primary source settling this complete `n=8` layer. This is bounded negative evidence, not a worldwide novelty or priority certificate. Before external submission, perform an ordinary author-level bibliography/citation review again.
