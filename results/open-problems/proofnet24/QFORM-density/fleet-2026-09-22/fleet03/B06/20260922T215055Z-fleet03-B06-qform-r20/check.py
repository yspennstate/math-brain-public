import math
import numpy as np

rng=np.random.default_rng(20260922)
max_rel=0.0
for nl,nr in [(3,4),(5,6),(9,7)]:
    for _ in range(250):
        alpha=float(rng.normal())
        if abs(alpha)<0.05:
            alpha += 0.1 if alpha>=0 else -0.1
        b=rng.normal(size=nr-1)
        c=rng.normal(size=nl-1)
        D=rng.normal(size=(nl-1,nr-1))
        Z=np.block([[np.array([[alpha]]),b[None,:]],[c[:,None],D]])
        M=alpha*D-np.outer(c,b)
        x0=float(rng.normal()); x=rng.normal(size=nl-1)
        y0=float(rng.normal()); y=rng.normal(size=nr-1)
        X=x0+c@x/alpha
        Y=y0+b@y/alpha
        lhs=np.r_[x0,x]@Z@np.r_[y0,y]
        rhs=alpha*X*Y+x@(M/alpha)@y
        rel=abs(lhs-rhs)/(1.0+abs(lhs))
        max_rel=max(max_rel,rel)

bank=1067/2000
m0=math.sqrt(bank)
C_A=8/(3**(3/4))
endpoint=8*math.exp(3/8)/(3**0.25)
current=4*endpoint*m0**(-0.25)
gap=abs((complex(math.cos(1),math.sin(1))-1)/1j-1)

print(f'max_schur_identity_relative_error={max_rel:.17g}')
print(f'm0={m0:.15f}')
print(f'C_A={C_A:.15f}')
print(f'weighted_endpoint_prefactor={endpoint:.15f}')
print(f'current_branch_prefactor={current:.15f}')
print(f'nonuniform_characteristic_gap={gap:.15f}')
assert max_rel < 1e-11
assert current < 38.269
assert gap > 0.486
print('QFORM_B06_R20_CHECK_PASS')
