#!/usr/bin/env python3
"""Independent local-state walk search, environment trace and exact algebra."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json
from math import comb, prod
import os
from pathlib import Path
import resource
import signal
import time

D = ((1, 0), (0, 1), (-1, 0), (0, -1))
TABLE = ((0, 1, 2, 3), (1, 0, 3, 2), (3, 2, 1, 0))


def circuit_key(corners):
    # Unordered maximal straight segments, with the mirror states at endpoints.
    seg = tuple(sorted(tuple(sorted((a, b))) for a, b in
                       zip(corners, corners[1:]+corners[:1])))
    mirrors = {}
    for i, (x, y) in enumerate(corners):
        a, b = corners[i-1], corners[(i+1) % len(corners)]
        dx, dy = (x > a[0])-(x < a[0]), (y > a[1])-(y < a[1])
        ex, ey = (b[0] > x)-(b[0] < x), (b[1] > y)-(b[1] < y)
        inc, out = D.index((dx, dy)), D.index((ex, ey))
        states = [s for s in (1, 2) if TABLE[s][inc] == out]
        assert len(states) == 1
        if (x, y) in mirrors:
            assert mirrors[x, y] == states[0]
        mirrors[x, y] = states[0]
    return seg, tuple(sorted((x, y, s) for (x, y), s in mirrors.items()))


def unit_walks(limit, bounded=False):
    counts = Counter()
    rank = {}
    box_counts = Counter()
    nodes = 0
    root_edge = ((0, 0), (1, 0))
    edges = {root_edge}
    path = [(0, 0), (1, 0)]

    def record(states, k):
        vs = path[:-1]
        visits = Counter(vs)
        t = sum(n-1 for v, n in visits.items() if states[v])
        c = sum(n-1 for v, n in visits.items() if not states[v])
        length = len(vs)
        assert all(n <= 2 for n in visits.values())
        assert sum(s != 0 for s in states.values()) == k-t
        assert len(states)-(k-t) == length-k-c
        counts[length, k, t, c] += 1
        if t+c:
            corners = tuple(v for i, v in enumerate(vs)
                            if (v[0]-vs[i-1][0], v[1]-vs[i-1][1]) !=
                            (vs[(i+1) % length][0]-v[0], vs[(i+1) % length][1]-v[1]))
            ox, oy = min(x for x, y in corners), min(y for x, y in corners)
            corners = tuple((x-ox, y-oy) for x, y in corners)
            xs, ys = {x for x, y in corners}, {y for x, y in corners}
            if xs == set(range(max(xs)+1)) and ys == set(range(max(ys)+1)):
                hs, vsums = Counter(), Counter()
                for a, b in zip(vs, vs[1:]+vs[:1]):
                    if a[1] == b[1]:
                        hs[min(a[0], b[0])-ox] += 1
                    else:
                        vsums[min(a[1], b[1])-oy] += 1
                assert all(n % 2 == 0 for n in (*hs.values(), *vsums.values()))
                h = tuple(hs[i]//2 for i in range(max(xs)))
                v = tuple(vsums[i]//2 for i in range(max(ys)))
                rank[circuit_key(corners)] = k, t, c, h, v
            if all(-1 <= x <= 1 and -1 <= y <= 1 for x, y in vs):
                box_counts[k-t, length-k-c] += 1

    def search(states, inc, k):
        nonlocal nodes
        nodes += 1
        pos = path[-1]
        for s in ((states[pos],) if pos in states else (0, 1, 2)):
            turns = k+(s != 0)
            if turns > 8:
                continue
            out = TABLE[s][inc]
            dx, dy = D[out]
            nxt = pos[0]+dx, pos[1]+dy
            edge = tuple(sorted((pos, nxt)))
            new = pos not in states
            if new:
                states[pos] = s
            if (pos, nxt) == root_edge:
                assert pos == root_edge[0]
                record(states, turns)
            elif (edge not in edges
                  and len(edges)+1+abs(nxt[0]-root_edge[0][0])+abs(nxt[1]-root_edge[0][1]) <= limit
                  and (not bounded or all(0 <= x <= 3 for x in nxt))):
                edges.add(edge)
                path.append(nxt)
                search(states, out, turns)
                path.pop()
                edges.remove(edge)
            if new:
                del states[pos]

    roots = [((0, y), (0, y+1)) for y in range(3)] if bounded else [root_edge]
    for root_edge in roots:
        edges = {tuple(sorted(root_edge))}
        path = list(root_edge)
        for initial in range(3):
            search({root_edge[0]: initial}, 1 if bounded else 0, 0)
    return counts, rank, box_counts, nodes


def environment_audit(box_counts):
    box = list(product(range(-1, 2), repeat=2))
    ix = {v: i for i, v in enumerate(box)}
    hist = Counter()
    raw = 0
    for cfg in product(range(3), repeat=9):
        pos, inc = (1, 0), 0
        visits = Counter()
        k = 0
        used = set()
        while pos in ix:
            state = cfg[ix[pos]]
            visits[pos] += 1
            k += state != 0
            out = TABLE[state][inc]
            dx, dy = D[out]
            nxt = pos[0]+dx, pos[1]+dy
            if (pos, nxt) == ((0, 0), (1, 0)):
                if k <= 8 and any(n > 1 for n in visits.values()):
                    raw += 1
                    m = sum(s != 0 for s in cfg)
                    hist[m] += 1
                break
            edge = tuple(sorted((pos, nxt)))
            assert edge not in used
            used.add(edge)
            pos, inc = nxt, out
    checks = []
    for p in (Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
        observed = sum(n*(p/2)**m*(1-p)**(9-m) for m, n in hist.items())
        predicted = sum(n*(p/2)**m*(1-p)**z for (m, z), n in box_counts.items())
        assert observed == predicted
        checks.append(dict(p=str(p), probability=str(observed)))
    return dict(environments=3**9, successes=raw,
                full_environment_mirror_histogram=dict(hist),
                orbit_weights=[dict(mirrors=m, empties=z, count=n) for (m, z), n in sorted(box_counts.items())],
                checks=checks)


def closed(p, k, t, c):
    q, d = 1-p, 2-p
    r = q*q
    if k == 6:
        return p*q/(8*d**5)
    if t:
        return p*p/(16*d**5)
    if c == 1:
        return p*q**3*(15+45*r+49*r*r+17*r**3)/(32*d**7*(1+r)**3)
    if c == 2:
        return 9*p*q*q/(64*d**7)
    assert c == 3
    return p*q**5*(2+r)/(16*d**7*(1+r)**3)


def formula_counts(m, k, t, c):
    if k == 6 or t:
        return 8*comb(m, 4) if m >= 4 else 0
    if c == 2:
        return 36*comb(m, 6) if m >= 6 else 0
    h = (120, 360, 392, 136) if c == 1 else (32, 16)
    shift = 6 if c == 1 else 8
    return sum(v*sum((-1)**j*comb(j+2, 2)*comb(m-shift-i-j+6, 6)
                     for j in range(m-shift-i+1))
               for i, v in enumerate(h) if m >= shift+i)


def audit_algebra(data):
    checks = []
    leading = Q(0)
    for f in data['families']:
        k, t, c = (f[s] for s in ('k', 't', 'c'))
        for m in range(41):
            assert formula_counts(m, k, t, c) == f['root_counts'][str(2*m)]
        # Leading gap poles, independently of the final closed probability.
        for g in f['groups']:
            a, b, n = (g[s] for s in ('ones', 'twos', 'count'))
            j = a+b
            assert k-t-j-1 >= 1
            if k-t-j-1 == 1:
                leading += Q(n*j, 2**(k-t+j+1+b))
        cutoff = 500
        ns = [formula_counts(m, k, t, c) for m in range(cutoff+1)]
        for p in (Q(1, 10), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
            q, r = 1-p, (1-p)**2
            value = closed(p, k, t, c)
            if q:
                total = Q(0)
                for g in f['groups']:
                    a, b, n = (g[s] for s in ('ones', 'twos', 'count'))
                    total += n*(r/(1-r))**a*(r*r/(1-r*r))**b*(Q(a)/(1-r)+Q(2*b)/(1-r*r))
                assert (p/2)**(k-t)*q**(-k-c)*total == value
            partial = sum(n*(p/2)**(k-t)*q**(2*m-k-c)
                          for m, n in enumerate(ns) if n)
            j = max(g['ones']+g['twos'] for g in f['groups'])
            count = sum(g['count'] for g in f['groups'])
            first = count*(cutoff+1)*comb(cutoff, j-1)*(p/2)**(k-t)*q**(2*(cutoff+1)-k-c)
            rho = r*Q(cutoff+2, cutoff+2-j)
            assert rho < 1
            tail = first/(1-rho)
            assert 0 <= value-partial <= tail < Q(1, 10**30)
            checks.append(dict(k=k, t=t, c=c, p=str(p), probability=str(value),
                               tail_bound_exact=str(tail)))
    assert leading == Q(37, 4096)
    # Second small-density calculation from the five displayed formulas.
    assert Q(1, 256)+Q(126, 32*2**7*8)+Q(9, 64*2**7)+Q(3, 16*2**7*8) == leading
    assert sum(closed(Q(1, 2), *s) for s in ((6, 0, 1), (8, 0, 1), (8, 0, 2), (8, 0, 3), (8, 1, 0))) == Q(164, 18225)
    for p in (Q(1, 10), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
        q, d, r = 1-p, 2-p, (1-p)**2
        total = sum(closed(p, f['k'], f['t'], f['c']) for f in data['families'])
        compact = (p/(16*d**4)+9*p*q*q/(64*d**7)
                   + p*q**3*(15+34*r+17*r*r)/(32*d**7*(1+r)**2))
        assert total == compact
        # Independent diagonal-rectangle sum: six outer mirrors and a shared
        # vertex that is either empty or carries the joining mirror.
        rectangles = (p/2)**6*(q+p/2)*8/(1-r)**5
        assert rectangles == p/(16*d**4)
    return checks, leading


def polynomial_audit(data):
    def mul(a, b):
        out = [0]*(len(a)+len(b)-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i+j] += x*y
        return out
    def power(a, n):
        out = [1]
        for _ in range(n):
            out = mul(out, a)
        return out
    def trim(a):
        while len(a) > 1 and a[-1] == 0:
            a.pop()
        return a
    for f in data['families']:
        groups = f['groups']
        ma = max(g['ones']+g['twos'] for g in groups)
        mb = max(g['twos'] for g in groups)
        common = [0]*30
        for g in groups:
            a, b, n = (g[s] for s in ('ones', 'twos', 'count'))
            term = mul(power([1, -1], ma-a-b), power([1, 1], mb-b))
            for i, x in enumerate(term):
                common[a+2*b+i] += n*x
        num, (a, b) = f['F_numerator'], f['F_poles']
        assert trim(common) == trim(mul(mul(num, power([1, -1], ma-a)), power([1, 1], mb-b)))
        dn = [i*num[i] for i in range(1, len(num))]
        first = mul(dn, [1, 0, -1])
        second = mul(num, [a-b, a+b])
        total = [0]*max(len(first), len(second))
        for i, x in enumerate(first): total[i] += x
        for i, x in enumerate(second): total[i] += x
        actual = trim([0]+total)
        if f['k'] == 6 or f['t']:
            expected, ga, gb = [0]*4+[8], 5, 0
        elif f['c'] == 1:
            expected, ga, gb = [0]*6+[120, 360, 392, 136], 7, 3
        elif f['c'] == 2:
            expected, ga, gb = [0]*6+[36], 7, 0
        else:
            expected, ga, gb = [0]*8+[32, 16], 7, 3
        assert actual == trim(mul(mul(expected, power([1, -1], a+1-ga)), power([1, 1], b+1-gb)))
    assert mul([1, 1], [15, 34, 17]) == [15, 49, 51, 17]
    print('PASS exact polynomial identities for every F and G', flush=True)


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
    signal.alarm(600)
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    start = time.monotonic()
    data = json.loads(Path('repeated_data.json').read_text())
    counts, rank, box_counts, nodes = unit_walks(16)
    expected = {circuit_key(tuple(map(tuple, s['corners']))):
                (s['k'], s['t'], s['c'], tuple(s['horizontal']), tuple(s['vertical']))
                for s in data['shapes']}
    assert rank == expected and len(rank) == 62
    for f in data['families']:
        for length in range(4, 17, 2):
            sig = (length, f['k'], f['t'], f['c'])
            assert counts[sig] == f['root_counts'][str(length)], (sig, counts[sig])
    assert not {sig for sig, n in counts.items() if n and sig[2]+sig[3]
                and (sig[1], sig[2], sig[3]) not in
                {(f['k'], f['t'], f['c']) for f in data['families']}}
    print('PASS independent state-carrying walks: every one of 62 rank circuits,')
    print('all rooted counts through 16; nodes='+str(nodes), flush=True)
    _, bounded_rank, _, bounded_nodes = unit_walks(24, bounded=True)
    assert bounded_rank == expected
    print('PASS exhaustive four-by-four-vertex state search: every circuit and both strip lists; nodes='+str(bounded_nodes), flush=True)
    env = environment_audit(box_counts)
    print('PASS all 19683 three-by-three environments:', env, flush=True)
    polynomial_audit(data)
    checks, leading = audit_algebra(data)
    print('PASS independent formulas, counts through 80, 25 exact sums/tails <1e-30, two small-p derivations', flush=True)
    base = Q(1459458421, 56687040000)
    result = dict(walk_nodes=nodes, bounded_walk_nodes=bounded_nodes, rank_count=len(rank),
                  root_counts=[dict(length=l, k=k, t=t, c=c, count=n) for (l, k, t, c), n in sorted(counts.items())],
                  environment_audit=env, checks=checks,
                  new_linear_coefficient=str(leading),
                  combined_linear_coefficient=str(Q(518043, 16777216)+leading),
                  new_half_density='164/18225', combined_half_density=str(base+Q(164, 18225)),
                  endpoint_new='1/16', endpoint_combined=str(Q(259, 2048)+Q(1, 16)),
                  elapsed_seconds=time.monotonic()-start,
                  priority=os.getpriority(os.PRIO_PROCESS, 0))
    Path('repeated_audit.json').write_text(json.dumps(result, indent=2)+'\n')
    result['full_peak_rss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert result['full_peak_rss_bytes'] < 1_000_000_000
    Path('repeated_audit.json').write_text(json.dumps(result, indent=2)+'\n')
    print({k: result[k] for k in ('new_linear_coefficient', 'combined_linear_coefficient', 'combined_half_density', 'endpoint_combined', 'elapsed_seconds', 'priority', 'full_peak_rss_bytes')}, flush=True)


if __name__ == '__main__':
    main()
