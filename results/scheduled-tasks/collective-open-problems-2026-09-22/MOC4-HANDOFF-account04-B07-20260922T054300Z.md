# MOC4 source-bound handoff — account04/B07

Run: `20260922T054300Z-account04-B07-MOC4-r12`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

Canonical scientific root: `proofnet24/collective-MOC4/account04/B07/20260922T054300Z-account04-B07-MOC4-r12/` in the private canonical mathematics archive. Main report blob: `cbc92020a503cc752f2871b3471f6e00346d9560`. Exact verifier blob: `b9179c8d8414aa2c4d027114852fedf68aaa4dce`. Captured verification output blob: `d852346c2d681c817ed6c1bebf71b57e128865e1`. Late-lead addendum blob: `7fdfd4cd96f1b931d0bbef2a1c14e70d566b9a45`.

## Dependencies consumed

- Latest campaign lead now consumed: account03/B07 run `20260922T055130Z-account03-B07-MOC4-r11`, report blob `055492abce4a340ed49b4dbc44787461454c2b71`, theorem `MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1`. It proves the full row/column pair Hessian inequality `||M||_op^2 <= 4(T^2-C^2)` and exact flat-pair traceless-Gram cancellation.
- Required assigned OTHER-account partner: account01/B08 run `20260922T044241Z-b08-moc4-r12`, report blob `f7391a0c2fdeaef6c5fac2bdfbca4513245e5abf`, including `MOC4-V4-BIRKHOFF-GLUE-v1`, `MOC4-COMPLEX-HADAMARD-COMMON-LIFT-v1`, and the interior certificate `8 min P + min R >= 2`.
- Predecessor account04/B07 report blob `0e64ed2b868fbee674c65fc6e3789e8bbbd7867d`, theorem `MOC4-SPINOR-TWO-ROOK-v1`.

## New theorem — P-coupled unistochastic augmentation

In an even-even Spin(6) gauge `(i,j)`, let `p=P_ij`, `B=|N_ij|^2`, and for `p<1` put `S=B/(1-p)`. Let `tau_alpha(i)` be the unique other tetrahedral label having the same sign as `i` in coordinate `alpha`. Then

`a_alpha = P_{tau_alpha(i),j}/(1-p)`,
`b_beta  = P_{i,tau_beta(j)}/(1-p)`.

The augmented matrix

`J^{ij} = [[S,a],[b^T,0]]`

is not merely doubly stochastic: it is **unistochastic**. If `A=N_ij/sqrt(1-p)`, then `A` is a rank-two partial isometry. Choosing unit kernel vectors `ell in ker A*`, `r in ker A`, the block matrix

`W=[[A,ell],[r*,0]]`

is unitary and `|W|^2=J^{ij}`. The same-unitary identity `D=(1/4)E^TPE` gives exactly

`sum_beta B_{alpha beta}=1-P_ij-P_{tau_alpha(i),j}`

and its column analogue, so the kernel-vector moduli are fixed by the same row and column of the original unistochastic `P=|U|^2`.

Consequently every pair of anti-linear block rows obeys

`sqrt(P_{tau_alpha(i),j} P_{tau_gamma(i),j}) <= sum_beta sqrt(B_{alpha beta} B_{gamma beta})`,

with the column analogue as well. Equivalently, the three overlap lengths plus the P-deficit length form a closed complex quadrilateral. This is a nonlinear same-unitary mixed-minor constraint, not a new 24-endpoint positivity claim.

## New boundary rigidity

`MOC4-TWO-ROOK-ROOF-RIGIDITY-v1`: if `B/(1-p)` is a two-rook vertex, the true 4x4 unitary is permutation/phase equivalent to a proper coordinate block unitary (`2+2` for `0<p<1`, smaller blocks for `p=0`, `1+3` for `p=1`) and is therefore MOC4-safe by the known <=3-dimensional cases. Hence whenever a two-rook coefficient minimum is uniquely exposed, a genuine MOC4 support violator must lie **strictly** below that roof; equality is impossible on the non-block-safe branch.

## Exact strictness witness

The rational matrix

`S=[[7/20,7/15,1/15],[7/30,0,31/60],[7/60,1/30,13/60]]`

has total mass two and an explicit denominator-60 convex decomposition into two-rook vertices. Its six determinant-term modulus radicands satisfy the predecessor determinant-hexagon polygon condition, but its augmented column-deficit bracelet fails exactly:

`sqrt(1/10) > sqrt(7/225)+sqrt(13/1800)`.

Thus the new P-coupled augmentation is genuinely stronger than the predecessor's sharp linear two-rook hull plus determinant-hexagon modulus inequalities. This is only a relaxation witness, not an MOC4 counterexample.

## Updated first missing implication

`MOC4-P-HESSIAN-TWO-ROOK-COLLAR-v1` remains open: on the non-block-safe branch, combine the lead's mixed-Hessian reserve (or its flat-pair Gram cancellation at zero reserve) with the P-coupled overlap inequalities above to pay the strict two-rook-roof deficit strongly enough against the subgroup/V4 reserve to force nonpositive total support gap. A refutation must use actual spectra/support and one genuine global maximizing unitary; free `P,R,D` or independently selected gauge data do not qualify.

No singularity or repeated-spectrum exception was introduced by these theorems; the block-safe equality cases include those target cases directly.
