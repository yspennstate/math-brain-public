"""Scalar root plus independent 4D products: deterministic, not GD."""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=110
k=mp.sqrt(mp.mpf(5)/4)
def vec(j):
    z=mp.matrix(4,1); z[j]=1; return z
e=[vec(j) for j in range(4)]
E=lambda i,j:e[i]*e[j].T
I=mp.eye(4); angles={}; records=[]
cases=[(n,'polynomial') for n in [8,32,128,512]]+[(8,'exponential'),(32,'exponential'),(32,'zero')]
for n,mode in cases:
    L=2*n+4; m=L; t=mp.sqrt(m)/n
    def rootfun(phi):
        w=mp.tan(phi/n); u=w*w/t
        return (k+u*u/k)*mp.cos(phi)+(k*u*u/w-w/k)*mp.sin(phi)
    if n not in angles:
        assert rootfun(mp.pi/4)>0 and rootfun(mp.pi/2)<0
        angles[n]=mp.findroot(rootfun,(mp.pi/4,mp.pi/2),solver='bisect',
                             tol=mp.mpf('1e-95'),maxsteps=400)
    phi=angles[n]; w=mp.tan(phi/n); u=w*w/t; rho=mp.sqrt(1+w*w)
    eps=mp.mpf(1)/n if mode=='polynomial' else mp.exp(-L) if mode=='exponential' else mp.mpf(0)
    B=I+t*E(0,2); C=I+t*E(3,1); A=B-u*E(2,0); Z=C-u*E(1,3)
    P=I-(1-eps)*E(2,2); Q=I-(1-eps)*E(3,3)
    P1=P-u*E(0,2); Q1=Q-u*E(3,1)
    v=k*e[0]; b=k*e[1]; a=v-u/k*e[2]; d=b-u/k*e[3]
    old=[v]+[B]*n+[P,Q]+[C]*n+[b.T]
    new=[a]+[A]*n+[P1,Q1]+[Z]*n+[d.T]
    drift=[]
    # These seven boundaries exhaust distinct adjacent-matrix pairs.
    for i in [0,1,n,n+1,n+2,n+3,2*n+2]:
        D=m*((new[i+1].T*new[i+1]-new[i]*new[i].T)-
             (old[i+1].T*old[i+1]-old[i]*old[i].T))
        drift.append(max(abs(z) for z in mp.eigsy(D,eigvals_only=True)))
    maxdrift=max(drift)
    assert maxdrift<=m*(u*u+eps*u)+mp.mpf('1e-85')
    pref=[mp.eye(1)]
    for mat in new[:-1]:pref.append(mat*pref[-1])
    suff=[None]*L;suff[-1]=mp.eye(1)
    for i in range(L-2,-1,-1):suff[i]=suff[i+1]*new[i+1]
    kernel=sum(mp.norm(pref[i])**2*mp.norm(suff[i])**2 for i in range(L))
    q=(P1*(A**n*a))[0]; r=(A**n*a)[2]
    assert abs(q)<mp.mpf('1e-88')
    p=a; normsum=mp.norm(p)**2
    for j in range(n):p=A*p;normsum+=mp.norm(p)**2
    exact=2*(q*q+eps*eps*r*r)*(1+normsum)
    assert abs(kernel-exact)<mp.mpf('1e-80')*max(abs(exact),mp.mpf('1e-100'))
    if eps:
        assert abs(kernel/(eps*eps)-2*r*r*(1+normsum))<mp.mpf('1e-80')
    assert mp.sqrt(m)*u<=12/L
    assert (new[-1]*pref[-1])[0]==0
    records.append(dict(n=n,L=L,mode=mode,phi=float(phi),root_residual=str(abs(q)),
        W_drift=float(mp.sqrt(m)*u),imbalance_drift=float(maxdrift),
        kernel=str(kernel),kernel_over_epsilon_squared=float(kernel/(eps*eps)) if eps else None,
        loss=0.5,initial_kernel=float(k**4*(L-2)+2*k*k),
        projector_original_min_singular=str(mp.sqrt(m)*eps)))
assert abs(records[3]['kernel_over_epsilon_squared']-25*float(mp.pi)**2/128)<0.05
result=dict(pass_check=True,scope='No Gaussian or actual-GD counterexample; exponentially conditioned projectors in exponential variant.',
    precision_digits=mp.mp.dps,kernel_over_epsilon_squared_limit=float(25*mp.pi**2/128),records=records)
(Path(__file__).resolve().parents[1]/'logs/tuned_averaged_kernel_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
