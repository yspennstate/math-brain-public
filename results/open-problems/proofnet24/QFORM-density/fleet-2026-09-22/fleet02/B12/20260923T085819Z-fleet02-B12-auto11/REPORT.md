SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-23T08:58:19Z.
attacking: aligned anisotropic anchor routing for two independently arbitrary eigenvalue replacements, stable under an arbitrary full-rank dense small tail.

# fleet02/B12 — aligned diagonal anchor routing under dense tails

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM + EXACT TARGET-CLASS FAMILY / FULL QFORM OPEN**  
Continuity: not claimed here; the output is an essential-density bound.

## 1. First unpaid implication

The missing global step is structural. From only `s_3(A)>=1`, current work does not force three ORIGINAL-coordinate physical triples whose normalized two-parameter update anchors are aligned and coordinatewise separated as in Theorem 3.1 below. Therefore the theorem does **not** solve QFORM. It says that once such an aligned three-anchor family is present, two eigenvalues may be changed independently by arbitrary real amounts, while an arbitrary dense small operator-norm tail is harmless at matrix level. A full proof must either extract this family or force one of the already-paid volume/hub/pair/Schur/local-core branches.

## 2. Sources actually used

Fresh owner control and all required QFORM state/corrections were read from the current brain main before publication. The full target remains OPEN.

Two completed mathematical inputs are used at equations:

1. **Designated partner fleet03/B12 matrix-parameter Schur gap**, source-pinned at
   `yspennstate/math-open-problems@333dd6db61c9d18e88f9b8be5bae55c811d49b42`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260923T074544Z-qform-eigenvalue-r28/REPORT.md`.
   Its equation (2.2) is recalled in Section 3.
2. **Newest-Claude localized physical-triple theorem (Theorem A)**, source-pinned at
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`:
   if an ORIGINAL-coordinate principal `3x3` block has all three eigenvalues of absolute value at least `c>0`, then, after conditioning on all other original coordinates,
   `||p_Q||_infinity <= 6 sqrt(pi)/c`, uniformly in the affine terms created by conditioning.

No post-rotation independence, moment, support, centering, identical-law, or log-concavity premise is used.

## 3. New deterministic theorem: anisotropic r+1 anchor routing for diagonal spectral motion

The partner's completed matrix-parameter lemma has the following setup on each physical core `I_j`. Let `B_j` be its baseline symmetric principal block and let `U_j` be the local restriction of the global rank-`r` update frame. The partner constructs quantities `K_j`, `S_j`, `f_j>0`, `mu_j>0`, `rho_j>=0` and

`ell(rho)=(sqrt(rho^2+4)-rho)/2`

such that for every symmetric parameter `Theta`,

`sigmamin(B_j+U_j Theta U_j^T)`
` >= ell(rho_j)^2 min{mu_j, f_j sigmamin(K_j+S_j Theta S_j^T)}.`      (3.1)

The new point is that for **independent eigenvalue replacement** the parameter is diagonal, so isotropic anchors are unnecessary.

### Theorem 3.1 — QFORM-ALIGNED-DIAGONAL-RPLUS1-ANCHOR-STABILITY-v1

Fix `r>=1` and `r+1` physical cores `I_0,...,I_r` satisfying (3.1). Assume their normalized update frames are aligned,

`S_j=I_r`,                                                        (3.2)

and write

`K_j = diag(c_{j1},...,c_{jr}) + E_j`,
`||E_j||op <= eps`,                                               (3.3)

where `eps<Delta/2`. Assume that for every update coordinate `k`, the `r+1` scalar anchors are pairwise separated:

`|c_{jk}-c_{lk}| >= Delta` for all `j!=l`.                        (3.4)

Then for every diagonal parameter

`Theta=diag(tau_1,...,tau_r)`,                                    (3.5)

there exists a core `j_*` such that

`sigmamin(K_j_*+Theta) >= Delta/2-eps`.                           (3.6)

Consequently, with

`f_* = min_j f_j`, `mu_* = min_j mu_j`, `ell_* = min_j ell(rho_j)`,

`gamma_* = ell_*^2 min{mu_*, f_*(Delta/2-eps)},`                  (3.7)

one has

`max_j sigmamin(B_j+U_j Theta U_j^T) >= gamma_*`                  (3.8)

for **every** choice of the `tau_k`, with no restriction on sign or magnitude.

Moreover let `H=H^T` be arbitrary globally and let `T=T^T` be an arbitrary dense perturbation with

`eta = max_j ||H[I_j,I_j]||op`,  `||T||op<=delta`.

If `eta+delta<gamma_*`, then for

`A=A_0+V Theta V^T+H+T`                                          (3.9)

at least one actual final physical core satisfies

`sigmamin(A[I_j,I_j]) >= gamma_*-eta-delta`.                     (3.10)

If `r=2` and the protected cores are triples, the required newest-Claude Theorem A gives

`||p_(X^T A X)||infinity <= 6 sqrt(pi)/(gamma_*-eta-delta)`       (3.11)

for every independent cap-one product law.

### Proof

Fix an update coordinate `k`. Define the bad core set

`B_k={j: |c_{jk}+tau_k|<Delta/2}`.

By (3.4), `B_k` has cardinality at most one: two bad anchors in the same column would be less than `Delta` apart. There are `r` coordinates, hence

`|union_k B_k| <= r`.

Among the `r+1` cores choose `j_*` outside this union. Then every diagonal entry of

`D_j_*+Theta`,  `D_j=diag(c_{j1},...,c_{jr})`,

has absolute value at least `Delta/2`, so

`sigmamin(D_j_*+Theta)>=Delta/2`.

Weyl's singular-value inequality and (3.3) give (3.6). Insert (3.6) into the completed partner inequality (3.1) to obtain (3.8). Principal compression cannot increase operator norm, so

`||(H+T)[I_j,I_j]||op <= eta+delta`.

A second Weyl inequality gives (3.10). For `r=2` and triple cores, condition on all original coordinates outside the selected triple. The retained three variables remain independent with densities at most one, while every external coupling becomes only an affine term. Apply the source-pinned localized Theorem A to obtain (3.11). QED.

### Why this is genuinely different from the partner's isotropic theorem

The partner's arbitrary-`Theta` theorem assumes `K_j=c_j I_r`; it tolerates arbitrary off-diagonal mixing in `Theta`. Theorem 3.1 instead restricts to diagonal `Theta`—exactly independent changes of a fixed eigenbasis—but allows the anchors themselves to be fully anisotropic diagonal matrices. Thus the two statements cover different geometry.

## 4. r+1 is sharp for this coordinatewise routing mechanism

The `r+1` count cannot be reduced to `r` under only columnwise separation, even with exact diagonal anchors and no dense tail.

Take `r` cores and set

`c_{jk}=j Delta` for `j=1,...,r` and every `k=1,...,r`.

Every column is pairwise `Delta`-separated. Choose

`Theta=diag(-Delta,-2Delta,...,-r Delta)`.

For core `j`, its `k=j` diagonal entry is

`c_{jj}+Theta_j=j Delta-j Delta=0`.

Hence every one of the `r` cores is singular simultaneously. This is the diagonal-parameter analogue of the designated partner's stronger obstruction that two full `Sym_r` resonance varieties must intersect for `r>=2`.

## 5. Exact target-class family with two arbitrary eigenvalue replacements

The theorem is non-vacuous inside the exact QFORM class. Work on nine ORIGINAL coordinates and define the three physical triples

`I_0={1,2,3}`, `I_1={4,5,6}`, `I_2={7,8,9}`.

On coordinate sets `{1,4,7}` and `{2,5,8}` put respectively

`C_1 = [[-2, 5/2, 1/2], [5/2, 0, -3/2], [1/2, -3/2, 2]]`,

`C_2 = [[-2, 1/2, 5/2], [1/2, 2, -3/2], [5/2, -3/2, 0]]`,             (5.1)

put the value `4` on coordinates `3,6,9`, and put all other baseline entries equal to zero. Call the resulting symmetric matrix `A_0`.

Both matrices in (5.1) have row sums one. Therefore

`v_1=(e_1+e_4+e_7)/sqrt(3)`,
`v_2=(e_2+e_5+e_8)/sqrt(3)`                                    (5.2)

are orthonormal eigenvectors of `A_0` with eigenvalue one. For arbitrary real `tau_1,tau_2`, set

`A_tau^0 = A_0 + tau_1 v_1 v_1^T + tau_2 v_2 v_2^T`.            (5.3)

Thus (5.3) **literally replaces two eigenvalues** `1,1` by `1+tau_1,1+tau_2`, independently, for arbitrary smaller/larger values and either sign.

The three physical blocks are exactly

`A_tau^0[I_0,I_0]=diag(-2+tau_1/3, -2+tau_2/3, 4)`,

`A_tau^0[I_1,I_1]=diag( tau_1/3,  2+tau_2/3, 4)`,

`A_tau^0[I_2,I_2]=diag( 2+tau_1/3,  tau_2/3, 4)`.                (5.4)

For the first update coordinate, the anchors are `(-2,0,2)`; for the second they are `(-2,2,0)`. In each column they are pairwise separated by two. For any `tau_1,tau_2`, at most one core has first entry of magnitude below one, and at most one core has second entry of magnitude below one. Hence one of the three cores satisfies

`sigmamin(A_tau^0[I_j,I_j])>=1`.                                (5.5)

This is also exactly the partner normalization: on each triple `U_j=(1/sqrt(3))[e_1,e_2]`, so `F_j=(1/3)I_2`, `rho_j=0`, `mu_j=4`, `S_j=I_2`, and the normalized anchors are

`K_0=diag(-6,-6)`, `K_1=diag(0,6)`, `K_2=diag(6,0)`.

Thus `Delta=6`, `eps=0`, `f_*=1/3`, `ell_*=1`, and (3.7) gives exactly

`gamma_*=min{4,(1/3)*3}=1`,                                    (5.6)

recovering (5.5) from the completed fleet03/B12 matrix-parameter inequality.

Now add **any** symmetric dense `9x9` matrix `T` with

`||T||op<=1/4`.                                                  (5.7)

It may have full rank and arbitrary sign pattern. From (5.5) and principal-compression Weyl,

`max_j sigmamin((A_tau^0+T)[I_j,I_j]) >= 3/4`.                  (5.8)

Applying the required e5f71d79... localized Theorem A to the selected actual final triple gives the concrete universal inequality

`||p_(X^T(A_tau^0+T)X)||infinity`
` <= 6 sqrt(pi)/(3/4)`
` = 8 sqrt(pi)`
` = 14.179630807244127...`.                                    (5.9)

This holds for every `tau_1,tau_2 in R`, every dense `T` satisfying (5.7), and every independent product source with one-dimensional density caps at most one.

### Exact target spectral check

Each `C_k` has spectrum

`{1, -1/2-2sqrt(3), -1/2+2sqrt(3)}`.

Hence

`spec(A_tau^0)`
`={1+tau_1,1+tau_2, 4,4,4, -1/2-2sqrt(3) (twice), -1/2+2sqrt(3) (twice)}`. (5.10)

In particular `s_3(A_tau^0)>=4` for every `tau_1,tau_2`. Another Weyl inequality gives

`s_3(A_tau^0+T)>=4-1/4=15/4>1`.                                (5.11)

Thus every matrix in (5.7) is genuinely inside the exact QFORM target class, uniformly even when either replaced eigenvalue tends to `+infinity` or `-infinity`.

## 6. Why the dense-tail step is legitimate

No step treats `X^T T X` as a small random perturbation. Such a statement is false uniformly on the allowed unbounded product laws: for `T=delta e_1e_1^T` and `X_1` uniform on `[R,R+1]`, one has `X^T T X>=delta R^2` almost surely. Here `||T||op` is used only through deterministic singular-value stability of the **actual final principal block** in (5.8), after which conditioning is performed in the original independent coordinates.

## 7. Sanity check

`CHECK.py` verifies the exact baseline eigendirections/local blocks and runs 10,000 deterministic-seed perturbation tests near all local resonances with arbitrary-rank symmetric tails of operator norm `1/4`. It records zero violations of either the proved `3/4` final-core floor or the proved `15/4` target spectral floor. This computation is only a sanity check; the theorem and family are analytic.

## 8. Remaining connection to the full conjecture

The new result pays a genuinely larger class of additional spectrum than the previous approximate-isotropic anchor theorem: two eigenvalues can move **independently** through all real values while the protecting normalized anchors are anisotropic. The price is alignment of the local update frames and coordinatewise anchor separation.

The next unpaid implication is therefore precise: in the no-pivot / delocalized survivor of the full QFORM problem, prove that either

- three ORIGINAL-coordinate triples provide an aligned two-parameter anchor table with universal columnwise separation and quantitative partner constants; or
- a fifth-volume / three-volume collective tail, hub, ridge, physical pair/triple, or scalar-Schur branch already gives a universal density bound.

The designated partner's resonance-intersection obstruction warns that arbitrary symmetric mixing of a two-parameter update cannot in general be protected by only two local cores. The present theorem shows that for the narrower but assignment-relevant operation of **independent eigenvalue replacement**, three anisotropic aligned anchors suffice and are worst-case sharp in count.

Full QFORM status after this run: **OPEN / NOT PROVED / NOT DISPROVED**.
