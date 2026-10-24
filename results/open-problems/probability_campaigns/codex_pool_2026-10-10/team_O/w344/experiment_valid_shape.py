import os
for option in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[option]='1'
import json
import math
import pathlib
import numpy as np

here=pathlib.Path(__file__).resolve().parent
rng=np.random.default_rng(344)
records=[]
for n in (64,128,256):
    norms=[]
    for _ in range(12):
        upper=np.triu(rng.choice(np.array([-1,1],dtype=np.int8),size=(n,n)),1)
        matrix=upper+upper.T
        assert np.count_nonzero(matrix)==n*(n-1)
        norms.append(float(np.max(np.abs(np.linalg.eigvalsh(matrix.astype(float))))))
    mean=float(np.mean(norms))
    records.append({'n':n,'samples':12,'shape':'one edge, U={u}, V={v}, disjoint partition','sample_mean_norm':mean,'deterministic_lower_bound':math.sqrt(n-1),'old_frobenius_upper_bound':math.sqrt(n*(n-1)),'mean_over_sqrt_n':mean/math.sqrt(n),'old_bound_to_sample_mean':math.sqrt(n*(n-1))/mean})
(here/'valid_shape_measurements.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print(json.dumps(records))
