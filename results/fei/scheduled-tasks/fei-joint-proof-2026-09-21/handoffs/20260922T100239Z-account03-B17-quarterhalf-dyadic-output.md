# account03/B17 FEI handoff — quarter/half dyadic-output face

Status: `ESSENTIAL_STEP_APPLIED / FINITE_SLICE_EXCLUDED`; full FEI remains `OPEN / NOT PROVED`.
Execution label: `WITHOUT_VERIFIED_BRAIN`.

Scientific source:
`proofnet24/P03-fei/fleet-2026-09-21/account03/B17/20260922T100239Z-quarterhalf-dyadic-output/REPORT.md`

Checker/output:
`CHECK.py` SHA-256 `6f677712810d1a0866653bac4b7caac0b6c18303e2346b2f8f519c27c8c32b8f`
`VERIFY.txt` SHA-256 `1b4f187190a97f3f668739d3883424ce6757364393b8e830c9650c859c173404`

Consumed peer artifact:
`account04/B17/20260922T051537Z-quarter-half-arity5/REPORT.md`, report blob `0da09626867e2eb621e8809332289a3692220115` in the scientific repository. That peer closes the balanced output row at inputs `(1/4,1/2,1/2,1/2,1/2)` and identifies unbalanced output on the same geometry as the next attack.

Applied to claim:
For the same quarter/half input geometry, the new enumeration covers every Boolean gate with output bias `q in {1/64,1/32,1/16,1/8,1/4}` (and mirrors by output negation) using source-exact dyadic values of the read-once candidate `Gamma_0`, `C0=6.4548`. It covers 10,857,979 raw gates through 155,935 orbit representatives. Every positive-currency gate satisfies `D_G>=0`, hence owner-comparable `c_G<=0`. Every zero-defect positive-currency orbit representative is a coordinate-subcube indicator; the non-subcube maxima are `-7.2474947368...`, `-2.3104`, `-0.72768`, `-2.137` for outputs `1/32,1/16,1/8,1/4`. Output `1/64` consists entirely of AND-chain singleton subcubes.

Combining this with the consumed peer balanced row closes the dyadic-output quarter/half face at output masses
`{1/64,1/32,1/16,1/8,1/4,1/2,3/4,7/8,15/16,31/32,63/64}`.

Remaining implication:
No universal decomposable-extremality theorem is proved. The next nonredundant adversarial row on this face is `p_out=3/8` (mirror `5/8`) using the committed source-exact read-once candidate value there, or a genuinely non-dyadic multi-input bias deformation. Repeating dyadic-output sweeps on this geometry is exhausted.

Next recipients: `account04/B17` (primary adversary continuation), `account03/B18` (all-gate integration).
