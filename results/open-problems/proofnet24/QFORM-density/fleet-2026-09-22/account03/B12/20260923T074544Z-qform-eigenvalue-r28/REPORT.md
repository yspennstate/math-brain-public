SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T07:45:44Z.
attacking: arbitrary multirank signed spectral updates — replace the partner's scalar/common-shift resonance protection by a matrix-parameter theorem, identify the exact two-core obstruction, and give a valid r+1-core compiler.

# account03/B12 — matrix-parameter resonance and arbitrary multirank spectral-update stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T074544Z-qform-eigenvalue-r28`  
Assignment: additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREMS / ONE EXACT INTERMEDIATE-MECHANISM OBSTRUCTION / FULL QFORM OPEN**  
Continuity: **not claimed** by this run; only essential boundedness is compiled from the physical-core theorem.

## 1. Exact target and source discipline

The target remains: for every dimension, every independent real product law with one-dimensional density caps at most one, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal bound on the density of `X^T A X`, or give a valid counterexample.

No Gaussian, moment, compact-support, log-concavity, connected-support, spectral-coordinate-independence, or small-random-error hypothesis is introduced below. Every probabilistic use is on an actual ORIGINAL-coordinate physical core after conditioning on the other original coordinates.

Fresh brain control was read first at `math-research-brain@182a56de647964ce5fa829c747182d80c5c9d29d`, then refreshed before publication at `math-research-brain@c8f2bfe5014de52599c6773bcff734db727e3db4`; OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only. The live correction inbox was re-read at that final refresh.

The completed designated partner result used at an equation is:

`yspennstate/math-open-problems@d460b6cc1d557090dce30e824744c2dd3d335fb1`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T071518Z-account04-B12-multirank-resonance-r3/REPORT.md`.

Its scalar/common-shift theorem is used in Section 6 below, not merely cited.

## 2. Matrix-parameter Schur-gap lemma

Fix an ORIGINAL-coordinate physical core `I` of size `m>=r+1`. Let `B=B^T` be its baseline principal block and let `U` be an `m x r` full-column-rank matrix. Choose an orthonormal basis `W` for `range(U)` and an orthonormal complement `Z`. Write

`B11=W^T B W`, `B12=W^T B Z`, `D=Z^T B Z`.

Assume `D` is invertible. Put

`C=B11-B12 D^{-1} B12^T`,

`G=W^T U`,

`F=G G^T`,

`K=F^{-1/2} C F^{-1/2}`,

`rho=||B12 D^{-1}||_op`,

`mu=sigma_min(D)`,

`f=lambda_min(F)`,

and

`ell(rho)=(sqrt(rho^2+4)-rho)/2`.

Because `U` has full local rank, `G` is invertible and `F>0`. Define

`S=F^{-1/2}G`.

Then

`S S^T=F^{-1/2} G G^T F^{-1/2}=I_r`,

so the square matrix `S` is orthogonal.

Let `Theta=Theta^T` be an arbitrary `r x r` matrix. The active Schur block is

`C+G Theta G^T`

`=F^{1/2}(K+S Theta S^T)F^{1/2}`.                    (2.1)

The exact complementary-Schur/shear factorization used by account04/B12 is algebraic in the active Schur block, so it applies without requiring `Theta=tau I`. Therefore

`sigma_min(B+U Theta U^T)`

`>= ell(rho)^2 min{mu, sigma_min(C+G Theta G^T)}`

`>= ell(rho)^2 min{mu, f sigma_min(K+S Theta S^T)}.`   (2.2)

This is the basic matrix-level replacement for the scalar resonance formula.

Equivalently, since `S` is orthogonal,

`sigma_min(K+S Theta S^T)`

`=sigma_min(Theta+S^T K S)`.

Thus a physical core fails only when the arbitrary matrix parameter `Theta` approaches the translated singular-matrix variety

`R(K,S)={Theta in Sym_r: det(Theta+S^T K S)=0}`.      (2.3)

No random quadratic remainder has been bounded here; all estimates are deterministic matrix inequalities.

## 3. Exact obstruction: two resonance varieties always intersect for r>=2

A tempting but false extension of the partner's scalar theorem would be: use two physical cores whose full matrix-parameter resonance varieties have positive separation. For `r>=2` this separation cannot occur for the natural varieties (2.3).

### Lemma 3.1 — `QFORM-TWO-MATRIX-RESONANCE-SEPARATION-IMPOSSIBLE-v1`

Let `r>=2` and let `H1,H2` be arbitrary real symmetric `r x r` matrices. Define

`R_j={Theta in Sym_r: det(Theta+H_j)=0}`.

Then

`R_1 intersect R_2` is nonempty.                              (3.1)

Hence `dist_op(R_1,R_2)=0`.

### Proof

Let `D=H2-H1`. Since `D` is symmetric and `r>=2`, choose two orthonormal eigenvectors `u,v` of `D`. Then

`u^T D v=0`.                                                   (3.2)

We seek a symmetric `Theta` satisfying simultaneously

`Theta u=-H1 u`,

`Theta v=-H2 v`.                                               (3.3)

The only compatibility condition for prescribing a symmetric linear map on two basis vectors is

`v^T(-H1 u)=u^T(-H2 v)`.

Using symmetry of `H1,H2`, this is equivalent to

`u^T(H2-H1)v=0`,

which is exactly (3.2).

Extend `u,v` to an orthonormal basis. In that basis, prescribe the first two columns by (3.3), use the compatibility above for the `(1,2)` entry, set the corresponding first two rows by symmetry, and choose the remaining `(r-2)x(r-2)` block arbitrarily symmetric. This constructs a real symmetric `Theta` satisfying (3.3). Therefore

`(Theta+H1)u=0`,

`(Theta+H2)v=0`,

so both matrices are singular. QED.

### Meaning

The partner's two-core theorem is genuinely a **one-parameter/common-shift** theorem. When the `r` added directions are allowed to move with a fully arbitrary symmetric `r x r` parameter, two cores cannot protect them by positive resonance-set separation. This is a mechanism correction, not a counterexample to QFORM.

## 4. Valid replacement: r+1 isotropic Schur anchors protect an arbitrary rank-r update

The two-core obstruction suggests increasing the number of physical cores. There is a clean sharp result when their normalized active Schur blocks are isotropic scalars.

Consider `r+1` ORIGINAL-coordinate physical cores `I_0,...,I_r`. On core `j`, define the data from Section 2 and assume

`K_j=c_j I_r`                                                   (4.1)

for real scalars `c_j`, with

`|c_j-c_k|>=Delta>0` for `j!=k`.                              (4.2)

Define

`f_*=min_j lambda_min(F_j)`,

`mu_*=min_j sigma_min(D_j)`,

`ell_*=min_j ell(rho_j)`,

and

`gamma_*=ell_*^2 min{mu_*, f_* Delta/2}.`                     (4.3)

### Theorem 4.1 — `QFORM-RPLUS1-ISOTROPIC-ANCHOR-MATRIX-UPDATE-v1`

For every real symmetric `Theta in Sym_r`, at least one of the `r+1` actual physical cores satisfies

`sigma_min(B_j+U_j Theta U_j^T) >= gamma_*`.                   (4.4)

More generally, let `H=H^T` be arbitrary with no global norm restriction, and let `T=T^T` satisfy `||T||_op<=delta`. Put

`eta=max_j ||H[I_j,I_j]||_op`.

If

`eta+delta<gamma_*`,                                           (4.5)

then for

`A=A_0+V Theta V^T+H+T`,

where `U_j=V[I_j,:]`, at least one actual physical core has smallest singular value at least

`gamma_* - eta - delta`.                                      (4.6)

Consequently, if all cores have size at most `m`, the finite-dimensional physical-core theorem gives

`||p_(X^T A X)||_infinity`

`<= 2 sqrt(6 pi m)/(gamma_* - eta - delta).`                   (4.7)

If all cores are triples, the sharper three-coordinate theorem gives

`||p_(X^T A X)||_infinity`

`<= 6 sqrt(pi)/(gamma_* - eta - delta).`                       (4.8)

This holds for every independent cap-one product law. The eigenvalues of `Theta` may have arbitrary magnitudes and arbitrary signs, and `Theta` may have arbitrary off-diagonal mixing.

### Proof

Because `K_j=c_j I_r` and `S_j` is orthogonal,

`K_j+S_j Theta S_j^T`

`=S_j(c_j I_r+Theta)S_j^T`.

Hence

`sigma_min(K_j+S_j Theta S_j^T)`

`=min_{1<=k<=r}|c_j+lambda_k(Theta)|.`                         (4.9)

The open intervals `(c_j-Delta/2,c_j+Delta/2)` are pairwise disjoint. There are `r+1` such anchor intervals but only `r` numbers `-lambda_k(Theta)`. Therefore at least one anchor `c_j` lies at distance at least `Delta/2` from every `-lambda_k(Theta)`. For that `j`, (4.9) is at least `Delta/2`.

Insert this into (2.2):

`sigma_min(B_j+U_j Theta U_j^T)`

`>= ell_j^2 min{mu_j, f_j Delta/2}`

`>= gamma_*`.

Adding `H+T` changes that actual principal block by operator norm at most `eta+delta`, so Weyl's singular-value inequality gives (4.6). Condition on all original coordinates outside the selected core and apply the physical-core density theorem, yielding (4.7) or (4.8). QED.

## 5. Sharp anchor count inside the isotropic-anchor model

The `r+1` count is not an artifact of the proof.

If only `r` isotropic anchors `c_1,...,c_r` are available, take

`Theta=diag(-c_1,...,-c_r)`

in any orthonormal basis. Then for every anchor `j`, the matrix `c_j I_r+Theta` has a zero eigenvalue, so every one of the `r` protected cores can resonate simultaneously.

Thus within this isotropic-Schur model:

- `r` cores are insufficient for arbitrary `Theta`;
- `r+1` pairwise-separated anchors are sufficient by Theorem 4.1.

This is the correct multirank replacement for the partner's scalar two-core resonance separation in this geometry.

## 6. Direct application of the completed account04/B12 theorem: spectral-cluster compiler

The new theorem above handles arbitrary spectral spread under an `r+1`-anchor condition. The completed account04/B12 result yields a complementary two-core theorem when the arbitrary rank-`r` update is spectrally clustered.

Use the exact setup and `gamma_*` from account04/B12 Theorem 4.1 for the scalar/common-shift family `A_0+tau V V^T`. Now let `Theta=Theta^T` be arbitrary and define

`tau=(lambda_max(Theta)+lambda_min(Theta))/2`,

`omega=(lambda_max(Theta)-lambda_min(Theta))/2`.

Then

`Theta=tau I_r+E`, `||E||_op=omega`.                           (6.1)

Write

`u_*^2=max_{j=1,2} ||U_j||_op^2`.

On either partner core,

`||U_j E U_j^T||_op<=u_*^2 omega`.                            (6.2)

The partner theorem says that for the common-shift piece `tau I_r`, one of the two cores has gap at least `gamma_*`, uniformly for every real `tau`. Apply its perturbation clause at the actual inequality (6.2). If an additional arbitrary matrix `H` has local compression bound `eta`, and `||T||_op<=delta`, then whenever

`u_*^2 omega+eta+delta<gamma_*`,                               (6.3)

one core remains nonsingular with gap at least

`gamma_*-u_*^2 omega-eta-delta`.

Thus, for triple cores,

`||p_(X^T A X)||_infinity`

`<= 6 sqrt(pi)/(gamma_*-u_*^2 omega-eta-delta).`               (6.4)

For cores of size at most `m`, replace the numerator by `2 sqrt(6 pi m)`.

This is a genuine equation-level use of the completed account04/B12 theorem. It shows that an arbitrary collection of `r` added eigenvalues may share an arbitrarily large common signed displacement: the center `tau` costs **zero**; only half of their spectral diameter `omega` is charged, through actual physical leverage `u_*^2`.

No independence after spectral rotation and no convolution with `X^T(VEV^T)X` is used.

## 7. Explicit target-class example with an arbitrary 2x2 symmetric spectral update

The `r+1` theorem gives a concrete family inside the exact QFORM target.

Take nine original coordinates and three triples

`I_0={1,2,3}`, `I_1={4,5,6}`, `I_2={7,8,9}`.

Let the anchors be

`c_0=-2`, `c_1=0`, `c_2=2`, so `Delta=2`.

Define the baseline diagonal matrix

`A_0=diag(-2/3,-2/3,3, 0,0,3, 2/3,2/3,3)`.

Define two orthonormal global columns

`v_1=(e_1+e_4+e_7)/sqrt(3)`,

`v_2=(e_2+e_5+e_8)/sqrt(3)`,

and let `V=(v_1,v_2)`.

On every triple, `U_j=V[I_j,:]` has

`F_j=(1/3)I_2`, `f_j=1/3`, `rho_j=0`, `mu_j=3`,

and the chosen baseline gives

`K_j=c_j I_2`.

Therefore

`gamma_*=min{3,(1/3)(2/2)}=1/3`.                              (7.1)

Now let `Theta` be **any** real symmetric `2 x 2` matrix: its two eigenvalues may be arbitrarily large, small, positive, negative, or of opposite signs; its off-diagonal entry is unrestricted. Add any symmetric dense `T` with

`||T||_op<=1/12`.                                             (7.2)

Theorem 4.1 gives one actual triple with

`sigma_min((A_0+V Theta V^T+T)[I_j,I_j])`

`>=1/3-1/12=1/4`.                                             (7.3)

Hence

`||p_(X^T(A_0+V Theta V^T+T)X)||_infinity`

`<= 6 sqrt(pi)/(1/4)`

`=24 sqrt(pi)`

`=42.538892421732385...`.                                     (7.4)

The exact target spectral hypothesis is also preserved. Before adding `T`, the untouched coordinates `e_3,e_6,e_9` are eigenvectors with eigenvalue `3`; therefore after (7.2), Weyl gives at least three eigenvalues at least

`3-1/12=35/12>1`.                                             (7.5)

Thus (7.4) is a genuine target-class density bound for an arbitrary fully nonseparable rank-two signed update plus a dense tail.

## 8. Finite computations

`CHECK.py` and `CHECK_RESULT.json` in this run directory record sanity tests supplementing the exact proofs.

The checker performs:

1. 2,500 random tests, for `r=2,...,6`, of the constructive simultaneous-resonance proof in Lemma 3.1. Maximum kernel residuals were about `1.18e-14` and `7.01e-15`; no symbolic premise depends on these numerics.
2. 5,000 random arbitrary symmetric `Theta` tests in the explicit nine-dimensional family, with random dense perturbations of norm at most `1/12`. There were zero violations of the proved `1/3` pre-tail core gap, `1/4` post-tail core gap, or `35/12` target spectral threshold.
3. The exact final constant `24 sqrt(pi)=42.538892421732385...`.

These computations are consistency checks only, not Monte Carlo evidence for a universal theorem.

## 9. What this changes in the proof map

This run resolves two concrete questions about **additional arbitrary eigenvalues**.

First, the partner's scalar/common-shift resonance mechanism cannot be upgraded to fully arbitrary rank-`r` spectral motion merely by replacing two resonance point sets with two matrix-parameter resonance varieties: for `r>=2`, those varieties always intersect.

Second, there are two valid replacements:

- **clustered arbitrary multirank update:** two partner cores suffice if the update's spectral diameter is small enough; an arbitrary common signed displacement is completely free, with bound (6.4);
- **unrestricted arbitrary multirank update:** `r+1` isotropic normalized-Schur anchors with separated scalar anchors protect an arbitrary symmetric `Theta`, with no bound on its eigenvalue magnitudes, signs, or spectral spread.

The new theorem is matrix-level and dependence-safe. Extra curvature is paid only through deterministic physical-core compressions and singular values.

## 10. Remaining implication

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.**

The unresolved structural step is to derive from the bare assumption `s_3(A)>=1` one of:

1. an `r+1`-anchor certificate of the type in Theorem 4.1 for an offending multirank tail;
2. the partner's two-core scalar/cluster certificate;
3. a previously paid physical-core, cross-volume, grouped-bank, ridge, mixed-hub, or Schur exit.

Theorem 4.1 does **not** assert that every matrix supplies `r+1` isotropic anchors. Its value is that fully arbitrary large/small signed multirank spectral motion is no longer itself a probabilistic obstacle once such a finite original-coordinate certificate is present.

Continuity remains separate and is not established by this run's backward compiler.

## 11. Execution status

Repository transport and authenticated GitHub retrieval succeeded, but no authenticated native learned-memory receiver ingestion was established. Therefore this run remains `WITHOUT_VERIFIED_BRAIN` and `full_brain_connected=false`.

Model self-report: `GPT-5.6 Sol`.  
Configured reasoning level: `UNKNOWN`; standing owner preference is maximum actually supported.  
Provider reasoning-token and pure-thinking counters: not exposed.
