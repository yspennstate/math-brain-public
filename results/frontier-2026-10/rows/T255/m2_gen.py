# audit 2 of the m=2 reduction, through the matrix generator (gen.py): drift and QV of w = tr(PV) at random PD 2x2 V
import numpy as np
from gen import bdrift, noise_basis
rng=np.random.default_rng(11); P=np.eye(2)-0.5; worst=0
for g2 in (0.2,0.5,0.9,1.0):
    c=g2*(2-g2)
    for _ in range(400):
        A=rng.standard_normal((2,2))*np.exp(rng.uniform(-2,3)); V=A@A.T+1e-3*np.eye(2)
        w=np.trace(P@V)
        dr=np.trace(P@bdrift(V,g2)); qv=sum(np.trace(P@E)**2 for E in noise_basis(V,g2,att=True,lin=True))
        e1=abs(dr-g2/4*w**3)/max(1e-12,g2/4*w**3); e2=abs(qv-(2*c*w**2+g2**2*w**4))/(2*c*w**2+g2**2*w**4)
        worst=max(worst,e1,e2)
print("max relative error of drift and QV of w against the 1D law:",worst)
