# R18 cumulative ledger

**Main target:** Salem's fourth problem for classical Bernoulli convolutions.  
**Full classification:** **OPEN**.  
**Lehmer reciprocal AC/singularity:** **OPEN**.

| ID | Status | Statement / scope | Source |
|---|---|---|---|
| R18-GH-C001 | **PROVED** | Polynomial translated-interval discrepancy for the four neutral phases of Lehmer's Salem number; deterministic Cartesian-product box discrepancy | `runs/2026-09-16/2026-09-16_12-50-00_UTC__R18__tri-geometry-a7c3__report.md` |
| R18-GH-C002 | **PROVED** | Residual coefficient phase geometry: 34 strict-triangle, 18 degenerate, 12 nontriangle magnitude classes; strict Jacobian lower bound and nontriangle defect | same |
| R18-GH-C003 | **PROVED** | Two-gap four-neutral small-ball bounds: strict `eta^8+Delta`, degenerate `eta^6+Delta eta^-2`, nontriangle fixed gap | same |
| R18-GH-C004 | **PROVED** | Growing truncated inverse-square bounds from C003 | same |
| R18-GH-C005 | **PROVED SUFFICIENT CRITERION** | Exact difference-measure transfer identity; bounded superharmonic majorant implies an L2 density | same |
| R18-GH-X001 | **DISPROVED ROUTE** | Final-return block contraction cannot be iterated because trajectories may exit and re-enter | same |
| R18-GH-C006 | **PROVED** | Bounded-coefficient exact Salem trinomial relations lie in a finite gap box; exact Lehmer residual search has no three-term relation | `runs/2026-09-16/2026-09-16_12-50-30_UTC__R18__tri-baker-b91e__report.md` |
| R18-GH-C007 | **PROVED** | Uniform no-floor polynomial lower bound for every Lehmer residual three-term neutral short packet | same |
| R18-GH-C008 | **PROVED** | Every exponentially action-weighted reciprocal-square sum of those short packets converges | same |

## Current obstruction

The fixed-target short-packet arithmetic is controlled. The next unresolved object is a moving bridge target whose algebraic height grows with the short packet, schematically

`A_s(a,b) + omega_s(a,b) z_s^c conjugate(A_s(a,b))`.

A fixed-target Baker estimate no longer suffices. Current next routes:

1. moving-target height versus available short-gap action;
2. certified superharmonic transfer-operator majorant from C005;
3. exact identity classification kept separate from nonzero near-cancellation.

No entry in this ledger is a full solution of Salem's fourth problem.
