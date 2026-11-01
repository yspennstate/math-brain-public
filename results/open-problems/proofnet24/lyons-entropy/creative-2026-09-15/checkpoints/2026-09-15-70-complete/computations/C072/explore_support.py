import numpy as np
from itertools import combinations
w=np.arange(1.,7.); k=1/(1+w); v=w/(1+w); h=sum(v)
U=np.array([[1,0,1],[0,1,1],[1,1,0],[1,-1,1],[2,1,-1],[1,2,1]],dtype=float)
V=np.column_stack([U[:,0],U[:,1],U[:,2],U[:,0]+U[:,1],U[:,0]+U[:,2],U[:,1]+U[:,2]])
def calc(s):
 rho=s/(1+s*h); vs=np.column_stack((v,V)); q=[]; rr=[]; ps=[]
 for mask in range(64):
  x=np.array([(mask>>i)&1 for i in range(6)]);eps=2*x-1;b=np.where(x,k,1-k);p0=np.prod(b);T=vs.T@np.diag(eps/b)@vs
  ps.append(p0*(1+rho*T[0,0])); q.append([p0*(T[i,i]+rho*(T[0,0]*T[i,i]-T[0,i]**2)) for i in range(1,7)])
  rr.append([p0*(T[i,i]*T[j,j]-T[i,j]**2+rho*np.linalg.det(T[np.ix_([0,i,j],[0,i,j])])) for i,j in combinations(range(1,7),2)])
 q=np.array(q);ps=np.array(ps);rr=np.array(rr);G=q.T@np.diag(1/ps)@q;C=np.zeros((6,6))
 for m,(i,j) in enumerate(combinations(range(6),2)):C[i,j]=C[j,i]=-rr[:,m]@np.log(ps)
 H=G-C;D=(V.T@V)**2
 return G,C,H,D
for s in [1e2,1e4,1e6,2**32]:
 G,C,H,D=calc(s); print(s,'eigH',np.linalg.eigvalsh(H),'eigH-D',np.linalg.eigvalsh(H-D),flush=True)
