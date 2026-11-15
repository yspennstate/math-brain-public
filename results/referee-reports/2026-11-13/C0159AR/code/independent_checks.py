"""Independent GP_b audit. Standard library; no claim code is imported.

Exact finite sums use integer configuration counts grouped by number of open edges.
The second solver eliminates non-terminal vertices while keeping a distribution
on connectivity partitions. Monte Carlo uses explicit edges and union-find.
"""
import collections
from fractions import Fraction as Q
import hashlib
import json
import math
import os
from pathlib import Path
import random
import resource
import time

ROOT = Path(__file__).resolve().parents[1]

def tree(b, depth, extra_parent=False):
    parents = {(): ('P',)} if extra_parent else {}
    vertices = {()}
    layer = [()]
    for _ in range(depth):
        following = []
        for node in layer:
            for i in range(b):
                child = node+(i,)
                vertices.add(child)
                parents[child] = node
                following.append(child)
        layer = following
    if extra_parent:
        vertices.add(('P',))
    return vertices, parents

def edges_from_parents(vertices, parents):
    edges = set()
    for v in vertices:
        u = parents.get(v)
        if u in vertices:
            edges.add(frozenset((v,u)))
        w = parents.get(u)
        if w in vertices:
            edges.add(frozenset((v,w)))
    return [tuple(e) for e in edges]

def connected(vertices, edges, s, t, mask):
    adjacent = {v: [] for v in vertices}
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            adjacent[u].append(v)
            adjacent[v].append(u)
    found, queue = {s}, [s]
    for v in queue:
        for w in adjacent[v]:
            if w not in found:
                if w == t:
                    return True
                found.add(w)
                queue.append(w)
    return s == t

def exact_uniform(vertices, edges, s, t, p):
    counts = [0]*(len(edges)+1)
    for mask in range(1<<len(edges)):
        if connected(vertices, edges, s, t, mask):
            counts[mask.bit_count()] += 1
    numerator, denominator = p.numerator, p.denominator
    value = Q(sum(c*numerator**k*(denominator-numerator)**(len(edges)-k)
                  for k,c in enumerate(counts)), denominator**len(edges))
    return value, counts

def finite_r(b, depth, p):
    result = p
    for _ in range(depth):
        result = 1-(1-p)*(1-p*result)**b
    return result

def core_network(b, parents, core, p, remaining_depth=None, r=None):
    # Core is ancestor-closed relative to its top. All original induced edges
    # remain independent; one auxiliary edge is kept for each omitted child.
    edges = [(u,v,p) for u,v in edges_from_parents(core, parents)]
    for t in core:
        s = parents.get(t)
        if s not in core:
            continue
        for j in range(b):
            z = t+(j,)
            if z in core:
                continue
            if remaining_depth is not None:
                dz = remaining_depth-len(z)
                if dz < 0:
                    continue
                rho = finite_r(b,dz,p)
            else:
                rho = r
            edges.append((s,t,p*rho))
    return edges

def canonical(blocks):
    return tuple(sorted((tuple(sorted(c)) for c in blocks if c)))

def merge_partition(partition, u, v):
    left = next(i for i,c in enumerate(partition) if u in c)
    right = next(i for i,c in enumerate(partition) if v in c)
    if left == right:
        return partition
    merged = tuple(sorted(partition[left]+partition[right]))
    return tuple(sorted([c for i,c in enumerate(partition) if i not in (left,right)]+[merged]))

def partition_reliability(vertices, edges, s, t):
    # Independent finite-network solver. Edge events merge connectivity blocks;
    # eliminate a vertex once its last incident edge was processed, retaining s,t.
    ordering = sorted(vertices, key=lambda v:(len(v),repr(v)), reverse=True)
    ids = {v:i for i,v in enumerate(ordering)}
    mapped = [(ids[u],ids[v],p) for u,v,p in edges]
    # Process all edges at deeper endpoint first, giving bounded active frontier
    # for a path-like core with a fixed number of marked vertices.
    mapped.sort(key=lambda e:min(e[0],e[1]))
    last = {i:-1 for i in ids.values()}
    for k,(u,v,_) in enumerate(mapped):
        last[u] = last[v] = k
    state = {(): 1}
    active = set()
    terminal_ids = {ids[s],ids[t]}
    for k,(u,v,p) in enumerate(mapped):
        missing = {u,v}-active
        if missing:
            expanded = collections.defaultdict(lambda:0)
            for part,prob in state.items():
                expanded[canonical(list(part)+[(w,) for w in missing])] += prob
            state = expanded
            active |= missing
        updated = collections.defaultdict(lambda:0)
        for part,prob in state.items():
            updated[part] += prob*(1-p)
            updated[merge_partition(part,u,v)] += prob*p
        forget = {w for w in active-terminal_ids if last[w] == k}
        state = collections.defaultdict(lambda:0)
        for part,prob in updated.items():
            reduced = canonical([tuple(w for w in c if w not in forget) for c in part])
            state[reduced] += prob
        active -= forget
    return sum(prob for part,prob in state.items()
               if any(ids[s] in c and ids[t] in c for c in part)) if s != t else 1

def infinite_r(b,p):
    lo,hi = 0.,1.
    for _ in range(60):
        mid = (lo+hi)/2
        if 1-(1-p)*(1-p*mid)**b-mid > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

def exact_checks():
    output = []
    for b,depth in [(2,0),(2,1),(2,2),(3,1),(4,1)]:
        vertices,parents = tree(b,depth,True)
        edges = edges_from_parents(vertices,parents)
        for p in [Q(1,4),Q(1,2),Q(3,4)]:
            exact,counts = exact_uniform(vertices,edges,(),('P',),p)
            expected = finite_r(b,depth,p)
            assert exact == expected
            output.append(dict(kind='cone',b=b,depth=depth,p=str(p),edges=len(edges),
                               configurations=1<<len(edges),exact=str(exact),counts=counts))
    vertices,parents = tree(2,2)
    edges = edges_from_parents(vertices,parents)
    # Two endpoints, one below the other; two cousins; two children.
    for s,t in [((),(0,0)),((0,0),(1,0)),((0,),(1,))]:
        core = {()}
        for v in (s,t):
            core.update(v[:i] for i in range(len(v)+1))
        for p in [Q(1,4),Q(1,2),Q(3,4)]:
            actual,_ = exact_uniform(vertices,edges,s,t,p)
            reduced = partition_reliability(core,core_network(2,parents,core,p,remaining_depth=2),s,t)
            assert actual == reduced, (s,t,p,actual,reduced)
            output.append(dict(kind='core',s=s,t=t,p=str(p),edges=len(edges),
                               configurations=1<<len(edges),core_vertices=len(core),exact=str(actual)))
    return output

def structural_checks():
    out = []
    for b in [2,3,4]:
        vertices,parents = tree(b,7)
        edges = edges_from_parents(vertices,parents)
        adj = {v:set() for v in vertices}
        for u,v in edges:
            adj[u].add(v); adj[v].add(u)
        x = (0,0,0)
        assert len(adj[x]) == b*b+b+2
        assert len(adj[x]&adj[parents[x]]) == b+1
        assert len(adj[x]&adj[parents[parents[x]]]) == 1
        # Explicitly scan all edges of a buffered tree, rather than generating
        # the boundary with the formula under audit.
        boundary_sets = []
        a0 = (0,0,0,0,0,0)
        for k in range(5):
            x = a0[:len(a0)-k]
            cone = {v for v in vertices if v[:len(x)] == x}
            observed = {frozenset(e) for e in edges if (e[0] in cone) != (e[1] in cone)}
            xp = parents[x]
            expected = {frozenset((x,xp)),frozenset((x,parents[xp]))}
            expected.update(frozenset((x+(j,),xp)) for j in range(b))
            assert observed == expected
            boundary_sets.append(observed)
        assert not boundary_sets[0]&boundary_sets[3]
        # Check all attachments of a buffered off-core cone (including its
        # deepest available generations) by inspecting both ends of every edge.
        z = (0,0,0)
        cone = {v for v in vertices if v[:len(z)] == z}
        attachments = {v for u,v in edges if u in cone and v not in cone}
        attachments |= {u for u,v in edges if v in cone and u not in cone}
        assert attachments == {parents[z],parents[parents[z]]}
        out.append(dict(b=b,degree=b*b+b+2,tree_common=b+1,long_common=1,
                        boundary_edges=b+2,attachment_vertices=2,boundaries_checked=5))
    return out

def sample_explicit(vertices, edges, pairs, p, samples, seed):
    labels = {v:i for i,v in enumerate(sorted(vertices, key=repr))}
    indexed = sorted((min(labels[u],labels[v]),max(labels[u],labels[v])) for u,v in edges)
    marked = [(labels[s],labels[t]) for s,t in pairs]
    rng = random.Random(seed)
    successes = [0]*len(pairs)
    for _ in range(samples):
        parent = list(range(len(vertices)))
        size = [1]*len(vertices)
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for u,v in indexed:
            if rng.random() < p:
                a,bb = find(u),find(v)
                if a != bb:
                    if size[a] < size[bb]: a,bb = bb,a
                    parent[bb] = a
                    size[a] += size[bb]
        for j,(s,t) in enumerate(marked):
            successes[j] += find(s) == find(t)
    return successes

def monte_carlo():
    # A free ancestor cap is explicit, not wired. Pairs near its root check the
    # exact in-cone polynomial. Full graph prediction is separately approximated
    # by a long ancestor core and certified with the report's cutset bound.
    b,depth,samples = 2,10,5000
    vertices,parents = tree(b,depth)
    edges = edges_from_parents(vertices,parents)
    pairs = [((),(0,0)),((0,),(1,)),((0,0),(1,0))]
    rows = []
    for j,p in enumerate([.28,.55,.76]):
        successes = sample_explicit(vertices,edges,pairs,p,samples,159000+j)
        for (s,t),wins in zip(pairs,successes):
            core = {()}
            for v in (s,t): core.update(v[:i] for i in range(len(v)+1))
            infinite = partition_reliability(core,core_network(b,parents,core,p,r=infinite_r(b,p)),s,t)
            finite = partition_reliability(core,core_network(b,parents,core,p,remaining_depth=depth),s,t)
            observed = wins/samples
            se = math.sqrt(finite*(1-finite)/samples)
            assert abs(observed-finite) < 5*se+.0002
            rows.append(dict(b=b,depth=depth,p=p,s=s,t=t,samples=samples,seed=159000+j,
                             infinite_cone_formula=infinite,finite_depth_formula=finite,
                             observed=observed,standard_error=se,z=(observed-finite)/se,
                             bottom_bias=infinite-finite))
    return rows

def main():
    started = time.monotonic()
    assert os.getpriority(os.PRIO_PROCESS,0) >= 10
    exact = exact_checks()
    structure = structural_checks()
    (ROOT/'data'/'exact_checks.json').write_text(json.dumps({'exact':exact,'structure':structure},indent=2)+'\n')
    print('Exact and structural checks passed:',len(exact),len(structure),flush=True)
    mc = monte_carlo()
    stats = dict(elapsed_seconds=time.monotonic()-started,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                 nice=os.getpriority(os.PRIO_PROCESS,0),threads=1,
                 code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (ROOT/'data'/'monte_carlo.json').write_text(json.dumps({'rows':mc,'resources':stats},indent=2)+'\n')
    print(json.dumps({'rows':mc,'resources':stats},indent=2),flush=True)

if __name__ == '__main__': main()
