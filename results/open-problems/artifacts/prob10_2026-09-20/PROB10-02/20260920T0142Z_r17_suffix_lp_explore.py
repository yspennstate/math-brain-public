from itertools import product
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


def T(z,k,v,c,u):
    x=z[:k]; g=z[k:]
    d=[0]*(k+1); d[0]=c
    for j in range(1,k+1):
        d[j]=(1-g[j-1])*int(bool(d[j-1] or x[j-1]==v))
    gp=[]
    for j in range(1,k):
        gp.append(g[j]+d[j+1]-d[j])
    gp.append((1-d[k])*int(u==v))
    return tuple(x[1:]+(u,)+tuple(gp))


def solve(k):
    bits=list(product((0,1), repeat=k))
    states=[tuple(x+g) for x in bits for g in bits]
    idx={z:i for i,z in enumerate(states)}
    S=len(states); nv=4*S
    def vid(si,v,c): return 4*si+2*v+c
    rows=[]; cols=[]; vals=[]; rhs=[]
    r=0
    # fair-v constraint at each state
    for si in range(S):
        for c in (0,1):
            rows += [r,r]; cols += [vid(si,0,c),vid(si,1,c)]; vals += [1.0,-1.0]
        rhs.append(0.0); r+=1
    fb=r
    # -mu on each flow row
    for si in range(S):
        for v in (0,1):
            for c in (0,1):
                rows.append(fb+si); cols.append(vid(si,v,c)); vals.append(-1.0)
    # incoming flow
    for si,z in enumerate(states):
        for v in (0,1):
            for c in (0,1):
                j=vid(si,v,c)
                for u in (0,1):
                    sj=idx[T(z,k,v,c,u)]
                    rows.append(fb+sj); cols.append(j); vals.append(0.5)
    rhs += [0.0]*S; r+=S
    # normalization
    for j in range(nv):
        rows.append(r); cols.append(j); vals.append(1.0)
    rhs.append(1.0); r+=1
    A=coo_matrix((vals,(rows,cols)),shape=(r,nv)).tocsr()
    obj=np.zeros(nv)
    for si,z in enumerate(states):
        for v in (0,1):
            for c in (0,1): obj[vid(si,v,c)]=-z[-1]
    res=linprog(obj,A_eq=A,b_eq=np.array(rhs),bounds=(0,None),method='highs')
    return -res.fun, res

for k in range(1,5):
    p,res=solve(k)
    print(f'k={k} success={res.success} p_star~{p:.15f} Gamma_k~{1-p:.15f} iterations={res.nit}')
print('NUMERICAL_ONLY_NOT_A_CERTIFICATE')
