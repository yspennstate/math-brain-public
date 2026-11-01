import numpy as np
rng=np.random.default_rng(81)
def g(R,B):
 D=np.linalg.norm(R[:,None]-B[None,:],axis=2); a=np.full(len(R),np.inf);b=np.full(len(B),np.inf)
 for ij in np.argsort(D,axis=None):
  i,j=divmod(int(ij),len(B))
  if np.isinf(a[i]) and np.isinf(b[j]): a[i]=b[j]=D[i,j]
 return a,b
for n in range(2,11):
 for t in range(500):
  R=rng.normal(size=(n,2));B=rng.normal(size=(n,2));a,b=g(R,B);aa,bb=g(np.vstack([R,rng.normal(size=(1,2))]),B)
  if (aa[:n]<a-1e-12).any() or (bb>b+1e-12).any():
   print('FAIL',n,t,'reds',a,aa[:n],'blues',b,bb);np.savez('insertion_failure.npz',R=R,B=B,a=a,b=b,aa=aa,bb=bb);raise SystemExit()
print('All colourwise comparative-static checks passed')
