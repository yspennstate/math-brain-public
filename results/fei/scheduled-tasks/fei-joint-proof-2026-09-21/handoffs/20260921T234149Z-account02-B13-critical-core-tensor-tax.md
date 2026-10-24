# account02/B13 -> joint FEI Campaign A handoff

Source-bound scientific artifact: `yspennstate/math-open-problems` private master report
`proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260921T232801Z-critical-core-tensor-tax/REPORT.md`, creation commit `2d3449a3be3930afeb3bd6e0d434b4bddf10f9bf`, report blob `6784e6b31765f4071c2aeaafadc68bcde821c21a`. Exact checker commit `146dfba4419f30151f2fef531281072cb62c180d`; archived output commit `246792215870732b6010f5c4f64245f94c16c849`; notation-only immutable readback erratum commit `be2dc611d6ef1512b18a1743698bcda672256938`.

Status: **ESSENTIAL_STEP_APPLIED for Campaign A critical-core/tensor quantifiers; full FEI OPEN.**

## Exact original-defect core

For every fixed finite `C`, if some Boolean `f` violates `H(f)<=C J(f)`, choose a violating function of minimum ambient dimension. Then it is simultaneously:

- tensor-primitive under every nontrivial disjoint multiplicative factorization;
- strict restriction-critical for every nonempty physical block `A`:
  `Delta_A H - C D_A = delta_C(f)-E delta_C(f_{A=a}) >= delta_C(f)>0`, where `delta_C=H-CJ` and `D_A=J-EJ(child)`;
- invariant as a critical statement under arbitrary character gauges, because restriction of a character multiple is a sign times a surviving character multiple of the same physical child.

Hence Campaign A may center the **original `H-CJ` core** with `I=J` and retain both primitivity and all-block criticality with no tensor loss. This is the safe simultaneous quantifier.

## Folded-cooling tensor compatibility

The completed other-account input actually used was account01/B18's folded-cooling compiler (`.../account01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, blob `9f2bb40584be20e5e440e7f3913873c34858bc91`). For its folded activation `A_z`, define `M_z=max_T E z^{|X triangle T|}`. Then

`A_z=(1-M_z)/(1-z)` and, at a common scale,
`M_z(otimes_r f_r)=prod_r M_z(f_r)` exactly.

At dimension cooling `z_d=1-1/d`, this yields the one-shot factorization tax

`sum_r A_{z_{d_r}}(f_r)-A_{z_d}(otimes_r f_r) <= kappa J(f)`

with `kappa=2 exp(-1/2)-1 < 1/4`.

For account01/B18's additive corrected entropy `F` and `G_lambda=F-lambda A_{z_d}`:

`G_lambda(otimes_r f_r) <= sum_r G_lambda(f_r)+kappa lambda J(f)`.

Therefore any finite primitive bound `G_lambda<=R J` transfers universally to

`H <= [R+(1+kappa)lambda+2/ln 2] J <= [same] I`.

## Zero-tax primitive shortcut is false

For the genuine two-bit one-point defect `w=(1,-1,1,1)`, exact values are
`A_{1/2}(w)=7/8`, `A_{3/4}(w)=15/16`, and
`A_{3/4}(w tensor w)=1695/1024`. Thus
`2 A_{1/2}(w)-A_{3/4}(w tensor w)=97/1024>0`, and for every `lambda>0`,
`G_lambda(w tensor w)/J(w tensor w)=G_lambda(w)/J(w)+lambda*97/2048`.
So a `G_lambda/J` restriction-maximizer cannot be declared tensor-primitive with zero loss.

## Remaining exact Campaign-A arrow

Either formulate the selector/certificate directly on the original minimum-dimensional `C`-critical core above, or prove a surgery lemma reconciling `G_lambda` restriction-criticality with the explicit `kappa lambda` tensor tax. The current result does not prove a finite primitive `R` and does not close FEI.
