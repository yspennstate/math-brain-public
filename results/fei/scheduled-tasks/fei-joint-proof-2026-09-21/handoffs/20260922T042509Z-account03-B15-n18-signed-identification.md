# FEI handoff — account03/B15 — n=18 one-step signed-identification rigidity

**Run:** `20260922T042509Z-account03-B15-r11`  
**Control revision:** `2026-09-22.2`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full FEI:** **OPEN / NOT PROVED**

## Source-bound result

Current common candidate: `LIMIT-PRIME-GATE-LIFT-v1`, with center `C*=6.5218512` and unpaid universal implication `D_{Gamma_*}(P;p)>=0` for every composition-prime Boolean gate and every interior product-bias vector.

Named other-account artifact consumed: account01/B12 `20260922T011847Z-prime-n18-gate/REPORT.md`, blob `9ab98c0e82f7cf0f34eac98923df23b7b160670b`. It supplies the source-valid balanced composition-prime n=18 gate, truth-table SHA-256 `f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`, `I=261/128`, and its certified entropy interval.

New theorem: classify all `2*C(18,2)=306` one-step signed identifications `X_b=X_a xor s` of that exact source gate. Exactly 90 are balanced: 72 host-host identifications and 18 matched core-host identifications. Every balanced identification has exact total influence `261/128`; all 36 one-coordinate fixings are unbalanced. Every host-host merge has the exact entropy identity

`H(child)=H(source)-1/128`.

The other 18 balanced identifications have strictly smaller entropy by exact-rational logarithm enclosures. Consequently every balanced one-step signed identification satisfies

`H/(I-1) < 6.514326913930565372650625175956097266`,

leaving certified gap

`C* - H/(I-1) > 0.007524286069434627349374824043902734`.

Thus the adversarial escape “strengthen the near-extremal n=18 obstruction by one signed coordinate identification” is **REFUTED** for the complete 306-map family. This is not a generic entropy monotonicity theorem.

Scientific archive root:
`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T042509Z-n18-signed-identification-rigidity/`

Readback blobs: report `e95ec2f7c69de7de2467b2e9c83ee95c14cafa3d`; checker `14a22c4814292b13eb7912f26683e79af7ee523f`; output `303e527e079a685ba46b0cb4cf7de76a188a41b3`.

## Required continuation fields

`candidate_version`: `LIMIT-PRIME-GATE-LIFT-v1`  
`prior_missing_implication`: universal prime-gate/all-bias nonnegativity of `D_{Gamma_*}`.  
`new_proved_inference_or_exact_failed_claim`: all one-step signed identifications of the exact n=18 source gate are classified; none yields a stronger balanced obstruction.  
`replacement_obligation`: move to genuinely biased product points, changed exceptional support/host group sizes, or a universal rigidity/compactness argument; do not spend another run merely merging two coordinates of this source gate.  
`peer_artifact`: account01/B12 n=18 composition-prime certificate, blob `9ab98c0e82f7cf0f34eac98923df23b7b160670b`.  
`next_recipient`: `account03/B18` primary; `account01/B12` secondary.  
`implication_to_full_FEI`: unchanged; proving universal prime-gate/all-bias `D_{Gamma_*}>=0` would imply full FEI with finite constant `6.5218512`.
