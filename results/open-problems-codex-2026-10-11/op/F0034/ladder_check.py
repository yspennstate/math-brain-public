"""Exact finite planar ladder, using rational times and spatial edge order.
This is a deterministic graph example, not a Brownian-net sample.
"""
from fractions import Fraction as F
import json,pathlib
P=pathlib.Path(__file__).parent

def ladder(N):
    pa={};ch={};t={};xy={}
    def node(v,time,x=F(0)):
        pa[v]=[];ch[v]=[];t[v]=time;xy[v]=x
    def rail(i,time):
        h=F(1,2**i)
        return min(time+h,2*h-time)
    def edge(u,v):
        assert t[u]<t[v],(u,v,t[u],t[v])
        ch[u].append(v);pa[v].append(u)
    node('in',F(-2));node('out',F(3));node('root',F(2))
    for i in range(N+1):node(('s',i),-F(1,2**i))
    for i in range(N):
        h=F(1,2**i)
        node(('m',i),h)
        node(('p',i),h/3,rail(i,h/3))
        node(('q',i),2*h/3,rail(i+1,2*h/3))
    edge('in',('s',0))
    for i in range(N):edge(('s',i),('s',i+1))
    edge(('s',N),('m',N-1))
    for i in range(N-1,0,-1):edge(('m',i),('m',i-1))
    edge(('m',0),'root');edge('root','out')
    for i in range(N):
        edge(('s',i),('p',i))
        edge(('p',i),('q',i)) # left side-branch, to the next inner rail
        edge(('p',i),'root' if i==0 else ('q',i-1)) # right continuation
        if i+1==N:edge(('s',N),('q',i))
        edge(('q',i),('m',i))
    # The last rail starts at s_N and reaches q_(N-1).
    # Order children/parents by edge coordinate at an infinitesimal step.
    for v in ch:
        ch[v].sort(key=lambda w:(xy[w]-xy[v])/(t[w]-t[v]))
        pa[v].sort(key=lambda u:-(xy[v]-xy[u])/(t[v]-t[u]))
    return pa,ch,t,xy

def extreme(v,links,side):
    result=[]
    while links[v]:
        v=links[v][side];result.append(v)
    return result

def first_reunion(v,links):
    left=extreme(v,links,0)
    right=set(extreme(v,links,-1))
    return next((w for w in left if w in right),None)

def edge_cross_checks(pa,ch,t,xy):
    # Exact linear interpolation; crossings must be a common graph endpoint.
    edges=[(u,v) for u in ch for v in ch[u]]
    checks=0
    for j,(u,v) in enumerate(edges):
        for u2,v2 in edges[j+1:]:
            lo=max(t[u],t[u2]);hi=min(t[v],t[v2])
            if lo>=hi:continue
            def x(e,time):
                a,b=e;return xy[a]+(xy[b]-xy[a])*(time-t[a])/(t[b]-t[a])
            d0=x((u,v),lo)-x((u2,v2),lo)
            d1=x((u,v),hi)-x((u2,v2),hi)
            assert d0*d1>=0,('interior crossing',(u,v),(u2,v2))
            assert not (d0==0 and d1==0),('overlapping edges',(u,v),(u2,v2))
            if d0==0:assert lo in {t[u],t[v]} and lo in {t[u2],t[v2]}
            if d1==0:assert hi in {t[u],t[v]} and hi in {t[u2],t[v2]}
            checks+=1
    return checks

rows=[]
for N in [1,2,3,5,10,20,40,80]:
    pa,ch,t,xy=ladder(N)
    for v in pa:
        assert (len(pa[v]),len(ch[v])) in [(0,1),(1,0),(1,2),(2,1)]
    for i in range(N+1):assert first_reunion(('s',i),ch)==('root' if i==0 else ('m',i-1))
    for i in range(N):assert first_reunion(('m',i),pa)==('s',i)
    assert first_reunion('root',pa)==('s',0)
    for i in range(N):
        assert first_reunion(('p',i),ch)==('root' if i==0 else ('m',i-1))
        assert first_reunion(('q',i),pa)==('s',i)
    c=edge_cross_checks(pa,ch,t,xy)
    rows.append({'N':N,'vertices':len(t),'exact_phi_checks':4*N+2,'inverse_chain_vertices':2*N+1,'overlap_pair_checks':c})
data={'description':'Exact rational planar trivalent ladder; not a Brownian-net counterexample','rows':rows}
(P/'ladder_results.json').write_text(json.dumps(data,indent=2),encoding='utf8')
print(json.dumps(data,indent=2))
