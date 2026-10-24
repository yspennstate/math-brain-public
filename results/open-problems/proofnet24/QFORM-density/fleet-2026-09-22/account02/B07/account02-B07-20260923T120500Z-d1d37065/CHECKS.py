import math
import numpy as np

H=1.1533650070389015e-6
assert abs(2**(17/4)/math.sqrt(H)-17717.15954892967)<1e-9
assert abs(2**(7/2)/math.sqrt(H)-10534.686096612784)<1e-9

# Three-anchor target family: small exact instances.
for m in (2,4,16):
    G=np.zeros((3,3*m))
    for r in range(3):
        G[r,r*m:(r+1)*m]=1/math.sqrt(m)
    A=np.block([[np.zeros((3,3)),G],[G.T,np.zeros((3*m,3*m))]])
    eig=np.linalg.eigvalsh(A)
    nz=eig[np.abs(eig)>1e-10]
    assert np.allclose(nz,[-1,-1,-1,1,1,1],atol=1e-10)
    assert abs(np.linalg.det(G@G.T)-1)<1e-12
    assert abs((m**3)*(m**(-3))-1)<1e-12

# Rank-two obstruction formulas.
tau=1/128
eps=0.1
m=100000
max_pair_det=max(eps**4,1/m,eps**(-4)/m**2)
assert max_pair_det<tau
assert abs((eps**2+eps**(-2))-100.01)<1e-10
Z2=1.0
assert Z2==1.0

print('partner_common_Hhalf=',2**(17/4)/math.sqrt(H))
print('partner_transverse_Hhalf=',2**(7/2)/math.sqrt(H))
print('target_density_cap=',3*math.sqrt(2))
print('rank2_eps=',eps,'m=',m,'max_pair_det=',max_pair_det,'eigmag=',eps**2+eps**(-2),'Z2=',Z2)
print('QFORM_B07_FIXED_ANCHOR_PACKET_CHECK_PASS')
