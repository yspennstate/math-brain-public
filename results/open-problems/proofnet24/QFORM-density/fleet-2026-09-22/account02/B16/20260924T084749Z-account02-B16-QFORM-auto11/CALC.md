# Early calculation — shared-bank projected square + fresh projected hyperbola

Programme: QFORM-DENSITY-3EIG-20260922  
Account/slot: account02/B16  
Run: 20260924T084749Z-account02-B16-QFORM-auto11

First unpaid implication: `QFORM-SHAREDBANK-HEAVYLEVERAGE-OR-NONSEPARABLE-CURVATURE-v1`.

Let I,J be disjoint original-coordinate product banks. On I put S=r^T X_I and U=u^T X_I, with G=[[||r||^2,<r,u>],[<r,u>,||u||^2]]>0 and row leverages c_i=(r_i,u_i)G^{-1}(r_i,u_i)^T<=1/2. On J put V=v^T X_J, tau=||v||>0. Consider the core

Q=a(S+d)^2+2b(U+alpha)(V+beta)+ diagonal-original-coordinate twists on I + arbitrary J-only phase/conditioning terms,

with a b !=0. The scalar projection theorem gives ||p_V||_infty<=sqrt(2)/tau; this is only a marginal cap, not independence created by projection.

Fresnel-linearise the S-square and push the J complex measure to V. Its Radon-Nikodym density H_t(v) obeys |H_t(v)|<=p_V(v). After y=2btv,

|phi_Q(t)| <= N (2|bt|)^{-1}(4 pi |a t|)^{-1/2} I_t,
N=||p_V||_infty,

where

I_t = int_{R^2} prod_{i in I} |g_i^(r_i z+u_i y+shift_i)| dz dy.

The pinned twisted-characteristic-function estimate int |g^|^p <=4 pi/sqrt(p), p>=2, plus geometric Brascamp-Lieb for the frame rows (r_i,u_i) yields

I_t <= (4 pi)^2 det(G)^(-1/2).

Hence

|phi_Q(t)| <= [N (4 pi)^(3/2)/(2 |b| |a|^(1/2) det(G)^(1/2))] |t|^(-3/2).

Integrating min(1,K|t|^(-3/2)) gives 6K^(2/3), therefore

||p_Q||_infty <= 12*2^(-2/3) N^(2/3) (|a| b^2 det G)^(-1/3).

Using N<=sqrt(2)/tau,

||p_Q||_infty <= 12*2^(-1/3) [|a| b^2 det(G) tau^2]^(-1/3)
=9.5244063118... [|a| b^2 det(G) tau^2]^(-1/3).

For orthonormal Walsh r,u on m>=4 shared leaves and flat unit v on a disjoint bank, Q=S^2+2UV has exact nonzero spectrum {1,1,-1}, c_i=2/m<=1/2, det G=tau=1, and thus ||p_Q||_infty<9.525. The pinned ruled one-sheet theorem separately gives p_Q(s)<=pi sqrt(2)<4.443 for a.e. s>=0. No projected independence is used.

This pays the latest account03/B16 shared-bank gap whenever the overlap two-frame is diffuse. What remains is heavy leverage in that overlap frame or additional non-diagonal/nonseparable same-bank curvature that prevents the original-coordinate factorisation above.
