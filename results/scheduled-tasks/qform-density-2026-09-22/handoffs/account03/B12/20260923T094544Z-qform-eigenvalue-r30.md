SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T09:45:44Z.

attacking: rank-budget spectral-window shield: large low-rank coupling leakage costs protected-mode count, not magnitude.

# account03/B12 r30 handoff

Status: **PROVED_SUPPORTING_THEOREM / FULL_QFORM_OPEN / NOT_INDEPENDENTLY_REVIEWED**.

Fresh final control observed: brain main `e70dbfa64bf15bda1a238d715e3e4e3e1b432835`, OWNER CONTROL `2026-09-22.15`, programme revision `2026-09-22.5`; live correction inbox blob remained `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe` and no B12/account03 pause was present.

Canonical mathematics:
- repository: `yspennstate/math-open-problems`
- final bundle commit: `5d483a217c0a6133c2aec3780d9d0a24b4754984`
- report path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T094544Z-qform-eigenvalue-r30/REPORT.md`
- report blob: `4adebbe9e832acaec28e3652ed3c69ea5a79b0a3`
- erratum path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T094544Z-qform-eigenvalue-r30/ERRATUM.md`
- checker/result are in the same immutable run directory.

New theorem `QFORM-RANK-BUDGET-LEAKAGE-SHIELD-v1`: for an ACTUAL original-coordinate principal block `H=[[C,B],[B^T,D]]`, choose only for deterministic matrix algebra a reducing spectral projection `P` of `D`, set `Q=I-P`, and assume `D_P` has at least `j+2k` singular values >=`mu`. With `rho=||BP D_P^{-1}||op` and `ell(rho)=(sqrt(rho^2+4)-rho)/2`,

` s_j(H) >= mu*ell(rho)^2 - s_{k+1}(BQ).`

Thus the first `k` singular leakage directions into the unprotected spectral sector may have arbitrarily large magnitude. If `rank(BQ)<=k`, their cost is exactly zero; the entire complementary spectrum `D_Q` may be singular, tiny, huge, and of either sign.

Proof mechanism: apply account04/B12's exact complementary-Schur factorization to the block with `BQ` deleted, obtaining `j+2k` singular values >=`g=mu ell(rho)^2`; restore the best rank-k part of `BQ` as a symmetric update of rank <=`2k`, which can spend at most `2k` protected singular values; restore the residual by Weyl at cost exactly `s_{k+1}(BQ)`.

For `r` protected modes the optimal reserve count is `K=floor((r-3)/2)`, so after an arbitrary local dense tail `T` with `||T||op<=delta`,

` s3(H+T) >= g - s_{K+1}(BQ) - delta.`

If the actual physical core has size `m` and the right side is `gamma>0`, conditioning only on outside ORIGINAL coordinates and applying the finite-dimensional projected-gradient theorem yields

` ||p_Q||inf <= 2 sqrt(6 pi m)/gamma.`

All outside spectrum and couplings are arbitrary. This branch proves essential boundedness, not continuity.

Concrete family: a 12-coordinate core split `3+7+2` with `D_P=diag(2,-2,2,-2,2,-2,2)`, `BP=0`, arbitrary symmetric `C,D_Q`, and completely unbounded `3x2` matrix `BQ` has `s3(H)>=2` and hence

` ||p_Q||inf <= sqrt(72 pi)=15.039769647786...`.

Newest volume result applied at an actual inequality: if `r>=7`, `K=floor((r-3)/2)`, `g=mu ell(rho)^2`, and `epsilon=s_{K+1}(BQ)>=g/2`, then because the actual original-coordinate cross block `B` satisfies `BB^T >= BQ BQ^T`, one has `s3(B)>=g/2`. If one side also satisfies the exact diffuse gate `max diag(P_range(B))<=1/2`, the `q=1` fractional three-volume theorem gives the full ambient continuous `C_0` density bound

` ||p_Q||inf <= 3e/s3(B) <= 6e/g.`

If instead `epsilon<g/2`, the rank-budget shield gives `s3(H)>g/2`; on a bounded-size core `m<=M`, this gives `4 sqrt(6 pi M)/g`. Hence in that scoped diffuse/bounded-core regime:

` ||p_Q||inf <= max{4 sqrt(6 pi M),6e}/g.`

Partner actually applied: account04/B12 at `yspennstate/math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T081758Z-account04-B12-complementary-schur-shield-r4/REPORT.md`.

Newest Claude-derived result actually applied: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Finite checks: 10,000 random rank-budget instances and 5,000 auxiliary projection instances gave zero violations; these are consistency checks only, not proof evidence for the full conjecture.

A typographical display immediately before numbered equation (7.5) in `REPORT.md` is corrected by `ERRATUM.md`; numbered (7.5), all theorem statements, constants and deductions are unchanged.

Remaining gap: starting only from `s3(A)>=1`, force either a bounded original-coordinate core with enough protected reserve, a diffuse actual cross block, or an already-paid grouped-bank/hub/ridge/pair/rank-two mechanism. The complementary unpaid geometry is high-leverage and spread over too many original coordinates.

Continuity: proved on the volume branch only; unrestricted full target continuity remains open. Execution remains `WITHOUT_VERIFIED_BRAIN`.
