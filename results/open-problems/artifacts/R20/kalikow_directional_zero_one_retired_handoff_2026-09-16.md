# Retired R20 handoff — Kalikow higher-dimensional directional zero-one

Status: RETIRED FROM R20 by the 2026-09-16 R-series redeployment. This file preserves the final state visible in the immediately preceding R20 work so a future reassignment does not restart from scratch. It is **not** a new claim of proof and was not independently re-audited in the Paley run.

Target was the iid nearest-neighbor elliptic RWRE question in d>=3: whether P_0(X_n·ell -> +infinity) is always 0 or 1. The milestone was uniformly elliptic d=3. No closure was claimed.

Final retained route at retirement:

- semantic harmonic function h_x=P_{x,omega}(A_ell), q_x=h_x(1-h_x), local semantic energy V_x=sum_e omega_x(e)(h_{x+e}-h_x)^2;
- exact potential identity q-Kq=V and excursion identity E_z sum_{n<tau_z^+} V_{X_n}=q_z/G_omega(z,z);
- one-row Möbius representation after freezing all rows except z: h_z(p)=(p·a)/(p·c), with p·c the no-return probability after first departure;
- conditional row influence is first-order visible: nonconstant row response forces nonzero covariance with row coordinates;
- row influence bound with one escape factor: under kappa-uniform ellipticity, \bar w_z Var_nu(h_z) <= kappa^{-4} E_nu[h_z(1-h_z)];
- same-environment two-walk identity for ordered opposite phases: sum_z E[r_{0,z}^2 h_z(1-h_z)] equals the annealed expected common-range size on {X -> +ell, Y -> -ell}; the common range is finite pathwise, but finiteness of its annealed mean remained open;
- deep influential traps have a two-gate structure: all neighbor escape probabilities are small, while at least two rare nonreturn gates have separated conditional directional-phase probabilities;
- every deep trap has a finite local cylinder certificate, and under uniform ellipticity a certificate for escape scale eta requires radius at least c_kappa log(1/eta).

Remaining obstruction at retirement: prove a sufficiently strong probability/moment bound for large two-gate metastable traps, or prove finite annealed mean for the ordered opposite-phase common range. These were the highest-value next attacks. The directional zero-one problem remained OPEN.

The new R20 owner problem is I0100 / Randomstrasse 2025 Conjecture 26. Do not continue the Kalikow route under R20 unless the fleet explicitly reassigns it.
