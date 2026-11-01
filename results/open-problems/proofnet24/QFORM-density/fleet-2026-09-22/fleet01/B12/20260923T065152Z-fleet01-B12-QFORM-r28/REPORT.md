# fleet01/B12 — singular-core Schur rescue and two-core resonance separation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T065152Z-fleet01-B12-QFORM-r28`  
Assignment: Additional eigenvalue control  
Status: **PROVED_SUPPORTING_THEOREMS / FULL_QFORM_OPEN / NOT_INDEPENDENTLY_REVIEWED**  
Continuity: **not claimed**; all density conclusions below are essential-supremum bounds.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Question attacked and relation to the preceding runs

The full target remains: for independent real coordinates with one-dimensional density caps at most one, and a real symmetric matrix having at least three eigenvalues of absolute value at least one, prove a universal bound on the density of `Q=X^T A X`, or give a valid counterexample.

This run only attacks the assigned stability question: how arbitrary additional eigenvalues can be absorbed without rotating the independent random coordinates and without pretending that the resulting quadratic remainder is an independent convolution.

Runs r26-r27 controlled arbitrary signed spectral changes on an **invertible** physical core, using Woodbury. The first essential missing case is when the useful physical baseline block itself is singular or nearly singular. Woodbury with `B^{-1}` then cannot even be written, although a large spectral addition can make the physical block perfectly nonsingular. The mechanism below replaces `B^{-1}` by an exact Schur factorization relative to the update subspace. It gives:

1. a multirank theorem valid for singular baseline cores;
2. a magnitude threshold after which arbitrary signs are harmless;
3. an exact rank-one resonance formula even when the baseline core is singular;
4. a two-physical-core compiler: **two distinct local resonance points already give a uniform bound for every real added eigenvalue**, with no opposite-sign inverse-leverage hypothesis.


## 2. Sources actually consumed

### Designated partner source

The completed `fleet02/B12` source is

`yspennstate/math-open-problems@06fbcbb277d5db4f89dfc0c04b14174cc4315cc7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260923T045101Z-fleet02-B12-auto11/REPORT.md`.

Its Lemma 2.1 is the rank-one sign-routed Sherman-Morrison theorem and its Section 4 gives the exact family

`C=[[4,-3,-3,3],[-3,4,-3,3],[-3,-3,4,3],[3,3,3,-8]]`,

`v=(1,1,1,1)^T/2`,

with

`spec(C+tau vv^T)={1+tau,7,7,-11}`.

It proves that for every real `tau`, one of the original-coordinate triples `H_-={1,2,3}` and `H_+={2,3,4}` has all three singular values at least `2`, and hence after an arbitrary symmetric tail `E` with `||E||op<=1/4`,

`||p_(X^T(C+tau vv^T+E)X)||infinity <= 24 sqrt(pi)/7`.             (2.1)

I apply (2.1) again at an actual inequality in Section 8.

### Localized terminal theorem

The terminal density theorem is Theorem A of

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

If an ORIGINAL-coordinate physical `3 x 3` principal quadratic block has all eigenvalue magnitudes at least `c>0`, then after conditioning on all other original coordinates, arbitrary induced affine terms are allowed and

`||p_Q||infinity <= 6 sqrt(pi)/c`.                                 (2.2)

This is the only probabilistic input below. All new work is deterministic matrix algebra in original coordinates.

## 3. Exact complementary-Schur factorization for a singular baseline

Let `B=B^T` be a real `m x m` matrix; **B need not be invertible**. Let `U` be an `m x r` real matrix and let

`s = rank(U)`, `1 <= s < m`.

Let `W` be an `m x s` matrix with orthonormal columns spanning `range(U)`, and let `Z` be an `m x (m-s)` orthonormal complement. In the orthogonal basis `[W,Z]`, write

`B11 = W^T B W`,
`B12 = W^T B Z`,
`D   = Z^T B Z`.                                                    (3.1)

Assume only that the complementary block `D` is invertible. Put

`C = B11 - B12 D^{-1} B12^T`,                                     (3.2)

and for an arbitrary symmetric coefficient matrix `Theta`, put

`F = W^T U Theta U^T W`.                                           (3.3)

Then the updated physical block

`A = B + U Theta U^T`

has, in `[W,Z]` coordinates, the exact representation

`A_hat = [[B11+F, B12],[B12^T,D]]`.

Define

`R = B12 D^{-1}`, `S=C+F`.                                         (3.4)

Then

`boxed:
 A_hat = L diag(S,D) L^T,
 L=[[I_s,R],[0,I_{m-s}]].`                                         (3.5)

Indeed, the upper-left block of the right side is

`S + R D R^T = C+F+B12 D^{-1}B12^T = B11+F`,

and the off-diagonal block is `R D=B12`.

This identity is the core of the run. It avoids `B^{-1}` completely.

## 4. Exact shear loss and the singular-core stability theorem

For `rho>=0` define

`ell(rho) = (sqrt(rho^2+4)-rho)/2
          = 2/(sqrt(rho^2+4)+rho)`.                                (4.1)

### Lemma 4.1 — exact smallest singular value of the block shear

For

`L_R=[[I,R],[0,I]]`,

`boxed: sigma_min(L_R)=ell(||R||op).`                              (4.2)

Proof: take an SVD `R=P Sigma Q^T` and conjugate `L_R` by the corresponding block orthogonal matrices. It decomposes into `2 x 2` scalar shears `[[1,sigma_j],[0,1]]` plus identities. The smaller singular value of the scalar shear is `(sqrt(sigma_j^2+4)-sigma_j)/2`, decreasing in `sigma_j`. QED.

### Theorem 4.2 (`QFORM-SINGULAR-CORE-SCHUR-RESCUE-v1`)

Under the notation of Section 3, put

`mu  = sigma_min(D)>0`,
`eta = sigma_min(C+F)`,
`rho = ||B12 D^{-1}||op`.                                          (4.3)

If `eta>0`, then `B+U Theta U^T` is invertible and

`boxed:
 sigma_min(B+U Theta U^T)
 >= ell(rho)^2 min(mu,eta).`                                       (4.4)

#### Proof

By (3.5),

`A_hat = L diag(S,D)L^T`.

For any matrices, `sigma_min(PQR)>=sigma_min(P)sigma_min(Q)sigma_min(R)`. Therefore

`sigma_min(A_hat)
 >= sigma_min(L)^2 sigma_min(diag(S,D))
 = ell(rho)^2 min(eta,mu)`

by Lemma 4.1. Orthogonal change from physical coordinates to `[W,Z]` does not change singular values. QED.

This theorem permits the baseline `B` itself to be singular. Only its restriction to the orthogonal complement of the update footprint must be nonsingular, and the update must make the Schur block `C+F` nonsingular.

## 5. Arbitrary-sign sufficiently-large eigenvalues rescue a singular core

Assume now that `U` has full column rank `r=s`, so `G=U^T U` is positive definite. Since `range(U)=range(W)`, write

`U=W R_U`,

where `R_U=W^T U` is invertible and

`R_U^T R_U=G`.                                                      (5.1)

Thus

`F=R_U Theta R_U^T`.

For arbitrary symmetric invertible `Theta`, regardless of the signs of its eigenvalues,

`sigma_min(F)
 >= sigma_min(R_U)^2 sigma_min(Theta)
 = lambda_min(G) sigma_min(Theta).`                                (5.2)

Hence

`sigma_min(C+F)
 >= lambda_min(G) sigma_min(Theta)-||C||op`.                       (5.3)

### Corollary 5.1 (`QFORM-SINGULAR-CORE-LARGE-SPECTRUM-v1`)

If

`lambda_min(G) sigma_min(Theta) > ||C||op`,                        (5.4)

then

`boxed:
 sigma_min(B+U Theta U^T)
 >= ell(rho)^2
     min{ mu,
          lambda_min(G)sigma_min(Theta)-||C||op }.`                (5.5)

There is no sign hypothesis on `Theta`. Thus, once all active added eigenvalues are sufficiently large in absolute value, they may independently have either sign and arbitrarily larger magnitudes. This remains true even when the baseline physical block `B` is singular.

### Literal spectral-addition interpretation

If the columns of a global matrix `V` are orthonormal eigen-directions and `U=V[I,:]` is their restriction to the chosen physical core `I`, then the nonzero eigenvalues of the global added matrix `V Theta V^T` are exactly those of `Theta`. Condition (5.4) depends only on their absolute magnitudes and on the physical footprint Gram matrix `G=U^T U`; it does not rotate the random variables.

### Arbitrary-rank small dense tail

Let `T` be any symmetric matrix, of arbitrary rank and sign, with

`||T||op<=delta`.                                                   (5.6)

If the right side of (5.5) is `gamma>delta`, then by Weyl the actual physical block of

`B+U Theta U^T+T`

has smallest singular value at least `gamma-delta`. For a physical triple, (2.2) gives

`boxed:
 ||p_Q||infinity <= 6 sqrt(pi)/(gamma-delta).`                     (5.7)

The small tail is paid only at the deterministic matrix level. Nothing asserts that `X^T T X` is a small random variable.

## 6. Rank-one exact resonance theorem, including singular baselines

Let the update have rank one:

`A_tau=B+tau u u^T`, `u != 0`.                                     (6.1)

Set

`w=u/||u||`, `g=||u||^2`,

and let `Z` be an orthonormal basis of `w^perp`. Assume

`D=Z^T B Z`

is invertible. Define

`c=w^T B w - w^T B Z D^{-1} Z^T B w`,                             (6.2)

`mu=sigma_min(D)`,
`rho=||w^T B Z D^{-1}||_2`,
`r_*=-c/g`.                                                         (6.3)

Then `F=tau g` and the Schur block is the scalar

`S(tau)=c+tau g=g(tau-r_*)`.                                       (6.4)

Theorem 4.2 becomes

`boxed:
 sigma_min(B+tau uu^T)
 >= ell(rho)^2 min{mu, g|tau-r_*|}.`                               (6.5)

Moreover, from the block determinant formula,

`det(B+tau uu^T)=det(D) g(tau-r_*)`.                              (6.6)

Therefore:

* the physical block has **exactly one possible resonance**, `tau=r_*`;
* the statement remains valid when `B` is singular (`c=0` gives `r_*=0`);
* away from that one coefficient, the block is nonsingular;
* as `|tau|` grows, the local gap saturates at the complementary gap `mu` up to the fixed shear factor `ell(rho)^2`.

### Relation to Sherman-Morrison when B is invertible

If `B` is invertible, then necessarily `c!=0`. The block inverse gives

`u^T B^{-1}u = g/c`.                                               (6.7)

Hence the Sherman-Morrison resonance

`tau=-1/(u^T B^{-1}u)`

is exactly

`tau=-c/g=r_*`.                                                     (6.8)

Thus (6.5)-(6.8) strictly extend the partner's inverse-leverage picture through singular baseline cores.

## 7. Two-core resonance separation: a uniform all-real-eigenvalue compiler

The rank-one formula yields a useful new physical-core switch that does not require opposite signs of inverse leverage.

Let `I_1,I_2` be two ORIGINAL-coordinate physical triples for the same baseline matrix `A0` and global update direction `v`. For `j=1,2`, let

`B_j=A0[I_j,I_j]`, `u_j=v[I_j] !=0`,

and assume the complementary `2 x 2` block `D_j` on `u_j^perp` is invertible. Define `g_j,mu_j,rho_j,r_j` as in Section 6. Suppose

`r_1 != r_2`.                                                       (7.1)

Put

`g_*   = min(g_1,g_2)`,
`mu_*  = min(mu_1,mu_2)`,
`ell_* = min(ell(rho_1),ell(rho_2))`,
`Delta = |r_1-r_2|`.                                                (7.2)

### Theorem 7.1 (`QFORM-TWO-CORE-RESONANCE-SEPARATION-v1`)

For every real `tau`, at least one of the two physical triples satisfies

`boxed:
 sigma_min(B_j+tau u_j u_j^T)
 >= gamma_* := ell_*^2 min{mu_*, g_* Delta/2}.`                    (7.3)

#### Proof

For every real `tau`,

`max{|tau-r_1|,|tau-r_2|} >= |r_1-r_2|/2=Delta/2`.                (7.4)

Choose a core attaining the maximum. Then (6.5) gives

`sigma_min(B_j+tau u_j u_j^T)
 >= ell(rho_j)^2 min{mu_j,g_j|tau-r_j|}
 >= ell_*^2 min{mu_*,g_*Delta/2}.`

QED.

Consequently, after an arbitrary symmetric dense tail `T` with `||T||op<=delta<gamma_*`, the full ambient quadratic form satisfies

`boxed:
 ||p_(X^T(A0+tau vv^T+T)X)||infinity
 <= 6 sqrt(pi)/(gamma_*-delta)`                                    (7.5)

for **every** `tau in R`.

This is a true additional-eigenvalue stability theorem. The coefficient `tau` can pass through zero, become arbitrarily large, change sign, and cross the resonance of either individual core. The second core covers that resonance. Neither baseline core needs to be globally invertible; only its two-dimensional complement to the local update footprint is required to be invertible.

If both `B_j` happen to be invertible, then `r_j=-1/q_j` with `q_j=u_j^T B_j^{-1}u_j`. The condition is merely `q_1 != q_2`; the signs of `q_1,q_2` may be the same. Hence Theorem 7.1 is structurally different from the partner's opposite-sign routing lemma.

## 8. Exact application to the designated partner family

For the partner matrix `C` and `v`, use

`w=(1,1,1)^T/sqrt(3)`,
`z_1=(1,-1,0)^T/sqrt(2)`,
`z_2=(1,1,-2)^T/sqrt(6)`.

The local restriction of `v` to either physical triple is `(1,1,1)^T/2`, so

`g_1=g_2=3/4`.                                                      (8.1)

### Core H_-={1,2,3}

In the `[w,z_1,z_2]` basis,

`B_- = diag(-2,7,7)`.

Thus

`c_1=-2`, `D_1=diag(7,7)`, `mu_1=7`, `rho_1=0`,

and

`r_1=8/3`.                                                         (8.2)

### Core H_+={2,3,4}

A direct exact calculation in the same basis gives

`B11=2`,
`B12=(0,2 sqrt(2))`,
`D_2=diag(7,-9)`.                                                   (8.3)

Therefore

`c_2 = 2-(0,2sqrt(2)) diag(1/7,-1/9) (0,2sqrt(2))^T
     = 26/9`,

`mu_2=7`,
`rho_2=2 sqrt(2)/9`,

and

`r_2=-(26/9)/(3/4)=-104/27`.                                      (8.4)

The two resonance points are separated by

`Delta = 8/3 + 104/27 = 176/27`.                                  (8.5)

The exact shear factor of the second core is

`ell(rho_2)
 = 2/(sqrt(4+8/81)+2sqrt(2)/9)
 = (sqrt(83)-sqrt(2))/9`.                                          (8.6)

Hence Theorem 7.1 yields the purely structural uniform gap

`gamma_*
 = [(sqrt(83)-sqrt(2))/9]^2 * (22/9)
 = 22(85-2sqrt(166))/729
 = 1.78751667493017... .`                                          (8.7)

After an arbitrary dense tail of norm `1/4`, this generic resonance-separation compiler alone gives

`||p_Q||infinity
 <= 6 sqrt(pi)/(gamma_*-1/4)
 = 6.91681806047150... .`                                          (8.8)

Now apply the **completed fleet02/B12 result itself** to the same actual matrix. It proves the sharper selected-core inequality

`sigma_min((C+tau vv^T+E)[I_tau,I_tau]) >= 2-1/4=7/4`             (8.9)

for every real `tau` and every symmetric `E` with `||E||op<=1/4`. Therefore its density conclusion is

`boxed:
 ||p_(X^T(C+tau vv^T+E)X)||infinity
 <= 6 sqrt(pi)/(7/4)
 = 24 sqrt(pi)/7
 = 6.076984631676055... .`                                         (8.10)

Equation (8.10) is the required designated-partner result applied at an actual inequality. The new theorem explains the same all-real-`tau` stability without requiring the special sign monotonicity exploited by the sharper partner proof.

## 9. Why this is a genuine new stability mechanism

The previous r26/r27 theorems require an invertible baseline physical block because they use `B^{-1}` and the inverse-leverage matrix. Theorem 4.2 does not. For example,

`B=diag(0,1,-1)`, `u=e_1`.

Here `B` is singular, so neither Woodbury theorem applies. But `D=diag(1,-1)`, `c=0`, `rho=0`, `g=1`; therefore

`sigma_min(B+tau e_1e_1^T)=min{1,|tau|}`                           (9.1)

exactly, and every `|tau|>=1` gives a unit physical gap. A large added eigenvalue literally repairs the singular baseline core.

More generally, the dangerous coefficient set for one rank-one update is not an unbounded large-`|tau|` region: under the complementary nondegeneracy `D` invertible, it is a single resonance `r_*`. Two physical cores with separated resonances eliminate that obstruction uniformly.

## 10. What remains unpaid

This does **not** prove the full QFORM conjecture. The still-missing implication is structural: starting solely from the global assumption `s_3(A)>=1`, one must force at least one of the currently paid original-coordinate certificates — for example a localized nonsingular triple, two-core resonance separation, ridge/grouped-bank/hub/cross-volume structure, or another dependence-safe terminal mechanism.

The present run specifically removes one additional-eigenvalue obstacle: a physical baseline core need not be invertible in order for arbitrary large signed spectral additions to become controllable, and a rank-one arbitrary eigenvalue replacement can be made uniformly safe by two cores with distinct local resonance points.

No claim of a continuous density is made here. The terminal source supplies an essentially bounded density in this scope.

## 11. Status

**PROVED_SUPPORTING_THEOREMS / FULL_QFORM_OPEN / NOT_INDEPENDENTLY_REVIEWED.**

The new named statements are:

* `QFORM-SINGULAR-CORE-SCHUR-RESCUE-v1`;
* `QFORM-SINGULAR-CORE-LARGE-SPECTRUM-v1`;
* `QFORM-TWO-CORE-RESONANCE-SEPARATION-v1`.

Execution remains `WITHOUT_VERIFIED_BRAIN`: repository retrieval and writeback occurred, but no authenticated native learned-memory receiver use was verified.
