import numpy as np
from itertools import product
rng=np.random.default_rng(78)
best=(1,None)
for it in range(15000):
 U,_=np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
 ev=np.clip(rng.beta(.12,.12,3),1e-12,1-1e-12); K=(U*ev)@U.conj().T
 a=np.diag(K).real;q=a*(1-a);s=np.sqrt(q);D=np.diag(q**(-.25));T=D@(K-np.diag(a))@D
 atoms=np.array(list(product((0,1),repeat=3)))
 mu=np.prod(np.where(atoms,a,1-a),axis=1);Y=(atoms-a)/s
 p=np.array([((-1)**(3-sum(x))*np.linalg.det(K-np.diag(1-x))).real for x in atoms])
 L=-np.array([np.sum(mu*np.prod(Y[:,[j,k]],axis=1)*np.log(p/mu)) for j,k in [(1,2),(2,0),(0,1)]])
 z=np.sum(mu*np.prod(Y,axis=1)*np.log(p/mu))
 def accel(v):
  e=v[:3]+1j*v[3:]
  return 2*np.sum(L*abs(e)**2)+4*z*np.real(T[1,2]*e[1]*e[2]+T[2,0]*e[2]*e[0]+T[0,1]*e[0]*e[1])
 M=np.array([[(accel(np.eye(6)[i]+np.eye(6)[j])-accel(np.eye(6)[i]-np.eye(6)[j]))/4 for j in range(6)] for i in range(6)])
 mn=np.linalg.eigvalsh(M)[0]
 if mn<best[0]:best=(mn,(K,L,z,np.linalg.eigh(M)))
 if mn< -1e-6:break
print('best',best)
