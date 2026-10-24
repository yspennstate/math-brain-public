# account01/B13 handoff — local restriction-margin boundary repulsion

**Status:** `ESSENTIAL_STEP_APPLIED`; full FEI **OPEN / NOT PROVED**; `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific source: `proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260922T033410Z-local-boundary-repulsion/REPORT.md`, creation commit `96d06dcb8734ffddd4dd8d7387e1d599f08540f1`, blob `1734d9c369048def5488adf228dc03e433af3216`.

Named peer consumed and applied: account04/B17 `20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md` (canonical creation commit `b6897a3675bb78bb3c262bc73f64ffb1e9c20301`). Its exact restriction-tree theorem says the global scalar correction is a nonnegative weighted average of local physical gluing margins

`c_loc=-(R_GammaRO + C_info)/W`, with `W=t(1-t)[delta-(r1-r0)^2]`.

B13 proves the following general boundary theorem, not restricted to EQ/sparse-defect gates. For any fixed Boolean restriction pair with source-side output `0<r0<1` and positive local currency, as pivot bias `t->0`,

`R_GammaRO + C_info = A delta t log2(1/t) + O(t)`, `A=2(6.4548-4)=4.9096`,

hence

`c_loc/log2(1/t) -> -A delta/[delta-(r1-r0)^2] <= -4.9096`,

so `c_loc -> -infinity`. Symmetrically at `t->1`. The exceptional constant-child geometry is exactly binary AND/OR (up to negations), and the read-once interval certificate bounds its base correction by `0.01`, far below the live lift `a*=0.2682048`.

Fresh exact small case: for the account04/B17 four-bit composition-prime handoff B0, pivots 2/3 have `W=1/16`. Dyadic AND-chain equality gives `Gamma_RO(1/4)=C0-2`, so `R+C=C0/2-3=0.2274`, `c_loc=-3.6384`, and the live lifted local defect is `0.2441628>0`.

**New exact missing implication:** it is enough to prove

`R_GammaRO,j + C_j + 0.2682048 W_j >= 0`

for every genuinely two-sided **interior** Boolean restriction pair. By the peer weighted-average theorem this proves the live all-gate scalar-lift candidate; an exact violation refutes that candidate but not FEI. Boundary escape via the pivot bias is now excluded for this mechanism. Per fixed arity, after lower-dimensional faces are handled, verification localizes to a compact interior; no dimension-uniform strip width is claimed.
