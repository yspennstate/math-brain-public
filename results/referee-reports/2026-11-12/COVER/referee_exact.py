"""First-principles rational cover times, holding occupation, and Laplacian audit.

No authors' modules are imported. Each visited-set block solves (I-P_SS)t=b.
A separate, full augmented-state solve cross-checks selected cases.
"""
import itertools as it
import json
import random
import resource
import signal
import time
from fractions import Fraction as F
from pathlib import Path

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError()))
signal.alarm(280)

def solve(A,B):
    """Gaussian elimination with multiple RHS and back substitution."""
    n=len(A)
    if not n:
        return []
    k=len(B[0])
    M=[[F(x) for x in a+b] for a,b in zip(A,B)]
    for j in range(n):
        p=next(i for i in range(j,n) if M[i][j])
        M[j],M[p]=M[p],M[j]
        for i in range(j+1,n):
            if M[i][j]:
                r=M[i][j]/M[j][j]
                for v in range(j+1,n+k):
                    M[i][v]-=r*M[j][v]
                M[i][j]=F(0)
    X=[[F(0)]*k for _ in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(k):
            X[i][j]=(M[i][n+j]-sum(M[i][v]*X[v][j] for v in range(i+1,n)))/M[i][i]
    return X

def chain(n,w,h):
    q=[F(0)]*n
    P=[[F(0)]*n for _ in range(n)]
    for (i,j),v in zip(it.combinations(range(n),2),w):
        q[i]+=v
        q[j]+=v
        P[i][j]=P[j][i]=v
    m=[q[i]+h[i] for i in range(n)]
    assert all(v>0 for v in q)
    L=[[q[i] if i==j else -P[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        P[i][i]=h[i]
        P[i]=[F(v)/m[i] for v in P[i]]
    assert all(sum(row)==1 for row in P)
    assert all(m[i]*P[i][j]==m[j]*P[j][i] for i in range(n) for j in range(n))
    return P,q,m,L

def augmented_blocks(P,occupations=False):
    n=len(P)
    full=(1<<n)-1
    width=n if occupations else 1
    V={(full,i):[F(0)]*width for i in range(n)}
    for mask in sorted(range(1,full),key=int.bit_count,reverse=True):
        S=[i for i in range(n) if mask>>i&1]
        A=[[F(i==j)-P[i][j] for j in S] for i in S]
        B=[]
        for i in S:
            b=[F(i==y) for y in range(n)] if occupations else [F(1)]
            for j in range(n):
                if not(mask>>j&1):
                    for y in range(width):
                        b[y]+=P[i][j]*V[mask|1<<j,j][y]
            B.append(b)
        for i,v in zip(S,solve(A,B)):
            V[mask,i]=v
    return [V[1<<i,i] for i in range(n)]

def full_augmented(P):
    n=len(P)
    states=[(mask,i) for mask in range(1,(1<<n)-1) for i in range(n) if mask>>i&1]
    index={s:k for k,s in enumerate(states)}
    A=[[F(i==j) for j in range(len(states))] for i in range(len(states))]
    for k,(mask,i) in enumerate(states):
        for j in range(n):
            dest=(mask|1<<j,j)
            if dest in index:
                A[k][index[dest]]-=P[i][j]
    t=solve(A,[[F(1)] for _ in states])
    return [t[index[1<<i,i]][0] for i in range(n)]

def alternating(n,L,m):
    total=F(0)
    for mask in range(1,(1<<n)-1):
        S=[i for i in range(n) if mask>>i&1]
        v=solve([[L[i][j] for j in S] for i in S],[[m[i]] for i in S])
        total+=(-1)**(n-len(S)+1)*sum(m[i]*v[k][0] for k,i in enumerate(S))
    return total/sum(m)

def connected(n,w):
    seen={0}
    edges=list(it.combinations(range(n),2))
    for _ in range(n):
        for (i,j),v in zip(edges,w):
            if v and (i in seen or j in seen):
                seen.update((i,j))
    return len(seen)==n

def stationary(m,c):
    return sum(a*b for a,b in zip(m,c))/sum(m)

def inspect(n,w,holdings,full=False):
    w=list(map(F,w))
    Q,q,_,L=chain(n,w,[F(0)]*n)
    N=augmented_blocks(Q,True)
    K=[[N[i][j]/q[j] for j in range(n)] for i in range(n)]
    assert all(K[i][j]>=0 and K[i][j]==K[j][i] for i in range(n) for j in range(n))
    base=[sum(row) for row in N]
    assert all(v>=n-1 for v in base)
    baseE=stationary(q,base)
    c0=F(3) if n==3 else F(11,2)
    rows=[]
    for h in holdings:
        h=list(map(F,h))
        P,_,m,L=chain(n,w,h)
        c=[v[0] for v in augmented_blocks(P)]
        assert c==[sum(K[i][j]*m[j] for j in range(n)) for i in range(n)]
        E=stationary(m,c)
        assert E==alternating(n,L,m) and E>=c0
        assert (E==c0)==(len(set(w))==1 and not any(h))
        if full:
            assert c==full_augmented(P)
        rhs=sum(q)*(baseE-c0)+sum(h[i]*(2*base[i]-c0) for i in range(n))
        rhs+=sum(h[i]*K[i][j]*h[j] for i in range(n) for j in range(n))
        assert sum(m)*(E-c0)==rhs
        if n==3:
            a,b,cc=w
            defect=(4*(a**3+b**3+cc**3)-sum(a1*a1*b1 for i,a1 in enumerate(w) for j,b1 in enumerate(w) if i!=j)-6*a*b*cc)
            assert baseE-3==defect/(2*(a+b+cc)*(a*b+b*cc+cc*a))
        rows.append(dict(h=list(map(str,h)),from_states=list(map(str,c)),stationary=str(E)))
    return rows

def main():
    start=time.monotonic()
    rng=random.Random(61302026)
    names={
      3:{'K3':[1,1,1],'path3':[1,0,1],
         'holding_decrease':[1,F(1,100),F(1,100)],
         'near_disconnected':[1,F(1,10**9),F(1,10**9)]},
      4:{'K4':[1]*6,'path4':[1,0,0,1,0,1],'star4':[1,1,1,0,0,0],
         'cycle4':[1,0,1,1,0,1],'K4_minus_edge':[0,1,1,1,1,1],
         'near_disconnected':[1,F(1,10**9),F(1,10**9),F(1,10**9),F(1,10**9),1],
         'near_vertex_isolated':[1,1,F(1,10**12),1,F(1,10**12),F(1,10**12)]}}
    named={}
    chains=fullchecks=0
    for n,examples in names.items():
        for name,w in examples.items():
            holdings=[[0]*n,[1 if i==n-1 else 0 for i in range(n)],[F(1,1000) if i==0 else (10**6 if i==1 else 0) for i in range(n)]]
            named[f'{n}:{name}']=dict(weights=list(map(str,w)),results=inspect(n,w,holdings,True))
            chains+=3
            fullchecks+=3
    randomcounts={}
    for n in (3,4):
        count=0
        while count<80:
            w=[F(0) if rng.random()<0.2 else F(rng.randint(1,25),rng.choice([1,10,10**5])) for _ in range(n*(n-1)//2)]
            if not connected(n,w):
                continue
            hs=[[0]*n,[F(rng.randint(0,15),rng.choice([1,100,10**6])) for _ in range(n)]]
            inspect(n,w,hs,full=count<6)
            chains+=2
            fullchecks+=2*(count<6)
            count+=1
        randomcounts[n]=count
    grid=0
    equal=[]
    minimum=None
    for w in it.product(range(3),repeat=6):
        if not connected(4,w):
            continue
        rows=inspect(4,w,[[0]*4,[1,0,2,3],[0,1000,0,0]])
        grid+=1
        chains+=3
        for row in rows:
            E=F(row['stationary'])
            minimum=E if minimum is None else min(minimum,E)
            if E==F(11,2):
                equal.append(dict(weights=w,h=row['h']))
    # Exact finite max/min identity, independently for all small time vectors.
    for n in (3,4,5):
        for ts in it.product(range(3),repeat=n):
            val=sum((-1)**(len(J)+1)*min(ts[i] for i in J)
                    for k in range(1,n+1) for J in it.combinations(range(n),k))
            assert val==max(ts)
    out=dict(passed=True,named=named,random_loopless_weightings=randomcounts,grid_connected=grid,
             total_chains=chains,full_augmented_crosschecks=fullchecks,grid_minimum=str(minimum),
             grid_equalities=equal,seconds=time.monotonic()-start,
             max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    Path('referee_exact_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='named'},indent=2))
    for name,r in named.items():
        print(name,[(v['h'],v['stationary']) for v in r['results']])

if __name__=='__main__':
    main()
