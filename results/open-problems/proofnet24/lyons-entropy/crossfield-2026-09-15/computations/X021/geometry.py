import numpy as np
from scipy.optimize import linprog

def atoms(K):
 n=len(K); eye=np.eye(n)
 return np.array([np.linalg.det(np.column_stack([K[:,j] if mask>>j&1 else (eye-K)[:,j] for j in range(n)])).real for mask in range(1<<n)])

def coordinates(B):
 return np.array([B[i,i].real for i in range(3)]+[np.sqrt(2)*B[i,j].real for i,j in [(0,1),(0,2),(1,2)]]+[np.sqrt(2)*B[i,j].imag for i,j in [(0,1),(0,2),(1,2)]])

def matrix(v):
 B=np.diag(v[:3]).astype(complex)
 for l,(i,j) in enumerate([(0,1),(0,2),(1,2)]):
  B[i,j]=(v[3+l]+1j*v[6+l])/np.sqrt(2); B[j,i]=B[i,j].conjugate()
 return B

def data(K):
 p=atoms(K); neglog=-np.log(p); c=[]
 for k in range(3):
  r=[j for j in range(3) if j!=k]; x=1<<r[0]; y=1<<r[1]
  c.append(neglog[x+y]-neglog[x]-neglog[y]+neglog[0])
 tau=sum((-1)**(3-mask.bit_count())*neglog[mask] for mask in range(8))
 M=np.diag(c)+tau*K; gs=[]; ws=[]
 for k in range(3):
  R=[j for j in range(3) if j!=k]; a=K[k,k].real
  for s in [0,1]:
   g=K[:,k] if s else (np.eye(3)-K)[:,k]
   pi=a if s else 1-a
   rr=a-(1-s); v=K[R,k]
   J=K[np.ix_(R,R)]-np.outer(v,v.conjugate())/rr
   q=atoms(J); omega=2+(q[1]+q[2])/np.sqrt(q[0]*q[3])
   gs.append(g); ws.append(omega/pi)
 G=np.column_stack([coordinates(np.outer(g,g.conjugate())) for g in gs]); w=np.array(ws)
 return dict(p=p,c=np.array(c),tau=tau,M=M,gs=gs,ws=w,G=G)

def probe(K):
 d=data(K); G=d['G']; m=coordinates(d['M']); co,res,rank,sv=np.linalg.lstsq(G,3*m,rcond=None)
 print('K=',K);print('eigK=',np.linalg.eigvalsh(K));print('c,tau=',d['c'],d['tau']);print('span rank residual=',rank,np.linalg.norm(G@co-3*m));print('coefficients / caps=',co/d['ws']);
 # Homogeneous support comparison with all Hermitian B, bounded for witness extraction.
 cost=np.r_[-3*m,d['ws']]; ub=np.column_stack([G.T,-np.eye(6)])
 r=linprog(cost,A_ub=ub,b_ub=np.zeros(6),bounds=[(-1,1)]*9+[(0,None)]*6,method='highs')
 B=matrix(r.x[:9]); q=G.T@r.x[:9]
 print('min difference=',r.fun,'eigB=',np.linalg.eigvalsh(B),'quadratics=',q,'trMB=',np.trace(d['M']@B).real)
 print('B=',B)
 return d,B,r

if __name__=='__main__':
 for K in [np.array([[.2,.1,.05],[.1,.6,.1],[.05,.1,.8]],complex), np.array([[.2,.1,.05j],[.1,.6,.1],[-.05j,.1,.8]],complex), np.array([[.5,.1,0],[.1,.22,.1],[0,.1,.8]],complex)]:
  probe(K)
