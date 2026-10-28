SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B07, 2026-09-24T06:41:26Z.
attacking: the global rank-two separator — aggregate pair transfers by determinant weight into one physical E3 cut, then synchronize the unpaid local two-planes to the global rank-two carrier.

# account03/B07 r49 — pair-block random-cut E3 compiler and global two-plane synchronization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
Status: **NEW DIMENSION-FREE RANDOM-CUT COMPILER + NEW GLOBAL TWO-PLANE NORMAL FORM / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No Gaussian, moment, log-concavity, compact-support, connected-support, iid, diagonal-basis, post-rotation independence, pointwise quadratic-phase decay, arbitrary-joint coarea, fiber supremum, or deletion of a nonzero coefficient tail is used. SVDs below are deterministic coefficient algebra only.

## 1. Fresh source state and exact incoming branch


The incoming live branch is account03/B07 r48:

`yspennstate/math-open-problems@cdd0eb22227a505e827a658038a1512897c0ad56`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260924T053826Z-account03-B07-qform-r48/REPORT.md`.

There is a literal physical cut `T | S`, where `S` is partitioned into the pair-disjoint matching `P`, and

`M=A[T,S]`.

On the unpaid non-near-rank-one branch r48 proves

`dist_F(M,rank<=2)<eps`, `eps=2^-16`,                              (1.1)

`s2(M)>d_*=0.10429071727552326290...`,                            (1.2)

`s1(M)s2(M)>p_*=1.19876993884320...`.                             (1.3)

For each physical matched pair `K subset S`, deleting both columns gives `M_{-K}`. The determinant-weighted pair inclusion theorem in r48 says that all but at most two pairs are **stable**, with

`Z_K:=e2(M_{-K}M_{-K}^T)>z0:=p_*^2/3`
`=0.4790164554247098227...`.                                     (1.4)

The completed marginal-free physical-E3 receiver actually used below is account02/B03:

`yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T184716Z-account02-B03-QFORM-auto11/REPORT.md`.

For every literal physical crossing `C` with `Z3=e3(CC^T)>0`, it retains arbitrary same-side blocks, affine terms, outside couplings, signs and extra spectrum and gives

`||p_Q||_infinity <= C3 Z3^(-1/6)`,
`C3=10.5501688311648...`,                                        (1.5)

with a continuous density on this paid branch.

The designated partner read and applied below is account04/B07:

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T161510Z-account04-B07-coordinate-core-r2/REPORT.md`.

Its theorem states that an actual physical principal block of size `m=r+3` with

`A[I,I]=D+R+E`, `D` diagonal, `|D_ii|>=d`, `rank R<=r`, `|E|_max<=eta0`,

satisfies

`s3(A[I,I])>=d-(r+3)eta0`,                                       (1.6)

and therefore the full ambient essential-density bound

`||p_Q||_infinity <= 2 sqrt(6 pi (r+3))/(d-(r+3)eta0)`           (1.7)

when the denominator is positive. Continuity is not claimed by that gate.

## 2. All but five pairs retain a robust restriction of the same global rank-two carrier

Let

`M=L+E`,                                                         (2.1)

where `L` is the top-two SVD truncation of `M`. Then `rank L<=2` and

`||E||_F<eps`.                                                    (2.2)

Let `V` be the `|S| x 2` matrix of the two right singular vectors of `M`. For a matched physical pair `K`, define its global rank-two leverage

`ell_K=||V[K,:]||_F^2`.                                          (2.3)

Because `V^T V=I_2`,

`sum_K ell_K=2`.                                                  (2.4)

Hence at most three pairs have `ell_K>1/2`. Call a pair **good** when it is stable in the sense of (1.4) and `ell_K<=1/2`. There are at most five non-good pairs total.

Fix a good pair `K`. Put

`N_K=M[:,S\K]`, `L_K=L[:,S\K]`.                                  (2.5)

Since

`V[S\K,:]^T V[S\K,:]=I_2-V[K,:]^T V[K,:]`,                      (2.6)

its smallest eigenvalue is at least `1-ell_K>=1/2`. Therefore

`s2(L_K)>=s2(M)/sqrt(2)>d_*/sqrt(2)`.                             (2.7)

Weyl gives

`s2(N_K)>c_N:=d_*/sqrt(2)-eps`
`=0.07372941461126901...`.                                       (2.8)

Also

`sum_{j>=3}s_j(N_K)^2<=||N_K-L_K||_F^2<eps^2`.                  (2.9)

Thus deletion of any good pair leaves not merely aggregate E2 mass, but a quantitatively robust two-dimensional singular carrier inherited from the SAME global two-plane.

## 3. The second Newton transform is uniformly positive off the local top-two plane

Write the squared singular values of `N_K` as

`x1>=x2>=x3>=...>=0`,

and set

`Z_K=e2(x)`, `t=sum_{j>=3}x_j`.                                  (3.1)

From (2.8)-(2.9),

`x2>=c_N^2`, `t<eps^2`.                                          (3.2)

Let `P_K` be the orthogonal projector onto the top-two **right** singular subspace of `N_K`. For

`G_K=N_K^T N_K`,

its second Newton transform is

`H2(G_K)=G_K^2-tr(G_K)G_K+Z_K I`.                                (3.3)

In an eigenvector with eigenvalue `x_j`, the eigenvalue of `H2` is

`Z_K(1-alpha_j)`,
`alpha_j=x_j(tr G_K-x_j)/Z_K`.                                   (3.4)

For every `j>=3`, using `Z_K>=x1 x2`,

`alpha_j <= t(x1+x2+t)/(x1 x2)`
`          <=2r+r^2`,                                            (3.5)

where

`r=eps^2/c_N^2=4.28310348144e-8`,
`2r+r^2<8.566208e-8<1/2`.                                       (3.6)

Hence

`boxed: H2(G_K) >= (Z_K/2)(I-P_K)`                               (3.7)

as a Loewner inequality on the full column space.

This is stronger than the generic `Z/3` heavy-marginal bound because the live global rank-two tube makes the entire tail quantitatively tiny after every good pair deletion.

## 4. Exact pair-transfer packet and one random physical cut

For a good pair `K`, let

`R_K=A[K,S\K]`                                                    (4.1)

be its two physical rows into the rest of the matched bank. Define the complete pair-transfer determinant packet

`F_K := sum_{r in K} sum_{I subset T, |I|=2}`
`                   sum_{J subset S\K, |J|=3}`
`                   det A[I union {r},J]^2`.                     (4.2)

Cauchy-Binet gives the exact identity

`boxed: F_K=tr(R_K H2(G_K) R_K^T).`                              (4.3)

Therefore, with

`q_K=||R_K(I-P_K)||_F`,                                          (4.4)

(1.4) and (3.7) yield

`boxed: F_K >= (Z_K/2) q_K^2 > (z0/2) q_K^2.`                   (4.5)

Now independently mark every matched pair of `S` moved/not moved with probability `1/2`. For a moved-pair set `U`, take the literal physical cut

`L_U=T union (union_{K in U} K)`,
`R_U=S \ (union_{K in U} K)`.                                   (4.6)

Every determinant in (4.2) appears in the crossing `A[L_U,R_U]` whenever its row pair `K` is moved and every matched pair touched by its three columns is not moved. Three columns touch at most three matched pairs, so this event has probability at least

`2^-4=1/16`.                                                      (4.7)

The packets for different `K` contain distinct physical row triples, so there is no double counting. Hence

`E_U e3(A[L_U,R_U]A[L_U,R_U]^T)`
` >= (1/16) sum_{K good} F_K`.                                  (4.8)

Combining with (4.5):

`boxed:
 max_U e3(A[L_U,R_U]A[L_U,R_U]^T)
 > (z0/32) sum_{K good} q_K^2.
}`                                                               (4.9)

This is `QFORM-PAIRBLOCK-RANDOMCUT-E3-COMPILER-v1`.

The selection is dimension free and aggregate-before-inversion: it spends the complete determinant packets of every good pair, and only then chooses one literal physical cut. No reciprocal individual coordinate minor appears.

## 5. Concrete paid branch and aggregate plane synchronization

Set

`tau=2^-30`.                                                      (5.1)

If the cut furnished by (4.9) has `E3>=tau`, the completed account02/B03 theorem gives the full ambient form a **continuous** density satisfying

`boxed: ||p_Q||_infinity <= C3 tau^(-1/6)`
`=337.6054025972736... .`                                        (5.2)

Therefore every survivor of this payment satisfies

`sum_{K good} q_K^2`
` < 32 tau/z0`
` =6.22156547028676e-8`,                                        (5.3)

and hence

`boxed: (sum q_K^2)^(1/2)<2.49430661112e-4.`                    (5.4)

So the unpaid branch cannot have independently wandering pair-transfer residuals at macroscopic total scale.

## 6. The local planes are restrictions of one global rank-two plane, up to 2.93e-4 angle

Let `Q_K` be the row space of `L_K`; equivalently it is the two-dimensional space generated by the restriction `V[S\K,:]`. Because `ell_K<=1/2`, it is genuinely two dimensional.

Let `v_1,v_2` be the top-two right singular vectors of `N_K`, with left singular vectors `u_1,u_2`. From

`N_K^T u_j=s_j(N_K)v_j`                                         (6.1)

and `(I-Q_K)L_K^T=0`,

`s_j(N_K)(I-Q_K)v_j=(I-Q_K)(N_K-L_K)^T u_j`.                    (6.2)

Using (2.2) and (2.8),

`||(I-Q_K)v_j|| <= eps/c_N`.                                    (6.3)

Thus

`||(I-Q_K)P_K||_F`
` <= eta:=sqrt(2) eps/c_N`
` =2.92680832356e-4`.                                            (6.4)

Define the fixed-carrier residual

`d_K=dist_F(R_K,Q_K)=||R_K(I-Q_K)||_F`.                          (6.5)

Then

`d_K<=q_K+eta ||R_K||_F`.                                       (6.6)

Consequently, if

`E_star=sum_{K good}||R_K||_F^2`,                               (6.7)

an unpaid state obeys

`boxed:
 sum_{K good} d_K^2
 < 64 tau/z0 + 2 eta^2 E_star.
}`                                                               (6.8)

Numerically,

`64 tau/z0=1.24431309406e-7`,
`2 eta^2=1.71324139258e-7`.                                     (6.9)

This is the first common-plane synchronization on the live pair-matching branch: except for at most five pair blocks, every local determinant-heavy transfer plane is quantitatively tied to the restriction of the SAME global top-two right-singular plane.

## 7. A bounded-complexity normal form on the matched bank

Assume the concrete moderate-internal-energy subbranch

`E_star<=1`.                                                     (7.1)

Then (6.8) gives

`D0:=sqrt(sum d_K^2)`
` <5.43834026762e-4`.                                            (7.2)

For each good physical row `i in K`, choose a coefficient `c_i in R^2` whose global carrier row `c_i^T V^T`, restricted to `S\K`, is the orthogonal projection of `A[i,S\K]` onto `Q_K`. Assemble these coefficients into `C` and set

`H=C V^T`, `R4=(H+H^T)/2`.                                      (7.3)

Then `rank R4<=4`. On the good-good off-pair entries, the symmetric residual has Frobenius norm at most `D0`: rowwise projection has squared error `sum d_K^2`, and symmetrizing cannot increase that Frobenius norm.

There are at most five exceptional pair blocks, hence at most ten exceptional physical coordinates. Every symmetric matrix supported on rows/columns of ten coordinates has rank at most twenty. Absorbing every interaction involving those exceptional coordinates into such a matrix gives the exact physical-bank decomposition

`boxed:
 A[S,S]=B_pair + R_24 + E_S,
}`                                                               (7.4)

where

* `B_pair` is block diagonal on the good original matched `2 x 2` physical pair blocks (and zero on the exceptional coordinates if desired);
* `rank R_24<=24`;
* `E_S` is symmetric, supported only on good-good off-pair entries, and

`boxed: ||E_S||_F<5.43834026762e-4.`                            (7.5)

No probabilistic coordinate rotation is performed. `B_pair` remains in literal original-coordinate pairs. This is `QFORM-GLOBAL-R2-PAIRBLOCK-NORMALFORM-v1`.

If (7.1) fails, the survivor instead carries the explicit new resource

`boxed: sum_{K good}||A[K,S\K]||_F^2>1,`                        (7.6)

which is a same-bank physical-star energy branch rather than an unstructured remainder.

## 8. Required account04/B07 result applied to the new normal form

Stay in the unpaid `E_star<=1` branch. Suppose there are 27 distinct **good** matched pairs for which the pair-block term `B_pair` has at least one physical diagonal entry of magnitude at least

`d=1/64`.                                                        (8.1)

Choose one such literal coordinate from each pair. On the resulting actual 27-coordinate principal set `I`, the restriction of `B_pair` is diagonal because no two chosen coordinates come from the same pair. Equation (7.4) becomes exactly the partner hypothesis with

`r=24`, `m=r+3=27`, `epsilon0=D0`.                               (8.2)

Therefore

`s3(A[I,I])`
` >=1/64-27 D0`
` >0.000941481277444...`.                                        (8.3)

The account04/B07 physical-core theorem gives the full ambient essential-density bound

`boxed: ||p_Q||_infinity <47923.746.`                            (8.4)

Continuity is not claimed by this partner gate.

Thus a still-unpaid moderate-energy normal-form survivor has at most **26** good pair blocks with a `B_pair` physical diagonal of magnitude `>=1/64`. All remaining good pair blocks have both residual physical diagonals `<1/64` in magnitude; their off-diagonal pair coefficient is retained exactly and is not discarded as a small perturbation.

This is an actual application of the designated partner theorem to the new rank-24 inequality, not a repetition of the earlier r48 graph condition.

## 9. What is closed and what remains

The r48 global rank-two separator is now substantially sharper.

For its pair-matching branch, one of the following must occur:

1. a literal physical crossing has `E3>=2^-30`, giving the full ambient law a **continuous density <=337.606**;
2. more than unit total same-bank pair-star energy survives as in (7.6);
3. the entire matched bank has the physical normal form `2x2-pair-block-diagonal + rank<=24 + Frobenius tail <5.44e-4`; within this branch, 27 large residual pair-diagonal pivots trigger the account04/B07 core and give essential density `<47924`, so an unpaid survivor has at most 26 such pair blocks.

The genuinely new mechanism is (4.9): a random cut of **whole physical pair blocks** compiles all pair-transfer determinant packets into one third exterior volume with a universal `1/16` loss. The argument never chooses one tiny principal minor.

The next exact debt is `QFORM-PAIRBLOCK-R24-SMALLTAIL-RECEIVER-v1`: consume the survivor

`B_pair + rank<=24 + ||E||_F<5.44e-4`

when almost all pair-block residual diagonals are `<1/64`, while retaining arbitrary pair off-diagonals, arbitrary `A[T,T]`, the nonzero global cross tail, outside couplings and all extra spectrum. The separate `E_star>1` same-bank-star branch is now an explicit alternative and should be attacked by the same random-cut/exterior-volume currency before any reciprocal pivot.

Full QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**. Continuity is proved here only on the physical-E3 payment (5.2); the partner core (8.4) establishes essential boundedness only.

## 10. Finite regression checks

`CHECKS.py`/`CHECKS.txt` in this run directory verify:

* the exact identity `F_K=tr(R_K H2(N_K^T N_K)R_K^T)` on seeded random matrices;
* exhaustive small pair-block random cuts satisfy `average E3 >= (sum F_K)/16`;
* the leverage count `sum ell_K=2` and the numerical tail-marginal bound in (3.6);
* the propagated constants in Sections 5--8.

These computations are regression evidence only; the proof is the deterministic Cauchy-Binet/Newton-transform/random-cut argument above.
