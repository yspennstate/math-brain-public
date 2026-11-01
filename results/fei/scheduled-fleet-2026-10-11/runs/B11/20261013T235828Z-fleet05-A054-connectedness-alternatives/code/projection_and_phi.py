from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,sys
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); pilot='--pilot' in sys.argv;checks=0;limit=55 if pilot else 175
def ck(c):
 global checks
 checks+=1
 assert c
 if time.perf_counter()-start>limit:raise RuntimeError('frozen runtime limit')
def add(*terms):
 d={}
 for a,b in terms:
  for k,v in a.items():d[k]=d.get(k,F(0))+v*b
 return {k:v for k,v in d.items() if v}
@lru_cache(None)
def fac(a):
 d={};k=2
 while k*k<=a:
  while a%k==0:d[k]=d.get(k,0)+1;a//=k
  k+=1
 if a>1:d[a]=d.get(a,0)+1
 return d
def logv(q):return add((fac(q.numerator),1),(fac(q.denominator),-1))
def entropy(ws):
 d={}
 for w in ws:
  if w:d=add((d,1),(logv(w),-w))
 return d
@lru_cache(None)
def logbound(k):
 shift=k.bit_length()-1;z=F(1,3) if k==2 else F(k-2**shift,k+2**shift)
 lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
 hi=lo+2*z**65/(65*(1-z*z))
 if k!=2:
  a,b=logbound(2);lo+=shift*a;hi+=shift*b
 scale=1<<112
 return F(lo.numerator*scale//lo.denominator,scale),F(-((-hi.numerator*scale)//hi.denominator),scale)
def interval(v):
 lo=hi=F(0)
 for k,c in v.items():
  a,b=logbound(k);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 return lo,hi
def ge(v):
 if not v:return True
 lo,hi=interval(v);ck(lo>0 or hi<0);return lo>0
def nonneg(v):ck(ge(v))
def vec(v):return {str(k):str(x) for k,x in sorted(v.items())}
def serial(q):
 if isinstance(q,F):return str(q)
 if isinstance(q,dict):return {str(k):serial(v) for k,v in q.items()}
 if isinstance(q,(tuple,list)):return [serial(v) for v in q]
 return q
def save(name,obj):(ROOT/'out'/name).write_text(json.dumps(serial(obj),indent=2)+'\n',encoding='utf-8')
@lru_cache(None)
def spec(h):
 a=list(h);N=len(a);w=1
 while w<N:
  for i in range(0,N,2*w):
   for j in range(w):u=a[i+j];v=a[i+j+w];a[i+j]=u+v;a[i+j+w]=u-v
  w*=2
 return tuple(F(x*x,N*N) for x in a)
def direct(h):
 N=len(h)
 return tuple(F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(h))**2,N*N) for s in range(N))
@lru_cache(None)
def raw(h):return entropy(spec(h))
def energy(h,A):return sum((p*(s&A).bit_count() for s,p in enumerate(spec(h))),F(0))
def edges(h,A):return F(sum((h[x]-h[x^(1<<i)])**2 for i in range(len(h).bit_length()-1) if A>>i&1 for x in range(len(h))),4*len(h))
def mass(h):return F(sum(v*v for v in h),len(h))
@lru_cache(None)
def children(h,A):
 n=len(h).bit_length()-1;a=[i for i in range(n) if A>>i&1];c=[i for i in range(n) if not A>>i&1]
 def scatter(z,ids):return sum((z>>j&1)<<i for j,i in enumerate(ids))
 return tuple(tuple(h[scatter(x,a)|scatter(y,c)] for y in range(1<<len(c))) for x in range(1<<len(a)))
@lru_cache(None)
def ledger(h,A):
 ch=children(h,A);avg={}
 for v in ch:avg=add((avg,1),(raw(v),F(1,len(ch))))
 L=add((raw(h),1),(avg,-1));m={}
 for s,q in enumerate(spec(h)):m[s&~A]=m.get(s&~A,F(0))+q
 B=add((raw(h),1),(entropy(m.values()),-1));J=add((L,1),(B,-1))
 return L,B,J
def components(h):
 rem={x for x,v in enumerate(h) if v};out=[];n=len(h).bit_length()-1
 while rem:
  seed=min(rem);rem.remove(seed);vis={seed};todo=[seed]
  while todo:
   x=todo.pop()
   for i in range(n):
    y=x^(1<<i)
    if y in rem:rem.remove(y);vis.add(y);todo.append(y)
  out.append(tuple(int(x in vis) for x in range(len(h))))
 return out
def projection(h,A):return {x&A for x,v in enumerate(h) if v}
cases=paid=isolating=0
def check_projection(h,A):
 global cases,paid,isolating
 cases+=1;cs=components(h);Ls=[];Q={};ps=mass(h);r=A.bit_count();rs=[]
 ck(spec(h)==direct(h));ck(energy(h,A)==edges(h,A))
 for c in cs:
  R=projection(c,A);mu=F(len(R),1<<r);p=mass(c);rs.append(R)
  credit=add((logv(mu),-p));Q=add((Q,1),(credit,1))
  L,B,J=ledger(c,A);Ls.append(L)
  nonneg(add((B,1),(credit,-1)));nonneg(add((J,1),(credit,-1)))
  nonneg(add(({2:2*energy(c,A)},1),(credit,-1)))
 sumL=add(*[(v,1) for v in Ls]) if Ls else {}
 L,B,J=ledger(h,A);cross=add((L,1),(sumL,-1));gap=raw(h)
 for c in cs:gap=add((gap,1),(raw(c),-1))
 terminal={};hc=children(h,A);cc=[children(c,A) for c in cs]
 for x,v in enumerate(hc):
  d=raw(v)
  for ch in cc:d=add((d,1),(raw(ch[x]),-1))
  terminal=add((terminal,1),(d,F(1,len(hc))))
 ck(gap==add((cross,1),(terminal,1)))
 separated=all(not(rs[i]&rs[j]) for i in range(len(rs)) for j in range(i))
 if separated:
  isolating+=1;ck(not terminal)
  cond=add((Q,2),({2:r*ps},-1))
  if ge(cond):
   paid+=1;nonneg(add((sumL,1),(B,-1)))
 return dict(Q=Q,projection_sizes=[len(x) for x in rs],paid=separated and ge(add((Q,2),({2:r*ps},-1))),cross=cross,terminal=terminal)
tables=0
if pilot:
 small=[(0,0),(2,1),(2,3),(2,7),(2,15)]
else:small=[(n,m) for n in range(4) for m in range(1<<(1<<n))]
for n,m in small:
 h=tuple(m>>x&1 for x in range(1<<n));tables+=1
 for A in range(1,1<<n):check_projection(h,A)
skew=0;noncartesian=0;moderate=0
for z0 in range(1 if pilot else 8):
 for z1 in range(1 if pilot else 8):
  R0=[0,1,2];R1=[12,13,14];a=[0]*32;b=[0]*32
  for j,x in enumerate(R0):a[x]=1;a[x+16]=z0>>j&1
  for j,x in enumerate(R1):b[x]=1;b[x+16]=z1>>j&1
  g=tuple(x+y for x,y in zip(a,b));ck(len(components(g))==2)
  record=check_projection(g,15);ck(record['paid']);skew+=1
  noncartesian+=int(z0 not in [0,7] or z1 not in [0,7]);moderate+=int(mass(g)>=F(1,4))
N=128;a=tuple(int((x&15).bit_count()<=1) for x in range(N));b=tuple(int(x==15) for x in range(N));g=tuple(u+v for u,v in zip(a,b));f=tuple(1-2*v for v in g)
ck(len(components(g))==2);ck(spec(f)==direct(f))
phi_records=[]
for A in ([1,15] if pilot else range(1,127)):
 pr=check_projection(g,A);L,B,J=ledger(f,A);d=energy(f,A);ck(d==edges(f,A))
 ck(d==4*energy(g,A));ck(ge(J));ck(interval(J)[1]<=2*d)
 rawL=ledger(g,A)[0];rawcost=add((rawL,1/energy(g,A)));cost=add((L,1/d))
 phi_records.append(dict(mask=A,query_bits=A.bit_count(),influence=d,entropy_drop=vec(L),B=vec(B),J=vec(J),sign_cost=cost,raw_cost=rawcost,cross=vec(pr['cross']),terminal=vec(pr['terminal'])))
def summarize(key):
 best=phi_records[0]
 for v in phi_records[1:]:
  diff=add((v[key],1),(best[key],-1))
  if diff and not ge(diff):best=v
 ties=[v['mask'] for v in phi_records if v[key]==best[key]]
 for v in phi_records:
  if v[key]!=best[key]:nonneg(add((v[key],1),(best[key],-1)))
 lo,hi=interval(best[key]);lnlo,lnhi=logbound(2)
 return dict(masks=ties,exact_natural_ratio_vector=vec(best[key]),bit_ratio_interval=[lo/lnhi,hi/lnlo])
sign_phi=summarize('sign_cost');raw_phi=summarize('raw_cost')
root_sign=add((raw(f),1/energy(f,127)));root_raw=add((raw(g),1/energy(g,127)))
root_sign_bounds=interval(root_sign);lnlo,lnhi=logbound(2)
actual_descent=ge(add((root_sign,1),(phi_records[[v['mask'] for v in phi_records].index(sign_phi['masks'][0])]['sign_cost'],-1)))
save('BRAIN45_PHI_'+('PILOT.json' if pilot else 'EXACT.json'),dict(sign_phi=sign_phi,raw_phi=raw_phi,root_sign_ratio_bits=[root_sign_bounds[0]/lnhi,root_sign_bounds[1]/lnlo],root_sign_vector=vec(root_sign),root_raw_vector=vec(root_raw),strict_own_ratio_descent=actual_descent,profiles=[{**v,'sign_cost':vec(v['sign_cost']),'raw_cost':vec(v['raw_cost'])} for v in phi_records]))
if not pilot:
 N=512;a9=tuple(int((x&31).bit_count()<=1) for x in range(N));b9=tuple(int(x==31) for x in range(N));g9=tuple(x+y for x,y in zip(a9,b9))
 pr9=check_projection(g9,31)
 save('HISTORICAL_PROJECTION_DEBTS.json',dict(brain45=check_projection(g,15),brain44=pr9))
result=dict(status='PASS',pilot=pilot,tables=tables,projection_cases=cases,isolating_cases=isolating,paid_cases=paid,skew_cases=skew,noncartesian_cases=noncartesian,moderate_density_skew_cases=moderate,assertions=checks,seconds=time.perf_counter()-start,sign_phi_masks=sign_phi['masks'],raw_phi_masks=raw_phi['masks'],strict_sign_descent=actual_descent)
save('PILOT.json' if pilot else 'EXACT_CHECK.json',result);print(json.dumps(result,indent=2))
