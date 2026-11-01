# Early checkpoint — kernel-cofactor routing at the rank-two center endpoint

Programme: QFORM-DENSITY-3EIG-20260922. Slot: fleet02/B01. Run: 20260923T071338Z-fleet02-B01-qform-auto12.

Work in the source-valid three-original-coordinate packet of the latest fleet03/B01 receiver. Let `B=B^T` be the 3x3 physical center block, `K` the 3xm cross block with rank 2, `v` a unit generator of `ker K^T`, and `Delta=sigma_1(K)sigma_2(K)`. The partner's intrinsic unpaid endpoint is `d=g=0`, equivalently `Bv=0`.

At this endpoint there is an exact synchronization identity. Put `c=pdet(B)` when `rank B=2` and `c=0` when `rank B<=1`. For deletion of physical coordinate `k`, write `B_hatk` for the remaining 2x2 principal block and `K_hatk` for the remaining two rows. Since

`adj(B)=c vv^T`, `adj(KK^T)=Delta^2 vv^T`,

we have simultaneously

`det(B_hatk)=c v_k^2`,
`det(K_hatk K_hatk^T)=Delta^2 v_k^2`.

Hence one and the same deletion `k0` with `v_k0^2>=1/3` satisfies

`|det B_hatk0|>=|c|/3`,
`sqrt(det(K_hatk0 K_hatk0^T))>=Delta/sqrt(3)`.

This already routes the endpoint if `|c|` is not tiny, using the completed determinant-only physical-pair theorem. If `|c|` is tiny, the same physical pair still carries a fixed fraction of the entire rank-two cross area; the remaining issue is how to spend that area without assuming the outside self block is diagonal.

A concrete strict-N3 target family sits exactly on this interface. Let

`v=(1,1,1)/sqrt(3)`, `u1=(1,-1,0)/sqrt(2)`, `u2=(1,1,-2)/sqrt(6)`, `U=[u1 u2]`.
For even `m`, choose an `m x 2` orthonormal-column matrix `V_m` whose rows all have squared norm `2/m`, set `K=U V_m^T`, and

`B_{eps,delta}=eps u1 u1^T + delta v v^T`,
`A=[[B_{eps,delta},K],[K^T,0]]`.

The nonzero spectrum is `{(eps+sqrt(eps^2+4))/2, (eps-sqrt(eps^2+4))/2, 1, -1, delta}`, so for every `eps>=0, delta>=0` there are at least three eigenvalues of absolute value at least 1. For small `eps,delta` and large `m`, all physical diagonals and all physical 2x2 determinants are arbitrarily small. The partner packet has `Delta=1`, `d=delta`, `g=0`, so its logarithmic bound grows like `log(1/delta)` as `delta->0`.

By contrast the newest Fresnel/Brascamp-Lieb hub theorem applied to any two center coordinates after deleting one index has `Gamma=sqrt(det(K_hatk K_hatk^T))=1/sqrt(3)` and leaf leverage `2/m<=1/2`. It gives the uniform target-level estimate

`||p_{X^T A X}||_inf <= 4 Gamma^{-1/2} = 4*3^(1/4) < 5.265`,

for every cap-one product law, uniformly in `m,eps,delta`. Thus paying the nonzero local `d` before routing to the two-hub packet is provably the wrong proof currency on this exact target family.

Full proof and exact scope will follow in REPORT.md. Full QFORM remains open.
