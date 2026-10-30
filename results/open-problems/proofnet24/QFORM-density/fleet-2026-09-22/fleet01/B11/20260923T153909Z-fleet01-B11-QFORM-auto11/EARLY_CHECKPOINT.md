SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T15:39:09Z.
attacking: scalar completion plus a bounded-density Schur remainder, using the newest volume-stability exit to pay a higher-rank opposite-sign branch without false independence.

# Early substantive checkpoint: square-over-bounded-remainder compiler

Let X0 be independent of Z, with density f0<=1. Suppose

Q = a X0^2 + 2 X0 b^T Z + Z^T D Z + ell0 X0 + ell^T Z + c,   a!=0.

Completing the scalar square gives the exact identity

Q = a (X0 + m(Z))^2 + R(Z),

where

m(Z)=(b^T Z+ell0/2)/a

and R is the full Schur-complement quadratic-plus-affine remainder. For every deterministic shift m, the pushforward of a(X0+m)^2 has density bounded by

|a|^{-1/2}|y|^{-1/2}.

Therefore, without asserting any independence between the shifted square and R,

p_Q(t) <= |a|^{-1/2} E |t-R|^{-1/2}.

If R has a density bounded by K, then for every rho>0,

E|t-R|^{-1/2}
 <= K integral_{|u|<=rho}|u|^{-1/2}du + rho^{-1/2}
 = 4K sqrt(rho)+rho^{-1/2}.

Optimizing at sqrt(rho)=1/(2sqrt(K)) gives

sup_t E|t-R|^{-1/2} <= 4sqrt(K),

hence

||p_Q||_infty <= 4 sqrt(K/|a|).                     (EC.1)

Actual newest-Claude application: if the Schur remainder R has an ORIGINAL-coordinate cross block satisfying the volume-stability hypotheses of math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba, namely M=M0+E with s3(M0)>=c0, max diag(P_range(M0))<=1/2 and ||E||op<=c0/16, then R has a continuous density with K<23/c0. Equation (EC.1) yields the higher-rank scalar-pivot branch

||p_Q||_infty < 4 sqrt(23/(|a| c0)).                 (EC.2)

This is essential boundedness for Q; continuity of Q is not claimed because the shift m(Z) is correlated with R and f0 may be fragmented.

Next: package the exact constant from the sharp volume theorem, apply the designated fleet02/B11 bound to a genuinely cross-coupled scalar extension, and verify a target-valid diffuse-Schur family.
