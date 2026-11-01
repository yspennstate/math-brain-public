import numpy as np, itertools
from scipy.optimize import linprog
rng=np.random.default_rng(5)
def dpm(Q,k,N):
    """determinantal measure of a rank-k projection Q on {0..N-1}: P(S)=det(Q_S), |S|=k"""
    out={}
    for S in itertools.combinations(range(N),k):
        out[S]=float(np.linalg.det(Q[np.ix_(S,S)]))
    return out
def rand_split(N,k1,k2,seed):
    r=np.random.default_rng(seed)
    A=r.normal(size=(N,k1+k2)); Qf,_=np.linalg.qr(A)
    V1=Qf[:,:k1]; V2=Qf[:,k1:k1+k2]
    return V1@V1.T, V2@V2.T
print("Lyons Question 2.8: couple P_{Q1}, P_{Q2} (disjointly) so the UNION is P_{Q1+Q2}.")
print("Feasibility by LP over joint distributions on disjoint pairs (S1,S2).")
print(f"{'N':>3} {'k1':>3} {'k2':>3} {'instances':>10} {'feasible':>9} {'infeasible':>11}")
for (N,k1,k2) in [(4,1,1),(4,1,2),(4,2,1),(5,1,2),(5,2,2),(5,1,3),(6,2,2),(6,1,2),(6,2,3)]:
    feas=0; inf=0
    for trial in range(12):
        Q1,Q2=rand_split(N,k1,k2,1000*trial+N*17+k1*3+k2)
        Q=Q1+Q2
        p1=dpm(Q1,k1,N); p2=dpm(Q2,k2,N); pu=dpm(Q,k1+k2,N)
        pairs=[(S1,S2) for S1 in p1 for S2 in p2 if not set(S1)&set(S2)]
        idx={pr:i for i,pr in enumerate(pairs)}
        rows=[];rhs=[]
        for S1 in p1:
            r=np.zeros(len(pairs))
            for pr in pairs:
                if pr[0]==S1: r[idx[pr]]=1
            rows.append(r); rhs.append(p1[S1])
        for S2 in p2:
            r=np.zeros(len(pairs))
            for pr in pairs:
                if pr[1]==S2: r[idx[pr]]=1
            rows.append(r); rhs.append(p2[S2])
        for U in pu:
            r=np.zeros(len(pairs))
            for pr in pairs:
                if tuple(sorted(set(pr[0])|set(pr[1])))==U: r[idx[pr]]=1
            rows.append(r); rhs.append(pu[U])
        res=linprog(np.zeros(len(pairs)),A_eq=np.array(rows),b_eq=np.array(rhs),bounds=(0,None),method='highs')
        if res.status==0: feas+=1
        else: inf+=1
    print(f"{N:>3} {k1:>3} {k2:>3} {12:>10} {feas:>9} {inf:>11}")
