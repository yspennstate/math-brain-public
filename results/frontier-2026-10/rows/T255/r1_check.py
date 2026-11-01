# rank-one stratum V = lam u u^T: check lam drift = lam^3 f(u), du = (g2 lam^2 beta/(2 m tau0^2)) Pi_perp(u o u), against bdrift
import numpy as np
from gen import bdrift
rng=np.random.default_rng(3); tau0=1.0; worst=0
for m in (2,3,4,6):
    P=np.eye(m)-1.0/m
    for g2 in (0.3,1.0):
        for _ in range(200):
            u=rng.standard_normal(m); u/=np.linalg.norm(u); lam=np.exp(rng.uniform(-1,3))
            V=lam*np.outer(u,u); b=bdrift(V,g2)
            Pu=P@u; d=Pu*Pu-(Pu@Pu)/m; beta=u@d
            f=g2/tau0**2*((Pu@Pu)**2/m**2+beta*np.sum(u**3)/m)
            w=u*u-np.sum(u**3)*u; du=g2*lam**2*beta/(2*m*tau0**2)*w
            pred=lam**3*f*np.outer(u,u)+lam*(np.outer(du,u)+np.outer(u,du))
            worst=max(worst,np.max(abs(pred-b))/np.max(abs(b)))
print("rank-one drift decomposition, max rel err:",worst)
for m in (2,3,4,8):
    print("m",m,"explosion iff gamma^2 <",(m*m-m-1)/(2*(m-1)))
