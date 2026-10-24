import os
for option in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[option]='1'
import json
import pathlib
import numpy as np
from scipy.optimize import root

here=pathlib.Path(__file__).resolve().parent
laws=[('point-mass',[2.],[1.]),('symmetric',[-1.,1.],[.5,.5]),('three-atom',[-1.,0.,3.],[.2,.6,.2]),('zero-third-nonzero-fifth',[-2.,1.,3.],[.4,.5,.1])]
records=[]
for name,locations,masses in laws:
    x=np.array(locations)
    p=np.array(masses)
    mean=float(p@x)
    y=x-mean
    mu2,mu3,mu5=[float(p@y**k) for k in (2,3,5)]
    coefficient=5*mu5-22*mu2*mu3
    errors=[]
    for variance in (100.,400.,1600.):
        def equations(z):
            u,r=z
            den=r+(u-y)**2/variance
            return [float(p@(1/den))-1,float(p@((u-y)/den**2))]
        result=root(equations,[-2*mu3/variance,1-mu2/variance],tol=1e-12)
        assert np.max(np.abs(equations(result.x)))<1e-11
        u,r=result.x
        shift=u+float(p@((u-y)/(r+(u-y)**2/variance)))
        scaled_second=(shift+3*mu3/variance)*variance**2
        error=abs(scaled_second-coefficient)
        errors.append(error)
        records.append({'law':name,'t':variance,'mu2':mu2,'mu3':mu3,'mu5':mu5,'mode':mean+shift,'scaled_second_coefficient':scaled_second,'predicted_second_coefficient':coefficient,'absolute_coefficient_error':error,'equation_residual':float(np.max(np.abs(equations(result.x))))})
    if abs(coefficient)+abs(mu3)>1e-10:
        assert errors[-1]<errors[0], (name,errors)
(here/'mode_boundary_measurements.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print(json.dumps({'cases':len(records),'last_time_results':[record for record in records if record['t']==1600]}))
