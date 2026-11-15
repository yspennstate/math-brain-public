import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json,math,time
import numpy as np
from scipy.optimize import linprog
from scipy.stats import binom
from audit import truth,wht
from pathlib import Path
# Fixed candidate before census: F_A <= c rho_A + k I(g) + l Var(g).
# Multiplying by mean^2 avoids division. Fit c+2k+2l, the integrated budget.
# Cutting planes retain worst violated constraints; this is an LP exploration, not a proof.
source=Path('../FEIB11/npn5.txt');codes=np.array([int(s.strip(),16) for s in source.open() if s.strip()],dtype=np.uint64)
rows=[];count=0;start=time.time();cuts=[];theta=np.array([0.,0.,0.]);N=32
masks=np.array([[(j>>i)&1 for i in range(5)] for j in range(32)],float)
# NPN quotient suffices: input negations only alter coefficient signs, permutations permute A.
def scan(theta,collect=False):
    worst=(-1,None);maxrat=0.;nonzero=0
    for a in range(0,len(codes),4096):
        cc=codes[a:a+4096];c=wht(truth(cc,5));mu=c*c;b=mu[:,0];coeff=mu[:,[1,2,4,8]] if False else mu[:,[1,2,4,8,16]]
        I=(mu*np.array([i.bit_count() for i in range(32)])).sum(1);V=1-b
        z=coeff*np.log2(1+b[:,None]/np.maximum(coeff,1e-300));valid=b>0
        for mask in masks:
            x1=(coeff*mask).sum(1);y=(z*mask).sum(1);x2=b*I;x3=b*V
            violation=y-theta[0]*x1-theta[1]*x2-theta[2]*x3
            violation=np.where(valid,violation,-1);j=int(np.argmax(violation))
            if violation[j]>worst[0]:worst=(float(violation[j]),dict(code=hex(int(cc[j])),mask=mask.tolist(),x=[float(x1[j]),float(x2[j]),float(x3[j])],y=float(y[j])))
            if collect and violation[j]>1e-10:cuts.append([float(x1[j]),float(x2[j]),float(x3[j]),float(y[j])])
    return worst
history=[]
for step in range(16):
    worst=scan(theta,True);history.append(dict(step=step,theta=theta.tolist(),worst=worst));print(history[-1],flush=True)
    if worst[0]<1e-9:break
    ar=np.array(cuts);res=linprog([1,2,2],A_ub=-ar[:,:3],b_ub=-ar[:,3],bounds=[(0,None)]*3,method='highs',options={'threads':1});assert res.success
    theta=res.x
out=dict(scope='all five-variable NPN representatives, every coordinate subset A; no proof beyond dimension 5',representatives=len(codes),source_sha256=__import__('hashlib').sha256(source.read_bytes()).hexdigest(),theta=theta.tolist(),objective=float(theta@[1,2,2]),history=history,elapsed_seconds=time.time()-start)
# External family, kept out of the LP: monotone thresholds t=n/2+round(n^(1/4)).
family=[]
for n in [256,1024,4096,16384,65536,262144,1048576,4194304,16777216]:
    t=n//2+round(n**.25);mean=1-2*binom.sf(t-1,n,.5);alpha=binom.pmf(t-1,n-1,.5);I=n*alpha;rho=n*(alpha/mean)**2;F=rho*math.log2(1+(mean/alpha)**2);V=1-mean*mean
    rhs=theta[0]*rho+theta[1]*I+theta[2]*V
    family.append(dict(n=n,t=t,mean=float(mean),single_influence=float(alpha),I=float(I),rho_sum=float(rho),F=float(F),F_over_I_rho_V=float(F/(I+rho+V)),lp_rhs=float(rhs),violation=float(F-rhs)))
out['threshold_holdout']=family
Path('vertex_lp.json').write_text(json.dumps(out,indent=2));print('DONE',json.dumps(out,indent=2),flush=True)
