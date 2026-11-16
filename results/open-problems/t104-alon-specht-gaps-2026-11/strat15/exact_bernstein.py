"""STRAT15 exact controls, using the unchanged inherited integer converter."""
import sys,importlib.util
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
S12=HERE/'STRAT14/STRAT13/STRAT12'
sys.path.append(str(S12/'STRAT10'))
spec=importlib.util.spec_from_file_location('inherited_bernstein',S12/'exact_bernstein.py')
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
SELECT='c2'

@lru_cache(None)
def chart_data():
    rr,t,V,R,M,delta,Q,tau,D,edges,P,num=base.construct()
    cs=[{}for _ in range(3)]
    for m,c in num.items():
        assert c.denominator==1 and int(c)%8==0
        cs[m[-1]][m[:6]]=int(c)//8
    def add(*terms):
        out={}
        for k,p in terms:
            for m,c in p.items():out[m]=out.get(m,0)+k*c
        return {m:c for m,c in out.items()if c}
    targets=dict(c2=cs[2],d1=add((1,cs[1]),(2,cs[2])),C1=add(*[(1,p)for p in cs]))
    # Weaker all-N residual: r>=3/25, a>=129/250.
    gs=dict(orientation=t*t-1-rr.gens[5]**2,order12=V[1][0]-V[0][0],
            order23=V[2][0]-V[1][0],x3bound=V[2][0]+1)
    gs.update({'row'+str(i):4*t-R[i][i]for i in range(5)})
    gs.update({'g'+str(i)+str(j):g for (i,j),g in edges.items()if(i,j)!=(3,4)})
    X=129*D-250*tau
    gs.update(spectral00=5*t-M[0][0],spectral11=5*t-M[1][1],
              connected=25*t*t-5*t*tau+delta,rank=delta,
              ratio=784*delta-75*tau*tau,scale_guard=X,
              scale14=62500*(tau*tau-4*delta)-X*X)
    def dic(p):
        assert all(m[-1]==0 and c.denominator==1 for m,c in p.items())
        return {m[:6]:int(c)for m,c in p.items()}
    return targets,{k:dic(p)for k,p in gs.items()},cs

def data():return chart_data()[0][SELECT],chart_data()[1]
base.data=data
degree=base.degree;normal=base.normal;controls=base.controls
bernstein_min=base.bernstein_min;active_constraints=base.active_constraints
multiply=base.multiply;volume=base.volume;conversion=base.conversion

def verify_certificate(r):
    global SELECT
    SELECT=r.get('coefficient',SELECT)
    return base.verify_certificate(r)

def select(key):
    global SELECT
    assert key in chart_data()[0]
    SELECT=key

