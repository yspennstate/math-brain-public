import numpy as np, itertools
from scipy.optimize import linprog
def dpm(Q,k,N):
    return {S: float(np.linalg.det(Q[np.ix_(S,S)])) for S in itertools.combinations(range(N),k)}
def build(N,k1,k2,seed):
    r=np.random.default_rng(seed)
    A=r.normal(size=(N,k1+k2)); Qf,_=np.linalg.qr(A)
    V1=Qf[:,:k1]; V2=Qf[:,k1:k1+k2]
    return V1,V2,V1@V1.T,V2@V2.T
def lp(N,k1,k2,seed,obj):
    V1,V2,Q1,Q2=build(N,k1,k2,seed); Q=Q1+Q2
    p1=dpm(Q1,k1,N); p2=dpm(Q2,k2,N); pu=dpm(Q,k1+k2,N)
    pairs=[(S1,S2) for S1 in p1 for S2 in p2 if not set(S1)&set(S2)]
    idx={pr:i for i,pr in enumerate(pairs)}
    rows=[];rhs=[]
    for S1 in p1:
        r=np.zeros(len(pairs))
        for pr in pairs:
            if pr[0]==S1: r[idx[pr]]=1
        rows.append(r);rhs.append(p1[S1])
    for S2 in p2:
        r=np.zeros(len(pairs))
        for pr in pairs:
            if pr[1]==S2: r[idx[pr]]=1
        rows.append(r);rhs.append(p2[S2])
    for U in pu:
        r=np.zeros(len(pairs))
        for pr in pairs:
            if tuple(sorted(set(pr[0])|set(pr[1])))==U: r[idx[pr]]=1
        rows.append(r);rhs.append(pu[U])
    res=linprog(obj(len(pairs)),A_eq=np.array(rows),b_eq=np.array(rhs),bounds=(0,None),method='highs')
    return res,pairs,V1,V2
print("Is the coupling UNIQUE?  Optimise in several random directions; if the solution is unique they coincide.")
print(f"{'N':>3} {'k1':>3} {'k2':>3} {'max spread over 6 objectives':>30}")
for (N,k1,k2) in [(4,1,1),(4,1,2),(5,2,2),(5,1,3),(6,2,2)]:
    worst=0.0
    for seed in [11,29,53]:
        sols=[]
        for t in range(6):
            rr=np.random.default_rng(700+t)
            res,pairs,V1,V2=lp(N,k1,k2,seed,lambda n: rr.normal(size=n))
            if res.status!=0: sols=None; break
            sols.append(res.x)
        if sols:
            S=np.array(sols); worst=max(worst,float(np.abs(S.max(0)-S.min(0)).max()))
    print(f"{N:>3} {k1:>3} {k2:>3} {worst:>30.6f}")
print("\n(spread ~0 => the coupling is essentially unique; large => a whole polytope of couplings)")
