import numpy as np,json,pathlib,math
from fractions import Fraction
rng=np.random.default_rng(59)
rows=[]
for d in [2,3,4,8,16,32,64,128,256]:
 u=np.cos(2*np.pi*np.arange(d)/d)
 ek=2*np.sum((u-u.mean())**2)
 em=np.sum((u-np.roll(u,1))**2)
 ratio=ek/em;expected=1/(2*math.sin(math.pi/d)**2)
 assert abs(ratio/expected-1)<1e-10
 rows.append({'degree':d,'slow_mode_distortion':float(ratio),'exact_formula':expected})
exact=0
for d in range(2,21):
 u=[Fraction(int(x),7) for x in rng.integers(-20,21,size=d)]
 z=Fraction(3,11)
 lhs=d*sum((x-z)**2 for x in u)
 rhs=sum((x-y)**2 for x in u for y in u)/2+(sum(u)-d*z)**2
 assert lhs==rhs
 # Arbitrary clique current lift, including non-gradient circulation.
 j=[[Fraction(0) for _ in range(d)] for _ in range(d)]
 for i in range(d):
  for k in range(i+1,d):j[i][k]=Fraction(int(rng.integers(-5,6)),9);j[k][i]=-j[i][k]
 b=[sum(x) for x in j]
 star=sum(x*x for x in b)/2
 clique=Fraction(d,2)*sum(j[i][k]**2 for i in range(d) for k in range(i+1,d))
 assert star<=clique
 jmin=[[(b[i]-b[k])/d for k in range(d)] for i in range(d)]
 assert all(sum(jmin[i])==b[i] for i in range(d))
 assert Fraction(d,2)*sum(jmin[i][k]**2 for i in range(d) for k in range(i+1,d))==star
 exact+=1
# Global multigraphs: loops and parallel edges included, no planarity needed for identity.
def add(L,i,j,c):
 if i!=j:L[i,i]+=c;L[j,j]+=c;L[i,j]-=c;L[j,i]-=c
checks=[]
for n in [3,5,8,12]:
 edges=[(i,i+1) for i in range(n-1)]
 edges += [(int(rng.integers(n)),int(rng.integers(n))) for _ in range(2*n)]
 m=len(edges);L=np.zeros((n+m,n+m));inc=np.zeros((n,m))
 for e,(v,w) in enumerate(edges):
  add(L,v,n+e,2);add(L,w,n+e,2);inc[v,e]+=1;inc[w,e]+=1
 schur=L[n:,n:]-L[n:,:n]@np.linalg.solve(L[:n,:n],L[:n,n:])
 C=np.zeros((m,m))
 for v in range(n):C+=2*np.outer(inc[v],inc[v])/inc[v].sum()
 np.fill_diagonal(C,0)
 K=np.diag(C.sum(axis=1))-C
 error=float(np.max(np.abs(K-schur)));assert error<1e-12
 assert C.sum(axis=1).max()<=4+1e-12
 def resistance(A,i,j):
  ids=[k for k in range(len(A)) if k!=j];b=np.zeros(len(ids));b[ids.index(i)]=1
  return np.linalg.solve(A[np.ix_(ids,ids)],b)[ids.index(i)]
 rfull=resistance(L,n,n+m-1);rk=resistance(K,0,m-1)
 assert abs(rfull-rk)<1e-10
 checks.append({'centers':n,'edges':m,'loops':sum(v==w for v,w in edges),'schur_error':error,'full_resistance':rfull,'trace_resistance':rk,'max_weighted_degree':float(C.sum(axis=1).max())})
result={'scope':'deterministic trace identities; not Boltzmann simulation','exact_star_and_flow_cases':exact,'cycle_distortion':rows,'global_multigraphs':checks}
pathlib.Path('star_mesh_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result,indent=2))
