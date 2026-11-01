SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-23T07:31:01Z.
attacking: a weighted joint negative-moment receiver for the shared-coefficient double-null fiber, and the collinear endpoint forced by the third large direction.

# Early checkpoint: shared-coefficient reciprocal product

Let (U,V) have a joint density bounded by K and marginal densities bounded by L_U,L_V. Put kappa=K/(L_U L_V). From

x^(-1/2)=(1/2) integral_x^infinity s^(-3/2) ds

and the rectangle estimate

P(|U|<=s,|V|<=t)<=min(1,2L_U s,2L_V t,4Kst),

one gets after x=2L_U s, y=2L_V t

E|UV|^(-1/2) <= (1/2)sqrt(L_U L_V) J(kappa),
J(kappa)=integral_0^infinity integral_0^infinity min(1,x,y,kappa xy)x^(-3/2)y^(-3/2) dxdy.

For kappa>=1, integrating first in y gives

J(kappa)=16+4 log kappa,

hence

E|UV|^(-1/2) <= sqrt(L_U L_V)[8+2 log kappa].

For affine linear forms U=a.Z+u0, V=b.Z+v0 of independent cap-one coordinates, the already proved weighted affine-fiber Brascamp--Lieb theorem gives

L_U<=sqrt(e)/||a||, L_V<=sqrt(e)/||b||,
K<=e/sqrt(||a||^2||b||^2-(a.b)^2).

Writing A=||a||, B=||b|| and D=sqrt(A^2 B^2-(a.b)^2), this yields

E|UV|^(-1/2) <= [2sqrt(e)/sqrt(AB)] [4+log(AB/D)], D>0.

Therefore for genuine independent cap-one anchors X,Y independent of Z and arbitrary R(Z),

T=2XU+2YV+R(Z)

obeys

||p_T||_infinity <= [sqrt(e)/sqrt(AB)] [4+log(AB/D)].

This pays the shared-coefficient double-null branch whenever the two coefficient rows are quantitatively transverse; no conditional fiber supremum and no independence between U and V is used. The remaining endpoint D=0 must use the third direction rather than a fictitious angle bound.
