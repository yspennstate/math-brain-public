import numpy as np, itertools, math

rng = np.random.default_rng(20260924)

def e2_psd(B):
    return (np.trace(B)**2 - np.trace(B@B))/2.0

def e3_psd(B):
    tr1=np.trace(B); tr2=np.trace(B@B); tr3=np.trace(B@B@B)
    return (tr1**3 - 3*tr1*tr2 + 2*tr3)/6.0

def proj_Z(K,m):
    if np.linalg.norm(m)<1e-13:
        C=K.copy()
    else:
        q=m/np.linalg.norm(m)
        C=K@(np.eye(K.shape[1])-np.outer(q,q))
    return e2_psd(C@C.T)

def fixed_oriented_phi(A,I,J,h,k):
    total=0.0
    for r,s in itertools.combinations(I,2):
        for j,l in itertools.combinations(J,2):
            total += np.linalg.det(A[np.ix_([h,r,s],[k,j,l])])**2
    return total

def test_instance(nH=5,nI=3,nJ=4):
    n=nH+nI+nJ
    M=rng.normal(size=(n,n))
    A=(M+M.T)/2
    H=list(range(nH)); I=list(range(nH,nH+nI)); J=list(range(nH+nI,n))
    K=A[np.ix_(I,J)]
    Z={h:proj_Z(K,A[h,J]) for h in H}
    min_ratio=float('inf')
    for h in H:
        for k in H:
            if h==k: continue
            rhs=A[h,k]**2*Z[h]
            phi=fixed_oriented_phi(A,I,J,h,k)
            if rhs>1e-12:
                min_ratio=min(min_ratio,phi/rhs)
            assert phi+1e-8 >= rhs
    weighted=sum(A[h,k]**2*(Z[h]+Z[k]) for h,k in itertools.combinations(H,2))
    best=-1e99
    for bits in itertools.product([0,1], repeat=nH):
        L=[H[t] for t,b in enumerate(bits) if b==0]
        R=[H[t] for t,b in enumerate(bits) if b==1]
        X=A[np.ix_(L+I,R+J)]
        best=max(best,e3_psd(X@X.T))
    assert best+1e-7 >= weighted/4
    return min_ratio,best-weighted/4

mins=[]; gaps=[]
for _ in range(120):
    r,g=test_instance(int(rng.integers(3,7)),3,4)
    mins.append(r); gaps.append(g)
print('oriented_trials',120)
print('min_phi_over_rhs',min(mins))
print('min_bestcut_minus_quarter_weighted',min(gaps))

def independence_number(adj):
    n=len(adj); best=0
    for mask in range(1<<n):
        bits=[i for i in range(n) if mask>>i&1]
        if len(bits)<=best: continue
        if all(not adj[i,j] for i,j in itertools.combinations(bits,2)):
            best=len(bits)
    return best

graph_min=float('inf'); graph_trials=0
for n in range(5,10):
    for _ in range(80):
        cut=int(rng.integers(1,n))
        adj=np.ones((n,n),dtype=bool); np.fill_diagonal(adj,False)
        for i in range(cut):
            for j in range(cut,n):
                if rng.random()<0.5:
                    adj[i,j]=adj[j,i]=False
        assert independence_number(adj)<=2
        for _attempt in range(1000):
            w=rng.random(n); W=w.sum()
            if w.max()<W/4: break
        deg=adj.sum(axis=1)
        lhs=(deg*(w**2)).sum()
        ratio=lhs/(W**2/4)
        graph_min=min(graph_min,ratio)
        assert lhs+1e-12 >= W**2/4
        graph_trials+=1
print('graph_trials',graph_trials)
print('min_graph_ratio_to_W2_over4',graph_min)

S0=2/3125; d=1/64; W0=S0/4
eta0=d*d*W0/4; E3hi=W0/576
C3=3*2**(4/3)*math.e**(1/3)
sq_bound=8*math.e**0.25*eta0**(-1/8)
e3_hi_bound=C3*E3hi**(-1/6)
low_edge=1/12500; low_e3=low_edge/4
low_bound=C3*low_e3**(-1/6)
print('S0',S0)
print('W0',W0)
print('eta0',eta0)
print('E3_high_dense_min',E3hi)
print('square_bound',sq_bound)
print('high_dense_Z3_bound',e3_hi_bound)
print('low_edge_threshold',low_edge)
print('low_Z3_min',low_e3)
print('low_Z3_bound',low_bound)
print('STATUS=PASS')
