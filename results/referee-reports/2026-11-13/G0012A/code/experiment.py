"""Reproducible NBW survival experiments. One process, one numerical thread."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR'] = str(ROOT / 'data' / 'mplconfig')
import argparse
import csv
from fractions import Fraction
import hashlib
import json
import math
import random
import resource
import time
import networkx as nx


def adjacency(g):
    return [sorted(g.neighbors(v)) for v in range(len(g))]


def validate(adj):
    n = len(adj)
    assert all(len(a) >= 3 and len(a) == len(set(a)) for a in adj)
    sets = [set(a) for a in adj]
    assert all(v != w and 0 <= w < n and v in sets[w] for v, a in enumerate(adj) for w in a)


def fingerprint(adj):
    h = hashlib.sha256()
    for v, a in enumerate(adj):
        h.update((str(v) + ':' + ','.join(map(str, a)) + '\n').encode())
    return h.hexdigest()


def biregular(n_target, high, seed):
    """Simple (3,high)-biregular graph, with deterministic duplicate repair."""
    rng = random.Random(seed)
    r = max(2, n_target // (high + 3))
    left, right = high * r, 3 * r
    ls = [i for i in range(left) for _ in range(3)]
    rs = [left + j for j in range(right) for _ in range(high)]
    rng.shuffle(rs)
    edges = list(zip(ls, rs))
    counts = {}
    for e in edges:
        counts[e] = counts.get(e, 0) + 1
    for i, (u, v) in enumerate(edges):
        if counts[u, v] == 1:
            continue
        for _ in range(100000):
            j = rng.randrange(len(edges))
            x, y = edges[j]
            if u != x and v != y and (u, y) not in counts and (x, v) not in counts:
                counts[u, v] -= 1
                counts[x, y] -= 1
                if not counts[x, y]:
                    del counts[x, y]
                counts[u, y] = counts[x, v] = 1
                edges[i], edges[j] = (u, y), (x, v)
                break
        else:
            raise RuntimeError('duplicate repair failed')
    adj = [[] for _ in range(left + right)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return [sorted(a) for a in adj]


def necklace(n):
    """Ring of K4-minus-edge cells; every vertex has degree three."""
    r = max(3, n // 4)
    g = nx.Graph()
    g.add_nodes_from(range(4*r))
    for t in range(r):
        b = 4*t
        for x in range(4):
            for y in range(x+1, 4):
                if (x, y) != (0, 1):
                    g.add_edge(b+x, b+y)
        g.add_edge(b+1, 4*((t+1) % r))
    return adjacency(g)


def halin(n):
    """Root of degree three, binary branching below it, leaf cycle."""
    height = max(2, int(math.log2((n+2)/3)))
    g = nx.Graph()
    g.add_node(0)
    leaves = [0]
    next_id = 1
    for depth in range(height):
        new = []
        for v in leaves:
            for _ in range(3 if depth == 0 else 2):
                g.add_edge(v, next_id)
                new.append(next_id)
                next_id += 1
        leaves = new
    g.add_edges_from(zip(leaves, leaves[1:] + leaves[:1]))
    return adjacency(g)


def hub_necklace(n, q=60):
    """Cycle of hubs, each joined to all vertices of its own q-cycle."""
    r = max(3, n // (q+1))
    g = nx.Graph()
    g.add_nodes_from(range(r*(q+1)))
    for t in range(r):
        g.add_edge(t, (t+1) % r)
        vs = list(range(r+t*q, r+(t+1)*q))
        g.add_edges_from((t, v) for v in vs)
        g.add_edges_from(zip(vs, vs[1:]+vs[:1]))
    return adjacency(g)


def exact_survival(adj, edge):
    """Exact rational DP on (previous,current,visited vertex mask)."""
    n = len(adj)
    u, v = edge
    states = {(u, v, (1 << u) | (1 << v)): Fraction(1)}
    result = {1: Fraction(1)}
    state_counts = {1: 1}
    for k in range(2, n+1):
        nxt = {}
        for (prev, curr, mask), mass in states.items():
            part = mass / (len(adj[curr])-1)
            for w in adj[curr]:
                if w != prev and not (mask >> w) & 1:
                    key = (curr, w, mask | (1 << w))
                    nxt[key] = nxt.get(key, Fraction()) + part
        states = nxt
        result[k] = sum(states.values(), Fraction())
        state_counts[k] = len(states)
    return result, state_counts


def simulate(adj, edge, trials, kmax, seed):
    rng = random.Random(seed)
    times = []
    for _ in range(trials):
        prev, curr = edge
        visited = {prev, curr}
        collision = kmax+1
        for k in range(2, kmax+1):
            a = adj[curr]
            w = a[rng.randrange(len(a)-1)]
            if w == prev:
                w = a[-1]
            if w in visited:
                collision = k
                break
            visited.add(w)
            prev, curr = curr, w
        times.append(collision)
    return times


def wilson(success, trials):
    z = 1.959963984540054
    p = success/trials
    den = 1 + z*z/trials
    center = (p+z*z/(2*trials))/den
    half = z*math.sqrt(p*(1-p)/trials+z*z/(4*trials*trials))/den
    return center-half, center+half


def run(trials):
    start = time.time()
    info = {'seed': 120526, 'trials_per_start': trials, 'nice': os.getpriority(os.PRIO_PROCESS, 0),
            'networkx': nx.__version__, 'graphs': [], 'caution': 'pointwise Wilson intervals; chosen starts, not worst-case optimization'}
    assert info['nice'] >= 10
    fields = ['family', 'target_n', 'n', 'graph_seed', 'min_degree', 'max_degree', 'start_u', 'start_v',
              'trials', 'k', 'k_over_sqrt_n', 'survivors', 'p', 'wilson_low', 'wilson_high']
    with (ROOT/'data/survival.csv').open('w') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for target in (1000, 10000, 100000):
            specs = [('random_cubic', 120526), ('random_cubic', 120527),
                     ('biregular_3_30', 120526), ('biregular_3_300', 120526),
                     ('circular_ladder', 0), ('cycle_necklace', 0), ('halin_tree_cycle', 0),
                     ('hub_necklace', 0), ('K_3_large', 0)]
            for family, seed in specs:
                if family == 'random_cubic':
                    adj = adjacency(nx.random_regular_graph(3, target, seed=seed))
                elif family.startswith('biregular'):
                    adj = biregular(target, int(family.rsplit('_', 1)[1]), seed)
                elif family == 'circular_ladder':
                    adj = adjacency(nx.circular_ladder_graph(target//2))
                elif family == 'cycle_necklace':
                    adj = necklace(target)
                elif family == 'halin_tree_cycle':
                    adj = halin(target)
                elif family == 'hub_necklace':
                    adj = hub_necklace(target)
                else:
                    adj = adjacency(nx.complete_bipartite_graph(3, target-3))
                validate(adj)
                n = len(adj)
                ds = list(map(len, adj))
                edge = (0, adj[0][0])
                edges = [edge]
                if min(ds) != max(ds):
                    edges.append((edge[1], edge[0]))
                graph_info = {'family': family, 'target_n': target, 'n': n, 'seed': seed,
                              'min_degree': min(ds), 'max_degree': max(ds), 'edges': sum(ds)//2,
                              'sha256_adjacency': fingerprint(adj), 'starts': edges}
                info['graphs'].append(graph_info)
                for u, v in edges:
                    ks = sorted(set(max(1, int(x*math.sqrt(n))) for x in (.25,.5,.75,1,1.5,2,3,4,6)))
                    times = simulate(adj, (u,v), trials, max(ks), seed+target+u+1009*v)
                    for k in ks:
                        count = sum(t > k for t in times)
                        lo, hi = wilson(count, trials)
                        writer.writerow(dict(zip(fields, [family,target,n,seed,min(ds),max(ds),u,v,trials,k,
                                                         k/math.sqrt(n),count,count/trials,lo,hi])))
                    with (ROOT/'data/collision_times.jsonl').open('a') as raw:
                        raw.write(json.dumps({'family': family, 'n': n, 'graph_seed': seed, 'start': [u,v],
                                              'kmax': max(ks), 'times': times})+'\n')
                f.flush()
                print(family, n, min(ds), max(ds), 'finished', flush=True)
    exact_rows = []
    for name, g in [('K4', nx.complete_graph(4)), ('K5_minus_edge', nx.complete_graph(5)),
                    ('cube', nx.cubical_graph()), ('petersen', nx.petersen_graph()),
                    ('K_3_8', nx.complete_bipartite_graph(3,8)),
                    ('ladder_12', nx.circular_ladder_graph(6))]:
        if name == 'K5_minus_edge':
            g.remove_edge(0,1)
        adj = adjacency(g)
        validate(adj)
        edge = (0, adj[0][0])
        probs, counts = exact_survival(adj, edge)
        # An independent Monte Carlo check of the entire exact curve.
        ts = simulate(adj, edge, 20000, len(adj), 9012+len(adj))
        for k, prob in probs.items():
            estimate = sum(t>k for t in ts)/len(ts)
            assert abs(estimate-float(prob)) <= 6*math.sqrt(float(prob)*(1-float(prob))/len(ts))+0.002
            exact_rows.append({'family':name,'n':len(adj),'start':edge,'k':k,
                               'probability':str(prob),'p':float(prob),'states':counts[k], 'mc_p':estimate})
    (ROOT/'data/exact.json').write_text(json.dumps(exact_rows, indent=2)+'\n')
    info.update(wall_seconds=time.time()-start, max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    (ROOT/'data/experiment_metadata.json').write_text(json.dumps(info,indent=2)+'\n')
    print('wall_seconds', info['wall_seconds'], 'max_rss_bytes', info['max_rss_bytes'], flush=True)


def plot():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    with (ROOT/'data/survival.csv').open() as f:
        rows = list(csv.DictReader(f))
    fig, axes = plt.subplots(2,4,figsize=(16,8), sharex=True, sharey=True)
    panels = [['random_cubic'],['biregular_3_30'],['biregular_3_300'],['circular_ladder'],
              ['cycle_necklace'],['halin_tree_cycle'],['hub_necklace'],['K_3_large']]
    colors = {'1000':'tab:blue','10000':'tab:orange','100000':'tab:green'}
    for ax, families in zip(axes.flat,panels):
        subset = [r for r in rows if r['family'] in families]
        keys = list(dict.fromkeys((r['family'],r['n'],r['graph_seed'],r['start_u'],r['start_v']) for r in subset))
        for key in keys:
            rs = [r for r in subset if (r['family'],r['n'],r['graph_seed'],r['start_u'],r['start_v'])==key]
            x = [float(r['k_over_sqrt_n']) for r in rs]
            y = [float(r['p']) for r in rs]
            reverse_start = int(key[3]) > int(key[4])
            second_seed = key[2]=='120527'
            label = f'n={key[1]}' if not reverse_start and not second_seed else None
            style = '--' if reverse_start else (':' if second_seed else '-')
            color = colors[rs[0]['target_n']]
            ax.plot(x,y,marker='.',linewidth=.9,alpha=.8,label=label,linestyle=style,color=color)
            ax.fill_between(x,[float(r['wilson_low']) for r in rs],
                            [float(r['wilson_high']) for r in rs],alpha=.06,color=color)
        ax.set_title(' / '.join(families).replace('_',' '))
        ax.grid(alpha=.2)
        ax.set_ylim(-.02,1.02)
        ax.set_xlabel(r'$k/\sqrt{n}$')
        ax.set_ylabel('P(simple)')
        ax.legend(fontsize=7)
        ax.tick_params(labelbottom=True)
    fig.suptitle('Non-backtracking walk survival: 4000 trials per selected start\n'
                 'Bands: pointwise 95% Wilson intervals; dashed: reverse start; dotted: second cubic graph seed',fontsize=12)
    fig.tight_layout()
    fig.savefig(ROOT/'data/survival.png',dpi=160)
    fig.savefig(ROOT/'data/survival.svg')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--trials',type=int,default=4000)
    parser.add_argument('--plot-only',action='store_true')
    args = parser.parse_args()
    if not args.plot_only:
        raw = ROOT/'data/collision_times.jsonl'
        raw.write_text('')
        run(args.trials)
    plot()
