"""Unstructured tree enumeration and deterministic lattice counterchecks."""
from collections import Counter
from itertools import combinations
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(600)
START = time.monotonic()
HERE = Path(__file__).resolve().parent


def full_tree_count(d, saved):
    # Independently reproduce the weighted module graph and classify every
    # subset of the needed size, without choosing local rooted forests.
    m, L = 2*d-2, 2*d-3
    root = 4*d
    edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 1),
             (1, root, m), (2, root, m),
             (0, 4, 1), (4, root, m+1), (3, 5, 1), (5, root, m+1)]
    for i in range(L):
        x, y = 6+2*i, 7+2*i
        edges += [(0, x, 1), (x, y, 1), (y, 3, 1), (x, root, m), (y, root, m)]
    def key(tree):
        tree = set(tree)
        direct = 1 if 4 in tree else 2 if 5 in tree else -1
        tails = tuple(tuple(i for i in range(2) if start+i in tree) for start in (6, 8))
        pairs = tuple(sorted(tuple(i for i in range(5) if 10+5*j+i in tree)
                             for j in range(L)))
        reflected_local = (2, 1, 0, 4, 3)
        reflected_pairs = tuple(sorted(tuple(sorted(reflected_local[i] for i in p)) for p in pairs))
        reflection = (3-direct if direct >= 0 else -1, tuple(reversed(tails)), reflected_pairs)
        return min((direct, tails, pairs), reflection)
    expected = Counter()
    for group in saved['groups']:
        expected[key(group['tree'])] += group['multiplicity']
    actual = Counter()
    candidates = 0
    for extra in combinations(range(3, len(edges)), root-3):
        candidates += 1
        parent = list(range(root+1))
        def find(a):
            while parent[a] != a:
                a = parent[a]
            return a
        tree = (0, 1, 2)+extra
        for i in tree:
            a, b = map(find, edges[i][:2])
            if a == b:
                break
            parent[a] = b
        else:
            # An acyclic graph with root edges on root+1 vertices is a tree.
            actual[key(tree)] += 1
    assert actual == expected
    assert sum(actual.values()) == saved['tree_count']
    return dict(d=d, candidates=candidates, trees=sum(actual.values()), groups=len(actual))


def edge(a, b):
    return tuple(sorted((a, b)))


def neighbors(v):
    for axis in range(len(v)):
        for sign in (-1, 1):
            w = list(v)
            w[axis] += sign
            yield tuple(w)


def mst(region, weights, omitted=None):
    root = len(region)
    ids = {p: i for i, p in enumerate(sorted(region))}
    parent = list(range(root+1))
    def find(a):
        while parent[a] != a:
            a = parent[a]
        return a
    accepted = set()
    for e, weight in sorted(weights.items(), key=lambda x: x[1]):
        if e == omitted or not any(p in region for p in e):
            continue
        a, b = (find(ids.get(p, root)) for p in e)
        if a != b:
            parent[a] = b
            accepted.add(e)
    return accepted


def lattice_checks():
    checks = 0
    for d in range(2, 13):
        o, v = (0,)*d, (1,)+(0,)*(d-1)
        for axis in range(1, d):
            for sign in (-1, 1):
                a = list(o)
                a[axis] = sign
                a = tuple(a)
                b = tuple(x+y for x, y in zip(a, v))
                path = {edge(o, a), edge(a, b), edge(b, v)}
                old = {o, a, b, v} | set(neighbors(o))
                new = old | set(neighbors(v))
                incident = {edge(p, q) for p in new for q in neighbors(p)}
                internal = {e for e in incident if all(p in new for p in e)}
                m = 2*d-2
                assert len(new) == 4*d and len(internal) == 3*m+3
                assert len(incident) == 2*m*m+5*m+5
                # All original edges are retained as separate independent labels.
                weights = {e: 100+i for i, e in enumerate(sorted(incident))}
                x = (2,)+(0,)*(d-1)
                far = tuple(p+q for p, q in zip(b, v))
                low = [edge(v, x), edge(b, far), edge(o, a), edge(a, b)]
                for i, e in enumerate(low, 1):
                    weights[e] = i
                weights[edge(b, v)] = 20
                assert not path.issubset(mst(old, weights))
                assert path.issubset(mst(new, weights))
                # Deleting a matched edge can create an invalid certificate.
                left = tuple(-z for z in a)
                right = tuple(p+q for p, q in zip(left, v))
                low = [edge(o, left), edge(left, right), edge(right, v),
                       edge(o, a), edge(a, b), edge(b, v)]
                weights = {e: 100+i for i, e in enumerate(sorted(incident))}
                for i, e in enumerate(low, 1):
                    weights[e] = i
                assert not path.issubset(mst(new, weights))
                assert path.issubset(mst(new, weights, omitted=edge(left, right)))
                checks += 1
    assert checks == 132
    return checks


def main():
    saved = json.loads((HERE/'audit.json').read_text())
    assert saved['status'] == 'PASS'
    tree_checks = []
    for row in saved['rows']:
        result = full_tree_count(row['d'], row)
        tree_checks.append(result)
        print('unstructured tree enumeration', json.dumps(result), 'PASS', flush=True)
    checks = lattice_checks()
    print('all square orientations d=2,...,12:', checks,
          'geometry, strict-inclusion witnesses and missing-edge counterexamples PASS', flush=True)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        rss *= 1024
    assert rss < 1024**3
    out = dict(status='PASS', tree_checks=tree_checks, oriented_lattice_checks=checks,
               usage=dict(seconds=time.monotonic()-START, peak_rss_bytes=rss,
                          nice=os.getpriority(os.PRIO_PROCESS, 0), threads=1, deadline=600))
    (HERE/'adversarial.json').write_text(json.dumps(out, indent=2)+'\n')
    print('PASS', json.dumps(out['usage']))


if __name__ == '__main__':
    main()
