# Lead-sync corollary — P-weighted endpoint-gap reserve on a zero face

Run: `20260922T034112Z-account02-B09-MOC4-r14`  
Parent report: `REPORT.md`, creation commit `6a0065c802a066495e3130f94d45b61600cfd878`, blob `20a1ea240bb65b81b880cad265e4db5f225d2a8a`.

This note records the additional implication obtained after reading the campaign lead's newer complete scientific version account03/B07 `account03-B07-20260922T033411Z-d2a63b2a`, report commit `dcce2e52aee9c3fb338be4dd56acb02114ebfdde`, blob `28cbce0f0a6213c0760e0777a5baa5b0de12b31a`, theorem `MOC4-V4-PAIR-GAP-CEILING-v1`. It also uses the pair-specific endpoint gaps of account04/B08 `MOC4-PAIR-SPECIFIC-ENDPOINT-ROOF-v1`.

Outcome remains **ESSENTIAL_STEP_APPLIED**; parent MOC4 remains open.

## Setup

Use the zero-face notation of the parent report. After relabeling, `u_00=0`,

`U(W)=[[0,r*],[c,YWX*]]`,

with `R_j=|r_j|^2=P_{0j}` and `C_i=|c_i|^2=P_{i0}`, `i,j in {1,2,3}`.

For each ordered pair `(i,j)`, let `pi^+_{ij},pi^-_{ij}` be the two permutations satisfying

`pi(0)=i`, `pi(j)=0`,

with the two possible bijections between the remaining two nonzero columns and remaining two nonzero rows.

The exact residual-Haar lift from `MOC4-ZERO-FIBER-HAAR-LIFT-v1` gives each of these two permutations weight `C_iR_j/2`. Hence, for a fixed support direction with endpoint supports `H_pi` and maximum `M`, the residual-Haar support deficit is

`Delta_mu := M-E_W h(U(W))`

`= sum_{i,j>0} C_i R_j z_{ij}`,                                          (1)

where

`z_{ij}:=M-(H_{pi^+_{ij}}+H_{pi^-_{ij}})/2 >=0`.                         (2)

This is already an exact same-unitary `P`-dependent reserve: its weights are products of the first-column and first-row entries of the *same* unistochastic matrix `P=|U|^2`.

## Pair-gap lower bound for each reserve cell

For a transposition `tau`, define the right- and left-composition endpoint gaps

`g^R_tau := 2M-max_sigma(H_sigma+H_{sigma o tau})`,

`g^L_tau := 2M-max_sigma(H_sigma+H_{tau o sigma})`.                      (3)

For fixed `j`, let `tau_j` swap the two elements of `{1,2,3}\{j}`; for fixed `i`, let `tau_i` swap the two elements of `{1,2,3}\{i}`.

The two residual permutations differ simultaneously by

`pi^-_{ij}=pi^+_{ij} o tau_j = tau_i o pi^+_{ij}`                        (4)

(with the obvious extension of `tau_i,tau_j` fixing `0` and the distinguished index).

Therefore their two-endpoint average is bounded by both pair roofs, so

`z_{ij} >= (1/2) max{g^L_{tau_i}, g^R_{tau_j}}`.                         (5)

Substitution into (1) yields the exact source-compatible lower bound

`Delta_mu >= (1/2) sum_{i,j>0} C_iR_j max{g^L_{tau_i},g^R_{tau_j}}`.      (6)

In particular,

`Delta_mu >= (1/2) sum_i C_i g^L_{tau_i}`,                              (7)

`Delta_mu >= (1/2) sum_j R_j g^R_{tau_j}`.                              (8)

No bistochastic replacement is used: `C_i=P_{i0}` and `R_j=P_{0j}` come from the same true unitary that lies on the zero face.

## Boundary Hessian consequence

At a residual-fiber support maximizer with target violation gap `gamma>0`, the parent report proved the exact quaternion-Rayleigh identity

`-Tr Hess_{S^3} h = 8(gamma+Delta_mu)`.                                  (9)

Combining (6) and (9) gives

`-Tr Hess_{S^3} h`

`>= 8 gamma + 4 sum_{i,j>0} C_iR_j max{g^L_{tau_i},g^R_{tau_j}}`.         (10)

This is a genuine same-unitary, support-face-sensitive curvature payment on the zero-entry branch. It is complementary to the lead's global ceiling

`gamma <= (3d-Delta-G/2)/4`

because (10) injects the actual first row/column of `P` into the endpoint-gap reserve instead of using only endpoint-only aggregate quantities.

If the maximizing target endpoint is unique with second-endpoint gap `delta`, every relevant left/right transposition gap is at least `delta`; (6) immediately recovers

`Delta_mu >= delta/2`

and (10) becomes

`-Tr Hess_{S^3} h >= 8 gamma+4 delta`.

## Updated first missing implication

`MOC4-ZERO-FACE-PR-RESERVE-v2`:

Use the exact `P`-weighted reserve (6), the lead's `V4`/six-transposition ceiling, the zero-face rank-one corner factorization, and the exact quaternion Hessian to prove that a positive residual reserve cannot coexist with `lambda_max(H)>M`; equivalently derive a structured upper bound on the same zero-fiber Hessian that is strictly below (10) whenever `gamma>0`.

This is the zero-face specialization of the lead's current `MOC4-RESIDUAL-PR-RESERVE-v1`. A failure must be exhibited on an actual zero-entry unitary with actual spectra/support direction.
