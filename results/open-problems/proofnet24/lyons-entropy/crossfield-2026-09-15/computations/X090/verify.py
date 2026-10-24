"""Exact checks supplementing the all-size analytic proof in agents/X090.md.

No finite sign check is used as a universal proof. This program independently
expands the original four-scalar count-Fisher/log-acceleration expression and
compares every coefficient with the claimed even/odd contraction matrices.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


checks = 0


def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def block(p):
    out = []
    for h in range(p + 1):
        x = F(2*h-p, p)
        a2 = (p*x*x-1)/(p-1)
        a3 = (p*p*x**3-(3*p-2)*x)/((p-1)*(p-2)) if p > 2 else F(0)
        out.append((x, a2, a3, F(comb(p, h), 2**p)))
    return out


def moment(p, j):
    return sum(w*x**j for x, _, _, w in block(p))


def quantities(p, k):
    j = 2*k
    data = block(p)
    m = sum(w*x**j for x, a2, a3, w in data)
    n = sum(w*x**(j+2) for x, a2, a3, w in data)
    t = sum(w*a2*x**j for x, a2, a3, w in data)
    u = sum(w*a2*a2*x**(j-2) for x, a2, a3, w in data)
    v = sum(w*a3*x**(j-1) for x, a2, a3, w in data)
    c = F(j, j+1)
    D = u+F(p, p-1)*t/j+F(p-2, p-1)*v/(j-1)
    ell = D-t*t/(c*c*n)
    return m, n, t, u, v, c, D, ell


def zero():
    return [[F(0) for j in range(4)] for i in range(4)]


def direct_coefficient(p, q, n):
    """Coefficient of rho**n in X051(14)/4, using original count sums."""
    out = zero()
    alpha = beta = gamma = delta_prev = eps_prev = zeta_prev = F(0)
    for x, a2, a3, wx in block(p):
        for y, b2, b3, wy in block(q):
            w = wx*wy
            xy = x*y
            s0 = [x, F(0), y, F(0)]
            s1 = [F(0), -a2*y, F(0), -x*b2]
            for i in range(4):
                for j in range(4):
                    out[i][j] += w*s0[i]*s0[j]*xy**n
                    if n >= 1:
                        out[i][j] += w*(s0[i]*s1[j]+s1[i]*s0[j])*xy**(n-1)
                    if n >= 2:
                        out[i][j] += w*s1[i]*s1[j]*xy**(n-2)
            if n >= 1:
                z = w*xy**n/n
                alpha += z*a2
                beta += z*b2
                gamma += z*xy
            if n >= 2:
                z = w*xy**(n-1)/(n-1)
                delta_prev += z*a3*y
                eps_prev += z*x*b3
                zeta_prev += z*a2*b2
    kp, kq = F(p-2, p-1), F(q-2, q-1)
    out[0][1] -= alpha
    out[1][0] -= alpha
    out[1][1] += (2-kp)*alpha+kp*delta_prev
    out[2][3] -= beta
    out[3][2] -= beta
    out[3][3] += (2-kq)*beta+kq*eps_prev
    out[0][2] -= gamma
    out[2][0] -= gamma
    out[1][3] += zeta_prev
    out[3][1] += zeta_prev
    return out


def contraction_coefficient(p, q, n):
    out = zero()
    if n == 0:
        out[0][0], out[2][2] = F(1, p), F(1, q)
        return out
    if n == 1:
        return out
    k = n//2
    mp, np, tp, up, vp, c, Dp, lp = quantities(p, k)
    mq, nq, tq, uq, vq, _, Dq, lq = quantities(q, k)
    if n % 2 == 0:
        out[0][0], out[0][1], out[1][0], out[1][1] = mq*np, -mq*tp/c, -mq*tp/c, mq*Dp
        out[2][2], out[2][3], out[3][2], out[3][3] = mp*nq, -mp*tq/c, -mp*tq/c, mp*Dq
    else:
        cross = [[c*np*nq, -np*tq], [-tp*nq, tp*tq/c]]
        for i in range(2):
            for j in range(2):
                out[i][j+2] = out[j+2][i] = cross[i][j]
        check(cross[0][0]*cross[1][1] == cross[0][1]*cross[1][0], (p, q, k, "rank one"))
    return out


def polynomial(p):
    return 45*p**4-766*p**3+3952*p*p-5536*p+2176


for p in range(2, 7):
    for q in range(2, 7):
        for n in range(14):
            direct = direct_coefficient(p, q, n)
            paired = contraction_coefficient(p, q, n)
            for i in range(4):
                for j in range(4):
                    check(direct[i][j] == paired[i][j], (p, q, n, i, j))

for p in range(2, 21):
    m, n, t, u, v, c, D, ell = quantities(p, 1)
    check(n == F(3*p-2, p**3), (p, "n1"))
    check(t == F(2, p*p), (p, "t1"))
    check(D == F(3, p*(p-1)), (p, "D1"))
    check(ell == F(3, p*(p-1)*(3*p-2)), (p, "ell1"))
    u2 = quantities(p, 2)[3]
    u3 = quantities(p, 3)[3]
    check(u2 == F(2*(5*p-8), p**3*(p-1)), (p, "u2"))
    check(u3 == F(2*(39*p*p-142*p+136), p**5*(p-1)), (p, "u3"))
    eta = ell-u2/16-u3/10
    check(eta == F(polynomial(p), 40*p**5*(p-1)*(3*p-2)), (p, "eta formula"))
    check(eta > 0, (p, "finite eta diagnostic"))
    for k in range(2, 16):
        j = 2*k
        m, n, t, u, v, c, D, ell = quantities(p, k)
        J = p*p*n+(2*j-3*p)*m-2*(j-1)*moment(p, j-2)
        check(D-F(j+2, j)*u == J/((p-1)**2*j*(j-1)), (p, k, "moment identity"))
        check(J >= 0, (p, k, "finite lemma diagnostic"))
        check(t*t <= n*u, (p, k, "Cauchy diagnostic"))
        check(ell >= -u/(j*j), (p, k, "tail diagnostic"))

for x in range(6):
    check(polynomial(x+8) == 45*x**4+674*x**3+2848*x*x+2784*x+2944, (x, "shifted polynomial"))

bad = quantities(2, 2)
check(bad[1]*bad[6]-bad[2]**2/bad[5]**2 == -F(1, 64), "retained failed coefficientwise strengthening")
result = {
    "status": "PASS",
    "exact_assertions": checks,
    "coefficient_scope": "Every matrix entry, p,q=2,...,6, rho powers 0,...,13",
    "small_integer_polynomial_values": {str(p): polynomial(p) for p in range(2, 8)},
    "universal_proof": "Analytic Sections 2-4 of agents/X090.md; finite checks are supplementary only",
}
Path(__file__).with_name("results.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
