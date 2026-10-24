# B16 handoff — cell Möbius phase-switch orientation criterion

**Status:** partial theorem package; unrestricted FEI remains OPEN / NOT PROVED.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

The new exact source identity is, for every dual relation crossing the gate in two odd cells,
\[
r_f=r_U\oplus r_V=r_U+r_V-2r_Ur_V.
\]
Consequently the authentic finite-resolvent gate packet splits as
\[
G=L_U+L_V+O,
\]
with all-order relation coefficients
\[
L_U: 2(-1)^{q/2}r_U a_q,\qquad
L_V: 2(-1)^{q/2}r_V a_q,\qquad
O:-4(-1)^{q/2}r_Ur_V a_q,
\]
where `a_q=sin^q(theta)cos^(N-q)(theta)`.

For every nonnegative finite/live Borel kernel `w`, the mixed channel is an exact signed difference of PSD banks,
\[
\int wO
=\frac14 E\|\Delta_U+\Delta_V\|^2
-\frac14 E\|\Delta_U-\Delta_V\|^2.
\]
This commutes with `w_<2`, `w_>2`, the actual live window, its complement, and the terminal code subtraction.

The decisive no-reuse theorem is
\[
r_Ur_V\ne0\Rightarrow r_f=0,
\qquad
r_f=1\Rightarrow r_Ur_V=0.
\]
Hence the mixed overlap cancels only globally unfrustrated packets introduced by the two one-cell split. It is already spent inside the authentic gate source and cannot be extracted after same-syndrome aggregation as a new external refund.

The sharpened physical target is now a two-bit orientation-preserving coupling. If a precompression pivot sends
\[
p=r_U\oplus r_V,\qquad o=r_Ur_V,
\]
then, using account03/B18's `kappa=p+4o`,
\[
2(r_U+r_V)\le2p+4o\le2\kappa,
\]
and the exact source Möbius refund `4r_Ur_V` lands on the physical opposite-orientation coefficient. This criterion is conditional: the existing parent-mask pivot does not yet establish it for the original Boolean phase `f`.

Consumed exact inputs:

- account02/B16 actual parent weights: `proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`, handoff revision `e4f58c7ac32a2699fb3c50da09922a7fa77f9958`;
- account03/B18 signed physical curvature: `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`, proof revision `4843e50690013fd18b85dd8763b53bdc75da79e8`;
- account03/B16 signed square-root resolvent: `proofnet24/P03-fei/fleet-2026-09-21/account03/B16/20260921T211732Z-signed-square-root-resolvent/REPORT.md`, blob `be465709537514dc3d483fa61532630ac78dce66`;
- account03/B18 critical descent: `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T221012Z-affine-defect-critical-descent/REPORT.md`, blob `075eaed4478012929ddf58cd3fea4d96f221415d`;
- previous account04/B16 finite-resolvent source: `proofnet24/P03-fei/fleet-2026-09-21/account04/B16/20260921T213921Z-finite-resolvent-rkhs-refund/REPORT.md`, blob `9cb2bfed95112b295cb668348aa386e010f7d53a`.

Checker `check_b16_cell_mobius.py` passed 1,500 direct packet identities, 7,500 exact relation coefficient checks, 1,800 overlap-support cases, 3,804 frustrated-source cases, and all four two-bit orientation patterns. SHA-256 `45240f01ad75e2311654962842f1ad18dee27457dcdc9b752695e27a547ad22c`.

**Next exact implication:** construct the original-coordinate coupling `(r_U,r_V)->(p,o)` at the refunded precompression square-root-resolvent field, or find a restriction-maximal Boolean counterpacket to that coupling. Do not return to scalar `mu_j` inversion or reuse the mixed cell overlap as a second credit.
