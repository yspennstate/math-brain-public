SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T20:15:51Z.
attacking: carrier-local spectral tail control by signed Schur complements and best low-rank action approximation.

# account01/B12 — signed local spectral-mass reserve compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Additional eigenvalue control  
Claim: `QFORM-SIGNED-LOCAL-SPECTRAL-MASS-RESERVE-v1`  
Status: **PROVED SUPPORTING STABILITY THEOREM / DESIGNATED account02-B12 RESULT APPLIED / EXACT TARGET-CLASS FAMILY / FULL QFORM OPEN.**  
Continuity: **not claimed** for the theorem below; only essential boundedness is imported from the physical-core receiver.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and overlap audit

The exact owner target remains open: independent real inputs with scalar densities at most one, arbitrary symmetric `A`, and only the global hypothesis `s_3(A)>=1`. No moment, compact-support, log-concavity, diagonal-basis, or independence-after-rotation assumption is introduced here.

There is already a completed sign-resolved adaptive spectral-tail theorem in account03/B12. In particular, favorable positive spectrum is free when protecting positive eigenvalues, favorable negative spectrum is free when protecting negative eigenvalues, and hostile eigenmodes can be spent through rank reserve. I therefore do **not** claim that one-sided/sign-resolved interlacing is new.

The new point is a bridge from the **literal eigenvalues of an added symmetric packet and their original-coordinate overlaps** to the hostile local tail. Instead of requiring the eigenvalues of the compressed hostile tail as input, the theorem below controls them by an exact local spectral mass

`sum |theta_a| ||P_H v_a||^2`.

This makes arbitrarily large global eigenvalues harmless when their physical overlaps are sufficiently small, and completely removes the magnitudes of any chosen hostile packet whose physical footprints span only a small dimension. The remainder is paid by local overlap mass divided by the number of unused reserve directions.

The newest designated partner result actually used is account02/B12:

- repository `yspennstate/math-open-problems`,
- commit `c635fcdce6aa206c68f1f14e061cf617d72376fb`,
- path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/account02-B12-20260923T185321Z-r11/REPORT.md`,
- theorem `QFORM-SIX-SQUARE-MODE-PAIR-COMPILER-v2`.

That theorem says: if `H` is an original-coordinate carrier of size `m>=6` and the **actual final matrix** satisfies

`lambda_6((A^2)[H,H]) >= g^2>0`,

then

`||p_(X^T A X)||_infinity <= C_m/g`,

where, with `N_2=binom(m,2)`,

`C_m=max{8 N_2 sqrt(6 pi m), 4 pi N_2, 3*400^(1/3)*(4N_2)^(5/6), 10 sqrt(2e/3)}`.

It keeps all outside spectrum/couplings and all signs. Its overall conclusion is essential boundedness; continuity is not claimed for every branch.

The current correction set was respected: no pointwise van-der-Corput estimate, arbitrary-joint coarea cap, conditional-density-supremum shortcut, fiber-sup dimension-free step, or independence after spectral rotation is used.

## 2. Setup: global signed spectrum versus a physical core

Let `H` be a set of `m` **original coordinates**, and let `P=P_H` be the orthogonal coordinate projection. Let

`A=A_0+E+T`,

with `A_0,E,T` real symmetric. Write the spectral decomposition of the added packet `E` as

`E=sum_a theta_a v_a v_a^T`,

where the `v_a` are orthonormal and `theta_a` are arbitrary real numbers. Define the global positive and negative parts

`E_+=sum_(theta_a>0) theta_a v_a v_a^T`,

`E_-=sum_(theta_a<0) |theta_a| v_a v_a^T`.

Thus `E=E_+-E_-`, with `E_+,E_- >=0`.

Compress to the physical core:

`C_0=P A_0 P|_H`,

`F=P E_+ P|_H >=0`,

`G=P E_- P|_H >=0`,

`T_H=P T P|_H`,

so the actual final principal block is

`C=C_0+F-G+T_H`.

The rest of `T` is unrestricted. In particular, `T` may have arbitrarily large outside-outside spectrum and arbitrarily large couplings between `H` and `H^c`; only

`delta_H:=||T_H||_op`

will be charged. This is legal because the final probabilistic receiver conditions on the coordinates outside `H`; those coefficients become affine/constant terms rather than a random error that must be small.

For each spectral vector put

`w_a=P v_a`.

The exact trace identities are

`tr F = sum_(theta_a>0) theta_a ||w_a||^2`,

`tr G = sum_(theta_a<0) |theta_a| ||w_a||^2`.                 (2.1)

These quantities are coordinate-local. A global coefficient `|theta_a|` can therefore be arbitrarily large if its overlap `||P v_a||^2` is correspondingly small.

## 3. One-sided local mass lemma

### Lemma 3.1 — positive reserve against a hostile negative packet

Fix an integer `u>=1`. Choose any subset `B_-` of the negative spectral modes. Let

`U_- = span{w_a: theta_a<0, a in B_-}`,

`r_- = dim U_-`.

The chosen coefficients `|theta_a|`, `a in B_-`, are unrestricted. Define the remaining negative local mass

`M_- = sum_(theta_a<0, a notin B_-) |theta_a| ||w_a||^2`.      (3.1)

Then for every integer `p>=0` with `u+r_-+p<=m`, the actual final block satisfies

`boxed:
lambda_u(C)
 >= lambda_(u+r_-+p)(C_0) - M_-/(p+1) - delta_H.`              (3.2)

Hence

`boxed:
lambda_u(C)
 >= max_(0<=p<=m-u-r_-)
      [lambda_(u+r_-+p)(C_0)-M_-/(p+1)] - delta_H.`            (3.3)

### Proof

Split the compressed hostile packet as

`G=G_big+G_tail`,

where

`G_big=sum_(theta_a<0,a in B_-) |theta_a| w_a w_a^T`.

By construction

`rank G_big <= r_-`.                                           (3.4)

The remainder is positive semidefinite and, by (2.1),

`tr G_tail=M_-`.                                               (3.5)

Let its eigenvalues be

`mu_1>=mu_2>=...>=0`.

Because

`sum_(j=1)^(p+1) mu_j <= tr G_tail=M_-`,

we have the elementary tail estimate

`boxed: mu_(p+1) <= M_-/(p+1).`                                (3.6)

Let `G_p` be the sum of the first `p` eigenmodes of `G_tail` and put `R_p=G_tail-G_p`. Then

`rank(G_big+G_p)<=r_-+p`,

`||R_p||_op=mu_(p+1)<=M_-/(p+1)`.                              (3.7)

First ignore `R_p` and `T_H` and set

`K=C_0+F-(G_big+G_p)`.

Since `F>=0`, Weyl monotonicity gives

`lambda_(u+r_-+p)(C_0+F)
 >= lambda_(u+r_-+p)(C_0)`.                                   (3.8)

Subtracting a matrix of rank at most `r_-+p` can move the desired eigenvalue down by at most that many positions, so rank interlacing gives

`lambda_u(K)
 >= lambda_(u+r_-+p)(C_0+F)
 >= lambda_(u+r_-+p)(C_0)`.                                   (3.9)

Restore `-R_p`. Weyl's operator-norm inequality and (3.7) imply

`lambda_u(K-R_p)
 >= lambda_u(K)-M_-/(p+1)`.                                   (3.10)

Finally restore `T_H`, which costs at most `delta_H`. This proves (3.2), and maximizing over `p` proves (3.3). QED.

### Flat-reserve corollary

If `C_0` has at least `N_+` positive eigenvalues at least `kappa_+>0`, and

`N_+>=u+r_-`,

choose

`p=N_+-u-r_-`.

Then

`boxed:
lambda_u(C)
 >= kappa_+ - M_-/(N_+-u-r_-+1) - delta_H.`                   (3.11)

Thus every chosen hostile negative mode is magnitude-free; the unchosen hostile modes are paid only through their **local overlap-weighted spectral mass divided by unused positive reserve count**. All positive spectrum of `E` is free in this inequality, regardless of rank and magnitude.

## 4. The negative side

Apply Lemma 3.1 to `-C`. Choose any subset `B_+` of the positive spectral modes and set

`r_+ = dim span{w_a: theta_a>0, a in B_+}`,

`M_+ = sum_(theta_a>0, a notin B_+) theta_a ||w_a||^2`.        (4.1)

For every `v>=1` and `p>=0` with `v+r_++p<=m`,

`boxed:
lambda_v(-C)
 >= lambda_(v+r_++p)(-C_0) - M_+/(p+1) - delta_H.`             (4.2)

If `C_0` has at least `N_-` negative eigenvalues at most `-kappa_-`, `N_->=v+r_+`, then

`boxed:
lambda_v(-C)
 >= kappa_- - M_+/(N_--v-r_++1) - delta_H.`                   (4.3)

Again, the chosen hostile positive packet is magnitude-free, the remainder is paid by local positive spectral mass divided by negative reserve, and the entire negative part of `E` is favorable/free for this side.

## 5. Signed local spectral-mass compiler

### Theorem 5.1 — `QFORM-SIGNED-LOCAL-SPECTRAL-MASS-RESERVE-v1`

Use the setup of Sections 2-4. Let `u,v` be nonnegative integers with

`u+v>=3`.

For each active positive side (`u>0`) choose a hostile negative set `B_-`; for each active negative side (`v>0`) choose a hostile positive set `B_+`. Define

`Gamma_+
 = max_(0<=p<=m-u-r_-)
   [lambda_(u+r_-+p)(C_0)-M_-/(p+1)]-delta_H`,                 (5.1)

`Gamma_-
 = max_(0<=p<=m-v-r_+)
   [lambda_(v+r_++p)(-C_0)-M_+/(p+1)]-delta_H`.                (5.2)

Ignore a `Gamma` whose count is zero. If every active `Gamma` is positive, put

`g=min(active Gamma_+, active Gamma_-)`.

Then the actual physical block `C=A[H,H]` has at least `u` positive eigenvalues at least `g` and `v` negative eigenvalues at most `-g`. In particular it has at least three eigenvalues of modulus at least `g`.

Condition on all original coordinates outside `H`. The coordinates in `H` remain independent and each keeps density cap one. All outside quadratic/cross terms become an arbitrary affine-plus-constant perturbation of the form on `H`. The completed finite physical-core receiver therefore gives

`boxed:
||p_(X^T A X)||_infinity <= 2 sqrt(6 pi m)/g.`                 (5.3)

Only essential boundedness is asserted here. No post-rotation independence is used.

### Literal eigenvalue interpretation

The theorem applies to the literal spectral decomposition of **the added matrix** `E`. If `E` commutes with `A_0`, it is also a theorem about literal replacements of baseline eigenvalues. In the noncommuting case it is still a valid arbitrary signed spectral-addition theorem: the random variables in the spectral basis are never used, so their dependence is irrelevant.

The key currencies are exactly

`rank span{P_H v_a: selected hostile modes}`

and

`sum |theta_a| ||P_H v_a||^2`

for the unselected hostile modes. Thus an arbitrary number of large eigenvalues can be free in either of two ways:

1. their physical footprints lie in a low-dimensional subspace and are placed in the selected packet; or
2. their physical overlaps are tiny enough that the overlap-weighted local mass stays bounded.

This is strictly a deterministic matrix certificate followed by original-coordinate conditioning.

## 6. Exact target-class stress family

Take an original-coordinate core `H` of size `m=8` and baseline

`C_0=diag(4,4,4,4,-4,-4,-4,-4)`.                            (6.1)

Outside `H`, allow arbitrary additional coordinates.

### Unbounded selected packets

Choose any collection of negative eigenmodes of `E` whose projected vectors `P_H v_a` all lie in `span(e_1)`. Their coefficients may be independently arbitrarily large. Put all of them into `B_-`. Then

`r_-=1`,                                                       (6.2)

regardless of their number and magnitudes.

Similarly choose any collection of positive eigenmodes whose projected vectors all lie in `span(e_5)`, put them into `B_+`, and allow all their coefficients to be independently arbitrarily large. Then

`r_+=1`.                                                       (6.3)

Such collections exist in arbitrarily large ambient dimension: orthogonal global eigenvectors can have collinear small projections onto `H` and use mutually orthogonal outside components.

### Arbitrarily many residual modes

Allow all remaining negative modes, of arbitrary number and arbitrary global magnitudes, subject only to

`M_- = sum_(remaining negative a) |theta_a| ||P_H v_a||^2 <=1/2`.    (6.4)

Allow all remaining positive modes under

`M_+ = sum_(remaining positive a) theta_a ||P_H v_a||^2 <=1/2`.      (6.5)

The individual `|theta_a|` are not bounded: large coefficients are permitted when their physical overlaps are correspondingly small.

Finally add any symmetric matrix `T` such that only

`||T[H,H]||_op<=1/4`.                                         (6.6)

Every other entry of `T`, including its entire outside-outside block and all couplings to `H`, is unrestricted in magnitude.

Protect `u=2` positive and `v=1` negative modes. For the positive side,

`N_+=4`, `kappa_+=4`, `r_-=1`,

so (3.11) gives

`Gamma_+ >= 4 - (1/2)/(4-2-1+1) - 1/4`
`          =4-1/4-1/4`
`          =7/2.`                                              (6.7)

For the negative side,

`N_-=4`, `kappa_-=4`, `r_+=1`,

so

`Gamma_- >=4-(1/2)/(4-1-1+1)-1/4`
`          =4-1/6-1/4`
`          =43/12.`                                            (6.8)

Hence `g=7/2`. The final physical block has two eigenvalues at least `7/2` and one eigenvalue at most `-7/2`. By principal-submatrix interlacing, the **full final matrix** has at least three eigenvalues of modulus at least `7/2`; the family therefore lies literally inside the owner's exact target class.

The physical-core receiver gives

`boxed:
||p_Q||_infinity
 <= 2 sqrt(48 pi)/(7/2)
 = (16/7) sqrt(3 pi)
 = 7.017097425918778... .`                                    (6.9)

This is uniform in the number and magnitudes of all selected modes, in all residual global eigenvalue magnitudes satisfying (6.4)-(6.5), in ambient dimension, in every allowed off-core matrix entry, and in every independent cap-one input law.

## 7. Required application of the completed account02/B12 result

The same family gives a direct equation-level use of the designated partner theorem.

Let `L` be the sum of the two selected hostile local packets. From (6.2)-(6.3),

`rank L<=2`.                                                   (7.1)

Let the remaining signed local spectral packet be

`R=F_tail-G_tail`,

where `F_tail,G_tail>=0` and, by (6.4)-(6.5),

`tr F_tail<=1/2`, `tr G_tail<=1/2`.

For positive semidefinite `F_tail,G_tail`,

`-G_tail <= F_tail-G_tail <= F_tail`,

so

`boxed: ||R||_op<=1/2.`                                       (7.2)

The actual final physical block is

`C=C_0+L+R+T_H`.

Because `rank L<=2` and all eight singular values of `C_0` equal four, rank interlacing gives

`s_6(C_0+L)>=s_8(C_0)=4`.                                     (7.3)

Weyl plus (7.2) and (6.6) yields

`boxed: s_6(C)>=4-1/2-1/4=13/4.`                              (7.4)

Now write the full actual matrix in the original-coordinate split `H direct_sum H^c` as

`A=[[C,B],[B^T,D]]`.

The exact identity

`(A^2)[H,H]=C^2+B B^T`                                        (7.5)

contains an arbitrary `B`; no smallness is assumed. Since `B B^T>=0`,

`lambda_6((A^2)[H,H])
 >=lambda_6(C^2)
 =s_6(C)^2
 >=(13/4)^2.`                                                  (7.6)

Apply the completed account02/B12 `QFORM-SIX-SQUARE-MODE-PAIR-COMPILER-v2` with

`m=8`, `g=13/4`.

Here `N_2=28` and

`C_8=max{`
` 224 sqrt(48 pi),`
` 112 pi,`
` 3*400^(1/3)*112^(5/6),`
` 10 sqrt(2e/3)`
`}`
` =2750.7021909601613... .`                                   (7.7)

Thus the partner theorem gives, on the same actual final matrices,

`boxed:
||p_Q||_infinity
 <= C_8/(13/4)
 =846.3699049108188... .`                                     (7.8)

The direct signed local-mass theorem is much sharper on this family, but (7.6)-(7.8) verify the required partner application on an actual inequality. Notice that even for the partner route the arbitrary cross block `B` is harmless here because it enters (7.5) positively.

## 8. Why this does not solve full QFORM

The missing implication is still structural. Starting only from

`s_3(A)>=1`,

we do not know how to force a bounded-size original-coordinate core `H` and a baseline/addition decomposition for which enough signed reserve survives while the hostile spectrum has either low physical footprint rank or small overlap-weighted local mass. Nor is it known that failure of every such certificate automatically forces one of the completed D5, ridge, grouped-hub/bank, projected-crossing, physical-pair, half-Riesz, or Schur exits.

The theorem therefore solves a genuine **additional-eigenvalue stability** question but not the universal extraction problem. It also does not establish the full target's requested continuity.

## 9. Source/correction discipline


No use was made of:

- uniform pointwise quadratic-phase decay;
- arbitrary-joint rank-three coarea;
- conditional projection density moments;
- independence after diagonalizing `A`;
- a universal good physical minor;
- a universal rank-three cross cut;
- a claim that small matrix norm makes `X^T T X` small.

The local `delta_H` in this proof appears only inside a deterministic eigenvalue Weyl inequality for the actual physical principal block.

Full target status: **OPEN**.  
Global continuity status: **OPEN**.  
This run: **supporting theorem proved, exact target-class family proved, designated partner applied, no full-solution claim**.
