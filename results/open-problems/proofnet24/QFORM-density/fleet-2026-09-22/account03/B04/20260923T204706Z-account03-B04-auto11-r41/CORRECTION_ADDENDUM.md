# Numerical correction addendum

The theorem statements, derivations, example determinant, spectral brackets, and new bound in `REPORT.md` are unchanged. One comparison decimal in equation (6.6) was mistyped after the proof was committed.

The completed peer scalar-pivot formula there is correctly stated as

`128 * 15^(-1/4)`.

Its numerical value is

`65.04099176379069...`,

not `65.016...` as written in the prose of equation (6.6). The deterministic checker records the corrected value. The comparison remains stronger than claimed qualitatively: the new zero-pivot product-rearrangement bound `1.9309787692112597...` improves the peer scalar-pivot numerical bound by a factor exceeding 33 on the same example.

This addendum preserves the immutable original report while correcting the only detected numerical transcription error.
