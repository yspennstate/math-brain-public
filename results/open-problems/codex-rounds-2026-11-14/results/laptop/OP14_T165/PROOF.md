# All linear fluid paths for a repeated-middle reflection family

## Statement

Let m >= 2, n=m+2, and let

    a>0, b>0, 0<c<1, 0<h<1.

Index the coordinates by 0, 1,...,m, and L=m+1. Let theta be the n-vector with every entry -1. Define R by

    R_00=R_LL=1,             R_0L=1-h,     R_L0=1+a,
    R_0i=1+b,               R_i0=1,
    R_ii=1,                 R_ij=1-c      (1<=i!=j<=m),
    R_iL=R_Li=1-c            (1<=i<=m).

Every entry of R is positive. In particular, every principal submatrix maps the all-ones vector to a strictly positive vector, so R is completely-S.

Put

    A=m-(m-1)c, B=mb+(m-1)c, T=m+1-mc,
    q=h-m(b+c).

There are exactly two pairs (u,v) satisfying

    u>=0, v=Ru-1>=0, u_i v_i=0 for every i.                 (1)

The first is always

    u=(1,0,...,0),       v=(0,...,0,a).                     (2)

If q<=0, the second is

    u=(0,1/T,...,1/T),   v=(-q/T,0,...,0).                 (3)

If q>0, define

    D=cq+a[A(h-c)+(1-c)B].

Then D>0 and the second pair is

    u=(cq/D, a(h-c)/D,...,a(h-c)/D, aB/D),   v=0,           (4)

where the middle entry a(h-c)/D occurs m times.

Consequently, when q<0 both linear fluid solutions from the origin diverge. When q>=0 exactly one diverges and the other remains at the origin. These assertions concern linear fluid solutions only.

## Relation between (1) and fluid paths

A fluid path from the origin has the decomposition z(t)=-t*1+Ry(t), remains in the nonnegative orthant, and has continuous nondecreasing regulators y_i starting at zero, with

    integral from 0 to t of z_i(s) dy_i(s)=0.

For a linear path y(t)=ut, z(t)=vt, these conditions say u>=0, v>=0, v=Ru-1, and

    integral from 0 to t of v_i s u_i ds = u_i v_i t^2/2=0.

They are therefore equivalent to (1). A nonzero nonnegative v makes z(t) unbounded as t increases, while v=0 makes z identically zero.

## Proof of completeness

For any two middle indices i,j, the row definitions give

    v_i-v_j=c(u_i-u_j).                                    (5)

If u_i>u_j, then u_i>0 and (1) gives v_i=0. Equation (5) would give v_j=-c(u_i-u_j)<0, a contradiction. Interchanging i and j rules out u_j>u_i. All middle regulator rates are therefore equal, say u_i=w. Write u_0=x and u_L=z. All middle velocities equal a common value v_M. The remaining equations are

    v_0=x+m(1+b)w+(1-h)z-1,
    v_M=x+Aw+(1-c)z-1,
    v_L=(1+a)x+m(1-c)w+z-1.                               (6)

Subtracting gives

    v_0-v_M=Bw+(c-h)z,
    v_L-v_M=ax-cw+cz.                                     (7)

### Case w=0

If x=z=0, (6) makes every velocity -1, which is impossible. If x=0 and z>0, complementarity at L gives z=1 and then v_0=-h<0, also impossible. If x>0 and z>0, complementarity gives v_0=v_L=0, whereas subtracting the first and third lines of (6), with w=0, gives

    v_L-v_0=ax+hz>0.

This is a contradiction. The only remaining possibility is x>0,z=0. Complementarity at 0 gives x=1. Substitution in (6) gives v_0=v_M=0 and v_L=a. Thus (2) is the only solution with w=0.

### Case w>0

Complementarity forces v_M=0. First suppose z=0. The first identity in (7) gives v_0=Bw>0 since B>0. It follows that x=0. The second identity in (7) then gives v_L=-cw<0. Therefore z>0 and complementarity forces v_L=0. The second identity in (7) now becomes

    ax=c(w-z).                                            (8)

If x=0, (8) gives z=w. The equation v_M=0 in (6) becomes

    (A+1-c)w=Tw=1.

The first identity in (7) gives

    v_0=(B+c-h)w=[m(b+c)-h]/T=-q/T.

This pair is feasible exactly when q<=0, and it is (3).

It remains to consider x>0. Complementarity gives v_0=0. Equations (7)–(8) imply

    (h-c)z=Bw,       ax=c(w-z)>0.                         (9)

Because B,w,z are positive, h-c>0. Also z<w by the second equation. Substituting z=Bw/(h-c) shows

    B<h-c, equivalently h>m(b+c), equivalently q>0.

For q>0, solving (9) gives

    z=Bw/(h-c),       x=cq*w/[a(h-c)].

Substituting in v_M=0 yields

    [cq+aA(h-c)+a(1-c)B]w=a(h-c).

The bracket is D. Every summand of D is positive when q>0, so D>0. Solving gives exactly (4). All its regulator rates are strictly positive, and (6)–(9) verify v=0. This proves existence and uniqueness in this last case. The cases are exhaustive, and (2) differs from the second pair because its middle rates vanish. The claimed classification follows.

The same proof also holds for m=1; equality of middle rates is then vacuous.

## Four-dimensional specialization

Take m=2, a=b=c=1/20, h=3/5. Then

    R = [ 1       21/20   21/20   2/5   ]
        [ 1       1       19/20   19/20 ]
        [ 1       19/20   1       19/20 ]
        [ 21/20   19/20   19/20   1     ].

Here A=39/20, B=3/20, T=29/10, q=2/5, and

    A(h-c)+(1-c)B
      = (39/20)(11/20)+(19/20)(3/20)
      = 243/200,
    D=(1/20)(2/5)+(1/20)(243/200)=323/4000.

The complete list is therefore

    u=(1,0,0,0),                v=(0,0,0,1/20),
    u=(80,110,110,30)/323,      v=(0,0,0,0).

Direct multiplication provides a separate check of the stationary rate:

    80+(21/20)110+(21/20)110+(2/5)30=323,
    80+110+(19/20)110+(19/20)30=323,
    80+(19/20)110+110+(19/20)30=323,
    (21/20)80+(19/20)110+(19/20)110+30=323.

Thus Ru=1. For the divergent rate, the first column of R minus 1 is precisely (0,0,0,1/20).

The antisymmetric middle direction (0,1,-1,0) is an eigenvector of R with eigenvalue c. On the invariant subspace with equal middle coordinates, R has matrix

    M = [ 1     m(1+b)    1-h ]
        [ 1     A         1-c ]
        [ 1+a   m(1-c)    1   ].

Subtracting its middle row from its first and last rows and expanding gives

    det(M)=B[a(1-c)-c]+(c-h)[-c-aA]
          =cq+a[A(h-c)+(1-c)B]=D.

The middle sum-zero subspace has dimension m-1 and eigenvalue c. Therefore det(R)=c^(m-1)D. At the four-dimensional specialization this is 323/80000. This determinant identity is an auxiliary check; the classification proof does not require nonsingular principal submatrices.

## What this does and does not settle

This gives a complete parameter classification of linear fluid solutions for the stated reflection family, in every dimension n=m+2>=4. In particular, it proves uniqueness of the divergent linear solution at the explicit four-dimensional matrix above, even though a strictly positive stationary regulator rate exists.

The matrix and its divergent solution occur in Curtis Heyda, *Construction of positive recurrent semimartingale reflecting Brownian motions with divergent fluid paths using predator–prey models*, Queueing Systems 110, article 48 (2026), Sections 2.3 and 5:
https://link.springer.com/article/10.1007/s11134-026-10006-5 . The paper already proves the existence of the divergent solution; that is not a new claim here. The contribution here is the complete list and its parameter threshold, with an exact finite audit. No claim of priority for the algebraic classification is made.

No statement about nonlinear fluid paths or positive recurrence follows from this list alone. In particular, the general covariance-sensitive recurrence classification in T165 remains unresolved.
