from pathlib import Path
from functools import lru_cache
from math import factorial
import mpmath as mp
import json,time
from stationary_law import survival,prepare,matrix_for

mp.mp.dps=55
N=32
@lru_cache(None)
def dimension(lam):
    n=sum(lam)
    hook=1
    for i,row in enumerate(lam):
        for j in range(row):
            hook*=row-j+sum(1 for lower in lam[i+1:] if lower>j)
    return factorial(n)//hook

def children(lam):
    for i in range(len(lam)+1):
        if i==len(lam):
            yield lam+(1,)
        elif i==0 or lam[i]<lam[i-1]:
            yield lam[:i]+(lam[i]+1,)+lam[i+1:]

@lru_cache(None)
def graph(d):
    states=[()];seen={()}
    for lam in states:
        if sum(lam)==N:continue
        for mu in children(lam):
            if len(mu)<=d and mu not in seen:seen.add(mu);states.append(mu)
    states.sort(key=lambda x:(sum(x),x))
    ids={s:i for i,s in enumerate(states)}
    edges=[]
    for lam in states:
        row=[];n=sum(lam);f=dimension(lam)
        # Branching identity checked with every child, including killed ones.
        assert sum(dimension(mu) for mu in children(lam))==(n+1)*f
        for mu in children(lam):
            if mu in ids:
                row.append((ids[mu],mp.mpf(dimension(mu))/((n+1)*f)))
        edges.append(row)
    return states,edges

def positive_law(observations):
    obs=prepare(observations)
    if not obs:return mp.mpf(1),mp.mpf(0)
    T,k=obs[-1];d=k-1
    if not d:return mp.exp(-T),mp.mpf(0)
    states,edges=graph(d)
    p=[mp.mpf(0)]*len(states);p[0]=1;t0=mp.mpf(0)
    for t,k in obs:
        delta=t-t0;t0=t
        v=p[:];w=mp.exp(-delta);result=[w*z for z in v]
        for j in range(1,N+1):
            nxt=[mp.mpf(0)]*len(states)
            for i,vi in enumerate(v):
                if vi:
                    for dest,rate in edges[i]:nxt[dest]+=vi*rate
            v=nxt;w*=delta/j
            for i in range(len(states)):result[i]+=w*v[i]
        p=[z if len(lam)<k else mp.mpf(0) for lam,z in zip(states,result)]
    tail=mp.exp(-T)*T**(N+1)/mp.factorial(N+1)
    n=N+1;term=tail
    while term>mp.mpf('1e-65'):
        n+=1;term*=T/n;tail+=term
    return sum(p),tail

cases=[[(1,2),(2,3)],[(1,1),(2,2),(3,3)],[(1,2),(2,3),(3,4)],
       [(1,4),(2,2),(3,4)],[(1,2),(2,2),(3,4)],
       [(1,1),(2,2),(3,3),(4,4),(5,5)],[(1,3),(2,1)]]
start=time.monotonic();rows=[]
for obs in cases:
    exact_formula=survival(obs,precision=65)
    positive,tail=positive_law(obs)
    difference=exact_formula-positive
    assert difference>=-mp.mpf('1e-45'),(obs,difference)
    assert difference<=tail+mp.mpf('1e-45'),(obs,difference,tail)
    row={'observations':obs,'finite_determinant':mp.nstr(exact_formula,50),
         'positive_sum_to_size_32':mp.nstr(positive,50),
         'difference':mp.nstr(difference,12),'poisson_tail':mp.nstr(tail,12),'result':'PASS'}
    rows.append(row);print('PASS',obs,mp.nstr(exact_formula,15),'tail',mp.nstr(tail,4),flush=True)
Path('positive_growth_checks.json').write_text(json.dumps({'size_cutoff':N,'cases':rows,'seconds':time.monotonic()-start},indent=2),encoding='utf8')
print('ALL POSITIVE GROWTH CHECKS PASS',time.monotonic()-start)
