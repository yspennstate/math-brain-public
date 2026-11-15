"""NUMERICAL feasibility repair and reference checks for retained candidates."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import json
import numpy as np
from scipy.linalg import helmert
from terms import terms

def main():
    data=json.load(open('optimized.json'))
    for rec in data:
        W=np.array(rec['best']['W'])
        if 'both' in rec['name']:
            m=5 if rec['name'].startswith('5') else 4
            # Apply a uniform complete-graph addition inside the carrier, then
            # normalize. Top multiplicity two is preserved exactly in the model.
            L=np.diag(W[:m,:m].sum(1))-W[:m,:m]
            lm=np.linalg.eigvalsh(L)[-1]
            eps=1e-8
            W[:m,:m]=(1-eps)*W[:m,:m]+eps*lm/m*(np.ones((m,m))-np.eye(m))
            if m==4:W[4:,4:] *= 1-eps
            W/=W.sum()/2
        D,x1,x2,x3,y=terms(W)
        ev=np.linalg.eigvalsh(np.diag(W.sum(1))-W)
        rec['polished']=dict(W=W.tolist(),D=D,terms=[x1,x2,x3,y],T=x1+x2+x3-y,quotient=(x1+x2+x3-y)/(x1+x2+x3),eigenvalues=ev.tolist(),min_weight=float(np.min(W)))
        assert D==2 and np.min(W)>=0
        print('NUMERICAL',rec['name'],rec['polished']['quotient'])
    json.dump(data,open('polished.json','w'),indent=2)
if __name__=='__main__':main()
