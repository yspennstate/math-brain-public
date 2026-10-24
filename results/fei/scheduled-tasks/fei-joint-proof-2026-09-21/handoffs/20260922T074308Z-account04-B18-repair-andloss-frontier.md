# account04/B18 — joint center/shape/AND-loss repair frontier

Source archive: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account04/B18/20260922T074308Z-repair-andloss-frontier/REPORT.md`, report blob `7d295b4d9a480727ee2d08c0214e9ea1f55c99c1`. Endpoint-sign correction: sibling `CORRECTION.md`, blob `97eb0b1652db84049a940e36a4b3d07e3e1567a2`. Full FEI remains **OPEN / NOT PROVED**. Execution: **WITHOUT_VERIFIED_BRAIN**.

The fixed candidate `Gamma^dagger(1/2)=6.521851214` is already refuted as a universal all-gate potential by the exact composition-prime 18-input witness; this does not refute FEI. Let `eta` be any bounded symmetric additive repair, `E=eta(1/2)`, and decompose

`eta(u)=E*4u(1-u)+psi(u)`, with `psi(1/2)=0`.

For the exact prime witness,

`L_wit(eta)=(1078193/1048576) E + R_wit(psi)`.

Account02/B17's exact AND-slack theorem implies, for

`Kcal=sup_{p,q} [-L_AND(psi;p,q)]_+ / [pq(1-p)(1-q)]`, 

that `R_wit(psi) <= 0.069645 Kcal`. Since the certified witness deficit is `d>0.0176114`, every repair obeys the new universal frontier

`(1078193/1048576) E + 0.069645 Kcal > 0.0176114`.

Hence zero normalized AND loss forces

`E > 0.01712763055074555...`, so the repaired center must exceed `6.5389788445507455...`. At `E=0.01`, one already needs `Kcal>0.1052329711`.

Simultaneously, the preceding B18 local-shape theorem remains independent:

`(57/256) A + B >= d-(1121/1024)E`,

where `A=(eta(3/8)-E)_+` and `B=((967/1024)E-eta(967/2048))_+`. Thus at `E=0.01` the repair also needs weighted local shape distortion `>0.006664134375`. A low-center repair therefore needs **both** nonconcave local shaping and actual transport of negative slack into the two-input AND family; it cannot choose only one mechanism.

Preserved invariants: account04/B18 mixed curvature `kappa_ik=p_ik+4o_ik=kappa_ki`, exact zero-depth one-point-defect classification with `H<4J`, and all posted refuted bridges. The newest account01/B18 minimum-counterexample anti-amplification theorem and account04/B12-B14 local fixed-candidate results remain valid at their exact scopes but are not double-counted as repair credits.

Next smallest universal arrow: construct a symmetric nonnegative finite-cap all-gate potential by optimizing the repair against the **actual source-certified AND slack profile** and remaining composition-prime constraints. The free-bump/free-concavity route is quantitatively excluded at low center.
