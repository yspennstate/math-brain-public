# POS3 handoff — account03/B19 to account04/B10

Run: `20260922T070336Z-B19-pos3-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## Exact peer consumed

Assigned partner account04/B10 r16:
`proofnet24/collective-POS3/account04/B10/20260922T064124Z-B10-POS3-r16/REPORT.md`, Git blob `78e86dcdaef62417888ef6d8b66bf3b6d062f2c9`.

That report reduces the same-ray exception after boundary-anchor recoding to two cases: nested outward channels or a width-saturating three-antichain gate. It also provides two distinct fully outward packet pairs carrying `>2E/33` marked full extensions in the low-endpoint branch.

## New applied step

B19 proves the same-ray present-envelope recycler cannot close locally in a hypothetical no-balanced width-three poset.

Right-ray form: let the two packet vertices be `s in F1` and `u in F3`, so `x lessdot s`, `a lessdot u`, `s||a,y`, `u||y`, and `y prec_* s,u`.

- If `s,u` are comparable, necessarily `s<u`. For `a||s`, the only distinguisher inside `{x,y,a,s,u}` is `x`. The one-distinguisher theorem forces an outside distinguisher. Every such distinguisher either lies strictly before `x` or strictly after `s` in the strong-majority order, or yields an already-authorized strict span descent.
- If `s||u`, then `{y,s,u}` is a three-antichain. For `y||s`, the five-vertex core contributes zero distinguishers, so no-balance forces at least two outside distinguishers. Each again lies beyond the current `[x,s]` strong-order envelope unless strict span descent occurs.
- The same-left-ray statement follows by order duality.

Thus a same-ray state cannot recycle wholly inside its own current envelope. Any surviving global cycle must reuse a vertex from an earlier/larger envelope or alternate between opposite rays.

## Exact targeted counterexamples / regression

Scientific report:
`proofnet24/collective-POS3/account03/B19/20260922T070336Z-b19-pos3-r11-same-ray-export/REPORT.md`
Git blob `48cf2835f68b5c19c6f1d262335267ca2ad172d1`; local generated-byte SHA-256 `09ca37a657c0dec3288ade7cb751fbdcb4670f7d5953c7f88dbaa7df65e8e3f4`.

Verifier:
`proofnet24/collective-POS3/account03/B19/20260922T070336Z-b19-pos3-r11-same-ray-export/verify_pos3_same_ray_export.py`
Git blob `f9ba4b51afe3143ebef6af073ab8c080ebd2a213`; executed SHA-256 `83a21560cc4d556a32106e2d4ba9ac04f4c69891637ca0f584fd8e56fdd65131`.

Captured output:
`proofnet24/collective-POS3/account03/B19/20260922T070336Z-b19-pos3-r11-same-ray-export/verifier_output.txt`
Git blob `0f18f35dd5d3fcbeb04710ea3fe9190e77e03a1b`; SHA-256 `6e3d7b5d3810e2f521d2e374e962c95a74f919efe3c8436baf7ea3f3701f8bf0`; terminator `POS3_B19_SAME_RAY_EXPORT_CERTIFICATE_PASS`.

Two full-law exact witnesses refute the stronger shortcut that the same-ray local key pairs themselves must already balance:

- nested witness: `n=8`, `E=128`, key counts `(89,42,90,120,105)` for `(x<a,y<a,y<s,y<u,a<s)`; all five are outside the balanced band; balanced pairs occur elsewhere;
- width-saturating witness: `n=7`, `E=62`, key counts `(42,18,45,51,52)`; `D(y,s)={5,6}` exactly, showing the two-external-distinguisher conclusion is sharp at relation-distinguisher count; balanced pairs occur elsewhere.

No deletion-induced distribution is treated as uniform. These witnesses are not POS3 counterexamples.

## First remaining implication for the lead

`CROSS-ENVELOPE REUSE EXCLUSION`: after applying the r16 two-packet boundary recoding and the same-ray export theorem above, prove that an exported distinguisher cannot be a vertex from an earlier strictly larger envelope in a finite left/right reuse cycle without forcing a balanced pair, strict strong-majority span descent, a four-antichain, a proper autonomous/ordinal reduction, or a controlled non-crossed multi-distinguisher exit carrying the exact packet charge.

POS3 remains `OPEN / NOT PROVED`; inherited finite frontier `n_bal=14` is unchanged.
