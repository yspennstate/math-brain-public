#!/usr/bin/env python3
"""Exact rank enumeration of compatible circuits with at most eight turns."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
import json
from math import prod
import os
from pathlib import Path
import resource
import signal
import time


def guard():
    resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
    signal.alarm(600)
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15


def canonical(corners):
    v = tuple(corners)
    return min(w[i:]+w[:i] for w in (v, v[::-1]) for i in range(len(v)))


def expand(corners):
    path = []
    for (x, y), (u, v) in zip(corners, corners[1:]+corners[:1]):
        dx, dy = (u > x)-(u < x), (v > y)-(v < y)
        assert (dx == 0) != (dy == 0)
        while (x, y) != (u, v):
            path.append((x, y))
            x, y = x+dx, y+dy
    return path


def signature(path):
    """Reject repeated edges and incompatible uses of a local scatterer."""
    edges = [tuple(sorted((v, path[(i+1) % len(path)])))
             for i, v in enumerate(path)]
    if len(set(edges)) != len(edges):
        return None
    states = {}
    visits = Counter(path)
    k = 0
    for i, v in enumerate(path):
        prev, nxt = path[i-1], path[(i+1) % len(path)]
        dx, dy = v[0]-prev[0], v[1]-prev[1]
        ex, ey = nxt[0]-v[0], nxt[1]-v[1]
        if (ex, ey) == (dx, dy):
            state = 0
        elif (ex, ey) == (dy, dx):
            state = 1
        elif (ex, ey) == (-dy, -dx):
            state = 2
        else:
            return None
        k += state != 0
        if v in states and states[v] != state:
            return None
        states[v] = state
    assert max(visits.values()) <= 2
    c = sum(n-1 for v, n in visits.items() if states[v] == 0)
    t = sum(n-1 for v, n in visits.items() if states[v] != 0)
    assert sum(s != 0 for s in states.values()) == k-t
    assert sum(s == 0 for s in states.values()) == len(path)-k-c
    return k, t, c


def classify(k):
    n = k//2
    words = [s for a in range(2, n+1) for s in product(range(a), repeat=n)
             if len(set(s)) == a and all(s[i] != s[i-1] for i in range(n))]
    found = {}
    representations = 0
    for xs, ys in product(words, repeat=2):
        corners = tuple(z for i in range(n) for z in
                        ((xs[i], ys[i]), (xs[(i+1) % n], ys[i])))
        path = expand(corners)
        sig = signature(path)
        if sig is None:
            continue
        assert sig[0] == k
        h = tuple(sum(min(xs[i], xs[(i+1) % n]) <= j <
                      max(xs[i], xs[(i+1) % n]) for i in range(n))//2
                  for j in range(max(xs)))
        v = tuple(sum(min(ys[i], ys[(i+1) % n]) <= j <
                      max(ys[i], ys[(i+1) % n]) for i in range(n))//2
                  for j in range(max(ys)))
        assert all(c in (1, 2) for c in h+v)
        key = canonical(corners)
        if key in found:
            assert found[key] == (sig, h, v)
        found[key] = sig, h, v
        representations += 1
    assert representations == k*len(found)
    return found, dict(word_count=len(words), candidates=len(words)**2,
                      representations=representations, count=len(found))


def gap_coefficients(gaps, limit):
    out = [1]+[0]*limit
    for c in gaps:
        nxt = [0]*(limit+1)
        for m in range(c, limit+1):
            nxt[m] = out[m-c]+nxt[m-c]
        out = nxt
    return out


def multiply(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def power(a, n):
    out = [1]
    for _ in range(n):
        out = multiply(out, a)
    return out


def trim(a):
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def divide(a, sign):
    if len(a) <= 1:
        return None
    out = [a[0]]
    for x in a[1:-1]:
        out.append(x-sign*out[-1])
    return trim(out) if a[-1] == sign*out[-1] else None


def rational(groups):
    amax = max(a+b for a, b in groups)
    bmax = max(b for a, b in groups)
    num = [0]*(4*amax+1)
    for (a, b), count in groups.items():
        p = multiply(power([1, -1], amax-a-b), power([1, 1], bmax-b))
        for i, x in enumerate(p):
            num[a+2*b+i] += count*x
    num = trim(num)
    poles = [amax, bmax]
    for i, sign in enumerate((-1, 1)):
        while poles[i]:
            q = divide(num, sign)
            if q is None:
                break
            num = q
            poles[i] -= 1
    return num, poles


def evaluate(poly, r):
    out = Q(0)
    for c in reversed(poly):
        out = out*r+c
    return out


def root_rational(num, poles, r):
    a, b = poles
    f = evaluate(num, r)/((1-r)**a*(1+r)**b)
    dn = [i*num[i] for i in range(1, len(num))]
    return r*(evaluate(dn, r)/((1-r)**a*(1+r)**b)
              + f*(Q(a)/(1-r)-Q(b)/(1+r)))


def main():
    guard()
    start = time.monotonic()
    shapes = []
    groups = Counter()
    stats = {}
    for k in (4, 6, 8):
        found, stats[k] = classify(k)
        print('k='+str(k)+': '+str(stats[k]), flush=True)
        simple = sum(sig[1:] == (0, 0) for sig, h, v in found.values())
        assert simple == {4: 1, 6: 4, 8: 38}[k]
        for corners, (sig, h, v) in sorted(found.items()):
            k, t, c = sig
            if t+c == 0:
                continue
            groups[k, t, c, (h+v).count(1), (h+v).count(2)] += 1
            shapes.append(dict(corners=corners, k=k, t=t, c=c,
                               horizontal=h, vertical=v))
    families = []
    checks = defaultdict(Q)
    for k, t, c in sorted({g[:3] for g in groups}):
        table = {(a, b): count for (kk, tt, cc, a, b), count in groups.items()
                 if (kk, tt, cc) == (k, t, c)}
        num, poles = rational(table)
        coeff = [0]*41
        for (a, b), count in table.items():
            seq = gap_coefficients((1,)*a+(2,)*b, 40)
            coeff = [u+count*w for u, w in zip(coeff, seq)]
        values = []
        for p in (Q(1, 10), Q(1, 4), Q(1, 2), Q(3, 4)):
            q, r = 1-p, (1-p)**2
            direct = Q(0)
            for s in shapes:
                if (s['k'], s['t'], s['c']) != (k, t, c):
                    continue
                h, v = s['horizontal'], s['vertical']
                direct += prod(r**d/(1-r**d) for d in h+v)*sum(Q(2*d)/(1-r**d) for d in h)
            assert direct == root_rational(num, poles, r)
            probability = (p/2)**(k-t)*q**(-k-c)*direct
            values.append(dict(p=str(p), probability=str(probability)))
            checks[p] += probability
        entry = dict(k=k, t=t, c=c,
                     groups=[dict(ones=a, twos=b, count=count) for (a, b), count in sorted(table.items())],
                     F_numerator=num, F_poles=poles,
                     root_counts={str(2*m): m*x for m, x in enumerate(coeff)}, checks=values)
        families.append(entry)
        print({key: value for key, value in entry.items() if key != 'root_counts'}, flush=True)
        print('counts 8..20:', {l: n for l, n in entry['root_counts'].items() if 8 <= int(l) <= 20}, flush=True)
    out = dict(stats=stats, shapes=shapes, families=families,
               checks=[dict(p=str(p), probability=str(v)) for p, v in checks.items()],
               elapsed_seconds=time.monotonic()-start,
               priority=os.getpriority(os.PRIO_PROCESS, 0))
    Path('repeated_data.json').write_text(json.dumps(out, indent=2)+'\n')
    out['full_peak_rss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert out['full_peak_rss_bytes'] < 1_000_000_000
    Path('repeated_data.json').write_text(json.dumps(out, indent=2)+'\n')
    print('total:', out['checks'])
    print('non-simple rank circuits:', len(shapes))
    print('resources:', {key: out[key] for key in ('elapsed_seconds', 'priority', 'full_peak_rss_bytes')})


if __name__ == '__main__':
    main()
