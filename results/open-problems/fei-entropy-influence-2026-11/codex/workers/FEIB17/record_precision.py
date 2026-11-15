import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import itertools,json,decimal,numpy as np
from pathlib import Path
n=18;N=1<<n;x=np.arange(N,dtype=np.uint32);core=x&511;val=np.zeros(N,dtype=bool)
for p in itertools.permutations(range(3)):
    mask=sum(1<<(3*r+p[r]) for r in range(3));val|=(core&mask)==mask
for e in range(9):
    r,c=divmod(e,3);cross=sum(1<<j for j in range(9) if j//3==r or j%3==c);val|=((core==cross)|(core==(cross^(1<<e))))&(((x>>(9+e))&1)>0)
a=1-2*val.astype(np.int64);k=1
while k<N:
    v=a.reshape(-1,2,k);u=v[:,0,:].copy();w=v[:,1,:].copy();v[:,0,:]=u+w;v[:,1,:]=u-w;k*=2
assert sum(int(z)**2 for z in a)==N*N
values,counts=np.unique(abs(a),return_counts=True);den=N*N;Inum=sum(j.bit_count()*int(z)**2 for j,z in enumerate(a));decimal.getcontext().prec=80;D=decimal.Decimal;ln2=D(2).ln();H=D(0)
for r,c in zip(values,counts):
    if r:
        p=D(int(r)**2)/D(den);H-=D(int(c))*p*p.ln()/ln2
I=D(Inum)/D(den);ratio=H/(I-1);out=dict(n=n,integer_parseval_sum=den,influence_numerator=Inum,influence_denominator=den,H_bits_80digits=str(H),I=str(I),H_over_Iminus1_80digits=str(ratio),lower_bound_6p5218_margin=str(ratio-D('6.5218')),method='integer Walsh transform, grouping exact squared integer coefficients, Decimal logs at 80 digits; numeric verification, not interval arithmetic')
Path('record_precision.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
