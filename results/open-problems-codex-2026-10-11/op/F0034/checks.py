"""Finite planar graph stress test, not a Brownian-net simulation."""
import random, json, math, pathlib
P=pathlib.Path(__file__).parent
rng=random.Random(34012)
totals={'networks':0,'finite_phi2_checks':0,'ancestry_checks':0,'cycle_checks':0,'maximum_transient':0}
def network(steps=100):
    # Event vertices only. Active strands point back to their last event.
    parents={}; children={}; times={}; types={}
    active=[(-i-1,0) for i in range(6)]
    for v,slot in active: parents[v]=[]; children[v]=[None]; times[v]=-1; types[v]='boundary'
    for t in range(steps):
        split=len(active)<2 or (len(active)<20 and rng.random()<.5)
        i=rng.randrange(len(active) if split else len(active)-1)
        v=t
        strands=[active[i]] if split else active[i:i+2]
        parents[v]=[p for p,slot in strands]; children[v]=[None,None] if split else [None]; times[v]=t; types[v]='S' if split else 'M'
        for p,slot in strands: children[p][slot]=v
        active[i:i+(1 if split else 2)]=[(v,0),(v,1)] if split else [(v,0)]
    # Repeated active event ids represent distinct strands; terminal vertices separate them.
    for i,(p,slot) in enumerate(active):
        v=steps+i; parents[v]=[p]; children[v]=[]; times[v]=steps; types[v]='boundary'
        children[p][slot]=v
    return parents,children,times,types

def extremal_chain(v,links,side):
    result=[v]
    while links[v]:
        v=links[v][side];result.append(v)
    return result

def phi(v,parents,children,types):
    links=children if types[v]=='S' else parents
    a=extremal_chain(v,links,0)[1:]
    b=set(extremal_chain(v,links,-1)[1:])
    return next((x for x in a if x in b),None)

def reachable(u,v,children):
    stack=[u];seen=set()
    while stack:
        w=stack.pop()
        if w==v:return True
        if w not in seen:seen.add(w);stack.extend(children[w])
    return False

for _ in range(1000):
    pa,ch,ti,ty=network()
    f={v:phi(v,pa,ch,ty) for v in ty if ty[v] in ['S','M']}
    for v,w in f.items():
        if w is None:continue
        assert ty[w]!=ty[v]
        u=f[w]
        if u is not None:
            totals['finite_phi2_checks']+=1
            if ty[v]=='S':
                assert ti[u]<=ti[v]
                assert reachable(u,v,ch)
            else:
                assert ti[u]>=ti[v]
                assert reachable(v,u,ch)
            totals['ancestry_checks']+=1
            if ti[u]==ti[v]:assert u==v
        seen={};path=[];x=v
        while x is not None and x not in seen:
            seen[x]=len(path);path.append(x);x=f[x]
        if x is not None:
            assert len(path)-seen[x]==2
            totals['cycle_checks']+=1
        totals['maximum_transient']=max(totals['maximum_transient'],len(path) if x is None else seen[x])
    totals['networks']+=1
totals['density_values']=[{'h':h,'Psi_minus_2':math.exp(-h)/math.sqrt(math.pi*h)-math.erfc(math.sqrt(h)),
 'upper_bound':math.exp(-h)/math.sqrt(math.pi*h)} for h in [.01,.1,1,2,5,10,20]]
for x in totals['density_values']:assert 0<x['Psi_minus_2']<=x['upper_bound']
(P/'checks_results.json').write_text(json.dumps(totals,indent=2),encoding='utf8')
print(json.dumps(totals,indent=2))
