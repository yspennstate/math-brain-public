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

def make_rows(k,m,n1,n2,n3,phase,padding=0):
 rho=F(1,1<<k);rhoc=rho*2**padding;kp=k-padding;mu=F(3,4)**m
 nu=F(0) if n1 else phase*F(1,2)**n2*F(3,4)**n3
 a=rhoc*(1-nu)/2;p=rho*(1-mu)/2;rr=[];seed=[]
 for j1 in range(n1+1):
  for j2 in range(n2+1):
   for j3 in range(n3+1):
    count=comb(n1,j1)*comb(n2,j2)*3**j2*comb(n3,j3)*7**j3
    empty=j1+j2+j3==0
    pg=F(int(j1==n1),4**n2)*F(9,16)**(n3-j3)*F(1,16)**j3
    rg=F(3,4)**(n1-j1)*F(1,4)**j1*F(5,8)**(n2-j2)*F(1,8)**j2*F(9,16)**(n3-j3)*F(1,16)**j3
    seed.append((count,pg,rg))
    for pad0,npad in [(True,1),(False,(1<<kp)-1)]:
     if not npad:continue
     for u in [0,1]:
      at_u=bool(u and pad0 and empty);at0=bool(not u and pad0 and empty)
      pp=rhoc*rhoc*(pg+(1-2*nu)*int(empty))/4+(1-2*a)*int(at_u)
      qq=rho*rhoc*(rg+(1-2*mu)*int(empty))/8+(1-2*p)*int(at_u)/2+F(int(at0),2)
      ck(pp>=0 and qq>=0,'actual normalized overlapping-row coefficients')
      if not padding and m>=4 and nu<=F(1,2):
       M=rho*rho*(rg+(1-2*nu)*int(empty))/4+(1-2*a)*int(at_u)
       ck(qq>=M/8,'A020 combined vacuum domination, not termwise negative-mean bound')
      rr.append((count*npad,pp,qq,at0))
 return rr,seed,nu,a,p

def review(k,m,n1,n2,n3,phase):
 rr,seed,nu,a,p=make_rows(k,m,n1,n2,n3,phase);C=fullcost(rr)
 ig=F(n1+n2)+F(3*n3,4);seedC=cehist(seed);R0=F(3,4)**n1*F(5,8)**n2*F(9,16)**n3
 ck(R0>=nu*nu,'original projected vacuum >=actual mean squared, all phases')
 ck(seedC[1]<=4*ig if ig else seedC==val(0),'complete supplied seed cross-entropy paid')
 dv=3*R0+3-8*F(3,4)**m+2*nu
 if nu<=F(1,2):ck(dv>=F(13,96),'combined vacuum envelope including negative mean')
 U=add(Lq(p),conversion(p));ck(U[0]>=0 and U[1]<F(5,8),'same actual old debit')
 reserves=[]
 for sign in [-1,1]:
  fourI=6+2*(k-1)*a+F(1,1<<k)*ig+sign*a
  z=sub(sub(val(fourI),C),U);ck(z[0]>F(5,8),'A020 all cleaned profiles, both q signs');reserves.append(z)
 return {'k':k,'m':m,'counts':[n1,n2,n3],'phase':phase,'nu':str(nu),'D_vac':str(dv),'reserves':list(map(pack,reserves))}

def walsh(values):
 a=values[:];h=1;n=len(a)
 while h<n:
  for i in range(0,n,2*h):
   for j in range(i,i+h):x,y=a[j],a[j+h];a[j]=x+y;a[j+h]=x-y
  h*=2
 return {i:F(x*x,n*n) for i,x in enumerate(a) if x}

def project(P,remain):
 q=defaultdict(F)
 for t,v in P.items():q[sum(((t>>b)&1)<<j for j,b in enumerate(remain))]+=v
 return {t:v for t,v in q.items() if v}

def literal(pilot=False):
 from itertools import product
 k=1;m=2;n=2+k+3*m
 def fn(x):
  G=1
  for b in range(m):G*= -1 if ((x>>(3+3*b))&7)==0 else 1
  active=((x>>2)&1)==0 and G==-1
  return -1 if (x>>(0 if active else 1))&1 else 1
 truth=[fn(x) for x in range(1<<n)];P=walsh(truth);Q={t:v/2 for t,v in P.items()};Q[1]=Q.get(1,F(0))+F(1,2)
 seen=set();partial=0
 domain=product([-1,0,1],repeat=2 if pilot else 6)
 for raw in domain:
  if pilot:raw=(raw[0],-1,-1,raw[1],-1,-1)
  partial+=1;fixed={};counts=[0,0,0,0];phase=1;sig=[]
  for b in range(m):
   v=raw[3*b:3*b+3];remain=[j for j,x in enumerate(v) if x==-1]
   if 1 in v:
    # Independently verify every actually irrelevant remaining seed coordinate.
    for xx in range(8):
     if all(v[j]==-1 or ((xx>>j)&1)==v[j] for j in range(3)):
      for j in remain:ck((xx==0)==((xx^(1<<j))==0),'actual cleanup seed has identical physical children')
    for j in range(3):fixed[3+3*b+j]=int(j==0)
    sig.append((0,1,0))
   elif not remain:
    phase*=-1
    for j in range(3):fixed[3+3*b+j]=0
    sig.append((0,-1,0))
   else:
    counts[len(remain)]+=1
    for j in range(3):
     if j not in remain:fixed[3+3*b+j]=0
    sig.append((len(remain),1,sum(1<<j for j in remain)))
  key=tuple(sig)
  if key in seen:continue
  seen.add(key)
  for padding in [0,1]:
   for qval in [0,1]:
    assign={**fixed,0:qval}
    if padding:assign[2]=0
    rem=[j for j in range(n) if j not in assign];vals=[]
    for x in range(1<<len(rem)):
     xx=sum(v<<j for j,v in assign.items())+sum(((x>>i)&1)<<j for i,j in enumerate(rem));vals.append(truth[xx])
    actual=walsh(vals);ref=project(Q,rem)
    rr,seed,nu,a,p=make_rows(k,m,counts[1],counts[2],counts[3],phase,padding)
    obs=defaultdict(int);expected=defaultdict(int)
    for x in range(1<<len(rem)):obs[(actual.get(x,F(0)),ref.get(x,F(0)),x==0)]+=1
    for count,pp,qq,z in rr:expected[(pp,qq,z)]+=count
    ck(obs==expected,'literal original Boolean spectra + original-reference marginals, including mixed padding')
    I=sum(t.bit_count()*v for t,v in actual.items());edges=sum(vals[x]!=vals[x^(1<<j)] for x in range(len(vals)) for j in range(len(rem)))
    ck(I==F(edges,len(vals)),'independent physical edges equal Fourier influence')
    rho=F(1,2)*2**padding;ig=F(counts[1]+counts[2])+F(3*counts[3],4)
    ck(I==1+((k-padding)-1)*a+rho*ig/2,'both signed full-influence input from actual core')
 return {'original_core_dimension':n,'partial_assignments':partial,'signed_histories':2*partial,'unique_cleaned_coordinate_states':len(seen),'includes_padding_event':True}

def terminal(k):
 rho=F(1,1<<k);m=4;mu=F(3,4)**m;p=rho*(1-mu)/2
 rr,seed,nu,a,_=make_rows(k,m,0,0,1,1,k);C=fullcost(rr);U=add(Lq(p),conversion(p));out=[]
 for qsign in [-1,1]:
  def fun(x):
   u=-1 if x&1 else 1;g=-1 if ((x>>1)&7)==0 else 1;mask=-1 if ((x>>4)&3)==0 else 1
   h=qsign if g==-1 else u
   return h*mask if (x>>6)&1 else 1
  vals=[fun(x) for x in range(128)];P=walsh(vals);Q={}
  for t in range(128):
   core=t&15;u=core&1;g=core>>1
   pg=F(9,16) if not g else F(1,16)
   qc=rho*(pg+(1-2*mu)*int(g==0))/8+(1-2*p)*int(core==1)/2+F(int(core==0),2)
   Q[t]=qc/16+F(int((t&63)==0),4)
  direct=cehist([(1,P.get(t,F(0)),Q[t]) for t in range(128)])
  ck(not (direct[1]<C[0] or direct[0]>C[1]),'full7bit actual gate interference/CE independent direct spectrum')
  influences=[F(sum(vals[x]!=vals[x^(1<<j)] for x in range(128)),128) for j in range(7)]
  ck(influences==[F(7,16)]+[F(1,16)]*3+[F(1,4)]*2+[F(1,2)-F(qsign,32)],'ALL7 physical coordinates essential, exact influences')
  ck(sum(v for t,v in P.items() if t&14)==F(7,64),'selected complete row mass7/64')
  ck(all(Q[t]==rho/2048 and P.get(t,F(0))==F(1,1024) for t in range(128) if t&14),'selected actual atom/reference weights')
  fourI=4*sum(influences);z=sub(sub(val(fourI),direct),U)
  ck(fourI in [F(51,8),F(53,8)],'fixed actual I, independent of original k')
  if k>=64:ck(z[1]<F(-101,64),'cleanup-closed mixed-padding explicit witness')
  # Source before padding remains eligible at its completed tensor cleanup endpoint.
  if qsign==-1:
   rootrows,_,_,small_a,_=make_rows(k,m,0,0,1,1,0);preC=fullcost(rootrows)
   preI=6+2*(k-1)*small_a+rho*F(3,4)-small_a
   ck(sub(sub(val(preI),preC),U)[0]>F(5,4),'positive cleanup endpoint BEFORE relevant padding block')
  selected=F(7*(k+11),64)
  ck(direct[0]>=selected and direct[1]<=selected+F(342,64),'nonselected complete rows have code lengths <6')
  liability=scale(sub(add(direct,U),val(fourI)),rho)
  positive=(max(F(0),liability[0]),max(F(0),liability[1]))
  spent=F(k)*rho/16
  ck(positive[1]<5*spent,'reach-weighted positive bad-leaf liability, actual padding influence benchmark')
  ratio=scale(positive,1/spent)
  ck(ratio[1]<=F(7,4)+F(51,4*k),'explicit finite-width upper ratio, not unallocated bank')
  out.append({'weighted_positive_liability':pack(positive),'actual_padding_influence_spent':str(spent),'liability_to_spent_ratio':pack(ratio),'qsign':qsign,'four_I':str(fourI),'influences':list(map(str,influences)),'full_cost':pack(direct),'reserve_after_same_U':pack(z),'physical_reach_ignoring_cleanup':'2^(-'+str(k+4)+') per q sign'})
 # Original actual root is eligible for every frozen k; prove all-k bound in REPORT.
 rootrows,_,_,roota,_=make_rows(k,4,0,0,4,1,0)
 rootcoreC=cehist([(n,pp,qq) for n,pp,qq,z in rootrows])
 JA=2*k*p+3*rho
 rootC=add(scale(rootcoreC,F(1,2)),val(3))
 rootsurplus=sub(val(6+JA),rootC)
 ck(rootsurplus[0]>F(139,64),'actual supplied ORIGINAL full root eligible before rare history')
 return {'k':k,'m':m,'original_root_surplus':pack(rootsurplus),'actual_dimension':7,'profiles':out,'selected_cost_exact':str(F(7*(k+11),64)),'analytic_upper_reserve':str(F(53,8)-F(7*(k+11),64))}

def pack(z):return [str(rnd(z[0])),str(rnd(z[1],True))]
if __name__=='__main__':
 from itertools import product
 pilot='--pilot' in sys.argv;results=[]
 for n1,n2,n3 in product(range(2 if pilot else 3),repeat=3):
  for phase in [-1,1]:results.append(review(5,n1+n2+n3+4,n1,n2,n3,phase))
 if not pilot:
  for d in [1,2,3]:
   for count in [16,64]:
    ns=[0,0,0];ns[d-1]=count
    for phase in [-1,1]:results.append(review(5,count+4,*ns,phase))
 mixed=[terminal(k) for k in ([64] if pilot else [5,8,16,32,64,128,256])]
 lit=literal(pilot)
 ck(15**15>2**56 and 31**31>2**152,'integer entropy-envelope signs')
 ck(F(7*75,64)-F(53,8)==F(101,64),'strict finite selected-row no-go gap at k64')
 result={'status':'PASS','assertions':N,'runtime_seconds':time.perf_counter()-START,'source_review_profiles':results,'mixed_padding_profiles':mixed,'literal':lit,'arithmetic':'Fraction, integer Walsh/physical edges;90bit outward dyadic40term atanh','scope':'A020 all-tensor scoped review; new mixed-padding obstruction, no FEI disproof'}
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'status':'PASS','assertions':N,'runtime_seconds':result['runtime_seconds'],'review_profiles':len(results),'mixed_profiles':len(mixed),'literal':lit}))