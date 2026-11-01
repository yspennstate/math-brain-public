# F0012 source-scope README

Model/runtime note for the creating run: **GPT-5.6 Sol; reasoning level UNVERIFIED; not GPT-6 maximum.**

## Exact source scope

This package addresses only Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 9, **Conjecture 9.5 (Gaussian integral spectrum)**:

> for the nonsymmetric iid Rademacher `n x n` matrix `M_n`, the probability that every eigenvalue is a Gaussian integer is `2^{-(1+o(1))n^2}`.

The package does **not** claim to settle the separate symmetric integral-spectrum Conjecture 9.4, normality Conjecture 9.2, fingerprint Conjecture 11.2, or any other source problem.

## Main result in this package

For every even `n`, an explicit fixed-flag family of

`4^{m(m-1)} 6^m = 2^{n^2/2+O(n)}`,  `n=2m`,

distinct sign matrices has spectrum contained in `{-2,0,2}`. Hence

`P(Spec(M_n) subset Z[i]) >= 2^{-n^2/2 + (n/2) log_2(3/2)}`

along every even `n`. This contradicts the exponent `1` in Conjecture 9.5.

The proof is elementary and appears in `main.tex`. `check.py` is an exact local 16-case count certificate; `check.out` is the executed output from the creating run.

## Verification / closure state

Mathematical status: **REFUTED-CANDIDATE** for the literal source statement. The proof has been self-checked and a finite local count certificate executed, but these are not independent audits.

Protocol closure is **NOT YET CERTIFIED**. Required independent checks still missing at creation time:

- independent P26 audit: `0/1`;
- distinct OTHER-track audit: `0/1`.

A bounded literature search dated 2026-09-18/19 found the original Vu statement, later conditional characteristic-polynomial irreducibility work (notably Eberhard 2022), and older integral-graph literature, but no source-matching published refutation of Conjecture 9.5. This negative search is not a novelty certificate. Do not claim publication novelty until a broader prior-art/citation review is completed.

## Reproducibility

Run `python3 check.py`. Expected final line:

`EXACT_LOCAL_COUNT_AND_EXPONENT_PASS`
