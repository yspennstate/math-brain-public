# QFORM-PROJECTED-2HUB-MARGINAL-FREE-TRANSVERSE-v1

Run 20260924T222046Z-account03-B06-fixedmult-r69.

Let X_H and X_L be independent original-coordinate product vectors with scalar density caps one. Assume the exact H-to-L crossblock has rank two, B=UM with U^T U=I_2. Split L=P disjoint_union J. Assume M_J has rank two and put S=s_1(M_J)s_2(M_J). Let Pi project onto row(M_J), C=A_{P,J}(I-Pi), F=||C||_F.

If F>0, the full quadratic-plus-affine output has a C_0 density and

||p_Q||_infinity <= 3 e 2^(1/6) (S F)^(-1/3) < 9.154 (S F)^(-1/3).

All internal same-bank quadratic terms and affine terms are arbitrary.

Proof. Write c_p for the rows of C.

If every ||c_p||^2<=F^2/2, use the grouped projected-crossing theorem (NEW_PROJECTED_CROSSING.md at commit 829192412f2a2d84e72b4bed91115fc5fab68401) with k=2, ell=1. The projected hub W=U^T X_H has density cap <=e by the product-projection theorem in the five-eigenvalue paper. Thus

||p_Q||_infinity
 <=3*2^(5/6)e^(1/3)(S F)^(-1/3)
 =7.460095923... (S F)^(-1/3).

Otherwise choose a literal p in P with ||c_p||>F/sqrt(2), and condition on all coordinates in P except p. The remaining source banks H union {p} and J are independent original-coordinate product banks. The crossing is

T=[U M_J; a_p],  a_p=A_{p,J}.

Let T0=[M_J;a_p] and L0=diag(U,1). Then T=L0 T0 and L0^T L0=I_3, so T and T0 have the same nonzero singular values. Since c_p=a_p(I-Pi), the Gram Schur complement gives

det(T0 T0^T)=det(M_J M_J^T)||c_p||^2=S^2||c_p||^2.

Hence T has exact rank three and singular-product P3=S||c_p||>S F/sqrt(2).

The exact-rank-three crossing theorem from the same source applies after conditioning; arbitrary internal functions are allowed. Each three-dimensional orthogonal projection of a cap-one product bank has density cap <=e^(3/2). Therefore

||p_(Q | conditioned)||_infinity
 <=3(e^3/P3)^(1/3)
 <3e2^(1/6)(S F)^(-1/3).

The envelope is uniform and integrable, so averaging yields the same unconditional cap and a C_0 density. Since the heavy-row constant dominates the diffuse one, the theorem follows.

The proof aggregates F^2=sum_p ||c_p||^2 before any reciprocal payment. Diffuse mass is spent by weighted Fourier integration; concentrated mass is promoted into a literal third crossing direction. No fiber supremum is used.
