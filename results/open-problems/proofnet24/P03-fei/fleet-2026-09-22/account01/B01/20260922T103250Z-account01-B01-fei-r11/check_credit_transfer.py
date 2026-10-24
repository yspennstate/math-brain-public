from fractions import Fraction
from math import log2

VALUES = [-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,1]


def walsh_raw(values):
    a = list(values)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def restrict(values, bit, value):
    return [v for i, v in enumerate(values) if ((i >> bit) & 1) == value]


def spectral_data(values):
    raw = walsh_raw(values)
    N = len(values)
    sq = [Fraction(x*x, N*N) for x in raw]
    v = 1 - sq[0]
    n = N.bit_length() - 1
    r = []
    for bit in range(n):
        marginal = Fraction(0)
        for mask in range(1, N):
            if (mask >> bit) & 1:
                marginal += sq[mask] / v
        r.append(marginal)
    return raw, sq, v, r


def iproj_parameter(r):
    # Positive solution of 1-c = prod_i (1-c r_i), found deterministically.
    # The examples below also have the exact closed forms recorded in REPORT.md.
    mu = sum(float(x) for x in r)
    if abs(mu - 1.0) < 1e-15:
        return 1.0
    def f(c):
        prod = 1.0
        for x in r:
            prod *= 1.0 - c*float(x)
        return 1.0 - c - prod
    lo, hi = 1e-15, 1.0
    for _ in range(220):
        mid = (lo + hi)/2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi)/2


def kocc(values):
    raw, sq, v, r = spectral_data(values)
    c = iproj_parameter(r)
    t = [c*float(x) for x in r]
    K = 0.0
    for mask in range(1, len(values)):
        if sq[mask] == 0:
            continue
        p = float(sq[mask] / v)
        q = 1.0
        for i, ti in enumerate(t):
            q *= ti if ((mask >> i) & 1) else (1.0-ti)
        q /= c
        K += p*log2(p/q)
    return raw, v, r, c, K, float(v)*K


def main():
    c0 = restrict(VALUES, 0, 0)
    c1 = restrict(VALUES, 0, 1)
    rows = []
    for name, values in [('parent', VALUES), ('child0', c0), ('child1', c1)]:
        raw, v, r, c, K, C = kocc(values)
        rows.append((name, values, raw, v, r, c, K, C))
        print(name)
        print('values', values)
        print('raw', raw)
        print('v', v)
        print('r', r)
        print('c', repr(c), 'K', repr(K), 'C', repr(C))

    parent, child0, child1 = rows
    assert parent[2] == [-4,-4,-4,4,-4,-4,4,-4,-4,4,-4,-4,-4,4,4,4]
    assert parent[3] == Fraction(15,16)
    assert parent[4] == [Fraction(8,15)]*4
    assert abs(parent[5] - Fraction(15,16)) < 1e-14
    assert abs(parent[6]) < 1e-14

    assert child0[2] == [-4,0,-4,0,0,-4,0,4]
    assert child0[3] == Fraction(3,4)
    assert child0[4] == [Fraction(2,3)]*3
    assert abs(child0[5] - (9-3*(3**0.5))/4) < 1e-14
    assert child0[6] > 0

    assert child1[2] == [0,-4,0,4,-4,0,-4,0]
    assert child1[3] == 1
    assert child1[4] == [Fraction(1,2)]*3
    assert abs(child1[5] - (3-5**0.5)) < 1e-14
    assert child1[6] > 0

    Xi = parent[7] - (child0[7] + child1[7])/2
    print('Xi', repr(Xi))
    assert Xi < 0

    a = Fraction(sum(c0), len(c0))
    b = Fraction(sum(c1), len(c1))
    plus = minus = disagree = 0
    for x, y in zip(c0, c1):
        if x != y:
            disagree += 1
            z = (y-x)//2
            plus += (z == 1)
            minus += (z == -1)
    delta = Fraction(disagree, len(c0))
    Pplus = Fraction(plus, len(c0))
    Pminus = Fraction(minus, len(c0))
    print('means', a, b, 'delta', delta, 'P+', Pplus, 'P-', Pminus)
    assert (a,b,delta,Pplus,Pminus) == (Fraction(-1,2), Fraction(0), Fraction(1,2), Fraction(3,8), Fraction(1,8))
    print('PASS')


if __name__ == '__main__':
    main()
