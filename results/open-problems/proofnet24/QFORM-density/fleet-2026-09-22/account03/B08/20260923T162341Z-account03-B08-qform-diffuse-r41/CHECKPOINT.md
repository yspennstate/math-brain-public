SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T16:23:41Z.
attacking: join diffuse volume exits to high-leverage/low-cross-rank survivors quantitatively while retaining the full spectrum.

# Early substantive checkpoint — high leverage in a physical 3-column cross block

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T162341Z-account03-B08-qform-diffuse-r41`  
Status: worked supporting derivation; full target OPEN.

Let `C in R^{m x 3}` be a literal ORIGINAL-coordinate cross block of the full quadratic form. Assume `rank C=3`, `s3(C)>=gamma>0`, and let `P=C(C^T C)^{-1}C^T` be the projection onto `range(C)`. Suppose a physical row `i` has leverage `ell_i=P_ii>1/2`.

Write `C=U Sigma V^T`, with `U^T U=I_3`, `Sigma=diag(s1,s2,s3)`, and let `u_i` be row `i` of `U`. The Cauchy--Binet volume law on row triples,

`w(S)=det(C[S,:])^2/det(C^T C)`, `|S|=3`,

has inclusion probability `P_w(i in S)=ell_i`. Hence the anchored third-volume

`Z_i=sum_{R subset [m]\{i}, |R|=2} det C[{i} union R,:]^2`

satisfies the exact identity

`Z_i=ell_i det(C^T C)=ell_i (s1 s2 s3)^2`.                      (C1)

The physical row norm obeys

`R_i=||C_{i,*}||_2=||u_i^T Sigma||_2 <= s1 sqrt(ell_i)`.          (C2)

Therefore

`Z_i/R_i >= sqrt(ell_i) s1 s2^2 s3^2 >= gamma^5/sqrt(2)`,       (C3)

so

`2 Z_i/R_i > sqrt(2) gamma^5`.                                   (C4)

Because the right bank has exactly three physical columns, every nonzero 3x3 minor uses every column. Thus `Z_i` is precisely the double-incident anchored third-volume appearing in account03/B08 r28 for ANY choice of physical anchor column. Let `alpha_k=P_w(k in S | i in S)` for `k!=i`; then `sum alpha_k=2`.

If `max_{k!=i} alpha_k <=3/5`, r28's `QFORM-ANCHORED-THREEVOLUME-JENSEN-EXTENSION-v1` with `q=6/5` gives

`||p_Q||_infinity <=25 e sqrt(5/6) (2Z_i/R_i)^(-1/5)`

and (C4) yields

`||p_Q||_infinity <25 e sqrt(5/6) 2^(-1/10) gamma^(-1)`

`=57.8816453581... gamma^(-1) <58/gamma`.                         (C5)

The density is continuous and in `C_0`; the cited theorem retains arbitrary same-bank curvature, outside variables, couplings and induced affine terms.

If this diffuse-secondary gate fails, choose `k!=i` with `alpha_k>3/5`. Under the rank-three projection DPP the pair inclusion probability is

`P_w(i,k in S)=det P[{i,k},{i,k}]=ell_i ell_k-P_ik^2=||u_i wedge u_k||_2^2`.   (C6)

Thus

`||u_i wedge u_k||_2^2=ell_i alpha_k >3/10`.                       (C7)

For the actual physical two-row block `B=C[{i,k},:]`, exterior singular-value monotonicity gives

`E2(B)=||C_{i,*} wedge C_{k,*}||_2^2
      >=(s2 s3)^2 ||u_i wedge u_k||_2^2
      >(3/10) gamma^4`.                                             (C8)

Moreover, for either row anchor and column anchors `r=1,2,3`, the double-incident rank-two masses satisfy

`sum_r Delta_{i r}(B)=2 E2(B)`,                                    (C9)

so some ACTUAL physical column `r` has

`Delta_{i r}(B)>(1/5) gamma^4`.                                   (C10)

Applying the completed exact-rank-two grouped theorem `QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1` to this literal 2x3 block gives the full ambient output an `L^3` density with

`||p_Q||_3 <=3^(2/3)2^(1/3) Delta_{ir}(B)^(-1/6)
           <3^(2/3)2^(1/3)5^(1/6) gamma^(-2/3)
           =3.4270399653... gamma^(-2/3)`.                         (C11)

This is not yet the target `L^infinity` conclusion; it converts failure of the continuous high-leverage exit into a concrete rank-two grouped smoothing resource on two ACTUAL physical rows. The missing implication is to upgrade (C11) to `L^infinity` using the third curvature without assuming a disjoint nonzero square or deleting Schur leakage.

For the r40 high-leverage branch `gamma=L/16`, (C5) becomes `<926.107/L`, and (C11) becomes `<21.761 L^(-2/3)`.

Sources used: account03/B08 r28 at `math-open-problems@af8d585f3ac8b3cc243045caf6bbe65d8e956f99`; exact grouped rank-two theorem at `math-open-problems@c248abc9be918698c6d5a68108c615ba1c4790b3`; current required volume-stability package `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba` supplies the r40 entry into this high-leverage branch.
