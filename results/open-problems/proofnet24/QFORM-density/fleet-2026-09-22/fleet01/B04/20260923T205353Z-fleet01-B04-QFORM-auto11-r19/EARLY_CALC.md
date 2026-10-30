SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T20:53:53Z.
attacking: make the overlap-one third-compound Schur packet rank-free by proving a marginal-free second-compound L^p product-Fourier estimate, then bootstrap it with the dependent physical square.

# Early substantive calculation

Full QFORM status remains OPEN. This calculation stays in original-coordinate product space.

Let two disjoint original-coordinate product banks U,V have arbitrary same-bank quadratic/affine terms and physical cross block N. Put Z_2=E_2(N)=e_2(NN^T)>0.

The preceding B04 exact weighted-subset argument, applied before its final time integration, gives a t^{-1} Fourier estimate for the canonical pair-volume law. If every canonical pair-row marginal is <=1/2, its fixed-cardinality entropy factor satisfies F_2<=sqrt(2), hence

|phi_R(t)| <= min(1, 2^(7/4) pi Z_2^(-1/4) |t|^(-1)).

If a canonical pair row has marginal alpha_1>1/2, physically promote that original scalar coordinate. The exact promotion identity S_1^2 Z_1=alpha_1 Z_2 and the ell=1 estimate give constant 2 pi (alpha_1 Z_2)^(-1/4)<2^(5/4)pi Z_2^(-1/4). If the residual one-volume law again has a row marginal alpha_2>1/2, promote it too; exact rank-two crossing gives 2 pi (alpha_1 alpha_2 Z_2)^(-1/4)<2^(3/2)pi Z_2^(-1/4). Thus the balanced coefficient 2^(7/4) is uniform over all promotion branches.

For p>=2, q=p/(p-1), splitting the q-norm integral at K=2^(7/4)pi Z_2^(-1/4) gives

||phi_R||_q^q <= 2 K p.

Hausdorff-Young therefore yields the candidate rank-free second-compound estimate

||p_R||_p <= (2^(7/4) p)^(1-1/p) Z_2^{-(p-1)/(4p)}.

At p=3,

||p_R||_3 <= 3^(2/3) 2^(7/6) Z_2^(-1/6).

Now take an actual physical pivot h with a=A_hh !=0. After completing the square in the ORIGINAL coordinate X_h, let N be the I-J cross block of the scalar Schur complement. The completed-square variable is a translate of X_h conditional on the residual, hence has conditional density <=1. Feeding the p=3 estimate into QFORM-DEPENDENT-SQUARE-L3-SMOOTHING-v1 gives

||p_Q||_infinity <= sqrt(3) 2^(23/8) |a|^(-1/2) E_2(N)^(-1/8).

For overlap-one third minors, define

M_{1,h}=sum_{|K|=|L|=2, K cap L=empty} det A[{h} union K,{h} union L]^2.

The already-proved Schur identity and random-cut identity are

M_{1,h}=a^2 sum det S_h[K,L]^2,
E_P E_2(S_h[P,P^c])=M_{1,h}/(16a^2).

Hence some physical cut gives the rank-free overlap-one estimate

||p_Q||_infinity <= sqrt(3) 2^(27/8) |a|^(-1/4) M_{1,h}^(-1/8).

This removes the old exact-rank-three hypothesis from the overlap-one Schur packet. The new branch currently proves an essentially bounded density; continuity is not yet claimed from the dependent-square endpoint.

Stress family under calculation: N_e=2I_3+((e-2)/3)J_3, S_e=[[0,N_e],[N_e,0]]. Its singular values are 2,2,e on each bipartite sign pair, while exact disjoint second-compound energy is

D_e=sum_{|K|=|L|=2,K cap L=empty} det S_e[K,L]^2
=(4/9)(e^4+60e^2+16e+144),

which tends to 64 as e->0. This is the intended tiny-third-direction stress test.
