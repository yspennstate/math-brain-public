# MOC4 fleet01/B09 — mixed-Schur positive-gap conditioning ceiling

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T074619Z-b09-moc4-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact state consumed

The source-exact target is the `4 x 4` Marcus-de Oliveira statement for complex normal pairs. The newest complete campaign-lead report consumed is fleet03/B07 run `20260922T064004Z-fleet03-B07-MOC4-r12`, theorem `MOC4-KERNEL-QUARTIC-RESERVE-v1`: after strict scalar Spin(4) sectors, a positive-gap support maximizer lies either on a genuine mixed-Schur pair-Hessian boundary (`MSQR`) or in the all-pair negative-definite branch (`NDI`).

The named OTHER-account result applied is fleet02/B07 `MOC4-SPIN4-PAIR-ROOF-RESERVE-IDENTITY-v1`, already source-bound in the preceding B09 run. For a complementary transposition pair `(tau,tau^c)` at a hypothetical support maximizer `h(U)=M+gamma`, `gamma>0`, it gives

`a=T-C=g_tau=2(gamma+r_tau)`, `b=T+C=g_{tau^c}=2(gamma+r_{tau^c})`,

with roof reserves `r_tau,r_{tau^c}>=0`. Hence

`Q:=T^2-C^2 = ab = 4(gamma+r_tau)(gamma+r_{tau^c})`.          (1)

I also apply the new exact same-account result fleet01/B07 `MOC4-EXACT-SPECTRAL-COVARIANCE-RECONSTRUCTION-v1` / `MOC4-EDGE-BUDGETED-SPECTRAL-PAYMENT-v1` from run `20260922T073048Z-fleet01-B07-MOC4-r12`. On a generic mixed-Schur row edge `e={alpha,gamma}`, if `G_alpha,G_gamma` are the exact positive spectral covariance inverses and

`lambda_alpha=lambda_min(G_alpha)`, `lambda_gamma=lambda_min(G_gamma)`,

then with block-row nonconformality energies `E_alpha,E_gamma`,

`E_alpha+E_gamma >= 4 Q * lambda_alpha lambda_gamma/(lambda_alpha+lambda_gamma)`.   (2)

## 2. New theorem — `MOC4-MIXED-SCHUR-GAP-CONDITIONING-CEILING-v1`

At every generic positive-gap global support maximizer having a mixed-Schur row edge `e={alpha,gamma}`, define

`h_e := lambda_alpha lambda_gamma/(lambda_alpha+lambda_gamma)>0`.

Then necessarily

`boxed( 8 h_e (gamma+r_tau)(gamma+r_{tau^c}) <= 1 )`,          (3)

and in particular

`boxed( gamma <= 1/sqrt(8 h_e) = sqrt((lambda_alpha+lambda_gamma)/(8 lambda_alpha lambda_gamma)) )`.   (4)

The identical statement holds for a mixed-Schur column edge using the column covariance metrics.

### Proof

For the exterior-square matrix `O=Lambda^2 U in SO(6)`, write its `2 x 2` blocks as `B_{alpha beta}` and

`R_{alpha beta}=(1/2)||B_{alpha beta}||_F^2`, `D_{alpha beta}=det B_{alpha beta}`.

For singular values `s_1,s_2` of a block,

`R=(s_1^2+s_2^2)/2 >= s_1 s_2 = |D|`.

Block-row orthogonality of `O` gives

`sum_beta ||B_{alpha beta}||_F^2=2`, hence `sum_beta R_{alpha beta}=1`.

Therefore the exact row nonconformality energy satisfies

`E_alpha = sum_beta (R_{alpha beta}^2-D_{alpha beta}^2)
         <= sum_beta R_{alpha beta}^2
         <= (sum_beta R_{alpha beta})^2 = 1`.                (5)

Likewise `E_gamma<=1`, so

`E_alpha+E_gamma<=2`.                                        (6)

Combining (2), (1), and (6) gives

`2 >= 4Q h_e = 16 h_e (gamma+r_tau)(gamma+r_{tau^c})`,

which is exactly (3). Since both reserves are nonnegative,

`(gamma+r_tau)(gamma+r_{tau^c}) >= gamma^2`,

and (4) follows. QED.

## 3. Why this matters to the live proof tree

This is a target-roof-to-spectral-conditioning bridge on the actual common-unitary mixed-Schur branch. A mixed-Schur positive-gap maximizer cannot have an arbitrarily large support violation once the exact spectral covariance metrics are well conditioned. The obstruction is quantitative and uses no bistochastic relaxation, determinant inverse, or coefficient representation.

Equivalently, any surviving large-gap counterexample on `MSQR` must drive at least one of the two exact covariance metrics toward the real-cross-ratio conditioning locus. This gives a concrete dichotomy for the campaign lead: either spectral covariance degenerates (a separately structured boundary) or the positive support gap is explicitly bounded by (4).

This does **not** prove MOC4 and does **not** eliminate `MSQR`; the bound can be positive. It is also not a new coefficient-lift counterexample. It is a new necessary condition that directly combines the assigned OTHER-account roof identity with the newest exact common-unitary covariance reconstruction.

## 4. First remaining implication

The live first missing implication is now sharpened as follows. On the generic mixed-Schur branch, combine the lead's quartic Lyapunov-Schmidt reserve and B09's previous roof-weighted cubic coercivity with (3), then show that the determinant-specific cubic/quartic tensors cannot satisfy all three payments simultaneously at `gamma>0`; alternatively produce a true-unitary source-valid witness that satisfies them and violates the target hull. The all-pair negative-definite `NDI` branch remains separate.

No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive data, public posting, paid model/API/Codex call, remote workflow, or permission bypass was used.
