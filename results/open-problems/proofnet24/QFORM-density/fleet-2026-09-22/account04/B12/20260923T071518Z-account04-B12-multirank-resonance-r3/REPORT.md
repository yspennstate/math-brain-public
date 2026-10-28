# account04/B12 — multirank resonance separation with dense-tail stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T071518Z-account04-B12-multirank-resonance-r3`  
Assignment: Additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**  
Continuity: separate; the theorem below asserts essential boundedness.

## 1. Scope

The full target is the universal density bound for `X^T A X), for independent real coordinates with density caps at most one and arbitrary symmetric `A` satisfying `s_3(A) >= 1`.

This report proves a stability theorem for a genuine multirank spectral hub. The coefficient may be arbitrarily large, have either sign, and pass through every local singularity. Two original-coordinate physical cores with separated finite resonance sets guarantee that at least one actual principal block remains uniformly nonsingular. An arbitrary dense tail is then absorbed by Weyl's matrix inequality only; it is never treated as a small random quadratic error.

The remaining global extraction problem is stated in Section 7.

## 2. Sources used

1. Required Claude source:
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.
   Its physical three-coordinate theorem gives

   `||p_Q||_infinity <= 6 sqrt(pi)/c`

   whenever an actual original-coordinate `3 x 3` principal block has all singular values at least `c>0`, uniformly in the affine terms created by conditioning.

2. Its finite-dimensional companion in the subsequent Claude synthesis gives, on an actual `m`-coordinate block with `s_3 >= c`,

   `||p_Q||_infinity <= 2 sqrt(6 pi m)/c.`                     (2.1)

3. Completed partner account01/B12:
   `yspennstate/math-open-problems@c63eec6fd03d23bb41493a502670d52bed383d35`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B12/20260923T065152Z-account01-B12-QFORM-r28/REPORT.md`.
   Its exact complementary-Schur factorization and shear estimate are applied below:

   `B+U Theta U^T = L diag(C+F,D) L^T`,  
   `sigma_min(L)=ell(rho)`,                                    (2.2)

   where `ell(rho)=(sqrt(rho^2+4)-rho)/2`.


## 3. A multirank local resonance formula

Fix an original-coordinate set `I` of size `m>=3`. Let `B=B^T` be the baseline principal block and `U` an `m x r` matrix of full column rank, with `1<=r<m`. Choose an orthonormal basis `W` for `range(U)` and an orthonormal complement `Z). Write

`B11=W^T B W`, `B12=W^T B Z`, `D=Z^T B Z`.

Assume `D` invertible, and put

`C=B11-B12 D^(-1) B12^T`,  
`F=W^T U U^T W`,  
`rho=||B12 D^(-1)||_op`,  
`mu=sigma_min(D)`.

Since `U` has full local rank, `F>0`. Define

`K=F^(-1/2) C F^(-1/2)`,  
`R={-lambda: lambda in spec(K)}`,  
`f=lambda_min(F)`.                                             (3.1)

For the scalar spectral hub `B(tau)=B+tau U U^T`, the account01/B12 factorization (2.2) has Schur block

`C+tau F = F^(1/2) (K+tau I) F^(1/2)`.                         (3.2)

Therefore

`sigma_min(C+tau F) >= f dist(tau,R)`.                         (3.3)

Applying the completed account01/B12 shear inequality at this actual equation gives

`sigma_min(B+tau U U^T) >= ell(rho)^2 min{mu, f dist(tau,R)}.`  (3.4)

For `r=1`, `R` is the single resonance from account01/B12 r28. Equation (3.4) is its multirank extension: a rank-`r` scalar hub has at most `r` local resonance points.

## 4. Two-core multirank resonance separation

Let `I_1,I_2` be two original-coordinate physical cores for the same baseline `A_0` and the same global hub matrix `V). Put

`B_j=A_0[I_j,I_j]`, `U_j=V[I_j,:]`.

Assume each `U_j` has full column rank `r<|I_j|`, and each complementary block `D_j` above is invertible. Define `R_j,f_j,mu_j,rho_j` as in Section 3. Suppose the finite resonance sets are disjoint, with

`Delta=dist(R_1,R_2)>0`.                                       (4.1)

Set

`f_*=min(f_1,f_2)`, `mu_*=min(mu_1,mu_2)`,  
`ell_*=min(ell(rho_1),ell(rho_2))`,

and

`gamma_*=ell_*^2 min{mu_*,f_* Delta/2}`.                       (4.2)

### Theorem 4.1 — `QFORM-MULTIRANK-TWO-CORE-RESONANCE-SEPARATION-v1`

For every real `tau`, at least one `j in {1,2}` satisfies

`sigma_min(B_j+tau U_j U_j^T) >= gamma_*`.                     (4.3)

Moreover, let `H=H^T` be arbitrary, with no global norm bound, and let `T=T^T` be an arbitrary dense perturbation with `||T||_op<=delta`. Put

`eta=max_j ||H[I_j,I_j]||_op`, `epsilon=eta+delta`.          (4.4)

If `epsilon<gamma_*`, then for

`A=A_0+tau V V^T+H+T`

one of the two actual principal blocks has smallest singular value at least `gamma_*-epsilon`. Consequently, if both cores have size at most `m`,

`||p_(X^T A X)||_infinity <= 2 sqrt(6 pi m)/(gamma_*-epsilon).` (4.5)

If the cores are triples, the sharper physical-fiber theorem gives

`||p_(X^T A X)||_infinity <= 6 sqrt(pi)/(gamma_*-epsilon).`    (4.6)

### Proof

For every real `tau`,

`dist(tau,R_1)+dist(tau,R_2) >= Delta`.

Hence one of the two distances is at least `Delta/2`. Equation (3.4) on that core gives (4.3).

The compression of `H+T` to that core has operator norm at most `eta+delta`. Weyl's singular-value inequality therefore gives the actual gap `gamma_*-epsilon`. Condition on every coordinate outside that original-coordinate core and apply (2.1), or the sharper three-coordinate theorem. No probabilistic estimate of `X^T(H+T)X` is used. QED.

## 5. Literal two-eigenvalue replacement with an arbitrary dense tail

The theorem applies to an explicit target-class family.

On seven original coordinates let

`A_0=diag(1,1,3,1,1,3,3)`,

and define orthonormal eigenvectors of `A_0`

`v_1=(1/2)e_1+(sqrt(3)/2)e_4`,  
`v_2=(1/2)e_2+(sqrt(3)/2)e_5`.

Let `V=(v_1,v_2)`. Then

`A_tau^0=A_0+tau V V^T`                                       (5.1)

literally replaces two eigenvalues `1` by `1+tau`. The replacement is simultaneous, may be arbitrarily large, may have either sign, and may cross zero.

Take `I_1={1,2,3}` and `I_2={4,5,6}`. For both cores `B_j=diag(1,1,3)`, while

`U_1 U_1^T=diag(1/4,1/4,0)`,  
`U_2 U_2^T=diag(3/4,3/4,0)`.

Thus

`R_1={-4}`, `R_2={-4/3}`, `Delta=8/3`.

Also `rho_1=rho_2=0`, `mu_1=mu_2=3`, and `f_*=1/4`. Hence

`gamma_*=min{3,(1/4)(8/3)/2}=1/3`.                             (5.2)

Now add any symmetric dense `T` with

`||T||_op<=1/12`.                                               (5.3)

Equations (4.6) and (5.2) give the concrete target-level inequality

`||p_(X^T(A_tau^0+T)X)||_infinity <= 6 sqrt(pi)/(1/3-1/12)`  
`                                      = 24 sqrt(pi) < 42.539`. (5.4)

This is uniform for every real `tau`, every admissible product law, and every dense `T` satisfying (5.3).

The family always satisfies the original spectral hypothesis. Before adding `T`, the unaffected coordinates `e_3,e_6,e_7` give three eigenvalues equal to `3`; hence after (5.3),

`s_3(A_tau^0+T) >= 3-1/12 = 35/12 > 1`.                        (5.5)

## 6. Why the dense tail is legitimate

The tail `T` appears only in the deterministic inequality

`sigma_min((A_tau^0+T)[I_j,I_j])`  
`>= sigma_min(A_tau^0[I_j,I_j])-||T||_op`.

It is not treated as a small random error. For the allowed unbounded inputs, small `||T||_op` does not imply small `X^T T X`.

The arbitrary matrix `H` in Theorem 4.1 is even allowed to have unbounded global norm; it is charged only through its actual compressions to the protected cores.

## 7. Remaining implication

The full conjecture remains open. The missing structural statement is to force, from `s_3(A)>=1` alone, either:

1. two bounded physical cores with quantitatively separated multirank resonance sets;
2. one already-paid actual principal block;
3. a threshold-robust cross-volume, mixed-hub, grouped-bank, ridge, or Schur certificate.

The theorem does not claim that every matrix admits the two-core certificate, and it does not select one universally good minor. It proves that once two such cores exist, arbitrary signed common shifts of up to `m-1` eigen-directions and an arbitrary small dense tail are completely paid.

## 8. Status

**PROVED SUPPORTING THEOREM / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED.**

Named result: `QFORM-MULTIRANK-TWO-CORE-RESONANCE-SEPARATION-v1`.

Execution remains `WITHOUT_VERIFIED_BRAIN`: repository reads and writes are verified, but native learned-memory ingestion is not.
