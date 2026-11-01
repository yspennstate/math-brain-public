"""Exact rational certificates for the explicit anisotropic example."""
from fractions import Fraction as F
import json
from pathlib import Path

def log_bounds(x,N=240):
    assert 0<x<=1
    z=(1-x)/(1+x)
    partial=sum((z**(2*k+1)/F(2*k+1) for k in range(N)),F(0))
    rem=2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
    return -2*partial-rem,-2*partial

def entropy_bounds(x):
    a,b=log_bounds(x);c,d=log_bounds(1-x)
    return -x*b-(1-x)*d,-x*a-(1-x)*c

rlo=F(223606797749978,10**14);rhi=F(223606797749980,10**14)
assert rlo*rlo<5<rhi*rhi
alo=(5-rhi)/10;ahi=(5-rlo)/10
blo=1-ahi;bhi=1-alo
dlo=(1-2/rlo)/2;dhi=(1-2/rhi)/2
# h(x) is increasing on (0,1/2), by its explicit derivative.
assert entropy_bounds(dlo)[0]>F(2066,10000)
assert -log_bounds(1-ahi/2)[0]<F(1488,10000)
assert -log_bounds(1-blo/2)[1]>F(449,1000)
assert entropy_bounds(ahi)[1]<F(5896,10000)
assert 3*alo-2>-F(1171,1000)
assert 3*blo-2>F(1708,10000)
C_lower=(F(2066,10000)-F(1171,1000)*F(1488,10000)+F(1708,10000)*F(449,1000))/2-F(5896,10000)
assert C_lower>-F(67,125)
assert -log_bounds(F(4,5))[0]<F(224,1000)
assert -log_bounds(F(1,2))[1]>F(693,1000)
D_lower=-F(25,256)*F(224,1000)+F(121,256)*F(693,2000)-F(55,256)*F(536,1000)
assert D_lower==F(13693,512000)
assert D_lower-F(23,10000)>F(1,50)
# A universal pair Lipschitz bound uses 4/sqrt(e)<5/2,
# hence 8/sqrt(e)<5; e>8/3>(8/5)^2.
assert F(1)+1+F(1,2)+F(1,6)+F(1,24)>F(8,3)>F(64,25)
res={'C_lower':str(C_lower),'Delta_zero_lower':str(D_lower),'Delta_for_epsilon_at_most_1e-4_lower':str(D_lower-F(23,10000)),'certified_Delta_gt':'1/50'}
Path(__file__).with_name('certificate.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
