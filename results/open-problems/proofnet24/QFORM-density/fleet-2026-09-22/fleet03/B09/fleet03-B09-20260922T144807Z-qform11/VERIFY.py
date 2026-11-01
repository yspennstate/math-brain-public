from fractions import Fraction
from math import sqrt


def matvec(m, x):
    n = 3*m
    y = [Fraction(0) for _ in range(n)]
    I = range(0, m)
    J = range(m, 2*m)
    K = range(2*m, 3*m)
    sI = sum(x[i] for i in I)
    sJ = sum(x[j] for j in J)
    sK = sum(x[k] for k in K)
    for i in I:
        y[i] = sJ / Fraction(m)
    for j in J:
        y[j] = sI / Fraction(m)
    for k in K:
        y[k] = sK / Fraction(m)
    return y


for m in (1, 2, 5, 17):
    n = 3*m
    eI = [Fraction(int(i < m)) for i in range(n)]
    eJ = [Fraction(int(m <= i < 2*m)) for i in range(n)]
    eK = [Fraction(int(2*m <= i)) for i in range(n)]
    vp = [eI[i] + eJ[i] for i in range(n)]
    vm = [eI[i] - eJ[i] for i in range(n)]

    assert matvec(m, vp) == vp
    assert matvec(m, vm) == [-z for z in vm]
    assert matvec(m, eK) == eK

    if m > 1:
        zI = [Fraction(0)] * n
        zJ = [Fraction(0)] * n
        zK = [Fraction(0)] * n
        zI[0], zI[1] = Fraction(1), Fraction(-1)
        zJ[m], zJ[m+1] = Fraction(1), Fraction(-1)
        zK[2*m], zK[2*m+1] = Fraction(1), Fraction(-1)
        assert all(v == 0 for v in matvec(m, zI))
        assert all(v == 0 for v in matvec(m, zJ))
        assert all(v == 0 for v in matvec(m, zK))

print("exact family checks PASS")
print("8sqrt2 =", 8*sqrt(2))
