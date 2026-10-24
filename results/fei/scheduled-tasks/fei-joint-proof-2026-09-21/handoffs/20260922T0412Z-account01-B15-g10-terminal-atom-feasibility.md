# FEI handoff — account01/B15 — G10 terminal-atom feasibility

Status: `ESSENTIAL_STEP_APPLIED` for the explicit G10 stopped corridor; full FEI remains OPEN.

Scientific source: `yspennstate/math-open-problems`, commit `8c6d5f2de7bc6ebe90b6cd611ca14f853af20d8a`, path `proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260922T0405Z-g10-terminal-atom-feasibility/REPORT.md`, blob `04e4cb693cd1d3fd6709f3ae27cdb8aa2a067c29`.

Consumed exact peer inputs:
- account04/B12 `20260922T0254Z-and-atom-stopping`, blob `8a35d08850c8bf38a36c58af4ee3dcd670fa0de9`;
- account02/B12 `20260922T025438Z-gate-margin-falsification`, blob `bf37b4fd5ceae2c40e2b59266e2701fed8ff2780`.

For symmetric endpoint-zero `Gamma`, write `C=Gamma(1/2)`, `g=Gamma(1/4)=Gamma(3/4)`. Using the exact G10 stopping weights, the retained-terminal preblock slack is

`D_block = (71/128) C + (29/64) g - (H10 - 29/32)`.

The negative entropy refund is exactly `-29/32`. Terminal AND/OR certification is `g<=C-2`; preblock certification is

`g >= T(C) := (64/29)(H10-29/32-(71/128)C)`.

The feasible interval has exact width

`(C-2)-T(C) = (129/58)(C - H10/(129/128))`.

Hence the complete common-potential terminal-atom subtraction problem for this fixed G10 corridor is feasible iff

`C >= R(G10) = H10/(I10-1)`.

At equality the unique quarter value is `g=C-2`; above it there is positive room. Thus this explicit unbalanced corridor adds no center obstruction beyond the already-known balanced G10 ratio. It does not construct a universal Gamma and does not prove FEI.

Execution label: `WITHOUT_VERIFIED_BRAIN`; repository retrieval only, no authenticated cognitive-brain context consumed.
