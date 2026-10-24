import os
for option in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[option]='1'
import json
import math
import pathlib
import numpy as np
from scipy.optimize import root

here=pathlib.Path(__file__).resolve().parent
# Geometric P(X=k)=2^(-k-1), k>=0, is unbounded and has all polynomial moments.
# A 160-point truncation is numerical evidence; tail control is recorded below.
x=np.arange(160,dtype=float)
p=2.**(-x-1)
mean=float(p@x)
y=x-mean
mu2,mu3,mu5=[float(p@y**k) for k in (2,3,5)]
assert abs(mean-1)<1e-14 and abs(mu2-2)<1e-13 and abs(mu3-6)<1e-12 and abs(mu5-270)<1e-10
B=(math.sqrt(2)+2)*math.sqrt(mu2)
A=B*B+mu2
threshold=1024*A
records=[]
for variance in (30000.,120000.,480000.):
    assert variance>=threshold
    def equations(z):
        u,r=z
        denominator=r+(u-y)**2/variance
        return [float(p@(1/denominator))-1,float(p@((u-y)/denominator**2))]
    result=root(equations,[-2*mu3/variance,1-mu2/variance],tol=1e-12)
    assert np.max(np.abs(equations(result.x)))<1e-11
    u,r=result.x
    assert r>0 and abs(u)<=B and r>=1-A/variance-1e-12
    denominator=r+(u-y)**2/variance
    shift=u+float(p@((u-y)/denominator))
    scaled_second=(shift+3*mu3/variance)*variance**2
    records.append({'t':variance,'global_uniqueness_sufficient_threshold':threshold,'mean':mean,'mu2':mu2,'mu3':mu3,'mu5':mu5,'mode_shift':shift,'scaled_second_coefficient':scaled_second,'predicted_second_coefficient':5*mu5-22*mu2*mu3,'equation_residual':float(np.max(np.abs(equations(result.x))))})
# For k>=160, ((k+1)/k)^7/2<0.523, so the omitted raw seventh moment
# is <=160^7*2^(-161)/(1-0.523); omitted mass is exactly 2^(-160).
tail_seventh_bound=160.**7*2.**(-161)/(1-.523)
assert tail_seventh_bound<2e-33
report={'law':'geometric(1/2) on nonnegative integers','numerical_truncation_points':160,'omitted_mass':2.**(-160),'omitted_raw_seventh_moment_upper_bound':tail_seventh_bound,'label':'numerical unbounded-law approximation with explicit tail control, not a proof certificate','records':records}
(here/'unbounded_mode_measurements.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report))
