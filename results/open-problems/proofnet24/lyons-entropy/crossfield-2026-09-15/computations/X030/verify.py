"""Independent determinant check of the X030 two-block envelope Hessian.
The analytic proof is in agents/X030.md; these finite checks only verify algebra.
"""
import itertools, json, math
from pathlib import Path
import numpy as np


def basis():
    rows=[]; names=[]
    for i in range(4):
        a=np.zeros((4,4),complex); a[i,i]=1
        rows.append(a); names.append(f'd{i}')
    for i,j in itertools.combinations(range(4),2):
        for imag in (False,True):
            a=np.zeros((4,4),complex)
            a[i,j]=1j if imag else 1
            a[j,i]=a[i,j].conjugate()
            rows.append(a); names.append(f'{i}{j}'+('i' if imag else 'r'))
    return np.array(rows),names


def check(rho):
    bm,names=basis()
    h=np.array([[1,1],[1,-1]],float)/math.sqrt(2)
    u=np.zeros((4,4)); u[:2,:2]=h; u[2:,2:]=h
    dirs=np.array([u@a@u.T for a in bm])
    km=np.eye(4)/2
    km[0,2]=km[2,0]=math.sqrt(rho)/2
    k=u@km@u.T
    fs=np.zeros(9); df=np.zeros((9,16)); ddf=np.zeros((9,16,16))
    atoms=[]; atomscore=[]; dd_atoms=[]; formula_error=0
    for mask in range(16):
        ss=np.array([(mask>>i)&1 for i in range(4)])
        m=np.where(ss[None,:],k,np.eye(4)-k)
        p=np.linalg.det(m).real
        rr=np.array([np.linalg.solve(m,a*(2*ss-1)[None,:]) for a in dirs])
        tr=np.trace(rr,axis1=1,axis2=2)
        dp=(p*tr).real
        ddp=(p*(np.outer(tr,tr)-np.einsum('aij,bji->ab',rr,rr))).real
        r,s=int(ss[:2].sum()),int(ss[2:].sum()); cell=3*r+s
        fs[cell]+=p; df[cell]+=dp; ddf[cell]+=ddp
        atoms.append(p); atomscore.append(dp); dd_atoms.append(ddp)
        formula_error=max(formula_error,abs(p-(1-rho*(r-1)*(s-1))/16))
    weights=np.array([math.comb(2,r)*math.comb(2,s) for r in range(3) for s in range(3)])
    q=fs/weights
    neg_env=(df.T/fs)@df+np.einsum('a,aij->ij',np.log(q),ddf)
    atomscore=np.array(atomscore); atoms=np.array(atoms); dd_atoms=np.array(dd_atoms)
    neg_full=(atomscore.T/atoms)@atomscore+np.einsum('a,aij->ij',np.log(atoms),dd_atoms)
    fisher_loss=(atomscore.T/atoms)@atomscore-(df.T/fs)@df
    L=-math.log1p(-rho*rho); R=2*math.atanh(rho)
    def predicted(vec):
        d,s,e,t=vec[:4]; ta,tb=d+s,e+t
        pa,pb=ta-rho*t,tb-rho*s
        value=(pa*pa+pb*pb+2*rho*pa*pb)/(1-rho*rho)+(ta+rho*t)**2+(tb+rho*s)**2
        value+=L*(s*s+t*t+rho*s*t-ta*s-tb*t)-R*ta*tb
        for j,name in enumerate(names[4:],4):
            edge=name[:2]
            coeff=L if edge in ('01','23') else (R-rho*L if edge=='13' else R)
            if name=='02r': coeff+=4*rho/(1-rho*rho)
            value+=coeff*vec[j]**2
        return value
    eye=np.eye(16); pred=np.diag([predicted(e) for e in eye])
    for i,j in itertools.combinations(range(16),2):
        pred[i,j]=pred[j,i]=(predicted(eye[i]+eye[j])-pred[i,i]-pred[j,j])/2
    scalar=[]
    for x in (rho,-rho):
        a=2+x+x*x+x*L/2-math.atanh(x)
        b=-x*x-(1+x)*L/2
        c=x*x*(2-x)/(1-x)+(1+x/2)*L
        scalar.append({'x':x,'a':a,'b2_over_c':b*b/c,'eigmin':float(np.linalg.eigvalsh([[a,b],[b,c]])[0])})
    return {'rho':rho,'atom_formula_error':formula_error,
        'full_envelope_hessian_formula_error':float(np.max(np.abs(neg_env-pred))),
        'touching_hessian_identity_error':float(np.max(np.abs(neg_full-neg_env-fisher_loss))),
        'negative_envelope_hessian_eigmin':float(np.linalg.eigvalsh(neg_env)[0]),
        'negative_measured_hessian_eigmin':float(np.linalg.eigvalsh(neg_full)[0]),
        'fisher_loss_eigmin':float(np.linalg.eigvalsh(fisher_loss)[0]),'scalar':scalar}

if __name__=='__main__':
    out=[check(r) for r in (0.01,0.25,0.36,0.81,0.99)]
    print(json.dumps(out,indent=2))
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n')
    assert max(x['atom_formula_error'] for x in out)<1e-12
    assert max(x['full_envelope_hessian_formula_error'] for x in out)<1e-9
    assert max(x['touching_hessian_identity_error'] for x in out)<1e-9
    assert min(x['negative_envelope_hessian_eigmin'] for x in out)>0
