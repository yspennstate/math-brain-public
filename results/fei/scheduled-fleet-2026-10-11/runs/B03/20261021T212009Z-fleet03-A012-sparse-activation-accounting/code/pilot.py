import os,time,json
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
ROOT=Path(__file__).resolve().parents[1]
(ROOT/'out').mkdir(exist_ok=True)
t0=time.perf_counter()
W=np.array([[(-1)**((s&t).bit_count()%2) for s in range(8)] for t in range(8)])/8
def phi(a,b):
    v=a+b
    with np.errstate(divide='ignore',invalid='ignore'):
        return np.where(a>0,a*np.log2(v/a),0)+np.where(b>0,b*np.log2(v/b),0)
best={'ratio':0}
done=0
for mask in range(128):
    c=np.array([1-2*((mask>>s)&1) for s in range(8)])
    a=W@c;M=W[:,[0,1,2]]*c[[0,1,2]]
    def ratio(q):
        d=sum(q)/8
        if d<1e-12:return 2.
        b=M@q
        return (2*(d-sum(q*q)/8)+sum(phi((a-b)**2,b*b)))/d
    for start in [[.1,.1,.1],[.5,.1,.8],[.02,.8,.1],[.9,.9,.9]]:
        fit=minimize(lambda q:-ratio(q),start,method='SLSQP',bounds=[(0,1)]*3,options={'maxiter':70,'ftol':1e-10})
        r=ratio(fit.x)
        if r>best['ratio']:best={'ratio':float(r),'mask':mask,'q':fit.x.tolist()}
        done+=1
        if time.perf_counter()-t0>50:break
    if time.perf_counter()-t0>50:break
out={'status':'NUMERICAL_EVIDENCE_ONLY','done':done,'best':best,'seconds':time.perf_counter()-t0}
(ROOT/'out'/'PILOT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
