SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B12, 2026-09-23T09:19:31Z.
attacking: frame-covariant routing of arbitrary signed eigenvalue replacements through nonaligned physical cores, plus arbitrary dense matrix tails.

# fleet01/B12 — frame-covariant diagonal-anchor routing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Additional eigenvalue control  
Status: **PROVED SUPPORTING STABILITY THEOREM + EXACT TARGET-CLASS FAMILY / FULL QFORM OPEN**  
Continuity: **not claimed** by this branch; the terminal localized-core input gives the required essential density bound.

## 1. Exact target and the first unpaid implication

The full target remains OPEN: for every `n`, independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal bound for the density of `X^T A X`, or give a valid counterexample. No Gaussianity, moment, compact-support, connected-support, log-concavity, identical-law, or post-rotation-independence assumption is used below.

The newest partner theorem `fleet02/B12` protects independent motion of `r` spectral parameters by `r+1` physical cores, but states the anisotropic diagonal-anchor version under the exact local-frame alignment `S_j=I_r`. The first useful missing implication is whether that alignment is genuine or merely a coordinate artifact of the deterministic Schur compiler. This run proves that it is a coordinate artifact: the theorem is naturally **frame covariant**. Each core may have its own orthogonal update frame; one must transport its Schur anchor into the common global spectral-parameter frame before applying the partner's coordinatewise separation argument.

This still does not extract such a protected core family from the bare global hypothesis `s_3(A)>=1`; that structural step remains open.

## 2. Completed sources actually used

Three completed inputs are applied at equations.

1. `fleet03/B12` matrix-parameter Schur gap:
   `yspennstate/math-open-problems@333dd6db61c9d18e88f9b8be5bae55c811d49b42`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260923T074544Z-qform-eigenvalue-r28/REPORT.md`.
   For a physical core `j`, its data satisfy

   `sigma_min(B_j+U_j Theta U_j^T)`
   ` >= ell(rho_j)^2 min{mu_j, f_j sigma_min(K_j+S_j Theta S_j^T)}`,          (2.1)

   where `S_j` is an `r x r` orthogonal matrix.

2. Designated partner `fleet02/B12`, `QFORM-ALIGNED-DIAGONAL-RPLUS1-ANCHOR-STABILITY-v1`:
   `yspennstate/math-open-problems@09d93ccc40876d6dc6dd8bd0dff62769b4a75ea8`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260923T085819Z-fleet02-B12-auto11/REPORT.md`.
   Its exact combinatorial step is: for diagonal `Theta=diag(tau_1,...,tau_r)`, if the `r+1` diagonal anchor values are pairwise `Delta`-separated in every column, then each parameter coordinate can make at most one core bad, so one core remains uniformly nonresonant in all `r` coordinates.

3. Newest-Claude localized physical-triple bound:
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.
   If an ORIGINAL-coordinate principal `3x3` block has all three eigenvalues of modulus at least `c>0`, then after conditioning on all other original coordinates,

   `||p_(X^T A X)||_infinity <= 6 sqrt(pi)/c`,                              (2.2)

   uniformly over the affine terms created by conditioning.

No result is transferred through spectral-coordinate independence.

## 3. Exact frame-covariance identity

The fleet03/B12 construction gives an orthogonal matrix `S_j`. Define the **parameter-frame Schur anchor**

`Khat_j := S_j^T K_j S_j`.                                                   (3.1)

Then, for every symmetric parameter `Theta`,

`K_j+S_j Theta S_j^T`
` = S_j (Khat_j+Theta) S_j^T`.                                               (3.2)

Because `S_j` is orthogonal,

`sigma_min(K_j+S_j Theta S_j^T)`
` = sigma_min(Khat_j+Theta)`.                                                (3.3)

This exact identity is the new compiler step. It says that the local normalized frame `S_j` never needs to agree between different physical cores. The object that must be compared across cores is `Khat_j`, not `K_j` itself.

## 4. New theorem: frame-covariant `r+1` routing

### Theorem — `QFORM-FRAME-COVARIANT-DIAGONAL-ANCHOR-ROUTING-v1`

Fix `r>=1` and `r+1` ORIGINAL-coordinate physical cores `I_0,...,I_r` satisfying the completed matrix-parameter inequality (2.1). On each core define `Khat_j` by (3.1). Assume

`Khat_j = D_j + E_j`,

`D_j = diag(c_{j1},...,c_{jr})`,

`||E_j||_op <= eps`,                                                         (4.1)

and for every spectral parameter coordinate `k`,

`|c_{jk}-c_{lk}| >= Delta_k` for all `j!=l`.                                 (4.2)

Let

`Delta = min_k Delta_k`, and assume `eps<Delta/2`.                            (4.3)

Then for every diagonal spectral update

`Theta=diag(tau_1,...,tau_r)`, with arbitrary real `tau_k`,                   (4.4)

there exists a core `j_*` such that

`sigma_min(Khat_j_*+Theta) >= Delta/2-eps`.                                  (4.5)

Consequently, with

`gamma_* = min_j ell(rho_j)^2 min{mu_j, f_j(Delta/2-eps)},                   (4.6)

one has

`max_j sigma_min(B_j+U_j Theta U_j^T) >= gamma_*`                            (4.7)

for every choice of the `tau_k`, with no sign or magnitude restriction.

More generally, let `H=H^T` be arbitrary and let `T=T^T` satisfy `||T||_op<=delta`. Define

`eta=max_j ||H[I_j,I_j]||_op`.                                               (4.8)

If `eta+delta<gamma_*`, then for

`A=A_0+V Theta V^T+H+T`                                                      (4.9)

at least one actual final physical core obeys

`sigma_min(A[I_j,I_j]) >= gamma_*-eta-delta`.                               (4.10)

If `r=2` and the protected cores are triples, then by (2.2)

`||p_(X^T A X)||_infinity`
` <= 6 sqrt(pi)/(gamma_*-eta-delta)`.                                        (4.11)

### Proof

For each parameter coordinate `k`, call core `j` bad if

`|c_{jk}+tau_k|<Delta_k/2`.

By (4.2), two distinct cores cannot both be bad for the same coordinate. Thus each of the `r` parameter coordinates rules out at most one core. There are `r+1` cores, so choose `j_*` outside the union of all bad-core sets. For this core,

`min_k |c_{j_*k}+tau_k| >= min_k Delta_k/2 = Delta/2`,

hence

`sigma_min(D_j_*+Theta)>=Delta/2`.

Weyl's singular-value inequality and (4.1) give (4.5). By the exact covariance (3.3),

`sigma_min(K_j_*+S_j_* Theta S_j_*^T)>=Delta/2-eps`.

Insert this actual inequality into the completed fleet03/B12 Schur bound (2.1). This gives (4.7) and (4.6). Principal compression cannot increase operator norm, so adding `H+T` changes the selected physical block by at most `eta+delta`; another Weyl inequality gives (4.10). When the cores are original-coordinate triples, condition on every coordinate outside the selected triple. The remaining three variables are still independent cap-one variables and all outside couplings become affine terms. Apply the source-pinned localized theorem (2.2), proving (4.11). QED.

## 5. What this adds to the designated partner theorem

The partner theorem assumed `S_j=I_r` and required `K_j` itself to be approximately diagonal. The present result removes that exact-frame alignment assumption. The correct invariant condition is instead that

`S_j^T K_j S_j`

be approximately diagonal in the **common global spectral-parameter basis**. The local `S_j` may be completely different orthogonal matrices on different physical cores.

This is not a variable rotation. The independent random coordinates are never transformed. Equation (3.2) is only a deterministic matrix identity inside the Schur compiler.

## 6. Exact target-class family with genuinely nonaligned local frames

This section applies the designated partner result to an actual inequality and shows that the extension is non-vacuous.

Start from the exact nine-dimensional target-class family in fleet02/B12 Section 5. Its three physical triples are

`I_0={1,2,3}`, `I_1={4,5,6}`, `I_2={7,8,9}`.                               (6.1)

The baseline has two orthonormal eigenvectors

`v_1=(e_1+e_4+e_7)/sqrt(3)`,
`v_2=(e_2+e_5+e_8)/sqrt(3)`                                                 (6.2)

with eigenvalue one, and for arbitrary `Theta=diag(tau_1,tau_2)` its three actual principal blocks are

`diag(-2+tau_1/3, -2+tau_2/3, 4)`,
`diag(    tau_1/3,  2+tau_2/3, 4)`,
`diag(2+ tau_1/3,      tau_2/3, 4)`.                                        (6.3)

The partner proved the actual inequality

`max_j sigma_min(A_tau^0[I_j,I_j]) >= 1`                                    (6.4)

for every real `tau_1,tau_2`.

Now choose three **different** orthogonal `2x2` matrices, for example

`R_0=I_2`,

`R_1=[[0,-1],[1,0]]`,

`R_2=(1/sqrt(2))*[[1,-1],[1,1]]`,                                           (6.5)

and let `O_j=diag(R_j,1)` on physical triple `I_j`. Put

`O=O_0 direct_sum O_1 direct_sum O_2`,

`A_0 = O A_0^0 O^T`,

`w_k=O v_k`, `k=1,2`.                                                       (6.6)

Then `w_1,w_2` remain orthonormal eigenvectors of `A_0` with eigenvalue one. Replacing those two eigenvalues independently by arbitrary real amounts gives

`A_tau=A_0+tau_1 w_1 w_1^T+tau_2 w_2 w_2^T`
`     =O(A_0^0+tau_1 v_1v_1^T+tau_2 v_2v_2^T)O^T`.                          (6.7)

Because `O` is block diagonal in the ORIGINAL physical triples,

`A_tau[I_j,I_j]=O_j A_tau^0[I_j,I_j] O_j^T`.                               (6.8)

Therefore the completed partner inequality (6.4) applies at the actual matrix level:

`max_j sigma_min(A_tau[I_j,I_j])`
` = max_j sigma_min(A_tau^0[I_j,I_j])`
` >=1`.                                                                      (6.9)

This is already a direct application of the designated partner result to a new exact family.

The local update frames are genuinely nonaligned. On core `j`,

`U_j=(1/sqrt(3))*[[R_j],[0 0]]`,

so the matrix-parameter compiler has

`F_j=(1/3)I_2`, `f_j=1/3`, `rho_j=0`, `mu_j=4`, `S_j=R_j`.                  (6.10)

The physical active Schur anchors satisfy

`K_j=R_j D_j R_j^T`,                                                        (6.11)

where

`D_0=diag(-6,-6)`,
`D_1=diag(0,6)`,
`D_2=diag(6,0)`.                                                            (6.12)

Hence

`S_j^T K_j S_j=D_j`,                                                        (6.13)

exactly the new frame-covariant hypothesis. Here `Delta=6`, `eps=0`, so (4.6) gives

`gamma_*=min{4,(1/3)*3}=1`,                                                 (6.14)

recovering the actual partner inequality (6.9) even though `S_0,S_1,S_2` are different.

Now add an **arbitrary full symmetric dense tail** `T` with

`||T||_op<=1/4`.                                                            (6.15)

No sign, rank, or separability condition is imposed on `T`. Principal-compression Weyl gives, for one of the three actual final triples,

`sigma_min((A_tau+T)[I_j,I_j])>=3/4`.                                       (6.16)

The localized physical-triple theorem therefore yields

`||p_(X^T(A_tau+T)X)||_infinity`
` <= 6 sqrt(pi)/(3/4)`
` = 8 sqrt(pi)`
` = 14.179630807244127... .`                                                (6.17)

This is uniform over every `tau_1,tau_2 in R`, every dense tail satisfying (6.15), and every independent cap-one product law.

### Exact target spectral check

The block-diagonal physical twist `O` is globally orthogonal, so the spectrum before the dense tail is exactly the partner spectrum:

`{1+tau_1,1+tau_2,4,4,4,-1/2-2sqrt(3) (twice),-1/2+2sqrt(3) (twice)}`.       (6.18)

Thus `s_3(A_tau)>=4` for every `tau_1,tau_2`. Weyl for (6.15) gives

`s_3(A_tau+T)>=4-1/4=15/4>1`.                                               (6.19)

Every matrix in this family therefore lies inside the exact QFORM target class.

Notice again that no probabilistic rotation has been made: `A_tau` is simply a concrete rotated matrix relative to the fixed original independent coordinates.

## 7. Why the dense-tail step is valid

The dense matrix tail is never interpreted as a small random variable. A small matrix norm does not imply `X^T T X` is uniformly small for arbitrary unbounded product inputs. The only use of `||T||_op` is the deterministic principal-block inequality (6.16), after which the full final quadratic form is handled by conditioning on ORIGINAL coordinates and applying (2.2).

## 8. Remaining full-target gap

This theorem removes a genuine artificial restriction from the independent-eigenvalue-replacement compiler: local update frames need not align. The remaining hypothesis is geometric, not coordinate bookkeeping. One still needs, from only `s_3(A)>=1`, to force either

1. `r+1` physical cores whose **parameter-frame anchors** `S_j^T K_j S_j` have a quantitative coordinatewise separated diagonal structure; or
2. one of the already-paid fifth-/three-volume, ridge, grouped-bank/hub, physical-pair/triple, half-Riesz scalar-Schur, or other product-preserving exits.

The theorem therefore advances additional-eigenvalue control but does not solve or disprove the unrestricted conjecture.

## 9. Status

- Supporting frame-covariant stability theorem: **PROVED**.
- Exact target-class nonaligned-frame family: **PROVED**.
- Essential density bound in this scope: **PROVED**.
- Continuity in this branch: **NOT CLAIMED**.
- Full universal QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Independent end-to-end review of this new theorem: **PENDING**.
