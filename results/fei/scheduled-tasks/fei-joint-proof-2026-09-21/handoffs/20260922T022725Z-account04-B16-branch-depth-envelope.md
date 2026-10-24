# account04/B16 handoff — heterogeneous branch-depth envelope

Status: **AUXILIARY_ONLY / HETEROGENEOUS_BRANCH_DEPTH_CLOSED**. Full unrestricted FEI remains **OPEN / NOT PROVED**. Execution: **WITHOUT_VERIFIED_BRAIN**.

Scientific source: `proofnet24/P03-fei/fleet-2026-09-21/account04/B16/20260922T021315Z-branch-depth-envelope/REPORT.md`, final scientific commit `e0b28339d504430c0a436fb965c738a269c7678a`, report blob `174269803dc83068a935e86d04b47e169a945a53`.

Consumed peer state: account02/B15 partial-branch renormalization blob `a8fd8e0a00b60ec8a4348d992f8df8d0365449b5`; account01/B17 one-branch shared-core blob `317694313bd078634b62d252fe9efa0085afcb14`; account02/B16 restriction-margin martingale blob `335d6ffa58cae84c7b47e742a250a20d2e2bddd4`; account03/B16 exact Numaro two-step refund commit `4b65fd3a49ec23454eaced80648d5b28e310cd42`.

New theorem: for the exact 19-class source forcing function

`K(b)=H_core(b)+(9/256)[-phi(b^2)+16(1-b^2)]`,

one has the analytic strong-concavity bound

`K''(b) <= -9/64` for every `0<b<=1/4`.

Exact rational-log enclosures put its unique maximizer in

`0.002713295 < b_* < 0.002713296`

and the generic source forcing ceiling at

`K(b_*)/(133/128) < 6.521851213012878`.

For arbitrary heterogeneous **integer one-branch depths** `m>=1`, the reusable singleton stays in the invariant interval `[57/256,57/255]`. Hence `b=c^m` lies either below `(57/255)^4` when `m>=4` or above `(57/256)^3` when `m<=3`. Strong concavity plus exact endpoint comparison gives the tighter reachable forcing ceiling

`T_int = K((57/255)^4)/(133/128) < 6.521851180069836`.

Since every ratio update is a convex combination of the previous excess ratio and this forcing level, **every finite adaptive sequence of integer branch depths** stays below `6.521851180069836`. Relative to account02/B15's completed fixed-depth-four limit upper endpoint `6.5218511673480`, all possible branch-depth heterogeneity has less than `1.3e-8` operator-specific headroom.

Therefore the next nonredundant adversarial work is not another branch length. It must either use a genuinely different balanced gadget with a better joint `(R,D,c)` tradeoff or prove a universal adaptive restriction/block upper mechanism preserving account02/B16's signed descendant credits.

Older interface-C sources requested in the inherited prompt were freshly reread and preserved: account02/B16 actual parent-mask incidence and account03/B18 signed flag curvature. They were not reused in this theorem because OWNER CONTROL revision `2026-09-22.2` later supersedes that phase-switch assignment with the all-gate convergence target.
