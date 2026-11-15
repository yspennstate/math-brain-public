"""Search small Rademacher matrices; certify every reported zero exactly."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","VECLIB_MAXIMUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.linalg import eigh
from threadpoolctl import threadpool_limits
from referee_simulation import governor

x=sp.Symbol("x")
rng=np.random.default_rng(1123581321)
records=[]
with threadpool_limits(limits=1):
    for n in (8,12,16,24,32,64):
        m=3000
        flagged=repeated=zero=unconfirmed=0
        witness=None
        for trial in range(m):
            if trial%100==0: governor()
            b=rng.integers(0,2,size=(n,n))*2-1
            b=np.triu(b)+np.triu(b,1).T
            lam,u=eigh(b.astype(float),check_finite=False)
            tiny=np.any(np.abs(u)<1e-11,axis=1)
            suspected_repeat=np.min(np.diff(lam))<1e-9
            if not tiny.any() and not suspected_repeat: continue
            flagged+=1
            a=sp.Matrix(b.tolist()); p=a.charpoly(x).as_poly()
            if sp.gcd(p,p.diff()).degree():
                repeated+=1
                continue
            certified=False
            for i in np.flatnonzero(tiny):
                q=a.minor_submatrix(int(i),int(i)).charpoly(x).as_poly()
                common=sp.gcd(p,q)
                if common.degree():
                    certified=True
                    if witness is None:
                        witness=dict(trial=trial,coordinate=int(i)+1,matrix=b.tolist(),
                                     characteristic_polynomial=str(p.as_expr()),
                                     minor_polynomial=str(q.as_expr()),common_factor=str(common.as_expr()))
                    break
            if certified: zero+=1
            else: unconfirmed+=1
        record=dict(n=n,matrices=m,candidate_matrices=flagged,confirmed_repeated=repeated,
                    confirmed_simple_with_zero=zero,unconfirmed_candidates=unconfirmed,
                    probability_simple_with_zero=zero/m,
                    confirmed_exists_some_zero_eigenvector=(zero+repeated)/m)
        records.append(record)
        print(json.dumps(record),flush=True)
        record["witness"]=witness
Path(__file__).resolve().parents[1].joinpath("data/small_zero_search.json").write_text(json.dumps(
    dict(seed=1123581321,numerical_trigger=1e-11,repetitions=3000,
         caveat="All positives exact-certified; floating trigger is not an exact proof of negative cases.",
         results=records),indent=2)+"\n")
