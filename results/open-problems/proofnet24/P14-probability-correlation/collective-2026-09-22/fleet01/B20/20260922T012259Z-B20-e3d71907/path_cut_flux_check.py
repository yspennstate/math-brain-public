from itertools import combinations


def forest_components(n, edges):
    p=list(range(n))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a==b: return False
        p[a]=b; return True
    for u,v in edges:
        if not union(u,v): return None
    return [find(i) for i in range(n)]


def path_edges(n,H,a,b):
    adj=[[] for _ in range(n)]
    for j,(u,v) in enumerate(H):
        adj[u].append((v,j)); adj[v].append((u,j))
    par={a:(-1,-1)}; stack=[a]
    while stack:
        x=stack.pop()
        if x==b: break
        for y,j in adj[x]:
            if y not in par:
                par[y]=(x,j); stack.append(y)
    if b not in par: return None
    out=set(); x=b
    while x!=a:
        px,j=par[x]; out.add(j); x=px
    return out


def flux_pair(n,edges,ei,fi):
    e,f=edges[ei],edges[fi]
    K=[ed for j,ed in enumerate(edges) if j not in (ei,fi)]
    L10=L01=LQ=R10=R01=RQ=0
    n00=q=qzero=0
    for mask in range(1<<len(K)):
        H=[K[j] for j in range(len(K)) if mask>>j&1]
        comp=forest_components(n,H)
        if comp is None: continue
        pe=path_edges(n,H,*e); pf=path_edges(n,H,*f)
        X=pe is None; Y=pf is None
        if not X and not Y:
            n00+=1
            L10+=len(pe-pf); L01+=len(pf-pe); LQ+=len(pe&pf)
        elif X and not Y:
            pair=frozenset((comp[e[0]],comp[e[1]]))
            R10+=sum(1 for u,v in K if frozenset((comp[u],comp[v]))==pair)
        elif not X and Y:
            pair=frozenset((comp[f[0]],comp[f[1]]))
            R01+=sum(1 for u,v in K if frozenset((comp[u],comp[v]))==pair)
        else:
            pecomp=frozenset((comp[e[0]],comp[e[1]]))
            pfcomp=frozenset((comp[f[0]],comp[f[1]]))
            if len(pecomp)==2 and pecomp==pfcomp:
                q+=1
                cq=sum(1 for u,v in K if frozenset((comp[u],comp[v]))==pecomp)
                RQ+=cq
                qzero += (cq==0)
    return (L10,L01,LQ),(R10,R01,RQ),n00,q,qzero


def connected_minus(n,edges,deleted):
    verts=[v for v in range(n) if v not in deleted]
    if len(verts)<=1: return True
    adj=[[] for _ in range(n)]
    for u,v in edges:
        if u not in deleted and v not in deleted:
            adj[u].append(v); adj[v].append(u)
    seen={verts[0]}; stack=[verts[0]]
    while stack:
        x=stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y); stack.append(y)
    return len(seen)==len(verts)


def three_connected(n,edges):
    if n<4: return False
    return all(connected_minus(n,edges,set(S))
               for k in range(3) for S in combinations(range(n),k))


graphs=pairs=flux_fail=lower_fail=qzero3=0
for n in range(2,6):
    allE=list(combinations(range(n),2))
    for gm in range(1<<len(allE)):
        edges=[allE[j] for j in range(len(allE)) if (gm>>j)&1]
        if len(edges)<2: continue
        graphs+=1
        tc=three_connected(n,edges)
        for ei,fi in combinations(range(len(edges)),2):
            pairs+=1
            L,R,n00,q,qz=flux_pair(n,edges,ei,fi)
            flux_fail += (L!=R)
            lower_fail += (sum(L)<3*n00 or L[0]+L[2]<2*n00 or L[1]+L[2]<2*n00)
            if tc: qzero3 += qz

print('FOREST_PATH_CUT_FLUX_CHECK_PASS' if flux_fail==0 and lower_fail==0 else 'FAIL')
print('graphs_checked',graphs)
print('marked_pairs_checked',pairs)
print('flux_identity_failures',flux_fail)
print('simple_path_lower_bound_failures',lower_fail)
print('q_states_with_zero_direct_reconnect_in_3connected_n_le_5',qzero3)
