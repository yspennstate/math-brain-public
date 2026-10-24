# B04 r30 substantive checkpoint: soft-ridge control of third-volume marginals

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains open.

Let M be an original-coordinate cross block with squared singular values lambda_1>=lambda_2>=...>=0, T2=sum_{j>=3} lambda_j>0, E_k=e_k(lambda), and let W be the exact row third-volume marginal matrix from the fractional-volume theorem, so alpha_i=W_ii and in an SVD basis

p_j=lambda_j e_2(lambda without j)/E_3,
W=U diag(p_j) U^T.

Account01/B20 proved T2 E2 <= 3 E3. Therefore

p_j <= min(1, lambda_j E2/E3) <= min(1, 3 lambda_j/T2).

For every theta>0 and every x>=0,

min(1,3x/T2) <= (1+3theta) x/(x+theta T2).

Indeed, for x<=T2/3 this reduces to 3x<=T2, and for x>=T2/3 it reduces to T2<=3x. Hence, with

K_theta = M M^T (M M^T + theta T2 I)^(-1),

we have the operator inequality

W <= (1+3theta) K_theta.

Thus if L_theta=max_i (K_theta)_ii and A_theta=(1+3theta)L_theta<3/4, then every volume marginal satisfies alpha_i<=A_theta. Taking q=max(1,2A_theta)<3/2 in the completed q-dependent third-volume product-Fourier theorem yields a continuous C0 density and

||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] E3(M)^(-1/6),

with arbitrary within-bank quadratic terms, outside couplings and affine terms preserved. In particular if A_theta<=1/2 then

||p_Q||_infinity <= 3e E3(M)^(-1/6).

This is a soft-ridge certificate: it can succeed even when every orthogonal projection P satisfying the previous residual-op-norm gate is forced to be P=I and therefore has leverage one.

Next: verify an explicit dense indefinite family where the hard projection certificate fails for every P but this soft-ridge certificate gives q=1, then publish the complete proof and exact constants.
