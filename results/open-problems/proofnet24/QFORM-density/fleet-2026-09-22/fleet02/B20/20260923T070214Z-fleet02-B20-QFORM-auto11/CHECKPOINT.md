# B20 auto11 substantive checkpoint — rank-two cross near-kernel identity

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: supporting deterministic reduction; full QFORM remains open.

In the exact-rank-three synthesis branch write

`A = R Lambda R^T`, `R^T R = I_3`, `min_j |lambda_j| >= 1`,

and take a full physical partition `I union J`. Put `U=R_I`, `V=R_J`, `G=U^TU`, so `V^TV=I-G`. Assume `rank(U)=3` and the physical cross block `C=U Lambda V^T` has rank two. Then `rank(V)=2`; if `q` is the unit kernel vector of `V`, `Gq=q`.

Let `E=range(U)`, let `P=range(C)`, and let `r` be the unit vector spanning `E cap P^perp`. Put `B=A_II=U Lambda U^T`, and let `s1>=s2>0` be the two nonzero singular values of `C`.

The key identity to prove in the final report is

`(s1 s2)^2 ||Br||^2 = det(Lambda)^2 det(G) pdet(I-G)`.

Sketch of exact algebra: write `r=Ux`. Orthogonality `C^T r=0` implies `V Lambda Gx=0`, hence `Lambda Gx=alpha q`. Since `||Uq||=1`, `Br=alpha Uq` and `||Br||=|alpha|`; normalization gives `alpha^{-2}=q^T Lambda^{-1}G^{-1}Lambda^{-1}q`. On the other hand, identify exterior two-vectors in dimension three by Hodge star. The rank-one map `wedge^2 V^T` has squared norm `pdet(I-G)` and image along `*q`; `wedge^2 Lambda(*q)=det(Lambda)*Lambda^{-1}q`; finally `||wedge^2 U(*v)||^2=det(G) v^TG^{-1}v`. This gives the identity.

Since `C` is a compression of `A`, `s1(C)s2(C) <= s1(A)s2(A) <= |det Lambda|` because `s3(A)>=1`. Hence

`det(G) pdet(I-G) <= ||Br||^2`.

If the designated-partner survivor satisfies `||Br||<sqrt(2)/64`, then, writing the two nontrivial eigenvalues of `G` as `gamma_1,gamma_2 in (0,1)`,

`gamma_1 gamma_2 (1-gamma_1)(1-gamma_2) < 1/2048`.

Therefore for some `j`, `gamma_j(1-gamma_j)<1/(32sqrt(2))`, and so

`min(gamma_j,1-gamma_j) < delta_* := (1-sqrt(1-1/(8sqrt(2))))/2 = 0.02260821845...`.

Thus every still-unpaid exact-rank-three rank-two-cross near-kernel packet has a spectral unit direction carrying more than `0.9773917815` of its squared mass on one physical bank. This is a quantitative near-coloop replacement for the partner's mixed-row debt; it does not assert independence in that spectral direction.
