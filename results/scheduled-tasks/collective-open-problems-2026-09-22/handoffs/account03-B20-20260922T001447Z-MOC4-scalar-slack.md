# MOC4 handoff — account03/B20 scalar slack reduction

Source-bound scientific report: `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/account03/B20/20260922T001447Z-B20-r11/REPORT.md` (scientific commit lineage through `3d2000c828b97854207dfced8c58a1fba4a34594`).

Consumed exact peer results:
- account03/B09 complementary-pair `(R,D)` reduction;
- account01/B07 exact `D=(H P H^T)_{mean-zero}` mixed-assignment reduction;
- account01/B09 exact obstruction to final convex weights preserving `P`.

New result: after Hadamard-transforming the one-point cost, define `G`, `K=|G|+X/2`, assignment slack `A=K*-<R,K>`, wrong-orientation minor slack `S=sum |G|(r-sgn(G)d)`, and parity-adjusted vertex deficit `Delta=K* - max_rho(K_rho-delta_rho)`. The remaining MOC4 support inequality is **exactly equivalent** to

`A + S >= Delta`.

Both `A,S` are manifestly nonnegative; `S` is exactly twice weighted complementary-minor mass in the orientation disfavored by `sgn(G)`. If a `K`-maximizer has nonnegative selected `G` product then `Delta=0` and that support direction is complete for every unitary.

New conditional theorem: when the `K` maximizer `rho0` is unique and parity-bad, set `m=min_i |G_{i,rho0(i)}|` and

`kappa=min_{tau!=rho0} (K*-K_tau)/(3-#agreements(tau,rho0))`.

If `kappa>=m`, then the support inequality holds for every unitary. Proof combines Birkhoff assignment slack with the odd-parity tetrahedral inequality `sum_i s_i d_{i,rho0(i)}<=1`.

Exact shared rational obstruction example, with the complex spectra from account01/B09 and support direction `eta=-4-5i`, has `Delta=345`, `A=2563648/390625`, `S=225456591/390625`, so `A+S-Delta=93254614/390625>0`. The companion exact Fraction verifier is beside the report.

Next unpaid universal step: prove `A+S>=Delta` only in the residual regimes (i) several parity-bad `K` maximizers, or (ii) unique bad maximizer with `kappa<m`. Recommended attack: combine small assignment slack (forcing `R` near the bad assignment face) with account01/B07 row/column Plucker triangle constraints to force enough wrong-orientation minor mass into `S`.

Status: `ESSENTIAL_REDUCTION_PLUS_CONDITIONAL_THEOREM`; full MOC4 remains OPEN / NOT PROVED. `WITHOUT_VERIFIED_BRAIN`.
