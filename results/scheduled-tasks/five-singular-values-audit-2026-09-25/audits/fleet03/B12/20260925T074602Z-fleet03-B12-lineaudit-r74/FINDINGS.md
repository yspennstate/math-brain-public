# r74 findings

- No new fatal mathematical defect on lines 1–240.
- C04: abstract line 41 missing no-pivot qualifier — literal descriptive FALSE, repair local.
- C05: outline line 65 says “has a ... singularity” where only an upper envelope is proved — literal descriptive FALSE, repair local.
- C06: line 148 says “Both” for three assertions — wording FALSE; change to “These assertions”.
- Line 148 padded-index proof coverage — GAP; for j>min(rows,cols), use s_j(T)=0 and B=T.
- C07 current-open-status claim — UNCHECKED.
- Line 222 zero-beta phrase — PASS under numeric reading (“factors are at most 1”), not a cardinality assertion.
- Repaired mathematics in audited ranges remains unrebutted under P3.
