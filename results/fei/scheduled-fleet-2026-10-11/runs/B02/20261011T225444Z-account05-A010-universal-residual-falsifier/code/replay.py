"""Separate queue-growth enumeration of DISTINCT partition runs, n<=3 and top n=4."""
import search as s
from itertools import product, combinations, permutations
from fractions import Fraction as Q
import json,time

def direct_mass(A,gates,lam,n):
    supp=[g[0] for g in gates]; js=[j for j in range(n) if A>>j&1]
    low=Q(0); high=Q(0); total=0
    for assigned in product(*[[l for l,m in enumerate(supp) if m>>j&1] for j in js]):
        parts={}
        for j,l in zip(js,assigned): parts[l]=parts.get(l,0)|(1<<j)
        used=set(parts); source=s.graph_roots(tuple(used),parts,supp)
        d=Q(1); base=lam**len(used)
        for l,B in parts.items():
            d*=Q(B.bit_count(),(A&supp[l]).bit_count())**B.bit_count()
            earlier=0; rank=0
            for j in range(n):
                if supp[l]>>j&1:
                    rank+=1
                    if B>>j&1: d*=Q(earlier+1,rank)
                    earlier+=A>>j&1
        dl,dh=s.power_interval(d)
        for roots in product(*[sorted(c) for c in source]):
            rootset=tuple(sorted(roots)); keys=set()
            def grow(queue,discovered,trace):
                if not queue:
                    if discovered==used: keys.add((rootset,tuple(trace)))
                    return
                p=queue[0]; available=sorted(used-discovered)
                for k in range(len(available)+1):
                    for group in combinations(available,k):
                        for children in permutations(group):
                            choices=[[j for j in js if (parts[p]&supp[c])>>j&1] for c in children]
                            for attach in product(*choices):
                                if list(attach)!=sorted(attach): continue
                                grow(queue[1:]+list(children),discovered|set(children),trace+[(p,parts[p],tuple(zip(attach,children)))])
            grow(list(rootset),set(rootset),[])
            factor=base*len(keys)*Q(1,1<<sum(supp[l].bit_count() for l in roots))
            low+=factor*dl; high+=factor*dh; total+=len(keys)
    return low,high,total

start=time.monotonic(); tests=[]
for n in range(1,4):
    for t,c in s.reps(n):
        for v in {t,t^((1<<(1<<n))-1)}:
            if v in (0,(1<<(1<<n))-1): continue
            gates=s.primes(v,n); lam=Q(1,max(sum(m>>j&1 for m,_ in gates) for j in range(n)))
            for A,a in enumerate(s.walsh(v,n)):
                if A and a:
                    first=s.mass(A,gates,lam,n); second=direct_mass(A,gates,lam,n)
                    assert first==second,(n,v,A,first,second)
                    tests.append([n,v,A,first[2]])
rows=json.loads((s.OUT/'results.json').read_text())['rows']
for r in rows[:3]:
    n=r['n']; t=r['truth']; gates=s.primes(t,n); lam=Q(1,r['read'])
    for A,a in enumerate(s.walsh(t,n)):
        if A and a:
            first=s.mass(A,gates,lam,n); second=direct_mass(A,gates,lam,n)
            assert first==second,(n,t,A)
            tests.append([n,t,A,first[2]])
result={'method':'explicit queue-growth and deduplicated run traces','exact_comparisons':len(tests),'distinct_runs_in_comparisons':sum(t[3] for t in tests),'elapsed_seconds':time.monotonic()-start,'cases':tests}
(s.OUT/'replay.json').write_text(json.dumps(result,indent=2)); print({k:v for k,v in result.items() if k!='cases'})
