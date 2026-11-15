"""Finite, exact audit of weighted routing identities, written for this review."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations, product
import json
import os
from pathlib import Path
import random
import time
import networkx as nx

ROOT = Path(__file__).resolve().parents[1]
COUNTS = defaultdict(int)


def local_data(a):
    choices = []
    inverses = []
    for row in a:
        ds = [dict(zip(row,p)) for p in permutations(row) if all(u!=v for u,v in zip(row,p))]
        lookup = {tuple(d[u] for u in row): i for i,d in enumerate(ds)}
        inv = []
        for d in ds:
            r = {v:u for u,v in d.items()}
            inv.append(lookup[tuple(r[u] for u in row)])
        choices.append(ds)
        inverses.append(inv)
    return choices,inverses


def walk(plan, ds, start, k):
    p = list(start)
    for _ in range(k-1):
        p.append(ds[p[-1]][plan[p[-1]]][p[-2]])
    return p


def first_repeat(path):
    seen = set()
    for j,v in enumerate(path):
        if v in seen:
            return j
        seen.add(v)
    return None


def excursion(plan, ds, path, i, z, L):
    e = [path[i],z]
    while e[-1] not in path and len(e)-1 < L:
        e.append(ds[e[-1]][plan[e[-1]]][e[-2]])
    bad = first_repeat(path[:i] + e) is not None
    return e,bad


def audit_graph(name,g):
    a = [tuple(sorted(g[v])) for v in range(len(g))]
    ds, inv = local_data(a)
    plans = list(product(*(range(len(x)) for x in ds)))
    q = F(max(map(len,a)), min(map(len,a))-1)
    for u in range(len(a)):
        for v in a[u]:
            for k in range(2,len(a)):
                simple = [(p,walk(p,ds,(u,v),k)) for p in plans]
                simple = [(p,x) for p,x in simple if first_repeat(x) is None]
                for L in range(1,len(a)+2):
                    incoming = defaultdict(F)
                    bad_mass = total_mass = F(0)
                    for p,x in simple:
                        used = set()
                        terminal = set()
                        for i in range(1,k):
                            w = F(1,len(a[x[i]])-1)
                            for z in a[x[i]]:
                                if z in (x[i-1],x[i+1]):
                                    continue
                                total_mass += w
                                e,bad = excursion(p,ds,x,i,z,L)
                                if bad:
                                    bad_mass += w
                                returning = e[-1] in x
                                COUNTS['departures'] += 1
                                if not returning and not bad:
                                    edges = set(zip(e,e[1:]))
                                    assert len(edges)==L and used.isdisjoint(edges)
                                    used.update(edges)
                                    COUNTS['nonreturn_pieces'] += 1
                                if returning and e[-1]==x[-1]:
                                    last = tuple(e[-2:])
                                    assert last not in terminal
                                    terminal.add(last)
                                    COUNTS['terminal_injections'] += 1
                                if returning and e[-1] in x[1:-1]:
                                    ell = x.index(e[-1])
                                    rev = list(p)
                                    for y in set(e[1:-1]):
                                        rev[y] = inv[y][rev[y]]
                                    rev = tuple(rev)
                                    assert walk(rev,ds,(u,v),k)==x
                                    assert e[-2] not in (x[ell-1],x[ell+1])
                                    er,br = excursion(rev,ds,x,ell,e[-2],L)
                                    assert er==e[::-1] and (bad or br)
                                    back = list(rev)
                                    for y in set(er[1:-1]):
                                        back[y] = inv[y][back[y]]
                                    assert tuple(back)==p
                                    wr = F(1,len(a[x[ell]])-1)
                                    assert 1/q <= w/wr <= q
                                    COUNTS['reversals'] += 1
                                    if len(set(e[1:-1])) < len(e[1:-1]):
                                        COUNTS['reversals_with_repeated_exterior_vertex'] += 1
                                if bad and i <= k-L:
                                    d = x[i]
                                    for s,local in enumerate(ds[d]):
                                        if local[x[i-1]]!=z:
                                            continue
                                        out = list(p)
                                        out[d] = s
                                        out = tuple(out)
                                        j = first_repeat(walk(out,ds,(u,v),k))
                                        assert j is not None and i<j<=i+L
                                        incoming[out] += F(1,len(ds[d]))
                                        COUNTS['replacements'] += 1
                        assert len(used) <= sum(map(len,a))
                        assert len(terminal) <= len(a[x[-1]])
                    assert (1+q)*bad_mass >= total_mass-len(simple)*(q*len(a)/L+q)
                    for value in incoming.values():
                        assert value <= L
                        COUNTS['output_congestion'] += 1
                    COUNTS['aggregate_inequalities'] += 1
    return {'graph':name,'n':len(a),'plans':len(plans),'starting_edges':sum(map(len,a))}


def repeated_vertex_checks():
    """Larger random plans to exercise returning excursions with repeated vertices."""
    rng = random.Random(114901)
    g = nx.random_regular_graph(4,12,seed=114901)
    # Removing a matching makes the example irregular with degrees 3 and 4.
    g.remove_edges_from([(0,next(iter(g[0])))])
    a = [tuple(sorted(g[v])) for v in range(len(g))]
    ds,inv = local_data(a)
    count = 0
    attempts = 0
    for _ in range(30000):
        p = tuple(rng.randrange(len(d)) for d in ds)
        u = rng.randrange(len(a))
        start = (u,rng.choice(a[u]))
        k = rng.choice((2,3,4,5))
        x = walk(p,ds,start,k)
        if first_repeat(x) is not None:
            continue
        for i in range(1,k):
            for z in a[x[i]]:
                if z in (x[i-1],x[i+1]):
                    continue
                e,bad = excursion(p,ds,x,i,z,30)
                if e[-1] not in x[1:-1]:
                    continue
                attempts += 1
                rev = list(p)
                for y in set(e[1:-1]):
                    rev[y] = inv[y][rev[y]]
                ell = x.index(e[-1])
                er,br = excursion(tuple(rev),ds,x,ell,e[-2],30)
                assert er==e[::-1] and (bad or br)
                if len(set(e[1:-1]))<len(e[1:-1]):
                    count += 1
    assert count>0
    return {'interior_return_checks':attempts,'repeated_exterior_vertex_checks':count,'seed':114901}


def main():
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    t = time.monotonic()
    g = nx.complete_graph(5)
    g.remove_edge(0,1)
    graphs = [audit_graph('K4',nx.complete_graph(4)),audit_graph('K5_minus_edge',g),
              audit_graph('K3_3',nx.complete_bipartite_graph(3,3))]
    results = {'exhaustive':graphs,'counts':dict(COUNTS),'random_reversals':repeated_vertex_checks(),
               'seconds':time.monotonic()-t,'nice':os.getpriority(os.PRIO_PROCESS,0)}
    (ROOT/'data'/'routing_summary.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))


if __name__=='__main__':
    main()
