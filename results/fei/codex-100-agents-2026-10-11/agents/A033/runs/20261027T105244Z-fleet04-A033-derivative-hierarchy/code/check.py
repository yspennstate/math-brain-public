"""Frozen A033 flat-completion certificate v1; exact finite arithmetic."""
import argparse
import hashlib
import json
import time
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path

START = time.monotonic()
CHECKS = 0


def ck(v, label):
    global CHECKS
    CHECKS += 1
    if not v:
        raise AssertionError(label)
    if time.monotonic() - START > 55:
        raise TimeoutError('frozen 55-second runtime exceeded')


def walsh(v):
    a = list(v)
    step = 1
    while step < len(a):
        for j in range(0, len(a), 2 * step):
            for k in range(j, j + step):
                u, w = a[k], a[k + step]
                a[k], a[k + step] = u + w, u - w
        step *= 2
    return a


def bitdot(x, y):
    return (x & y).bit_count() % 2


def pack(x, indices):
    return sum(((x >> j) & 1) << k for k, j in enumerate(indices))


def embed(x, indices):
    return sum(((x >> k) & 1) << j for k, j in enumerate(indices))


def spectrum(v):
    return [F(w*w, len(v)**2) for w in walsh(v)]


def factors(n):
    d = 2
    while d*d <= n:
        while n % d == 0:
            yield d
            n //= d
        d += 1
    if n > 1:
        yield n


def entropy(p):
    z = {}
    for q in p:
        if not q:
            continue
        for prime in factors(q.numerator):
            z[prime] = z.get(prime, F(0)) - q
        for prime in factors(q.denominator):
            z[prime] = z.get(prime, F(0)) + q
    return {k: v for k, v in z.items() if v}


def add_scaled(out, v, weight):
    for p, c in v.items():
        out[p] = out.get(p, F(0)) + weight*c


def influence_edges(v, j):
    return F(sum(v[x] != v[x ^ (1 << j)] for x in range(len(v))), len(v))


def main(mode):
    maxm = 2 if mode == 'pilot' else 3
    functions = prefixes = direct = convolutions = 0
    for m in range(maxm + 1):
        for table in range(1 << (1 << m)):
            functions += 1
            g = [1 - 2*((table >> y) & 1) for y in range(1 << m)]
            pg = spectrum(g)
            ig = [influence_edges(g, j) for j in range(m)]
            root = [(-1 if bitdot(x, y) else 1)*g[y]
                    for y in range(1 << m) for x in range(1 << m)]
            wr = walsh(root)
            for a in range(1 << m):
                for b in range(1 << m):
                    ck(wr[a | (b << m)] == (1 << m)*(-1 if bitdot(a, b) else 1)*g[a], 'root signed phase')
            ck(all(p == F(1, 1 << (2*m)) for p in spectrum(root)), 'flat actual parent')
            ck(sum(influence_edges(root, j) for j in range(2*m)) == m, 'original influence')
            ck(all(v in [-1, 1] for v in root), 'full Booleanity')
            if m <= 2:
                for u in range(len(root)):
                    ck(sum(wr[s]*wr[s ^ u] for s in range(len(root))) == (len(root)**2 if u == 0 else 0), 'complete signed convolution')
                    convolutions += 1
            for k in range(m + 1):
                for Ktuple in combinations(range(m), k):
                    K = list(Ktuple)
                    J = [j for j in range(m) if j not in K]
                    r = len(J)
                    slice_h = {2: F(2*r)} if r else {}
                    for a in range(1 << r):
                        gs = [g[embed(a, J) | embed(z, K)] for z in range(1 << k)]
                        add_scaled(slice_h, entropy(spectrum(gs)), F(1, 1 << r))
                    for t in range(1 << k):
                        prefixes += 1
                        child = [(-1 if bitdot(embed(u, J) | embed(t, K), y) else 1)*g[y]
                                 for y in range(1 << m) for u in range(1 << r)]
                        wc = walsh(child)
                        for a in range(1 << r):
                            gs = [g[embed(a, J) | embed(z, K)] for z in range(1 << k)]
                            ws = walsh(gs)
                            for b in range(1 << m):
                                predicted = (1 << r)*(-1 if bitdot(a, pack(b, J)) else 1)*ws[pack(b, K) ^ t]
                                ck(wc[a | (b << r)] == predicted, 'all-prefix signed spectrum')
                        h = entropy([F(w*w, len(child)**2) for w in wc])
                        ck(h == {p:c for p,c in slice_h.items() if c}, 'all-prefix entropy exact prime-log vector')
                        ck(all(influence_edges(child, j) == F(1, 2) for j in range(r)), 'unqueried mask influence')
                        if k == m:
                            pc = [F(w*w, len(child)**2) for w in wc]
                            ck(all(pc[b] == pg[b ^ t] for b in range(1 << m)), 'ALL terminal core spectral translates')
                            ci = [influence_edges(child, j) for j in range(m)]
                            ck(all(ci[j] == (1-ig[j] if (t >> j) & 1 else ig[j]) for j in range(m)), 'terminal influences')
                            ck(sum(min(v, 1-v) for v in ci) == sum(min(v, 1-v) for v in ig), 'canonical influence invariant')
            for y in range(1 << m):
                easy = [(-1 if bitdot(x, y) else 1)*g[y] for x in range(1 << m)]
                ck(sum(bool(p) for p in spectrum(easy)) == 1, 'opposite policy has character terminals')
            if m <= 2:
                for a in range(1 << m):
                    for b in range(1 << m):
                        charsum = sum(root[x | (y << m)]*(-1 if bitdot(a, x) ^ bitdot(b, y) else 1)
                                      for x in range(1 << m) for y in range(1 << m))
                        ck(charsum == wr[a | (b << m)], 'independent direct character transform')
                        direct += 1
    result = {'status':'PASS','mode':mode,'functions':functions,'prefix_states':prefixes,'assertions':CHECKS,
              'direct_character_coefficients':direct,'complete_convolution_checks':convolutions,
              'seconds':time.monotonic()-START,'rung':'exact finite certificate; general theorem has analytic proof',
              'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).resolve().parents[1].joinpath('out', mode.upper()+'.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['pilot','main'])
    main(ap.parse_args().mode)
