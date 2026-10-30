from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import comb
import json,time,sys,hashlib
R=Path(__file__).resolve().parents[1]; START=time.perf_counter();N=0
D=1<<90;CACHE={}
def ck(x,msg):
 global N
 assert x,msg
 N+=1
 assert time.perf_counter()-START<60,'frozen runtime exceeded'
def rnd(x,up=False):return F(-((-x*D).__floor__()) if up else (x*D).__floor__(),D)
def mul(a,b):return rnd(a[0]*b[0]),rnd(a[1]*b[1],True)
def lnunit(x):
 z=(x-1)/(x+1);z=(rnd(z),rnd(z,True));z2=mul(z,z);v=z;s=(F(0),F(0))
 for j in range(40):
  s=s[0]+2*v[0]/(2*j+1),s[1]+2*v[1]/(2*j+1)
  v=mul(v,z2)
 tail=2*z[1]**81/(81*(1-z[1]**2))
 return s[0],s[1]+tail
LN2=lnunit(F(2))
def log(x):
 if x in CACHE:return CACHE[x]
 orig=x; e=x.numerator.bit_length()-x.denominator.bit_length()
 x=x/(F(2)**e)
 if x<1:x*=2;e-=1
 if x>=2:x/=2;e+=1
 a,b=lnunit(x)
 CACHE[orig]=rnd(e+a/LN2[1]),rnd(e+b/LN2[0],True)
 return CACHE[orig]
def add(*xs):return sum((x[0] for x in xs),F(0)),sum((x[1] for x in xs),F(0))
def scale(a,w):return (a[0]*w,a[1]*w) if w>=0 else (a[1]*w,a[0]*w)
def sub(a,b):return add(a,scale(b,-1))
def val(x):return F(x),F(x)
def eta(x):return scale(log(x),-x) if x else val(0)
def cehist(rows):
 groups=defaultdict(F)
 ck(sum(n*p for n,p,q in rows)==1,'true normalization')
 ck(sum(n*q for n,p,q in rows)==1,'reference normalization')
 for n,p,q in rows:
  ck(n>=0 and p>=0 and q>=0 and (not p or q>0),'support')
  if p:groups[q]-=n*p
 return add(*(scale(log(q),w) for q,w in groups.items()))
def fullcost(rows):
 # Gate reference uniform. True data marginal exactly (P_core*P_s+point0)/2.
 data=[]
 for n,p,q,is0 in rows:
  for multiplicity,mask0 in [(1,True),(3,False)]:
   data.append((n*multiplicity,(p/4+int(is0 and mask0))/2,(q/4+int(is0 and mask0))/2))
 return add(val(1),cehist(data))
def K(t):return sub(val(1),scale(log((1+t)/t),t)) if t else val(1)
def Lq(p):return add(scale(log((9+p*p)/8),F(1,2)),scale(log((9+p*p)/(1+p*p)),p*p/8))
def conversion(p):
 a=p/2;t=(1+a)**2/(2*(1+a*a))
 return scale(add(scale(log(2*t),t),scale(log(2*(1-t)),1-t)),(1+a*a)/2)
def terminals(p):
 cp=add(val(5),scale(log((9+p)*(1-p)),F(-1,2)))
 cc=add(val(5),scale(log(9+p),F(-5,8)),scale(log(1+p),F(-3,8)))
 end=add(scale(cp,1-p),scale(cc,p))
 deficit=(max(F(0),p*(cc[0]-3)/2),max(F(0),p*(cc[1]-3)/2))
 return end,deficit

def rows(k,r,s,ghost=False):
 rho=F(1,1<<k);mu=F(3,4)**(r+1);nu=F(3,4)*F(1,2)**s
 p=rho*(1-mu)/2;a=rho*(1-nu)/2;data=[]
 d=F(5,8)**r if ghost else F(1)
 for j in range(s+1):
  multiplicity=comb(s,j)*3**j
  for live0,nlive,liveprob in [(True,1,F(9,16)),(False,7,F(1,16))]:
   g0=live0 and j==0
   actual=F(1,4)**s*liveprob
   reference=F(5,8)**(s-j)*F(1,8)**j*liveprob*d
   for pad0,npad in [(True,1),(False,(1<<k)-1)]:
    for u in [0,1]:
     at_u=bool(u and pad0 and g0);at0=bool(not u and pad0 and g0)
     pp=rho*rho*(actual+(1-2*nu)*int(g0))/4+(1-2*a)*int(at_u)
     qq=rho*rho*(reference+(1-2*mu)*int(g0))/8+(1-2*p)*int(at_u)/2+F(int(at0),2)
     if s:
      pseudo=rho*rho*(reference+(1-2*nu)*int(g0))/4+(1-2*a)*int(at_u)
      ck(qq>=pseudo/8,'all atom domination, including merged principal atom')
     data.append((multiplicity*nlive*npad,pp,qq,at0))
 missing=1-sum(n*q for n,p,q,is0 in data)
 ck(missing>=0,'ambient reference slice')
 if missing:data.append((1,F(0),missing,False))
 return data,p,a

def profile(k,r,s,ghost=False):
 rr,p,a=rows(k,r,s,ghost);cost=fullcost(rr);U=add(Lq(p),conversion(p));ck(U[1]<F(5,8),'same original U')
 ig=F(s)+F(3,4);res=[]
 for sign in [-1,1]:
  influence4=6+2*(k-1)*a+F(1,1<<k)*ig+sign*a
  z=sub(sub(val(influence4),cost),U);res.append(z)
  if not ghost and k>=5:ck(z[0]> (F(5,4) if s==0 else F(3,4)),'complete cleaned profile after SAME U')
 if ghost and k==5 and r==4096:ck(all(z[1]<F(-241,256) for z in res),'independent exact A020 rare witness')
 return cost,res

def walsh(values):
 a=values[:];n=len(a);h=1
 while h<n:
  for i in range(0,n,2*h):
   for j in range(i,i+h):x,y=a[j],a[j+h];a[j]=x+y;a[j+h]=x-y
  h*=2
 return {i:F(v*v,n*n) for i,v in enumerate(a) if v}

def project(P,remain):
 q=defaultdict(F)
 for t,v in P.items():q[sum(((t>>b)&1)<<j for j,b in enumerate(remain))]+=v
 return {t:v for t,v in q.items() if v}

def literal(r):
 k=1;m=r+1;n=3+3*m;size=1<<n
 def fun(x):
  G=1
  for b in range(m):G*= -1 if ((x>>(3+3*b))&7)==0 else 1
  active=((x>>2)&1)==0 and G==-1
  return -1 if (x>>(0 if active else 1))&1 else 1
 truth=[fun(x) for x in range(size)];P=walsh(truth);Q={t:v/2 for t,v in P.items()};Q[1]=Q.get(1,F(0))+F(1,2)
 for outcomes in range(1<<r):
  s=r-outcomes.bit_count();fixed={3+3*b:(outcomes>>b)&1 for b in range(r)}
  ghostbits=[3+3*b+j for b in range(r) if (outcomes>>b)&1 for j in [1,2]]
  for x in range(size):
   if all(((x>>b)&1)==v for b,v in fixed.items()):
    ck(all(truth[x]==truth[x^(1<<b)] for b in ghostbits),'physical zero influence of cleanup coordinates')
  for qval in [0,1]:
   assignments={**fixed,0:qval,**{b:0 for b in ghostbits}};remain=[b for b in range(n) if b not in assignments]
   vals=[]
   for x in range(1<<len(remain)):
    full=sum(v<<b for b,v in assignments.items())+sum(((x>>j)&1)<<b for j,b in enumerate(remain));vals.append(truth[full])
   actual=walsh(vals);inherited=project(Q,remain)
   rr,p,a=rows(k,r,s);observed=defaultdict(int)
   for t in range(1<<len(remain)):observed[(actual.get(t,F(0)),inherited.get(t,F(0)),t==0)]+=1
   expected=defaultdict(int)
   for count,pp,qq,empty in rr:expected[(pp,qq,empty)]+=count
   ck(observed==expected,'literal physical spectrum/reference equals independent compressed rows')
   I=sum(F(t.bit_count())*v for t,v in actual.items());rho=F(1,2)
   # qval0 gives +1 and qval1 gives -1; core influence follows via exact physical edges.
   edges=sum(vals[x]!=vals[x^(1<<j)] for x in range(len(vals)) for j in range(len(remain)))
   ck(I==F(edges,len(vals)),'Walsh/physical influence identity')
   # The masked, gated function has I_F=1/2+I_core/2+(1-qsign*a)/4.
   sign=1 if qval==0 else -1
   iff=F(1)+I/2-sign*a/4
   target=F(3,2)+(k-1)*a/2+rho*(F(s)+F(3,4))/4-sign*a/4
   ck(iff==target,'complete full influence, both q signs')
 return {'r':r,'dimension':n,'original_atoms':len(P),'physical_histories':2**(r+1)}

def pack(z):return [str(rnd(z[0])),str(rnd(z[1],True))]
if __name__=='__main__':
 pilot='--pilot' in sys.argv
 cases=[]
 for r in ([3] if pilot else [3,4,16,64,256,4096]):
  ss=[0,1,2,r if r<=64 else 16]
  for s in ss:
   C,z=profile(5,r,s);cases.append({'r':r,'s':s,'cost_interval':pack(C),'reserves':list(map(pack,z))})
  if not pilot or r==3:
   C,z=profile(5,r,0,True);cases.append({'r':r,'s':0,'before_cleanup':True,'cost_interval':pack(C),'reserves':list(map(pack,z))})
  ck(sum(comb(r,s) for s in range(r+1))==2**r,'all outcome class reaches retained')
 # Independent seed Walsh, erasure and actual restriction identities.
 seed=[-1]+[1]*7;P=walsh(seed);proj=project(P,[1,2]);ck(proj=={0:F(5,8),1:F(1,8),2:F(1,8),3:F(1,8)},'critical 5/8 ghost factor')
 ck(walsh(seed[:1]+seed[2:3]+seed[4:5]+seed[6:7])=={i:F(1,4) for i in range(4)},'outcome0 gives actual g2 uniform spectrum')
 ck(walsh(seed[1::2])=={0:F(1)},'outcome1 is actually constant')
 ck(F(7,64)*F(1,32)*4096*F(1,2)==7,'selected full rows mass7rho/64, log penalty>r/2')
 ck(F(8,5)**2>2 and 31**31>2**152,'integer witnesses for no-go and entropy bound')
 c2=add(scale(log(F(8,5)),F(1,4)),val(F(9,4)));ck(c2[1]<F(5,2),'nonconstant residual seed cross entropy <5/2')
 H0=add(val(4),scale(log(F(3)),F(-9,8)));ck(H0[1]<3,'unqueried seed H0<3')
 literals=[literal(1)] if pilot else [literal(1),literal(2)]
 result={'status':'PASS','assertions':N,'runtime_seconds':time.perf_counter()-START,'profiles':cases,'literal_cases':literals,'arithmetic':'Fraction;90-bit dyadic outward logs;40-term atanh tail; integer Walsh','scope':'analytic all-k>=5,r>=3 cleanup-closed outcome theorem; exact frozen cases and independent A020 review','FEI':'OPEN'}
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'status':'PASS','assertions':N,'runtime_seconds':result['runtime_seconds'],'profiles':len(cases),'literal_cases':len(literals)}))
