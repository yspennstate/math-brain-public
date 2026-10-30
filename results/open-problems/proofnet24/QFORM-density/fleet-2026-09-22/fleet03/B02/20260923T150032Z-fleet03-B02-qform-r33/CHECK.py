import math
import numpy as np

rng=np.random.default_rng(330150032)
mx=0.0
for _ in range(1000):
    a,u,v,b=rng.normal(size=4)
    r0=rng.normal(size=5)
    rho=rng.normal(size=5)
    c0=rng.normal(size=6)
    gamma=rng.normal(size=6)
    M=rng.normal(size=(6,5))
    K=b*M-np.outer(gamma,rho)
    det=a*b-u*v
    # C adj(P) R, P=[[a,u],[v,b]]
    CadjR=np.outer(b*c0-v*gamma,r0)+np.outer(-u*c0+a*gamma,rho)
    L=det*M-CadjR
    rhs=L+u*(v*M-np.outer(c0,rho))+np.outer(b*c0-v*gamma,r0)
    den=max(1.0,np.linalg.norm(a*K))
    mx=max(mx,np.linalg.norm(a*K-rhs)/den)

c=4/125
C_high=9*math.exp(5/9)*2**(-5/18)*c**(-1/18)
C04=5*2**(37/60)*3**(1/10)*math.sqrt(math.e)
print('instances=1000')
print('max_relative_identity_error=',repr(mx))
print('D5_direct_constant=',repr(5*math.sqrt(2*math.e)))
print('highrank_G_constant=',repr(C_high))
print('highrank_Z_constant=',repr(C_high*864**(1/6)))
print('rank1_Z_constant=',repr(38.541905462520745*864**(1/6)))
print('partner_base_constant=',repr(C04))
print('partner_highrank_G_constant=',repr(C04*c**(-1/20)))
print('partner_Z_constant=',repr(C04*c**(-1/20)*864**(3/20)))
