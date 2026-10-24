from itertools import combinations

def is_forest(n, edges):
    p=list(range(n))
    def f(a):
        while p[a]!=a:
            p[a]=p[p[a]]
            a=p[a]
        return a
    for u,v in edges:
        a,b=f(u),f(v)
        if a==b: return False
        p[a]=b
    return True

def uv_connected(n, edges, u, v):
    p=list(range(n))
    def f(a):
        while p[a]!=a:
            p[a]=p[p[a]]
            a=p[a]
        return a
    for a,b in edges:
        x,y=f(a),f(b)
        if x!=y: p[x]=y
    return f(u)==f(v)

def weighted_counts(n, edges, e, f, vars):
    z=ze=zf=zef=0
    m=len(edges)
    for mask in range(1<<m):
        sub=[edges[i] for i in range(m) if mask>>i&1]
        if not is_forest(n,sub): continue
        w=1
        for h in sub: w*=vars.get(h,1)
        z+=w
        ie=e in sub
        jf=f in sub
        if ie: ze+=w
        if jf: zf+=w
        if ie and jf: zef+=w
    return z,ze,zf,zef

def gap(c):
    z,ze,zf,zef=c
    return ze*zf-z*zef

def star_mixed_examples():
    mp={0:0,2:1,3:2,4:3}
    orig=[(0,2),(0,3),(0,4),(2,3),(2,4),(3,4)]
    edges=[tuple(sorted((mp[a],mp[b]))) for a,b in orig]
    e=tuple(sorted((mp[0],mp[3])))
    f=tuple(sorted((mp[2],mp[4])))
    h1=tuple(sorted((mp[2],mp[3])))
    h2=tuple(sorted((mp[3],mp[4])))
    vals={}
    for a,b in [(1,1),(2,1),(1,2),(2,2)]:
        vals[(a,b)]=gap(weighted_counts(4,edges,e,f,{h1:a,h2:b}))
    mix=vals[(2,2)]-vals[(2,1)]-vals[(1,2)]+vals[(1,1)]
    print("NEG_MIXED", vals, "mixed=", mix)
    assert vals=={(1,1):6,(2,1):12,(1,2):12,(2,2):16} and mix==-2

    edges=[(0,1),(0,2),(0,3),(1,2)]
    e=(0,1); f=(1,2); h1=(0,2); h2=(0,3)
    vals={}
    for a,b in [(1,1),(2,1),(1,2),(2,2)]:
        vals[(a,b)]=gap(weighted_counts(4,edges,e,f,{h1:a,h2:b}))
    mix=vals[(2,2)]-vals[(2,1)]-vals[(1,2)]+vals[(1,1)]
    print("POS_MIXED", vals, "mixed=", mix)
    assert vals=={(1,1):8,(2,1):24,(1,2):18,(2,2):54} and mix==20

def conditional_exhaustive(n):
    all_edges=list(combinations(range(n),2))
    uv=(0,1)
    rem=[h for h in all_edges if h!=uv]
    N=1<<len(rem)
    a=[0]*N
    for mask in range(N):
        sub=[rem[i] for i in range(len(rem)) if mask>>i&1]
        if is_forest(n,sub) and not uv_connected(n,sub,0,1):
            a[mask]=1
    zeta=a[:]
    for i in range(len(rem)):
        bit=1<<i
        for mask in range(N):
            if mask&bit:
                zeta[mask]+=zeta[mask^bit]
    failures=0
    checked_pairs=0
    for J in range(N):
        inds=[i for i in range(len(rem)) if J>>i&1]
        if len(inds)<2: continue
        Z=zeta[J]
        for ii,jj in combinations(inds,2):
            Ze=Z-zeta[J^(1<<ii)]
            Zf=Z-zeta[J^(1<<jj)]
            Zef=Z-zeta[J^(1<<ii)]-zeta[J^(1<<jj)]+zeta[J^(1<<ii)^(1<<jj)]
            checked_pairs+=1
            if Ze*Zf-Z*Zef<0:
                failures+=1
                print("COND_FAIL",n,J,rem[ii],rem[jj],Ze*Zf-Z*Zef)
                return failures, checked_pairs
    return failures, checked_pairs

def pendant_scaling_exhaustive(maxn=5):
    total=0
    for n in range(2,maxn+1):
        E=list(combinations(range(n),2))
        for mask in range(1<<len(E)):
            H=[E[i] for i in range(len(E)) if mask>>i&1]
            if len(H)<2: continue
            for e,f in combinations(H,2):
                dH=gap(weighted_counts(n,H,e,f,{}))
                Q=H+[(0,n)]
                dQ=gap(weighted_counts(n+1,Q,e,f,{(0,n):2}))
                assert dQ==9*dH
                total+=1
    print("PENDANT_SCALE checked_marked_instances=",total,"factor=9")

if __name__=="__main__":
    star_mixed_examples()
    for n in range(3,7):
        fail,pairs=conditional_exhaustive(n)
        print("COND_N",n,"failures=",fail,"marked_pairs_checked=",pairs)
        assert fail==0
    pendant_scaling_exhaustive(5)
    print("STATUS=PASS")
