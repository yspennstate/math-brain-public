# Stronger calculation — curved joint-cap receiver removes the overlap leverage gate

The first calculation used Fresnel/BL and required leverage <=1/2 in the shared source bank. The exact shared-bank core admits a stronger direct density estimate with no leverage condition.

## Lemma — parabolic-hyperbolic receiver from a dependent planar density

Let (S,U) have an arbitrary joint probability density rho on R^2 with ||rho||_infinity<=M. Let V be independent of (S,U), with density f and ||f||_infinity<=N. For a,b !=0 and arbitrary real shifts d,alpha,beta,r0, define

Q = a(S+d)^2 + 2b(U+alpha)(V+beta) + r0.

Then Q has an essentially bounded density and

||p_Q||_infinity <= 6 (MN)^(2/3) (|a| b^2)^(-1/3).            (1)

No independence between S and U is assumed.

Proof. Absorb the deterministic shifts and r0 into S,U,V and the output. For u !=0, conditioning on (S,U) and changing variables in V gives

p_Q(q)=int_R [1/(2|b u|)] int_R rho(s,u) f((q-a s^2)/(2bu)) ds du.    (2)

Write m(u)=int rho(s,u) ds. The inner integral J_q(u) has two bounds.

First, f<=N gives J_q(u)<=N m(u).

Second, rho<=M gives

J_q(u)<=M int f((q-a s^2)/(2bu)) ds.                         (3)

For c=2bu, the square substitution y=|a|s^2 yields

int f((q-a s^2)/c) ds
 <= sqrt(|c|/|a|) sup_z int f(v)|v-z|^(-1/2) dv.              (4)

Among probability densities bounded by N, the last half-potential is maximized by density N on the centered interval of length 1/N, hence

sup_z int f(v)|v-z|^(-1/2) dv <=2 sqrt(2N).                  (5)

Therefore

J_q(u)<=4M sqrt(N |b u|/|a|).                                (6)

Put A=N/(2|b|) and B=2M sqrt(N/(|ab|)). Equations (2),(6) give

p_Q(q)<=int min(A m(u)/|u|, B/|u|^(1/2)) du.                 (7)

For any R>0, use the second bound on |u|<=R and the first outside. Since int m=1,

p_Q(q)<=4B sqrt(R)+A/R.                                      (8)

The minimum occurs at sqrt(R)=(A/(2B))^(1/3), giving

p_Q(q)<=3*2^(2/3) A^(1/3)B^(2/3)
       =6 (MN)^(2/3)(|a|b^2)^(-1/3).                         (9)

This is uniform in q, proving (1). The argument proves essential boundedness; continuity is not asserted. QED.

## Product-projection corollary

Let I,J be disjoint original-coordinate product banks with scalar input densities <=1. Put

S=r^T X_I, U=u^T X_I, V=v^T X_J,
G=[[||r||^2,<r,u>],[<r,u>,||u||^2]], tau=||v||.

Assume G>0 and tau>0. The legitimate two-dimensional product-projection theorem gives

||p_(S,U)||_infinity <=2 det(G)^(-1/2),

and the one-dimensional projection theorem gives

||p_V||_infinity <=sqrt(2)/tau.

Substitution into (1) yields the determinant-homogeneous source-valid estimate

||p_Q||_infinity
 <=12 [ |a| b^2 det(G) tau^2 ]^(-1/3).                       (10)

There is no leverage condition and no inference that S,U are independent.

For orthonormal Walsh r,u on one m-coordinate bank and a flat unit v on a disjoint bank,

Q=S^2+2UV

has exact nonzero spectrum {1,1,-1}, det G=tau=1, and therefore ||p_Q||_infinity<=12 for all independent cap-one physical source laws, uniformly in m. All three eigendirections may be delocalized.

The pinned ruled one-sheet theorem applies to the same strict target family and sharpens the positive side to

p_Q(s)<=pi sqrt(2)<4.443 for a.e. s>=0.

Thus the latest account03/B16 implication `QFORM-SHAREDBANK-PROJECTEDSQUARE-HYPERBOLIC-PREABSOLUTE-v1` is paid for the exact shared-square/hyperbolic normal form: the dependence between S and U is retained and used only through the true joint projection-density cap. The new unpaid debt is additional nonseparable same-bank curvature or failure to reduce the live near-coloop state to this exact normal form with quantitative |a| b^2 det(G) tau^2.
