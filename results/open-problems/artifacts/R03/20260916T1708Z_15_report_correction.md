# R03 run15 immutable-report rendering correction

The immutable report `runs/R03/20260916T1708Z_15_f3_hyperplane_geometry.md` contains one serialization/rendering typo in the displayed Fourier-inversion formula in C242: the coefficient `\frac{2}{3}` was mangled in transit.

The intended and mathematically used formula is

\[
\Pr(\ell(U)=2)
=
\frac{1}{3}
+
\frac{2}{3}\,2^{-s}
\cos\!\left(\frac{(p-q)\pi}{3}-\frac{4\pi}{3}\right).
\]

No mathematical statement, checker input, output, metric value, proof status, or ledger field changes. The source report is left immutable rather than overwritten.
