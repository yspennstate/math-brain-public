"""Independent Gaussian quadrature checks of the unsubmitted closed drift.

This is a numerical formula check, never an interval or convergence proof.
"""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS']:
    os.environ[name] = '1'
from resource_limits import apply_limits
RESOURCE_LIMITS=apply_limits()
from pathlib import Path
import hashlib
import json
import math
import numpy as np
from scipy.special import erf
from numpy.polynomial.hermite import hermgauss

ROOT=Path(__file__).resolve().parents[1]
MU=2/math.pi

def kernel(v,w,z):
    arg=z/math.sqrt((1+v)*(1+w))
    if not -1 < arg < 1:
        raise ValueError(('Invalid Gaussian kernel argument',arg))
    return MU*math.asin(arg)

def closed(q,c,r,eta):
    A=MU/math.sqrt(1+2*q)
    B=MU/math.sqrt((1+q)**2-c*c)
    T=MU/math.sqrt(2*(1+q)-r*r)
    beta=(q*A+c*B-2*r*T)/(1+q)
    D=1+2*q
    u,v,w=q/D,q-2*c*c/D,c/D
    t,s=1-2*r*r/D,-2*r*r/D
    x,y=r/D,r-2*c*r/D
    C0=A*(kernel(u,u,u)+kernel(v,v,v)+2*kernel(u,v,w)
          +2*kernel(t,t,t)+2*kernel(t,t,s)
          -4*kernel(u,t,x)-4*kernel(v,t,y))
    P,L=q+c,q-c
    u=(P/(1+P)+L/(1+L))/2
    w=(P/(1+P)-L/(1+L))/2
    t,s,x=1-2*r*r/(1+P),-2*r*r/(1+P),r/(1+P)
    C1=B*(2*kernel(u,u,u)+2*kernel(u,u,w)
          +2*kernel(t,t,t)+2*kernel(t,t,s)-8*kernel(u,t,x))
    drift=[-2*eta*beta+eta*eta*C0,
           2*eta*((beta-A)*c-B*q+2*r*T)+eta*eta*C1,
           eta*(T+(beta-A-B)*r)]
    return np.array([beta,C0,C1,*drift])

def quadrature(q,c,r,eta,order):
    G=np.array([[q,c,r,r],[c,q,r,r],[r,r,1,0],[r,r,0,1]])
    chol=np.linalg.cholesky(G)
    nodes,weights=hermgauss(order)
    nodes=nodes*math.sqrt(2)
    weights=weights/math.sqrt(math.pi)
    n1,n2,n3=np.meshgrid(nodes,nodes,nodes,indexing='ij')
    tail=np.column_stack([n1.ravel(),n2.ravel(),n3.ravel()])
    wt=np.einsum('i,j,k->ijk',weights,weights,weights).ravel()
    ans=np.zeros(6)
    for node,weight in zip(nodes,weights):
        base=np.column_stack([np.full(len(tail),node),tail])
        f=base@chol.T
        g=erf(f/math.sqrt(2))
        gp=math.sqrt(MU)*np.exp(-f[:,:2]**2/2)
        e=g[:,2]+g[:,3]-g[:,0]-g[:,1]
        h1,h2,z1=f[:,0],f[:,1],f[:,2]
        c0=e*e*gp[:,0]**2
        c1=e*e*gp[:,0]*gp[:,1]
        vals=[-e*h1*gp[:,0],c0,c1,
              2*eta*e*gp[:,0]*h1+eta*eta*c0,
              eta*e*(gp[:,0]*h2+gp[:,1]*h1)+eta*eta*c1,
              eta*e*gp[:,0]*z1]
        ans+=weight*np.array([wt@v for v in vals])
    return ans

def main():
    cases=[(1.,0.,0.,.5),(.8,.1,.2,.5),(.37,.32,.41,.5),
           (.36771969907760643,.32538554792403124,
            .4143941508524791,.5)]
    rows=[]
    for case in cases:
        exact=closed(*case)
        low=quadrature(*case,24)
        high=quadrature(*case,32)
        error=float(np.max(np.abs(high-exact)))
        convergence=float(np.max(np.abs(high-low)))
        rows.append({'point':case,'closed':exact.tolist(),
                     'GH24':low.tolist(),'GH32':high.tolist(),
                     'max_error':error,'quadrature_change':convergence})
        if error>2e-6 or convergence>2e-5:
            raise AssertionError(rows[-1])
    output={'passed':True,'scope':'numerical formula check only',
            'sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'cases':rows}
    (ROOT/'logs'/'symmetric_closed_check.json').write_text(
        json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output),flush=True)

if __name__=='__main__':
    main()
