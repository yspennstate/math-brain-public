SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-23T22:38:22Z.
attacking: the innovation-free shared-square / punctured ultracoloop collar by extracting a source-valid projected-crossing currency that is independent of the Rayleigh pivot.

# Early calculation — exact cut currency in the true-near-coloop chamber

Full QFORM remains OPEN. This note is a supporting calculation, not a full solution.

Work in the exact-rank-three near-coloop coordinates from account03/B16: `Lambda=[[a,b,0],[b,u,v],[0,v,w]]`, hub row `sqrt(c)e_1`, `delta=1-c`, leaf row matrix `E=(s,p,q)` with

`E^T E=diag(delta,1,1)`, `p_i^2+q_i^2<1/64`, and `D=|det Lambda|>=1`.

The hub-to-leaf crossing vector is

`m=sqrt(c) E g`, where `g=Lambda e_1=(a,b,0)^T`.

For ANY partition of the leaf indices into `I disjoint_union J`, let

`G_I=E_I^T E_I`, `G_J=E_J^T E_J`,
`B=A_(I,J)=E_I Lambda E_J^T`,
`m_J=sqrt(c) E_J g`,
`C=B(I-P_(m_J))`,
`S^2=||m_J||_2^2`, and `Z_2=e_2(CC^T)`.

Whenever the right side is positive (and hence `m_J!=0`, `rank C=2`), the exact identity is

`boxed: S^2 Z_2 = c D^2 det(G_J) det(T_I),`

where `T_I=[[sum_I p_i^2,sum_I p_i q_i],[sum_I p_i q_i,sum_I q_i^2]]` is the transverse `2x2` Gram on `I`.

Proof: `H_J=E_J^T(I-P_(m_J))E_J=G_J-G_J g g^T G_J/(g^T G_J g)`. For invertible `G_I,G_J`, `adj(H_J)=det(G_J) g g^T/(g^T G_J g)`. Since `CC^T` has the same two nonzero eigenvalues as `G_I^(1/2) Lambda H_J Lambda G_I^(1/2)`, the rank-two adjugate identity gives

`Z_2=det(G_I)D^2 det(G_J)/(g^T G_J g) * g^T Lambda^(-1)G_I^(-1)Lambda^(-1)g`.

But `Lambda^(-1)g=e_1`, while `S^2=c g^T G_J g`; hence

`S^2Z_2=cD^2 det(G_J) det(G_I)(G_I^(-1))_11
       =cD^2 det(G_J)det(T_I)`.

The formula extends to singular `G_I` by continuity (both sides are polynomial after multiplying out the projection identity on the positive branch).

A deterministic good partition exists. Put each leaf index into `I` independently with probability `q_0=2/5`, and into `J` otherwise. By Cauchy--Binet,

`det(T_I)=sum_(|S|=2,S subset I) d_S`, `sum_S d_S=1`,
`det(G_J)=sum_(|T|=3,T subset J) tau_T`, `sum_T tau_T=delta`.

For a fixed triple `T`, the total transverse pair-minor mass meeting `T` is at most `sum_(i in T)(p_i^2+q_i^2)<3/64`, because for a Parseval two-frame `sum_(S contains i)d_S=p_i^2+q_i^2`. Therefore the disjoint pair mass is `>61/64`, and

`E[det(T_I)det(G_J)]
 > (2/5)^2(3/5)^3(61/64) delta
 = (1647/50000) delta
 =0.03294 delta.`

Hence some partition satisfies

`det(T_I)det(G_J) >= kappa_0 delta`, `kappa_0=1647/50000`.

Moreover `G_J <= diag(delta,1,1)` in Loewner order, so `det(G_J)<=delta`; consequently `det(T_I)>=kappa_0`. Since `T_I<=I_2`, `lambda_min(T_I)>=det(T_I)>=kappa_0`. The row-volume marginal of the residual rank-two crossing `C` at row `i in I` is exactly the leverage of `(p_I,q_I)`, because `range(C)=range([p_I,q_I])`; hence

`alpha_i=(p_i,q_i)T_I^(-1)(p_i,q_i)^T
        < (1/64)/kappa_0
        =50000/(64*1647)
        =0.474347... <1/2.`

Thus every hypothesis of the pinned grouped-hub projected-crossing theorem is met with `k=1, ell=2`, hub density cap `M_H<=1`, and

`S^2 Z_2 >= c kappa_0 delta D^2`.

Using its exact constant `3*2^(7/6)*exp(1/3)` gives the new branch estimate

`boxed: ||p_Q||_infinity
 <=3*2^(7/6)*exp(1/3) (c kappa_0 delta D^2)^(-1/6)
 <16.61 (c delta D^2)^(-1/6).`

The same Fourier majorant is `L^1`, so this branch has a continuous `C_0` density.

This estimate is independent of the Rayleigh pivot `a`. Combined with the existing account03/B16 punctured estimate `4 sqrt(2e)c^(-1/2)(|a|D)^(-1/4)`, it pays every near-coloop point for which either `delta D^2` or `|a|D` has a quantitative lower bound. The still-unpaid endpoint is therefore sharper: `a!=0` with BOTH `|a|D ->0` and `delta D^2 ->0`, plus the already-known source-overlap issue. At `a=0` the completed zero-pivot theorem remains uniformly bounded `<7.6`.
