"""Finite exact-spectrum checks of PEER_TAIL_EXTENSION.md; not proof certification."""
import json
import math
from pathlib import Path
import numpy as np
from check_stability import hadamard, volume_data

rows=[]
for m in (256,512):
    N=m-2
    U=hadamard(m)/math.sqrt(m)
    s=np.r_[1.,1.,np.full(N,1/math.sqrt(N))]
    M=(U*s)@U.T
    Z,alpha,W,actual=volume_data(M)
    T2=float((actual[2:]**2).sum())
    assert abs(T2-1)<1e-11
    assert actual[2] <= 1/math.sqrt(N)+1e-11
    assert max(alpha)<2/3
    assert T2/actual[2]**2 >=225-1e-9
    assert Z >=1-1e-10
    assert np.max(abs(M))**2 <1/64
    # Eigenvalues of [[0,M],[M,0]] are exactly +-singular values(M).
    assert actual[1]>=1-1e-11
    pref=9*math.sqrt(3)*math.e/2
    rows.append({'m':m,'n_full':2*m,'tail_count':N,'tail_stable_rank':T2/actual[2]**2,
        's3':float(actual[2]),'T2':T2,'E3':Z,'max_alpha':float(max(alpha)),
        'max_physical_pair_determinant':float(np.max(abs(M))**2),
        'uniform_density_bound':pref,'sharper_E3_bound':pref*Z**(-1/6)})
out={'status':'PASS','scope':'Two finite matrix instances and exact-spectrum formula; no full-conjecture or independent analytic verification','cases':rows,'full_conjecture_verified':False}
Path(__file__).with_name('tail_check_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
