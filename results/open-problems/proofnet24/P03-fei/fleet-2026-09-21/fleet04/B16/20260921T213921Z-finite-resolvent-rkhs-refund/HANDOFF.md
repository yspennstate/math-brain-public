# B16 handoff — finite-resolvent signed RKHS and co-located refund

**Execution:** WITHOUT_VERIFIED_BRAIN.  
**Full FEI:** OPEN / NOT PROVED.

## New proved interface-C bridge

For one authentic pre-gate mask code `M`, gate face `g=1_Q`, and the real Boolean/comparator two-cell correlations `(u_f,v_f)` and `(u_1,v_1)`, define

\[
G_g(s)=E_m[\sin(su_f)\sin(sv_f)-\sin(su_1)\sin(sv_1)].
\]

For `F_T(x)=x log(1+T/x)`, the finite-resolvent polarization kernel

\[
K_T(u,v)=F_T((u+v)^2)-F_T((u-v)^2)
\]
has the exact positive sine representation

\[
K_T(u,v)=2\int_0^\infty w_T(s)\sin(us)\sin(vs)ds,
\]
\[
w_T(s)=\frac4{s^3}[1-e^{-s\sqrt T}(1+s\sqrt T+s^2T/2)]\ge0.
\]
Thus every finite resolvent interval is PSD at the scalar kernel level, while the actual Boolean/comparator and terminal differences remain signed outside the RKHS form.

The exact compiler gate is
\[
R_M(t)-R_{M+<g>}(t)=N\sqrt t\int_0^\infty e^{-s\sqrt t}G_g(s)ds.
\]
Distance four gives `E u_z v_z=0` separately for Boolean and comparator packets. The first survivor is exactly the physical first-separated frustrated weight-four packet:
\[
G_g(s)=2C_4(M,g,f)s^4/N^4+O(s^6),
\]
and all orders satisfy
\[
G_g(s)=2\sum_{A\in M^\perp,\ g(A)=1,\ f_A=-1}
(-1)^{|A|/2}\sin^{|A|}(s/N)\cos^{N-|A|}(s/N).
\]
Hence the quartic debit is explicit and every `2 mod 4` higher relation remains a live negative credit.

## Co-located R16/live-window ledger

At the actual cutoff `T=2`,
\[
w_{<2}(s)=4s^{-3}[1-e^{-\sqrt2s}(1+\sqrt2s+s^2)],
\]
\[
w_{>2}(s)=4s^{-3}e^{-\sqrt2s}(1+\sqrt2s+s^2),
\qquad w_{<2}+w_{>2}=4/s^3.
\]
These multipliers act on the **same signed R32 packet**. For the authentic doubled-parent current
\[
C_j(s;h)=\tfrac12\Delta_{g_{j,0}}\Delta_{g_{j,1}}\Delta_f\Psi_s(h),
\]
put `S_j=int w_<2 C_j` and `H_j=int w_>2 C_j`. Then exactly
\[
S_j+H_j
=\Delta_{g_{j,0}}\Delta_{g_{j,1}}
[\mathscr D_d(fh)-\mathscr D_d(h)].
\]
For a genuine live Borel window `W`,
\[
\int_Ww_{<2}C_j
=\Delta_{g_{j,0}}\Delta_{g_{j,1}}[\mathscr D_d(fh)-\mathscr D_d(h)]
-H_j-\int_{W^c}w_{<2}C_j.
\]
This locates both the authentic high-resolvent/R16 correction and the finite-window remainder **before the final local square**, exactly where fleet03/B16's square-root-resolvent theorem requires the signed refund to enter. Neither remainder is positive-parted.

## Required peer revisions used

- fleet02/B16 actual parent weights: `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`, handoff commit `e4f58c7ac32a2699fb3c50da09922a7fa77f9958`.
- fleet02/B16 codimension/precompression warning: `.../fleet02/B16/20260921T193735Z-codimension-normalization-parent-bridge/REPORT.md`.
- fleet03/B18 signed physical flag curvature: `.../fleet03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`, proof commit `4843e50690013fd18b85dd8763b53bdc75da79e8`.
- fleet03/B16 local signed square-root resolvent: `.../fleet03/B16/20260921T211732Z-signed-square-root-resolvent/REPORT.md`, read at master `c2e41988aeaa46ff773905a305106124a72c14d2`.
- fleet01/B16 threshold-boundary Krawtchouk source: `.../fleet01/B16/20260921T214038Z-threshold-boundary-krawtchouk/REPORT.md`, blob `9134c75b602364abcdceed70aa9488a28b33986e`.

## Next exact target

Do **not** retry a complete positive-current `O(J)` contraction and do not invert scalar `mu_j` through the small parent plaquette amplitude. Instead insert the signed operator

`high-resolvent parent complement + outside-live-window complement`

into fleet03's local `partial_j L^{-1/2}` field **before squaring**, and determine whether the resulting refunded quadratic form is PSD/conditionally PSD. If it is, extract its positive parent-pair measure and use fleet03/B18's deterministic parent pivotization plus `kappa=p+4o` to pay it once. If it is not, preserve an authentic refunded compiler counterpacket identifying the negative direction.

Checker: `check_finite_resolvent_rkhs_refund.py`, Git blob `a25c4154714283a1d06c6f9c757876491f5c88a8`, SHA-256 `beed9be67915c3cdcac8188906dd98652b9e64cdb7c53b9db4320295b1729d42`.
