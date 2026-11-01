import numpy as np
from fractions import Fraction

def wreath_cycle(m):
    # C_m [ empty K2 ]: vertices (j,e), j in Z_m, e in {0,1}; (j,e)~(j+-1,e')
    V=[(j,e) for j in range(m) for e in range(2)]
    idx={v:i for i,v in enumerate(V)}
    n=len(V)
    A=np.zeros((n,n))
    for (j,e) in V:
        for dj in (-1,1):
            for e2 in (0,1):
                A[idx[(j,e)],idx[((j+dj)%m,e2)]]=1
    return V,idx,A

def hitting_times(A,target):
    # E_i[T_target] for SRW, solve (I-P)h=1 off target
    n=A.shape[0]; P=A/A.sum(1,keepdims=True)
    keep=[i for i in range(n) if i!=target]
    M=np.eye(len(keep))-P[np.ix_(keep,keep)]
    h=np.linalg.solve(M,np.ones(len(keep)))
    out=np.zeros(n)
    for k,i in enumerate(keep): out[i]=h[k]
    return out

for m in [5,7,9,11,15,21]:
    V,idx,A=wreath_cycle(m); n=2*m
    deg=A.sum(1); pi=deg/deg.sum()
    H=np.array([hitting_times(A,t) for t in range(n)]).T   # H[i,t]=E_i T_t
    C=H+H.T                                                 # commute
    tau_star=C.max()
    tau0=float(sum(pi[t]*sum(pi[i]*H[i,t] for i in range(n)) for t in range(n)))
    # relaxation time of SRW (regular graph -> P symmetric)
    P=A/deg[:,None]
    ev=np.sort(np.linalg.eigvalsh((P+P.T)/2))
    lam=max(abs(ev[0]),ev[-2])
    tau2=1/(1-ev[-2])
    # claimed formulas
    cl_hit_diff = lambda j: j*(m-j)+m
    ok_hit=all(abs(H[idx[(0,0)],idx[(j,e)]]-cl_hit_diff(j))<1e-7 for j in range(1,m) for e in (0,1))
    ok_twin=abs(H[idx[(0,0)],idx[(0,1)]]-2*m)<1e-7
    cl_star=2*(m*m//4)+2*m
    cl_tau0=(m*m-1)/6+m
    cl_tau2=1/(1-np.cos(2*np.pi/m))
    print(f"m={m:3d} n={n:3d} | hit-formula {ok_hit} twin {ok_twin} | tau*={tau_star:.4f} (claim {cl_star}) "
          f"tau0={tau0:.4f} (claim {cl_tau0:.4f}) tau2={tau2:.4f} (claim {cl_tau2:.4f}) "
          f"| tau*/(2 tau0)={tau_star/(2*tau0):.4f}  tau*/(n log n)={tau_star/(n*np.log(n)):.3f}  tau2/n={tau2/n:.3f}")
