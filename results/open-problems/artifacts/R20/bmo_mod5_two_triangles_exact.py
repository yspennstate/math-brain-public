from itertools import permutations

S=(0,1,2)

def w_arc(d):
    assert d>=2
    if d==2:return [0,2,0]
    if d==3:return [0,1,2,0]
    if d==4:return [0,2,1,2,0]
    if d==5:return [0,2,0,1,2,0]
    q,r=divmod(d-6,4)
    tails={0:[2],1:[1,2],2:[1,0,2],3:[1,0,0,2]}
    return [0,2,0,0,0]+[z for _ in range(q) for z in (1,0,0,0)]+tails[r]+[0]

def y_adj(m):
    assert m>=4
    if m==4:return [0,1,0,2]
    if m==5:return [0,1,0,0,2]
    q,r=divmod(m-6,4)
    tails={0:[2],1:[1,2],2:[1,0,2],3:[1,0,0,2]}
    return [0,1,0,0,0]+[z for _ in range(q) for z in (1,0,0,0)]+tails[r]

def tri_options(a,e):
    out={}
    for b,c in permutations(S,2):
        leaf_b=(2*b+a+c)%5
        leaf_c=(2*c+a+b)%5
        root=(e+2*a+b+c)%5
        if leaf_b!=leaf_c and root!=leaf_b and root!=leaf_c:
            out.setdefault(root,(b,c))
    return out

def build(m,k):
    assert m>=4 and 1<=k<m
    reflected=(k==m-1)
    target_k=k
    if reflected:k=1
    if k==1:
        y=y_adj(m)
    else:
        y=[None]*m
        a=w_arc(k)
        for i,z in enumerate(a): y[i]=z
        b=w_arc(m-k)
        for j,z in enumerate(b):
            i=(k+j)%m
            if y[i] is not None: assert y[i]==z
            y[i]=z
        assert all(z is not None for z in y)
    if reflected:
        yy=[None]*m
        for i,z in enumerate(y): yy[(-i)%m]=z
        y=yy;k=target_k

    roots=[0,k]
    central=[(2*y[i]+y[(i-1)%m]+y[(i+1)%m])%5 for i in range(m)]
    opts={}
    for r in roots:
        opts[r]=tri_options(y[r],central[r])
        assert len(opts[r])==3,(m,k,r,y[r],central[r],opts[r])

    choose={}
    if k in (1,m-1):
        fixed0=m-1 if k==1 else 1
        fixedk=2 if k==1 else m-2
        A=[s for s in opts[0] if s!=central[fixed0]]
        B=[s for s in opts[k] if s!=central[fixedk]]
        for s0 in A:
            for sk in B:
                if s0!=sk:
                    choose[0],choose[k]=s0,sk
                    break
            if 0 in choose: break
        assert len(choose)==2
    else:
        for r in roots:
            forbid={central[(r-1)%m],central[(r+1)%m]}
            A=[s for s in opts[r] if s not in forbid]
            assert A
            choose[r]=A[0]

    adj={i:set() for i in range(m+4)}
    for i in range(m):
        j=(i+1)%m;adj[i].add(j);adj[j].add(i)
    Y={i:y[i] for i in range(m)}
    nxt=m
    for r in roots:
        b,c=opts[r][choose[r]]
        u,v=nxt,nxt+1;nxt+=2
        for p,q in ((r,u),(u,v),(v,r)):
            adj[p].add(q);adj[q].add(p)
        Y[u]=b;Y[v]=c

    qcol={v:(len(adj[v])*Y[v]+sum(Y[u] for u in adj[v]))%5 for v in adj}
    assert all(qcol[u]!=qcol[v] for u in adj for v in adj[u] if u<v)
    rho={v:2-Y[v] for v in adj}
    sigma={v:(1+rho[v])*len(adj[v])+sum(rho[u] for u in adj[v]) for v in adj}
    assert all((sigma[v]+qcol[v])%5==0 for v in adj)
    assert all(sigma[u]!=sigma[v] for u in adj for v in adj[u] if u<v)
    assert max(rho.values())<=2

def check_words(limit):
    for d in range(2,limit+1):
        a=w_arc(d)
        assert len(a)==d+1 and a[0]==a[-1]==0
        if d==3:
            assert (a[1],a[-2])==(1,2)
        else:
            assert (a[1],a[-2])==(2,2)
        col=[(2*a[i]+a[i-1]+a[i+1])%5 for i in range(1,d)]
        assert all(col[i]!=col[i+1] for i in range(len(col)-1))
    for m in range(4,limit+1):
        y=y_adj(m)
        assert len(y)==m
        col=[(2*y[i]+y[i-1]+y[(i+1)%m])%5 for i in range(2,m)]
        assert all(col[i]!=col[i+1] for i in range(len(col)-1))
        assert (3*y[0]+y[1]+y[-1])%5 in (3,4)
        assert (3*y[1]+y[0]+y[2])%5 in (3,4)

check_words(500)
cases=0
for m in range(4,301):
    for k in range(1,m):
        build(m,k);cases+=1
print('R20 BMO mod-5 exact construction check')
print('word_lengths_checked_through=500')
print('central_cycle_lengths_checked=4..300')
print('ordered_attachment_distances_checked=%d'%cases)
print('all_constructed_pushes_in={0,1,2}')
print('all_edges_distinct_mod_5=True')
print('all_edges_distinct_over_Z=True')
print('VERDICT=PASS')