# account01/B16 FEI C — source-exact NET candidate and required obstruction test

**Execution:** `WITHOUT_VERIFIED_BRAIN`. **Classification:** `ESSENTIAL_STEP_APPLIED`. **Full FEI remains OPEN / NOT PROVED.**

Scientific source: `yspennstate/math-open-problems`, own root
`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260921T234240Z-net-candidate-two-defect/`.

Recovered original all-dimensional candidate at the fully source-backed cutoff
`d_*=n-floor(n/5)-1`:

`N_*(f)=Q_{d_*,<2}(f)-B_{d_*}(f) <= C_* J(f)`.

Exact compiler identity and terminal theorem:

`H_nat = kappa_2 J + N_* + R_{d_*}`,
`kappa_2=2/3+(1/2)log 3`, `|R_{d_*}|<3J/2`.

Therefore this single NET bound would imply full FEI with
`C_FEI=(C_*+3/2+kappa_2)/log 2`; the report writes every case and the minimizing-character gauge deduction explicitly.

Required account02 half-band two-point-defect family was evaluated exactly.  On an n-cube (`M=2^n`), its Fourier law is
`p0=(1-4/M)^2` plus `M/2-1` atoms of mass `16/M^2`, and `J=4n/M`.  Hence

`H_nat/J = 4 log2 + (2-8 log2)/n + O(2^-n)`.

At the carried half-band endpoint,

`(Q_{d_h,<2}-B_{d_h})/J -> 4 log2-kappa_2 = 1.55661591123906...`,

although the authentic already-positive live current satisfies `L_D/J -> infinity`.  Thus the original NET candidate survives this obstruction.  Any exact representation exposing that positive current must cancel it by a co-located **pre-square signed** term of the same leading scale; the aggregate high bank alone is `O(J)` and cannot be the later compensator.

Named peer results applied: account02/B18 `20260921T230348Z-oriented-relation-square-root/REPORT.md` blob `74a8144e588366e95d5c8b5ca8f0e384d8f1d6fd`; account02/B16 `20260921T225920Z-live-low-amplitude-parent-aggregation/REPORT.md` blob `4eb584133626148cdc89213fdaca906ae7b70ef8`.  Therefore the live unresolved object is specifically the Borel-scale variance/high/outside-live residual with the even-correlation cross ledger retained before squaring.

New rigorous obstruction: on the same family the exact self-phase packet obeys
`M Xi(s)=cos s-cos((1-4/M)s)+(M/2-1)[1-cos(4s/M)]`; at `s=c sqrt(M)`, `M Xi(s)->4c^2` while `J->0`.  So a pointwise source bound by `C J` is false.  The next C attack must be genuinely integrated/multiscale and preserve signed cancellation.

Checker blob `fb27a65cdf125629dc34f210dd03dab4360dec8f`; verification PASS. No scheduler, notification, email, permission, public-posting, remote-compute or unrelated-data action was taken.
