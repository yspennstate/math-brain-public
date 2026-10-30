from pathlib import Path
from fractions import Fraction as F
from math import comb
import time,json
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x
 checks+=1
def chi(s,x):return 1-2*((s&x).bit_count()%2)
def direct(a):return [sum(a[x]*chi(s,x) for x in range(len(a))) for s in range(len(a))]
def fw(a):
 a=a[:];k=1
 while k<len(a):
  for p in range(0,len(a),2*k):
   for j in range(k):
    x,y=a[p+j],a[p+j+k];a[p+j],a[p+j+k]=x+y,x-y
  k*=2
 return a
def rank(rows):
 basis={}
 for x in rows:
  while x:
   k=x.bit_length()-1
   if k in basis:x^=basis[k]
   else:basis[k]=x;break
 return len(basis)
def quadratic(m,mask):
 mon=[0]+[1<<i for i in range(m)]+[(1<<i)|(1<<j) for i in range(m) for j in range(i+1,m)]
 return [1-2*(sum((mask>>j)&1 for j,s in enumerate(mon) if x&s==s)%2) for x in range(1<<m)]
phases=0
for m in range(4):
 for mask in range(1<<(1+m+m*(m-1)//2)):
  a=quadratic(m,mask);W=direct(a);N=1<<m;phases+=1
  vals=[(1-x)//2 for x in a]
  rows=[sum(((vals[0]^vals[1<<i]^vals[1<<j]^vals[(1<<i)^(1<<j)])<<j) for j in range(m)) for i in range(m)]
  r=rank(rows);support=[s for s,w in enumerate(W) if w]
  ck(len(support)==1<<r);ck(all(F(W[s]*W[s],N*N)==F(1,1<<r) for s in support))
  I=sum(F(s.bit_count()*w*w,N*N) for s,w in enumerate(W));ck(r<=2*I)
  t=support[0];linear=[s^t for s in support];ck(all(x^y in linear for x in linear for y in linear))
lifts=0
controls=[quadratic(2,k) for k in range(16)]
for base in range(16):
 h=[1-2*((base>>x)&1) for x in range(4)];H=direct(h)
 for a in controls:
  for b in controls:
   values=[h[x^((a[z]<0)+2*(b[z]<0))] for z in range(4) for x in range(4)]
   W=fw(values);lifts+=1
   for s in range(4):
    packet=[(a[z] if s&1 else 1)*(b[z] if s&2 else 1) for z in range(4)];A=direct(packet)
    for t in range(4):ck(W[s+4*t]==H[s]*A[t])
   ix=sum(F((s&3).bit_count()*w*w,256) for s,w in enumerate(W));ck(ix==sum(F(s.bit_count()*w*w,16) for s,w in enumerate(H)))
   if time.perf_counter()-start>60:raise RuntimeError('frozen runtime exceeded')
q=5;N=1<<(2*q);values=[]
for u in range(N):
 x=u&31;z=u>>5
 y=x
 for i in range(q):
  if (z>>i)&1 and (z>>((i+1)%q))&1:y^=1<<i
 values.append(1 if y.bit_count()<3 else -1)
influences=[F(sum(values[x]!=values[x^(1<<i)] for x in range(N)),N) for i in range(10)]
c=F(comb(q-1,(q-1)//2),1<<(q-1));ck(all(t==c for t in influences[:5]));ck(all(t==3*c/4 for t in influences[5:]))
W=fw(values);H=direct([1 if x.bit_count()<3 else -1 for x in range(32)])
for s in range(32):
 control=[]
 for z in range(32):
  exponent=sum(((z>>i)&1)*((z>>((i+1)%q))&1) for i in range(q) if s&(1<<i))%2
  control.append(1-2*exponent)
 A=direct(control)
 for t in range(32):ck(W[s+32*t]==H[s]*A[t])
out={'status':'PASS','assertions':checks,'seconds':time.perf_counter()-start,'quadratic_phases':phases,'two_data_lifts':lifts,'cyclic_q':q,'cyclic_data_influence':str(sum(influences[:5])),'cyclic_control_influence':str(sum(influences[5:]))}
(ROOT/'out/A068_VALIDATION.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
