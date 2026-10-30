SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T03:23:34Z.
attacking: join the r25 diffuse third-volume exit to the high-volume-leverage survivor by forcing an anchored third-minor packet, then feed the transverse branch into the B07 four-bank tail/core compiler.

# Early substantive checkpoint — volume-marginal exit or anchored hub

Let B be an ORIGINAL-coordinate cross block and

Delta3(B)=sum_{|S|=|T|=3} det B[S,T]^2>0.

Put the normalized third-volume law

w_{S,T}=det B[S,T]^2/Delta3(B),
alpha_i=sum_{S contains i,T} w_{S,T},
beta_j=sum_{S,T contains j} w_{S,T}.

The newest fractional-volume theorem at math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba gives, for 1<=q<3/2, a continuous density bound

||p_Q||_inf <= 3e/[(3-2q)sqrt(q)] Delta3(B)^(-1/6)

whenever max_i alpha_i<=q/2 on one physical side (and likewise after transposing B).

Therefore, for 1<q<3/2, if neither side pays, there exist a physical row i and column j with alpha_i>q/2 and beta_j>q/2. By the union bound under w,

Z_ij := sum_{S contains i,T contains j} det B[S,T]^2
      = Delta3(B) P_w(i in S, j in T)
      > (q-1) Delta3(B).

Write B around i,j as [[b,r^T],[c,D]]. The exact anchored exterior identity from fleet03/B07 r21 is

T = b C2(D) - L_c D iota_r,

where ||T||_HS^2=Z_ij and

||L_c D iota_r||_HS
 = ||c|| ||r|| ||P_c^perp D P_r^perp||_F.

Hence by reverse triangle, at least one of

|b| sqrt(E2(D)) > (1/2)sqrt((q-1)Delta3(B)),

or

||L_c D iota_r||_HS > (1/2)sqrt((q-1)Delta3(B))

holds. In the second case the B07 random physical two-coloring argument yields four mutually disjoint original-coordinate banks with

||c_L|| ||r_R|| ||D[L',R']||_F
 > (1/16)sqrt((q-1)Delta3(B)).

For the B08 r25 q=0 packet, Delta3(B)>=L^6/2304. Taking q=4/3 gives the explicit exhaustive branch

(A) ||p_Q||_inf < 77/L, continuously; or
(B) |b| sqrt(E2(D)) > L^3/(96 sqrt(3)); or
(C) four disjoint banks satisfy ||c_L||||r_R||||D[L',R']||_F > L^3/(768 sqrt(3)).

This removes the r25 full-range-leverage gate from the q=0 branch. The remaining work is to splice (B) and (C) into existing pivot/E2 and B07 tail/core receivers without using a one-good-minor shortcut.
