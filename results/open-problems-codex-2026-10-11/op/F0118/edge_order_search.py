"""Find exact failure of pairwise binary Blackwell order under a Potts edge.
The searched objects are symmetric finite posterior laws, not broadcast limits.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import numpy as np,json,math
from scipy.optimize import linprog
ROOT=Path(__file__).resolve().parent
def orbits(q,M):
    def rec(a,total):
        if len(a)==q-1:
            if total>=a[-1]:yield tuple(a+[total])
            return
        for x in range(a[-1] if a else 0,total+1):yield from rec(a+[x],total-x)
    return [tuple(F(x,M) for x in a) for a in rec([],M)]
def hist(v,alpha):
    q=len(v);ps=set(permutations(v));h={}
    for p in ps:
        a=(1-alpha)/q+alpha*p[0];d=(1-alpha)/q+alpha*p[1]
        if a+d:
            z=abs(a-d)/(a+d);w=F(q,2)* (a+d)/len(ps);h[z]=h.get(z,F(0))+w
    assert sum(h.values())==1
    return h
def payoff(h,t):return sum(w*max(z-t,0) for z,w in h.items())
for q,M in [(3,6),(3,12),(4,8)]:
    vs=orbits(q,M); hs=[hist(v,F(1)) for v in vs];Hs=[hist(v,F(1,2)) for v in vs]
    ts=sorted(set().union(*(set(h) for h in hs)));Ts=sorted(set().union(*(set(h) for h in Hs)))
    G=[[payoff(h,t) for h in hs] for t in ts];J=[[payoff(h,t) for h in Hs] for t in Ts]
    found=False
    for t,row in zip(Ts,J):
        lp=linprog(np.array(row,dtype=float),A_ub=-np.array(G,dtype=float),b_ub=np.zeros(len(G)),
                   A_eq=np.ones((1,len(vs))),b_eq=[0.],bounds=[(-1,1)]*len(vs),method='highs')
        if not lp.success or lp.fun>=-1e-8:continue
        delta=[F(float(x)).limit_denominator(100000) for x in lp.x]
        if sum(delta)!=0 or any(sum(a*d for a,d in zip(g,delta))<0 for g in G):continue
        diff=sum(a*d for a,d in zip(row,delta))
        if diff>=0:continue
        pos=sum(max(d,0) for d in delta);strong=[max(d,0)/pos for d in delta];weak=[max(-d,0)/pos for d in delta]
        payload={'q':q,'M':M,'edge_lambda':'1/2','threshold':str(t),'post_edge_stop_loss_difference':str(diff/pos),
                 'orbits':[[str(x) for x in v] for v in vs], 'strong_weights':[str(w) for w in strong], 'weak_weights':[str(w) for w in weak],
                 'pre_edge_checks':{str(t):str(sum(g[i]*(strong[i]-weak[i]) for i in range(len(vs)))) for t,g in zip(ts,G)},
                 'post_edge_checks':{str(t):str(sum(g[i]*(strong[i]-weak[i]) for i in range(len(vs)))) for t,g in zip(Ts,J)}}
        (ROOT/'edge_order_witness.json').write_text(json.dumps(payload,indent=2),encoding='utf8')
        print('EXACT EDGE-COMPOSITION OBSTRUCTION',json.dumps(payload),flush=True);found=True;break
    print('finished',q,M,'orbits',len(vs),'found',found,flush=True)
    if found:break
