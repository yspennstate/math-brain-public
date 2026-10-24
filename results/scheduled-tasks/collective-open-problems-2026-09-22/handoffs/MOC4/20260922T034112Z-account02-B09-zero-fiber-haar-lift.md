# MOC4 handoff — account02/B09 zero-fiber Haar lift and P-weighted reserve

Run: `20260922T034112Z-account02-B09-MOC4-r14`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific artifacts in the private mathematical archive:
- `proofnet24/collective-MOC4/account02/B09/20260922T034112Z-account02-B09-MOC4-r14/REPORT.md`
  - creation commit `6a0065c802a066495e3130f94d45b61600cfd878`
  - blob `20a1ea240bb65b81b880cad265e4db5f225d2a8a`
- `proofnet24/collective-MOC4/account02/B09/20260922T034112Z-account02-B09-MOC4-r14/LEAD_SYNC_COROLLARY.md`
  - creation commit `4b903c22f7579a47d3f5bd97f1676799cd132665`
  - blob `942a9480d776068763885e181c19142c32bdbb22`

Latest complete lead version actually consumed and applied: account03/B07 `account03-B07-20260922T033411Z-d2a63b2a`, theorem `MOC4-V4-PAIR-GAP-CEILING-v1`, scientific commit `dcce2e52aee9c3fb338be4dd56acb02114ebfdde`, blob `28cbce0f0a6213c0760e0777a5baa5b0de12b31a`.

Named OTHER-account inputs also applied:
- account01/B07 `MOC4-CARTAN-HESSIAN-PACKING-v1`, shared commit `dabcb6098e8abcb960ebf4700ae1354d5e3e97a`.
- account03/B08 `MOC4-ONE-CYCLE-SU2-ELLIPSE-v1`, shared commit `afb708e6900d6eb53f12e96226add63f2d16654f`.
- account04/B08 `MOC4-PAIR-SPECIFIC-ENDPOINT-ROOF-v1`, shared commit `f6de93d3fe3b7a1af69b55e3b45f446f5b2e8770`.

## Exact new zero-face theorem

Relabel a zero-entry unitary so `u_00=0` and write

`U=[[0,r*],[c,V]]`,

with `r,c in C^3` unit. Choose isometries `X,Y:C^2->C^3` onto `r^perp,c^perp`. Every genuine unitary with this same first row and column is

`U(W)=[[0,r*],[c,Y W X*]]`, `W in U(2)`.

Put `R_j=|r_j|^2=P_{0j}`, `C_i=|c_i|^2=P_{i0}` for `i,j=1,2,3`.

Define a probability law on `S_4`: choose `i` with probability `C_i`, choose `j` independently with probability `R_j`, impose `pi(0)=i`, `pi(j)=0`, and choose uniformly one of the two bijections between the remaining rows/columns. Thus each compatible permutation has mass `C_i R_j/2`.

Then for Haar `W in U(2)`, simultaneously for every equal-cardinality `I,J`,

`E_W |det U(W)[I,J]|^2 = Pr_pi[pi(J)=I]`.

The proof is exact: `k=1` uses `E|y*Wx|^2=||x||^2||y||^2/2`; `k=2` is split by zero incidence, with the mixed case reduced to one Haar matrix coefficient; `k=3` follows by complementary-minor duality. Substitution in the exterior-power determinant expansion yields

`E_W det(D_a+U(W)D_bU(W)*) = sum_pi mu(pi) prod_t(a_t+b_{pi(t)})`.

Hence the whole residual zero-face Haar barycenter lies in the target convex hull. This is only an averaged common lift and therefore does not conflict with account03/B07's fixed-unitary common-lift counterexample.

## Exact quaternion polarization and boundary curvature

Modulo the irrelevant global phase, write the residual `U(2)` parameter as an `SU(2)` unit quaternion `q in S^3`. In every fixed real support direction,

`h(q)=q^T H q`

for a real symmetric `4 x 4` matrix `H`. The Haar-lift theorem gives `tr(H)/4<=M`, where `M` is the maximum endpoint support.

At a residual-fiber maximizer with violation gap `gamma=lambda_max(H)-M>0`, define

`Delta_mu=M-E_Haar h>=0`.

Then exactly

`-Tr Hess_{S^3} h = 8(gamma+Delta_mu) >= 8 gamma`.

If the target endpoint maximum is unique with second-endpoint gap `delta`, every Haar-lift atom is at most `1/2`, so `Delta_mu>=delta/2` and

`-Tr Hess_{S^3} h >= 8 gamma+4 delta`.

## Lead-sync P-weighted reserve

For each `i,j>0`, let `pi^+_{ij},pi^-_{ij}` be the two residual permutations and set

`z_ij=M-(H_{pi^+}+H_{pi^-})/2`.

The same-unitary Haar reserve is exactly

`Delta_mu=sum_{i,j>0} C_iR_j z_ij`.

Let

`g^R_tau=2M-max_sigma(H_sigma+H_{sigma o tau})`,
`g^L_tau=2M-max_sigma(H_sigma+H_{tau o sigma})`.

If `tau_j` swaps the two nonzero columns other than `j`, and `tau_i` the two nonzero rows other than `i`, then

`pi^-_{ij}=pi^+_{ij} o tau_j=tau_i o pi^+_{ij}`,

hence

`z_ij >= (1/2) max{g^L_{tau_i},g^R_{tau_j}}`.

Therefore

`Delta_mu >= (1/2) sum_{i,j>0} C_iR_j max{g^L_{tau_i},g^R_{tau_j}}`,

and so the exact zero-face Hessian payment strengthens to

`-Tr Hess_{S^3} h >= 8 gamma + 4 sum_{i,j>0} C_iR_j max{g^L_{tau_i},g^R_{tau_j}}`.

This is a genuine same-unitary `P=|U|^2` reserve, directly addressing the lead's current `MOC4-RESIDUAL-PR-RESERVE-v1` on the zero-face branch rather than replacing it by endpoint-only or arbitrary-bistochastic data.

## First unpaid implication

`MOC4-ZERO-FACE-PR-RESERVE-v2`: combine the exact P-weighted reserve above, the lead's V4/six-transposition ceiling, the zero-face rank-one corner factorization, and the quaternion Hessian to prove `lambda_max(H)<=M`. Equivalently derive a structured upper bound on the same residual-fiber Hessian that contradicts the displayed lower payment whenever `gamma>0`. Any failure must be an actual zero-entry true unitary with actual complex spectra and one common support direction.

No numerical computation was used as evidence for these results. Singular and repeated spectra are included because the determinant/minor identities are polynomial and use no spectral inverses or gap division.
