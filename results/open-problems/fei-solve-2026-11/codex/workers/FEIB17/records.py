import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import itertools,math,json,numpy as np
from audit import calc,truth
from pathlib import Path
out={};best=(-1,None);maxerasure=(-1,None)
codes=np.array([int(s,16) for s in open('../FEIB11/npn5.txt')],dtype=np.uint64)
for a in range(0,len(codes),4096):
    cc=codes[a:a+4096];o=calc(truth(cc,5));live=o['Inf']>0;rat=np.min(np.where(live,o['D']/np.maximum(o['Inf'],1e-300),1e20),1);rat=np.where(o['I']>0,rat,-1);j=int(np.argmax(rat))
    if rat[j]>best[0]:best=(float(rat[j]),hex(int(cc[j])))
    rat=o['E'].sum(1)/np.maximum(o['I'],1e-300);j=int(np.argmax(rat))
    if rat[j]>maxerasure[0]:maxerasure=(float(rat[j]),hex(int(cc[j])))
out['npn5']=dict(representatives=len(codes),maximum_best_D_ratio=best,maximum_erasure_ratio=maxerasure)
n=18;x=np.arange(1<<n,dtype=np.uint32);core=x&511;val=np.zeros(len(x),dtype=bool)
for p in itertools.permutations(range(3)):
    mask=sum(1<<(3*r+p[r]) for r in range(3));val|=(core&mask)==mask
for e in range(9):
    r,c=divmod(e,3);cross=sum(1<<j for j in range(9) if j//3==r or j%3==c);site=(core==cross)|(core==(cross^(1<<e)));val|=site&(((x>>(9+e))&1)>0)
f=1-2*val.astype(float);o=calc(f[None,:]);out['PM_K33_plus_9_coins']=dict(n=n,mean=float(f.mean()),H=float(o['H'][0]),I=float(o['I'][0]),H_over_Iminus1=float(o['H'][0]/(o['I'][0]-1)))
n=14;x=np.arange(1<<n);bits=((x[:,None]>>np.arange(n))&1).reshape(-1,7,2);f=np.where(bits.all(2).any(1),-1.,1.);o=calc(f[None,:]);out['tribes2x7']=dict(best_D_ratio=float((o['D']/o['Inf']).min()),H=float(o['H'][0]),I=float(o['I'][0]))
out['address']=[]
for k in [1,2,3]:
    n=k+(1<<k);x=np.arange(1<<n);addr=x&((1<<k)-1);f=1.-2*((x>>(k+addr))&1);o=calc(f[None,:]);out['address'].append(dict(k=k,n=n,Psi=float(o['D'].sum()),expected_Psi=2*k,H=float(o['H'][0])))
Path('records.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
