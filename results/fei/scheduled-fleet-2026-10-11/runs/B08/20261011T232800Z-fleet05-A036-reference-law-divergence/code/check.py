"""Frozen six-case exact collision experiment; no floating-point signs."""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial
from pathlib import Path
import json,time,hashlib
START=time.perf_counter()
GRID=2**90
def round_iv(lo,hi):return F((lo*GRID).__floor__(),GRID),F((hi*GRID).__ceil__(),GRID)
def ln_series(x):
 t=(x-1)/(x+1); n=18
 s=sum((2*t**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
 return s,s+2*t**(2*n+1)/(F(2*n+1)*(1-t*t))
LN2=ln_series(F(2))
@lru_cache(None)
def log2(x):
 assert x>0
 k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 lo,hi=ln_series(x)
 return round_iv(F(k)+lo/LN2[1],F(k)+hi/LN2[0])
def atom(x):
 if not x:return F(0),F(0)
 lo,hi=log2(x);return -x*hi,-x*lo
def add(ivs):
 lo=hi=F(0)
 for a,b in ivs:lo+=a;hi+=b
 return lo,hi
def scale(iv,z):return iv[0]*z,iv[1]*z
def h(p):return add([atom(p),atom(1-p)])
def enc(iv):
 grid=10**15
 return {'lower':str(F((iv[0]*grid).__floor__(),grid)),'upper':str(F((iv[1]*grid).__ceil__(),grid)),'rounding':'outward rational grid 10^-15'}
def ratios(T,K,M,I):return {'payment_required':enc(((T[0]/4-K[1])/I,(T[1]/4-K[0])/I)), 'recovery_required':enc(((M[0]-T[1]/4)/I,(M[1]-T[0]/4)/I))}
def summary(name,q,H,groups,support_mass=F(1)):
 assert sum(mult for mult,v in groups)==2**len(q)
 assert all(F(0)<=v<=1 for mult,v in groups)
 Z=sum((mult*v for mult,v in groups),F(0));assert Z>=1
 L=add(scale(atom(v),mult) for mult,v in groups)
 T=scale(L,1/Z); R_H=add([T,log2(Z)])
 M=add(h(p) for p in q); I=sum(q,F(0));K=(M[0]-H[1],M[1]-H[0])
 Ks=tuple(-x for x in reversed(log2(support_mass)))
 Kshape=(K[0]-Ks[1],K[1]-Ks[0])
 assert T[1]/4-K[0]<8*I
 assert M[1]-T[0]/4<8*I
 if I<=F(1,16):
  loge=(1/LN2[1],1/LN2[0])
  residual=(T[0]/4-M[1]+(2+loge[0])*I,T[1]/4-M[0]+(2+loge[1])*I)
  error=9*I*M[0]+15*I*I
  assert -error<residual[0]<=residual[1]<error
 result={'name':name,'dimension':len(q),'marginals':[str(x) for x in q],'I':str(I),'M':enc(M),'H':enc(H),'TC':enc(K),'Q_support_mass':str(support_mass),'K_supp':enc(Ks),'K_shape':enc(Kshape),'Z':str(Z),'L':enc(L),'T':enc(T),'H_v_over_Z':enc(R_H),'v_groups':[{'multiplicity':mult,'v':str(v)} for mult,v in groups],**ratios(T,K,M,I)}
 return result, (T,K,M,I)
def fwht(truth):
 a=truth[:];step=1
 while step<len(a):
  for j in range(0,len(a),2*step):
   for i in range(j,j+step):a[i],a[i+step]=a[i]+a[i+step],a[i]-a[i+step]
  step*=2
 return [F(x,len(a)) for x in a]
def validate_spectrum(truth,q):
 aa=fwht(truth);P=[x*x for x in aa]
 assert sum(P)==1
 assert [sum((P[s] for s in range(len(P)) if s>>i&1),F(0)) for i in range(len(q))]==q
 return aa,P
def direct_collision(phase,q):
 n=len(q);size=2**n;out=[]
 for u in range(size):
  c=F(0);shift_factor=F(1)
  for i in range(n):
   if u>>i&1:shift_factor*=q[i]*(1-q[i])
  for s in range(size):
   term=F(phase[s]*phase[s^u])
   for i in range(n):
    if not(u>>i&1):term*=q[i] if s>>i&1 else 1-q[i]
   c+=term
  out.append(c*c*shift_factor)
 return out

def address(a):
 N=2**a;t=F(1,N);aa=4*t*(1-t);u=t*(1-t)**(N-1)
 groups=[(1,F(1)),(N-1,(1-N*u)**2)]
 for w in range(1,N+1):
  for has_zero in [0,1]:
   bad=w-has_zero
   if not(0<=bad<=N-1):continue
   mult=comb(N-1,bad)*N
   c=1-F(2,2**w)*(bad*(1-t)**(N-w)+(N-1-bad)*t*(1-t)**(N-w-1))
   if w==2 and not has_zero:c+=F(2,2**w)*(1-t)**(N-2)
   groups.append((mult,aa**w*c*c))
 q=[F(1,2)]*a+[t]*N
 H=(F(2*a),F(2*a));supp=(1-t)**(N-1)
 result,raw=summary('address_a'+str(a),q,H,groups,supp)
 result['conditioned_reference_T']='0 (actual Boolean Fourier amplitudes)'
 if a<=2:
  n=a+N;truth=[1 if not(x>>(a+(x&(N-1)))&1) else -1 for x in range(2**n)]
  coeff,P=validate_spectrum(truth,q)
  assert all(x in [F(0),F(1,N*N)] for x in P)
  phase=[1 if x>=0 else -1 for x in coeff]
  vv=direct_collision(phase,q)
  assert sorted(vv)==sorted(v for mult,v in groups for _ in range(mult))
 return result,raw

def scalar_table(q,rt,tt,u):
 val=F(0)
 for s in range(2):
  ss=s^u
  if rt!='F' and s!=int(rt):continue
  if tt!='F' and ss!=int(tt):continue
  val+=F(1) if u else (q if s else 1-q)
 return val
def pair_table(q,rt,tt,u):
 val=F(0)
 for s in range(4):
  ss=s^u
  if rt=='D' and s!=0:continue
  if tt=='D' and ss!=0:continue
  z=F(1)
  if rt=='Q' and s==3:z=-z
  if tt=='Q' and ss==3:z=-z
  for i in range(2):
   if not(u>>i&1):z*=q if s>>i&1 else 1-q
  val+=z
 return val
def b05(k):
 r=2*k;p=F(1,2**r);delta=F(1,2**k);root=F(1,2**(k//2));d=p*delta
 qd=p*(F(1,2)+delta);qc=p*(1-root+delta);qy=d
 q=[qd]*k+[qc]*r+[qy]
 comps=[(1,'Q','F','0'),(-2,'D','F','0'),(2,'D','0','0'),(1,'F','F','1')]
 hpair=k//2
 @lru_cache(None)
 def value(e0,e1,e2,l,y):
  c=F(0)
  for cr,dr,ar,yr in comps:
   for ct,dt,at,yt in comps:
    z=F(cr*ct)
    for u,count in [(0,e0),(1,e1),(3,e2)]:z*=pair_table(qd,dr,dt,u)**count
    z*=scalar_table(qc,ar,at,0)**(r-l)*scalar_table(qc,ar,at,1)**l
    z*=scalar_table(qy,yr,yt,y)
    c+=z
  sq=(qd*(1-qd))**(e1+2*e2)*(qc*(1-qc))**l*(qy*(1-qy))**y
  return c*c*sq
 groups=[]
 for e0 in range(hpair+1):
  for e1 in range(hpair-e0+1):
   e2=hpair-e0-e1
   dm=factorial(hpair)//(factorial(e0)*factorial(e1)*factorial(e2))*2**e1
   for l in range(r+1):
    for y in [0,1]:groups.append((dm*comb(r,l),value(e0,e1,e2,l,y)))
 pos=(2**k+2**(k//2))//2-1;neg=(2**k-2**(k//2))//2
 anchor=1+p*(root-1-delta)
 hp=[(1,anchor*anchor),(2**r-1,(p*(root-1-delta))**2),(pos*2**r,(p*(root-delta))**2),(neg*2**r,(p*(-root-delta))**2),(2**(k+r),d*d)]
 assert sum((mult*x for mult,x in hp),F(0))==1
 H=add(scale(atom(x),mult) for mult,x in hp)
 result,raw=summary('B05_k'+str(k),q,H,groups)
 result['spectral_classes']=[{'multiplicity':mult,'P':str(x)} for mult,x in hp]
 n=3*k+1
 truth=[]
 for x in range(2**n):
  data=x&((1<<k)-1);ctrl=(x>>k)&((1<<r)-1);sel=x>>(k+r)
  bend=(-1)**sum(((data>>(2*j))&1)*((data>>(2*j+1))&1) for j in range(k//2))
  truth.append(1 if ctrl else (-1 if sel and data==0 else bend))
 coeff,P=validate_spectrum(truth,q)
 assert all(x!=0 for x in coeff)
 assert sorted(P)==sorted(x for mult,x in hp for _ in range(mult))
 if k==2:
  vv=direct_collision([1 if x>0 else -1 for x in coeff],q)
  assert sorted(vv)==sorted(v for mult,v in groups for _ in range(mult))
 return result,raw

rows=[];raws=[]
for k in [2,4]:
 rr,raw=b05(k);rows.append(rr);raws.append(raw)
for a in [1,2,3,4]:
 rr,raw=address(a);rows.append(rr);raws.append(raw)
# Find the first certified failure of zero-price collision payment in the ordered addressing domain.
violations=[row['name'] for row,(T,K,M,I) in zip(rows,raws) if T[0]/4>K[1]]
assert violations==['address_a4']
assert raws[-1][0][0]/4-raws[-1][1][1]>F(77,100)
out={'helper_version':'A036-B05-addressing-collision-v2','cases':rows,'zero_price_payment_failures':violations,'all_assertions_passed':True,'runtime_seconds_diagnostic':time.perf_counter()-START,'arithmetic':'Exact Fraction with rigorous range-reduced atanh log bounds; outward rational-grid exports'}
path=Path('out/verification.json');path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'cases':len(rows),'all_assertions_passed':True,'zero_price_payment_failures':violations,'runtime_seconds_diagnostic':out['runtime_seconds_diagnostic'],'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}))
