from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import json,time,math,sys

checks=0
def eq(a,b):
 global checks
 assert a==b,(a,b);checks+=1
def ok(v,msg=''):
 global checks
 assert v,msg;checks+=1
@lru_cache(None)
def fac(x):
 out={};p=2
 while p*p<=x:
  while x%p==0:out[p]=out.get(p,0)+1;x//=p
  p+=1
 if x>1:out[x]=out.get(x,0)+1
 return out
@lru_cache(None)
def loge(q):
 out=defaultdict(F)
 for p,v in fac(q.numerator).items():out[p]+=v
 for p,v in fac(q.denominator).items():out[p]-=v
 return {p:v for p,v in out.items() if v}
def add(*es):
 out=defaultdict(F)
 for scale,e in es:
  for p,v in e.items():out[p]+=scale*v
 return {p:v for p,v in out.items() if v}
def H(ps):return add(*[(-p,loge(p)) for p in ps if p])
def plog(p):return add((p,loge(p))) if p else {}
def fwht(t):
 a=list(t);h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
  h*=2
 return [F(v,len(t)) for v in a]
def ins(x,i,b):return (x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)
def metrics(a,i):
 B={};L={};d=F()
 for w in range(len(a)//2):
  x,y=a[ins(w,i,0)]**2,a[ins(w,i,1)]**2;q=x+y;d+=y
  if q:
   B=add((1,B),(1,H([x,y])),(-1,H([q])))
   if y:L=add((1,L),(y,loge(q/y)))
 ap=[a[ins(w,i,0)]+a[ins(w,i,1)] for w in range(len(a)//2)]
 am=[a[ins(w,i,0)]-a[ins(w,i,1)] for w in range(len(a)//2)]
 D=add((1,H([x*x for x in a])),(-F(1,2),H([x*x for x in ap])),(-F(1,2),H([x*x for x in am])))
 return d,B,L,D,ap,am

TERMS=64
SCALE=2**192
def rounded(iv):
 a,b=iv
 return F((a*SCALE).numerator//(a*SCALE).denominator,SCALE),F(-((-b*SCALE).numerator//(-b*SCALE).denominator),SCALE)
def lnunit(q):
 z=(q-1)/(q+1);z2=z*z;p=z;s=F()
 for j in range(TERMS):s+=2*p/(2*j+1);p*=z2
 return s,s+2*p/((2*TERMS+1)*(1-z2))
ln2=lnunit(F(2))
@lru_cache(None)
def logi(q):
 if F(1,2)<=q<1:
  a,b=logi(1/q);return -b,-a
 e=0
 while q<1:q*=2;e-=1
 while q>=2:q/=2;e+=1
 a,b=lnunit(q);return rounded((e+a/ln2[1],e+b/ln2[0]))
def ivsum(*ts):
 a=b=F()
 for c,(x,y) in ts:
  if c>=0:a+=c*x;b+=c*y
  else:a+=c*y;b+=c*x
 return a,b
def ive(e):return ivsum(*[(c,logi(F(p))) for p,c in e.items()])
def Hiv(ps):return ivsum(*[(-p,logi(p)) for p in ps if p])
def logmassiv(x):return ivsum((x,logi(x))) if x else (F(),F())
def kern(u):
 A=(u-1)**2+1
 ell=loge(A);beta=add((A,loge(A)),(-1,plog((u-1)**2)))
 gamma=add((F(1,2),plog(u*u)),(F(1,2),plog((u-2)**2)),(-1,plog((u-1)**2)))
 return ell,beta,gamma

start=time.perf_counter();roots=splits=newsplits=oldchecks=0
def check(t,r,v,q=4):
 global roots,splits,newsplits,oldchecks
 n=r+q;delta=F(1,1<<n);d=2*delta;s=t[v]
 core=fwht(t);K=sum(bool(x) for x in core)
 old=[t[x&((1<<r)-1)] for x in range(1<<n)];edited=old.copy();edited[v]*=-1
 a=fwht(edited);base=fwht(old);roots+=1
 eq(sum(x*x for x in a),F(1));ok(all(a),'full support')
 eps=F(2,2**(n//2));omega=Hiv([eps,1-eps]);omega=(omega[0]+eps,omega[1]+eps)
 newrows=[]
 for i in range(n):
  dc,B,L,D,ap,am=metrics(a,i);do,Bo,Lo,Do,_,_=metrics(base,i);splits+=1
  eq(ap,fwht([edited[ins(w,i,0)] for w in range(1<<(n-1))]))
  eq(am,fwht([edited[ins(w,i,1)] for w in range(1<<(n-1))]))
  ok(abs(dc-do)<=2*delta)
  if not do:
   newsplits+=1;eq(dc,d)
   expectedL={2:d};expectedB={2:2*d};expectedD={2:4*d};occupied=0
   for w in range(1<<(n-1)):
    c=base[ins(w,i,0)]
    if c:
     occupied+=1;phase=-1 if (ins(w,i,0)&v).bit_count()%2 else 1
     u=c*phase/(s*d);ok(u.denominator==1 and abs(u)>=2**(q-1))
     e,b,g=kern(u)
     expectedL=add((1,expectedL),(d*d,e),(-d*d,{2:F(1)}))
     expectedB=add((1,expectedB),(d*d,b),(-2*d*d,{2:F(1)}))
     expectedD=add((1,expectedD),(d*d,g),(-4*d*d,{2:F(1)}))
   eq(occupied,K);eq(L,expectedL);eq(B,expectedB);eq(D,expectedD)
   newrows.append((L,B,D))
   for expr,lower,extra in [(L,1,2*K*d*(n+1)),(B,2,K*d*(2*n+4)),(D,4,K*d*(2*n+7))]:
    if expr=={2:lower*d}:eq(expr,{2:lower*d})
    else:ok(ive(add((1,expr),(-lower*d,{2:F(1)})))[0]>=0)
    ok(ive(expr)[1]<=d*(lower+extra))
  else:
   oldchecks+=1
   for expr,prev,cost in [(B,Bo,1),(L,Lo,1),(D,Do,2)]:
    diff=ive(add((1,expr),(-1,prev)))
    ok(diff[0]>=-cost*omega[1] and diff[1]<=cost*omega[1])
 for row in newrows:eq(row,newrows[0])

pilot='--pilot' in sys.argv
for r in range(2 if pilot else 4):
 for mask in range(1<<(1<<r)):
  t=[1 if mask&(1<<x) else -1 for x in range(1<<r)]
  check(t,r,0)
for r in range(2 if pilot else 3):
 for mask in range(1<<(1<<r)):
  t=[1 if mask&(1<<x) else -1 for x in range(1<<r)]
  for v in range(1<<r):check(t,r,v)
ok(time.perf_counter()-start<(60 if pilot else 600),'frozen runtime cap')
out=Path(__file__).resolve().parents[1]/'out';out.mkdir(exist_ok=True)
finite={'status':'PASS','roots':roots,'coordinate_splits':splits,'new_coordinate_splits':newsplits,'old_relevant_splits':oldchecks,'exact_assertions':checks,'seconds':time.perf_counter()-start,'arithmetic':'integer FWHT; Fraction; exact prime-log equalities; proved-remainder rational log intervals','log_terms':TERMS}
(out/('PILOT_CHECK.json' if pilot else 'FINITE_CHECK.json')).write_text(json.dumps(finite,indent=2)+'\n',encoding='utf-8')
print(json.dumps(finite,indent=2))
if pilot:sys.exit(0)

# Only original support packets are traversed; no padded truth tables allocated.
seeds=[('point3',[ -1 if x==0 else 1 for x in range(8)],3),('f5',[-1 if x in (0,1,3) else 1 for x in range(32)],5),('f6',[-1 if x in (0,1,2,4,8,16,32,3,12,48) else 1 for x in range(64)],6)]
profiles=[];profile_start=time.perf_counter()
for name,t,r in seeds:
 core=fwht(t);s=t[0];K=sum(bool(c) for c in core)
 for q in (4,8,16,32):
  n=r+q;d=F(1,2**(n-1));L=(F(1),F(1));B=(F(2),F(2));D=(F(4),F(4))
  for c in core:
   if not c:continue
   u=c/(s*d);A=(u-1)**2+1
   ell=logi(A);beta=ivsum((A,logi(A)),(-1,logmassiv((u-1)**2)))
   gamma=ivsum((F(1,2),logmassiv(u*u)),(F(1,2),logmassiv((u-2)**2)),(-1,logmassiv((u-1)**2)))
   L=ivsum((1,L),(d,ell),(-d,(F(1),F(1))))
   B=ivsum((1,B),(d,beta),(-d,(F(2),F(2))))
   D=ivsum((1,D),(d,gamma),(-d,(F(4),F(4))))
  ok(L[0]>=1 and B[0]>=2 and D[0]>=4)
  ok(L[1]<=1+2*K*d*(n+1));ok(B[1]<=2+K*d*(2*n+4));ok(D[1]<=4+K*d*(2*n+7))
  profiles.append({'seed':name,'r':r,'q':q,'support_size':K,'L_interval':list(map(str,L)),'B_interval':list(map(str,B)),'D_interval':list(map(str,D)),'display_LBD':[float(sum(z)/2) for z in (L,B,D)],'display_only':True})
profile={'status':'PASS','profiles':profiles,'additional_assertions':checks-finite['exact_assertions'],'seconds':time.perf_counter()-profile_start,'no_padded_truth_tables':True}
(out/'COMPRESSED_PROFILES.json').write_text(json.dumps(profile,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in profile.items() if k!='profiles'},indent=2))
