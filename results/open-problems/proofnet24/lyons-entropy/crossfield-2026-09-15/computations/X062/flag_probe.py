import numpy as np,itertools
rng=np.random.default_rng(62)
for n in [4,5,6]:
 V=np.linalg.qr(rng.normal(size=(n,3)))[0]
 U=[np.outer(v,v) for v in V]; t=np.sum(V*V,axis=1)
 W=np.zeros((3,3)); tau=0.; G=np.zeros((3,3));b={}; c={}
 for i,j in itertools.combinations(range(n),2):
  w=np.cross(V[i],V[j]); bb=w@w;b[i,j]=bb;c[i,j]=np.log(t[i]*t[j]/bb);W+=c[i,j]*np.outer(w,w)
 for T in itertools.combinations(range(n),3):
  r=np.linalg.det(V[list(T)])**2
  cc=np.log(np.prod([b[p] for p in itertools.combinations(T,2)])/(np.prod(t[list(T)])*r));tau+=r*cc
  for i in T:
   jk=tuple(j for j in T if j!=i)
   G+=r*(cc+c[jk])*U[i]/t[i]
 C=W+tau*np.eye(3)
 print(n,'tau',tau,'traces',np.trace(G),np.trace(C),'D',np.linalg.eigvalsh(G-C),'W',np.linalg.eigvalsh(W))
