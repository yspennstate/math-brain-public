# R19 — Separable free-group-factor isomorphism

## Exact target

Decide whether the separable group von Neumann II_1 factors

\[
L(\mathbb F_m),\qquad L(\mathbb F_n)
\]

are isomorphic for distinct `2 <= m,n <= infinity`, first `L(F_2)` versus `L(F_3)`.

This is the classical W*-algebra problem rooted in Murray--von Neumann (1943) and explicitly listed by Kadison (1967). Reduced group C*-algebras are a different target. The Boutonnet--Drimbe--Ioana--Popa 2024 theorem solves a non-separable analogue, not this separable problem.

## Exact reduction

Dykema/Radulescu interpolation gives

\[
L(\mathbb F_r)^t\cong L\!\left(\mathbb F_{1+(r-1)/t^2}\right).
\]

In particular

\[
L(\mathbb F_2)^{1/\sqrt2}\cong L(\mathbb F_3).
\]

Any claimed full closure must respect the precise amplification normalization and justify the all-or-none implication.

## Current research program

1. **Invariant route:** construct a genuinely W*-intrinsic microstate / singular-spectrum / derivation-module invariant before computing rank-dependent values. Canonical-generator entropy or hard-edge exponents alone are not sufficient.
2. **Completion/homology route:** understand the passage from algebraic Stein derivations over `A^e` to the closed coarse Hilbert module; quantify any Tor/dimension-flatness defect.
3. **Separable BDIP route:** replace the non-separable singular-core cardinal with analytic/intertwining/coarse-bimodule data. Bare singular-MASA cardinality is universal in the separable II_1 category.
4. **Constructive route:** exploit new free-complementation results (notably Shlyakhtenko 2026) and exact crossed-product/free-shift models, while recording explicit mixed-moment obstructions.

## Archive

Immutable run reports are under `runs/YYYY-MM-DD/`; run-specific scripts and certificates are under `artifacts/`. See `ledger.md` for stable GitHub-local claim IDs.
