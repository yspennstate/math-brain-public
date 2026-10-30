"""Independent two-core stopping hull, exact prime-log arithmetic."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from itertools import product
import json,time,sys
from arithmetic import Q,log2,scale,plus
ROOT=Path(__file__).resolve().parents[1];CHECKS=0
def ck(x):
 global CHECKS
 assert x;CHECKS+=1
def save(n,x):(ROOT/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def add(*ps):
 d={}
 for p in ps:
  for k,v in p.items():d[k]=d.get(k,F(0))+v
 return {k:v for k,v in d.items() if v}
def mul(p,x):return {k:v*x for k,v in p.items() if v*x}
def neg(p):return mul(p,-1)
def mean(ps):return mul(add(*ps),F(1,len(ps)))
def minus(p,q):return add(p,neg(q))
def pack(p):return {str(k):str(v) for k,v in sorted(p.items())}
@lru_cache(None)
def factors(n):
 ck(n>0);out={};k=2
 while k*k<=n:
  while n%k==0:out[k]=out.get(k,0)+1;n//=k
  k=3 if k==2 else k+2
 if n>1:out[n]=out.get(n,0)+1
 return out
def lp(q):
 ck(q>0);d={}
 for n,sign in [(q.numerator,1),(q.denominator,-1)]:
  for p,e in factors(n).items():d[p]=d.get(p,F(0))+sign*e
 return {k:v for k,v in d.items() if v}
@lru_cache(None)
def evitem(k):return (Q,Q) if k==2 else log2(F(k))
def ev(p):
 out=(0,0)
 for k,v in p.items():
  a=evitem(k)
  out=plus(out,scale(a,v) if v>=0 else tuple(-z for z in scale(a,-v)[::-1]))
 return out
def cmp(a,b):
 d=minus(a,b)
 if not d:return 0
 x=ev(d)
 if x[0]>0:return 1
 if x[1]<0:return -1
 raise ArithmeticError('Unresolved exact prime-log comparison')
def pos(p):return p if cmp(p,{})>0 else {}
def child(t,i,b):return tuple(t[x] for x in range(len(t)) if x>>i&1==b)
@lru_cache(None)
def canon(t):
 for i in range((len(t)-1).bit_length()):
  if all(t[x]==t[x^(1<<i)] for x in range(len(t))):
   ck(child(t,i,0)==child(t,i,1));return canon(child(t,i,0))
 return t
G=tuple(-1 if x<3 else 1 for x in range(64))
H=tuple(-1 if x in {0,1,2,4,8,16,32,6,17,40} else 1 for x in range(64))
K4=tuple(-H[sum(((z>>j)&1)<<(j+2) for j in range(4))] for z in range(16))
@lru_cache(None)
def core(t):
 N=len(t);n=(N-1).bit_length();ck(all(x in [-1,1] for x in t));w=list(t);h=1
 while h<N:
  for j in range(0,N,2*h):
   for k in range(j,j+h):w[k],w[k+h]=w[k]+w[k+h],w[k]-w[k+h]
  h*=2
 direct=[sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(t)) for s in range(N)]
 ck(direct==w and sum(z*z for z in w)==N*N)
 for x,y in enumerate(t):ck(sum(z*(-1 if (s&x).bit_count()%2 else 1) for s,z in enumerate(w))==N*y)
 ent={};ds=[]
 for z in w:
  if z:ent=add(ent,mul(lp(F(abs(z),N)),-2*F(z*z,N*N)))
 for i in range(n):
  d=F(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N)
  ck(d==sum(F(z*z,N*N) for s,z in enumerate(w) if s>>i&1));ds.append(d)
 return dict(mu=F(sum(t),N),H=ent,I=sum(ds),ds=ds)
def prod(xs):
 v=F(1)
 for x in xs:v*=x
 return v
@lru_cache(None)
def outer(mus):
 vs=[1-m*m for m in mus];co=list(map(F,K4))
 for j,m in enumerate(mus):
  for x in range(16):
   if x>>j&1:continue
   a,b=co[x],co[x|1<<j];co[x]=(1+m)*a/2+(1-m)*b/2;co[x|1<<j]=(a-b)/2
 mass=[c*c*prod(vs[j] for j in range(4) if T>>j&1) for T,c in enumerate(co)]
 ck(sum(mass)==1)
 qs=[]
 for j in range(4):
  q=sum(prod((1-mus[k])/2 if x>>k&1 else (1+mus[k])/2 for k in range(4) if k!=j) for x in range(16) if not(x>>j&1) and K4[x]!=K4[x|1<<j])
  ck(sum(mass[T] for T in range(16) if T>>j&1)==vs[j]*q);qs.append(q)
 for x,y in enumerate(K4):
  ck(sum(co[T]*prod(1-2*(x>>j&1)-mus[j] for j in range(4) if T>>j&1) for T in range(16))==y)
 # Separate direct weighted moments, including deterministic inputs without division.
 active=[j for j,v in enumerate(vs) if v]
 for T in range(16):
  if any(T>>j&1 and not vs[j] for j in range(4)):ck(mass[T]==0);continue
  moment=sum(F(K4[x])*prod((1-mus[j])/2 if x>>j&1 else (1+mus[j])/2 for j in range(4))*prod(1-2*(x>>j&1)-mus[j] for j in active if T>>j&1) for x in range(16))
  var=prod(vs[j] for j in active if T>>j&1);ck(var>0 and mass[T]==moment*moment/var)
 ent={}
 for T,(c,p) in enumerate(zip(co,mass)):
  if not p:continue
  logs=mul(lp(abs(c)),2)
  for j in range(4):
   if T>>j&1:logs=add(logs,lp(vs[j]))
  ent=add(ent,mul(logs,-p))
 for q,v in zip(qs,vs):
  for p in [v,1-v]:
   if p:ent=add(ent,mul(lp(p),q*p))
 return dict(C=ent,q=qs,masses=mass)
@lru_cache(None)
def full(ts):
 cs=[core(t) for t in ts];o=outer(tuple(c['mu'] for c in cs));h=add(o['C'],*[mul(c['H'],q) for c,q in zip(cs,o['q'])]);I=sum(c['I']*q for c,q in zip(cs,o['q']))
 return dict(H=h,I=I,S=add({2:4*I},neg(h)),q=o['q'],cores=cs)
def graph():
 states={}
 def visit(t):
  if t in states:return
  acts=[];states[t]=acts
  for i in range((len(t)-1).bit_length()):
   kids=tuple(canon(child(t,i,b)) for b in range(2));acts.append((i,kids))
   for c in kids:visit(c)
 visit(G);ck(len(states)==12)
 for pat in product([-1,0,1],repeat=6):
  free=[i for i,b in enumerate(pat) if b==-1];fixed=sum((b==1)<<i for i,b in enumerate(pat))
  raw=tuple(G[fixed|sum(((x>>k)&1)<<i for k,i in enumerate(free))] for x in range(1<<len(free)));t=canon(raw);ck(t in states)
  for i in range(len(free)):
   kids=tuple(canon(child(raw,i,b)) for b in range(2));ck(kids==(t,t) or any(kids==a[1] for a in states[t]))
 return states
def main():
 start=time.perf_counter();dag=graph();pilot='--pilot' in sys.argv
 for z in range(16):
  for a,b in [(0,2),(1,3)]:
   zz=z^((1<<a)|(1<<b)) if (z>>a&1)!=(z>>b&1) else z;ck(K4[z]==K4[zz])
 pairs=[(0,2)] if pilot else [(0,2),(1,3),(0,1)]
 results=[]
 for pair in pairs:
  records={};allocation=[]
  @lru_cache(None)
  def solve(t,u):
   ts=[G]*4;ts[pair[0]]=t;ts[pair[1]]=u;p=full(tuple(ts));stop=pos(neg(p['S']));R=stop;winner='stop';acts=[]
   for side,state in enumerate([t,u]):
    for i,kids in dag[state]:
     args=[(c,u) if side==0 else (t,c) for c in kids];zs=[solve(*arg) for arg in args];r=mean([z['R'] for z in zs]);d=p['q'][pair[side]]*core(state)['ds'][i]
     ck(p['I']-sum(z['I'] for z in zs)/2==d)
     e=minus(mean([z['S'] for z in zs]),p['S']);ck(e==add(p['H'],neg(mean([z['H'] for z in zs])),{2:-4*d}))
     acts.append(dict(side=side,coordinate=i,args=args,r=r,e=e,d=d))
     if cmp(r,R)>0:R=r;winner=f'{side}:{i}'
   for a in acts:
    spare=minus(R,a['r']);ck(cmp(spare,{})>=0)
    ac=[add(solve(*arg)['R'],spare) for arg in a['args']];dc=[add(solve(*arg)['S'],credit) for arg,credit in zip(a['args'],ac)]
    ck(mean(ac)==R and mean(dc)==add(p['S'],R,a['e']))
    for v in ac+dc:ck(cmp(v,{})>=0)
    allocation.append(dict(state=[list(t),list(u)],side=a['side'],coordinate=a['coordinate'],physical_influence=str(a['d']),parent_required_credit=pack(R),child_credit=[pack(x) for x in ac],child_debit=[pack(x) for x in dc],query_excess=pack(a['e']),new_outside_flow='0'))
   z=dict(S=p['S'],H=p['H'],I=p['I'],R=R,winner=winner,acts=acts);records[(t,u)]=z;return z
  root=solve(G,G);A=neg(root['S']);gap=minus(root['R'],A);ck(cmp(gap,{})>=0)
  # Lower-bound witness: chosen action attains the hull, with true reach weights.
  reaches={(G,G):F(1)};terminal=[]
  for key in sorted(records,key=lambda k:sum((len(t)-1).bit_length() for t in k),reverse=True):
   w=reaches.get(key,F(0));node=records[key]
   if not w:continue
   if node['winner']=='stop':terminal.append((key,w));continue
   side,i=map(int,node['winner'].split(':'));act=next(a for a in node['acts'] if a['side']==side and a['coordinate']==i)
   for arg in act['args']:reaches[arg]=reaches.get(arg,F(0))+w/2
  ck(sum(w for key,w in terminal)==1)
  ck(add(*[mul(pos(neg(records[key]['S'])),w) for key,w in terminal])==root['R'])
  results.append(dict(pair_original=[x+2 for x in pair],states=len(records),query_rows=len(allocation),initial_S=ev(root['S']),initial_credit=ev(A),required_credit=ev(root['R']),extra_required=ev(gap),exact_required=pack(root['R']),exact_extra=pack(gap),verdict='SAME_CREDIT_ALL_TWO_CORE_POLICIES' if not gap else 'STRICT_EXTRA_CREDIT_REQUIRED',states_certificate=[dict(truths=[list(t) for t in key],S=pack(z['S']),R=pack(z['R']),winner=z['winner']) for key,z in records.items()],rows=allocation,attaining_terminals=[dict(truths=[list(t) for t in key],reach=str(w),negative_slack=pack(pos(neg(records[key]['S'])))) for key,w in terminal]))
  save('PILOT_CASES.json' if pilot else 'JOINT_CASES.json',results)
  ck(time.perf_counter()-start<55)
 result=dict(version='A084-joint-credit-v1',pairs=[{k:v for k,v in r.items() if k in ['pair_original','states','query_rows','initial_credit','required_credit','extra_required','verdict']} for r in results],exact_assertions=CHECKS,unique_full_profiles=full.cache_info().currsize,outer_profiles=outer.cache_info().currsize,core_profiles=core.cache_info().currsize,runtime_seconds=time.perf_counter()-start,scale_bits=192,full_fei='OPEN')
 save('PILOT.json' if pilot else 'VALIDATION.json',result);print(json.dumps(result))
if __name__=='__main__':main()
