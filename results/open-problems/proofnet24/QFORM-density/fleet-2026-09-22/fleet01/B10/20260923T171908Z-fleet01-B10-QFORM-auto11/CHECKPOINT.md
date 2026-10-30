# Early substantive checkpoint — disjoint transverse-pair / leaf-triple packing

In the current exact-rank-three near-coloop notation, write `u_0=sqrt(h) r`, `u_i=t_i r+p_i`, with `p_i in r^perp`, `sum_i p_i p_i^T=I_2`, and assume the already-isolated diffuse transverse gate `tau_i=||p_i||^2<1/4` for every leaf. Let `G_L=sum_i u_i u_i^T=I-h rr^T`, hence `det G_L=1-h`.

For a leaf set `I`, put `S_I=sum_{i in I}p_i p_i^T`; for its complement bank `J`, put `G_J=sum_{j in J}u_j u_j^T`. Independently put every leaf into `I` with probability `p=2/5` and into `J` otherwise. Cauchy--Binet gives

`det S_I=sum_{a<b in I} det(p_a,p_b)^2`,
`det G_J=sum_{c<d<e in J} det(u_c,u_d,u_e)^2`.

For a fixed triple `T={c,d,e}`, the transverse pair mass avoiding `T` is exactly

`sum_{a<b, a,b notin T} det(p_a,p_b)^2 = det(I_2-S_T)`,
`S_T=sum_{i in T}p_i p_i^T`.

Since `S_T>=0` and `tr S_T=sum_{i in T}tau_i<3/4`,

`det(I_2-S_T)=1-tr S_T+det S_T>1/4`.

A disjoint pair lands in `I` and the triple lands in `J` with probability

`p^2(1-p)^3=(2/5)^2(3/5)^3=108/3125`.

Therefore

`E[det S_I det G_J] > (108/3125)(1/4) sum_T det(u_T)^2`
` = (27/3125) det G_L`
` = (27/3125)(1-h)`.

Hence some deterministic ORIGINAL-coordinate split satisfies

`det S_I det G_J > (27/3125)(1-h)`.

Now apply the completed designated-partner fleet02/B10 exact factorization

`V_3 = h (det M)^2 det(S_I) det(G_J)`

from commit `144e391e6a0aed00bb8ded766cf5609d88d260b2`. With `D=|det M|`, this yields the actual inequality

`V_3 > (27/3125) h D^2 (1-h)`.

The completed row-marginal-free one-hub theorem can therefore pay every punctured diffuse-transverse state, with a constant deteriorating only as `[hD^2(1-h)]^(-1/6)`. The remaining universal issue is the ultra-coloop limit, not the near-null Rayleigh scalar itself. Full QFORM remains open.