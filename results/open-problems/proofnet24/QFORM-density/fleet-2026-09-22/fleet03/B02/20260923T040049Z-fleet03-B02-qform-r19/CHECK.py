import itertools
import math
import numpy as np

rng=np.random.default_rng(19023)
max_cb=0.0
max_delta=0.0
for trial in range(50):
    m=8
    C=rng.normal(size=(m,3))
    G=float(np.linalg.det(C.T@C))
    U,_=np.linalg.qr(C,mode='reduced')
    weights={}
    for R in itertools.combinations(range(m),3):
        d=float(np.linalg.det(U[list(R),:]))
        weights[R]=d*d
    max_cb=max(max_cb,abs(sum(weights.values())-1.0))
    delta=0.0
    Sdis=0.0
    for R,w in weights.items():
        dR=float(np.linalg.det(C[list(R),:]))
        for S,v in weights.items():
            if set(R).isdisjoint(S):
                delta += w*v
                dS=float(np.linalg.det(C[list(S),:]))
                Sdis += dR*dR*dS*dS
    max_delta=max(max_delta,abs(delta-Sdis/(G*G)))

direct=3*math.sqrt(math.e)
hybrid=2**(5/3)*3**0.25*math.exp(3/8)
print(f'max_cauchy_binet_weight_error={max_cb:.17g}')
print(f'max_disjoint_mass_identity_error={max_delta:.17g}')
print(f'direct_k3_constant={direct:.15f}')
print(f'partner_hybrid_constant={hybrid:.15f}')
assert max_cb < 1e-12
assert max_delta < 1e-12
assert abs(direct-4.946163812100385) < 1e-12
assert abs(hybrid-6.079353591267567) < 1e-12
print('STATUS=PASS')
