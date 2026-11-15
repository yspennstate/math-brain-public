from pathlib import Path
from datetime import datetime
from fractions import Fraction as F
import os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['MKL_NUM_THREADS']='1'
import sys,time,json,hashlib
import numpy as np
from scipy.sparse import coo_matrix,eye
H=Path(__file__).resolve().parent;d=int(sys.argv[1]);cap=int(sys.argv[2]);assert 3<=d<=35 and 2<=cap<=128
rp=H/f'T170_ROLLING_d{d}_C{cap}_RECEIPT.json';assert not rp.exists(),'Pilot already completed; read saved result'
began=time.monotonic();m=d-1;states=cap*cap
f=[0]*(cap+1)
for n in range(1,cap+1):f[n]=f[n-1]+(n-1).bit_count()
sigma=np.array([2*m*n-2*f[n] for n in range(cap+1)],dtype=np.int64);assert np.all(sigma[1:]>0)
aa=np.repeat(np.arange(1,cap+1,dtype=np.int64),cap);bb=np.tile(np.arange(1,cap+1,dtype=np.int64),cap);idx=np.arange(states,dtype=np.int64)
ra=np.where(aa<cap,sigma[aa],0);rb=np.where(bb<cap,sigma[bb]+np.maximum(aa-bb,0),0);rd=bb
ca=np.minimum(idx+cap,states-1);cb=np.minimum(idx+1,states-1);cd=(bb-1)*cap
total=ra+rb+rd;R=int(total.max())+1
row=np.concatenate([idx,idx,idx,idx]);col=np.concatenate([ca,cb,cd,idx]);data=np.concatenate([ra,rb,rd,-total]).astype(float)
L=coo_matrix((data,(row,col)),shape=(states,states)).tocsr();P=(eye(states,format='csr')+L/R).tocsr()
assert np.max(np.abs(np.asarray(P.sum(axis=1)).ravel()-1))<1e-14
pi=np.zeros(states);pi[-1]=1
stationary_iterations=0
for it in range(20000):
 new=P.T@pi;delta=float(np.abs(new-pi).sum());pi=new;stationary_iterations=it+1
 if delta<1e-13:break
 if time.monotonic()-began>20:break
assert abs(pi.sum()-1)<1e-10
a_guess=1/float(pi@rd)
cost=(1-a_guess*rd)/R;h=np.zeros(states);ref=states-1;bias_iterations=0
for it in range(30000):
 new=P@h+cost;new-=new[ref];change=float(np.max(np.abs(new-h)));h=new;bias_iterations=it+1
 if change<2e-15:break
 if time.monotonic()-began>55:break
scale=2**40;bias=[int(round(x*scale)) for x in h]
# The certificate is checked in unbounded integers, not numpy fixed widths.
best=F(-10**100);worst=None
for k in range(states):
 numerator=scale+int(ra[k])*(bias[int(ca[k])]-bias[k])+int(rb[k])*(bias[int(cb[k])]-bias[k])+int(rd[k])*(bias[int(cd[k])]-bias[k])
 ratio=F(numerator,scale*int(rd[k]))
 if ratio>best:best=ratio;worst=k
assert all(scale+int(ra[k])*(bias[int(ca[k])]-bias[k])+int(rb[k])*(bias[int(cb[k])]-bias[k])+int(rd[k])*(bias[int(cd[k])]-bias[k])-best*int(rd[k])*scale<=0 for k in range(states))
payload={'dimension':d,'cap':cap,'scale':scale,'bias':bias,'axis_upper_conditional':str(best),'state_order':'(a-1)*cap+(b-1), a,b=1..cap','sigma':'2*(d-1)*n-2*sum_{j<n}popcount(j)'}
bp=H/f'T170_ROLLING_d{d}_C{cap}_BIAS.json';bp.write_text(json.dumps(payload,separators=(',',':'))+'\n',encoding='utf-8')
floorfile=Path('~/brain_workers/w685/T170/logs/chord5_exact_certificates.json');floorrow=next(x for x in json.loads(floorfile.read_bytes())['rows'] if x['d']==d)['lower'];floor=F(int(floorrow['n']),int(floorrow['d']))
out={'at':datetime.now().astimezone().isoformat(),'status':'Exact finite-model bias inequalities PASS; physical rolling comparison is proposed and unaudited; no FPP admission','dimension':d,'cap':cap,'states':states,'seconds':time.monotonic()-began,'stationary_iterations':stationary_iterations,'stationary_l1_delta':delta,'bias_iterations':bias_iterations,'last_bias_change':change,'stationary_axis_estimate':a_guess,'conditional_axis_certificate':str(best),'conditional_axis_float':float(best),'diagonal_floor':str(floor),'conditional_margin':float(floor-best),'cap0_mass':float(pi[aa==cap].sum()),'cap1_mass':float(pi[bb==cap].sum()),'worst_state':[int(aa[worst]),int(bb[worst])],'bias_sha256':hashlib.sha256(bp.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite generator/reward control only; no proof of adaptive physical coupling or canonical regeneration supplied by this computation. No novelty assertion.'}
rp.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
