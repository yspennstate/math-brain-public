"""Independent 4D algebra, no Gaussian or training experiment."""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=60
k=mp.sqrt(mp.mpf(5)/4)
def unit(j):
    v=mp.matrix(4,1); v[j]=1; return v
e=[unit(j) for j in range(4)]
E=lambda i,j:e[i]*e[j].T
I=mp.eye(4)
records=[]
for n in [8,32,128,512]:
    L=2*n+4; m=L; eps=mp.mpf(1)/n
    w=mp.tan(mp.pi/(2*n)); t=mp.sqrt(m)/n; u=w*w/t; rho=mp.sqrt(1+w*w)
    B=I+t*E(0,2); C=I+t*E(3,1)
    A=B-u*E(2,0); Z=C-u*E(1,3)
    P=I-(1-eps)*E(2,2); Q=I-(1-eps)*E(3,3)
    P1=P-u*E(0,2); Q1=Q-u*E(3,1)
    v=k*e[0]; b=k*e[1]
    a=v-u/k*e[2]; d=b-u/k*e[3]
    initial=[v]+[B]*n+[P,Q]+[C]*n+[b.T]
    changed=[a]+[A]*n+[P1,Q1]+[Z]*n+[d.T]
    drift=[]
    for i in range(L-1):
        old=initial[i+1].T*initial[i+1]-initial[i]*initial[i].T
        new=changed[i+1].T*changed[i+1]-changed[i]*changed[i].T
        D=m*(new-old)
        # Frobenius dominates op; test the sharper exact block spectral norm separately.
        eigs=mp.eigsy(D,eigvals_only=True)
        drift.append(max(abs(z) for z in eigs))
    maxdrift=max(drift)
    assert maxdrift<=m*(u*u+eps*u)+mp.mpf('1e-50')
    pref=[mp.eye(1)]
    for mat in changed[:-1]: pref.append(mat*pref[-1])
    suff=[None]*L; suff[-1]=mp.eye(1)
    for i in range(L-2,-1,-1): suff[i]=suff[i+1]*changed[i+1]
    kernel=sum(mp.norm(pref[i])**2*mp.norm(suff[i])**2 for i in range(L))
    output=mp.sqrt(m)*(changed[-1]*pref[-1])[0]
    assert output==0
    p_n=A**n*a
    q=-rho**n*(w/k-k*u*u/w); r=-rho**n*k*u/w
    assert mp.norm(P1*p_n-(q*e[0]+eps*r*e[2]))<mp.mpf('1e-48')
    h2=q*q+eps*eps*r*r
    p=a; normsum=mp.norm(p)**2
    for j in range(n):
        p=A*p; normsum+=mp.norm(p)**2
    formula=2*h2*(1+normsum)
    assert abs(kernel-formula)<mp.mpf('1e-45')
    assert mp.sqrt(m)*u<=12/L
    records.append(dict(n=n,L=L,original_W_drift=float(mp.sqrt(m)*u),
        imbalance_op_drift=float(maxdrift),endpoint_small_gram=float(h2),
        kernel=float(kernel),kernel_over_L=float(kernel/L),L_times_kernel=float(L*kernel),
        initial_kernel=float(k**4*(L-2)+2*k*k),output=float(output),
        projector_original_min_singular=float(mp.sqrt(m)*eps)))
result=dict(pass_check=True,scope='Deterministic invertible hidden initial matrices; not Gaussian or actual GD.',
    precision_digits=mp.mp.dps,limit_L_times_kernel=float(mp.pi**2/2),records=records)
(Path(__file__).resolve().parents[1]/'logs/averaged_kernel_witness_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
