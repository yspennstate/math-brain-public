"""Eliminate acyclic births between front advances; solve only a C-state chain."""
from pathlib import Path
from datetime import datetime
from fractions import Fraction as F
import os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['MKL_NUM_THREADS']='1'
import numpy as np
import json,hashlib,time,sys
H=Path(__file__).resolve().parent;d=int(sys.argv[1]);C=int(sys.argv[2]);assert 3<=d<=35 and 1<=C<=512
rp=H/f'T170_EMBEDDED_d{d}_C{C}_RECEIPT.json';assert not rp.exists(),'Read saved result'
t0=time.monotonic();f=[0]*(C+1)
for n in range(1,C+1):f[n]=f[n-1]+(n-1).bit_count()
sigma=[2*(d-1)*n-2*f[n] for n in range(C+1)]
K=np.zeros((C,C));T=np.zeros(C);prev=np.zeros((C,C));pt=np.zeros(C)
# Before the next front shift, both counts only increase. Downward induction
# computes its last-count distribution and holding time without any iteration.
for a in range(C,0,-1):
 cur=np.zeros((C,C));ct=np.zeros(C);ra=sigma[a] if a<C else 0
 for b in range(C,0,-1):
  rb=sigma[b]+max(a-b,0) if b<C else 0;total=ra+rb+b
  v=ra*prev[b-1]
  if b<C:v=v+rb*cur[b]
  v[b-1]+=b;cur[b-1]=v/total
  ct[b-1]=(1+ra*pt[b-1]+(rb*ct[b] if b<C else 0))/total
 K[a-1]=cur[0];T[a-1]=ct[0];prev=cur;pt=ct
assert np.max(abs(K.sum(axis=1)-1))<1e-12
M=K.T-np.eye(C);M[-1]=1;y=np.zeros(C);y[-1]=1
pi=np.linalg.solve(M,y);assert pi.min()>-1e-12 and max(abs(pi@K-pi))<1e-12
gain=float(pi@T)
bias_base=np.linalg.solve(np.eye(C)-K+np.ones((C,1))*pi[None,:],T-gain)
hs=np.zeros((C,C))
for a in range(C,0,-1):
 ra=sigma[a] if a<C else 0
 for b in range(C,0,-1):
  rb=sigma[b]+max(a-b,0) if b<C else 0;total=ra+rb+b
  hs[a-1,b-1]=(1+(ra*hs[a,b-1] if a<C else 0)+(rb*hs[a-1,b] if b<C else 0)+b*(bias_base[b-1]-gain))/total
residual=float(max(abs(hs[:,0]-bias_base)));assert residual<1e-10
scale=2**40;bias=[round(float(x)*scale) for x in hs.ravel()]
best=F(-10**100);worst=None
for a in range(1,C+1):
 for b in range(1,C+1):
  k=(a-1)*C+b-1;ra=sigma[a] if a<C else 0;rb=sigma[b]+max(a-b,0) if b<C else 0
  numerator=scale+(ra*(bias[k+C]-bias[k]) if a<C else 0)+(rb*(bias[k+1]-bias[k]) if b<C else 0)+b*(bias[(b-1)*C]-bias[k])
  q=F(numerator,scale*b)
  if q>best:best=q;worst=[a,b]
bp=H/f'T170_EMBEDDED_d{d}_C{C}_BIAS.json'
bp.write_text(json.dumps({'dimension':d,'cap':C,'scale':scale,'bias':bias,'axis_upper_conditional':str(best),'state_order':'(a-1)*cap+(b-1), a,b=1..cap'},separators=(',',':'))+'\n',encoding='utf-8')
floorrow=next(x for x in json.loads(Path('~/brain_workers/w685/T170/logs/chord5_exact_certificates.json').read_bytes())['rows'] if x['d']==d)['lower'];floor=F(int(floorrow['n']),int(floorrow['d']))
r={'at':datetime.now().astimezone().isoformat(),'status':'Finite rolling-model candidate ONLY; physical comparison unaudited','dimension':d,'cap':C,'states':C*C,'seconds':time.monotonic()-t0,'axis_estimate':gain,'axis_certificate':str(best),'axis_float':float(best),'margin':float(floor-best),'embedded_residual':residual,'embedded_mean_front_count':float(pi@np.arange(1,C+1)),'worst_state':worst,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'bias_sha256':hashlib.sha256(bp.read_bytes()).hexdigest()}
rp.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r))
