# fleet02/B12 r36 — substantive checkpoint

Status: supporting theorem in progress; full QFORM remains OPEN.

First unpaid implication attacked: fleet03/B12 r35 proves a spectral-square spill theorem but its leverage-free D5 closure needs a 7-mode carrier because two self-block directions are spent before 5 cross directions survive. I try to recover the missing sixth carrier mode by paying the intermediate rank-two self-block regime with an ORIGINAL-coordinate physical pair.

Let H be an original-coordinate set of size m, C=A[H,H], B=A[H,H^c], and suppose 0<=G<=A^2 with lambda_6(G[H,H])>=g^2. Let N=binom(m,2). Fix 0<a<b/N and b<g.

Three exhaustive regimes:

1. If s3(C)>=a, the completed finite physical receiver used by fleet03/B12 gives ||p_Q||inf <= 2sqrt(6 pi m)/a after conditioning only outside H.

2. If s3(C)<a but s2(C)<b, apply fleet03/B12 r35 spectral-square spill with k=6,r=1: s5(B)>=sqrt(g^2-s2(C)^2)>sqrt(g^2-b^2). The completed e5f71d79... D5 theorem therefore gives

   ||p_Q||inf <= 5sqrt(2e)/sqrt(g^2-b^2).

3. If s3(C)<a<=s2(C), truncate C to its top two signed eigenmodes C2=lambda1 uu^T+lambda2 vv^T and write C=C2+E, ||E||=s3(C)<a. Since sum_{i<j}(u_i v_j-u_j v_i)^2=1, some original-coordinate pair I={i,j} has squared Pluecker weight >=1/N. For K=C2[I,I],

   |det K|=|lambda1 lambda2|(u_i v_j-u_j v_i)^2 >= s1(C)s2(C)/N,
   ||K||op<=s1(C),

so sigma_min(K)>=s2(C)/N>=b/N. Weyl on the actual pair C[I,I]=K+E[I,I] gives

   sigma_min(C[I,I]) >= kappa := b/N-a >0.

If this pair is definite, conditioning outside I and completing the square gives the elementary 2D bound ||p_Q||inf<=pi/kappa. If it is indefinite, the full-matrix physical-pair theorem at math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc gives, for s=s3(A),

   ||p_Q||inf <= 3*400^(1/3)*(D^2*kappa*s)^(-1/6)
               <= 3*400^(1/3)*kappa^(-5/6)*s^(-1/6),

because |det C[I,I]|=D>=kappa^2.

Thus six spectral-square carrier modes already close, with an explicit finite constant, without a cross-range leverage assumption. This lowers the partner r35 leverage-free carrier count from 7 to 6. All statements concern the ACTUAL final matrix; no small operator-norm matrix is treated as a small random quadratic error and no spectral rotation is used probabilistically.

Remaining gap: the owner target supplies only three global large eigenvalues, not six spectral-square carrier modes on a bounded original-coordinate H. The structural carrier-or-grouped/diffuse/hub fallback remains unpaid.