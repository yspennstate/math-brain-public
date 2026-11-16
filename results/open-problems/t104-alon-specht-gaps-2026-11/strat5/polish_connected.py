"""NUMERICAL: move retained frames a tiny distance toward the complete graph."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
import json
import numpy as np
from stratum import closed,direct,matrices,ratio
for filename in ('connected_floor_0.001.json','connected_floor_1e-06.json'):
    data=json.load(open(filename))
    raw=data['best']
    u=np.array(raw['frame'])
    a,b=raw['a'],raw['b']
    z=matrices(a,b,u)[4]
    floor=data['floor']
    factor=min(1.,(.1-floor-2e-12)/(.1-min(z)))
    a*=factor
    b*=factor
    lam,_,_,L,z=matrices(a,b,u)
    terms=closed(a,b,u)
    check=direct(a,b,u)
    assert min(z)>floor and lam>a
    assert max(abs(terms-check))<1e-12
    record=dict(a=a,b=b,ratio=float(ratio(terms)),minimum_weight=float(min(z)),floor_margin=float(min(z)-floor),
                terms=terms.tolist(),direct_terms=check.tolist(),spectrum=np.linalg.eigvalsh(L).tolist(),
                orthogonality_error=float(np.max(np.abs(u.T@u-np.eye(2)))))
    data['polished_best']=record
    with open(filename,'w') as out:json.dump(data,out,indent=2)
    print('NUMERICAL:',filename,record,flush=True)
