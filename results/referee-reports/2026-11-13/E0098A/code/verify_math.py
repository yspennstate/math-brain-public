"""Independent checks of the Gaussian constant, spherical density, and numerics."""
import os
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import json
import math
from pathlib import Path
import numpy as np
from scipy.special import gammaln, erf
from scipy.linalg import eigh
from simulate import matrix

ROOT=Path(__file__).resolve().parents[1]
c=math.sqrt(2/math.pi)
audit={'rate_from_density':c, 'rate_from_cdf_difference':float(erf(1e-7/math.sqrt(2))/1e-7),
       'spherical_small_box_bounds':[], 'independent_eigensolver':[]}
for n in (32,128,512,2048,8192):
    for r in (1,2,3,4):
        t=1.
        # Density of sqrt(n) times r coordinates of a uniform unit vector.
        density=math.exp(gammaln(n/2)-gammaln((n-r)/2)-r/2*math.log(math.pi*n))
        upper=(2*t)**r*density  # bounds on n**r * P(all r coordinates <= t/n)
        lower=upper*math.exp((n-r-2)/2*math.log1p(-r*t*t/n**3))
        audit['spherical_small_box_bounds'].append(dict(n=n,r=r,lower=lower,upper=upper,
                                                       predicted_limit=(c*t)**r))
for ensemble in ('goe','rademacher','bernoulli_p010'):
    for n in (128,512):
        rng=np.random.default_rng(980099+n)
        a=matrix(rng,n,ensemble)
        full_vals,full_vectors=eigh(a,driver='evd',check_finite=False)
        for index in (0,n//2,n-1):
            vals,vectors=eigh(a,subset_by_index=(index,index),driver='evr',check_finite=False)
            v,w=vectors[:,0],full_vectors[:,index]
            error=float(np.max(np.abs(np.abs(v)-np.abs(w))))
            minimum_error=float(n**1.5*abs(np.min(np.abs(v))-np.min(np.abs(w))))
            assert error<1e-10 and minimum_error<1e-6
            audit['independent_eigensolver'].append(dict(ensemble=ensemble,n=n,index=index+1,
                eigenvalue_error=float(abs(vals[0]-full_vals[index])),
                absolute_coordinate_max_error=error,scaled_minimum_error=minimum_error))
(ROOT/'data/math_audit.json').write_text(json.dumps(audit,indent=2))
print('rate',c,'cdf difference',audit['rate_from_cdf_difference'])
print('max independent scaled minimum error',max(x['scaled_minimum_error'] for x in audit['independent_eigensolver']))
