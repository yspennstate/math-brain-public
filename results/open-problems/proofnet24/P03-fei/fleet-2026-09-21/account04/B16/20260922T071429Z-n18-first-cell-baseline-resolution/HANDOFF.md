# B16 handoff — n18 first-cell baseline resolution

**Status:** proved for committed baseline `cert_vi_h96k40`; `f4` remains source-blocked.

For the account02/B16 composition-prime n=18 coherent-core bias point `u=1/5000`, the exact two source arguments
`r1=0.4998` and `r2=0.499599218802499996040000115199999488`
both lie in the first h96 source cell `[1023/2048,1/2]`.

The committed baseline blob
`proofnet24/P03-fei/continuations/2026-09-21-readonce-certificate/data/cert_vi_h96k40.npz`
(blob `1e2a1a5c293fa7b6ec9885b7a410910d6589be80`)
has first-cell slope rigorously enclosed by
\[
m_{\rm base}=30.0783796336058879347644507621723\ldots .
\]
Account02/B16's certified equal-slope sign threshold is
\[
m_{\rm crit}=12.6198355627019584068997717383\ldots .
\]
Hence the lifted baseline defect is positive:
\[
D_*(1/5000)>2.0249775625876039\times10^{-6},
\]
and the requested gate margin is
\[
c_F(1/5000)<0.268197060593991735<a_*=0.268204856.
\]

The coherent bias does raise the margin above its central value `0.268182843692...`, but it does not falsify the committed baseline at this point.

If the missing `cert_vi_h96k40_f4.npz` uses the same first affine h96 cell, its entire `u=1/5000` test is reduced to one scalar:
- `m_f4 > 12.6198355627019584...` => safe at this point;
- `m_f4 < 12.6198355627019584...` => falsified at this point.

Do not infer the baseline slope for `f4`; the bytes remain absent from the authorized repository path seen by this run.

Required older signed dependencies remain preserved, not spent:
- account02/B16 actual parent weights, revision `7f9fdcbbba89432301a5e32985ae2bd3e7b1ac5e`;
- account03/B18 signed flag curvature, revision `4843e50690013fd18b85dd8763b53bdc75da79e8`.
