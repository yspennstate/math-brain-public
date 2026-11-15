"""Independent killed-walk DP and NBW experiments. No claim code is used."""
import csv
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import random
import resource
import time

os.environ.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
import networkx as nx

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'


def adj_of(g):
    g = nx.convert_node_labels_to_integers(g)
    assert not g.is_multigraph() and nx.number_of_selfloops(g) == 0
    a = [tuple(sorted(g[v])) for v in range(len(g))]
    assert min(map(len, a)) >= 3
    assert all(v in a[w] for v, row in enumerate(a) for w in row)
    return a


def bound_params(a):
    q = Fraction(max(map(len, a)), min(map(len, a)) - 1)
    return q, 256*q*(1+q)*len(a)


def exact(a, edge):
    """All masses have denominator H**(k-1); transitions use integer factors.

    Keep the previous vertex explicitly: the forbidden back edge must remain in
    the transition denominator even though all visited destinations are killed.
    """
    n = len(a)
    h = math.lcm(*(len(row)-1 for row in a))
    u, v = edge
    states = {(1 << u | 1 << v, u, v): 1}
    denom = 1
    probabilities = [Fraction(1), Fraction(1)]
    state_counts = [0, 1]
    for k in range(2, n+1):
        nxt = defaultdict(int)
        for (visited, prev, cur), mass in states.items():
            factor = h // (len(a[cur])-1)
            for w in a[cur]:
                if w != prev and not (visited >> w & 1):
                    nxt[(visited | 1 << w, cur, w)] += mass * factor
        denom *= h
        states = nxt
        probabilities.append(Fraction(sum(states.values()), denom))
        state_counts.append(len(states))
    assert probabilities[-1] == 0
    assert all(x >= y for x, y in zip(probabilities, probabilities[1:]))
    return probabilities, state_counts


def enumerate_paths(a, edge, k):
    """Second implementation for selected tiny graphs: direct rational recursion."""
    def descend(path, weight):
        if len(path) == k+1:
            return weight
        prev, cur = path[-2:]
        return sum((descend(path + (w,), weight / (len(a[cur])-1))
                    for w in a[cur] if w != prev and w not in path), Fraction(0))
    return descend(tuple(edge), Fraction(1))


def exact_suite():
    cases = [(f'atlas_{i}', g) for i,g in enumerate(nx.graph_atlas_g())
             if len(g) >= 4 and min(dict(g.degree()).values()) >= 3]
    for n in range(8, 15):
        for seed in (1601, 1602):
            # An even-order cubic graph; for odd n, subdivide one edge and give
            # the added vertex a third neighbour. This preserves min degree 3.
            g = nx.random_regular_graph(3, n if n % 2 == 0 else n-1, seed=seed+n)
            if n % 2:
                u,v = next(iter(sorted(g.edges())))
                g.remove_edge(u,v)
                g.add_edges_from([(u,n-1),(n-1,v),(n-1,next(w for w in g if w not in (u,v)))])
            r = random.Random(7100+n+seed)
            for u,v in r.sample(list(nx.non_edges(g)), min(3, len(list(nx.non_edges(g))))):
                g.add_edge(u,v)
            cases.append((f'irregular_{n}_{seed}',g))
    cases.extend([
        ('petersen',nx.petersen_graph()),
        ('heawood',nx.heawood_graph()),
        ('K3_11',nx.complete_bipartite_graph(3,11)),
        ('disconnected_two_K4',nx.disjoint_union(nx.complete_graph(4),nx.complete_graph(4))),
    ])
    results = []
    total_starts = total_values = total_states = 0
    max_live = 0
    crosschecks = 0
    for name,g in cases:
        a = adj_of(g)
        q,b = bound_params(a)
        record = {'graph':name,'n':len(a),'adjacency':a,'Q':str(q),'B':str(b),'starts':[]}
        for u in range(len(a)):
            for v in a[u]:
                p,s = exact(a,(u,v))
                expectation = sum(p)
                assert float(expectation) <= 32*math.sqrt(float(q*(1+q)*len(a)))+2
                for k in range(1,len(a)+1):
                    assert p[k] <= min(Fraction(1),b/(k*k))
                if len(a) <= 5:
                    for k in range(1,len(a)+1):
                        assert enumerate_paths(a,(u,v),k) == p[k]
                        crosschecks += 1
                record['starts'].append({'edge':[u,v],'p':[str(x) for x in p],
                                         'E_tau':str(expectation),'live_states':s})
                total_starts += 1
                total_values += len(a)
                total_states += sum(s)
                max_live = max(max_live,max(s))
        results.append(record)
    (DATA/'exact_all_starts.json').write_text(json.dumps(results,indent=2)+'\n')
    return {'graphs':len(results),'starts':total_starts,'probabilities':total_values,
            'processed_states':total_states,'max_live_states':max_live,
            'direct_enumeration_crosschecks':crosschecks,
            'nontrivial_bound_checks':0,
            'note':'For every n<=14 case, B/k^2>=1 whenever k<n; finite tests check the law, not the nontrivial asymptotic tail.'}


def sample_tau(a, edge, rng):
    prev,cur = edge
    visited = {prev,cur}
    k = 1
    while True:
        # Rejection of the previous vertex samples uniformly among d(cur)-1
        # possibilities, independently at each time. Avoid a self-avoiding law.
        row = a[cur]
        w = row[rng.randrange(len(row))]
        while w == prev:
            w = row[rng.randrange(len(row))]
        k += 1
        if w in visited:
            return k
        visited.add(w)
        prev,cur = cur,w


def interval(successes,trials,z=1.959963984540054):
    p = successes/trials
    d = 1+z*z/trials
    c = (p+z*z/(2*trials))/d
    r = z*math.sqrt(p*(1-p)/trials+z*z/(4*trials*trials))/d
    return max(0,c-r), min(1,c+r)


def large_cases():
    for n in (4096,16384,65536):
        base = nx.random_regular_graph(3,n,seed=811+n)
        yield f'cubic_{n}',base,[(0,min(base[0]))]
        # A few hubs with degree approximately sqrt(n), plus cubic base.
        g = base.copy()
        rng = random.Random(819+n)
        s = math.isqrt(n)
        for j in range(3):
            g.add_edges_from((n+j,w) for w in rng.sample(range(n),s))
        hub = n
        ngh = min(g[hub])
        ordinary = next((u,v) for u,v in sorted(g.edges()) if u<n and v<n and g.degree(u)==g.degree(v)==3)
        yield f'three_sqrt_hubs_{n}',g,[(hub,ngh),(ngh,hub),ordinary]
        # Bounded ratio m=3, M<=5 (add a disjoint matching to half the base).
        g = base.copy()
        vertices = list(range(n))
        rng.shuffle(vertices)
        for u,v in zip(vertices[:n//2:2],vertices[1:n//2:2]):
            if not g.has_edge(u,v):
                g.add_edge(u,v)
        e = next((u,v) for u,v in sorted(g.edges()) if g.degree(u)!=g.degree(v))
        yield f'degree_3_4_{n}',g,[e,e[::-1]]
    n = 4096
    g = nx.complete_bipartite_graph(3,n-3)
    yield 'K3_4093',g,[(0,3),(3,0)]
    # Cubic ladder with a hub attached to every sqrt(n)-th vertex.
    g = nx.circular_ladder_graph(2048)
    g.add_edges_from((4096,w) for w in range(0,4096,64))
    yield 'ladder_with_hub',g,[(4096,0),(0,4096),(1,2)]


def monte_carlo(trials=5000):
    rows = []
    metadata = []
    raw = []
    nstarts = nontrivial = 0
    for name,g,starts in large_cases():
        a = adj_of(g)
        q,b = bound_params(a)
        meta = {'graph':name,'n':len(a),'min_degree':min(map(len,a)),
                'max_degree':max(map(len,a)),'Q':str(q),'B':str(b),'starts':starts,
                'edges_sha256':hashlib.sha256(repr(sorted(g.edges())).encode()).hexdigest()}
        metadata.append(meta)
        for index,edge in enumerate(starts):
            rng = random.Random(917003 + nstarts)
            times = [sample_tau(a,edge,rng) for _ in range(trials)]
            raw.append({'graph':name,'start':edge,'seed':917003+nstarts,'tau':times})
            nstarts += 1
            ks = sorted(set([1,2,3,len(a)-1,len(a)] +
                [max(1,round(s*math.sqrt(len(a)))) for s in (.25,.5,1,2,4,8,16,24,32,48,64,96,128)] +
                [math.ceil(math.sqrt(float(b))*s) for s in (1.01,2,4)]))
            ks = [k for k in ks if k <= len(a)]
            for k in ks:
                surviving = sum(t>k for t in times)
                lo,hi = interval(surviving,trials)
                bd = min(1,float(b)/(k*k))
                if k<len(a) and bd<1:
                    nontrivial += 1
                # A six-standard-error screen, not a proof or simultaneous CI.
                assert surviving/trials <= bd+6*math.sqrt(max(bd*(1-bd),1/trials)/trials)
                rows.append({'graph':name,'n':len(a),'start':str(edge),'k':k,
                    'k_over_sqrt_n':k/math.sqrt(len(a)),'trials':trials,'survivors':surviving,
                    'p_hat':surviving/trials,'wilson_lo':lo,'wilson_hi':hi,'bound':bd,
                    'mean_tau':sum(times)/trials,'max_tau':max(times),
                    'expectation_bound':32*math.sqrt(float(q*(1+q)*len(a)))+2})
        print('finished', name, flush=True)
    (DATA/'mc_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
    with (DATA/'collision_times.jsonl').open('w') as f:
        for record in raw:
            f.write(json.dumps(record)+'\n')
    with (DATA/'monte_carlo.csv').open('w',newline='') as f:
        w = csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return {'graphs':len(metadata),'starts':nstarts,'trials_per_start':trials,
            'walks':nstarts*trials,'rows':len(rows),'nontrivial_tail_rows':nontrivial,
            'largest_n':max(r['n'] for r in metadata),'all_six_se_screen_checks_passed':True}


def main():
    assert os.getpriority(os.PRIO_PROCESS,0) >= 10
    DATA.mkdir(exist_ok=True)
    t = time.monotonic()
    result = {'exact':exact_suite()}
    print(json.dumps(result), flush=True)
    result['monte_carlo'] = monte_carlo()
    result.update(seconds=time.monotonic()-t, peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  nice=os.getpriority(os.PRIO_PROCESS,0),threads=1,networkx=nx.__version__)
    (DATA/'probability_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__ == '__main__':
    main()
