# account04/B18 handoff — prime repair barrier and Bellman envelope

**Status:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Source-exact scientific root:

`proofnet24/P03-fei/fleet-2026-09-21/account04/B18/20260922T071537Z-prime-repair-shape-barrier/`

in `yspennstate/math-open-problems`.

Principal artifacts:

- `REPORT.md`, blob `10fe27f959269ff47003d1c27a17f7d6d36168f3`;
- `PRIME_BELLMAN_ENVELOPE.md`, blob `1c0f2010f45d1ca25e23d5ef53c46b9ab71279f0`;
- checker commit `16fe8076cfce8f4e17818c8e8e68f812d9f70663` and output commit `85102a11198e9f9db86fbd875cdaf3e77d074696`.

Consumed current source:

- account01/B18 corrected owner pivot, blob `13aacee16ac78f05d89cde2d493a115cf3579d6a`;
- account03/B12 exact biased prime refutation, blob `36fea824c2dcae8c65c3d485e5d5714899699855`;
- account04/B14 exact composition-primality proof, blob `43ad8483eb8a56cb7141a33821ab89e4119dbc49`;
- account04/B15 exact gate-slack composition law, blob `f28787116ef84606407150d3c4619bb8811bb928`.

New exact repair barrier.  For the known prime witness at output `r=967/2048`, put `d=-D_{Gamma^dagger}>0.017611` and write any additive repair as `Gamma=Gamma^dagger+eta`.  Let

`E=eta(1/2)`,
`A=(eta(3/8)-E)_+`,
`B=((967/1024)E-eta(r))_+`.

Then every repair of this witness must satisfy

`(57/256) A + B >= d - (1121/1024) E`.

Hence every repair obeying the two local concave/unimodal inequalities `eta(3/8)<=eta(1/2)` and `eta(r)>=(967/1024)eta(1/2)` must raise the center above `6.5379383362`; in particular this excludes symmetric concave endpoint-zero additive repairs below that cap.  This is a repair-class exclusion, not a FEI lower bound.

New exact Bellman reduction.  Define `T Gamma(p)` as the infimum of the gate RHS over unary identity and all composition-prime Boolean gates/bias vectors with output `p`.  Identity gives `T Gamma<=Gamma`; the exact composition theorem implies that finite symmetric `Gamma` satisfies all gates iff `T Gamma=Gamma`.  `T` is monotone and continuous from above.  Therefore, for any finite symmetric seed `Gamma_0`, if every descending iterate `Gamma_{m+1}=T Gamma_m` remains nonnegative, the limit is a nonnegative fixed point and full FEI follows with constant at most `Gamma_0(1/2)`.  Conversely this positivity condition is equivalent to existence of a nonnegative fixed point dominated by that particular seed.

Applied to the refuted seed, the exact 18-input prime witness forces

`T Gamma^dagger(967/2048) <= Gamma^dagger(967/2048) - d`.

Thus the canonical envelope performs the downward-dent branch of the repair barrier immediately.  The next smallest honest implication is to determine whether this forced dent can propagate under the second prime-envelope step to a negative value, or prove all iterates remain nonnegative.  A negative iterate kills only the dominated-`Gamma^dagger` route; positivity of all iterates would close FEI at `C=6.521851214`.

The newest B12--B14 MUX/collar facts are retained only as fixed-seed local certificates after the prime refutation; they are not counted as universal closure credits.  The exact mixed-curvature zero-defect classification and all prior refuted bridges remain preserved.
