import itertools, math
import numpy as np


def circular_L(m, r):
    k = r / math.sqrt(1.0 + r*r)
    t = 1.0 / math.sqrt(1.0 + r*r)
    cols = [np.array([k, 0.0, 0.0])]
    for j in range(m):
        th = 2.0 * math.pi * j / m
        cols.append(np.array([
            t / math.sqrt(m),
            math.sqrt(2.0/m) * math.cos(th),
            math.sqrt(2.0/m) * math.sin(th),
        ]))
    return np.column_stack(cols), k, t


def check(m, r):
    L, k, t = circular_L(m, r)
    assert np.max(np.abs(L @ L.T - np.eye(3))) < 1e-10

    W = {0: 0.0, 1: 0.0}
    bases = []
    for S in itertools.combinations(range(m+1), 3):
        d2 = float(np.linalg.det(L[:, S])**2)
        if d2 < 1e-26:
            continue
        a = int(0 in S)
        W[a] += d2
        bases.append((S, d2, a))

    assert abs(W[1] - k*k) < 1e-10
    assert abs(W[0] - t*t) < 1e-10

    marginal = np.zeros(m+1)
    Zlog = 0.0
    entropy = 0.0
    for S, d2, a in bases:
        p = 0.5 * d2 / W[a]
        entropy -= p * math.log(p)
        Zlog += p * math.log(d2)
        for i in S:
            marginal[i] += p

    assert abs(marginal[0] - 0.5) < 1e-10
    assert np.max(np.abs(marginal[1:] - 5.0/(2.0*m))) < 1e-10
    Z = math.exp(entropy + Zlog)
    assert abs(Z - 2.0*k*t) < 1e-10

    a = 5.0/(2.0*m)
    Bm = 2.0**0.25 * (1.0-a)**(-m*(1.0-a)/2.0)
    C = 3.0 * Bm**(2.0/3.0) * ((1.0+r*r)/(2.0*r))**(1.0/3.0)
    return W[0], W[1], Z, Bm, C


if __name__ == '__main__':
    for m in (5, 6, 8, 54):
        print('m=', m, 'r=3', check(m, 3.0))
    limit_prefactor = 3.0 * 2.0**(1.0/6.0) * math.exp(5.0/6.0)
    print('uniform_m_prefactor_limit=', limit_prefactor)
