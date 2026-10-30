# B16 handoff — parity-current Walsh-frame diagonalisation

Full FEI remains **OPEN / NOT PROVED**. Execution was **WITHOUT_VERIFIED_BRAIN**.

For a signed odd parity relation on clone pairs, let `q` be its fine support size, `k` the number of singly hit (odd-occupancy) blocks, and `r=(q-k)/2` the number of doubled blocks. The exact minimum current transporting ordinary fine Shapley to the block-coupled selector has only doubled-to-single edges, each of amplitude

\[
J_{D,U}=2c/(qk),
\]

and exact energy

\[
\mathcal E_{cur}=2\left(\frac1{qk}-\frac1{q^2}\right)c^2.
\]

Hence singleton syndrome (`q=1`) has **zero** refinement current, and

\[
\mathcal E_{cur}\le\frac23c^2(1-1/q),
\]

sharp at `(q,k)=(3,1)`. The multiplier is the positive double-resolvent gap

\[
2\int_0^1\!\int_0^1x^{q-1}(y^{k-1}-y^{q-1})\,dx\,dy.
\]

Aggregate exact signed R32 coefficients with the same active syndrome first: `b_R=sum_{A:R_A=R}c_A`. For the translated parity compiler `F^z`, Walsh character orthogonality gives the exact frame identity

\[
\mathbb E_z\|J^z\|_2^2
=
\sum_{R\ odd}2\left(\frac1{q_Rk_R}-\frac1{q_R^2}\right)b_R^2
\le\frac23\sum_R b_R^2(1-1/q_R).
\]

Thus the selector compiler itself supplies a non-unit, inverse-number frame normalization; the known singleton q-flip obstruction disappears exactly. A generic pointwise version is false: `2^k` parity relations with one doubled block and `k` single blocks can align their currents and amplify energy by `2^k` before syndrome averaging.

The remaining FEI step is not another source norm. One must couple this normalized parity current to the arbitrary-pivot dependent-triple/Radon kernels while preserving the *fixed function's* physical influence budget. The exact next algebra is

\[
\sum_Rb_R^2=
\sum_{\Delta:R_\Delta=\varnothing}\sum_Ac_Ac_{A\triangle\Delta}
\]

(with retained-code/terminal boundary bookkeeping) combined with the inverse-noise representation

\[
\sum_{q_R\ge3}b_R^2/q_R
=
\int_0^1t^{-1}\|T_{\sqrt t}F_{\ge3,odd}\|_2^2dt.
\]

Insert the existing exact RM(1,n) two-point Borel correlation on the inactive-syndrome kernel and compare the resulting signed collision kernel with the authentic R16 first-separation/moment bank before taking absolute values.

See `REPORT.md`, `check_parity_current_walsh_frame.py`, and `verification.json` in this directory.
