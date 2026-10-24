# B16 handoff — signed Brownian/Cayley interface C

**Execution:** WITHOUT_VERIFIED_BRAIN.  
**Full FEI:** OPEN / NOT PROVED.

## New proved bridge

For the account01 retained-shell Brownian threshold coefficient
\[
d_{N,k}(a)=2^{1-k}\nabla^{k-1}p_{N-k}(a),
\]
the generating function is
\[
D_{N,k}(z)=2^{1-N}(1-z)^{k-1}(1+z)^{N-k}.
\]
For a same-syndrome relation-weight packet `c_k`, put `B_a=sum_k c_k d_{N,k}(a)`. Then
\[
\mathcal I=\int_0^1\left(\sum_kc_k\lambda_k^{th}(u)\right)^2du
=\frac2{N^2}\langle B,|L|B\rangle,
\quad (LB)_a=(N-1-2a)B_a,
\]
and
\[
\mathcal I=\frac4{\pi N^2}\int_0^\infty
\langle LB,(L^2+t^2)^{-1}LB\rangle dt.
\]
The Cayley transform gives
\[
\sum_aB_a^2=\frac2\pi\int_0^{\pi/2}
\left(\frac{\sum_kc_k(-1)^{k/2}\sin^kx\cos^{N-k}x}{\sin x}\right)^2dx.
\]
Thus the R32 `0 mod 4 / 2 mod 4` sign is literally retained inside the Brownian transform before squaring.

## Authentic parent compatibility

Using account02/B16's actual central weights
\[
\varepsilon_{q,k}=2\frac{2^{-q}}q\left(\frac{2^{-k}}k-\frac{2^{-q}}q\right),
\]
the Brownian image splits over the same doubled parents:
\[
\widetilde\mu^{M}_{R,j}=\frac{\varepsilon_R}{r_R}\mathcal I_R,
\qquad
\sum_j\widetilde\mu_j^M=\sum_R\varepsilon_R\mathcal I_R.
\]
This is a scalar parent mass after the Brownian transform; it is **not** an invented physical pair measure.

## Decisive no-go and required signed remainder

Account02's genuine half-band Boolean counterfamily has exact positive central current divided by `J(f)` tending to infinity, while account03/B18's signed physical flag satisfies `sum E kappa^2 <=4J`. Hence no universal PSD contraction of the complete positive live current into that physical sink exists. Interface C must combine a signed compiler correction before positivity.

The live window is kept as
\[
\int_W E_{cen}s^{-3}ds
=\int_0^\infty E_{cen}s^{-3}ds-T_{cen}(W^c),\qquad T_{cen}\ge0,
\]
and the Brownian/Dirac upper representation retains this tail as an explicit negative remainder.

The exact frequencywise candidate shape is
\[
\varepsilon_R=\frac{11}{192}(1-1/q_R)-\rho_R,
\qquad \rho_R\ge0.
\]
Do **not** spend the Ward comparison bank as a refund unless the authentic R16/Shapley/terminal ledger proves it is co-located and unspent. The next source gate is exactly that ledger identity. Once a residual positive parent-pair measure is genuinely produced, account03/B18 `20260921T195855Z-parent-signed-pivotization` lands it in the signed physical curvature sink with orientation preserved.

## Required peer revisions consumed

- account02/B16 actual parent weights: `.../account02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`, handoff commit `e4f58c7ac32a2699fb3c50da09922a7fa77f9958`.
- account03/B18 signed flag curvature: `.../account03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`, proof commit `4843e50690013fd18b85dd8763b53bdc75da79e8`.
- account03/B18 parent pivotization: `.../account03/B18/20260921T195855Z-parent-signed-pivotization/REPORT.md`, blob `e0ad48a8bb791b0536f5ceda92e3738cc378990a` at master `f536a48b1ae98e22bff294a10adbc59a3b8c907e`.
- account02 half-band obstruction: `.../account02/interactive/20260921T204926Z-threshold-contraction/HALFBAND_COLLISION_EXTENSION.md`, blob `2efc5dedf145a262700649c6e711c6a6fb91d622` at the same master.

Checker SHA-256: `39f5e291eedb7919980f5639c54c36d879cd7a8afe5a9e05ca7b59b3bfdd3f21`.
