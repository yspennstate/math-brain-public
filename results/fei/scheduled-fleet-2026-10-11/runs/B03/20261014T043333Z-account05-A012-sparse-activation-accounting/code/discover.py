from pathlib import Path
import numpy as np
from scipy.optimize import minimize
import json,time
root=Path(__file__).resolve().parents[1];start=time.perf_counter();rng=np.random.default_rng(1205)
W=np.array([[(-1)**((s&t).bit_count()) for s in range(8)] for t in range(8)])/8
def terms(x):
    u,v=x[:8],x[8:];a,b=W@u,W@v;d=(1-np.mean(u*v))/2
    A=(a+b)**2/4;E=(a-b)**2/4;m=A+E
    q=np.divide(E,m,out=np.zeros(8),where=m>0)
    h=np.zeros(8);pos=(q>0)&(q<1);h[pos]=-q[pos]*np.log2(q[pos])-(1-q[pos])*np.log2(1-q[pos])
    Bout=(2-np.mean(u*u)-np.mean(v*v))/2
    return d,Bout+np.dot(m,h)
def objective(x):
    d,B=terms(x);return -B/max(d,1e-9)
cons=[{'type':'ineq','fun':lambda x:terms(x)[0]-1/32},{'type':'ineq','fun':lambda x:1/6-terms(x)[0]}]
candidates=[];best=None
for i in range(64):
    if time.perf_counter()-start>50:break
    c=rng.choice([-1.,1.],8);u=c.copy();v=c.copy()
    if i%3==0:v[rng.integers(8)]=rng.uniform(-1,1)
    elif i%3==1:
        chosen=rng.choice(8,2,replace=False);u[chosen[0]]*=rng.uniform(0.1,1);v[chosen[1]]*=rng.uniform(0.1,1)
    else:u=c*rng.uniform(.8,1,8);v=c*rng.uniform(.8,1,8)
    fit=minimize(objective,np.r_[u,v],method='SLSQP',bounds=[(-1,1)]*16,constraints=cons,options={'maxiter':200,'ftol':1e-11})
    k=np.rint((fit.x+1)*128).astype(int);q=-1+k/128;d,B=terms(q)
    row={'start':i,'success':bool(fit.success),'message':str(fit.message),'continuous_d':terms(fit.x)[0],'continuous_ratio':-float(fit.fun),'u_counts':k[:8].tolist(),'v_counts':k[8:].tolist(),'rounded_d':d,'rounded_B':B,'rounded_ratio':B/d if d else 0}
    candidates.append(row)
    if best is None or row['rounded_ratio']>best['rounded_ratio']:best=row
    (root/'out/DISCOVERY_PARTIAL.json').write_text(json.dumps({'status':'FLOAT_EVIDENCE_ONLY','best':best,'completed_starts':len(candidates),'candidates':candidates},indent=2)+'\n',encoding='utf-8')
assert time.perf_counter()-start<55
(root/'out/DISCOVERY_RESULTS.json').write_text(json.dumps({'status':'FLOAT_EVIDENCE_ONLY','completed_starts':len(candidates),'elapsed_seconds':time.perf_counter()-start,'best':best,'candidates':candidates},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'completed_starts':len(candidates),'best':best,'elapsed_seconds':time.perf_counter()-start}))
