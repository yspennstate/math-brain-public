import itertools,json,time,math
from fractions import Fraction as F
from pathlib import Path
START=time.perf_counter(); checks=0
def ck(x):
 global checks
 checks+=1
 assert x
def walsh(v):
 v=v[:]; h=1
 while h<len(v):
  for i in range(0,len(v),2*h):
   for j in range(i,i+h):
    a,b=v[j],v[j+h];v[j],v[j+h]=a+b,a-b
  h*=2
 return v
def rho(m,k): return F(m+1,m*k*(k+1))
def traces(m):
 for k in range(1,m+1):
  for gs in itertools.combinations(range(1,m+1),k):
   for bs in itertools.product(range(3),repeat=k):
    # 0: common only; 1: private only; 2: both
    A=0
    for g,b in zip(gs,bs):
     if b!=1:A|=1
     if b!=0:A|=1<<g
    yield (gs,bs),A,rho(m,k)/math.comb(m,k)/3**k
def output_formula(m,A):
 t=(A>>1).bit_count()
 if not A&1:return rho(m,t)/math.comb(m,t)/3**t
 if not t:return sum((rho(m,k)/3**k for k in range(1,m+1)),F(0))
 return sum((math.comb(m-t,u)*rho(m,t+u)/math.comb(m,t+u)/3**(t+u)*((2**t-1) if u==0 else 2**t) for u in range(m-t+1)),F(0))
def length(q):
 k=0
 while F(1,2**k)>q:k+=1
 return k
def forest(key):
 gs,bs=key
 B={g:({0} if b==0 else {g} if b==1 else {0,g}) for g,b in zip(gs,bs)}
 A=set().union(*B.values());owned={g:{j for j in A if g==min(h for h in gs if j in B[h])} for g in gs}
 used=sorted(g for g in gs if owned[g]);adj={g:[h for h in used if g!=h and owned[g]&{0,h}] for g in used}
 reach={}
 for g in used:
  r={g};todo=[g]
  while todo:
   for h in adj[todo.pop()]:
    if h not in r:r.add(h);todo.append(h)
  reach[g]=r
 comps=[];left=set(used)
 while left:
  g=min(left);c={h for h in left if h in reach[g] and g in reach[h]};comps.append(c);left-=c
 roots=sorted(min(c) for c in comps if not any(h in adj[g] for g in used if g not in c for h in c))
 seen=set(roots);todo=roots[:];edges=[]
 while todo:
  g=todo.pop(0)
  for h in adj[g]:
   if h not in seen:seen.add(h);todo.append(h);edges.append((g,h,min(owned[g]&{0,h})))
 ck(seen==set(used));ck(len(roots)+len(edges)==len(used))
 for g,h,j in edges:ck(j in owned[g] and j in {0,h})
 ck(set().union(*(owned[g] for g in used))==A)
 return roots,edges
def canonical_code(items):
 rows=sorted((length(q),key,q) for key,q in items)
 code=0;prev=0;book={}
 for le,key,q in rows:
  code<<=le-prev; ck(code<2**le)
  book[key]=format(code,'0'+str(le)+'b') if le else ''
  ck(F(1,2**le)<=q)
  if le:ck(q<F(1,2**(le-1)))
  code+=1;prev=le
 return book
summary={}
for m in range(1,9):
 vals=[1 if ((x&1) and (x>>1)!=0) else -1 for x in range(2**(m+1))]
 w=walsh(vals);P=[F(z*z,4**(m+1)) for z in w]
 ck(sum(P)==1)
 for S,p in enumerate(P):ck(p==((1-F(1,2**m))**2 if S==1 else F(1,4**m)))
 influence=sum((s.bit_count()*p for s,p in enumerate(P)),F(0))
 ck(influence==1+F(m-1,2**m))
 for j in range(m+1):
  physical=F(sum(vals[x]!=vals[x^(1<<j)] for x in range(len(vals))),len(vals))
  ck(physical==sum((p for s,p in enumerate(P) if s&(1<<j)),F(0)))
 ck(sum((rho(m,k) for k in range(1,m+1)),F(0))==1)
 # Exact analytic upper estimates without logarithms.
 for t in range(1,m+1):
  ck(t*(t+1)<=2**(2*m)); ck(math.comb(m,t)<=2**m)
  lower=rho(m,t)/math.comb(m,t)/3**t
  ck(lower>=F(1,2**(3*m+2*t)))
 rare_bound=F(8*m*2**m-6*m,4**m)
 ck(rare_bound<=4);ck(influence>=1)
 summary[str(m)]={'I':str(influence),'rare_cost_upper_bound_bits':str(rare_bound)}
for m in range(1,7):
 out={};tuples=[];mass=F(0)
 for key,A,q in traces(m):
  mass+=q;out[A]=out.get(A,F(0))+q;tuples.append((key,q))
  gs,bs=key;ck(len(gs)==len(set(gs)));ck(A>0)
  forest(key)
 ck(len(tuples)==4**m-1);ck(mass==1);ck(len(out)==2**(m+1)-1)
 for A,q in out.items():ck(q==output_formula(m,A))
 ck(out[1]>=F(1,6))
 if m<=4:
  book=canonical_code(tuples);trie={}
  for key,bits in book.items():
   node=trie
   for bit in bits:
    ck('key' not in node);node=node.setdefault(bit,{})
   ck(not node);node['key']=key
  for key,bits in book.items():
   node=trie
   for bit in bits:node=node[bit]
   ck(node['key']==key)
  ck(sum((F(1,2**len(s)) for s in book.values()),F(0))<=1)
  # Output codebook sums the exact ambiguity fibers before assigning lengths.
  obook=canonical_code(list(out.items()))
  ck(sum((F(1,2**len(s)) for s in obook.values()),F(0))<=1)
 summary['dictionary_'+str(m)]={'traces':len(tuples),'outputs':len(out),'total_mass':str(mass),'common_singleton_mass':str(out[1])}
for a in range(1,4):
 n=a+2**a; vals=[1 if x&(1<<(a+(x&(2**a-1)))) else -1 for x in range(2**n)]
 P=[F(w*w,4**n) for w in walsh(vals)]
 target={T|(1<<(a+u)) for u in range(2**a) for T in range(2**a)}
 ck({s for s,p in enumerate(P) if p}==target)
 for s in target:ck(P[s]==F(1,4**a))
 ck(sum((s.bit_count()*p for s,p in enumerate(P)),F(0))==1+F(a,2))
 ck(len(target)==4**a) # fixed 2a bits: gate address once + control subset
summary['assertions']=checks;summary['seconds']=time.perf_counter()-START
ck(summary['seconds']<60)
path=Path(__file__).resolve().parents[1]/'out'/'CHECK.json';path.write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,indent=2))
