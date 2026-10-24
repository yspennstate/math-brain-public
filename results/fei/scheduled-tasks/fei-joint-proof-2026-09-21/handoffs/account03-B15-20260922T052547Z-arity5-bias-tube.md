# account03/B15 FEI handoff — arity-5 full center-bias tube

Status: `ESSENTIAL_STEP_APPLIED`; full FEI remains `OPEN`.

Source-bound scientific artifact:
`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T052547Z-arity5-bias-tube/REPORT.md`
at scientific commit `d69b40a0be3d28ad5c5d4a526e35fa3b849ade30`.

Current candidate used: `C^dagger=6.521851214`, `a^dagger=0.268204856`,
`Gamma^dagger=Gamma_0+a^dagger p(1-p)` from account01/B18's fixed all-gate candidate.

Named peer artifacts consumed:
- account01/B17 `20260922T043923Z-arity5-uniform-c001`: all five-input Boolean gates satisfy `D_{Gamma_.01}>=0` at the exact uniform bias vector;
- account01/B18 `20260922T050337Z-complementary-mux-address-tube`: source-bound `|G'(x)|<31` regularity for the same h96 base potential.

New proved inference: for every Boolean gate `G:{0,1}^5->{-1,+1}` and every interior product bias vector with
`max_i |p_i-1/2| <= 1e-7`, the live candidate satisfies
`D_{Gamma^dagger}(G;p)>=0`.  Every nonconstant nondictator in the tube has checked lower defect reserve
`>0.000119819695452307`; when the Poincare denominator is positive this gives the comparable margin
`c_G(p)<0.26811`. Constants and signed dictators are exact all-bias base cases.

Mechanism: the peer center theorem plus the exact uniform lattice gap `W_G>=1/1024` gives center reserve `0.0002521531796875`; a source-valid `|Gamma^dagger'|<85` bound, product-TV control of pivotal prices/output bias, and an orthogonal biased-Fourier rotation plus Fannes-Audenaert bound limit total defect loss to `<0.000132334` throughout the tube.

Prior missing implication: universal `D_{Gamma^dagger}(P;p)>=0` for every composition-prime finite gate and every interior bias.

Replacement obligation: enlarge/patch the off-center five-input bias region (or find a source-valid violating gate/bias), then higher arities. Do not repeat the exact uniform center.

Next recipient: `account03/B18` integration lead. Suggested application: combine this all-gate center tube with the existing certified off-center/dyadic slices and attack the remaining compact five-input bias region.

Execution status: `WITHOUT_VERIFIED_BRAIN`; repository retrieval was authenticated, but no authenticated mathematical-brain receiver/context retrieval was used.
