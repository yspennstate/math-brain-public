# FEI handoff — account03/B17 B0 asymmetric dyadic/curve result

Status: `WITHOUT_VERIFIED_BRAIN`; full FEI remains **OPEN / NOT PROVED**.

Canonical mathematical report: `proofnet24/P03-fei/fleet-2026-09-21/account03/B17/20260922T050305Z-b0-dyadic-curve/REPORT.md` at research commit `44559058711098892c95e71677c809a630b76e38`, report blob `88d4bc458a0dae6e498815d84546af5a3791d5a1`.

Consumed peer artifacts: account01/B18 stable fixed candidate `Gamma^dagger=Gamma_0+0.268204856 z(1-z)`, and account04/B17 exact biased restriction-margin cocycle with retained information credits.

New exact reduction for the prime gate `B0={0,1,2,3,4,5,8,10}`: on biases `(s,s,1/2,1-s)` with `u=s(1-s)`, the output bias is exactly `1/2`, the currency is `W=u/2`, and

`D_Gamma(s)=Gamma(s)+h_2(4u)-2u*C0-Htilde_B0(s)`.

The nonzero squared spectral masses are: `u(1-s)^2` twice, `u s^2` twice, `(1-2u)^2` once, `u` once, `u^2` four times, and `u(1-4u)` once.

Source-exact lattice certificate: for `P12={1/2} union {2^-k,1-2^-k:2<=k<=12}`, all 639 four-bias tuples whose output is also dyadic/mirrored have `D_Gamma0>0` and `W>0`. The certified maximum margin upper endpoint is `c_B0 < -1.5137320439732223`. At `(1/4,1/4,1/2,3/4)`, exactly

`D=(5/8)C0-51/8+(27/64)log2(3)+(25/32)log2(5)`

and `c=-1.5137320439732223821...`.

Replacement obligation: do not repeat this dyadic battery. Primary next step is to use the committed read-once candidate array with interval interpolation to prove/refute the one-variable inequality above for every `0<s<1`; then move to a genuinely non-dyadic multi-parameter B0 deformation if it survives.

Primary next recipient: `account04/B17`. Secondary integration: `account01/B18`.
