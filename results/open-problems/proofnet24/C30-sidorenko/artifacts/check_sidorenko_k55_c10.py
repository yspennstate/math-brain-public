from fractions import Fraction
from collections import defaultdict
import itertools, math
import numpy as np
import networkx as nx

# Frozen H = K_{5,5} \ C_10.
# Bipartition L={0,...,4}, R={0,...,4}. Remove (L_i,R_i) and (L_{i+1},R_i).
# Hence R_i is adjacent to L_{i+2}, L_{i+3}, L_{i+4} (indices mod 5).
V_H=10
E_H=15

def hom_H(G):
    G=nx.convert_node_labels_to_integers(G, ordering='sorted')
    n=G.number_of_nodes()
    A=nx.to_numpy_array(G,nodelist=range(n),dtype=np.int64)
    C=np.einsum('iv,jv,kv->ijk',A,A,A,optimize=True)
    h=int(np.einsum('cde,dea,eab,abc,bcd->',C,C,C,C,C,optimize=True))
    assert 0 <= h <= n**V_H
    return h

def brute_hom_H(G):
    G=nx.convert_node_labels_to_integers(G, ordering='sorted')
    n=G.number_of_nodes()
    adj=[[False]*n for _ in range(n)]
    for u,v in G.edges():
        adj[u][v]=adj[v][u]=True
    Hedges=[]
    for i in range(5):
        for j in range(5):
            if j not in (i,(i-1)%5):
                Hedges.append((i,5+j))
    assert len(Hedges)==15
    total=0
    for f in itertools.product(range(n), repeat=10):
        if all(adj[f[u]][f[v]] for u,v in Hedges):
            total+=1
    return total

def burnside_unlabeled_count(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    pindex={e:k for k,e in enumerate(pairs)}
    total=0
    for perm in itertools.permutations(range(n)):
        seen=set(); orbits=0
        for idx in range(len(pairs)):
            if idx in seen: continue
            orbits += 1
            cur=idx
            while cur not in seen:
                seen.add(cur)
                i,j=pairs[cur]
                a,b=perm[i],perm[j]
                if a>b: a,b=b,a
                cur=pindex[(a,b)]
        total += 1 << orbits
    assert total % math.factorial(n) == 0
    return total // math.factorial(n)

def perm_matrix(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    idx={e:k for k,e in enumerate(pairs)}
    perms=list(itertools.permutations(range(n)))
    M=np.zeros((len(perms),len(pairs)),dtype=np.uint64)
    for r,p in enumerate(perms):
        for k,(i,j) in enumerate(pairs):
            a,b=p[i],p[j]
            if a>b: a,b=b,a
            M[r,k]=np.uint64(1)<<np.uint64(idx[(a,b)])
    return pairs,M

def canon_code(G,n,pairs,M):
    G=nx.convert_node_labels_to_integers(G, ordering='sorted')
    eset={tuple(sorted(e)) for e in G.edges()}
    inds=[k for k,e in enumerate(pairs) if e in eset]
    if not inds: return 0
    codes=np.bitwise_or.reduce(M[:,inds],axis=1)
    return int(codes.min())

def exact_defect(G):
    n=G.number_of_nodes(); m=G.number_of_edges(); h=hom_H(G)
    lhs=h*n**20
    rhs=(2*m)**15
    return h,lhs-rhs

atlas=nx.graph_atlas_g()
by_n=defaultdict(list)
for G in atlas:
    n=G.number_of_nodes()
    if 1 <= n <= 7:
        by_n[n].append(nx.convert_node_labels_to_integers(G,ordering='sorted'))

print('H=K_5,5\\C_10; v(H)=10; e(H)=15; degree sequence=(3^10)')
print('Exact finite host certificate via graph atlas + independent Burnside completeness count.')

for n in range(1,4):
    for G in by_n[n]:
        a=hom_H(G); b=brute_hom_H(G)
        assert a==b,(n,G.edges(),a,b)
print('hom_formula_bruteforce_crosscheck_n<=3=PASS')

global_min=None
for n in range(1,8):
    burn=burnside_unlabeled_count(n)
    graphs=by_n[n]
    assert len(graphs)==burn,(n,len(graphs),burn)
    pairs,M=perm_matrix(n)
    codes=[canon_code(G,n,pairs,M) for G in graphs]
    assert len(codes)==len(set(codes)),('duplicate isomorphism classes',n)
    violations=[]
    min_record=None
    for idx,G in enumerate(graphs):
        h,D=exact_defect(G)
        m=G.number_of_edges()
        if D<0: violations.append((idx,m,h,D))
        if m>0:
            ratio=Fraction(h*n**20,(2*m)**15)
            if min_record is None or ratio < min_record[0]:
                min_record=(ratio,idx,m,h,D,canon_code(G,n,pairs,M),sorted(G.edges()))
            if global_min is None or ratio < global_min[0]:
                global_min=(ratio,n,idx,m,h,D,sorted(G.edges()))
    assert not violations,(n,violations[:3])
    if min_record is None:
        print(f'n={n}: unlabeled={len(graphs)} burnside={burn} unique=PASS violations=0 nonempty_hosts=0')
    else:
        r,idx,m,h,D,code,edges=min_record
        print(f'n={n}: unlabeled={len(graphs)} burnside={burn} unique=PASS violations=0; min_nonempty_ratio={r} ~= {float(r):.15f}; atlas_index_within_n={idx}; m={m}; hom={h}; defect={D}; canon_code={code}')

r,n,idx,m,h,D,edges=global_min
print('GLOBAL_MIN_NONEMPTY_HOST')
print(f'n={n} atlas_index_within_n={idx} m={m} hom={h}')
print(f'ratio=t(H,G)/t(K2,G)^15={r} ~= {float(r):.15f}')
print(f'defect=hom*n^20-(2m)^15={D}')
print(f'edges={edges}')
print('largest_completely_checked_host_order=7')
print('ALL_EXACT_CHECKS_PASS')
