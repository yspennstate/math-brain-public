"""Exact rooted SAW counts on infinite graphs and their simple quotients.

Only the radius-N ball is built; no artificial periodic boundary is imposed.
One serial worker; inherited nice >=10; explicit graph/state size guards.
"""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import csv, itertools, json, math, resource, sys, time
from collections import deque, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def square(v, width=None):
    x, y = v
    ns = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
    return sorted(set((a % width if width else a, b) for a,b in ns) - {v})

def hexagonal(v, width=None):
    x, y = v
    ns = [(x+1,y), (x-1,y), (x,y+(1 if (x+y)%2 == 0 else -1))]
    return sorted(set((a % width if width else a, b) for a,b in ns) - {v})

def clique_strip(v, size):
    z, i = v
    return [(z-1,i), (z+1,i)] + [(z,j) for j in range(size) if j != i]

def tree(v, degree):
    # Reduced words in the free product of degree copies of C2.
    return [v[:-1] if v and v[-1] == i else v+(i,) for i in range(degree)]

def ball(neighbors, root, radius):
    vertices, ids, depth = [root], {root:0}, [0]
    adjacency = []
    for v in vertices:
        i = ids[v]
        if depth[i] == radius:
            adjacency.append([])
            continue
        ns = list(neighbors(v))
        assert v not in ns and len(ns) == len(set(ns))
        row = []
        for w in ns:
            if w not in ids:
                if len(vertices) >= 200000:
                    raise MemoryError('Conservative 200000-vertex graph budget exceeded')
                ids[w] = len(vertices)
                vertices.append(w); depth.append(depth[i]+1)
            row.append(ids[w])
        adjacency.append(row)
    return adjacency, vertices

def dfs_counts(adjacency, n):
    counts, used = [0]*(n+1), {0}
    def visit(v, k):
        counts[k] += 1
        if k == n: return
        for w in adjacency[v]:
            if w not in used:
                used.add(w); visit(w,k+1); used.remove(w)
    visit(0,0)
    return counts

def independent_counts(neighbors, root, n):
    # Counts states (endpoint, visited vertex set), merging multiplicities.
    states = {(root, frozenset([root])):1}
    counts = [1]
    for k in range(n):
        nxt = defaultdict(int)
        for (v, seen), multiplicity in states.items():
            for w in neighbors(v):
                if w not in seen:
                    nxt[w,seen|{w}] += multiplicity
        counts.append(sum(nxt.values())); states = nxt
        if len(states) > 200000:
            raise MemoryError('Conservative independent-check state budget exceeded')
    return counts

def group_audit():
    perms = list(itertools.permutations(range(3)))
    e, t = (0,1,2), (1,0,2)
    mul = lambda a,b: tuple(a[b[i]] for i in range(3))
    audits = []
    for name, elements, identity, generator, product in [
        ('S3', perms, e, t, mul),
        ('D8', [(r,f) for r in range(4) for f in range(2)], (0,0), (0,1),
         lambda a,b: ((a[0]+(-1 if a[1] else 1)*b[0])%4, a[1]^b[1]))]:
        subgroup = {identity, generator}
        inverse = lambda a: next(b for b in elements if product(a,b) == identity)
        conjugates = [{product(product(g,h),inverse(g)) for h in subgroup} for g in elements]
        core = set.intersection(*conjugates)
        canon = lambda g: min(product(a,g) for a in subgroup)
        cosets = sorted({canon(g) for g in elements})
        quotient = {c:set() for c in cosets}
        sparse = {c:set() for c in cosets}
        r = (1,2,0)  # only used for S3
        generating = [g for g in elements if g != identity]
        for g in elements:
            for s in generating:
                c,d = canon(g),canon(product(g,s))
                if c != d: quotient[c].add(d)
            if name == 'S3':
                for s in [t,r,inverse(r)]:
                    c,d = canon(g),canon(product(g,s))
                    if c != d: sparse[c].add(d)
        assert core == {identity} and any(c != subgroup for c in conjugates)
        assert all(product(generator,g) != g for g in elements)
        assert all(len(ns) == len(cosets)-1 for ns in quotient.values())
        audits.append({'group':name, 'order':len(elements), 'A_order':2,
                       'normal':False, 'free':True, 'core_order':len(core),
                       'quotient':f'K{len(cosets)}',
                       'sparse_S3_quotient': 'K3' if name == 'S3' and all(len(s)==2 for s in sparse.values()) else None})
    return audits

def sparse_s3(v):
    # Cayley(S3,{r,r^-1,t}) is the triangular prism C3 square K2.
    z,i,b = v
    return [(z-1,i,b),(z+1,i,b),(z,(i-1)%3,b),(z,(i+1)%3,b),(z,i,1-b)]

def main():
    assert os.getpriority(os.PRIO_PROCESS,0) >= 10
    # The host rejects lowering RLIMIT_AS and RLIMIT_DATA. Bounded balls,
    # bounded independent-check states, O(n) DFS stacks, and RSS checks apply.
    jobs = [
        ('square',lambda v:square(v),(0,0),14),
        ('square_cylinder_2',lambda v:square(v,2),(0,0),18),
        ('square_cylinder_3',lambda v:square(v,3),(0,0),14),
        ('square_cylinder_4',lambda v:square(v,4),(0,0),14),
        ('hexagonal',lambda v:hexagonal(v),(0,0),18),
        ('hex_cylinder_2',lambda v:hexagonal(v,2),(0,0),18),
        ('hex_cylinder_4',lambda v:hexagonal(v,4),(0,0),18),
        ('hex_cylinder_6',lambda v:hexagonal(v,6),(0,0),18),
        ('tree_3',lambda v:tree(v,3),(),12),
        ('tree_4',lambda v:tree(v,4),(),10),
        ('S3_complete_x_Z',lambda v:clique_strip(v,6),(0,0),9),
        ('S3_quotient_x_Z',lambda v:clique_strip(v,3),(0,0),14),
        ('D8_complete_x_Z',lambda v:clique_strip(v,8),(0,0),8),
        ('D8_quotient_x_Z',lambda v:clique_strip(v,4),(0,0),12),
        ('S3_sparse_x_Z',sparse_s3,(0,0,0),11),
        ('finite_S3_complete',lambda i:[j for j in range(6) if j != i],0,6),
        ('finite_S3_quotient',lambda i:[j for j in range(3) if j != i],0,6),
        ('finite_D8_complete',lambda i:[j for j in range(8) if j != i],0,8),
        ('finite_D8_quotient',lambda i:[j for j in range(4) if j != i],0,8),
    ]
    result = {'method':'exact DFS, independently checked by visited-set dynamic programming through n=6',
              'niceness':os.getpriority(os.PRIO_PROCESS,0),'threads':1,
              'vertex_budget':200000, 'independent_state_budget':200000,
              'graphs':{}, 'group_audit':group_audit()}
    for name, neighbors, root, n in jobs:
        start = time.monotonic()
        adjacency, vertices = ball(neighbors, root, n)
        counts = dfs_counts(adjacency,n)
        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 4*1024**3
        independent = independent_counts(neighbors,root,min(6,n))
        assert counts[:len(independent)] == independent, name
        if name.startswith('tree_'):
            d = int(name[-1]); assert counts == [1]+[d*(d-1)**(k-1) for k in range(1,n+1)]
        if name == 'square':
            assert counts[:11] == [1,4,12,36,100,284,780,2172,5916,16268,44100]
        if name == 'hex_cylinder_2': assert counts == [1]+[2]*n
        result['graphs'][name] = {'n_max':n,'counts':counts,'ball_vertices':len(vertices),
                                   'elapsed_seconds':time.monotonic()-start,
                                   'last_root':counts[-1]**(1/n) if counts[-1] else 0,
                                   'last_ratio':counts[-1]/counts[-2] if counts[-2] else None,
                                   'independent_check_through':min(6,n)}
        (ROOT/'data'/'enumeration.json').write_text(json.dumps(result,indent=2)+'\n')
        print(name,n,counts[-1],f'{result["graphs"][name]["elapsed_seconds"]:.3f}s',flush=True)
    pairs = [('square','square_cylinder_2'),('square','square_cylinder_3'),('square','square_cylinder_4'),
             ('hexagonal','hex_cylinder_2'),('hexagonal','hex_cylinder_4'),('hexagonal','hex_cylinder_6'),
             ('tree_3','hexagonal'),('tree_3','square_cylinder_2'),('tree_4','square'),
             ('S3_complete_x_Z','S3_quotient_x_Z'),('D8_complete_x_Z','D8_quotient_x_Z'),
             ('S3_sparse_x_Z','S3_quotient_x_Z')]
    result['comparisons'] = []
    for g,h in pairs:
        a,b = result['graphs'][g]['counts'],result['graphs'][h]['counts']
        n = min(len(a),len(b))-1
        assert all(b[k] <= a[k] for k in range(n+1)), (g,h)
        result['comparisons'].append({'G':g,'H':h,'common_n':n,'G_count':a[n],'H_count':b[n],
                                      'first_strict_n':next((k for k in range(n+1) if b[k]<a[k]),None)})
    result['max_rss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    (ROOT/'data'/'enumeration.json').write_text(json.dumps(result,indent=2)+'\n')
    with (ROOT/'data'/'counts.csv').open('w') as f:
        writer = csv.writer(f); writer.writerow(['graph','n','c_n','c_n_root','successive_ratio'])
        for name, info in result['graphs'].items():
            for n,c in enumerate(info['counts']):
                writer.writerow([name,n,c,c**(1/n) if n and c else '',c/info['counts'][n-1] if n and info['counts'][n-1] else ''])
    print('All independent counts, group claims, and quotient inequalities verified.',flush=True)

if __name__ == '__main__': main()
