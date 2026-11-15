"""Single-process, time-bounded four-state reversible search and exact audit."""
import json
import time
import warnings
from fractions import Fraction as F
import numpy as np
from scipy.optimize import minimize
from referee_core import exact_chain,lump,display

warnings.filterwarnings('ignore',category=RuntimeWarning)
begin=time.monotonic()
deadline=begin+95
rng=np.random.default_rng(579831)
edges=[(i,j) for i in range(4) for j in range(i,4) if (i,j)!=(0,2)]
evaluations=0
best=(0,None,None)
top=[]

def times(w):
    d=w.sum(axis=1)
    pi=d/d.sum()
    # Deviation matrix from the fundamental matrix. This is deliberately
    # independent of the exact grounded-Laplacian implementation.
    p=w/d[:,None]
    z=np.linalg.inv(np.eye(len(w))-p+np.ones((len(w),1))*pi[None,:])
    return np.max(1-z/pi[None,:])

def score(w):
    global evaluations,best
    evaluations+=1
    v=np.array([[w[0,0],w[0,1],sum(w[0,2:])],
                [w[1,0],w[1,1],sum(w[1,2:])],
                [sum(w[2:,0]),sum(w[2:,1]),sum(w[2:,2:].flat)]])
    try:
        a,b=times(w),times(v)
    except np.linalg.LinAlgError:
        return 0
    ratio=b/a
    if not np.isfinite(ratio) or a<=0 or ratio>3.01:
        return 0
    if ratio>best[0]:
        best=(ratio,w.copy(),(a,b))
    return ratio

def matrix(x,mask):
    w=np.zeros((4,4))
    w[0,2]=w[2,0]=1.
    for exponent,(i,j) in zip(x,mask):
        w[i,j]=w[j,i]=np.exp(exponent)
    return w

def objective(x,mask):
    if time.monotonic()>deadline:
        raise TimeoutError
    return -score(matrix(x,mask))

base=np.zeros((4,4))
for i,j,v in [(0,2,1),(1,2,1),(1,3,109),(2,3,54),(1,1,117),(3,3,10000)]:
    base[i,j]=base[j,i]=v
score(base)
sparse=[(1,1),(1,2),(1,3),(2,3),(3,3)]
starts=[(np.log([117,1,109,54,10000]),sparse)]
for k in range(6000):
    mask=sparse if k%3==0 else edges
    x=rng.uniform(-5,9,len(mask))
    val=score(matrix(x,mask))
    if len(top)<35 or val>top[0][0]:
        top.append((val,x.copy(),mask))
        top.sort(key=lambda t:t[0])
        top=top[-35:]
starts += [(x,mask) for _,x,mask in reversed(top)]
local_runs=0
try:
    for x,mask in starts:
        minimize(objective,x,args=(mask,),method='Powell',
                 bounds=[(-9,16)]*len(mask),
                 options={'maxfev':6000,'maxiter':140,'xtol':1e-7,'ftol':1e-10})
        local_runs+=1
    while time.monotonic()<deadline:
        mask=edges if local_runs%3==0 else sparse
        # Restarts near the best matrix, plus fresh random restarts.
        if local_runs%4:
            x=np.array([np.log(max(best[1][i,j],1e-8)) for i,j in mask])
            x=np.clip(x+rng.normal(0,1.2,len(mask)),-9,16)
        else:
            x=rng.uniform(-6,12,len(mask))
        minimize(objective,x,args=(mask,),method='Nelder-Mead',
                 bounds=[(-9,16)]*len(mask),
                 options={'maxfev':5000,'xatol':1e-7,'fatol':1e-10})
        local_runs+=1
except TimeoutError:
    pass

# Rationalize ALL entries, then recompute both times exactly. The optimized
# float is not itself used as evidence. Keep 8 significant decimal digits.
w=[[F(format(v,'.8g')) for v in row] for row in best[1]]
a=exact_chain(w)
b=exact_chain(lump(w,[0,1,2,2]))
exactratio=b['tmix']/a['tmix']
out=dict(seed=579831,seconds=time.monotonic()-begin,
         random_restarts=6000,local_searches_completed=local_runs,evaluations=evaluations,
         merged_states=[2,3],weights=[[str(x) for x in row] for row in w],
         float_best=best[0],tmix=display(a['tmix']),lumped=display(b['tmix']),
         ratio=display(exactratio),exact_certificates_passed=True,
         optimum_claimed=False)
assert exactratio>F(127,100)
with open('referee_search.json','w') as f:
    json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
