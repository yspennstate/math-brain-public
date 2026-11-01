# ProofNet24 P23 — Kernel Obstruction Audit / Post-Closure Hard-Edge Assist

**Run timestamp:** 2026-09-15 15:25:08 Asia/Jerusalem  
**Canonical transport correction:** complete replacement checkpoint for this run; the earlier same-run file at commit `a3d30af5771140bf4546e2423129d5cc4b6637c9` is preserved historically but is not the canonical checkpoint because exact readback did not match the locally generated report.  
**Track:** P23 — Gaussian-kernel obstruction audit  
**Scope:** P04 Target 3; after audit closure, assist unresolved kernel/RMT tracks. NO number theory.  
**Delivery:** GitHub-only. No email/Gmail action used.  
**Runtime model:** current system metadata exposes GPT-5.6 Sol. The requested GPT-6 / maximum-reasoning selector is not an exposed run control, so no GPT-6 switch or hidden agent is claimed.

## 0. Executive result

### 0.1 Original P04 Target 3 remains PROVED / AUDIT-CLOSED

For iid `X_i ~ Unif(S^{d-1})`, `n=2^d`, zero signal, independent Gaussian training noise of variance `sigma^2`, and fixed-bandwidth Gaussian kernel

`K_h(x,y) = exp(-||x-y||^2/(2h^2))`,

the expectation-level obstruction is audit-closed. The audited one-window theorem gives

`liminf_d E_training[ExcessRisk] / sigma^2 >= 5/36`.

The stronger P23 ten-window strengthening remains

`liminf_d E_training[ExcessRisk] / sigma^2 >= 3882594969529/12500000000000 = 0.31060759756232`.

No Target-3 dependency is reopened. The substantive work below follows the shared protocol and assists the unresolved P04 Target 4 / P20 quadratic hard edge.

### 0.2 New Target-4 theorem: ordinary DPP pairs are exactly blind to the Jordan defect

Let `V = Sym_d^0`, `m=(d-1)(d+2)/2`, and use the normalized pure degree-two harmonic feature map

`h(u) = c_d (u u^T - I/d)`,  `c_d = sqrt(d(d+2)/2)`.

Let `K(u,v)=<h(u),h(v)>_F`. For a rank-s coefficient projection P with Frobenius-orthonormal matrix basis `A_1,...,A_s`, define

`F_P(u)=||P h(u)||^2`,

`K_P(u,v)=<P h(u), P h(v)>`,

`C(P)=sum_a A_a^2`,

`Acal(P)=tr(C(P)^2)`,

`R(P)=sum_{a,b} tr(A_a A_b A_a A_b)`,

`delta(P)=Acal(P)-R(P)=(1/2) sum_{a,b} ||[A_a,A_b]||_F^2`,

`e(P)=Acal(P)-s^2/d`,

and

`beta_d = 8 d(d+2)/(d+4)^2`.

**Claim `P23-T4-DPP-PAIR-JORDAN-BLINDNESS-25` — PROVED.**

For `s>=2`, if U,V are two distinct labeled points from the rank-s projection DPP with kernel `K_P`, then pointwise for every fixed residual projection P,

`E[K(U,V) | P] = beta_d/[2s(s-1)] * [ delta(P) - 2s(s-1)/d ]`.

The symmetric/Jordan defect `e(P)` cancels exactly.

For the actual residual harmonic DPP, P20's exact commutator theorem gives

`E delta(P_s) = d s(s-1) / [2(m-1)]`,

hence

`E K(U,V) = theta_d := -4(d-2)(d+2)/[(d+4)(d^2+d-4)]`,

independently of residual rank `s>=2`.

Therefore ordinary labeled DPP pair overlap cannot control the open rank-two Jordan defect. This is a rigorous no-go theorem.

### 0.3 New positive representation: independent conditional replicas recover the defect exactly

Let U,V instead be conditionally independent replicas from the one-point conditional density `q_P(u)=F_P(u)/s`.

**Claim `P23-T4-REPLICA-JORDAN-OVERLAP-25` — PROVED.**

`E[K(U,V)|P] = beta_d e(P)/s^2`.

Thus for the actual residual rank-s law,

`e_s = s^2/beta_d * E_replica K(U,V)`.

The distinction is exact: ordinary DPP pairs retain only the commutator sector after repulsion subtraction, whereas two iid conditional replicas retain precisely the missing Jordan sector.

### 0.4 New rank-two signed cross-cofactor reduction

Take `m-2` iid original harmonic rows in a base matrix B and put `D=det(BB^T)`. For fresh iid sphere points u,v let `D_u` and `D_v` be the one-row extension Gram determinants. Let `M=(m)_{m-2}`. Under volume bias the residual rank-two base law has density `D/M`, and Schur complement gives `q_B(u)=D_u/(2D)`.

**Claim `P23-T4-REPLICA-COFACTOR-25` — PROVED.**

`e_2 = [1/(beta_d M)] E[ K(u,v) D_u D_v / D ]`.

Define the mixed cross-cofactor

`C_uv = det([[BB^T, B h(v)], [h(u)^T B^T, K(u,v)]]) = D h(u)^T P_2 h(v)`.

Let `D_uv` be the full Gram determinant after appending both u and v. The two-row Schur complement gives

`D_u D_v / D = D_uv + C_uv^2/D`.

Since `m-2+2=m`, volume bias by `D_uv` is the full rank-m projection DPP, and

`E[K(u,v) D_uv] = 2 M theta_d`.

Therefore:

**Claim `P23-T4-CROSS-COFACTOR-REDUCTION-25` — PROVED.**

`beta_d e_2 = 2 theta_d + (1/M) E[ K(u,v) C_uv^2 / D ]`.

Because `beta_d -> 8` and `theta_d=O(1/d)`, the open endpoint `e_2=O(1/d)` is equivalent to the signed coupled estimate

`(1/M) E[ K(u,v) C_uv^2 / D ] = O(1/d)`.

This preserves the dangerous inverse volume coupled to its cofactor numerator and is structurally aligned with the q=3/cofactor program.

---

## 1. Canonical evidence read

### 1.1 Shared protocol

Read on `master`:

- `README.md`, blob `9d18531dff608e0165fe4434614d8c9121903c4c`;
- `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, blob `a5773ae98d59ab7d6420f809452c3b20565c3379`.

These make GitHub the canonical archive, prohibit research email, require a new immutable complete report every run, and require exact source evidence.

### 1.2 Latest complete P23

`proofnet24/P23-kernel-obstruction/runs/2026-09-15/2026-09-15_14-27-25__run-report.md`

Creation commit `030608a299a3acd2e591b5e27455ef01078f5cf5`, blob `3516bbf553869ca60aa46b94ad5a3b2bb5928a8a`.

It records Target-3 audit closure and proves `P23-T4-JORDAN-INFO-TELESCOPE-NOGO-24`.

### 1.3 Latest complete P04

`proofnet24/P04-kernel-conjectures/runs/2026-09-15/2026-09-15_14-42-49__run-report.md`

Creation commit `a250cb01a6e4a66530c8293724f02526c8f0a663`, blob `8d626b482600d81c38529aa3c080be018f6bc194`.

Relevant current claims: `P04-T4-CHRISTOFFEL-JORDAN-SECTOR-36` and `P04-T4-HAAR-INTENSITY-SECTOR-SEPARATION-36`. Target 4 remains OPEN.

### 1.4 Kernel/RMT peer: P20

`proofnet24/P20-kernel-hard-edge/runs/2026-09-15/2026-09-15_14-28-25__run-report.md`

Creation commit `7fad083f015269e52c7b98f11b481c7cb89ab62a`, blob `7192350700c376e6eb818c576789bd010e872b79`.

Relevant claims: `P20-JORDAN-COVARIANCE-SANDWICH-43`, `P20-RANK2-JORDAN-EQUIVALENCE-43`, `P20-DYNAMIC-ORTHOBASIS-NOGO-43`, and `P20-RANK2-HODGE-QUOTIENT-43`.

### 1.5 Additional current peer state: P26

`proofnet24/P26-proof-audit-recovery/runs/2026-09-15/2026-09-15_15-13-51__run-report.md`

Creation commit `9ea9b4f87a50993e8ca97936146fb81df0aaf535`, blob `e8055aa9de3d515985221f852ce346577d631050`.

Its new `P26-T4-EXACT-024-SECTOR-04` and `P26-T4-CHI2-FLOOR-EQUIVALENCE-04` show that the live endpoint is suppression of the physical degree-two sector, not full L2 mixing.

---

## 2. Target-3 reduction retained

With harmonic blocks `K_s=lambda_s Phi_s Phi_s^T`, multiplicities `N_s`, `t_s=Tr(K^{-1}K_s)` and `q_s=Tr(K^{-1}K_sK^{-1})`, one has exactly

`V(X)/sigma^2 = sum_s lambda_s q_s`.

The addition theorem gives `||Phi_s||_F^2=nN_s`, and Hilbert-Schmidt Cauchy gives

`t_s^2 <= n N_s lambda_s q_s`.

For a finite deterministic window B, with `D_B=sum_B N_s` and `T_B=sum_B t_s`, weighted Cauchy gives

`V(X)/sigma^2 >= T_B^2/(nD_B)`.

This remains a reduction only. The expected-leverage estimate and the original Target-3 implication chain are already independently audited and closed. No high-probability theorem is substituted for the expectation target.

---

## 3. Primary-source Gaussian Mercer check

For fixed h, write `a=h^{-2}`. The exact spherical Gaussian-kernel Mercer eigenvalue is

`lambda_{d,s} = exp(-a) Gamma(d/2) (2/a)^(d/2-1) I_{s+d/2-1}(a)`.

Current NIST DLMF section 10.25.2 gives the positive series

`I_nu(z) = (z/2)^nu sum_{k>=0} (z^2/4)^k / [k! Gamma(nu+k+1)]`.

For positive a this yields the inherited adjacent-degree bound

`lambda_{d,s+1}/lambda_{d,s} <= a/(d+2s)`.

No asymptotic is reconstructed from an inaccessible source.

---

## 4. Polarized degree-two product projection

For `A in V`, put `f_A(u)=<h(u),A>_F=c_d u^T A u`. The normalization gives `int f_A f_B dmu = <A,B>_F`.

Let `M in V`. With a standard Gaussian `g=Ru`, `E R^6=d(d+2)(d+4)`, and Wick's formula for centered Gaussian quadratic forms gives

`E[(g^T A g)^2 (g^T M g)] = 8 tr(A^2 M)`.

Therefore

`<f_A^2,f_M> = gamma_d tr(A^2 M)`,

where

`gamma_d = 2 sqrt(2) sqrt(d(d+2))/(d+4)`.

Polarizing in A,B gives the pointwise degree-two projection formula

`Pi_2(f_A f_B)(u) = (gamma_d/2) < h(u), AB+BA - [2 tr(AB)/d] I >_F`.

This independently recovers the P04 Christoffel/Jordan constant. Squaring gives `beta_d=gamma_d^2=8d(d+2)/(d+4)^2`.

---

## 5. Triple-kernel identity

Define

`Tcal(P)=double_integral K(u,v) K_P(u,v)^2 dmu(u)dmu(v)`.

Expanding `K_P^2` and using that K is the projector kernel onto physical degree-two harmonics,

`Tcal(P)=sum_{a,b} ||Pi_2(f_a f_b)||_2^2`.

The polarized formula gives

`Tcal(P) = (beta_d/4) sum_{a,b} ||A_aA_b+A_bA_a - 2 delta_ab I/d||_F^2`.

For symmetric A,B,

`||AB+BA||_F^2 = 2 tr(A^2B^2)+2 tr(ABAB)`.

Hence:

**Claim `P23-T4-TRIPLE-KERNEL-JORDAN-25` — PROVED.**

`Tcal(P) = (beta_d/2) [ Acal(P)+R(P)-2s/d ]`.

---

## 6. Proof of ordinary-pair Jordan blindness

The labeled two-point density of a rank-s projection DPP is

`p_{2,P}(u,v) = [F_P(u)F_P(v)-K_P(u,v)^2]/[s(s-1)]`.

The first contribution satisfies

`double_integral K(u,v)F_P(u)F_P(v) = ||Pi_2 F_P||_2^2 = beta_d e(P)`.

Subtract the triple-kernel identity:

`E[K(U,V)|P] = [beta_d e(P)-Tcal(P)]/[s(s-1)]`.

Since `e(P)=Acal(P)-s^2/d`, exact simplification gives

`E[K(U,V)|P] = beta_d/[2s(s-1)] [Acal(P)-R(P)-2s(s-1)/d]`.

This is claim (B1). The entire `Acal`, hence Jordan, contribution cancels pointwise.

Averaging P20's exact commutator identity gives

`E K(U,V) = beta_d/2 [ d/(2(m-1)) - 2/d ]`

which simplifies to

`theta_d = -4(d-2)(d+2)/[(d+4)(d^2+d-4)]`.

A direct full-DPP check uses `T=(u dot v)^2` with moments

`ET=1/d`, `ET^2=3/[d(d+2)]`, `ET^3=15/[d(d+2)(d+4)]`,

and normalized kernel `rho=(dT-1)/(d-1)`. Exact expansion gives

`E rho^3 = 8(d-2)/[(d-1)^2(d+2)(d+4)]`,

which reproduces theta_d under the full projection-DPP pair density.

---

## 7. Proof of the replica-overlap theorem

For conditionally iid U,V from `q_P=F_P/s`,

`E[K(U,V)|P] = s^{-2} double_integral K F_P F_P = s^{-2} ||Pi_2 F_P||_2^2 = beta_d e(P)/s^2`.

This proves the replica theorem and its averaged form.

---

## 8. Cofactor derivation

Let the base contain `k=m-s` iid harmonic rows, with matrix B, `D=det(BB^T)`, and normalizer `M=(m)_k`. Under volume bias the base density is `D/M`. For a fresh u, Schur complement gives

`D_u = D h(u)^T P_s h(u) = D F_{P_s}(u)`

and hence `q_{P_s}(u)=D_u/(sD)`.

Two iid conditional replicas then give

`E_replica K(U,V) = [1/(s^2 M)] E[K(u,v) D_uD_v/D]`.

Compare with the replica-Jordan identity to obtain

`e_s = [1/(beta_d (m)_{m-s})] E[K(u,v) D_uD_v/D]`.

At s=2 define `C_uv=D h(u)^T P_2 h(v)` and the full two-row extension determinant `D_uv`. The 2-by-2 Schur complement gives

`D_uD_v/D = D_uv + C_uv^2/D`.

Because the base has m-2 rows, appending u,v yields m iid rows; volume bias by `D_uv` is the full projection DPP. Therefore

`E[K D_uv] = m! theta_d = 2 (m)_{m-2} theta_d`.

Substitution proves the cross-cofactor reduction.

---

## 9. Failed-route theorem and interpretation

Three objects must not be conflated:

1. **Ordinary DPP pair.** Its expected physical degree-two overlap is exactly a commutator observable; it is pointwise blind to `e(P)`.
2. **Two iid conditional replicas.** Their expected overlap is exactly proportional to `e(P)`.
3. **Cofactor correction.** At residual rank two, the difference between product-of-one-row cofactors and the actual two-row DPP determinant is precisely `C_uv^2/D`.

Therefore the small full-DPP pair marginal cannot by itself imply small `e_2`. This route is **DISPROVED structurally**, not merely shown difficult.

The open object is signed and inverse-sensitive. Taking absolute values inside

`E[K(u,v) C_uv^2/D]`

would destroy the centered-kernel cancellation and is not a valid solution strategy without a compensating theorem.

---

## 10. Exact regression checks

The analytic proof was checked against exact finite algebra.

- Symbolic simplification verifies the averaged pair constant theta_d.
- The Beta-moment expansion verifies the same theta_d directly from the full DPP pair marginal.
- For d=3 and the noncommuting plane
  `A=diag(1,-1,0)/sqrt(2)` and `B=(E12+E21)/sqrt(2)`, one has
  `Acal=2`, `R=0`, `delta=2`, `e=2/3`, `beta_3=120/49`, `Tcal=40/49`, and the pair formula gives `20/49`.
- For d=3 and the commuting plane
  `A=diag(1,-1,0)/sqrt(2)` and `B=diag(1,1,-2)/sqrt(6)`, one has
  `Acal=R=4/3`, `delta=0`, `e=0`, and the pair formula gives `-40/49`.

These are regression checks only; the exact identities above are the proof.

---

## 11. Independent peer audit

### `P23-AUDIT-P20-JORDAN-COVARIANCE-SANDWICH-25`

**Source:** `proofnet24/P20-kernel-hard-edge/runs/2026-09-15/2026-09-15_14-28-25__run-report.md`  
**Creation commit:** `7fad083f015269e52c7b98f11b481c7cb89ab62a`  
**Blob:** `7192350700c376e6eb818c576789bd010e872b79`  
**Claim:** `P20-JORDAN-COVARIANCE-SANDWICH-43`  
**Verdict:** **PASS**.

P20 claims

`a_s/s^2 <= b_s <= a_s/s - d(s-1)/[4(m-1)]`,

where `a_s=E tr(C_s^2)` and `b_s=E tr(N_s^4)`.

**Lower bound.** Conditional on `P_s`, the exact deletion mean is `E[N_s^2|P_s]=C_s/s`. Convexity of the Frobenius norm squared gives

`E[tr(N_s^4)|P_s] >= tr(C_s^2)/s^2`.

Averaging proves the lower bound.

**Upper bound.** For a Frobenius orthonormal basis `F_l` of all symmetric matrices, define self-adjoint Jordan multiplication operators `J_l` by

`<x,J_l y> = <F_l, [T(x)T(y)+T(y)T(x)]/2>_F`.

For a unit deletion coefficient v in `Ran(P_s)`, with `N=T(v)`, set `A_l=P_s J_l P_s`. Then

`<v,A_l v>^2 <= <v,A_l^2 v>`.

Using the exact conditional covariance `E[vv^T|P_s]=P_s/s`, summing over l and applying Parseval gives

`E[tr(N_s^4)|P_s] <= [Acal(P_s)+R(P_s)]/(2s)`.

Averaging and using P20's exact commutator identity

`E[Acal(P_s)-R(P_s)] = d s(s-1)/[2(m-1)]`

gives exactly

`b_s <= a_s/s - d(s-1)/[4(m-1)]`.

No iid-coordinate surrogate, false independence assumption, or bulk random-matrix theorem is used. The claim passes independently.

---

## 12. Cumulative ledger

### PROVED / AUDIT-CLOSED

Original P04 Target 3:

`liminf E_training[ExcessRisk]/sigma^2 >= 5/36`.

### PROVED — stronger P23 Target-3 strengthening

`liminf E_training[ExcessRisk]/sigma^2 >= 0.31060759756232`.

### PROVED — inherited Target-4 structure

- pure degree-two harmonic isometry;
- residual projection-DPP representation;
- exact exterior moments under volume sampling;
- exact commutator energy;
- Jordan reverse martingale;
- likelihood-information bridge;
- rank-two Jordan equivalence;
- P04 Christoffel/Jordan degree-two sector identity;
- P26 exact physical 0/2/4 sector decomposition;
- P20 rank-two Hodge quotient.

### PROVED — new this run

- `P23-T4-TRIPLE-KERNEL-JORDAN-25`;
- `P23-T4-DPP-PAIR-JORDAN-BLINDNESS-25`;
- `P23-T4-REPLICA-JORDAN-OVERLAP-25`;
- `P23-T4-REPLICA-COFACTOR-25`;
- `P23-T4-CROSS-COFACTOR-REDUCTION-25`;
- `P23-AUDIT-P20-JORDAN-COVARIANCE-SANDWICH-25`: PASS.

### DISPROVED / REJECTED

- **NEW:** ordinary labeled DPP pair correlations can control the missing rank-two Jordan energy — DISPROVED: the Jordan term cancels pointwise from the pair harmonic overlap.
- **NEW:** the small full-DPP pair marginal by itself implies small `e_2` — DISPROVED structurally: the pair observable sees only the commutator sector.
- Telescoping the Jordan recurrence with the scalar information bridge produces new contraction — DISPROVED previously; it reproduces the known identity.
- Full L2 mixing of the rank-two conditional intensity is the right target — DISPROVED by P04/P26; even coefficient-Haar has order-one total fluctuation.
- Static exterior design plus deletion first moments determine the endpoint — DISPROVED by P20's dynamic orthobasis surrogate.
- Bulk MP or ordinary local laws automatically imply the square hard edge — REJECTED.
- Adaptive harmonic coefficient coordinates may be replaced by iid coordinates — REJECTED.

### OPEN

Immediate angular endpoint:

`e_2 = O(1/d)`.

Equivalent forms include the P04 degree-two conditional-intensity sector, the P20 Hodge quotient, and the new signed cross-cofactor quotient

`(1/(m)_{m-2}) E[ K(u,v) C_uv^2/D ] = O(1/d)`.

Even after this angular endpoint, full P04 Target-4 hard-edge universality still requires the recorded radial/angular and ordinary-law transfer steps.

---

## 13. Next concrete attack

### Proposed `P23-T4-CROSS-COFACTOR-Q3-26`

For a base B of `m-2` iid harmonic rows and fresh iid u,v, prove

`| E[ K(u,v) C_uv^2/D ] | <= C (m)_{m-2}/d`

for an absolute C.

Do not move absolute values inside the expectation unless a compensating cancellation theorem is retained.

A plausible route is to expand the cross-cofactor square before inverse-volume estimates, introduce the minimum number of fresh harmonic replicas required to linearize the two cofactor factors, and keep the centered kernel `K(u,v)` coupled until after the Hodge/cofactor cancellation. This is closer to the P13/P14 q=3 architecture than the ordinary pair marginal and, unlike the latter, is exactly equivalent to the live Jordan defect.

---

## Bottom line

The original Gaussian-kernel Target 3 remains audit-closed; the stronger P23 constant remains `0.31060759756232 sigma^2`.

The new hard-edge result sharply separates ordinary DPP-pair geometry from replica geometry:

- actual DPP pair overlap sees the commutator sector and is exactly blind to the Jordan defect;
- two iid conditional replicas see exactly the Jordan defect.

At rank two the defect is equivalently the signed coupled cofactor quantity

`beta_d e_2 = 2 theta_d + (1/(m)_{m-2}) E[K(u,v) C_uv^2/D]`.

This rules out ordinary pair-marginal arguments and isolates a concrete signed cross-cofactor inverse-volume target for the next run.
