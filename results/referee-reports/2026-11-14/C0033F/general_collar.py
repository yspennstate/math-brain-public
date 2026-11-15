"""General disconnected collar: Q=[[a,sqrt(x)v*],[sqrt(x)v,C]]."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import mpmath as mp
from mp_core import tr,scaled_solve

def block_atoms(C):
 b,c=mp.re(C[0,0]),mp.re(C[1,1]);r2=abs(C[0,1])**2
 return [(1-b)*(1-c)-r2,b*(1-c)+r2,(1-b)*c+r2,b*c-r2]

def block_data(C,v):
 pi=block_atoms(C);ks=[]
 for s in range(4):
  M=C-mp.diag([int(not(s&1)),int(not(s&2))]);ks.append(mp.re((v.H*(M**-1)*v)[0]))
 alt=ks[0]-ks[1]-ks[2]+ks[3]
 b,c=mp.re(C[0,0]),mp.re(C[1,1]);r=C[0,1]
 # L2 is isolated--block-coordinate 0, L3 is isolated--coordinate 1.
 L2=abs((1-c)*v[0]+r*v[1])**2/(pi[0]*pi[1])
 L3=abs(mp.conj(r)*v[0]+(1-b)*v[1])**2/(pi[0]*pi[2])
 T=mp.diag([L3,L2])+alt*C
 K=mp.log(pi[1]*pi[2]/(pi[0]*pi[3]))
 return pi,ks,T,K

def bases2():
 return [mp.matrix([[1,0],[0,0]]),mp.matrix([[0,0],[0,1]]),mp.matrix([[0,1],[1,0]]),mp.matrix([[0,1j],[-1j,0]])]

def limit(C,v,details=False):
 pi,ks,T,K=block_data(C,v);B=bases2();gs=[]
 for s in range(4):
  M=C-mp.diag([int(not(s&1)),int(not(s&2))]);Mi=M**-1
  gs.append([pi[s]*mp.re(tr(Mi*A)) for A in B])
 F=mp.matrix([[sum(gs[s][i]*gs[s][j]/pi[s] for s in range(4)) for j in range(4)] for i in range(4)])
 # 2 det A = 2ab - 2c^2 - 2d^2.
 D=mp.matrix([[0,1,0,0],[1,0,0,0],[0,0,-2,0],[0,0,0,-2]])
 N=F-K*D;detT=mp.re(mp.det(T));Ti=T**-1
 z=mp.matrix([mp.re(tr(Ti*A)) for A in B])
 w=K*detT*(z.T*scaled_solve(N,z))[0];m0=1/(1+w)
 if details:return dict(m0=m0,w=w,T=T,K=K,N=N,pi=pi,k=ks,z=z)
 return m0

def block(e0,e1,angle):
 c,s=mp.cos(angle),mp.sin(angle);U=mp.matrix([[c,-s],[s,c]])
 return U*mp.diag([e0,1-e1])*U.T

def kernel(a,C,v,x):
 Q=mp.zeros(3);Q[0,0]=a
 for i in range(2):
  Q[i+1,0]=mp.sqrt(x)*v[i];Q[0,i+1]=mp.conj(Q[i+1,0])
  for j in range(2):Q[i+1,j+1]=C[i,j]
 return Q

if __name__=='__main__':
 from mp_core import evaluate
 mp.mp.dps=140
 C=block(mp.mpf('.07'),mp.mpf('.13'),mp.mpf('.61'));v=mp.matrix([mp.cos(mp.mpf('.37')),mp.sin(mp.mpf('.37'))*mp.exp(mp.j*mp.mpf('1.1'))])
 m0=limit(C,v);print('m0',mp.nstr(m0,35))
 for a in map(mp.mpf,['.002','.3','.999']):
  for x in map(mp.mpf,['1e-8','1e-16','1e-32']):
   ev=evaluate(kernel(a,C,v,x));print(a,x,mp.nstr(ev['margin'],35),'error/x',mp.nstr((ev['margin']-m0)/x,15))

def parameters(a,C):
 """Uniform, v-independent parameters of Theorem 2 in REPORT.md."""
 pi=block_atoms(C);p=min(pi);K=mp.log(pi[1]*pi[2]/(pi[0]*pi[3]));alpha=a*(1-a)
 omega=p*(-mp.expm1(-K))/2
 mu=min(mp.mpf('0.01'),alpha*p,K,omega/alpha,abs(C[0,1])**2/4)
 return dict(pi_min=p,K=K,alpha=alpha,omega=omega,mu=mu,
             remainder_radius=mu**9/mp.mpf('2e18'),
             collar_x=mu**15/(mp.mpf('2e30')*(2*K+3)))
