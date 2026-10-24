import numpy as np
from itertools import combinations
w=np.array([1.,2.,3.,4.,5.,6.])
k=1/(1+w); v=w/(1+w); h=sum(v)

def matrices(s,U):
 rho=s/(1+s*h); vs=np.column_stack((v,U)); q=[]; r=[]; ps=[]; xx=[]
 for mask in range(64):
  x=np.array([(mask>>i)&1 for i in range(6)]); eps=2*x-1; b=np.where(x,k,1-k); p0=np.prod(b)
  T=vs.T@np.diag(eps/b)@vs
  ps.append(p0*(1+rho*T[0,0])); xx.append(x)
  q.append([p0*(T[i,i]+rho*(T[0,0]*T[i,i]-T[0,i]**2)) for i in range(1,4)])
  r.append([p0*(T[i,i]*T[j,j]-T[i,j]**2+rho*np.linalg.det(T[np.ix_([0,i,j],[0,i,j])])) for i,j in combinations(range(1,4),2)])
 ps=np.array(ps); q=np.array(q); r=np.array(r); G=q.T@np.diag(1/ps)@q
 C=np.zeros((3,3))
 for z,(i,j) in enumerate(combinations(range(3),2)): C[i,j]=C[j,i]=-r[:,z]@np.log(ps)
 H=G-C
 xx=np.array(xx); mu=ps@xx; cov=(xx-mu).T@np.diag(ps)@(xx-mu)
 J1=(U*U).T@np.linalg.inv(cov)@(U*U)
 cnt=xx.sum(1); PN=np.bincount(cnt,weights=ps); QN=np.array([q[cnt==i].sum(0) for i in range(7)]); GN=QN.T@np.diag(1/PN)@QN
 return G,C,H,J1,GN

rng=np.random.default_rng(721)
for it in range(200):
 U=rng.integers(-2,3,size=(6,3)).astype(float)
 if np.linalg.matrix_rank(U)<3: continue
 U=U/np.linalg.norm(U,axis=0)
 G,C,H,J1,GN=matrices(3.,U)
 direction=np.array([1,1,-.03])
 f=direction@C@direction
 gap=direction@(C-J1)@direction
 if gap>.05 and np.linalg.eigvalsh(H)[0]>.03:
  print('it',it,'U',U.tolist(),'G',G,'C',C,'H',H,'eigH',np.linalg.eigvalsh(H),'f',f,'J1gap',gap,'countgap',direction@(C-GN)@direction,flush=True);break
else: print('no J1 failure')
U=np.array([[1,0,1],[0,1,1],[1,1,0],[1,-1,1],[2,1,-1],[1,2,1]],dtype=float)
G,C,H,J1,GN=matrices(3.,U)
print('fixed','G',G,'C',C,'H',H,'eigH',np.linalg.eigvalsh(H))
for a in [[1,1,-.001],[1,1,-.01],[1,1,-.1],[1,1,-1]]:
 a=np.array(a);print(a,'f',a@C@a,'I',a@G@a,'linear',a@J1@a,'count',a@GN@a)
