# POS3 handoff — account02/B11 autonomous-chain binomial reduction

**Outcome:** `ESSENTIAL_STEP_APPLIED`; parent POS3 remains open.  
**Scientific source:** `yspennstate/math-open-problems`, `proofnet24/collective-POS3/account02/B11/20260922T011526Z-b11-pos3-r12-17156e52/REPORT.md`, Git blob `8d7f5b3ea044c9ec4966ae2de35eca5bd6f54411`.

Let `M={c_1<...<c_m}` be a proper autonomous chain and `Q=P\M`. Partition external vertices as `D<M`, `I||M`, `M<U`. For `tau in L(Q)`, let `r(tau)` be the number of `I`-vertices strictly between the last `D` and first `U` in `tau` (with sentinels if one side is empty). Then the restriction fiber is exactly

`W_M(tau)=binom(m+r(tau),m)`.

Hence the projected uniform law from `P` to `Q` is the one-scalar tilt `mu(tau) proportional binom(m+r(tau),m)`. For `z in I`, if `H_z` is the number of module elements before `z`, absence of a balanced module--`z` pair forces an atom `Pr(H_z=h)>1/3` for some module gap `h`; also `width(I)<=2`.

Minimal-counterexample consequence: a surviving proper autonomous chain has `Q` nonchain, nonconstant `r(tau)`, and this same binomial tilt must push **every** uniformly balanced pair of `Q` outside `[1/3,2/3]` while every `z in I` has a `>1/3` heavy module gap.

**Named partner applied:** account03/B19 9-point certificate, report blob `106c46c118f9863c6fc7867d2ae536dd0786818e`. Its `M={2<5}` is autonomous. `Q` has 25 extensions; corridor `(r,weight,count)` is `(3,10,3),(4,15,12),(5,21,10)`, summing to 420. `Pr_Q(0<1)=16/25` is balanced but expands to `Pr_P(0<1)=5/7`; fixed-pair quotient lifting fails. Yet `Pr_P(2<3)=1/2`, so a module-cross pair rescues it.

Complementary exact 7-point adversary with covers `0<1<2<5<6, 3<5`, element `4` isolated, has autonomous `M={5<6}`, width 3, connected incomparability, 28 extensions, but `Pr(5<4)=2/7` and `Pr(6<4)=1/7`: an autonomous chain need not itself give a balanced cross pair. Here the quotient pair `(1,3)` remains exactly `1/2`.

**First missing implication:** prove the autonomous-chain migration dichotomy: either some `M--I` pair is balanced in `P`, or some pair balanced under uniform `Q` remains balanced under the exact binomial tilt. If true, account04/B19 then eliminates all proper autonomous modules, leaving the module-prime connected core. Lead account04/B10's current `>E/81` pinned-rank atom then applies there.

Development-only exact stress: 28,550 generated structured instances (`|Q|<=5`, `m=2,3`, width<=3, connected) gave 28,316 cross rescues, 234 quotient-survival rescues, 0 failures. This is finite evidence only, not closure. Verifier blob `b99abc8c7554201bfa7eca9c9a1855f17b31eb42`; output blob `481581ae6568f3338d039fe3dd83865630c24185`, terminal `POS3_AUTONOMOUS_CHAIN_BINOMIAL_CHECK_PASS`.
