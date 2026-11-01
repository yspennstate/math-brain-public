# B16 handoff — signed live-window parent-to-flag map

**Full FEI:** OPEN / NOT PROVED.

**Consumed peer results.** fleet03/B16 `20260921T211732Z-signed-square-root-resolvent/REPORT.md` (blob `be465709537514dc3d483fa61532630ac78dce66`) requires the missing compensation to enter before final positivity. fleet03/B18 `20260921T212630Z-positive-contraction-no-go/REPORT.md` (blob `2025b99b0086b01b6a9833d0ddc02fb4aae4b161`) proves that the genuine central half-band positive current cannot have any bounded positive/PSD contraction to a `J`-paid sink and forces an unaveraged compensation floor `liminf n^3 C_D >= 11/864` on its sparse affine-two-plane family.

**New exact map.** With authentic signed same-syndrome coefficients `b_R(s)`, define

`u_{j,R}(s)=1_{j doubled in R} sqrt(epsilon_R/r_R) b_R(s)`.

Then `sum_j ||u_j(s)||_2^2=E_cen(s)`. On the exact live interval `W=[a,b]`, put

`v_j(s)=int_a^s u_j(t) dt/t^3`.

The live current is exactly

`P_W^cen = sum_j <u_j(b),v_j(b)> - sum_j int_a^b <u'_j(s),v_j(s)> ds`.

For every authentic one-subcube parent of codimension `c_j>=2`, choose two defining coordinates `i_j != l_j` and the physical flag `(i_j,e_lj)`. Its parent signed curvature is exactly `kappa_j=2^(2-c_j)`. The signed atom `T_j(h)=(h/kappa_j) delta_(i_j,e_lj)` therefore satisfies `int kappa^{g_j} dT_j(h)=h`. Applying `T_j` componentwise to the Volterra boundary and bulk terms is an explicit finite-window authentic-parent -> physical-flag pushforward. The `c_j=1` character-parent sector remains an explicit source remainder because its parent plaquette curvature vanishes. **Do not take total variation** of this map: that recreates the proved codimension loss.

**New compensation triage.** On the same genuine sparse obstruction, the Fourier law is exactly `p0=(1-8/N)^2` and `p=64/N^2` with multiplicity `N/4-1`. The full R16 response obeys

`Delta_infty,>2 <= (8+16 ln(3/2))/N`,

so at the half-band the booked R16 bank satisfies `B_d <= (kappa_2+epsilon_d) J = O(n 2^-D)`. Hence `n^3 B_d -> 0` and it cannot meet the required `11/864` compensation floor. Also every charged mode has `(q,k)=(3,1)`, for which the central/Ward gap is exactly zero: `(11/192)(1-1/3)-epsilon_(3,1)=0`. The terminal-code subtraction already inside `b_R` was separately proved by fleet03/B18 to be exponentially too small. These facts do **not** spend or rule out distinct negative-R32 credits or the separate terminal endpoint.

**Remaining implication.** Find a source-exact, nonreused signed companion at the same `(parent, syndrome, time)` level, or a justified high-ratio critical-core reduction, so that the compensated signed Volterra flag measure plus the `c=1` remainder is paid by `O(J(f))`. Any candidate credit must pass the affine-two-plane floor test; the booked R16 bank and Ward gap fail it.

**Next recipients:** fleet03/B16 (live logarithmic/polarization), fleet04/B16 (phase-switch source cancellation), fleet02/B15 (negative-credit arithmetic scale).
