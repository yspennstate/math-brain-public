import sys,numpy as np
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'X006'))
from explore import data

def mats(K):
 Ns=[]
 for k in range(3):
  a=K[k,k].real;v=K[:,k].copy();v[k]=0;R=[j for j in range(3) if j!=k];vv=K[R,k]
  W=[]
  for s in [0,1]:
   J=K[np.ix_(R,R)]-np.outer(vv,vv.conj())/(a-(1-s))
   x=np.linalg.det(np.eye(2)-J).real;w=np.linalg.det(J).real
   y=J[0,0].real-w;z=J[1,1].real-w
   T=(y+z)/(2*np.sqrt(x*w))
   W.append(2*(1+T))
  c,tau=W[0],W[1]-W[0]
  eta=(c+tau*(1-a))/(a*(1-a))
  N=eta*np.outer(v,v.conj());N[k,k]=c+tau*a
  N[:,k]+=tau*v;N[k,:]+=tau*v.conj();Ns.append(N)
 return Ns
if __name__=='__main__':
 rng=np.random.default_rng(15017);res=[]
 for i in range(1000):
  z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));U,_=np.linalg.qr(z)
  ev=1/(1+np.exp(-rng.normal(size=3)*5));K=(U*ev)@U.conj().T
  try:
   d=data(K);N=sum(mats(K))/3
   vals=np.linalg.eigvalsh(N-d['M']);res.append((vals[0],K,vals,d['tau'],d['c'],ev))
  except Exception: pass
 print(min(res,key=lambda x:x[0]))
