import numpy as np
rng=np.random.default_rng(9009)
n=3;masks=np.arange(8);X=((masks[:,None]>>np.arange(n))&1);sg=2*X-1

def mat(p):
 der=np.stack([sg[:,i]*(p+p[masks^(1<<i)]) for i in range(n)],axis=1)
 J=der.T@(der/p[:,None]);C=np.zeros((3,3))
 for i in range(n):
  for j in range(i):
   ids=masks[((masks&(1<<i))==0)&((masks&(1<<j))==0)]
   a,b,c,d=p[ids],p[ids^(1<<i)],p[ids^(1<<j)],p[ids^(1<<i)^(1<<j)]
   C[i,j]=C[j,i]=np.sum((a+b+c+d)*np.log(b*c/(a*d)))
 return J-C

def atoms(a,b,c,u,v):
 leaves=(a**X[:,0]*(1-a)**(1-X[:,0]))*(c**X[:,2]*(1-c)**(1-X[:,2]))
 q=b-u*sg[:,0]/np.where(X[:,0],a,1-a)-v*sg[:,2]/np.where(X[:,2],c,1-c)
 return leaves*np.where(X[:,1],q,1-q)

if __name__=='__main__':
 worst=1e9;wbase=1e9;wder=1e9; neg=None
 for it in range(20000):
  a,b,c=rng.uniform(.005,.995,3); u,v=rng.uniform(0,1,2)
  cap=min(b/(u/a+v/c),(1-b)/(u/(1-a)+v/(1-c)))
  u*=cap*rng.uniform(.001,.999999);v*=cap*rng.uniform(.001,.999999)
  p=atoms(a,b,c,u,v)
  if min(p)<=0:continue
  M=mat(p);B=np.diag([1/(a*(1-a)),1/(b*(1-b)),1/(c*(1-c))])
  mine=np.linalg.eigvalsh(M)[0];base=np.linalg.eigvalsh(M-B)[0]
  der=np.linalg.eigvalsh((M-mat(atoms(a,b,c,u*.9999,v*.9999)))/.0001)[0]
  worst=min(worst,mine);wbase=min(wbase,base);wder=min(wder,der)
  if base<-.0001 and neg is None:neg=(a,b,c,u,v,base)
 print({'n':20000,'min_hessian':worst,'min_baseline':wbase,'min_radial':wder,'baseline_counterexample':neg})
