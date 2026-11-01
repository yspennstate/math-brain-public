from pathlib import Path
from fractions import Fraction as Q
from itertools import product,combinations,permutations
from math import factorial,prod
import json,time,sys
OUT=Path(__file__).resolve().parents[1]/'out'; ZERO=(0,0,0)

def add(p,q,scale=Q(1)):
    r=p.copy()
    for k,c in q.items():
        r[k]=r.get(k,Q(0))+scale*c
        if not r[k]: del r[k]
    return r
def mul(p,q):
    r={}
    for x,a in p.items():
        for y,b in q.items():
            z=tuple(i+j for i,j in zip(x,y)); r[z]=r.get(z,Q(0))+a*b
    return {z:c for z,c in r.items() if c}
def determinant(mat):
    n=len(mat); result={}
    for sigma in permutations(range(n)):
        sign=(-1)**sum(sigma[i]>sigma[j] for i in range(n) for j in range(i+1,n)); term={ZERO:Q(sign)}
        for i,j in enumerate(sigma): term=mul(term,mat[i][j])
        result=add(result,term)
    return result
def source_components(parts,support):
    vertices=sorted(parts); adjacency={u:{v for v in vertices if u!=v and parts[u]&support[v]} for u in vertices}
    reach={u:set(adjacency[u])|{u} for u in vertices}
    for k in vertices:
        for u in vertices:
            if k in reach[u]: reach[u]|=reach[k]
    comps={frozenset(v for v in vertices if v in reach[u] and u in reach[v]) for u in vertices}
    return [sorted(c) for c in comps if not any(adjacency[u]&c for u in vertices if u not in c)]

def one(parts,support):
    used=sorted(parts); sources=source_components(parts,support); rootchoices=list(product(*sources)); pi=[Q(1,1<<m.bit_count()) for m in support]
    edges={}
    for u in used:
        for v in used:
            if u==v: continue
            edges[u,v]={tuple(int(i==j) for i in range(3)):Q(1) for j in range(3) if (parts[u]&support[v])>>j&1}
    poly={}
    for roots in rootchoices:
        non=[v for v in used if v not in roots]; mat=[]
        for v in non:
            row=[]
            for u in non:
                if u==v:
                    entry={}
                    for w in used:
                        if w!=v: entry=add(entry,edges[w,v])
                else: entry={k:-c for k,c in edges[u,v].items()}
                row.append(entry)
            mat.append(row)
        poly=add(poly,determinant(mat),prod(pi[r] for r in roots))
    assert all(c>0 for c in poly.values())
    actual={}; traces_total=0
    for roots in rootchoices:
        traces={}; root_weight=prod(pi[r] for r in roots)
        def grow(queue,seen,trace,exponent):
            if not queue:
                if len(seen)==len(used): traces[tuple(trace)]=exponent
                return
            u=queue[0]; avail=[v for v in used if v not in seen]
            for k in range(len(avail)+1):
                for children in permutations(avail,k):
                    choices=[[j for j in range(3) if (parts[u]&support[v])>>j&1] for v in children]
                    for attach in product(*choices):
                        if tuple(sorted(attach))!=attach: continue
                        h=tuple(exponent[j]+attach.count(j) for j in range(3))
                        grow(queue[1:]+list(children),seen|set(children),trace+[(u,parts[u],tuple(zip(attach,children)))],h)
        grow(sorted(roots),set(roots),[],ZERO)
        for h in traces.values(): actual[h]=actual.get(h,Q(0))+root_weight
        traces_total+=len(traces)
    expected={h:c*prod(factorial(v) for v in h) for h,c in poly.items()}
    assert actual==expected,(parts,support,poly,actual)
    can=sum(poly.values()); moment=sum(expected.values()); e=len(used)-len(sources)
    D=[sum(v!=u and bool(support[v]>>j&1) for v in used) if (parts[u]>>j&1) else 0 for j in range(3) for u in used if parts[u]>>j&1]
    # One owner per coordinate; coefficients remain indexed by physical attachment coordinate.
    degree=[sum(v!=u and bool(support[v]>>j&1) for v in used) for j in range(3) for u in used if parts[u]>>j&1]
    values=[]
    for j in range(3):
        owner=next((u for u in used if parts[u]>>j&1),None)
        d=0 if owner is None else sum(v!=owner and bool(support[v]>>j&1) for v in used)
        values.append(Q(d+1,2) if d else Q(1))
    up=sum(c*prod(x**h for x,h in zip(values,exponent)) for exponent,c in poly.items())
    assert can<=moment<=min(factorial(e)*can,up)
    if all(x<=1 for x in values): assert can==moment
    return traces_total

if __name__=='__main__':
    pilot='pilot' in sys.argv; start=time.monotonic(); cases=traces=tables=0
    for ng in range(1,3 if pilot else 4):
        for support in combinations(range(1,8),ng):
            tables+=1
            for A in range(1,8):
                js=[j for j in range(3) if A>>j&1]; choices=[[i for i,m in enumerate(support) if m>>j&1] for j in js]
                for assignment in product(*choices):
                    assert time.monotonic()-start<(60 if pilot else 300)
                    parts={}
                    for j,u in zip(js,assignment): parts[u]=parts.get(u,0)|(1<<j)
                    traces+=one(parts,support); cases+=1
            (OUT/'review_checkpoint.json').write_text(json.dumps({'tables':tables,'ownership_cases':cases,'actual_traces':traces}))
    result={'tables':tables,'ownership_cases':cases,'actual_traces':traces,'verdict':'HOLDS_AT_WHOLE_ORIGINAL_SCOPE_NO_REPAIR; analytic reconstruction in REVIEW_A006.md','elapsed_seconds':time.monotonic()-start,'implementation':'Independent Leibniz polynomial determinant versus chronological BFS event enumeration; rational arithmetic; no source code imported'}
    (OUT/('review_pilot.json' if pilot else 'review.json')).write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2))
