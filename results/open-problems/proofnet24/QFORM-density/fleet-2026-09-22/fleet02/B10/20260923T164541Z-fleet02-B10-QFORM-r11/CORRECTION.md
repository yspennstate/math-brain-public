# Correction to the early checkpoint

The discriminant identity, determinant identity, and logarithmic obstruction mechanism in CHECKPOINT.md are correct, but its last comparison to the designated-partner exact-null theorem used an endpoint example whose two transverse rows had leverage 1. That does **not** satisfy fleet03/B10 r24's hypothesis that every complementary transverse leverage is at most 1/2. Do not use that particular four-row endpoint to invoke r24.

A source-compatible replacement keeps the same spectral matrix and the same logarithmic obstruction while satisfying the partner gate. Fix h=7/8 and use the Parseval rows

sqrt(h)e1, sqrt(1-h)e1, e2/sqrt(2), e2/sqrt(2), e3/sqrt(2), e3/sqrt(2).

Every complementary transverse leverage is now 0 or 1/2. Let the two e2-bank inputs be iid Uniform[-1/2,1/2], and the two e3-bank inputs be iid Uniform[1,2]. Then

Y=(X_2+X_3)/sqrt(2),   Z=(X_4+X_5)/sqrt(2)

are independent because they use disjoint ORIGINAL coordinate banks. Their densities satisfy

p_Y(y)>=1/sqrt(2) for 0<=y<=1/(2sqrt(2)),
p_Z(z)>=1/sqrt(2) for 5/(2sqrt(2))<=z<=7/(2sqrt(2)).

For the same

M_eps=[[eps,sqrt(1+eps),0],[sqrt(1+eps),0,0],[0,0,1]],
K=diag(1+eps,-eps),
D_0(Y,Z)=(1+eps)Y^2-eps Z^2,

choose 0<eps<=1/288 and integrate over

5/(2sqrt(2))<=z<=7/(2sqrt(2)),   3sqrt(eps)<=y<=1/(2sqrt(2)).

Since z<3 and y>=3sqrt(eps), D_0>0. Using D_0<=(1+eps)y^2 and the two density lower bounds gives

E[1_{D_0>0}D_0^(-1/2)]
 >= [1/(2sqrt(2)sqrt(1+eps))] log( 1/(6sqrt(2 eps)) ).

Thus the same logarithmic divergence holds as eps downarrow 0.

Now the exact-null endpoint eps=0 **does** satisfy the completed fleet03/B10 r24 theorem, so with h=7/8 and |det M_0|=1,

||p_Q||_infinity <=3*2^(4/3)(7/8)^(-1/3)<7.952.

For every eps>0, the required ruled one-sheet theorem still gives p_Q(s)<=pi sqrt(2) on the one-sheet side, including s=0. Hence the corrected family simultaneously establishes all three facts needed for the route obstruction: target-valid spectrum, a logarithmically divergent hub-first absolute discriminant receiver, and uniform actual control at the ruled side plus the compatible exact-null endpoint.

All subsequent statements for this run use this corrected six-row construction, not the four-row endpoint comparison in CHECKPOINT.md.
