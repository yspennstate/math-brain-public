"""Finite-label JS transport: exact finite checks; no floating sign decisions."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json, sys, time

RUN=Path(__file__).resolve().parents[1]
START=time.perf_counter()
PILOT='--pilot' in sys.argv
LIMIT=55 if PILOT else 180
COUNT=0

def ck(b):
 global COUNT
 COUNT+=1
 if not b: raise AssertionError(COUNT)

@lru_cache(None)
def factors(n):
 out=[];p=2
 while p*p<=n:
  e=0
  while n%p==0:n//=p;e+=1
  if e:out.append((p,e))
  p+=1
 if n>1:out.append((n,1))
 return tuple(out)

def add(*args):
 d={}
 for a in args:
  for p,c in a:d[p]=d.get(p,Q(0))+c
 return tuple((p,c) for p,c in sorted(d.items()) if c)

def scale(a,c):return tuple((p,v*c) for p,v in a if v*c)
def sub(a,b):return add(a,scale(b,-1))
def const(a):return ((2,Q(a)),) if a else ()

@lru_cache(None)
def atom(p):
 if not p:return ()
 return add(tuple((a,-p*b) for a,b in factors(p.numerator)),tuple((a,p*b) for a,b in factors(p.denominator)))

def ent(ps):return add(*(atom(p) for p in ps if p))

def ln_interval(x,N=32):
 z=(x-1)/(x+1);z2=z*z;term=z;s=Q(0)
 for k in range(N):s+=2*term/(2*k+1);term*=z2
 return s,s+2*term/((2*N+1)*(1-z2))

LN2=ln_interval(Q(2))
@lru_cache(None)
def log_interval(p):
 if p==2:return Q(1),Q(1)
 k=p.bit_length()-1;a,b=ln_interval(Q(p,1<<k))
 return k+a/LN2[1],k+b/LN2[0]

@lru_cache(None)
def interval(a):
 lo=hi=Q(0)
 for p,c in a:
  l,h=log_interval(p)
  if c<0:l,h=h,l
  lo+=c*l;hi+=c*h
 return lo,hi

def nonnegative(a):return not a or interval(a)[0]>=0

@lru_cache(None)
def walsh(t):
 a=list(t);h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):u,v=a[j],a[j+h];a[j]=u+v;a[j+h]=u-v
  h*=2
 return tuple(Q(v,len(t)) for v in a)

@lru_cache(None)
def spectrum(t):return tuple(v*v for v in walsh(t))
@lru_cache(None)
def entropy(t):return ent(spectrum(t))

def restrict(t,i,b):
 return tuple(t[(z&((1<<i)-1))|((z>>i)<<(i+1))|(b<<i)] for z in range(len(t)//2))

def influences(t):
 n=len(t).bit_length()-1
 return tuple(Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n))

def table(labels,cores):
 return tuple(cores[labels[y]][x] for x in range(len(cores[0])) for y in range(len(labels)))

def child(state,i,b):
 labels,cores=state;k=len(labels).bit_length()-1
 if i<k:return restrict(labels,i,b),cores
 return labels,tuple(restrict(t,i-k,b) for t in cores)

def stats(state,validate=False):
 labels,cores=state;k=len(labels).bit_length()-1;m=len(cores[0]).bit_length()-1
 weights=tuple(Q(labels.count(j),len(labels)) for j in range(len(cores)))
 q=tuple(sum((weights[j]*spectrum(cores[j])[t] for j in range(len(cores))),Q(0)) for t in range(1<<m))
 T=add(*(scale(entropy(c),p) for c,p in zip(cores,weights)))
 F=table(labels,cores);HF=entropy(F);HQ=ent(q);J=sub(HQ,T);L=sub(HF,HQ)
 if validate:
  P=spectrum(F)
  marginal=tuple(sum(P[(t<<k)+s] for s in range(1<<k)) for t in range(1<<m))
  ck(q==marginal);ck(sum(q)==1);ck(nonnegative(J));ck(nonnegative(L))
  ck(nonnegative(sub(ent(weights),J)))
  conditional=add(*(scale(ent(P[(t<<k)+s]/q[t] for s in range(1<<k)),q[t]) for t in range(1<<m) if q[t]))
  ck(conditional==L)
  inf=influences(F);ck(nonnegative(sub(const(3*sum(inf[:k])),J)))
  data_inf=tuple(sum((p*influences(c)[i] for c,p in zip(cores,weights)),Q(0)) for i in range(m))
  ck(inf[k:]==data_inf)
 return {'J':J,'L':L,'T':T,'H':HF,'F':F,'k':k,'weights':weights}

def check_state(state):
 a=stats(state,True);n=len(a['F']).bit_length()-1
 for i in range(n):
  bs=[stats(child(state,i,b)) for b in (0,1)]
  ck(tuple(restrict(a['F'],i,b) for b in (0,1))==tuple(s['F'] for s in bs))
  delta={key:sub(a[key],scale(add(*(s[key] for s in bs)),Q(1,2))) for key in ['J','L','T','H']}
  ck(delta['H']==add(delta['T'],delta['J'],delta['L']))
  if i<a['k']:ck(not delta['T']);ck(nonnegative(delta['J']))
  else:
   ck(sub(sub(delta['H'],delta['T']),delta['L'])==delta['J'])
 return a

def fixture():
 labels=(0,0,0,1,1,1,2,2)
 p3=tuple(-1 if x==0 else 1 for x in range(8))
 maj=tuple(1 if x.bit_count()>=2 else -1 for x in range(8))
 p2=tuple(-1 if x%4==0 else 1 for x in range(8))
 cores=tuple(tuple((1 if z==0 else -1)*g[x] for z in range(2) for x in range(8)) for g in (p3,maj,p2))
 return labels,cores

def encode(a):return {str(p):str(c) for p,c in a}
def bounds(a):return [str(v) for v in interval(a)]

def history(state,policy):
 root=stats(state);sums={k:() for k in ['DATA','CONTROL','LEAFJ','LEAFH','DROP','LEAFT','LEAFL']};nodes=leaves=0
 def walk(st,weight,depth,path):
  nonlocal nodes,leaves
  a=stats(st);n=len(a['F']).bit_length()-1;k=a['k']
  if not n or depth==4:
   leaves+=1
   for key,target in [('J','LEAFJ'),('H','LEAFH'),('T','LEAFT'),('L','LEAFL')]:sums[target]=add(sums[target],scale(a[key],weight))
   return
  if policy==0:i=0
  elif policy==1:i=k if k<n else 0
  elif policy==2:i=(k if (depth+path)%2 and k<n else 0)
  else:i=n-1 if path%2 else 0
  nodes+=1;cs=[child(st,i,b) for b in (0,1)];bs=[stats(c) for c in cs]
  d=sub(a['J'],scale(add(*(s['J'] for s in bs)),Q(1,2)))
  typ='CONTROL' if i<k else 'DATA';sums[typ]=add(sums[typ],scale(d,weight))
  dh=sub(a['H'],scale(add(*(s['H'] for s in bs)),Q(1,2)));sums['DROP']=add(sums['DROP'],scale(dh,weight))
  for b,c in enumerate(cs):walk(c,weight/2,depth+1,2*path+b)
 walk(state,Q(1),0,0)
 ck(add(sums['DATA'],sums['CONTROL'],sums['LEAFJ'])==root['J'])
 ck(add(sums['DROP'],sums['LEAFH'])==root['H'])
 ck(add(sums['LEAFT'],sums['LEAFJ'],sums['LEAFL'])==sums['LEAFH'])
 ck(nonnegative(sums['CONTROL']));ck(nonnegative(sums['LEAFJ']))
 return {'policy':policy,'internal_nodes':nodes,'leaves':leaves,**{k:encode(v) for k,v in sums.items()}}

def main():
 roots=queries=0
 masks=(1,2) if PILOT else range(4)
 for labels in product(range(3),repeat=4):
  for ms in product(masks,repeat=3):
   cores=tuple(tuple(-1 if mask>>x&1 else 1 for x in range(2)) for mask in ms)
   check_state((labels,cores));roots+=1;queries+=3
  if time.perf_counter()-START>LIMIT:raise RuntimeError('frozen runtime limit')
 result={'status':'PASS','mode':'pilot' if PILOT else 'full','census_roots':roots,'census_queries':queries}
 if not PILOT:
  st=fixture();a=check_state(st);N=7;faces=0
  for assignment in product((-1,0,1),repeat=N):
   cur=st
   for i in range(N-1,-1,-1):
    if assignment[i]>=0:cur=child(cur,i,assignment[i])
   check_state(cur);faces+=1
   if time.perf_counter()-START>LIMIT:raise RuntimeError('frozen runtime limit')
  # Both source children stay nonconstant at the chosen DATA exposure.
  ck(len(set(spectrum(c) for c in st[1]))==3)
  for b in (0,1):
   for c in child(st,3,b)[1]:ck(len(set(c))==2)
  data=child(st,3,0);ab=stats(data);ac=[stats(child(data,0,b)) for b in (0,1)]
  d=sub(a['J'],scale(add(*(stats(child(st,3,b))['J'] for b in (0,1))),Q(1,2)))
  ctrl=sub(ab['J'],scale(add(*(s['J'] for s in ac)),Q(1,2)))
  ck(nonnegative(ctrl));ck(interval(a['J'])[0]>0)
  # Predetermined dummy-query depths: symbolic accounts only, no truth-table expansion.
  for depth in range(6):
   naive=scale(a['J'],depth+1);ck(sub(naive,a['J'])==scale(a['J'],depth))
  result.update({'fixture_partial_restrictions':faces,'fixture_root':{k:encode(a[k]) for k in ['H','J','T','L']},'fixture_root_J_bounds':bounds(a['J']),'first_DATA_debit':encode(d),'first_DATA_debit_bounds':bounds(d),'next_CONTROL_release':encode(ctrl),'histories':[history(st,p) for p in range(4)],'dummy_depths':list(range(6))})
 result['assertions']=COUNT;result['seconds']=round(time.perf_counter()-START,6)
 (RUN/'out'/('pilot.json' if PILOT else 'check.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ['histories','fixture_root','first_DATA_debit','first_DATA_debit_bounds','next_CONTROL_release','fixture_root_J_bounds']}))

if __name__=='__main__':main()
