"""Compare two eigensolvers on new matrices using the referee generator."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS"):
    os.environ[key]="1"
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from threadpoolctl import threadpool_limits
from referee_simulation import matrix,governor

rng=np.random.default_rng(5566778899)
results=[]
with threadpool_limits(limits=1):
    for n in (128,512,2000):
        governor()
        for ensemble in ("GOE","Rademacher"):
            a=matrix(rng,n,ensemble)
            lam,full=eigh(a,driver="evd",check_finite=False)
            for j in (0,n//2,n-1):
                w,v=eigh(a,subset_by_index=(j,j),driver="evr",check_finite=False)
                full_min=float(n**1.5*np.min(np.abs(full[:,j])))
                narrow_min=float(n**1.5*np.min(np.abs(v[:,0])))
                results.append(dict(n=n,ensemble=ensemble,j=j+1,evd=full_min,evr=narrow_min,
                                    difference=abs(full_min-narrow_min),
                                    eigenvalue_difference=float(abs(lam[j]-w[0]))))
Path(__file__).resolve().parents[1].joinpath("data/solver_comparison.json").write_text(json.dumps(results,indent=2)+"\n")
print("maximum scaled-minimum disagreement",max(r["difference"] for r in results))
