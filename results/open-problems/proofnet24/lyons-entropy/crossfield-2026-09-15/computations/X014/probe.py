import numpy as np,itertools,json
from pathlib import Path

def matchings(edges):
 out=[]
 for b in itertools.product([0,1],repeat=len(edges)):
  s=[i for i,x in enumerate(b) if x]
  v=[j for i in s for j in edges[i]]
  if len(v)==len(set(v)):out.append(s)
 return out

def calc(w,edges):
 m=len(w);t=np.array(list(itertools.product([-1.,1.],repeat=m))); q=np.ones(len(t));d=np.zeros((len(t),m));dd=np.zeros((len(t),m,m))
 for M in matchings(edges):
  if not M:continue
  tm=np.prod(t[:,M],axis=1);q+=np.prod(w[M])*tm
  for i in M:
   d[:,i]+=np.prod(w[[j for j in M if j!=i]])*tm
   for j in M:
    if i!=j:dd[:,i,j]+=np.prod(w[[k for k in M if k not in [i,j]]])*tm
 if min(q)<=0:return None
 F=np.mean(q*np.log(q));g=np.mean(d*np.log(q[:,None]),axis=0);h=np.einsum('ti,tj,t->ij',d,d,1/q)/len(t)+np.einsum('tij,t->ij',dd,np.log(q))/len(t)
 hz=4*np.sqrt(w[:,None]*w[None,:])*h+2*np.diag(g)
 return dict(F=F,g=g,h=h,hz=hz,minq=min(q))

rng=np.random.default_rng(7);results=[]
for edges in [[(0,1),(1,2),(2,3)],[(0,1),(1,2),(2,3),(3,4)],[(0,1),(1,2),(2,3),(3,4),(4,5)],[(0,1),(1,2),(1,3),(3,4),(3,5)]]:
 n=1+max(max(e) for e in edges); best=[np.inf,None];bestz=[np.inf,None]
 for rep in range(1200):
  a=np.exp(rng.uniform(-4,2,len(edges)));B=np.zeros((n,n))
  for x,(i,j) in zip(a,edges):B[i,j]=B[j,i]=x
  a*=rng.uniform(.5,.9999)/np.linalg.norm(B,2);w=a*a;r=calc(w,edges)
  ev=np.linalg.eigvalsh(r['h'])[0];evz=np.linalg.eigvalsh(r['hz'])[0]
  if ev<best[0]:best=[float(ev),w.tolist()]
  if evz<bestz[0]:bestz=[float(evz),w.tolist()]
 results.append(dict(edges=edges,weight_hessian=best,amplitude_hessian=bestz))
print(json.dumps(results,indent=2));Path(__file__).with_name('probe.json').write_text(json.dumps(results,indent=2))
