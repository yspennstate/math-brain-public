import itertools, numpy as np

def cube(n):
 N=2**n
 L=np.zeros((N,N))
 for x in range(N):
  for i in range(n): L[x,x^(1<<i)]=1
  L[x,x]=-n
 return L

def quantities(p,theta,L):
 f=np.sqrt(p)*np.exp(-theta); g=np.sqrt(p)*np.exp(theta)
 v=g*(L@f)-f*(L@g)
 a=g*(L@L@f)+f*(L@L@g)-2*(L@f)*(L@g)
 fisher=np.dot(v,v/p)
 return fisher+np.dot(a,np.log(p)),fisher,a,v

if __name__=='__main__':
 rng=np.random.default_rng(9)
 for n in [1,2,3]:
  L=cube(n); best=(float('inf'),)
  for k in range(200):
   q=rng.normal(size=2**n)*2; p=np.exp(q)/np.exp(q).sum(); theta=rng.normal(size=2**n)*2
   B,I,a,v=quantities(p,theta,L)
   if B<best[0]:best=B,I,p.tolist(),theta.tolist()
  print(n,best)
