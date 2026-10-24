# account01/B07 MOC4 handoff — generic parity-slack refutation + exact X-rescue identity

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Run: `20260922T013731Z-b07-moc4-r11b`  
Outcome: **CANDIDATE_REFUTED** for the universal `MOC4-PARITY-SLACK-v1` gate; parent MOC4 remains **OPEN**.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Scientific artifact

Canonical report: `proofnet24/collective-MOC4/account01/B07/20260922T013731Z-b07-moc4-r11b/REPORT.md` in private `yspennstate/math-open-problems`, report commit `a0fac94c9342ee4a2c18ed94f7fe770bdf0b12df`.

Exact verifier creation commit: `f29fb159c3dc8a3224082a134cfe0cbcdf27d3fe`.  
Verification output creation commit: `35cf58c80fd159e5f6d1b99105d480a91daae207`.  
Verification status: `PASS` with standard-library `Fraction` arithmetic.

## Peer results consumed

- **Named assigned partner account02/B08**, `MOC4-BOUNDARY-CORE-AND-COLLAR-v1`, scientific commit `05ac3fec5e80a9471306a892a397d744faf20f50`: repeated-spectrum/common-block cases and exact opposite scalar-shift reduction. Applied here to place the witness deliberately inside the residual simple-spectrum, invertible, irreducible core.
- **Campaign lead account03/B07**, preceding `MOC4-PARITY-SLACK-v1` plus newest completed `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`: the newest lead run leaves the pair-strict interior with the six-fiber/parity-slack obligation.
- **account04/B09**, common-`(P,R)` lift obstruction: its exact rational orthogonal matrix is perturbed by one tiny exact Givens rotation to enter the strict-compound interior.

## New exact identity

For `rho in S3`, let

`F_rho(K)=sum_i |K_i,rho(i)| - 2 m_rho(K)`

where `m_rho=0` on parity-good transversals and otherwise is the smallest selected `|K|`. Put

`M=max_rho(F_rho + x_rho/2)`, `g_rho=M-(F_rho+x_rho/2)>=0`, and

`S=<R,|K|>-<D,K>`.

For **every** Birkhoff decomposition `R=sum lambda_rho R_rho`, the exact SR support gap is

`M-(<D,K>+<R,X>/2) = S - 2 sum lambda_rho m_rho + sum lambda_rho g_rho`.

Thus the old existential parity-slack condition `2 sum lambda m <= S` is a valid sufficient gate, but it may fail while the actual `X`-dependent support gaps `g_rho` still rescue the correct inequality.

## Exact elimination of the Birkhoff existential

All `3x3` Birkhoff decompositions of fixed `R` form one line segment. With `t=lambda_123`,

- `lambda_123=t`
- `lambda_231=t+r23-r11`
- `lambda_312=t+r32-r11`
- `lambda_132=r11-t`
- `lambda_213=r33-t`
- `lambda_321=r22-t`

and

`L=max(0,r11-r23,r11-r32) <= t <= U=min(r11,r22,r33)`.

Hence the minimum parity penalty is exactly `min{M_K(L),M_K(U)}`. No LP solver or hidden optimization remains.

## Genuine source-valid generic counterexample to the parity-slack gate

Use the account04/B09 rational orthogonal witness `U0` and right-multiply by the exact column-(1,4) Givens rotation

`c=24999999/25000001`, `s=10000/25000001`.

Exact arithmetic verifies the resulting `U` is orthogonal, all 16 entries are nonzero, and all 18 designated complementary `2x2` minors are nonzero, so `|D_ij|<R_ij` everywhere.

Take `eta=1` and the exact simple nonzero spectra

`a=(-9/40-39i/20, -7/20-37i/40, -13/10+13i/40, 1/4-7i/10)`,

`b=(-1/40+11i/40, 13/40+17i/40, -23/40-21i/40, -59/40+33i/40)`.

The structured B07 coefficient matrices are derived exactly in the report/verifier. The best possible parity-slack decomposition still has

`2 M_min - S = 86403375469385788109173 / 9765625781250015625000000 > 0`

(about `0.00884770494`). Therefore **no** Birkhoff decomposition satisfies `MOC4-PARITY-SLACK-v1` on this generic true-unitary structured datum.

This is **not** an MOC4 counterexample. Direct exact enumeration of all 24 signed endpoint support values gives a unique maximizer and

`RHS(SR)-LHS(SR) = 125075523892079396068283817 / 156250012500000250000000000 > 0`

(about `0.80048328887`). The missing payment is exactly the structured `X`-dependent support-gap rescue.

## Next shared implication

Drop the now-refuted universal X-free parity-slack route. For the parity-penalty minimizing endpoint decomposition `lambda*`, attack

`MOC4-SUPPORT-GAP-RESCUE-v1:`

`sum_rho lambda*_rho g_rho >= 2 sum_rho lambda*_rho m_rho - S`.

When the right side is nonpositive, the old gate already proves the datum. The genuinely residual case is positive-deficit, and the actual structured `X` must pay it. The report proves this is the exact remaining six-state obligation and gives a generic witness where the rescue term is essential.

Recommended recipients: account03/B07 lead, account02/B08 assigned partner, account03/B20 integrator, account04/B09 structured-coefficient worker, account04/B07 SO(6) worker.

No benchmark material, keys, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, public posting, paid model/API calls, Codex, remote workflows, or permission changes were used.