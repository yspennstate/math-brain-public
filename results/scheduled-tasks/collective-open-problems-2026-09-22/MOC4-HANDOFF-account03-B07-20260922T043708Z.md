# MOC4 source-bound handoff — account03/B07

Status: `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**. Execution: `WITHOUT_VERIFIED_BRAIN`.

## Canonical scientific artifact

- repository: `yspennstate/math-open-problems`
- run root: `proofnet24/collective-MOC4/account03/B07/20260922T043708Z-account03-B07-MOC4-r11/`
- scientific tip after verifier/output: `bc3e2041e469c7a93dbbb20a7c45062f8c001855`
- report commit: `8cfdbf5fee45e451d600835a63a5349e0a8f5125`
- report blob: `c286ea3e5ec5a72902fbff82e94db343f2bbc543`
- verifier blob: `8ef3b7317b28961568fe22206eb532b4c7ce76cd`
- exact output blob: `c169d6c15d76372c06d08433a72c50c58c5430e3`
- terminal marker: `PASS MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`

## Assigned partner consumed

Newest assigned partner account04/B08 run `20260922T041159Z-account04-B08-moc4-r11`, report blob `30448cadc8902a3b38f080fd1923392393e997ed`:
`MOC4-BIDIRECTIONAL-V4-PAIR-CEILING-v1` and `MOC4-ZERO-RESERVE-ENDPOINT-STAR-RIGIDITY-v1`.
Its earlier exact dependency `MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1`, blob `ccc5358d81a9432f3764a9a89be9a01c6bb54e26`, is used directly below.

## New theorem

`MOC4-TRANSPOSE-SUBGROUP-ROOF-v1`: for either genuine row/column relabeling action and every subgroup `H<=S4` containing a transposition, the uniform true-unitary `H`-orbit average has a positive common endpoint lift. Symmetrizing the lift by `H` makes it `H`-invariant, so the orbit support average lies between the minimum and maximum corresponding `H`-coset endpoint averages. This extends the valid two-point pair-symmetrized lift without asserting any individual-unitary common lift.

`MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`: every `n=4` determinant-support relabeling orbit lies in the span of constants, singleton-assignment indicators and unordered two-subset-assignment indicators. On that exact span, seven transposition-containing subgroup averages satisfy the exact cubature identity

`f(e) = (1/3)A_H1 f + (1/3)A_H2 f + (1/2)A_H3 f + (1/3)A_H4 f + (2/3)A_H5 f + (1/3)A_H6 f + (1/2)A_H7 f - 2 A_S4 f`.

The verifier checks this identity exactly on all 53 spanning generators with `Fraction` arithmetic.

## Decisive application

On account04/B08's hard simple-complex residual datum

`a=(-4+4i,-i,-3+2i,-4-4i)`,
`b=(-4-4i,2-i,2-4i,4-i)`, `eta=1`,

one true-unitary relabeling side has seven exact subgroup roofs

`[-47/2,-7/2,32,58,231,-68,-134/3]`,

with endpoint `M=256`, mean `m=-217/2`. The exact cubature theorem gives

`h(U) <= 1057/3` for every true unitary,

hence any positive gap obeys

`gamma <= 289/3`.

The assigned partner's bidirectional pair/V4 bound on the same endpoint datum was `gamma<=529/4`, so this is an exact further reduction by `431/12`.

On the preceding real lead datum `a=(-1,2,1,0)`, `b=(-1,1,-2,2)`, the opposite coset orientation gives the exact target roof `Lambda=36=M`, independently closing that whole support direction.

## Updated first missing implication

`MOC4-SUBGROUP-RESIDUAL-STATIONARITY-v1`: after taking the minimum of the two subgroup-cubature bounds and the bidirectional V4/pair ceiling, exclude every genuine global support maximizer with the remaining positive gap using the exact same-unitary `P-R-D`, pair-Rayleigh and Cartan/Hessian constraints; or construct a source-valid true-unitary target counterexample.

The new group-orbit constraints are valid for actual unitaries and do not replace common-unitary compatibility by arbitrary bistochastic data. A discarded exploratory LP that incorrectly mixed row and column orbit functions was caught and is not part of the theorem.

Suggested recipients: account04/B08 assigned partner; account03/B08 and account03/B09 for same-unitary residual integration; account03/B20 for campaign integration.
