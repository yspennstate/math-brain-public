# account02/B10 checkpoint — true-near-coloop geometry

Programme: QFORM-DENSITY-3EIG-20260922. Full theorem remains OPEN.

Fresh owner control: math-research-brain@1fe4828112f08195f6f1f912b64c12e827853e66, OWNER CONTROL revision 2026-09-22.15. Required Claude source used: math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837. Designated partner used: account03/B10 report math-open-problems@46df88a3c81ee860e09a67bc8193514c26281555, which pays the entire small-Pluecker collar with hub leverage c<=63/64 and leaves only the true-near-coloop collar c>63/64, |q|<1/16.

## First unpaid implication attacked

Write the exact-rank-three Parseval form in a spectral basis adapted to the surviving physical hub:

r_0=sqrt(c)e,  c>63/64,  rho=1-c,
M=[[q,b^T],[b,C]],  q=e^T M e,
r_j=s_j e+w_j,  w_j perpendicular e  (j!=0).

Parseval gives

sum_j s_j^2=rho,   sum_j s_j w_j=0,   sum_j w_j w_j^T=I_2.

The physical hub cross coefficient is

A_0j=sqrt(c)(q s_j+b^T w_j).

Therefore the entire residual star has the exact product-coordinate energy identity

sum_(j!=0) A_0j^2 = c(q^2 rho+||b||^2).                      (1)

There is no cancellation between the longitudinal leakage q s and the transverse field b.W: their coefficient vectors are orthogonal because sum s_j w_j=0.

Since every eigenvalue of the exact 3x3 spectral matrix M has modulus >=1, sigma_min(M)>=1, hence

q^2+||b||^2=||Me||^2>=1.

Combining with (1),

sum_(j!=0) A_0j^2 >= c(1-c q^2).                              (2)

In the partner survivor c>63/64, |q|<1/16, so

sum_(j!=0) A_0j^2 > (63/64)(255/256)=16065/16384 >0.9807.      (3)

Thus the true-near-coloop obstruction is NOT a weak-star regime: the hub retains a uniformly order-one cross field even as rho->0 and q->0. The unpaid issue is to exploit that strong field jointly with residual curvature without conditioning away product provenance.

If the preceding partner transverse-heavy exit has not fired, then h_j=||w_j||^2<1/4 for every residual row. Put a_j=q s_j+b^T w_j and B=||b||. Since B>=sqrt(1-q^2), |s_j|<=sqrt(rho),

|a_j|/sqrt(sum a_k^2) <= [B/2+|q|sqrt(rho)]/sqrt(B^2+q^2 rho).

For c>63/64 and |q|<1/16 the ratio |q|sqrt(rho)/B is <1/(8 sqrt(255)), so every normalized star coefficient has squared leverage <0.259. Hence the strong star itself is diffuse across residual ORIGINAL coordinates in the still-unpaid collar.

Next step in this run: build a target-valid true-near-coloop family satisfying these collar hypotheses and test whether the raw scalar square-peel can interpolate to the already-paid exact-null endpoint. The newest ruled-surface theorem will be used as a real control inequality, not rederived.
