"""Exact-formula checks for conditional two-site Lorentz matrices."""
import numpy as np
from explore import data
from pathlib import Path
import json

def matrices(K,d):
    c,tau,M=d['c'],d['tau'],d['M']
    Ns=[]
    for k in range(3):
        a=K[k,k].real;v=K[:,k].copy();v[k]=0
        eta=(c[k]+tau*(1-a))/(a*(1-a))
        N=eta*np.outer(v,v.conj())
        N[k,k]=M[k,k]
        N[:,k]+=tau*v;N[k,:]+=tau*v.conj()
        Ns.append(N)
    return Ns,sum(Ns)-M

def run():
    rng=np.random.default_rng(616006)
    records=[]
    for _ in range(500):
        z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
        U,_=np.linalg.qr(z)
        e=1/(1+np.exp(-rng.normal(size=3)*3))
        K=(U*e)@U.conj().T
        d=data(K);Ns,R=matrices(K,d)
        records.append((np.linalg.eigvalsh(R)[0],K,d,R))
    rec=min(records,key=lambda r:r[0])
    out={'tested':len(records),'min_R_eigenvalue':float(rec[0]),'K':str(rec[1]),'R':str(rec[3]),'tau':float(rec[2]['tau']),'c':rec[2]['c'].tolist()}
    Path(__file__).with_name('conditional_geometry_results.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))

if __name__=='__main__':run()
