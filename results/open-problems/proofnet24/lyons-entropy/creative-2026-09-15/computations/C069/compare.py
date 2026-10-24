from explore import output,P
import numpy as np
rng=np.random.default_rng(6999)
J=np.ones((3,3))/3
worst=(0,None)
for k in range(30000):
 p=rng.uniform(.005,.995,3)
 nu=rng.dirichlet(np.ones(6)); B=np.einsum('s,sij->ij',nu,P)
 delta=output(p,J)-output(p,B)
 ev=np.linalg.eigvalsh(delta)[0]
 if ev<worst[0]:worst=(ev,(p,B,np.linalg.eigh(delta)))
print(worst)
