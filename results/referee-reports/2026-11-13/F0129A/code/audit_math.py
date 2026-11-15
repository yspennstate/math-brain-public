#!/usr/bin/env python3
"""Independent scalar checks of the kernel normalization and covariance obstruction."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[key]='1'
from fractions import Fraction
from pathlib import Path
import csv
import json
import math
import numpy as np
from scipy.integrate import quad

ROOT=Path(__file__).resolve().parents[1]

def f(name,x):
    r=abs(x)
    if r==0 or r>=1 or name=='zero':return 0.
    sign=1 if x>0 else -1
    if name=='sign':v=1.
    elif name=='spline':
        q=2*r;v=3*(2*q-1.5*q*q) if q<1 else 1.5*(2-q)**2
    elif name=='bump':
        z=1-r*r;v=2*r/z**2*math.exp(1-1/z)
    else:
        def piece(a,b):return 6*(r-a)*(b-r)/(b-a)**3 if a<r<b else 0.
        if name=='annular':v=piece(.5,1)
        elif name=='two_bump':v=.5*piece(.1,.4)+.5*piece(.65,1.)
        else:raise ValueError(name)
    return sign*v

def main():
    c=[Fraction(1),Fraction(-1),Fraction(1)]
    K=[[1,1,0],[1,1,1],[0,1,1]]
    q=sum(c[i]*K[i][j]*c[j] for i in range(3) for j in range(3))
    assert q==-1
    rows=[]
    for name in ['zero','sign','spline','bump','annular','two_bump']:
        val,err=quad(lambda x:f(name,x),0,1,points=[.1,.4,.5,.65],epsabs=1e-12)
        assert abs(val-(name!='zero'))<1e-10
        for x in np.linspace(-1.1,1.1,1001):
            assert abs(f(name,x)+f(name,-x))<1e-12 and x*f(name,x)>=0
        for h in [.05,.025]:
            grid=h*sum(f(name,j*h) for j in range(1,round(1/h)+1))
            rows.append(dict(kernel=name,dx=h,positive_integral=val,quadrature_error_estimate=err,
                             grid_positive_integral=grid))
    with (ROOT/'data'/'kernel_checks.csv').open('w') as out:
        w=csv.DictWriter(out,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    result=dict(annular_quadratic_form=str(q),annular_covariance_eigenvalues=np.linalg.eigvalsh(K).tolist(),
                analytic_annular_integral=str(Fraction(48)*Fraction(1,2)**3/Fraction(6)),
                all_parity_and_repulsion_checks=True)
    (ROOT/'data'/'math_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
