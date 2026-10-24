"""Re-run the bounded Haugland 5-colour terminal relation search.
Requires the sibling exact verifier and archived witness JSON.
The search is heuristic SAT-finding only: SAT outputs are exact witnesses; failure is never UNSAT.
"""
from pathlib import Path
import runpy,sys,random,time,json
HERE=Path(__file__).resolve().parent
ver=HERE/'2026-09-16T13-46-26Z__haugland_exact_replay_verifier.py'
wit=HERE/'2026-09-16T13-46-26Z__haugland_relation_witnesses.json'
sys.argv=[str(ver),str(wit)]
ns=runpy.run_path(str(ver))
adj1,adj2=ns['adj1'],ns['adj2']
A1,B1,G2m,G2p=ns['A1'],ns['B1'],ns['G2m'],ns['G2p']

def quotient(adj,eq=None,neq=None):
    n=len(adj); parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b: parent[b]=a
    if eq: union(*eq)
    for u in range(n):
        for v in adj[u]:
            if find(u)==find(v): return None,None
    reps=sorted({find(i) for i in range(n)}); mp={r:i for i,r in enumerate(reps)}
    groups=[[] for _ in reps]
    for i in range(n): groups[mp[find(i)]].append(i)
    q=[set() for _ in reps]
    for u in range(n):
        a=mp[find(u)]
        for v in adj[u]:
            b=mp[find(v)]
            if a!=b:q[a].add(b)
    if neq:
        a,b=mp[find(neq[0])],mp[find(neq[1])]
        if a==b:return None,None
        q[a].add(b);q[b].add(a)
    return q,groups

def tabucol(adj,k,eq=None,neq=None,seconds=5,seed=0):
    q,groups=quotient(adj,eq,neq)
    if q is None:return False,None,0
    rng=random.Random(seed); n=len(q); deadline=time.time()+seconds; total=0
    while time.time()<deadline:
        order=sorted(range(n),key=lambda v:len(q[v]),reverse=True)
        col=[-1]*n
        for v in order:
            cnt=[sum(col[x]==c for x in q[v]) for c in range(k)]
            m=min(cnt); col[v]=rng.choice([c for c in range(k) if cnt[c]==m])
        nc=[[0]*k for _ in range(n)]
        for v in range(n):
            for x in q[v]: nc[v][col[x]]+=1
        conflicts=sum(nc[v][col[v]] for v in range(n))//2
        tabu=[[0]*k for _ in range(n)]; it=0; best=conflicts
        while conflicts and time.time()<deadline:
            it+=1;total+=1; bestdelta=10**9;moves=[]
            for v in range(n):
                old=col[v]
                if nc[v][old]==0:continue
                oc=nc[v][old]
                for c in range(k):
                    if c==old:continue
                    d=nc[v][c]-oc
                    if tabu[v][c]<=it or conflicts+d<best:
                        if d<bestdelta:bestdelta=d;moves=[(v,c)]
                        elif d==bestdelta:moves.append((v,c))
            if not moves:break
            v,new=rng.choice(moves);old=col[v]
            for x in q[v]:nc[x][old]-=1;nc[x][new]+=1
            col[v]=new;conflicts+=bestdelta
            tabu[v][old]=it+5+rng.randrange(10)+int(.6*conflicts)
            best=min(best,conflicts)
        if conflicts==0:
            orig=[-1]*len(adj)
            for qi,g in enumerate(groups):
                for v in g:orig[v]=col[qi]
            assert all(orig[u]!=orig[v] for u in range(len(adj)) for v in adj[u] if u<v)
            if eq:assert orig[eq[0]]==orig[eq[1]]
            if neq:assert orig[neq[0]]!=orig[neq[1]]
            return True,orig,total
    return None,None,total

out={}
for name,adj,u,v in [('G1_A_B',adj1,A1,B1),('G2_m1_p1',adj2,G2m,G2p)]:
    rec={'n':len(adj),'m':sum(map(len,adj))//2,'u':u,'v':v}
    for rel in ('eq','neq'):
        seed=100000*len(name)+(0 if rel=='eq' else 71)
        r,c,it=tabucol(adj,5,eq=(u,v) if rel=='eq' else None,neq=(u,v) if rel=='neq' else None,seconds=8,seed=seed)
        if r is not True:raise RuntimeError(f'no SAT witness found for {name} {rel}; this is not an UNSAT claim')
        rec[rel]={'sat':True,'iterations':it,'coloring':c}
        print('SAT_WITNESS',name,rel,'iterations',it)
    out[name]=rec
op=HERE/'regenerated_haugland_relation_witnesses.json'
op.write_text(json.dumps(out,separators=(',',':')))
print('WROTE',op.name)
