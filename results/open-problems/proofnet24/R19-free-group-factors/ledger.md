# R19 stable claim ledger

Canonical GitHub-local ledger initialized 16 September 2026 because the assigned R19 target folder did not previously exist on `master`.

| ID | Status | Claim / obligation |
|---|---|---|
| `R19-GH-K001` | KNOWN / VERIFIED | Dykema--Radulescu interpolation; all-or-none reduction; `L(F2)^(1/sqrt2) ~= L(F3)`. |
| `R19-GH-K002` | KNOWN / VERIFIED SCOPE | BDIP 2024 solves only the non-separable analogue; ordinary singular-MASA rank cannot distinguish separable II_1 factors. |
| `R19-GH-K003` | KNOWN / VERIFIED SCOPE | Shlyakhtenko 2026 Fuchsian theorem and free complement of the commutator do not compare distinct free ranks. |
| `R19-GH-C001` | PROVED | Escape-to-infinity normalization lemma for divergent approximate-relation slopes. |
| `R19-GH-C002` | PROVED ALGEBRAIC | A kernel created by scalar extension is the image of a first-Tor boundary. |
| `R19-GH-R001` | CONDITIONAL | Stein vertical completion should be controlled by a Tor defect if a dimension-completion/scalar-extension identification is proved. |
| `R19-GH-C003` | PROVED | Internal `P=W*(v,uvu*) ~= L(F2)` thickens an abelian complement but is not free from `W*(u)`; an explicit centered alternating moment equals 1. |
| `R19-GH-C004` | PROVED / STANDARD | `L(F_n) ~= L(F_infinity) rtimes_{alpha_{n-1}} Z`, where `alpha_{n-1}` is the `(n-1)`-orbit free shift. |
| `R19-GH-X001` | KNOWN ROUTE OBSTRUCTION | Standard free-shift entropy is zero and does not distinguish the multiplicity in `R19-GH-C004`. |

## Current OPEN obligations

- Decide `L(F_2) ?~= L(F_3)`.
- Prove a genuinely W*-intrinsic rank-sensitive invariant, including invariance under arbitrary generator changes and W*-closure.
- Prove or refute the dimension-completion/Tor bridge `R19-GH-R001`.
- Obtain a finite-matrix graph/restriction hard-edge compiler whose ordered singular-mass limit is a certified W*-module invariant.
- Find a quantitative separable replacement for BDIP's non-separable sans-rank.
- Construct an `L(F2)` free complement to Shlyakhtenko's commutator MASA, or prove a genuine obstruction; conjugate thickening is ruled out by `R19-GH-C003`.
