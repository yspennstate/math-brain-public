import json
import math
from pathlib import Path
import numpy as np

base=Path(__file__).resolve().parent
m=np.array([1.,2.,5.,8.])
x=np.array([.8,1.,1.2,1.6])
p=np.array([.72,.10,.13,.05])
K=np.array([2,3]); O=np.array([0,1])
M=m[:,None]*np.minimum(x[:,None],x[None,:])/x[:,None]*p[None,:]
direct=M[np.ix_(K,K)]
bridge=M[np.ix_(K,O)]
outside=M[np.ix_(O,O)]
back=M[np.ix_(O,K)]
R=direct+bridge@np.linalg.inv(np.eye(len(O))-outside)@back
radius=lambda A:float(max(np.linalg.eigvals(A).real))
pi=p*x/m
epsilon=float(m[O]@p[O])
rows=[]
RN=direct.copy(); power=np.eye(len(O))
for N in range(8):
    if N:
        RN+=bridge@power@back
        power=power@outside
    residual=float(np.max(np.abs(pi[K,None]*RN-RN.T*pi[K][None,:])))
    assert residual<1e-12
    rows.append(dict(N=N,radius=radius(RN),symmetry_residual=residual))
assert epsilon<1 and radius(direct)<1 and radius(R)>1 and rows[1]['radius']>1

# Conditional stopped-hazard check with n=8, d=2, four matching edges seen.
# Four active vertices on each side. Cross arrival absorbs; a second arrival
# also absorbs through the cap. Eight non-cross first arrivals remain possible.
n=8; a=.5; delta=a/4
times=np.linspace(0,delta,101)
q=8*np.exp(-23*times/8)-7*np.exp(-3*times)
bound=np.exp(-(a*a*n/4)*times)
assert np.all(q<=bound+1e-14)
assert np.all(q>=0)
out=dict(epsilon=epsilon,full_radius=radius(M),direct_radius=radius(direct),return_radius=radius(R),truncations=rows,stopped_hazard=dict(n=n,a=a,delta=delta,nonabsorption=float(q[-1]),claimed_bound=float(bound[-1])))
(base/'return_stress_independent.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
