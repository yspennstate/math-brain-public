"""Exact reversible-chain calculations, with independent hitting-system checks."""
from fractions import Fraction as F
import json


def inverse(a):
    n = len(a)
    b = [[F(x) for x in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for j in range(n):
        k = next(i for i in range(j, n) if b[i][j])
        b[j], b[k] = b[k], b[j]
        c = b[j][j]
        b[j] = [x / c for x in b[j]]
        for i in range(n):
            if i != j:
                c = b[i][j]
                b[i] = [x - c*y for x, y in zip(b[i], b[j])]
    return [row[n:] for row in b]


def lump(w, pair):
    n = len(w)
    a, b = sorted(pair)
    groups = [[i] if i != a else [a, b] for i in range(n) if i != b]
    return [[sum(w[i][j] for i in x for j in y) for y in groups]
            for x in groups], groups


def calculate(w, check=True):
    n = len(w)
    w = [[F(x) for x in row] for row in w]
    d = list(map(sum, w))
    total = sum(d)
    pi = [x / total for x in d]
    lap = [[(d[i] - w[i][i]) if i == j else -w[i][j]
            for j in range(n)] for i in range(n)]
    k0 = inverse([row[:-1] for row in lap[:-1]])
    k = [row + [F(0)] for row in k0] + [[F(0)] * n]
    a = [sum(k[i][j]*d[j] for j in range(n)) for i in range(n)]
    mu = sum(pi[i]*a[i] for i in range(n))
    dev = [[a[i]+a[j]-mu-total*k[i][j] for j in range(n)]
           for i in range(n)]
    h = [[a[i]-a[j]-total*(k[i][j]-k[j][j]) for j in range(n)]
         for i in range(n)]
    tm = max(map(max, dev))
    pairs = [[i,j] for i in range(n) for j in range(n) if dev[i][j] == tm]
    tau0 = sum(pi[j]*h[0][j] for j in range(n))
    if check:
        # Independently solve a killed hitting system for every target.
        for target in range(n):
            ix = [i for i in range(n) if i != target]
            inv = inverse([[lap[i][j] for j in ix] for i in ix])
            hh = [sum(inv[r][s]*d[j] for s,j in enumerate(ix))
                  for r in range(n-1)]
            assert all(h[i][target] == hh[r] for r,i in enumerate(ix))
            mean = sum(pi[i]*h[i][target] for i in range(n))
            assert all(dev[i][target] == h[i][target]-mean for i in range(n))
        # Explicit optimal stopping occupation certificates for each start.
        for start in range(n):
            ti = max(dev[start])
            v = [pi[j]*(ti-dev[start][j]) for j in range(n)]
            assert min(v) == 0 and sum(v) == ti
            for j in range(n):
                assert v[j]-sum(v[i]*w[i][j]/d[i] for i in range(n)) == F(start==j)-pi[j]
    return dict(tmix=tm, tau0=tau0, pairs=pairs, dev=dev, hitting=h,
                degrees=d, total=total, pi=pi)


def leaf_family(m, t):
    w = [[0]*(m+2) for _ in range(m+2)]
    for i in range(m):
        w[i][i] = t*t-1
        w[i][m] = w[m][i] = 1
        w[i][m+1] = w[m+1][i] = t
    w[m+1][m+1] = t**6
    return w


def save_json(path, obj):
    with open(path, 'w') as f:
        json.dump(obj, f, indent=2, default=str)


if __name__ == '__main__':
    records = []
    for m in (2,3,4,5):
        for t in (2,10,100,1000,1000000):
            w = leaf_family(m,t)
            hw, groups = lump(w, (m,m+1))
            x, y = calculate(w), calculate(hw)
            row = dict(n=m+2,t=t, original=x['tmix'],quotient=y['tmix'],
                       ratio=y['tmix']/x['tmix'], original_pairs=x['pairs'],
                       quotient_pairs=y['pairs'], tau0_quotient=y['tau0'])
            records.append(row)
            print(f"n={m+2} t={t} ratio={float(row['ratio']):.12f} "
                  f"X={row['original']} hX={row['quotient']} "
                  f"pairs={x['pairs']}/{y['pairs']}")
    save_json('leaf_exact.json', records)
