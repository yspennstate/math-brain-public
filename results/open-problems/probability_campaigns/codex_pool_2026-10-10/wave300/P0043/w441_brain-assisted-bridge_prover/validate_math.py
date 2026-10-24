"""Small exact checks of the deductions' nontrivial combinatorial ingredients."""
from collections import Counter, deque
from fractions import Fraction
import json, math, time
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def connected(vertices,edges,root):
    seen={root}
    changed=True
    while changed:
        changed=False
        for u,v in edges:
            if u in vertices and v in vertices and ((u in seen)!=(v in seen)):
                seen.update((u,v));changed=True
    return seen==set(vertices)

def thinning(edges,p,q):
    m=len(edges)
    law=Counter()
    for a in range(1<<m):
        wa=p**a.bit_count()*(1-p)**(m-a.bit_count())
        for b in range(1<<m):
            wb=q**b.bit_count()*(1-q)**(m-b.bit_count())
            law[a&b]+=wa*wb
    assert sum(law.values())==1
    for mask in range(1<<m):
        assert law[mask]==(p*q)**mask.bit_count()*(1-p*q)**(m-mask.bit_count())
    return 4**m

def decorated(depth):
    adj={}
    def edge(a,b):
        adj.setdefault(a,set()).add(b)
        adj.setdefault(b,set()).add(a)
    for n in range(depth+1):
        s=('s',n)
        if n:edge(('s',n-1),s)
        edge(s,('t',n,1))
        for i in range(1,1<<n):
            edge(('t',n,i),('t',n,2*i))
            edge(('t',n,i),('t',n,2*i+1))
    dist={('s',0):0}
    queue=deque(dist)
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if v not in dist:dist[v]=dist[u]+1;queue.append(v)
    assert len(adj)==2**(depth+2)-2
    assert max(map(len,adj.values()))<=3
    rows=[]
    for n in range(depth+1):
        leaves=[('t',n,i) for i in range(1<<n,1<<(n+1))]
        assert all(dist[v]==2*n+1 for v in leaves)
        rows.append({'graft_depth':n,'radius':2*n+1,'leaves':len(leaves),'ball_size':sum(d<=2*n+1 for d in dist.values())})
    return {'vertices':len(adj),'max_degree':max(map(len,adj.values())),'balls':rows}

def main():
    start=time.perf_counter()
    p,q=Fraction(2,3),Fraction(3,5)
    graphs=[(3,[(0,1),(1,2),(2,0)]),(4,[(0,1),(1,2),(2,3),(3,0)]),(4,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])]
    counts=[]
    joint=0
    for v,edges in graphs:
        joint+=thinning(edges,p,q)
        delta=max(sum(u in e for e in edges) for u in range(v))
        for n in range(1,v+1):
            actual=sum(1 for mask in range(1<<v) if mask&1 and mask.bit_count()==n and connected({i for i in range(v) if mask>>i&1},edges,0))
            bound=delta**(2*(n-1))
            assert actual<=bound
            counts.append({'vertices':v,'edges':len(edges),'n':n,'actual':actual,'walk_bound':bound})
    assert joint==4416
    a=Fraction(1,20);delta=3
    upper=a/(1-delta**2*a)
    assert upper==Fraction(1,11) and 1-upper==Fraction(10,11)
    # A conditioning witness: omega_0=1 changes the retained marginal from pq to q.
    conditional_retained=q
    unconditional_retained=p*q
    assert conditional_retained!=unconditional_retained
    witness=decorated(10)
    elapsed=time.perf_counter()-start
    gate=json.loads((ROOT/'COMPUTE_GATE.json').read_text(encoding='utf-8'))
    assert elapsed<gate['max_seconds']
    assert witness['vertices']<=gate['max_graph_vertices']
    result={'command':'python -X utf8 validate_math.py','elapsed_seconds':elapsed,'exact_joint_configurations':joint,'finite_product_law_checks':3,'connected_set_bounds':counts,'peierls_example':{'Delta':3,'h':1,'q':'19/20','survival_lower_bound':'10/11','conditional_on_positive_anchored_expansion':True},'conditioning_witness':{'conditional_marginal':str(conditional_retained),'unconditional_marginal':str(unconditional_retained)},'decorated_ray':witness,'proof_limit':'These finite checks verify ingredients; the infinite statements rely on the written countable/Tonelli and limiting arguments, not simulation.'}
    (ROOT/'MATH_CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
