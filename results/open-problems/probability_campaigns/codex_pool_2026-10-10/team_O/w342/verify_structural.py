"""Exact independent checks for C0035, P0001 and P0133, with per-stage receipts."""
from collections import Counter, deque
from fractions import Fraction as Q
from itertools import combinations
import json
from math import prod
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent


def save(problem, receipt):
    receipt['command'] = 'python -X utf8 verify_structural.py'
    receipt['label'] = 'exact finite checks; separate written proof awaiting audit'
    (ROOT/(problem.lower()+'_measurements.json')).write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
    print(problem, json.dumps(receipt), flush=True)


def determinant(matrix):
    a = [list(row) for row in matrix]
    answer = Q(1)
    for col in range(len(a)):
        pivot = next((i for i in range(col,len(a)) if a[i][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            answer = -answer
        entry = a[col][col]
        answer *= entry
        for row in range(col+1,len(a)):
            factor = a[row][col]/entry
            for k in range(col+1,len(a)):
                a[row][k] -= factor*a[col][k]
    return answer


start = time.perf_counter()
a,b,d = Q(1,2),Q(2,25),Q(1,25)
triples = [determinant([[a,b,s*d],[b,a,b],[s*d,b,a]]) for s in [1,-1]]
assert triples[0]-triples[1] == Q(16,15625)
checks = 0
positions = list(range(-2,5))
for k in [2,3]:
    def kernel(i,j):
        if i==j:
            return a
        return Q(1,10) if abs(i-j)==k else Q(0)
    for mask in range(1<<len(positions)):
        chosen = [x for n,x in enumerate(positions) if mask & (1<<n)]
        full = determinant([[kernel(i,j) for j in chosen] for i in chosen])
        factors = []
        for residue in range(k):
            group = [i for i in chosen if i%k==residue]
            factors.append(determinant([[kernel(i,j) for j in group] for i in group]))
        assert full == prod(factors)
        checks += 1
save('C0035', {'triple_probabilities':[str(x) for x in triples], 'exact_triple_difference':str(triples[0]-triples[1]),'sublattice_determinant_checks':checks,'violations':0,'seconds':round(time.perf_counter()-start,3)})


class DSU:
    def __init__(self,n):
        self.p = list(range(n))
    def find(self,a):
        while self.p[a]!=a:
            a = self.p[a]
        return a
    def union(self,a,b):
        a,b = self.find(a),self.find(b)
        if a==b:
            return False
        self.p[a] = b
        return True


start = time.perf_counter()
pair_checks = forest_count = subset_checks = 0
cases = [(2,2,2),(2,3,3),(1,2,3,3),(2,2,2,2),(1,1,2,2),(3,3),(1,1,1)]
for lengths in cases:
    edges,path_of,path_indices = [],[],[]
    next_vertex = 2
    for j,length in enumerate(lengths):
        vertices = [0] + list(range(next_vertex,next_vertex+length-1)) + [1]
        next_vertex += length-1
        ids = []
        for u,v in zip(vertices,vertices[1:]):
            ids.append(len(edges))
            edges.append((u,v))
            path_of.append(j)
        path_indices.append(ids)
    size = len(edges)
    for weights in [[1]*size,[2]*size,[1+i%3 for i in range(size)]]:
        Z = 0
        Ze = [0]*size
        Zef = [[0]*size for _ in range(size)]
        for mask in range(1<<size):
            subset_checks += 1
            selected = [i for i in range(size) if mask & (1<<i)]
            union = DSU(next_vertex)
            if not all(union.union(*edges[i]) for i in selected):
                continue
            forest_count += 1
            weight = prod(weights[i] for i in selected)
            Z += weight
            for e in selected:
                Ze[e] += weight
            for e,f in combinations(selected,2):
                Zef[e][f] += weight
        p = [Q(w,1+w) for w in weights]
        P = [prod(p[e] for e in group) for group in path_indices]
        t = [q/(1-q) for q in P]
        S = 1+sum(t)
        for e,f in combinations(range(size),2):
            pair_checks += 1
            actual = Q(Zef[e][f],Z)-Q(Ze[e]*Ze[f],Z*Z)
            assert actual <= 0
            i,j = path_of[e],path_of[f]
            if i==j:
                others = sum(t[k] for k in range(len(t)) if k!=i)
                alpha = others/(1+others)
                expected = -alpha*P[i]*(1-p[e])*(1-p[f])/(1-alpha*P[i])**2
            else:
                expected = -(1-p[e])*(1-p[f])*t[i]*t[j]/((1-P[i])*(1-P[j])*S*S)
            assert actual == expected
save('P0001', {'weighted_graph_cases':len(cases)*3,'subset_checks':subset_checks,'accepted_forests_with_case_multiplicity':forest_count,'exact_pair_formula_checks':pair_checks,'positive_covariances':0,'formula_mismatches':0,'seconds':round(time.perf_counter()-start,3)})


start = time.perf_counter()
L = 3
vertex = lambda x,y: (x%L)*L+(y%L)
primal, dual = [],[]
for x in range(L):
    for y in range(L):
        primal.append((vertex(x,y),vertex(x+1,y)))
        dual.append((vertex(x,y-1),vertex(x,y),(0,1)))
        primal.append((vertex(x,y),vertex(x,y+1)))
        dual.append((vertex(x-1,y),vertex(x,y),(1,0)))
trees = theta = bouquet = 0
winding_pairs = Counter()
for selected in combinations(range(len(primal)),L*L-1):
    uf = DSU(L*L)
    if not all(uf.union(*primal[i]) for i in selected):
        continue
    trees += 1
    complement = [i for i in range(len(dual)) if i not in selected]
    uf = DSU(L*L)
    adjacency = [[] for _ in range(L*L)]
    all_adjacency = [[] for _ in range(L*L)]
    extra = []
    for i in complement:
        u,v,(dx,dy) = dual[i]
        all_adjacency[u].append((v,(dx,dy),i))
        all_adjacency[v].append((u,(-dx,-dy),i))
        if uf.union(u,v):
            adjacency[u].append((v,(dx,dy)))
            adjacency[v].append((u,(-dx,-dy)))
        else:
            extra.append(i)
    assert len(extra)==2
    lifts = {0:(0,0)}
    todo = deque([0])
    while todo:
        u = todo.popleft()
        for v,step in adjacency[u]:
            if v not in lifts:
                lifts[v] = (lifts[u][0]+step[0],lifts[u][1]+step[1])
                todo.append(v)
    assert len(lifts)==L*L
    windings = []
    for i in extra:
        u,v,(dx,dy) = dual[i]
        cycle = (lifts[u][0]+dx-lifts[v][0],lifts[u][1]+dy-lifts[v][1])
        assert all(c%L==0 for c in cycle)
        windings.append(tuple(c//L for c in cycle))
    u,v = windings
    assert abs(u[0]*v[1]-u[1]*v[0])==1
    winding_pairs[str(windings)] += 1
    active = set(complement)
    degrees = [len(a) for a in all_adjacency]
    todo = deque(i for i,degree in enumerate(degrees) if degree<=1)
    while todo:
        u = todo.popleft()
        for v,step,i in all_adjacency[u]:
            if i in active:
                active.remove(i)
                degrees[u] -= 1
                degrees[v] -= 1
                if degrees[v]==1:
                    todo.append(v)
    branches = [i for i,dg in enumerate(degrees) if dg>2]
    if len(branches)==1:
        assert degrees[branches[0]]==4
        bouquet += 1
    else:
        assert len(branches)==2 and all(degrees[i]==3 for i in branches)
        s,t = branches
        displacements = []
        for first,step,e in all_adjacency[s]:
            if e not in active:
                continue
            last,current,total,last_edge = s,first,step,e
            while current != t:
                options = [(v,delta,i) for v,delta,i in all_adjacency[current] if i in active and i!=last_edge]
                assert len(options)==1
                nxt,delta,nxt_edge = options[0]
                total = (total[0]+delta[0],total[1]+delta[1])
                last,current,last_edge = current,nxt,nxt_edge
            displacements.append(total)
        assert len(displacements)==3
        x,y,z = displacements
        cu = tuple((x[k]-y[k])//L for k in range(2))
        cv = tuple((x[k]-z[k])//L for k in range(2))
        assert all((x[k]-y[k])%L==0 and (x[k]-z[k])%L==0 for k in range(2))
        assert abs(cu[0]*cv[1]-cu[1]*cv[0])==1
        theta += 1
assert trees == 11664  # independent matrix-tree eigenvalue product: 3^4*6^4/9
save('P0133', {'torus_side':L,'spanning_trees':trees,'unimodular_basis_checks':trees,'theta_core_checks':theta,'bouquet_cores':bouquet,'violations':0,'seconds':round(time.perf_counter()-start,3)})
