#!/usr/bin/env python3
"""Exact certificates for worker 049. Standard library only.

The universal inequalities and family optimization are proved in agents/049.md;
the checks here certify their algebraic constants and the explicit witnesses.
No floating-point number is used in an assertion.
"""
from fractions import Fraction as F
from itertools import combinations


class Quad:
    """a + b*sqrt(D), for the positive square root and D in {3,5}."""
    def __init__(self, a=0, b=0, D=3):
        self.a, self.b, self.D = F(a), F(b), D

    def coerce(self, x):
        if isinstance(x, Quad):
            assert self.D == x.D
            return x
        return Quad(x, 0, self.D)

    def __add__(self, x):
        x = self.coerce(x)
        return Quad(self.a+x.a, self.b+x.b, self.D)
    __radd__ = __add__

    def __neg__(self):
        return Quad(-self.a, -self.b, self.D)

    def __sub__(self, x):
        return self + (-self.coerce(x))

    def __rsub__(self, x):
        return self.coerce(x) - self

    def __mul__(self, x):
        x = self.coerce(x)
        return Quad(self.a*x.a+self.D*self.b*x.b,
                    self.a*x.b+self.b*x.a, self.D)
    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.coerce(x)
        den = x.a*x.a-self.D*x.b*x.b
        assert den != 0
        return self * Quad(x.a/den, -x.b/den, self.D)

    def __rtruediv__(self, x):
        return self.coerce(x) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = self.coerce(1)
        for _ in range(n):
            out *= self
        return out

    def sign(self):
        a, b, D = self.a, self.b, self.D
        if not b:
            return (a > 0) - (a < 0)
        if not a:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        v = a*a-D*b*b if a > 0 else D*b*b-a*a
        return (v > 0) - (v < 0)

    def __abs__(self):
        return -self if self.sign() < 0 else self

    def __eq__(self, x):
        x = self.coerce(x)
        return self.a == x.a and self.b == x.b

    def __lt__(self, x):
        return (self-x).sign() < 0

    def __le__(self, x):
        return (self-x).sign() <= 0

    def __gt__(self, x):
        return (self-x).sign() > 0

    def __ge__(self, x):
        return (self-x).sign() >= 0

    def __repr__(self):
        return f"({self.a}) + ({self.b})*sqrt({self.D})"


PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]


def row(*entries):
    out = [F(0)]*4
    for k, mass in entries:
        out[k] = mass
    return out


def check_array(P):
    assert set(P) == set(PAIRS)
    for (i, j), r in P.items():
        assert len(r) == 4 and sum(r) == 1
        assert all(x >= 0 for x in r)
        assert r[i] == 0 and r[j] == 0


def bilinear(P, x, y):
    out = [F(0)]*4
    for (i, j), r in P.items():
        w = x[i]*y[j] if i == j else x[i]*y[j]+x[j]*y[i]
        for k in range(4):
            out[k] += w*r[k]
    return out


def jacobian(P, p):
    return [[2*sum(P[min(i,j), max(i,j)][k]*p[i]
                   for i in range(4)) for j in range(4)]
            for k in range(4)]


def matvec(A, x):
    return [sum(a*b for a, b in zip(r, x)) for r in A]


def solve(A, b):
    rows = [list(r)+[x] for r, x in zip(A, b)]
    n = len(b)
    for k in range(n):
        pivot = next(i for i in range(k, n) if rows[i][k] != 0)
        rows[k], rows[pivot] = rows[pivot], rows[k]
        a = rows[k][k]
        rows[k] = [x/a for x in rows[k]]
        for i in range(n):
            if i != k:
                a = rows[i][k]
                rows[i] = [x-a*y for x, y in zip(rows[i], rows[k])]
    return [r[-1] for r in rows]


def norm_row(P):
    return max(sum(abs(x) for x in r) for r in P.values())


def difference(Q, P):
    return {ij: [a-b for a, b in zip(Q[ij], P[ij])] for ij in PAIRS}


def affine(P, tau, H):
    return {ij: [a+tau*b for a, b in zip(P[ij], H[ij])]
            for ij in PAIRS}


def family(t):
    P = {
        (0,0): row((1,t),(2,1-t)),
        (1,1): row((2,t),(0,1-t)),
        (2,2): row((0,t),(1,1-t)),
    }
    for i,j,k in [(0,1,2),(0,2,1),(1,2,0),
                  (0,3,2),(1,3,0),(2,3,0),(3,3,0)]:
        P[i,j] = row((k,F(1)))
    return P


def activating_direction():
    H = {ij: row() for ij in PAIRS}
    for ij,k in [((0,0),1),((1,1),2),((2,2),1),
                 ((0,1),2),((0,2),1),((1,2),0)]:
        H[ij][k] = F(-1,2)
        H[ij][3] = F(1,2)
    return H


def coefficient_derivative_norm(P, p):
    """Exact dual-cut formula on the full normalized affine direction space."""
    J = jacobian(P, p)
    M = [[F(i == j)-J[i][j] for j in range(4)] for i in range(4)]
    MT = list(map(list, zip(*M)))
    vals = []
    for mask in range(1, 15):
        h = [F(bool(mask & (1 << i))) for i in range(4)]
        r = solve(MT, h)
        val = F(0)
        for i,j in PAIRS:
            w = p[i]*p[j]*(1 if i == j else 2)
            rr = [r[k] for k in range(4) if k not in (i,j)]
            val += w*(max(rr)-min(rr))
        vals.append(val)
    return max(vals)


def poly_sub(a, b):
    out = [F(0)]*max(len(a), len(b))
    for i,x in enumerate(a): out[i] += x
    for i,x in enumerate(b): out[i] -= x
    while len(out)>1 and out[-1] == 0: out.pop()
    return out


def poly_mul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j] += x*y
    return out


def derivative(a):
    return [i*a[i] for i in range(1,len(a))]


def main():
    r5 = Quad(0,1,5)
    c = (3-r5)/2
    b = (1-c)/(1+2*c)
    d = 2*c*b
    B = c+b
    m0 = b*d
    upper = (1-2*m0)/(1-2*c)
    assert c*c == 3*c-1 and (1-c)**2 == c
    assert F(1,3) < c < F(2,5)
    assert F(2,3) < B < 2*c
    assert c < 2*B-1
    assert b > d > 0 and c > b
    assert m0 == (27-7*r5)/121
    assert upper == (204+95*r5)/121
    assert 1 < upper < 2*r5-1
    assert m0 > c*(1-2*c)
    assert m0 < c/4 < F(1,9)
    assert 2*c+2*c*c > 1  # Two coordinate caps cannot coexist.

    Pgeo = family(F(1))
    Pgeo[1,1] = row((0,F(1)))
    Pgeo[2,2] = row((0,F(1)))
    pgeo = [c,b,d,F(0)]
    check_array(Pgeo)
    assert sum(pgeo) == 1 and bilinear(Pgeo,pgeo,pgeo) == pgeo
    assert pgeo[0]*pgeo[3]+pgeo[1]*pgeo[2] == m0
    for i,j in combinations(range(4),2):
        assert pgeo[i]+pgeo[j]+2*pgeo[i]*pgeo[j] <= 1

    r3 = Quad(0,1,3)
    z = -2+4*r3/3
    t = (1+3*z)/2
    D = 4+3*z*z
    lower = (38+7*z+18*z*z)/(9*D)
    assert 0 < z < F(1,3)
    assert t == 2*r3-F(5,2) and 0 < t < 1
    assert 3*z*z+12*z-4 == 0
    assert lower == (93+14*r3)/108 and lower > 1
    N, den = [F(38),F(7),F(18)], [F(4),F(0),F(3)]
    assert poly_sub(poly_mul(derivative(N),den),
                    poly_mul(N,derivative(den))) == [28,-84,-21]

    P = family(t)
    p = [F(1,3),F(1,3),F(1,3),F(0)]
    H = activating_direction()
    check_array(P)
    assert bilinear(P,p,p) == p
    assert norm_row(H) == 1
    assert all(sum(r) == 0 and r[i] == r[j] == 0
               for (i,j),r in H.items())
    tau_max = 2*(1-t)
    assert tau_max == 7-4*r3 and tau_max > 0
    check_array(affine(P,tau_max,H))
    g = bilinear(H,p,p)
    assert g == [F(-1,9),F(-2,9),F(-1,6),F(1,2)]
    v = [(2+7*z-9*z*z)/(18*D),
         (-26+7*z-9*z*z)/(18*D),
         (-12-14*z-9*z*z)/(18*D),F(1,2)]
    J = jacobian(P,p)
    assert sum(v) == 0
    assert [x-y for x,y in zip(v,matvec(J,v))] == g
    assert v[0] > 0 and v[1] < 0 and v[2] < 0 and v[3] > 0
    assert sum(abs(x) for x in v) == lower
    assert coefficient_derivative_norm(P,p) == lower

    # The endpoint full-affine optimizer would decrease an initially zero
    # coefficient. The algebraic optimizer above avoids this obstruction.
    Pend = family(F(1))
    assert Pend[2,2][1] == 0 and H[2,2][1] < 0
    assert coefficient_derivative_norm(Pend,p) == F(127,117)

    # Exact finite rational pair. No numerical fixed-point solver is used.
    Prat = family(F(19,20))
    delta = F(200,39601)
    alpha = F(1922136413,793010025000)
    gamma = F(1449033423,629434134400)
    Q = affine(Prat,2*delta,H)
    Q[0,3] = row((1,alpha),(2,1-alpha))
    Q[1,3] = row((0,1-delta),(2,delta))
    Q[2,3] = row((0,1-gamma),(1,gamma))
    q = [F(267,800),F(19807,60000),F(4967,15000),F(1,200)]
    assert 0 < alpha < delta and 0 < gamma < delta < F(1,20)
    check_array(Prat)
    check_array(Q)
    assert sum(q) == 1 and all(x > 0 for x in q)
    assert bilinear(Prat,p,p) == p
    assert bilinear(Q,q,q) == q
    eta = norm_row(difference(Q,Prat))
    assert eta == F(400,39601)
    dist = sum(abs(a-b) for a,b in zip(q,p))
    assert dist == F(13,1200)
    finite_ratio = dist/eta
    assert finite_ratio == F(514813,480000) > 1

    # The alternative finite witness retained in the derivation record.
    v_alt = [F(329,7686),F(-2471,7686),F(-1701,7686),F(1,2)]
    s_alt = F(1,100)
    eta_alt = s_alt/(1-s_alt/2)**2
    q_alt = [a+s_alt*b for a,b in zip(p,v_alt)]
    q_alt[0] -= s_alt*s_alt/40
    q_alt[2] += s_alt*s_alt/40
    Q_alt = affine(Prat,eta_alt,H)
    residual_alt = [a-b for a,b in zip(q_alt,bilinear(Q_alt,q_alt,q_alt))]
    alpha_alt = residual_alt[1]/(2*q_alt[0]*q_alt[3])
    beta_alt = -residual_alt[0]/(2*q_alt[1]*q_alt[3])
    assert 0 < alpha_alt < eta_alt/2 and 0 < beta_alt < eta_alt/2
    Q_alt[0,3] = row((1,alpha_alt),(2,1-alpha_alt))
    Q_alt[1,3] = row((0,1-beta_alt),(2,beta_alt))
    check_array(Q_alt)
    assert bilinear(Q_alt,q_alt,q_alt) == q_alt
    assert norm_row(difference(Q_alt,Prat)) == eta_alt
    alternative_ratio = sum(abs(a-b) for a,b in zip(q_alt,p))/eta_alt
    assert alternative_ratio == F(47182651051,43920000000)

    # Full affine inverse conditioning differs from coefficient sensitivity.
    Phalf = family(F(1,2))
    Jh = jacobian(Phalf,p)
    M = [[F(i==j)-Jh[i][j] for j in range(4)] for i in range(4)]
    residual_ratios = []
    for i,j in combinations(range(4),2):
        rhs = [F(k==i)-F(k==j) for k in range(4)]
        vv = solve(M,rhs)
        assert sum(vv) == 0 and matvec(M,vv) == rhs
        residual_ratios.append(sum(abs(x) for x in vv)/2)
    assert max(residual_ratios) == F(7,6)
    assert coefficient_derivative_norm(Phalf,p) == F(19,18)

    print("All exact coefficient, fixed-point, norm, and radical checks passed.")
    print("Sharp geometry product:", m0)
    print("Universal upper:", upper)
    print("Attained feasible derivative lower:", lower)
    print("Attained finite rational ratio:", finite_ratio)
    print("Alternative finite rational ratio:", alternative_ratio)
    print("At t=1/2: inverse residual norm 7/6; coefficient norm 19/18.")


if __name__ == "__main__":
    main()
