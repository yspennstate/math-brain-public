from pathlib import Path
from fractions import Fraction as F
from math import prod
from itertools import combinations
import importlib.util,sys,json,time
sys.dont_write_bytecode=True
B=Path(__file__).resolve().parents[1];ROOT=B.parents[2];start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
def read(p):return json.loads(p.read_text(encoding='utf-8'))
source=ROOT/'A006/runs/20261021T182437Z-fleet03-A006-posterior-forest-optimization'
old=B.parent/'20261021T161852Z-fleet03-A010-universal-residual-falsifier'
sp=importlib.util.spec_from_file_location('own_prior_enumerator',old/'code/check.py');own=importlib.util.module_from_spec(sp);sp.loader.exec_module(own)
rows=read(source/'out/CHECK.json')['rows'];prior=read(old/'out/CHECK.json')['rows'];cost=read(source/'out/COST.json')['rows']
def cutlist(E,n,lift):
 out={};m=len(E)
 def insert(d):
  key=tuple(sorted((t,z) for t,z in d.items() if z));out.setdefault(key,dict(key))
 for i,j in combinations(range(m),2):
  if set(E[i]).isdisjoint(E[j]):continue
  for U in (range(1<<m) if lift else (0,)):
   if U&((1<<i)|(1<<j)):continue
   for t in map(F,[0,'1/4','1/2',1,2,4]):insert({U|1<<i:-t*t,U|1<<j:F(-1),U|1<<i|1<<j:4*(t+1)**2})
 if lift:
  for U in range(1,1<<m):
   for v in range(n):
    inc=[i for i,e in enumerate(E) if v in e and not(U>>i&1)]
    if inc:insert({U:F(-1),**{U|1<<i:F(4) for i in inc}})
 return list(out.values())
def logs(x):
 x=F(x);j=0
 while x<1:x*=2;j-=1
 while x>=2:x/=2;j+=1
 def ln(y):
  z=(y-1)/(y+1);l=2*sum((z**(2*i+1)/F(2*i+1) for i in range(24)),F(0));return l,l+2*z**49/(49*(1-z*z))
 l,u=ln(x);l2,u2=ln(F(2));return j+l/u2,j+u/l2,l2
duals=0;runs=0
for r,pr,cr in zip(rows,prior,cost):
 E=tuple(map(tuple,r['edges']));n=r['n'];m=len(E);ck(E==tuple(map(tuple,pr['edges']))==tuple(map(tuple,cr['edges'])))
 h={int(t):F(z) for t,z in r['h'].items()};caps={int(t):F(z) for t,z in r['caps'].items()};ck(r['h']==pr['h'])
 P,I=own.physical(E,n);v=sum(P.values());lam=F(1,2*max(sum(v0 in e for e in E) for v0 in range(n)));D=(1+lam/4)**m-1
 p={T:(lam/4)**T.bit_count()/D for T in h};ck(sum(p.values())==1 and sum(p[t]*h[t] for t in h)==v)
 C={};Q={};actual_runs=0
 for A in range(1,1<<n):
  if any(A>>v0&1 and not any(v0 in e for e in E) for v0 in range(n)):continue
  C[A],cnt=own.full(A,E,n);actual_runs+=cnt;Q[A]=sum(z*lam**T.bit_count() for T,z in C[A].items())/D
 ck(actual_runs==r['runs']);runs+=actual_runs
 ck(all(h[T]==sum(P[A]*C[A].get(T,F(0))*4**T.bit_count()/Q[A] for A in P) for T in h))
 for T in h:
  w=pr['root_caps'][str(T)];L=F(w['L']);z=list(map(F,w['primal']));y=list(map(F,w['dual']));J=[e for i,e in enumerate(E) if T>>i&1];k=len(J)
  ck(sum(z)==sum(y)==L and all(x>=0 for x in z+y));ck(all(sum(z[i] for i,e in enumerate(J) if v0 in e)<=1 for v0 in range(n)));ck(all(y[x]+y[y0]>=1 for x,y0 in J))
  ck(caps[T]==1/((1+F(4*k)/L)**k-(F(4*k)/L)**k) and p[T]<=caps[T])
 values=[]
 for name,lift in [('cap',False),('pair',False),('lifted',True)]:
  cert=r['certificates'][name];cuts=[] if name=='cap' else cutlist(E,n,lift);ck(len(cuts)==cert['cut_count'])
  ck(all(sum(a*p[t] for t,a in c.items())<=0 for c in cuts));score=dict(h)
  for j,ystr in cert['multipliers']:
   y=F(ystr);ck(y>=0)
   for t,a in cuts[j].items():score[t]-=y*a
  theta=F(cert['theta']);bound=theta+sum(caps[t]*max(score[t]-theta,0) for t in h);ck(bound==F(cert['value']));values.append(bound);duals+=1
  ck(bound>=v and bound-v==F(cert['gap']))
 Bmin=min(values);ck(Bmin==F(r['certificates']['lifted']['best_value']));ck(2*(Bmin-v)<F(9,10)*I)
 lower=F(0);upper=F(0)
 for A,z in P.items():
  l,u,l2=logs(1/Q[A]);lower+=z*l;upper+=z*u
 lo,hi=map(F,cr['reference_cost_interval_bits']);ck(lo<=lower<=upper<=hi and hi-lo<=F(1,1<<30))
 ilo,ihi=map(F,cr['joint_infimum_enclosure_bits']);ck(ilo<=lower-(Bmin-v)/l2 and ihi>=upper)
 ck(time.monotonic()-start<55)
# Exact relaxation separator, not an admissible physical vector.
weights=[F(2,5)]*3+[F(1,2)];D=prod(1+w/4 for w in weights)-1;ck(D==F(3979,8000));p={T:prod(weights[i]/4 for i in range(4) if T>>i&1)/D for T in range(1,16)}
for T in p:
 k=T.bit_count();L=int(bool(T&7))+int(bool(T&8));cap=1/((1+F(4*k,L))**k-F(4*k,L)**k);ck(p[T]<=cap)
for i,j in combinations(range(3),2):
 for U in range(16):
  if U&((1<<i)|(1<<j)):continue
  a,b,c=p[U|1<<i],p[U|1<<j],p[U|1<<i|1<<j];ck(a>=4*c and b>=4*c and a*b>=4*c*(a+b))
ck(4*sum(p[8|1<<i] for i in range(3))-p[8]==F(200,3979))
result={'status':'PASS','helper':'A010-source-review-v1','graphs':len(rows),'dual_certificates':duals,'complete_runs_reconstructed':runs,'complete_cost_enclosures':len(cost),'assertions':checks,'seconds':time.monotonic()-start,'scope':'A006 entire proof plus certificates and cost; same coefficients independently reconstructed with own prior enumerator, not author imports'}
(B/'out/REVIEW_A006.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
