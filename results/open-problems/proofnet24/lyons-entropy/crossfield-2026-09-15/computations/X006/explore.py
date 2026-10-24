"""Bounded diagnostics of explicit Lorentz certificates (not proof)."""
import json
import numpy as np
from pathlib import Path

BASIS=[]
for i in range(3):
    B=np.zeros((3,3),complex);B[i,i]=1;BASIS.append(B)
for i,j in [(0,1),(0,2),(1,2)]:
    B=np.zeros((3,3),complex);B[i,j]=B[j,i]=1/np.sqrt(2);BASIS.append(B)
    B=np.zeros((3,3),complex);B[i,j]=1j/np.sqrt(2);B[j,i]=-1j/np.sqrt(2);BASIS.append(B)

def data(K):
    p=[]; scores=[]
    for s in range(8):
        Q=K-np.diag([1-(s>>i&1) for i in range(3)])
        p.append((-1)**(3-s.bit_count())*np.linalg.det(Q).real)
        inv=np.linalg.inv(Q)
        scores.append([np.trace(inv@B).real for B in BASIS])
    p=np.array(p);scores=np.array(scores)
    f=-np.log(p)
    c=np.array([f[6]-f[2]-f[4]+f[0],f[5]-f[1]-f[4]+f[0],f[3]-f[1]-f[2]+f[0]])
    tau=f[7]-f[6]-f[5]-f[3]+f[4]+f[2]+f[1]-f[0]
    M=np.diag(c)+tau*K
    delta=np.linalg.det(M).real
    cov=np.diag(np.diag(K).real)-abs(K)**2
    d=np.diag(M).real
    three=d@np.linalg.solve(abs(M)**2+delta*cov,d)
    g=np.array([np.prod(c+tau*np.array([s>>i&1 for i in range(3)])) for s in range(8)])
    gprime=np.array([sum(np.prod(np.delete(c,i))*(s>>i&1) for i in range(3)) for s in range(8)])
    ratio=(p@(g-p@g)**2/(tau*tau*delta) if abs(tau)>1e-7 else p@(gprime-p@gprime)**2/delta)
    F=scores.T@(p[:,None]*scores)
    J=np.linalg.inv(M)
    N=F+delta*np.array([[np.trace(J@B@J@E).real for E in BASIS] for B in BASIS])
    ell=np.array([np.trace(J@B).real for B in BASIS])
    coef=np.linalg.solve(N,ell)
    Ast=sum(q*B for q,B in zip(coef,BASIS))
    scalar=delta*ell@coef
    return dict(p=p,c=c,tau=tau,M=M,delta=delta,ratio=ratio,three=three,scalar=scalar,astar_eig=np.linalg.eigvalsh(Ast))

def encode(d):
    return {k:(v.tolist() if isinstance(v,np.ndarray) and not np.iscomplexobj(v) else str(v) if np.iscomplexobj(v) else float(v)) for k,v in d.items()}

def run():
    rng=np.random.default_rng(600006)
    records=[]
    # The algebraic tau=0 family: D=(1-x)(1-y)(1-z).
    for k in range(800):
        xyz=1/(1+np.exp(-rng.normal(size=3)*2.5))
        x,y,z=xyz
        cosine=(x*y+x*z+y*z-x*y*z)/(2*np.sqrt(x*y*z))
        if cosine>=1: continue
        a,b,c=np.sqrt(xyz)
        R=np.array([[1,a,c*np.exp(-1j*np.arccos(cosine))],[a,1,b],[c*np.exp(1j*np.arccos(cosine)),b,1]])
        ell=np.exp(rng.normal(size=3)*3)
        L=np.sqrt(ell[:,None]*ell[None,:])*R
        K=np.linalg.solve(np.eye(3)+L,L)
        d=data(K)
        records.append((d,K,xyz,ell))
    worst_three=min(records,key=lambda q:q[0]['three'])
    worst_var=max(records,key=lambda q:q[0]['ratio'])
    negative_ast=min(records,key=lambda q:q[0]['astar_eig'][0])
    out={'tested':len(records)}
    for label,row in [('min_three',worst_three),('max_variance',worst_var),('min_astar',negative_ast)]:
        d,K,xyz,ell=row
        out[label]={'data':encode(d),'K':str(K),'xyz':xyz.tolist(),'fields':ell.tolist()}
    Path(__file__).with_name('tauzero_results.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))

if __name__=='__main__':run()
