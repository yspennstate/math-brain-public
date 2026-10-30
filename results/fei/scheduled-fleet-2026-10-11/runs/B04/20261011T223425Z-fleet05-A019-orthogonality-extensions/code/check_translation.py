import json,time,hashlib
from fractions import Fraction as Q
from pathlib import Path
from collections import defaultdict
R=Path(__file__).resolve().parents[1]
spec={'helper_version':'A019-translation-v1','family':'F(w,y)=g(y+xor_j v_j AND(w_j)); all two-bit Boolean cores','domain':'n=2; one block k=1,2,3 and v=0..3; two blocks (1,1),(1,2),(2,2), v pairs 0..3; conjunction closed forms k=1..100; bent splices m=2,4,6,8','case_count':960,'symmetry':'none','arithmetic':'integer Walsh, Fraction, exact formal prime logarithms; rational atanh enclosures','memory_estimate_MB':40,'max_runtime_seconds':60}
# This frozen spec is written before any enumeration.
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2))
t0=time.monotonic(); checks=0; cases=0
def ck(x):
 global checks
 checks+=1
 assert x
def walsh(a):
 a=a[:]; h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h): a[i],a[i+h]=a[i]+a[i+h],a[i]-a[i+h]
  h*=2
 return [Q(x,len(a)) for x in a]
def lf(n):
 d={}; p=2
 while p*p<=n:
  while n%p==0: d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def ent(p):
 d=defaultdict(Q)
 for x in p:
  if x:
   for z,e in lf(x.denominator).items():d[z]+=x*e
   for z,e in lf(x.numerator).items():d[z]-=x*e
 return {z:v for z,v in d.items() if v}
def esum(terms):
 d=defaultdict(Q)
 for weight,e in terms:
  for z,v in e.items():d[z]+=weight*v
 return {z:v for z,v in d.items() if v}
def ln_interval(x):
 z=(x-1)/(x+1); s=Q(0)
 for i in range(80):s+=2*z**(2*i+1)/(2*i+1)
 err=2*z**161/(161*(1-z*z))
 return s,s+err
def hsmall(k):
 delta=Q(1,2**k); return ent([(1-2*delta)**2]+[4*delta*delta]*(2**k-1))
def test(g,ks,vs):
 global cases
 cases+=1; a=sum(ks); N=2**a; ng=4
 c=walsh(g); p=[x*x for x in c]
 rho=[sum(p[T] for T in range(4) if (T&v).bit_count()%2) for v in vs]
 table=[]
 for y in range(4):
  for w in range(N):
   shift=0;off=0
   for k,v in zip(ks,vs):
    if ((w>>off)&(2**k-1))==2**k-1:shift^=v
    off+=k
   table.append(g[y^shift])
 ff=walsh(table); pp=[x*x for x in ff]
 ck(sum(pp)==1)
 ck(ent(pp)==esum([(Q(1),ent(p))]+[(r,hsmall(k)) for r,k in zip(rho,ks)]))
 ck(sum(Q(i.bit_count())*p[i] for i in range(4))==sum(Q((i>>a).bit_count())*pp[i] for i in range(len(pp))))
 off=0
 for k,r in zip(ks,rho):
  for i in range(off,off+k):
   edge=Q(sum(table[x]!=table[x^(1<<i)] for x in range(len(table))),len(table))
   ck(edge==r*Q(2,2**k));ck(edge==sum(pp[x] for x in range(len(pp)) if (x>>i)&1))
  off+=k
 for T in range(4):ck(sum(pp[(T<<a)+A] for A in range(N))==p[T])
for mask in range(16):
 g=[1-2*((mask>>y)&1) for y in range(4)]
 for k in (1,2,3):
  for v in range(4):test(g,[k],[v])
 for ks in ((1,1),(1,2),(2,2)):
  for v in range(4):
   for u in range(4):test(g,list(ks),[v,u])
ln2lo,ln2hi=ln_interval(Q(2));ck(ln2lo>Q(1,2))
ck(3**9<2**16) # H(point-defect on 3 bits)>2: singleton increment exceeds 4 Inf.
bounds=[]
for k in range(1,101):
 d=Q(1,2**k); p0=(1-2*d)**2
 ck(p0+(2**k-1)*4*d*d==1)
 # H/(2 k d) <= (1-d)[4-(4-2/ln2)/k] <4.
 upper=(1-d)*(4-(4-2/ln2lo)/k)
 ck(upper<4)
 if k in (2,4,8,16,32,64,100):bounds.append({'k':k,'ratio_upper_rational':str(upper)})
guards=[]
for m in (2,4,6,8):
 b=[(-1)**sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(m//2)) for y in range(2**m)]
 c=walsh(b);bp=b[:];bp[0]*=-1;cp=walsh(bp);d=Q(1,2**m)
 ck(all(x*x==d for x in c));ck(any(x*x!=z*z for x,z in zip(c,cp)))
 ck(Q(sum(x!=z for x,z in zip(b,bp)),2**m)==d)
 for x in c:
  q=(x-d)**2+d*d;ck(q/(d*d)>=1/(2*d))
 guards.append({'m':m,'selector_disagreement':str(d),'B_over_I_lower':m-1,'common_magnitude_hypothesis':False})
out={'status':'PASS','cases':cases,'assertions':checks,'runtime_seconds':time.monotonic()-t0,'ratio_bounds':bounds,'bent_guard':guards,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'out/CHECK.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:out[k] for k in ('status','cases','assertions','runtime_seconds')}))
