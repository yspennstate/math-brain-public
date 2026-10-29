import numpy as np
from scipy.integrate import quad
g2=0.2; tau=1.0; w0=1.0; D=4.0
kap=g2/(4*tau**2); k=g2/(2*tau); c=g2*(2-g2)
def P(eps, A):
    B=4*k*k; al=-2*eps/A; be=2*kap+2*eps*B/A
    sp=lambda y: y**(-al)*((A+B*y*y)/A)**(-be/(2*B))
    num=quad(sp,0,w0,limit=200)[0]
    den=num+quad(sp,w0,np.inf,limit=400)[0]
    return num/den
print("no MLP      ", P(0.0, 2*c))
print("MLP upper   ", P(0.0, 2*c+4*g2))
print("MLP lower   ", P(g2*D/4, 2*c+4*g2))
