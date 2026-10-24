# R19-I0084-C025 readback erratum

This is a transcription-only correction to the immutable report

`runs/R19/2026-09-20_07-45-13_UTC__i0084-weighted-cinfty-envelope-counterexample_c025_m1a19p29.md`

created at commit `3498ff448c8f8b2949a50f027d73fa7e9d11c4bb`.

Exact-commit readback showed that in equations (C025.36) and (C025.37) the LaTeX command `\frac` in the left-hand bracket was corrupted during tool-string serialization, appearing as `rac` after a control-character escape. The mathematical statement and all subsequent estimates already use the intended coefficient correctly.

The two corrected displayed equations are

\[
\frac{d}{dx}\left[\frac{a_n}{2}\phi_{-A_n,n}*k_{r,s}\right](x_{n,u})
\ge
\frac{a_n}{4s^2}d_r^+,
\tag{C025.36 corrected}
\]

and

\[
\frac{d}{dx}\left[\frac{a_n}{2}\phi_{-A_n,n}*k_{r,s}\right](x_{n,v})
\le
-\frac{a_n}{4s^2}d_r^-.
\tag{C025.37 corrected}
\]

No hypothesis, conclusion, constant, proof step, metric, status, or audit claim changes. The original run report remains immutable; this artifact is the authoritative readback correction for those two formulas only.
