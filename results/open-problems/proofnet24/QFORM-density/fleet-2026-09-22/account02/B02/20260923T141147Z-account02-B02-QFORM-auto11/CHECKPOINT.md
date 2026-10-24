SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T14:11:47Z.
attacking: QFORM-SECONDANCHOR-LOWSTABLERANK-RECEIVER-v1 by combining physical-anchor Plancherel endpoints with sharp-HY exterior-volume estimates and the account03/B02 heavy-anchor packet.

# Early mathematical checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

From account03/B02 r30 plus account02/B02 r12, the live two-sided heavy-star/transport-failure branch produces a physical cross block B with Z=E3(B)>0 and either an invertible physical 2x2 anchor P, D=|det P|, algebraic cross-Schur residual S, and G=D^2||S||_F^2>Z/24; or a rank-one second anchor that yields a genuine scalar pivot p and residual S1 with H=p^2 E2(S1)>Z/24.

## Physical 2x2 cross-anchor endpoint

For every t!=0,

    |phi_Q(t)| <= pi D^(-1/2)|t|^(-1).                       (A)

Condition on every original coordinate except the two row-anchor coordinates x and two column-anchor coordinates y. The conditional phase is F(x)+2x^T P y+G(y), with arbitrary real F,G. The amplitudes alpha=f_H exp(itF), beta=f_K exp(itG) satisfy ||alpha||_2,||beta||_2<=1. Plancherel for the bilinear Fourier kernel gives (A), uniformly in the conditioning. No scalar stationary-phase decay or post-rotation independence is used.

## Stable-rank lower bound for E3

Let x_j=s_j(S)^2, T=sum x_j=||S||_F^2 and rho=T/max x_j. For rho>2,

    E3(S) >= c3(rho) T^3,

    c3(rho)=(rho-2)/rho^3  for 2<rho<=3,
    c3(rho)=1/27           for rho>=3.                        (B)

Normalize y_j=x_j/T, so sum y_j=1 and y_j<=1/rho. For fixed y_i+y_j, e3(y)=y_i y_j A+(y_i+y_j)B+C with A>=0, hence is concave under pairwise mass transfer. A minimum on the capped simplex is therefore at a vertex: all but at most one entries are 0 or 1/rho. This yields (B). In particular rho>=5/2 implies c3>=4/125.

## D5 interpolation, with exact anchor cancellation

The reviewed sharp-Hausdorff--Young k=5,q=2 calculation gives

    |phi_Q(t)| <= min(1,
      e^(5/4)2^(-5/8)pi^(5/4) E5(B)^(-1/8)|t|^(-5/4)).       (C)

The same fixed 2x2 anchor gives

    E5(B)>=D^2 E3(S)>=c3(rho)G^3/D^4.                         (D)

Combining (A),(C),(D) with min(u,v)<=sqrt(uv) cancels D exactly:

    |phi_Q(t)| <= min(1,
      e^(5/8)2^(-5/16)pi^(9/8)c3(rho)^(-1/16)
      G^(-3/16)|t|^(-9/8)).                                  (E)

Hence

    ||p_Q||_infinity
      <=9 e^(5/9)2^(-5/18)c3(rho)^(-1/18)G^(-1/6).            (F)

For rho>=5/2 this is <15.665527 G^(-1/6), and since G>Z/24,

    ||p_Q||_infinity <26.606039 Z^(-1/6).                     (G)

Thus the unwanted positive power of the anchor determinant in the preceding D5 branch is not intrinsic. The branch has phi_Q in L1 and therefore a continuous C0 density.
