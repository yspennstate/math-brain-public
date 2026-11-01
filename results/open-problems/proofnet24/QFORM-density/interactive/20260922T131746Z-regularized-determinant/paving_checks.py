"""Finite checks of the partition constants and spectral transfer.
The universal partition existence is the cited MSS theorem, not this test.
"""
from pathlib import Path
import json
import math
import numpy as np
import sympy as sp

root=Path(__file__).resolve().parent
eta=(1/sp.sqrt(2)+1/sp.sqrt(32))**2
assert sp.simplify(eta-sp.Rational(25,32))==0
delta=sp.Rational(7,32)
assert sp.Rational(1,32)/delta==sp.Rational(1,7)
assert sp.Rational(1,7)<sp.Rational(1,2)
constant=96*math.e/(7*math.sqrt(2))
assert constant<27

# General noncommuting positive frame sums, including indefinite Lambda
# with very small extra eigenvalues. Test only the transfer, not existence.
rng=np.random.default_rng(2232)
cases=[]
for rank in [3,4,7]:
    for eps in [1e-2,1e-6,1e-10]:
        O,_=np.linalg.qr(rng.normal(size=(rank,rank)))
        S=O@np.diag(rng.uniform(float(delta),1-float(delta),rank))@O.T
        H,_=np.linalg.qr(rng.normal(size=(rank,rank)))
        vals=np.array([1.,1.,-1.]+[eps*(-1.)**j for j in range(rank-3)])
        Lam=H@np.diag(vals)@H.T
        eig,U=np.linalg.eigh(S)
        Mhalf=(U*np.sqrt(eig))@U.T
        e2,U2=np.linalg.eigh(np.eye(rank)-S)
        Nhalf=(U2*np.sqrt(e2))@U2.T
        s=np.linalg.svd(Mhalf@Lam@Nhalf,compute_uv=False)
        assert s[2]>=float(delta)-1e-9
        cases.append({"rank":rank,"small_eigenvalue_scale":eps,"third_cross_singular_value":float(s[2])})
result={"status":"PASS","scope":"exact partition-constant algebra and 9 finite spectral-transfer cases; not proof of MSS or of the full conjecture", "delta":str(delta),"leverage_bound":"1/7","constant":constant,"spectral_transfer_cases":cases}
(root/'paving_check_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
