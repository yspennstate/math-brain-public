from fractions import Fraction as F
from itertools import product,permutations
from math import comb,factorial
from pathlib import Path
import json,time,hashlib
start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x
def fwht(a):
 a=a[:];h=1
 while h<len(a):
  for b in range(0,len(a),2*h):
   for j in range(b,b+h):
    x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
  h*=2
 return a
def actual_runs(m,A):
 coords=[j for j in range(m+1) if A>>j&1]
 supports={g:1|(1<<g) for g in range(1,m+1)}
 choices=[list(supports) if j==0 else [j] for j in coords]
 for tau in product(*choices):
  owned={g:sum(1<<j for j,h in zip(coords,tau) if h==g) for g in set(tau)}
  used=sorted(owned);adj={g:[h for h in used if h!=g and owned[g]&supports[h]] for g in used}
  reach={g:{g}|set(adj[g]) for g in used}
  for _ in used:
   reach={g:set().union(*(reach[h] for h in reach[g])) for g in used}
  left=set(used);scc=[]
  while left:
   g=min(left);c={h for h in left if h in reach[g] and g in reach[h]};scc.append(c);left-=c
  sources=[sorted(c) for c in scc if not any(h in adj[g] for g in used if g not in c for h in c)]
  for roots0 in product(*sources):
   roots=tuple(sorted(roots0));nonroot=[g for g in used if g not in roots]
   parents=[[g for g in used if h in adj[g]] for h in nonroot]
   for par0 in product(*parents):
    par=dict(zip(nonroot,par0));valid=True
    for h in nonroot:
     visited=set();g=h
     while g not in roots:
      if g in visited:valid=False;break
      visited.add(g);g=par[g]
     if not valid:break
    if not valid:continue
    atts=[[j for j in coords if owned[par[h]]&supports[h]&(1<<j)] for h in nonroot]
    for att0 in product(*atts):
     att=dict(zip(nonroot,att0));groups=[]
     for g in used:
      for j in coords:
       hs=[h for h in nonroot if par[h]==g and att[h]==j]
       if hs:groups.append((g,j,hs))
     for perms in product(*(list(permutations(hs)) for g,j,hs in groups)):
      children={g:[] for g in used}
      for (g,j,hs),seq in zip(groups,perms):children[g]+=[(j,h) for h in seq]
      queue=list(roots);trace=[]
      while queue:
       g=queue.pop(0);trace.append((g,owned[g],tuple(children[g])));queue.extend(h for j,h in children[g])
      ck(len(trace)==len(used));yield roots,tuple(trace)
def residual_monomial(m,A,roots,trace):
 base=F(1)
 for g,B,ch in trace:
  s=B.bit_count();k=(A&(1|(1<<g))).bit_count();base*=F(s,k)
  if B&1:base*=1
  if B>>g&1:base*=F(1+bool(A&1),2)
 power=0
 while base<F(1):base*=2;power+=1
 ck(base==1)
 return power,F(1,m**len(trace)*4**len(roots))
def run_probability(m,roots,trace,a):
 D=(1+F(1,4*m))**m-1;prob=F(1,(4*m)**len(roots))/D
 for g,B,ch in trace:
  s=B.bit_count();c=len(ch)
  prob*=F(1,s*(s+1))
  if s==1:prob*=(1 if B&1 else a)/(1+a)
  else:ck(s==2)
  prob*=F(1,(c+1)*(c+2)*comb(s+c-1,c))*F(1,m**c)
 return prob
summary={'source_claim':'A006-SUNFLOWER-POSTERIOR-FOREST-PAYMENT@1','verdict':'HOLDS_AT_STATED_SCOPE_NO_REPAIR','counts':{}}
for m in range(1,9):
 vals=[1 if x&1 and x>>1 else -1 for x in range(2**(m+1))]
 P=[F(z*z,4**(m+1)) for z in fwht(vals)]
 for A,p in enumerate(P):ck(p==((1-F(1,2**m))**2 if A==1 else F(1,4**m)))
 I=sum((A.bit_count()*p for A,p in enumerate(P)),F(0));ck(I==1+F(m-1,2**m))
 for j in range(m+1):ck(F(sum(vals[x]!=vals[x^(1<<j)] for x in range(len(vals))),len(vals))==sum((p for A,p in enumerate(P) if A>>j&1),F(0)))
 ck(F(m*m,2**m)+F(11*m,5*2**m)+F(4,5*2**m)<=F(23,10))
 ck(F(m*m+9*m+5,2**m)<=F(15,2))
 ck(F(1,4)<=(1+F(1,4*m))**m-1<F(1,3))
 if m>5:continue
 total=0
 for A in range(1,2**(m+1)):
  traces=list(actual_runs(m,A));ck(len(traces)==len(set(traces)))
  total+=len(traces);poly={}
  for roots,trace in traces:
   exp,co=residual_monomial(m,A,roots,trace);poly[exp]=poly.get(exp,F(0))+co
  t=(A>>1).bit_count()
  if not A&1:expected={t:F(1,(4*m)**t)};count=1
  elif t==0:expected={0:F(1,4)};count=m
  else:
   expected={t-1:F(factorial(t),4*m**t)}
   if m>t:expected[t]=F((m-t)*factorial(t),4*m**(t+1))
   count=factorial(t)*(1+m-t)
  ck(poly==expected);ck(len(traces)==count)
  for a in [F(2,5),F(1,2)]:
   W=sum((run_probability(m,r,tr,a) for r,tr in traces),F(0));D=(1+F(1,4*m))**m-1
   if not A&1:closed=(a/(16*m*(1+a)))**t/D
   elif not t:closed=1/(16*(1+a)*D)
   else:
    wi=F(factorial(t),24*t*t*(t+1)*m**t)/D*(a/(4*(1+a)))**(t-1)
    wo=F((m-t)*factorial(t),8*m**(t+1)*(t+1)*(t+2))/D/(1+a)*(a/(4*(1+a)))**t
    closed=wi+wo
   ck(W==closed)
 summary['counts'][str(m)]=total
src=Path(__file__).resolve().parents[4]/'A006'/'runs'/'20261011T210855Z-fleet05-A006-posterior-forest-optimization'/'CLAIMS.json'
cl=json.loads(src.read_text(encoding='utf-8'))[0]
hashed=hashlib.sha256(json.dumps({'statement':cl['exact_statement'],'hypotheses':cl['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
ck(hashed==cl['statement_sha256']);summary['reviewed_statement_sha256']=hashed
summary['checks']=checks;summary['seconds']=time.perf_counter()-start;ck(summary['seconds']<60)
out=Path(__file__).resolve().parents[1]/'out'/'REVIEW_A006_CHECK.json';out.write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8');print(json.dumps(summary,indent=2))
