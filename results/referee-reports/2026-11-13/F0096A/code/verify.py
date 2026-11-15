"""Independent checks of saved simple graphs and Hamilton cycle certificates."""
import collections
import csv
import hashlib
import json
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]

def read_graph(stem):
    raw = (ROOT / (stem + '.bin')).read_bytes()
    n, m = struct.unpack_from('=ii', raw)
    assert len(raw) == 8 + 8*m
    adj = [set() for _ in range(n)]
    for u, v in struct.iter_unpack('=ii', raw[8:]):
        assert 0 <= u < n and 0 <= v < n and u != v
        assert v not in adj[u]
        adj[u].add(v)
        adj[v].add(u)
    assert min(map(len, adj)) >= 3
    return adj, m, hashlib.sha256(raw).hexdigest()

def check(stem):
    adj, m, digest = read_graph(stem)
    n = len(adj)
    cycle = list(map(int, (ROOT / (stem + '.cycle')).read_text().split()))
    valid = False
    if cycle:
        assert len(cycle) == n and len(set(cycle)) == n
        assert min(cycle) == 0 and max(cycle) == n-1
        assert all(cycle[(i+1) % n] in adj[u] for i, u in enumerate(cycle))
        valid = True
    # Iterative DFS counts components, bridges and articulation vertices.
    tin = [-1]*n
    low = [0]*n
    parent = [-1]*n
    children = [0]*n
    cut = set()
    bridges = 0
    components = 0
    timer = 0
    for root in range(n):
        if tin[root] >= 0:
            continue
        components += 1
        tin[root] = low[root] = timer
        timer += 1
        stack = [(root, iter(adj[root]))]
        while stack:
            v, it = stack[-1]
            w = next(it, None)
            if w is None:
                stack.pop()
                p = parent[v]
                if p >= 0:
                    low[p] = min(low[p], low[v])
                    bridges += low[v] > tin[p]
                    if parent[p] >= 0 and low[v] >= tin[p]:
                        cut.add(p)
                elif children[v] > 1:
                    cut.add(v)
                continue
            if w == parent[v]:
                continue
            if tin[w] >= 0:
                low[v] = min(low[v], tin[w])
            else:
                children[v] += 1
                parent[w] = v
                tin[w] = low[w] = timer
                timer += 1
                stack.append((w, iter(adj[w])))
    hist = dict(sorted(collections.Counter(map(len, adj)).items()))
    degree3_twins = collections.Counter(tuple(sorted(adj[v])) for v in range(n) if len(adj[v]) == 3)
    triples_same_neighborhood = sum(k*(k-1)*(k-2)//6 for k in degree3_twins.values())
    e33 = sum(len(adj[v]) == 3 and len(adj[w]) == 3 for v in range(n) for w in adj[v] if v < w)
    if valid:
        assert components == 1 and bridges == 0 and not cut
    return dict(prefix=stem, n=n, m=m, valid_cycle=valid, components=components, bridges=bridges, articulation_vertices=len(cut), degree3_triples_same_neighborhood=triples_same_neighborhood, e33=e33, degree_histogram=hist, graph_sha256=digest)

if __name__ == '__main__':
    rows = list(csv.DictReader(open(ROOT / 'data/sweep.csv')))
    checked = []
    for row in rows:
        result = check(row['prefix'])
        assert result['valid_cycle'] == bool(int(row['found']))
        assert result['n'] == int(row['n']) and result['m'] == int(row['m'])
        checked.append(result)
    (ROOT / 'data/verification.json').write_text(json.dumps(checked, indent=2))
    print('verified', len(checked), 'graphs;', sum(r['valid_cycle'] for r in checked), 'Hamilton cycles')
