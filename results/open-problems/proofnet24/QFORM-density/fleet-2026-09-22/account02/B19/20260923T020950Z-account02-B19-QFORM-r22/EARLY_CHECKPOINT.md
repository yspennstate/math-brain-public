SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T02:09:50Z.
attacking: the first unpaid O3 two-internal-rank-two routing gate by combining the newest Claude Fresnel theorem with the designated partner's grouped 2+1 payment at its actual scale.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: supporting derivation in progress; full target open.

Let an exact-rank-three target core be written

`A = R M R^T`, `R^T R=I_3`, `M=M^T`, `s_min(M)>=1`,

and write the physical spectral rows as `u_i=R^T e_i`. For two disjoint original-coordinate banks `G,H`, set

`S_G=sum_(i in G) u_i u_i^T`, `S_H=sum_(i in H) u_i u_i^T`.

Assume both have rank two. Let `g,h` be their least positive eigenvalues and `n_G,n_H` unit kernel normals; set

`eta=1-(n_G^T n_H)^2`.

The first calculation is the exact lower determinant identity

`det(g(I-n_G n_G^T)+h(I-n_H n_H^T))=(g+h)gh eta`.

Since `S_G>=g(I-n_Gn_G^T)` and `S_H>=h(I-n_Hn_H^T)`, whenever `eta>0`,

`det(S_G+S_H)>=(g+h)gh eta`.

Moreover if every row is internally diffuse in its own bank,

`u_i^T S_G^+ u_i<=1/2` on `G`, and `u_i^T S_H^+u_i<=1/2` on `H`,

then every row has leverage at most `1/2` in the combined Gram `S=S_G+S_H`: for `u in range(S_G)`,

`u^T S^{-1}u = sup_x(2u^Tx-x^TSx) <= sup_x(2u^Tx-x^TS_Gx)=u^T S_G^+u`,

and similarly for `H`. Therefore Claude's completed Fresnel--Brascamp--Lieb Theorem F applies to the ORIGINAL active coordinates after conditioning outside `G union H`, giving

`||p_Q||_infinity <=12 [|det M| det(S_G+S_H)]^(-1/3)
 <=12[(g+h)gh eta]^(-1/3)`.

In particular `g,h>=1/3` and `eta>=1/4` imply `||p_Q||_infinity<45.358`.

Second calculation, intended to cover the complementary physical-row exit: for a rank-two bank `G`, choose `W` with `WW^T=S_G` and a physical row `u_i`, `i notin G`; put `L_i=[u_i,W]` and `delta_i=det(L_i)^2`. Because `L_iL_i^T<=I`, `s_min(L_i)>=sqrt(delta_i)`. Hence for `B_i=L_i^TML_i`,

`s_min(B_i)>=delta_i`, `|det B_i|>=delta_i`.

The designated partner account03/B19 r21 split can therefore be rerun at scale `delta_i`: its near-null scalar branch plus the completed cross-transverse theorem is at most `83.707 delta_i^(-1/3)`, while its non-small scalar branch plus the orientation-free rank-two half-Riesz theorem is at most `104.217 delta_i^(-1/2)`. Thus for `0<delta_i<=1`,

`||p_Q||_infinity <105 delta_i^(-1/2)`.

The exact packet identity is

`delta_i=pdet(S_G)(n_G^T u_i)^2`,

and summing over `i in H` yields

`sum_(i in H) delta_i=pdet(S_G)n_G^TS_Hn_G >= g^2 h eta`.

So the two-rank-two gate has a rigorous diffuse whole-bank payment and a rigorous single-transverse-row payment. The remaining obstruction after these two exits is aggregate transverse mass spread over many individually small rows and/or nearly parallel kernel planes, plus the separate arbitrary-extra-spectrum descent.

Primary sources actually used at equations: Claude Theorem F at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`; account03/B19 r21 at `4b6025f5928ab6a35f3637965dd4639768c76087`; cross-transverse theorem at `8d262d18e5581cd02b8ea8be5102aa2a6d30ddd7`; rank-two half-Riesz theorem at `e542b1a6ef471b329e4e88a6553e1aacb45acc1a`.
