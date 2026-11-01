from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(exist_ok=True)
checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
def fac(n):
 d=defaultdict(int); j=2
 while j*j<=n:
  while n%j==0:d[j]+=1;n//=j
  j+=1
 if n>1:d[n]+=1
 return d
def logq(x):
 d=defaultdict(Q)
 for p,k in fac(x.numerator).items():d[p]+=k
 for p,k in fac(x.denominator).items():d[p]-=k
 return dict(d)
def add(*terms):
 d=defaultdict(Q)
 for c,t in terms:
  for p,v in t.items():d[p]+=c*v
 return {p:v for p,v in d.items() if v}
def ent(ps):return add(*[(-p,logq(p)) for p in ps if p])
def phi(a,b):return add((1,ent([a,b])),(-1,ent([a+b])))
def walsh(vals):
 v=list(vals); n=len(v); h=1
 while h<n:
  for i in range(0,n,2*h):
   for j in range(i,i+h):u,w=v[j],v[j+h];v[j],v[j+h]=u+w,u-w
  h*=2
 return [Q(w,n) for w in v]
def metrics(vals):
 a=walsh(vals); p=[x*x for x in a]; n=(len(vals)).bit_length()-1
 ck(sum(p)==1)
 inf=[sum(p[s] for s in range(len(p)) if s>>i&1) for i in range(n)]
 b=[add(*[(1,phi(p[s],p[s|(1<<i)])) for s in range(len(p)) if not s>>i&1]) for i in range(n)]
 return a,p,inf,b,ent(p)
def chain(r,d):
 n=1+d*(r+1); vals=[]
 for u in range(1<<n):
  x=1-2*(u&1)
  for t in range(d):
   z=1+t*(r+1)
   if (u>>z)&((1<<r)-1)==0:x=1-2*((u>>(z+r))&1)
  vals.append(x)
 return vals
def chain_closed(r,d):
 p=Q(1,1<<r);q=1-p;gain=(1-q**d)/p
 hgate=add((1,ent([q*q])),(2*r*p*(2-p),{2:Q(1)}))
 br=add((1,phi(q*q,p*p)),(2*p-2*p*p,{2:Q(1)}))
 singleton={1:q**d}
 for j in range(d):singleton[1<<(1+j*(r+1)+r)]=p*q**(d-1-j)
 return 1+r*(1-q**d),add((gain,hgate)),add((r*gain,br)),singleton
start=time.perf_counter();records=[]
for r,d in [(1,1),(1,2),(1,3),(2,1),(2,2),(3,1)]:
 a,ps,inf,b,h=metrics(chain(r,d));ii,hh,bb,singles=chain_closed(r,d)
 ck(sum(inf)==ii);ck(h==hh);ck(add(*[(1,v) for v in b])==bb);ck(a[0]==0)
 ck({1<<i:a[1<<i] for i in range(len(inf)) if a[1<<i]}==singles)
 lam=ent([v*v for v in singles.values()]);ck(lam==ent([a[1<<i]**2 for i in range(len(inf))]))
 p=Q(1,1<<r);q=1-p;br=add((1,phi(q*q,p*p)),(2*p-2*p*p,{2:Q(1)}))
 for t in range(d):
  for j in range(r):ck(b[1+t*(r+1)+j]==add((q**(d-1-t),br)))
  ck(b[1+t*(r+1)+r]=={} )
 ck(b[0]=={})
 td={};direct={}
 for t in range(1,d+1):
  _,_,_,ss=chain_closed(r,t-1);ll=ent([v*v for v in ss.values()])
  td=add((q,td),(r,br),(q,ll));direct=add((1,direct),(q**(d-t+1),ll))
 ck(td==add((1,bb),(1,direct)))
 records.append({'family':'chain','r':r,'d':d,'I':str(ii),'H_prime_logs':{str(k):str(v) for k,v in h.items()},'B_prime_logs':{str(k):str(v) for k,v in bb.items()}})
for aa,m in [(1,2),(2,2),(3,2),(1,4),(2,4),(3,4),(1,6),(2,6)]:
 p=Q(1,1<<aa);delta=Q(1,1<<m);sqrt=Q(1,1<<(m//2));L=1<<aa;N=1<<m
 bent=[(-1)**sum(((y>>j)&1)*((y>>(j+1))&1) for j in range(0,m,2)) for y in range(N)]
 vals=[bent[u>>aa]*(-1 if (u&(L-1))==0 and (u>>aa)==0 else 1) for u in range(L*N)]
 amps,ps,inf,b,h=metrics(vals);ba=walsh(bent)
 ck(amps[0]==sqrt-2*p*delta)
 for s in range(N):
  ck(amps[s<<aa]==ba[s]-2*p*delta)
  for t in range(1,L):ck(amps[(s<<aa)|t]==-2*p*delta)
 ck(inf[:aa]==[2*p*delta]*aa);ck(inf[aa:]==[Q(1,2)+2*p*delta]*m)
 u=4*p*p*delta*delta;counts=[(N+(1<<(m//2)))//2,(N-(1<<(m//2)))//2]
 vs=[(sqrt-2*p*delta)**2,(-sqrt-2*p*delta)**2];ms=[v+(L-1)*u for v in vs]
 ck(h==add((counts[0],ent([vs[0]])),(counts[1],ent([vs[1]])),(N*(L-1),ent([u]))))
 bw=add(*[(1,add((1,ent(ps[s<<aa:(s+1)<<aa])),(-1,ent([sum(ps[s<<aa:(s+1)<<aa])])))) for s in range(N)])
 ck(bw==add(*[(counts[j],add((1,ent([vs[j]])),(L-1,ent([u])),(-1,ent([ms[j]])))) for j in range(2)]))
 beta=4*p*(1-p)*delta;selector=[sum(ps[(s<<aa)|t] for s in range(N)) for t in range(L)]
 ck(selector==[1-beta]+[4*p*p*delta]*(L-1))
 chi=sum((ps[(s<<aa)|t]-selector[t]*ms[0 if ba[s]>0 else 1])**2/(selector[t]*ms[0 if ba[s]>0 else 1]) for s in range(N) for t in range(L))
 exactchi=beta/(1-beta)*16*p*p*delta*(1-delta)/((1+4*p*delta)**2-16*p*p*delta)
 ck(chi==exactchi);ck(sum(Q(bent[y])*Q(bent[y]-2*(y==0)) for y in range(N))/N==1-2*delta)
 records.append({'family':'selector','a':aa,'m':m,'I_W':str(sum(inf[:aa])),'I_data':str(sum(inf[aa:])),'chi_square':str(chi),'B_W_prime_logs':{str(k):str(v) for k,v in bw.items()}})
for vals in [chain(1,1),[(-1)**(((u>>1)&1)*((u>>2)&1))*(-1 if u==0 else 1) for u in range(8)]]:
 _,_,ii,bb,hh=metrics(vals);size=len(vals)
 _,_,ti,tb,th=metrics([vals[u%size]*vals[u//size] for u in range(size*size)])
 ck(sum(ti)==2*sum(ii));ck(th==add((2,hh)));ck(add(*[(1,v) for v in tb])==add(*[(2,v) for v in bb]))
for k in range(2,9):
 d=1<<(2*k);r=3*k;p=Q(1,1<<r)
 # Analytic Bernoulli lower bound for repeated dominant-singleton charge.
 lower=p*d*(d-1)*(1-3*d*p)
 ck(lower>0);ck(1+r*d*p<=Q(5,2))
 records.append({'family':'analytic_chain','k':k,'lower_repeated_log_nats':str(lower),'I_upper':str(1+r*d*p)})
out={'status':'PASS','assertions':checks,'runtime_seconds':time.perf_counter()-start,'records':records,'arithmetic':'Fraction/FWHT and exact rational prime-log identities; infinite inequalities proved in PROOF.md'}
(R/'out'/'validation.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='records'}))
