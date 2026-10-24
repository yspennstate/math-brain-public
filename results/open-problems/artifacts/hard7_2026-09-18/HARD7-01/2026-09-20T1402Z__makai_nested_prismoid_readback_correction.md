# HARD7-01 readback correction for the 1402Z Makai report

The immutable report at

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T1402Z__makai_nested_prismoid_defect.md`

was read back at its creation commit. One TeX token in equation (6.21) was mangled during transport: the intended sharp triangle identity is

`|T| * |(T-T)^circ| = 3/2`.

This is already the value used correctly in equation (6.22), `|B^circ| = 3/(2|T|)`, and in the multiplication (6.23). The theorem statement (5.3) and all subsequent algebra are unchanged. This note corrects only that readback typography while preserving the report itself as immutable.
