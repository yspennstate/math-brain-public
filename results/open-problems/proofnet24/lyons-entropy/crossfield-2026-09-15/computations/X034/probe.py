import numpy as np,itertools,json

def atoms(K):
 n=len(K)
 out=[]
 for b in itertools.product((0,1),repeat=n):
  Q=K-np.diag(1-np.array(b));p=np.linalg.det(Q).real*(-1)**(n-sum(b))
  out.append((b,p,np.linalg.inv(Q)))
 return out
rng=np.random.default_rng(3401)
results=[]
for n in (3,4,5):
 mins=1.;maxs=-1.;worst=None
 for j in range(500):
  U=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))[0]
  K=(U*rng.uniform(.005,.995,n))@U.conj().T
  a=K[0,0].real;k=K[1:,0];R=K[1:,1:]
  F=np.zeros((n-1,n-1),complex)
  for b,p,Y in atoms(R):
   q=a-np.vdot(k,Y@k).real
   F+=p*np.log(q/(1-q))*Y
  e=np.linalg.eigvalsh(F)
  if e.max()>maxs: maxs=e.max();worst=(K,e)
  mins=min(mins,e.min())
 results.append((n,mins,maxs))
 if maxs>1e-10:
  np.savez('computations/X034/arrow_counterexample_%d.npz'%n,K=worst[0],eigenvalues=worst[1])
print(results)
json.dump(results,open('computations/X034/probe_results.json','w'))
