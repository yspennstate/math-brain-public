SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-23T01:34:01Z.
attacking: generalize the exact-rank-three physical-cross-block L1 Fourier theorem to every exact physical cross rank r>=3, then splice it with fleet02/B02's ungated D5 tail theorem and the prior clustered-pair exterior identity.

# Early substantive checkpoint

Let I,J,W be disjoint original-coordinate banks and condition on X_W. Suppose M=A[I,J] has exact rank r>=3, thin SVD M=U Sigma V^T, and Gamma_r=prod_{k=1}^r sigma_k>0. For the twisted projected amplitudes a_t,b_t on the r-dimensional singular subspaces, the Livshyts-Paouris-Pivovarov product-marginal theorem gives projected-density caps M_L,M_R<=2^(r/2), hence ||a_t||_2||b_t||_2<=(M_L M_R)^(1/2). Bilinear Plancherel yields

|phi_Q(t)| <= min{1, pi^(r/2)(M_L M_R)^(1/2) Gamma_r^(-1/2)|t|^(-r/2)}.

Therefore

int_R |phi_Q(t)| dt <= [2 pi r/(r-2)] (M_L M_R)^(1/r) Gamma_r^(-1/r)

and

||p_Q||_infinity <= [r/(r-2)] (M_L M_R)^(1/r) Gamma_r^(-1/r)
                 <= [2r/(r-2)] Gamma_r^(-1/r).

This extends the completed fleet03/B02 r17 exact-rank-three theorem (which is exactly the r=3 case) to all exact physical cross ranks r>=3, retains arbitrary same-bank quadratic phases/outside couplings, and proves a continuous density on this branch.

Concrete new application to fleet01/B02 r18's clustered order-three volume branch: for clustered physical pair H={i,j}, Delta^2 L>=3Z3/8, where L=||N_H||_F^2. If the projected transverse packet N_H has exact rank two, write R=sr(N_H) in (1,2]. Then e2(N_H^T N_H)=L^2(R-1)/R^2 and rank(M)=4. Hence

Z4=Gamma_4^2 >= Delta^2 e2(N_H^T N_H)
   >= (3/8) Z3 L (R-1)/R^2.

The r=4 theorem gives the true unweighted Fourier estimate

int |phi_Q| <= 8 pi [(3/8)Z3 L (R-1)/R^2]^(-1/8)

and continuous-density bound

||p_Q||_infinity <=4[(3/8)Z3 L (R-1)/R^2]^(-1/8).

Thus the previously unpaid exact transverse-rank-two collar is Fourier-paid whenever its distance from rank one is quantified. For R>=3/2 this becomes

||p_Q||_infinity <=4*12^(1/8)(Z3 L)^(-1/8)<5.458 (Z3 L)^(-1/8),
int|phi_Q|<34.288 (Z3 L)^(-1/8).

The remaining limit R downarrow1 is a genuine near-rank-one transverse interpolation problem; at the exact endpoint rank(N_H)=1 the full cross block has exact rank three and the r=3 theorem gives int|phi_Q|<=12pi Z3^(-1/6), ||p_Q||<=6Z3^(-1/6).

Partner application to incorporate in the final report: fleet02/B02 r19 gives the ungated D5 tail bound when R_tail=T/s_3(M)^2>2; combine that completed inequality with the exact-rank theorem to isolate the surviving Fourier collar to higher-rank, low-tail-stable-rank/near-rank-one geometry rather than all sr(N)<5/2.
