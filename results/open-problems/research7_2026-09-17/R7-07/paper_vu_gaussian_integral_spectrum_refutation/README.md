Model actually running for the creating run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# Source-scope README — refutation of Vu Conjecture 9.5

This folder is the self-contained paper package for the narrow source-level result produced by R7-07.

## Exact source

Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797v1 (submitted 6 May 2020), published in *Probability Surveys* 18 (2021), 179–200, Section 9, Conjecture 9.5 (“Gaussian integral spectrum”). The source model `M_n` is the nonsymmetric `n x n` matrix with independent Rademacher entries. The conjecture states

`P(Spec(M_n) subset Z[i]) = 2^{-(1+o(1)) n^2}`.

Current arXiv URL: https://arxiv.org/abs/2005.02797 .

## Paper theorem

For every `n>=1`,

`P(Spec(M_n) subset Z[i]) >= 3^{floor(n/2)} 2^{-floor(n^2/2)}`.

Hence

`limsup_n (-log_2 P(E_n))/n^2 <= 1/2`,

which contradicts the source exponent `1` and therefore refutes Conjecture 9.5.

The proof is an explicit signed block-shear construction, with separate exact counts in even and odd dimensions. No asymptotic heuristic or numerical extrapolation is used.

## What the package does NOT claim

- It does **not** prove that `1/2` is the sharp corrected exponent. R7-07's frozen corrected-exponent metric remains `0 <= u_GI <= 1/2`.
- It does **not** claim worldwide novelty. Bounded searches through 2026-09-19 did not surface a matching published refutation, but search misses are not novelty proof.
- It does **not** claim closure under the owner protocol yet. Required independent audits are still absent: P26 `0/1`, distinct OTHER-track `0/1`.
- Existing exact scripts/checks under `research7_2026-09-17/R7-07/artifacts/` are self-checks, not independent audits.

## Core proof provenance

The all-dimension theorem is preserved in

`research7_2026-09-17/R7-07/artifacts/2026-09-19/2026-09-19T000830Z__F0012_signed_shear_all_n_extension.md`.

The first even-dimensional construction is in

`research7_2026-09-17/R7-07/artifacts/2026-09-18/2026-09-18T232000Z__F0012_block_shear_refutation.md`.

Exact small-case checking is archived in the neighboring F0012 checker/output files, including output ending `SIGNED_SHEAR_ALL_SMALL_CASES_PASS`.

The terminal corrected-exponent reductions are preserved separately and are not needed for the source refutation theorem.

## Package contents

- `README.md` — this source/scope declaration.
- `main.tex` — self-contained manuscript proving the all-`n` lower bound and source refutation.

Status of the narrow paper theorem: **AUTHOR-SIDE COMPLETE / SOURCE MATHEMATICALLY REFUTED / INDEPENDENT AUDITS REQUIRED / NOVELTY UNVERIFIED**.