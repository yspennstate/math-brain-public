# Rank compression and absorption pull against each other — and one condition governs both

Author: main session c53c1d50, 2026-08-19 ~05:4x. Elementary, and it follows from two things the campaign already has: the rank lane's `λ = dim B̄(ker P)` (R2) and its Target R-C. Status: the observation and the inequality are proved; the consequence for strategy is labelled as such.

## 1. The tension

**Target R-C** (horn 1's requirement, `attack_rank.md` §4): exhibit selectors whose residual private parts span `O(L)` dimensions inside a core of support `≍ log n·log log n`. Writing `d := dim span{p_a}` for the private-part span and `k` for the number of rows needing residuals, R-C asks for `d = O(L)` with `k ≫ L` — i.e. **massive dependency among the private parts.**

**R2** (proved, elementary): the leak is `λ = dim B̄(ker P)`, the boundary image of exactly those dependencies.

Rank–nullity gives `dim ker P = k − d`. So:

> **Compressing the private rank to `d` forces `k − d` independent dependencies, and absorption requires the boundary map `B̄` to annihilate every one of them.**
> `λ = dim B̄(ker P)`, with `dim ker P = k − d`. **The better the rank compression, the larger the space that absorption must kill.**

The two clauses of the rooted target are therefore not independent difficulties to be attacked separately: **clause (i) is satisfied by creating dependencies, and clause (ii) is the demand that those same dependencies be invisible on the boundary.**

## 2. One condition governs both

Both clauses are simultaneously satisfiable exactly when the residual system's boundary parts are **constant on private-sharing clusters** — the corrected leak mechanism (`lambda_first_multiblock.md`), now visible as the *joint* condition rather than a fact about absorption alone:

- share private parts (needed for clause (i)'s rank compression),
- and share boundary parts too (needed for clause (ii)'s absorption).

Checks against everything the campaign has measured:

| object | `k` | `d` | `dim ker P` | boundary parts on the shared private | `λ` |
|---|---|---|---|---|---|
| NAE path child | 2 | 1 | 1 | identical (`a`) | **0** |
| NAE star (my basis) | 3 | 1 | 2 | distinct (`z₁,z₂,z₃`) | 2 |
| NAE star (exhaustive optimum) | 3 | 1 | 2 | — | **1** |
| embedded crosspolytope r=4 | — | — | — | — | **0** |

The path child achieves maximal compression (`d = 1` from `k = 2`) *and* zero leak, because its two residuals are literally equal. The star achieves the same compression and cannot avoid a leak, because its boundary partners differ. **Same compression, opposite absorption outcome, decided entirely by whether the boundary parts agree.**

## 3. What this changes about strategy

- **It explains why no lane advanced clause (ii).** The iteration-1 referee's sharpest cross-lane finding was that neither delivered lane touched absorption. Both were working on rank compression — which, by §1, *manufactures* the dependencies absorption has to kill. Progress on clause (i) by that route strictly increases the burden on clause (ii).
- **It predicts where a proof must come from:** not from compressing harder, but from compressing *along structure that keeps boundary parts constant*. That is a statement about which rows may be clustered, not about how much they may be clustered — and it is checkable on any explicit block.
- **It gives the campaign's two-regime picture a common cause.** Horn 2 (singleton private supports) has little compression available and its difficulty is boundary multiplicity; horn 1 (multi-coordinate supports) demands heavy compression and inherits the corresponding leak burden. Both are the same trade-off at different points on the curve.

## 4. Honest limits

- `λ = dim B̄(ker P)` is the rank lane's R2, **still unrefereed**, though I have re-derived it and it is a two-line consequence of the definitions.
- §1 is an *obstruction to a naive strategy*, not to the target: nothing here says a simultaneous solution is impossible, only that the two clauses cannot be optimised independently, and that improving one by the obvious route worsens the other.
- The table's objects are all known class **non-members**, the campaign's standing limitation.
- Nothing here bears on the conjecture, which is OPEN, or on the block-internal certificate, which remains the open content of horn 1.
