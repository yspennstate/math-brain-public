import itertools,math,json,time
from pathlib import Path
import numpy as np
start=time.monotonic()
rows=[];worst3=0.;worst4=0.;worstmoment={k:0. for k in range(2,6)};Ngraphs=0;Nlaws=0;Ntuple3=0;Ntuple4=0;NB=0;nbworst=0.
for n in range(2,6):
 edges=list(itertools.combinations(range(n),2));m=len(edges);cache={}
 for mask in range(1<<m):
  parent=list(range(n))
  def root(x):
   while parent[x]!=x:x=parent[x]
   return x
  for e,(u,v) in enumerate(edges):
   if mask>>e&1:parent[root(u)]=root(v)
  comps={}
  for v in range(n):r=root(v);comps[r]=comps.get(r,0)|(1<<v)
  cache[mask]=list(comps.values())
 indicators=np.array([[(mask>>v)&1 for v in range(n)] for mask in range(1<<n)],dtype=float)
 sizes=indicators.sum(axis=1)
 for host in range(1,1<<m):
  A=np.zeros((n,n));neighbors=[[] for _ in range(n)]
  for e,(u,v) in enumerate(edges):
   if host>>e&1:A[u,v]=A[v,u]=1;neighbors[u].append(v);neighbors[v].append(u)
  lam=float(np.linalg.eigvalsh(A)[-1]);degree=int(A.sum(axis=1).max());B=min(degree-1,lam*lam/4) if degree>=2 else 0.;Ngraphs+=1
  # Exhaustive nonbacktracking row-count checks for lengths 1..8.
  if degree>=2:
   state={(u,u,v):1 for u in range(n) for v in neighbors[u]}
   for length in range(1,9):
    counts=np.zeros(n)
    for (u,prev,v),amount in state.items():counts[u]+=amount
    ratio=float(counts.max()/(4*B**length));nbworst=max(nbworst,ratio)
    assert ratio<=1+1e-10,(n,host,length,ratio)
    NB+=n
    nxt={}
    for (u,prev,v),amount in state.items():
     for w in neighbors[v]:
      if w!=prev:key=(u,v,w);nxt[key]=nxt.get(key,0)+amount
    state=nxt
  for p in [0.2,0.5,0.7/lam]:
   if p>=1:continue
   mass=np.zeros(1<<n);ehost=host.bit_count();sub=host
   while True:
    opens=sub.bit_count();prob=p**opens*(1-p)**(ehost-opens)
    for component in cache[sub]:mass[component]+=prob
    if sub==0:break
    sub=(sub-1)&host
   T=indicators.T@(mass[:,None]*indicators);chi=T.sum(axis=1)
   assert np.allclose(np.diag(T),1)
   joint3=np.einsum('s,si,sj,sk->ijk',mass,indicators,indicators,indicators,optimize=True)
   diag3=np.einsum('ia,ja,ka->ijk',T,T,T,optimize=True)
   joint4=np.einsum('s,si,sj,sk,sl->ijkl',mass,indicators,indicators,indicators,indicators,optimize=True)
   pair=(T[:,None,:]*T[None,:,:]).reshape(n*n,n)
   Q=(pair@T@pair.T).reshape(n,n,n,n)
   diag4=Q+Q.transpose(0,2,1,3)+Q.transpose(0,2,3,1)
   tol=3e-11
   assert np.all(joint3<=diag3+tol),(n,host,p,'triple')
   assert np.all(joint4<=diag4+tol),(n,host,p,'quadruple')
   worst3=max(worst3,float(np.max(joint3/np.maximum(diag3,1e-100))))
   worst4=max(worst4,float(np.max(joint4/np.maximum(diag4,1e-100))))
   Ntuple3+=n**3;Ntuple4+=n**4;Nlaws+=1
   F={k:float(mass@(sizes**k)) for k in range(2,6)}
   dmass={2:float(T.sum()),3:float(np.sum(chi**3)),4:float(3*(chi**2)@T@(chi**2)),5:float(15*np.sum(chi*(T@(chi**2))**2))}
   for k in range(2,6):
    assert F[k]<=dmass[k]+tol*max(1,dmass[k]),(n,host,p,k,'summed diagram')
    if degree<2:continue
    rho=max(p*lam,(p*lam)**(2/k)*(p*B)**(1-2/k))
    if rho>=1:continue
    M=4/(1-rho);diagramcount=math.prod(range(1,2*k-4,2)) if k>=3 else 1
    bound=n*diagramcount*M**(2*k-3)
    ratio=F[k]/bound;worstmoment[k]=max(worstmoment[k],ratio)
    assert ratio<=1+tol,(n,host,p,k,'moment')
rows.append(dict(graphs=Ngraphs,laws=Nlaws,triple_tuples=Ntuple3,quadruple_tuples=Ntuple4,nonbacktracking_rows=NB,max_joint3_over_diagram=worst3,max_joint4_over_diagram=worst4,max_row_bound_ratio=nbworst,max_moment_ratios=worstmoment))
# Weighted path product maximum: random paths and exact maximizing endpoint weights.
rng=np.random.default_rng(1042);prodmax=0.;eqerr=0.
for h in range(1,13):
 for it in range(80):
  w=np.exp(rng.normal(0,1,h));A=np.diag(w,1)+np.diag(w,-1);lam=np.linalg.eigvalsh(A)[-1]
  ratio=float(np.prod((w/lam)**2)*4**(h-1));prodmax=max(prodmax,ratio);assert ratio<=1+1e-10
 w=np.full(h,0.5)
 if h==1:w[0]=1.
 else:w[0]=w[-1]=1/math.sqrt(2)
 lam=float(np.linalg.eigvalsh(np.diag(w,1)+np.diag(w,-1))[-1]);ratio=float(np.prod((w/lam)**2)*4**(h-1));eqerr=max(eqerr,abs(ratio-1));assert abs(ratio-1)<1e-12
result=dict(exhaustive=rows[0],weighted_paths=dict(random_count=960,max_ratio=prodmax,equality_family_max_error=eqerr),elapsed_seconds=time.monotonic()-start)
Path('second_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
