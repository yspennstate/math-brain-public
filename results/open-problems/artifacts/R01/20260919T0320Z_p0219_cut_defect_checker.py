from collections import deque

def grid(n):
    V=[(i,j) for i in range(n) for j in range(n)]
    E=[]
    for i in range(n):
        for j in range(n):
            if i+1<n: E.append(((i,j),(i+1,j)))
            if j+1<n: E.append(((i,j),(i,j+1)))
    S={(0,j) for j in range(n-1)} | {(i,0) for i in range(1,n-1)}
    T={(i,n-1) for i in range(n)} | {(n-1,j) for j in range(n-1)}
    return V,E,S,T

def edmonds_karp(n, openmask, undirected=False):
    V,E,S,T=grid(n)
    ss=("s",); tt=("t",)
    cap={}
    adj={}
    def add_arc(u,v,c):
        adj.setdefault(u,[]); adj.setdefault(v,[])
        if v not in adj[u]: adj[u].append(v)
        if u not in adj[v]: adj[v].append(u)
        cap[(u,v)]=cap.get((u,v),0)+c
        cap.setdefault((v,u),0)
    BIG=100
    for s in S: add_arc(ss,s,BIG)
    for t in T: add_arc(t,tt,BIG)
    for k,(u,v) in enumerate(E):
        c=(openmask>>k)&1
        add_arc(u,v,c)
        if undirected:
            add_arc(v,u,c)
    flow=0
    while True:
        parent={ss:None}
        q=deque([ss])
        while q and tt not in parent:
            u=q.popleft()
            for v in adj.get(u,[]):
                if v not in parent and cap.get((u,v),0)>0:
                    parent[v]=u; q.append(v)
                    if v==tt: break
        if tt not in parent: break
        v=tt; aug=10**9
        while parent[v] is not None:
            u=parent[v]; aug=min(aug,cap[(u,v)]); v=u
        v=tt
        while parent[v] is not None:
            u=parent[v]
            cap[(u,v)]-=aug
            cap[(v,u)]=cap.get((v,u),0)+aug
            v=u
        flow+=aug
    return flow

def brute_cut_value(n, openmask):
    V,E,S,T=grid(n)
    free=[v for v in V if v not in S and v not in T]
    best=10**9
    for a in range(1<<len(free)):
        A=set(S)
        for i,v in enumerate(free):
            if (a>>i)&1: A.add(v)
        val=0
        for k,(u,v) in enumerate(E):
            if u in A and v not in A:
                val += (openmask>>k)&1
        best=min(best,val)
    return best

def main():
    n=3
    V,E,S,T=grid(n)
    m=len(E)
    K=2*n-2
    all_open=(1<<m)-1
    assert edmonds_karp(n,all_open,False)==K
    assert edmonds_karp(n,all_open,True)==K
    checked=0
    max_gap=0
    for openmask in range(1<<m):
        vd=edmonds_karp(n,openmask,False)
        vu=edmonds_karp(n,openmask,True)
        cut=brute_cut_value(n,openmask)
        assert vd==cut, (openmask,vd,cut)
        assert vd<=vu, (openmask,vd,vu)
        closedmask=all_open ^ openmask
        # exact defect rewrite:
        # K-vd = max_A [#closed outgoing(A) - (|outgoing(A)|-K)].
        free=[v for v in V if v not in S and v not in T]
        best=-10**9
        for a in range(1<<len(free)):
            A=set(S)
            for i,v in enumerate(free):
                if (a>>i)&1: A.add(v)
            out=[k for k,(u,v) in enumerate(E) if u in A and v not in A]
            score=sum((closedmask>>k)&1 for k in out) - (len(out)-K)
            best=max(best,score)
        assert K-vd==best, (openmask,K-vd,best)
        max_gap=max(max_gap,vu-vd)
        checked+=1
    print("SELF-CHECK ONLY; theorem proof is in the R01 report.")
    print(f"n={n}")
    print(f"directed_grid_edges={m}")
    print(f"configurations_checked={checked}")
    print(f"all_open_flow_K={K}")
    print("verified: directed max-flow = brute directed min-cut for every configuration")
    print("verified: exact cut-defect rewrite for every configuration")
    print("verified: directed max-flow <= undirected max-flow for every configuration")
    print(f"max_undirected_minus_directed_flow_seen={max_gap}")
    # Exact n=4 witness that the undirected relaxation can be strict.
    n4=4
    _,E4,_,_=grid(n4)
    closed_indices=(2,8,11,12)
    open4=(1<<len(E4))-1
    for k in closed_indices:
        open4 ^= (1<<k)
    vd4=edmonds_karp(n4,open4,False)
    vu4=edmonds_karp(n4,open4,True)
    assert (vd4,vu4)==(3,4), (vd4,vu4)
    print(f"n4_strict_relaxation_witness_closed_indices={closed_indices}")
    print(f"n4_directed_flow={vd4}")
    print(f"n4_undirected_flow={vu4}")
    print("verified: undirected relaxation can be strict at finite n")
    print("PASS")

if __name__=="__main__":
    main()
