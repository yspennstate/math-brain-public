# B20 r25 substantive checkpoint — finite-core whitening compiler

Status: PARTIAL CHECKPOINT. Full QFORM remains OPEN.

Fresh designated partner account03/B20 r29 reduces the normalized-heavy exact-rank-three/rank-two-cross chamber to K0 with |K0|<=31 and S0=I-T0. Besides its already-paid branch, its case C has delta0=lambda_min(S0)>=1/64, a set K1 of at most 95 residual original coordinates with S0-whitened leverage >1/32, and every row outside K0 union K1 of whitened leverage <=1/32.

Put u_i=S0^{-1/2}r_i for i outside K0, U1=sum_{K1}u_i u_i^T, UO=sum_{O}u_i u_i^T=I-U1. If lambda_min(UO)>=1/16, then the exact residual physical Gram after conditioning K0 union K1 is

S=S0^{1/2} UO S0^{1/2} >= (1/64)(1/16) I = I/1024.

Moreover each residual original row satisfies

r_i^T S^{-1}r_i=u_i^T UO^{-1}u_i <= (1/32)/(1/16)=1/2.

Writing the exact-rank-three residual quadratic block as Q L Q^T with Q^TQ=I_3 gives s_min(L)>=lambda_min(S)>=1/1024. The pinned Fresnel--Brascamp--Lieb Theorem F therefore applies after conditioning only original core coordinates and gives

||p_Q||_infinity <= 12/lambda_min(S) <= 12288.

If lambda_min(UO)<1/16, choose unit z with z^T UO z<1/16 and set w=S0^{-1/2}z. Since S0<=I, ||w||>=1. For v=w/||w||, the complement O has physical squared spectral mass

v^T (sum_{i in O} r_i r_i^T) v = z^T UO z / ||w||^2 <1/16.

Thus the finite original-coordinate core K0 union K1, of size <=126, carries >15/16 of one spectral direction. This converts the partner's case C either into an explicit <12288 payment or a universal finite-core coloop packet. Next step: combine this with a finite-core rank-three compiler to force an orthogonal core/shell double-coloop in every unpaid HC state.
