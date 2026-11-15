"""Repeated polynomial contractions; direct products resolve tiny kernels."""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=250
k=mp.sqrt(mp.mpf(5)/4)
def vec(j):
    z=mp.matrix(4,1);z[j]=1;return z
e=[vec(j) for j in range(4)]; E=lambda i,j:e[i]*e[j].T;I=mp.eye(4)
records=[]
for n in [8,16,32,64]:
    M=n;L=2*n+2*M+2;m=L;eps=mp.mpf(1)/n;t=mp.sqrt(m)/n
    def f(phi):
        w=mp.tan(phi/n);u=w*w/t
        return (k+u*u/k)*mp.cos(phi)+(k*u*u/w-w/k)*mp.sin(phi)
    assert f(mp.pi/4)>0 and f(mp.pi/2)<0
    phi=mp.findroot(f,(mp.pi/4,mp.pi/2),solver='bisect',tol=mp.mpf('1e-225'),maxsteps=850)
    w=mp.tan(phi/n);u=w*w/t;rho=mp.sqrt(1+w*w)
    B=I+t*E(0,2);C=I+t*E(3,1);A=B-u*E(2,0);Z=C-u*E(1,3)
    P=I-(1-eps)*E(2,2);Q=I-(1-eps)*E(3,3)
    P1=P-u*E(0,2);Q1=Q-u*E(3,1)
    a=k*e[0]-u/k*e[2];d=k*e[1]-u/k*e[3]
    old=[k*e[0]]+[B]*n+[P]*M+[Q]*M+[C]*n+[(k*e[1]).T]
    new=[a]+[A]*n+[P1]+[P]*(M-1)+[Q]*(M-1)+[Q1]+[Z]*n+[d.T]
    assert len(new)==L
    maxdrift=mp.mpf(0)
    # Check every imbalance; repeated identities have negligible cost in 4D.
    for i in range(L-1):
        D=m*((new[i+1].T*new[i+1]-new[i]*new[i].T)-
             (old[i+1].T*old[i+1]-old[i]*old[i].T))
        if mp.norm(D):
            maxdrift=max(maxdrift,max(abs(z) for z in mp.eigsy(D,eigvals_only=True)))
    assert maxdrift<=m*(u*u+eps*u)+mp.mpf('1e-200')
    pref=[mp.eye(1)]
    for mat in new[:-1]:pref.append(mat*pref[-1])
    suff=[None]*L;suff[-1]=mp.eye(1)
    for i in range(L-2,-1,-1):suff[i]=suff[i+1]*new[i+1]
    kernel=sum(mp.norm(pref[i])**2*mp.norm(suff[i])**2 for i in range(L))
    pn=A**n*a;r=pn[2];q=(P1*pn)[0]
    assert abs(q)<mp.mpf('1e-215')
    p=a;normsum=mp.norm(p)**2
    for j in range(n):p=A*p;normsum+=mp.norm(p)**2
    formula=2*eps**(2*M)*r*r*(1+normsum+r*r*sum(eps**(2*j) for j in range(1,M)))
    assert abs(kernel/formula-1)<mp.mpf('1e-100')
    assert mp.sqrt(m)*u<=20/L
    assert (new[-1]*pref[-1])[0]==0
    records.append(dict(n=n,L=L,kernel=str(kernel),kernel_over_n_to_minus_2n=float(kernel/eps**(2*n)),
        log_kernel=float(mp.log(kernel)),W_drift=float(mp.sqrt(m)*u),
        imbalance_drift=float(maxdrift),min_initial_hidden_original_singular=float(mp.sqrt(m)/n),
        root_residual=str(abs(q))))
result=dict(pass_check=True,precision_digits=250,scope='Deterministic neighborhood obstruction only, not Gaussian or actual GD.',
    limit_kernel_over_n_to_minus_2n=float(25*mp.pi**2/256),records=records)
(Path(__file__).resolve().parents[1]/'logs/repeated_contraction_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
