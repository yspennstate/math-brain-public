import numpy as np
from math import log,sqrt
rng=np.random.default_rng(270702)
def data(r):
 T=sum(r);q0=(1-4*T)/8;q=np.r_[q0,q0+T-r]
 m=np.array([log(q[(i+1)%3+1]*q[(i+2)%3+1]/(q0*q[i+1])) for i in range(3)])
 v=np.sqrt(r);z=np.r_[r,2*v[1]*v[2],2*v[2]*v[0],2*v[0]*v[1]]
 E=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)/4
 B=np.hstack((E,np.zeros((4,3))))-z
 F=2*(B.T/q)@B
 return q,m,F

def Hneg(F,m):
 Q=np.zeros((6,6))
 for k,(i,j) in enumerate([(1,2),(2,0),(0,1)]): Q[i,j]=Q[j,i]=m[k];Q[k+3,k+3]=-2*m[k]
 return F-Q
mins=np.ones(3)*1e100;worst=[None]*3
for _ in range(20000):
 r=rng.dirichlet([.25,.25,.25])*.25*(1-10**rng.uniform(-10,0))
 q,m,F=data(r);d=r/4+np.array([r[1]*r[2],r[2]*r[0],r[0]*r[1]])
 for kind,mm in enumerate([m,d/sqrt(np.prod(q)),d/sqrt(np.prod(q))/sqrt(3)]):
  val=np.linalg.eigvalsh(Hneg(F,mm))[0]
  if val<mins[kind]:mins[kind]=val;worst[kind]=(r.tolist(),q.tolist(),mm.tolist(),val)
print('Min eigenvalues actual, upper, upper/sqrt3: ',mins)
for x in worst:print(x)
