from fractions import Fraction as F


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def mv(A, x):
    return tuple(sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A)))


def tr(A):
    return tuple(tuple(A[j][i] for j in range(len(A))) for i in range(len(A[0])))


def cross(a, b):
    return (
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0],
    )


def build(sa, sb, m, rho, r2, s2):
    A = sa*sa
    B = sb*sb
    t = sa*sb
    D = A*B - m*m
    assert D > 0

    # Exact simple mixed-Schur pair-LS saturation.
    H = rho*rho + (A*r2*r2 + 2*m*r2*s2 + B*s2*s2)/D
    z = (A+B-H)/2
    r1 = sb*rho
    s1 = -sa*rho

    Z = ((t, F(0), r1),
         (F(0), m, r2),
         (s1, s2, z))
    p = (-r1, -r2, A-z)
    q = (-s1, -s2, B-z)

    kL = (A*r2 + m*s2)/D
    kR = (B*s2 + m*r2)/D
    wL = (F(0), F(1), -kL)
    wR = (F(0), F(1), -kR)
    aL = cross(p, wL)
    aR = cross(q, wR)

    # New exact signed/scaled bilateral transport.
    assert tuple(mv(tr(Z), aL)[i] + t*aR[i] for i in range(3)) == (F(0),)*3
    assert tuple(mv(Z, aR)[i] + t*aL[i] for i in range(3)) == (F(0),)*3
    assert dot(aL, aL) == dot(aR, aR)
    assert (aL == (F(0),)*3) == (aR == (F(0),)*3)

    # Finite scalar description of the bilateral-degenerate branch.
    if aL == (F(0),)*3:
        assert rho == 0
        assert A*r2*r2 - B*s2*s2 == (A-B)*D

    return A, B, t, D, H, z, aL, aR


tests = [
    ("source-calibration", (F(1), F(1), F(0), F(1,3), F(1,4), F(1,5))),
    ("unequal-sectors", (F(2), F(3), F(1), F(2,7), F(1,5), F(-3,8))),
    ("bilateral-degenerate", (F(1), F(1), F(0), F(0), F(1,3), F(1,3))),
]

print("PASS MOC4-MSQR-EXACT-AXIS-ANTITRANSPORT-v1")
for name, args in tests:
    A, B, t, D, H, z, aL, aR = build(*args)
    print(name)
    print(" A,B,t,D =", A, B, t, D)
    print(" H,z =", H, z)
    print(" aL =", aL)
    print(" aR =", aR)
