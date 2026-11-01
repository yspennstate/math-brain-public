import math,json,itertools,pathlib
checks=[]
# Finite component mass transport: enumerate all labelled trees up to n=6 using Pruefer codes.
count=0
for n in range(1,7):
 codes=[()] if n<=2 else itertools.product(range(n),repeat=n-2)
 for code in codes:
  adj=[set() for _ in range(n)]
  if n==2:adj[0].add(1);adj[1].add(0)
  elif n>2:
   deg=[1]*n
   for v in code:deg[v]+=1
   for v in code:
    leaf=next(i for i in range(n) if deg[i]==1)
    adj[leaf].add(v);adj[v].add(leaf);deg[leaf]-=1;deg[v]-=1
   a,b=[i for i in range(n) if deg[i]==1];adj[a].add(b);adj[b].add(a)
  def side(u,v):
   seen={u};stack=[u]
   while stack:
    z=stack.pop()
    for w in adj[z]:
     if (z==u and w==v) or w in seen:continue
     seen.add(w);stack.append(w)
   return len(seen)
  matrix=[[0]*n for _ in range(n)]
  for u in range(n):
   for v in adj[u]:matrix[u][v]=int(side(u,v)>side(v,u))
   matrix[u][u]=len(adj[u])-sum(matrix[u])
  received=[sum(matrix[u][v] for u in range(n)) for v in range(n)]
  expected=[]
  for u in range(n):
   sizes=[side(v,u) for v in adj[u]]
   expected.append(0 if all(2*x<n for x in sizes) else 1 if any(2*x==n for x in sizes) else 2)
  assert received==expected,(n,code,received,expected)
  assert sum(len(a) for a in adj)-2*n+2==0
  count+=1
checks.append({'check':'finite centroid transport and Euler defect','trees':count,'max_vertices':6,'passed':True})
# Independent site percolation validates the infinite branching-excess expression.
errors=[]
for d in [3,4,5,7]:
 for p in [.05,.2,.4,.6,.8,.95]:
  q=0.
  for _ in range(100000):
   nq=1-p+p*q**(d-1)
   if abs(nq-q)<1e-14: q=nq;break
   q=nq
  finite_density=p*q**d
  finite_edge=p*p*q**(2*d-2)
  f=finite_density-d/2*finite_edge
  B=d*p*p-2*p+2*f
  s=1-q
  rhs=p*sum(max(k-2,0)*math.comb(d,k)*s**k*(1-s)**(d-k) for k in range(d+1))
  errors.append(abs(B-rhs))
assert max(errors)<1e-10
checks.append({'check':'Bernoulli branching-excess identity','cases':len(errors),'maximum_error':max(errors),'passed':True})
# Poisson one-point augmentation: exact count ratio.
for ell in [.01,.1,1,5]:
 for n in range(1,20):
  old=math.exp(-ell)*ell**n/math.factorial(n)
  augmented=math.exp(-ell)*ell**(n-1)/math.factorial(n-1)
  assert math.isclose(augmented,old*n/ell,rel_tol=1e-12)
checks.append({'check':'Poisson augmentation count density N/ell','cases':76,'passed':True})
pathlib.Path('checks.json').write_text(json.dumps(checks,indent=2),encoding='utf8');print(json.dumps(checks,indent=2))
