SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-23T17:36:01Z.
attacking: hub-that-sees-P curved-fiber receiver; first isolate a product-preserving two-bank parabolic estimate uniform in the curvature, then test whether it routes an actual surviving rough-law packet.

# Early substantive calculation: two-bank parabolic receiver

Full QFORM remains OPEN. This checkpoint proves a scoped analytic lemma; it does not claim the bare spectral hypothesis produces the required bank geometry.

## Scalar lemma
Let A,B be independent real random variables with densities f,g satisfying ||f||_infinity<=K_A and ||g||_infinity<=K_B. Fix real p,q,r,s,c with Delta=ps-qr !=0 and put

F=pA+qB+c(rA+sB)^2.

Then F has an essentially bounded density and for every theta in (0,1),

||p_F||_infinity <= |Delta|^{-1}[2|r|K_B/theta + |s|K_A/(1-theta)].   (E1)

Interchanging A and B also gives

||p_F||_infinity <= |Delta|^{-1}[2|s|K_A/theta + |r|K_B/(1-theta)].   (E2)

Hence

||p_F||_infinity <= |Delta|^{-1} min{(sqrt(2|r|K_B)+sqrt(|s|K_A))^2,
                                      (sqrt(2|s|K_A)+sqrt(|r|K_B))^2}. (E3)

Proof. Set U=pA+qB, V=rA+sB. Their joint density is

h(u,v)=|Delta|^{-1} f((su-qv)/Delta) g((-ru+pv)/Delta).

Since F=U+cV^2,

p_F(z)=|Delta|^{-1} int_R f(A_z(t))g(B_z(t))dt,
A_z(t)=[s(z-ct^2)-qt]/Delta,
B_z(t)=[-r(z-ct^2)+pt]/Delta.

Differentiating gives the exact cancellation identity

r A_z'(t)+s B_z'(t)=1.                                             (E4)

Let E={t: |r A_z'(t)|>=theta}. Because A_z' is affine, E is a union of at most two intervals, on each of which A_z is monotone and |A_z'|>=theta/|r|. Therefore

int_E f(A_z(t))g(B_z(t))dt <= 2|r|K_B/theta.

On E^c, (E4) gives |sB_z'|>=1-theta. The set E^c is one interval and B_z' has no zero there, so

int_{E^c} f(A_z(t))g(B_z(t))dt <= |s|K_A/(1-theta).

The r=0 or s=0 endpoints follow directly from (E4). This proves (E1). Swap A,B for (E2); optimize A/theta+B/(1-theta)=(sqrt A+sqrt B)^2 to get (E3). No support, moment, connectedness, or smoothness hypothesis is used.

A translation V->V+v0 only changes the linear row (p,q) to (p+2cv0r,q+2cv0s), whose determinant with (r,s) is still Delta. Thus the same bound is uniform in an arbitrary frozen translation of the curved variable.

## Product-bank corollary
Let the original independent coordinates split as S disjoint T disjoint R. Let a,d,b,e be real numbers and let rho,sigma be unit vectors supported on S,T. Assume the restrictions of a two-direction frame are

u_S=a rho,   v_S=d rho,
u_T=b sigma, v_T=e sigma,

with Delta=ae-bd !=0; the restrictions on R may be arbitrary. Put U=<u,X>, V=<v,X>. Then for every real c and every measurable G(X_R),

Q=U+cV^2+G(X_R)

has, after conditioning X_R, exactly the scalar form above with A=<rho,X_S>, B=<sigma,X_T> and the same determinant Delta. The designated account02/B06 theorem QFORM-WEIGHTED-AFFINE-FIBER-BL-v1 (math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5) applies at the actual inequalities

||p_A||_infinity<=sqrt(e),  ||p_B||_infinity<=sqrt(e).

Therefore

||p_Q||_infinity <= sqrt(e)|Delta|^{-1}
 min{(sqrt(2|d|)+sqrt(|e|))^2,(sqrt(2|e|)+sqrt(|d|))^2}.              (E5)

The bound is uniform in the conditioned R variables, hence survives averaging. It is also uniform in c, including c->0, and never takes a curved-fiber supremum.

The grouped cross-Pluecker mass between S and T is exactly

sum_{i in S,j in T}(u_i v_j-v_i u_j)^2=Delta^2.                       (E6)

Thus if |d|,|e|<=1, (E5) implies the simple wedge form

||p_Q||_infinity <= (3+2sqrt(2))sqrt(e)/sqrt(W_ST) < 9.608/sqrt(W_ST). (E7)

If R is empty and u,v are orthonormal, the 2x2 coefficient matrix [[a,b],[d,e]] is orthogonal, so |Delta|=1 and d^2+e^2=1. Taking the minimum in (E5) and using |d|+|e|<=sqrt(2), min(|d|,|e|)<=1/sqrt(2), sqrt(|de|)<=1/sqrt(2) gives

||p_{U+cV^2}||_infinity <= (2+3/sqrt(2))sqrt(e) < 6.797.              (E8)

This pays the exact two-ray/two-bank subcase of the open curved marginal P2 from the current single_hub_core source, for arbitrary fragmented cap-one product laws and uniformly over the curvature c. It does NOT settle P2 for a genuinely diffuse overlapping frame, and it does NOT settle the hub-that-sees-P estimate (SP).

## Fresh source state
