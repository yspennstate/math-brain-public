"""PROVED: polynomial construction for the actual extreme-pair weight endpoint.

The polynomial has degree twelve in ordered-cone variables z and degree
six in the unrestricted coordinates x of W. No weight is relaxed.
"""
from sympy.polys.rings import ring
from sympy.polys.domains import QQ


def ingredients():
    ring0, *gens = ring('z0,z1,z2,z3,x0,x1,x2', QQ)
    z, x = gens[:4], gens[4:]
    U = [sum(((5-j) if i < j else -j)*z[j-1]
             for j in range(1, 5)) for i in range(5)]
    delta = U[0]-U[4]
    W = [sum((U[4]-U[j+1])*x[j] for j in range(3))]
    W += [delta*x[j] for j in range(3)]
    W += [sum((U[j+1]-U[0])*x[j] for j in range(3))]
    t, n = sum(q*q for q in U), sum(q*q for q in W)
    A, B = sum(q**4 for q in U), sum(q**4 for q in W)
    C = sum(q*q*v*v for q, v in zip(U, W))
    d, h = sum(q**3 for q in U), sum(q**3 for q in W)
    e = sum(q*q*v for q, v in zip(U, W))
    f = sum(q*v*v for q, v in zip(U, W))
    # Numerator of L_u+rL_w over t^2 n^2.
    Lu = QQ(14, 9)*(A*n*n+t*C*n-t*t*n*n/5)
    Lw = QQ(14, 9)*(t*t*B+t*C*n-t*t*n*n/5)
    # Numerator of P+rQ0+r^2 R_w over t^3 n^3.
    P = QQ(58, 45)*t**3*n**3-QQ(40, 9)*A*t*n**3
    P -= QQ(34, 9)*C*t*t*n*n
    P += QQ(8, 3)*d*d*n**3+QQ(2, 3)*e*e*t*n*n+2*d*f*t*n*n
    R = QQ(58, 45)*t**3*n**3-QQ(40, 9)*B*t**3*n
    R -= QQ(34, 9)*C*t*t*n*n
    R += QQ(8, 3)*h*h*t**3+QQ(2, 3)*f*f*t*t*n+2*h*e*t*t*n
    Q = QQ(2, 9)*(A*t*n**3+B*t**3*n-QQ(2, 5)*t**3*n**3)
    Q -= QQ(8, 9)*C*t*t*n*n
    Q += QQ(10, 3)*(e*e*t*n*n+f*f*t*t*n)
    Q += 2*d*f*t*n*n+2*h*e*t*t*n
    return ring0, U, W, t, n, Lu, Lw, P, Q, R


def construct(ratio):
    rr = QQ(ratio.numerator, ratio.denominator)
    ring0,U,W,t,n,Lu,Lw,P,Q,R = ingredients()
    L = Lu+rr*Lw
    D = (-20*U[0]*U[4]-t)*n-rr*t*(n+20*W[0]*W[4])
    expected = QQ(9, 2)*(D*L+2*(P+rr*Q+rr*rr*R))
    return ring0, expected
