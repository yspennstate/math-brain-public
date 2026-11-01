from pathlib import Path
import json
import numpy as np
import sympy as sp

def upsets(n):
    if n==0: return [0,1]
    prev=upsets(n-1); shift=1<<(n-1)
    return [a|(b<<shift) for a in prev for b in prev if a&~b==0]
report=[]
for n in range(2,5):
    count=0; maxmix=0; minavg=1e9; mingapdiff=1e9; exacttargets=0
    for mask in upsets(n):
        v=[x for x in range(1<<n) if mask>>x&1];m=len(v)
        if m<(1<<(n-1)):continue
        count+=1
        adj=np.array([[int((x^y).bit_count()==1) for y in v] for x in v],dtype=int)
        deg=adj.sum(axis=1);D=int(deg.sum())
        assert D==2*sum(n-x.bit_count() for x in v)
        assert 2*D>=n*m
        minavg=min(minavg,D/m)
        pi=deg/D;mu=np.ones(m)/m
        P=np.eye(m)/2+adj/(2*deg[:,None]);Q=adj/(2*n)+np.diag(1-deg/(2*n))
        assert np.max(abs(pi@P-pi))<1e-12
        assert np.max(abs(mu@Q-mu))<1e-12
        assert np.all(pi<=2*mu+1e-12)
        c=n*m/D
        EP=np.diag(pi)@(np.eye(m)-P);EQ=np.diag(mu)@(np.eye(m)-Q)
        assert np.max(abs(EP-c*EQ))<1e-12
        S=np.sqrt(pi[:,None])*P/np.sqrt(pi[None,:])
        gp=1-np.linalg.eigvalsh(S)[-2];gq=1-np.linalg.eigvalsh(Q)[-2]
        mingapdiff=min(mingapdiff,gp-gq)
        assert gp>=gq-1e-12
        M=np.eye(m);t=0
        while np.max(np.sum(abs(M-pi),axis=1)/2)>.25+1e-12:
            M=M@P;t+=1
            assert t<100
        maxmix=max(maxmix,t)
        if n<=3:
            for bmask in range(1,1<<m):
                if 4*sum(int(deg[i]) for i in range(m) if bmask>>i&1)<D:continue
                bcount=bmask.bit_count()
                assert 8*bcount>=m
                outside=[i for i in range(m) if not bmask>>i&1]
                if not outside:continue
                jump=sp.Matrix([[sp.Rational(int(adj[i,j]),int(deg[i])) for j in outside] for i in outside])
                hr=(sp.eye(len(outside))-jump).inv()*sp.ones(len(outside),1)
                # The killed-chain equations give hP=2 hR exactly and hQ>=hP.
                q=sp.Matrix([[sp.Rational(int(adj[i,j]),2*n)+(sp.Rational(1)-sp.Rational(int(deg[i]),2*n) if i==j else 0) for j in outside] for i in outside])
                hq=(sp.eye(len(outside))-q).inv()*sp.ones(len(outside),1)
                assert all(hq[k]>=2*hr[k] for k in range(len(outside)))
                exacttargets+=1
    report.append(dict(n=n,half_volume_upsets=count,max_P_mix=maxmix,min_average_degree=minavg,min_gap_difference=mingapdiff,exact_large_target_checks=exacttargets))
Path('independent_checks.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps(report,indent=2))

