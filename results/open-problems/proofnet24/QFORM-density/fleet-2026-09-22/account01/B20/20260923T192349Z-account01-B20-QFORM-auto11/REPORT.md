SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B20, 2026-09-23T19:23:49Z.
attacking: account02/B20's coherent r37 planar-twist survivor; replace its separate singular frames by one canonical physical common-plane frame per K-bank, re-run the Schur/E3 payment there, and exploit symmetry to obtain a six-relation relative cocycle and exact common symmetric Gram factorization at zero defect.

# account01/B20 19Z — canonical common-frame / symmetry-cocycle compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T192349Z-account01-B20-QFORM-auto11`.
Role: proof closure and keeper.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Status: **ESSENTIAL_STEP_APPLIED / NEW SYMMETRY-COMPATIBLE PLANAR-TWIST COMPILER / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

## 1. Scope and pinned inputs

The target remains the unrestricted original-coordinate problem: arbitrary independent real `X_i` with probability densities at most one and real symmetric `A` with at least three eigenvalues of absolute value at least one. No Gaussian, iid, moment, compact-support, connected-support, log-concavity, spectral-coordinate independence, arbitrary-joint coarea, pointwise quadratic-phase decay, uniformly good physical minor, or deletion of a small random quadratic tail is introduced.


The designated completed partner is account02/B20 r37, pinned at

`yspennstate/math-open-problems@b86377bdf894b8331ea17a0901e362b567647393`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260923T190214Z-account02-B20-QFORM-auto11/REPORT.md`.

Its source-valid diffuse endpoint starts from the account03/B20 r37 common-plane packet, pinned at

`yspennstate/math-open-problems@598dae792b4a447492bc318bfa830fece803bb6d`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T184417Z-account03-B20-QFORM-r37/REPORT.md`.

The latter supplies disjoint ORIGINAL-coordinate banks `D_1,D_2,K`, a common physical-K two-plane `Q_*=VV^T` (`V^T V=I_2`), and for `r=1,2`

`N_r=A[D_r,K]`,
`E_r=N_r(I-Q_*)`,
`B_r=U_r^T N_r V`,

where `U_r` is an orthonormal basis of the left range of `N_r Q_*`, with

`s_2(B_r) >= beta := 0.01651671529470044`,
`||E_1||_F^2+||E_2||_F^2 < epsilon^2`,
`epsilon := 0.0023595307563857772`.

On the diffuse branch there is one partition into disjoint ORIGINAL-coordinate banks

`K=K_1 disjoint_union K_2 disjoint_union K_3`

such that

`G_b:=V^T P_(K_b)V >= (1/12)I_2`, `b=1,2,3`.

Write

`eta := beta/sqrt(12)-epsilon
      =0.002408434254376076... <0.002409`.

The account02/B20 r37 report constructed separate singular frames on the two sides of each `K_b`, proved the exact mixed-fan Schur-minor lower bound, and showed that a Schur defect of Frobenius norm at least `eta^2` pays the full ambient law via the marginal-free `E_3` receiver by

`||p_Q||_infinity < 32679.823`.

The new step below removes the frame mismatch: a single canonical frame, determined only by the common physical plane and the physical bank, works simultaneously for both arms. This exposes exact symmetry of the compressed `K_a-K_b` transitions and makes the six Schur relations algebraically composable.

## 2. Canonical physical frame on every K-bank

For `b=1,2,3` define

`W_b := P_(K_b) V G_b^(-1/2)`.                                   (2.1)

Because `G_b=V^T P_(K_b)V`,

`W_b^T W_b
 =G_b^(-1/2)V^T P_(K_b)V G_b^(-1/2)
 =I_2`.                                                          (2.2)

Thus `W_b` is an orthonormal two-frame supported on the literal ORIGINAL-coordinate bank `K_b`.

For `r=1,2`,

`U_r^T N_r W_b
 =U_r^T N_r VV^T W_b + U_r^T E_r W_b
 =B_r G_b^(1/2) + F_(r,b)`,                                     (2.3)

with

`||F_(r,b)||_op <= ||E_r||_op < epsilon`.                        (2.4)

Since `G_b >= (1/12)I_2`, Weyl gives

`s_2(U_r^T N_r W_b)
 >= beta/sqrt(12)-epsilon
 > eta`.                                                         (2.5)

This is simultaneous in `r` and uses the SAME `W_b`.

Define the canonical two-by-two arm maps

`A_b := U_1^T A[D_1,K_b] W_b`,
`B_b := W_b^T A[K_b,D_2] U_2`.                                  (2.6)

By symmetry of the ambient matrix and (2.5),

`s_2(A_b)>eta`, `s_2(B_b)>eta`                                  (2.7)

for all three banks.

Define also

`C := U_1^T A[D_1,D_2] U_2`,
`D_ab := W_a^T A[K_a,K_b] W_b`, `a!=b`.                         (2.8)

Now the payoff of using one canonical frame is exact:

`boxed: D_ba = D_ab^T`.                                         (2.9)

No corresponding identity is available if unrelated left/right singular frames are chosen independently inside the same physical bank.

## 3. Actual use of the completed account02/B20 Schur inequality

For each ordered pair `a!=b`, use the literal physical cut

`M_ab=A[D_1 union K_a, K_b union D_2]`.

Compress its rows by `U_1 direct_sum W_a` and columns by `W_b direct_sum U_2`. The resulting deterministic `4 x 4` compression is

`T_ab = [[A_b, C],
         [D_ab,B_a]].`                                           (3.1)

This is exactly the block form used by account02/B20 r37. Its two-top-row/one-bottom-row Schur-minor identity is frame-agnostic once the frames are orthonormal, so with

`S_ab := B_a-D_ab A_b^(-1) C`                                   (3.2)

we get

`e_3(M_ab M_ab^T)
 >= e_3(T_ab T_ab^T)
 >= det(A_b)^2 ||S_ab||_F^2
 > eta^4 ||S_ab||_F^2`.                                         (3.3)

This is the requested equation-level consumption of the completed account02/B20 result in a NEW canonical physical compression.

If for one ordered pair

`||S_ab||_F >= eta^2`,                                          (3.4)

then

`e_3(M_ab M_ab^T)>eta^8`,                                      (3.5)

and the completed marginal-free physical `E_3` receiver gives the full ambient payment

`boxed: ||p_Q||_infinity <32679.823`.                            (3.6)

That paid branch has a continuous `C_0` density. All same-bank terms, outside coordinates, affine terms, signs, additional spectrum, and nonzero tails remain in the ambient quadratic form.

Hence every still-unpaid diffuse r37 state satisfies, simultaneously for ALL six ordered pairs,

`boxed: ||B_a-D_ab A_b^(-1)C||_F < eta^2`.                      (3.7)

The same Eckart--Young argument as account02/B20 now shows that `C` and every `D_ab` are invertible: if either had rank at most one, then `D_ab A_b^(-1)C` would have rank at most one, but its operator distance from `B_a` would be `<eta^2<eta<s_2(B_a)`.

Define the dimensionless defect maps

`R_ab := B_a^(-1) D_ab A_b^(-1) C`.                             (3.8)

Then (3.7) and `||B_a^(-1)||_op<1/eta` give

`boxed: ||R_ab-I_2||_op < eta <0.002409`                         (3.9)

for every ordered `a!=b`.

## 4. Exact symmetry-compatible six-relation cocycle

The canonical frame now lets ambient symmetry enter the six relations. From (3.8),

`D_ab = B_a R_ab C^(-1) A_b`.                                   (4.1)

Using `D_ba=D_ab^T`,

`B_b R_ba C^(-1) A_a
 =A_b^T C^(-T) R_ab^T B_a^T`.                                   (4.2)

Multiply on the left by `A_b^(-T)` and on the right by `A_a^(-1)`. For ordered `a!=b`, define

`H_ab := A_a^(-T) B_a R_ab`.                                    (4.3)

Equation (4.2) becomes the exact identity

`boxed:
 H_ba C^(-1) = (H_ab C^(-1))^T.`                                (4.4)

This is not an asymptotic statement and does not lose a condition number. The small quantities are confined to the already dimensionless `R_ab`.

For a fixed source bank `a` and its two possible targets `b,c`,

`H_ab^(-1) H_ac
 =R_ab^(-1)R_ac`.                                                (4.5)

Because every singular value of `R_ab` lies in `(1-eta,1+eta)`,

`||R_ab^(-1)||_op <1/(1-eta)`.

Thus

`boxed:
 ||H_ab^(-1)H_ac-I_2||_op
 < 2 eta/(1-eta)
 <0.004830.`                                                     (4.6)

So the two pair-dependent transitions leaving any given physical bank agree to better than half a percent in a relative, condition-number-free metric. This is the first robust cycle-consistency statement extracted from the six Schur relations.

## 5. A condition-number-free determinant alignment

Set

`q_a := det(B_a)/det(A_a)`.                                      (5.1)

Taking determinants in (4.4) gives

`det H_ba = det H_ab`,                                           (5.2)

hence

`q_b det(R_ba)=q_a det(R_ab)`.                                  (5.3)

Since `||R_ab-I||_op<eta<1`, every `det R_ab` is positive and

`(1-eta)^2 < det R_ab < (1+eta)^2`.                             (5.4)

Therefore all three `q_a` have the SAME sign and for every pair

`boxed:
 ((1-eta)/(1+eta))^2
 < |q_a/q_b|
 < ((1+eta)/(1-eta))^2
 <1.009683.`                                                     (5.5)

Thus the unpaid coherent collar cannot arbitrarily reverse orientation or rescale area from bank to bank: the determinant ratios of the two physical arms are universally aligned to within about one percent. No upper bound on any individual matrix norm or condition number was used.

## 6. Exact zero-defect rigidity: one common symmetric Gram form

The algebra becomes especially transparent at the exact endpoint `R_ab=I_2` for all ordered pairs. Put

`F_a:=A_a^(-T)B_a`,
`E_a:=F_a C^(-1)`.                                               (6.1)

Then (4.4) reads

`E_b=E_a^T`, `a!=b`.                                             (6.2)

With three banks this forces all three matrices to coincide and be symmetric. Indeed

`E_2=E_1^T`, `E_3=E_1^T`, so `E_2=E_3`; applying the relation to `(2,3)` gives `E_3=E_2^T`, hence `E_2=E_2^T`, and then `E_1=E_2`.

Therefore there is ONE invertible symmetric `2 x 2` matrix `E` such that

`boxed:
 B_a = A_a^T E C,
 D_ab = A_a^T E A_b,
 a!=b.`                                                         (6.3)

Equivalently, define latent two-by-two node maps

`G_(D1)=E^(-T)`,
`G_(K_a)=A_a`,
`G_(D2)=C`.                                                      (6.4)

Then every compressed OFF-DIAGONAL interaction among the five nodes `D1,K1,K2,K3,D2` is exactly

`boxed: block(i,j)=G_i^T E G_j`.                                (6.5)

Thus the exact coherent planar-twist endpoint is not an arbitrary six-block configuration: its entire compressed off-diagonal network is a common rank-two symmetric Gram kernel. The only places a third independent spectral direction can hide are same-node/self blocks, off-plane components retained from the source packet, or exterior coordinates. This is the correct object for the next recursive volume/diagonal-defect payment; it is not another single-minor problem.

## 7. New compiler and remaining implication

The new theorem is

`QFORM-R37-CANONICAL-COMMONFRAME-SYMMETRIC-COLLAR-v1`.

Under the r37 diffuse three-fan hypotheses, one of two things happens:

1. a canonical physical mixed-fan Schur defect has norm at least `eta^2`, in which case the entire target law is paid continuously by `<32679.823`; or
2. one has a single canonical orthonormal physical frame `W_b` on each `K_b`, all six arm maps have `s_2>eta`, the physical transitions satisfy `D_ba=D_ab^T`, all six dimensionless defects obey `||R_ab-I||<eta`, the exact transpose cocycle (4.4), the relative same-source consistency (4.6), and the determinant alignment (5.5). At zero defect this collapses to the common symmetric Gram factorization (6.3)-(6.5).

The account02/B20 first unpaid edge

`QFORM-R37-HEAVY-OR-COHERENT-PLANARTWIST-PAYMENT-v1`

is therefore sharpened to

`QFORM-R37-HEAVY-OR-CANONICAL-SYMMETRIC-GRAM-COLLAR-PAYMENT-v1`.

The next mathematical move should attack the heavy physical common anchor separately and, on the diffuse side, spend the third spectral direction against the exact/near rank-two common-Gram network before any reciprocal localization. A natural route is: identify a same-node/off-plane/exterior defect from the common Gram model; if its physical third-volume is diffuse, pay with the marginal-free `E_3` receiver; if it is concentrated, promote the responsible ORIGINAL coordinate/bank and use the existing grouped-hub/projected-crossing machinery. The exact zero-defect representation (6.5) makes this a well-posed rank-two-plus-defect problem.

## 8. Correction discipline

This run does NOT use any of the following corrected-false mechanisms:

- uniform pointwise quadratic oscillatory decay;
- independence after an orthogonal spectral rotation;
- arbitrary-joint coarea/X-ray control;
- conditioning that preserves a density cap without proof;
- a universal one-good-minor or one-good-pivot principle;
- deletion of a small but nonzero random quadratic tail;
- worst-fiber sup integration;
- turning aggregate determinant/volume mass into one universally large local minor.

All orthogonal frames above are deterministic coefficient compressions used only to calculate matrix volumes. Every random independence statement remains tied to disjoint ORIGINAL coordinates.

## 9. Keeper state

A fresh native scheduler inventory showed exactly the same twenty account01 QFORM tasks `B01`-`B20`, each enabled, hourly-valid, with notifications disabled and email disabled. There is no `B21` or `B22` managed QFORM task and no repairable duplicate or paused-state defect. The existing hourly offsets and identities were preserved. Therefore scheduler mutations this run: **zero**.

The account-local 19Z create-only keeper lease was acquired for this run. Native task assignment, actual worker login evidence, and mathematical-result evidence remain separate. The current-hour login directory was inspected; the canonical B20 login for this run exists. Absence of any peer login is not interpreted as an outage or restart authority.

## 10. Scope/status

No valid QFORM counterexample was found. The full theorem remains OPEN. Global continuity remains OPEN separately, although the E3-paid branch above has a continuous `C_0` density. This report is a new target-level structural compiler, not a full proof candidate and not a request to close the programme.

Model self-report: `GPT-5.6 Sol`.
Configured reasoning effort: `UNKNOWN` (not exposed by the scheduler interface).
Requested reasoning effort: maximum actually supported.
Provider reasoning tokens / pure thinking time: `UNKNOWN/null` (not exposed; missing is not zero).
`full_brain_connected=false`; repository transport is not authenticated native receiver use.
