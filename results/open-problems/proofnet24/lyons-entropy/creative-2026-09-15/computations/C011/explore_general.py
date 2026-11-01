import numpy as np
import itertools
atoms=np.array(list(itertools.product([0.,1.], repeat=3)))

def det_atoms(K):
 out=[]
 for x in atoms:
  Q=K-np.diag(1-x)
  out.append((-1)**int(3-x.sum())*np.linalg.det(Q).real)
 return np.array(out)

def calc(K):
 p=det_atoms(K)
 if min(p)<=0: return None
 f=-np.log(p)
 def val(bits): return f[int(bits[0]*4+bits[1]*2+bits[2])]
 tau=0
 for x in atoms: tau+=(-1)**int(3-x.sum())*val(x)
 d=[]
 for i in range(3):
  j,k=[z for z in range(3) if z!=i]
  e=np.eye(3)
  d.append(val(e[j]+e[k])-val(e[j])-val(e[k])+val([0,0,0]))
 d=np.array(d)
 M=np.diag(d)+tau*K
 if np.linalg.eigvalsh(M)[0]<=1e-13: return None
 delta=np.linalg.det(M).real
 raw=[]
 for x in atoms:
  raw.append((sum(d[j]*d[k]*x[i] for i,j,k in [(0,1,2),(1,0,2),(2,0,1)])+tau*sum(d[k]*x[i]*x[j] for i,j,k in [(0,1,2),(0,2,1),(1,2,0)])+tau*tau*x.prod())/delta)
 g=np.array(raw); g-=p@g
 h=(2*atoms-1).prod(1); h-=p@h
 V=p@g**2; cov=p@(g*h); vh=p@h**2
 J=2*K-np.eye(3)
 # adjugate stable polynomial
 G=2*(J@J-np.trace(J)*J+((np.trace(J)**2-np.trace(J@J))/2)*np.eye(3))
 den=delta*vh+np.trace(M@G@M@G).real
 b=-delta*cov/den
 obj=delta*V-delta*delta*cov*cov/den
 u=np.array([3.,np.trace(M@G).real])
 J2=np.array([[delta*V+3,delta*cov+u[1]],[delta*cov+u[1],den]])
 opt=3-u@np.linalg.solve(J2,u)
 return obj, tau, d, b, p, opt

if __name__ == "__main__":
 rng=np.random.default_rng(211)
 best=(-1,None)
 for j in range(100000):
  if j<30000:
   a=rng.random()
   b=rng.uniform(max(-a/2,a-1),min(1-a,a/2))
   K=np.eye(3)*(a-b)+b*np.ones((3,3))
  else:
   Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
   Q,_=np.linalg.qr(Z)
   lam=rng.beta(.2,.2,3)
   K=(Q*lam)@Q.conj().T
  out=calc(K)
  if out is None: continue
  if out[0]>best[0]: best=(out[0],(K,out))
  if out[0]>1.001:
   print('FAIL',j,repr(K),out);break
 else: print('PASS')
 print('BEST',best)
