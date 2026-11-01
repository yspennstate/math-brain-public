from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json, urllib.request, urllib.parse, math
ROOT=Path(__file__).resolve().parent
CLAIM=Path('~/brain_workers/TRIO_1011/op/G0002')
print('CLAIMANT FILES', [p.name for p in CLAIM.iterdir()], flush=True)
for name in ['source.txt','source_text.txt','cerf.txt']:
    if (CLAIM/name).exists():
        print('FOUND TEXT',name,flush=True)
n=10**14; r=10**6; h=10**7
assert n==h*h==100*r*r
assert F(r*r,12)-F(288*r**3,n)>=F(r*r,24)
assert F(r*r,2592)>10*h
print('EXACT MARGINS',F(r*r,12)-F(288*r**3,n)-F(r*r,24), F(r*r,2592)-10*h, flush=True)
# Enumerate every clause array independently; definitions tested directly.
total=0
for arr in product(list(product(range(3),repeat=2)),repeat=3):
    def member(w): return all(any((w>>i)&1 for i in clause) for clause in arr)
    for w in range(8):
        if not member(w): continue
        total+=1
        S={i for i in range(3) if (w>>i)&1 and not member(w&~(1<<i))}
        edges=[]
        for clause in arr:
            pos=[i for i in clause if (w>>i)&1]
            if len(pos)==2 and pos[0]!=pos[1]: edges.append(set(pos))
        C=set().union(*edges) if edges else set()
        bad=[e for e in edges if e&S]
        vb=set().union(*bad) if bad else set()
        P2=set(S)
        for j in range(3):
            if not (w>>j)&1: continue
            x=w&~(1<<j)
            for i in range(3):
                if not member(x&~(1<<i)) and member(x|(1<<i)): P2.add(i)
        assert C-vb <= P2-S
        assert len(P2-S)>=len(C)-2*len(bad)
print('GRAPH CHECK',729,total,flush=True)
# Independently enumerate single clauses with duplicates and confirm formulas.
for n0 in range(2,6):
    for rr in range(2,5):
        for s in range(1,n0+1):
            z=F(n0-s,n0); clauses=list(product(range(n0),repeat=rr))
            singleton=sum(len(set(c)&set(range(s)))==1 for c in clauses)
            edge=sum(len([x for x in c if x<s])==2 and len(set(c)&set(range(s)))==2 for c in clauses)
            inc=sum(len([x for x in c if x<s])==2 and len(set(c)&set(range(s)))==2 and 0 in c for c in clauses)
            assert F(singleton,n0**rr)==s*((z+F(1,n0))**rr-z**rr)
            assert F(edge,n0**rr)==math.comb(rr,2)*F(s*(s-1),n0*n0)*z**(rr-2)
            assert F(inc,n0**rr)==rr*(rr-1)*F(s-1,n0*n0)*z**(rr-2)
print('SINGLE CLAUSE FORMULAS PASS',flush=True)
queries={
 'arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"second order" AND all:pivotal')+'&max_results=10',
 'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('second order pivotal Cerf')+'&per-page=10',
 'source_abstract':'https://arxiv.org/abs/2608.23661',
}
for name,url in queries.items():
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'MathematicalAudit/1.0'})
        data=urllib.request.urlopen(req,timeout=30).read()
        (ROOT/(name+'.txt')).write_bytes(data)
        print('FETCH',name,len(data),flush=True)
    except Exception as e: print('FETCH ERROR',name,str(e),flush=True)
