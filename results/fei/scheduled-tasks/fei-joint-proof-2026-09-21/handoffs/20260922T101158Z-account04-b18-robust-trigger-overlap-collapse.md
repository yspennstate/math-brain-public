# account04/B18 handoff — robust trigger overlap collapses to support-hidden curvature

Status: `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN / WITHOUT_VERIFIED_BRAIN`.

Scientific source: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-22/account04/B18/20260922T101158Z-robust-trigger-overlap-collapse/REPORT.md`, creation commit `8139bb68a3d9e108c4dde159a11f70d7fbae8bcd`, read-back blob `db0b47d50ecccd086c9545439a206686f3624784`.

Consumed peer/source inputs:

- account01/B18 newest shaped-safe frontier, commit `a5f19f05fa03671fb5ffeb435081ed92e9827e6a`; its `eta_{epsilon_*}` direction is universally nonnegative under literal physical singleton reveals and therefore does not consume the A/B crossing banks;
- account04/B12 robust-row codimension staircase, commit `a1b2a93210fe7cc871cd10c5bbbf43b1b983a254`;
- account04/B13 near-optimal singleton-safe direction, commit `c50e06733fc1e7f109e20dbb1a0013d67aa71dc7`, superseded in scalar sharpness by the newer account01/B18 value and not double-counted;
- account04/B14 MUX coordinate-marginal block credit, commit `d760311c3190002395f33b11fad6d12e5950be56`, retained only at its MUX scope;
- account01/B18 curvature-refunded crossing theorem plus account04/B18 visible/hidden curvature and terminal-surplus reductions.

New proved inference.  Split the preceding hidden bank as

`U4 = H4 + O4`,

where

`H4 = sum_{k,i!=k} (4+j'(q_k)) [p_ki - 2 c_{k<-i}]`

is support-hidden curvature and `O4` is the weighted opposite-sign-overlap term.  For every centered `F/J`-critical core with ratio `rho>4`, if `R` denotes the relative-`1/16` robust derivative rows and `r_i` their physical trigger codimensions, then

`sum_{i in R} r_i q_i <= (2/11)[P-DTC(X)] + (1/11) H4`.

Fresh B12 also gives `r_i>=3`, hence

`sum_{i in R} q_i <= (2/33)[P-DTC(X)] + (1/33) H4`

and therefore

`sum_{i in R} q_i < 0.174873 J + 0.030304 H4`.

Mechanism: B12 gives `p_ik >= 7 q_i/4` for every actual trigger; Boolean-square integrability gives `p_ik=p_ki`; exact B18 splitting gives `p_ki=2c_{k<-i}+[p_ki-2c_{k<-i}]`; summing the actual incidence set before spending any bank removes repeated-trigger charging.  On a `rho>4` terminal core, the inherited derivative bound `j'(q)>16/7` gives the global weight floor `4+j'(q)>44/7`, which yields the exact coefficients above.

This strictly sharpens the prior B18 remainder for the robust-address subproblem: opposite-sign curvature is still preserved in the exact mixed-curvature law, but it is not needed to pay robust trigger addresses.  The remaining bank for this specific overlap problem is the smaller `H4<=U4`.

Unpaid arrows remain:

1. pay or realizably eliminate `H4` on positive-defect terminal critical cores;
2. handle nonrobust positive-defect rows outside the relative-`1/16` class;
3. prove the live repaired all-gate candidate `Gamma_*` on every composition-prime gate/bias (including boundary limits) or give a genuine prime counterexample.

Exact zero-defect classification is unchanged: all-zero folded depth defect forces a character-twisted signed one-point defect and `H<4J`.  No refuted prescribed-coordinate payment, fixed-relative near-subcube bridge, raw `sum d_i=O(J)`, blind arity induction, or AND/decomposable extremality claim is revived.  Full FEI remains OPEN / NOT PROVED.
