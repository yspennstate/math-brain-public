# Exact checks for QFORM-DETERMINANT-DUAL-RECEIVER-v1

## A. Determinant invariant

For

    B=[[a rho^2,0,b c rho tau],
       [0,0,b sigma tau],
       [b c rho tau,b sigma tau,0]],

expansion along the second row gives

    det B = -(a rho^2)(b sigma tau)^2
          = -a b^2 rho^2 sigma^2 tau^2.

The shear c cancels exactly.

## B. Strict target of the diffuse packet

For a=b=3,c=1,rho=sigma=tau=1,

    B=[[3,0,3],[0,0,3],[3,3,0]].

Its characteristic polynomial is

    p(lambda)=lambda^3-3lambda^2-18lambda+27.

Now

    p(-1)=41>0 and p(lambda)->-infinity as lambda->-infinity,
    p(1)=7>0, p(2)=-13<0,
    p(5)=-13<0, p(6)=27>0.

Because B is real symmetric, all roots are real. The three disjoint sign-change intervals therefore contain its three eigenvalues, proving one eigenvalue <-1, one in (1,2), and one in (5,6). Numerically they are

    -3.740938811..., 1.335125604..., 5.405813207....

Also det B=-27, so J=27 and 12 J^(-1/3)=4.

## C. Physical leverage and local coefficient scale

Take flat orthonormal r,t on a bank K of size m and a flat unit v on disjoint bank L. The range is span{r,t,v}; hence

    <P e_i,e_i>=r_i^2+t_i^2=2/m  for i in K,
    <P e_j,e_j>=v_j^2=1/m        for j in L.

For m>=4 the maximum is <=1/2, exactly the pinned Theorem-F leverage threshold.

For Q=3S^2+6(S+T)V, the K-K block is 3rr^T and the K-L block is 3(r+t)v^T. With r,t,v flat, every physical coefficient has modulus <=6/m. Thus every k x k physical minor has modulus <=(6 sqrt(k)/m)^k by Hadamard.

## D. Full-rank conditional-moment stress family

With epsilon=1/128,

    P1+P2-P3+epsilon(I-P_E)
      = epsilon I +(1-epsilon)P1 +(1-epsilon)P2 -(1+epsilon)P3.

Thus the rank-three Fresnel coefficients are

    127/128, 127/128, -129/128,

and their product modulus is

    D0=(127/128)^2(129/128)=0.9921269416809082....

The block-constant frame has Gram matrix I_3 and physical leverage 1/m. Hence pinned Theorem F applies for every m>=2.

Numerical constants:

    12 D0^(-1/3) = 12.031658545595015...
    (48/5)sqrt(pi)D0^(-1/6) = 17.037987508728477...
    (24sqrt(2)/5)D0^(-1/6) = 6.797173590183264....

All statements above are deterministic coefficient checks; no probabilistic rotation is used.
