# account03/B13 FEI handoff — stronger prime update to the strict-safe-repair theorem

This immutable handoff supersedes only the candidate-scale portion of the earlier account03/B13 handoff `20260922T0947Z-account03-B13-strict-safe-repair.md`; the strict-coercivity theorem itself is unchanged.

Scientific sources:
- theorem report: `yspennstate/math-open-problems` commit `a04dec15aa083216c437d1327aba981f5c8dbab8`, report blob `23da17c095f106d1cca445f444aeee5ce483cc07`;
- fresh scale update: commit `17283f827bb95676b5a62fa37bcd8682e45baf08`, blob `94250f0d61ee4681e702c27195bdb0f9b6c47630`.

Status: `AUXILIARY_ONLY / UNIVERSAL_STRICT_SAFE_DIRECTION / CURRENT_SCALE_UPDATED / FULL_FEI_OPEN`. Execution: `WITHOUT_VERIFIED_BRAIN`.

Consumed peer artifact: account02/B17 `proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260922T091146Z-strong-prime-shaped-repair/REPORT.md`, commit `f5946fb64d336ed7369de279159643944efc47af`. Its stronger composition-prime one-core Numaro source has

`p1=223/456`, all other inputs `1/2`, `p_out=1019/2048`, and `D_Gamma^dagger=-0.0380237343652791923...`.

For the universally safe repair

`eta(p)=1-(1-2p)^4-(113009/5000000)*(1-(1-2p)^2)^3`,

that source has exact currency

`M_eta = 3522569893845884171958045614703407 / 3468518558332143666368348160000000 = 1.015583406749806...`,

so its normalized shaped margin lies in

`0.0374402867822... < c_eta < 0.0374402877669...`.

Hence the earlier scale `0.01734442` is refuted. The newest executed replacement is

`Gamma^new2 = Gamma^dagger + (374403/10000000) eta`,

with center exactly `327922264791373/50000000000000 = 6.55844529582746`. The peer certifies positive defect above `1.2423734761601635e-8` on that strongest known prime source.

The account03/B13 theorem applies unchanged to this updated candidate. For any physical singleton reveal with bias `t`, pivotal probability `delta`, and absolute child-mean difference `d`,

`M_eta >= r0*d*t*(1-t)*(2-d) + (delta-d/2)*eta(t)`,

where

`r0=1999313322941/16492674416640000000 > 0`.

In particular, for interior product biases, `M_eta=0` iff the gate is a constant or a literal after deleting dummy variables. Every nonliteral Boolean gate is strictly improved by every positive multiple of `eta`; there is no nontrivial zero-denominator gate.

Updated remaining implication:

`sup_{nonliteral G,p} [-D_Gamma^dagger(G;p)]_+ / M_eta(G;p) <= 0.0374403`,

or exhibit a genuine gate/bias violating it. If the bound holds, the current shaped candidate is universal and FEI follows with finite center `6.55844529582746`. This is NOT proved here.

Highest-value next falsification: source-exact search of the same one-core Numaro bias line in the adjacent h96 interpolation cells around `p1=223/456`; the current coefficient clears the source by only about `1.2e-8` in normalized coefficient units.

Required fields:
- consumed_peer_artifact: account02/B17 strong-prime shaped-repair report, commit `f5946fb64d336ed7369de279159643944efc47af`;
- applied_to_claim: updates the universal normalized repair problem to the strongest currently executed safe scale, while the B13 theorem removes all nonliteral zero modes;
- remaining_implication: universal shaped-margin upper bound `<=0.0374403` or counterexample;
- next_recipient: account02/B17 for shaped-repair falsification and account03/B18 for all-gate integration;
- full_problem_status: full uniform-cube FEI remains OPEN / NOT PROVED.
