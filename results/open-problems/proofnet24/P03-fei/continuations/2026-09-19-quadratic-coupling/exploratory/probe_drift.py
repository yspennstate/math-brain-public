"""Exploratory finite majority drift probe; floating entropy is not proof evidence."""
from pathlib import Path
import numpy as np, math, json, time

def fwht(a):
 a=a.copy();h=1
 while h<a.size:
  b=a.reshape(-1,2*h)
  x=b[:,:h].copy();y=b[:,h:].copy()
  b[:,:h]=x+y;b[:,h:]=x-y;h*=2
 return a

def rank_add(basis,v):
 while v:
  b=v.bit_length()-1
  if b not in basis: basis[b]=v;return True
  v^=basis[b]
 return False

def orbit_min(ac,n,k):
 N=1<<n
 choices=[]
 for a in range(k+1):
  for b in range(n-k+1):
   v=((1<<a)-1)|(((1<<b)-1)<<k)
   c=(N-abs(int(ac[v]))) # /2N
   choices.append((c,v))
   if 0<a<k:
    choices.extend((c,1|(1<<j)) for j in range(1,k))
   if 0<b<n-k:
    choices.extend((c,(1<<k)|(1<<j)) for j in range(k+1,n))
 choices.sort()
 basis={};vsum=0
 for c,v in choices:
  if rank_add(basis,v):vsum+=c
 return vsum/(2*N)

rows=[]
for n in range(3,20,2):
 st=time.time();N=1<<n
 f=np.fromiter((1 if x.bit_count()>n//2 else -1 for x in range(N)),dtype=np.int64)
 wh=fwht(f);p=wh.astype(float)**2/N**2;p=p[p>0];H=float(-sum(p*np.log2(p)))
 If=(n-1)*math.comb(n-1,(n-1)//2)/(2**(n-1))
 avIf=avH=0
 ks=[]
 for k in range(n+1):
  z=(1<<k)-1;g=f*f[np.arange(N)^z];wg=fwht(g);ac=fwht(wg**2)//N
  ii=orbit_min(ac,n,k)
  p=wg.astype(float)**2/N**2;p=p[p>0];hh=float(-sum(p*np.log2(p)))
  wt=math.comb(n,k)/N;avIf+=wt*ii;avH+=wt*hh
  ks.append((k,ii,hh))
 D=2*H-avH;drift=2*If-avIf
 row=dict(n=n,H=H,If=If,D=D,drift=drift,ratio=D/drift,k=ks,seconds=time.time()-st)
 rows.append(row);print({key:v for key,v in row.items() if key!='k'},flush=True)
 open(Path(__file__).with_name('drift_majority.json'),'w').write(json.dumps(rows,indent=2))
