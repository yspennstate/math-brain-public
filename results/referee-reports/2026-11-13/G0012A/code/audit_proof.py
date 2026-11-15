"""Finite exact audits of the plan proof, separate from the large simulation."""
import itertools
import json
import os
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import time
from experiment import adjacency, exact_survival, validate
import networkx as nx

ROOT = Path(__file__).resolve().parents[1]


def derangements(a):
    return [p for p in itertools.permutations(a) if all(x != y for x,y in zip(a,p))]


def step(adj, plan, prev, curr):
    return plan[curr][adj[curr].index(prev)]


def walk(adj, plan, edge, k):
    vs = list(edge)
    for _ in range(1,k):
        vs.append(step(adj,plan,vs[-2],vs[-1]))
    return vs


def first_collision(vs):
    seen = set()
    for j,v in enumerate(vs):
        if v in seen:
            return j
        seen.add(v)
    return None


def excursion(adj,plan,path,i,beta,L):
    P = set(path)
    prev,curr = path[i],beta
    es = [(prev,curr)]
    seen = set(path[:i+1])
    bad = curr in seen
    seen.add(curr)
    for _ in range(1,L):
        if curr in P:
            break
        nxt = step(adj,plan,prev,curr)
        prev,curr = curr,nxt
        es.append((prev,curr))
        bad |= curr in seen
        seen.add(curr)
    return es, (path.index(curr) if curr in P else None), bad


def reverse(adj,plan,path,i,beta,L):
    es,l,bad = excursion(adj,plan,path,i,beta,L)
    assert l is not None and 1<=l<len(path)-1
    outside = {v for e in es for v in e} - set(path)
    pp = list(plan)
    for v in outside:
        inv = dict(zip(plan[v],adj[v]))
        pp[v] = tuple(inv[x] for x in adj[v])
    new = tuple(pp)
    return new,l,es[-1][0]


def audit_graph(name,g,edge):
    adj=adjacency(g)
    validate(adj)
    n=len(adj)
    ds=list(map(len,adj))
    Q=F(max(ds),min(ds)-1)
    local=[derangements(a) for a in adj]
    plans=list(itertools.product(*local))
    N=len(plans)
    # Independent exact stationary-law computation on the edge chain.
    for v in range(n):
        for w in adj[v]:
            assert sum((F(1,len(adj[v])-1) for u in adj[v] if u!=w),F())==1
    probs,_=exact_survival(adj,edge)
    result={'graph':name,'n':n,'degrees':ds,'edge':edge,'plans':N,
            'reversal_checks':0,'replacement_checks':0,'packing_checks':0,
            'congestion_checks':0,'probabilities':{}}
    for k in range(2,n):
        simple=[p for p in plans if first_collision(walk(adj,p,edge,k)) is None]
        assert F(len(simple),N)==probs[k]
        result['probabilities'][k]=str(probs[k])
        for L in range(1,n+2):
            total_bad=F()
            total_T=F()
            total_U=F()
            total_E=F()
            incoming=defaultdict(F)
            outgoing=F()
            for plan in simple:
                path=walk(adj,plan,edge,k)
                used_edges=set()
                terminal_edges=set()
                for i in range(1,k):
                    w=F(1,len(adj[path[i]])-1)
                    for beta in adj[path[i]]:
                        if beta in (path[i-1],path[i+1]):
                            continue
                        total_T+=w
                        es,l,bad=excursion(adj,plan,path,i,beta,L)
                        if bad:
                            total_bad+=w
                        if l is None and not bad:
                            assert len(es)==L and len(set(es))==L
                            assert not used_edges.intersection(es)
                            used_edges.update(es)
                            total_U+=w
                            result['packing_checks']+=1
                        if l==k:
                            assert es[-1] not in terminal_edges
                            terminal_edges.add(es[-1])
                            total_E+=w
                        if l is not None and 1<=l<k:
                            new,j,b=reverse(adj,plan,path,i,beta,L)
                            assert walk(adj,new,edge,k)==path
                            es2,l2,bad2=excursion(adj,new,path,j,b,L)
                            assert es2==[(b,a) for a,b in es[::-1]]
                            assert bad or bad2
                            assert reverse(adj,new,path,j,b,L)==(plan,i,beta)
                            ratio=w/F(1,len(adj[path[j]])-1)
                            assert 1/Q<=ratio<=Q
                            result['reversal_checks']+=1
                        if not bad or i>k-L:
                            continue
                        replacements=[p for p in local[path[i]] if p[adj[path[i]].index(path[i-1])]==beta]
                        for rp in replacements:
                            pp=list(plan)
                            pp[path[i]]=rp
                            target=tuple(pp)
                            j=first_collision(walk(adj,target,edge,k))
                            assert i<j<=i+L
                            mass=w/len(replacements)
                            incoming[target]+=mass
                            outgoing+=mass
                            assert mass==F(1,len(local[path[i]]))
                            result['replacement_checks']+=1
                assert len(terminal_edges)<=max(ds)
            if simple:
                assert (1+Q)*total_bad>=total_T-total_U-total_E
                assert (1+Q)*total_bad>=len(simple)*(F(k-1,2)-Q*n/L-Q)
            assert outgoing==sum(incoming.values(),F())
            assert all(v<=L for v in incoming.values())
            result['congestion_checks']+=len(incoming)
    return result


if __name__=='__main__':
    start=time.time()
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    irregular=nx.complete_graph(5)
    irregular.remove_edge(0,1)
    cases=[('K4',nx.complete_graph(4),(0,1)),
           ('K5_minus_edge_low_to_high',irregular,(0,2)),
           ('K5_minus_edge_high_to_low',irregular,(2,0)),
           ('K3_3',nx.complete_bipartite_graph(3,3),(0,3)),
           ('cube',nx.cubical_graph(),(0,1))]
    result=[]
    for name,g,edge in cases:
        r=audit_graph(name,g,edge)
        result.append(r)
        print(name,r['plans'],'plans checked',flush=True)
    (ROOT/'data/proof_audit.json').write_text(json.dumps({'wall_seconds':time.time()-start,'cases':result},indent=2)+'\n')
    print('all exact audits passed',flush=True)
