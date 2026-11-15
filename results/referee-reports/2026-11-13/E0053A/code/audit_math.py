#!/usr/bin/env python3
"""Independent finite checks of the counting/proof formulas and solver artifacts."""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import itertools,json,math,pathlib,statistics,subprocess
from fractions import Fraction
ROOT=pathlib.Path(__file__).resolve().parents[1]
def dfact(k):
    r=1
    while k>0:r*=k;k-=2
    return r
checks=[]
for d in [2,3,4,5]:
    for n in [6,8,10,12]:
        a=d*n//2
        probs={k:Fraction(math.comb(a,k)**2*math.factorial(k)*dfact(a-k-1)**2,dfact(2*a-1)) for k in range(a+1) if (a-k)%2==0}
        assert sum(probs.values())==1
        assert sum(k*p for k,p in probs.items())==Fraction(a*a,2*a-1)
        checks.append(f'pairing distribution normalization and mean n={n} d={d}')
for d in [0,1,2]:
    for n in [6,8,10,12]:
        if d==0:edges=[]
        else:
            path=ROOT/'data'/f'proof_d{d}_n{n}.graph'
            subprocess.run([str(ROOT/'code/bisection'),'generate',str(n),str(d),str(530000+d*100+n),str(path)],check=True,stdout=subprocess.DEVNULL)
            edges=[tuple(map(int,l.split())) for l in path.read_text().splitlines()[1:]]
        cuts=[];qs=[]
        for chosen in itertools.combinations(range(n),n//2):
            s=set(chosen);cut=sum((u in s)!=(v in s) for u,v in edges);cuts.append(cut);qs.append(len(edges)-2*cut)
        mn,mx=min(cuts),max(cuts)
        if d==0:assert (mn,mx)==(0,0)
        if d==1:assert mn==(n//2)%2 and mx==n//2
        if d==2:
            a=[[] for _ in range(n)]
            for u,v in edges:a[u].append(v);a[v].append(u)
            seen=set();odd=0
            for u in range(n):
                if u in seen:continue
                stack=[u];component=set()
                while stack:
                    v=stack.pop()
                    if v in component:continue
                    component.add(v);stack.extend(w for w in a[v] if w not in component)
                seen|=component;odd+=len(component)%2
            assert mx==n-odd and mn<=2
        assert mn+mx-len(edges)==-(max(qs)+min(qs))/2
        for beta in [.1,.5,2,10]:
            def logsum(v):
                top=max(v);return top+math.log(sum(math.exp(x-top) for x in v))
            diff=(logsum([beta*q for q in qs])-logsum([-beta*q for q in qs]))/(2*beta*n)
            assert abs((mn+mx-len(edges))/n+diff)<=math.log(math.comb(n,n//2))/(2*beta*n)+1e-12
        checks.append(f'd={d} theorem and finite-temperature bound n={n}')
# Independent witness verification on all recorded experiment modes.
certified=0;witnesses=0;records=0
for mode in ['small','large','deep','sa']:
    path=ROOT/'data'/f'{mode}.jsonl'
    if not path.exists():continue
    for l in path.read_text().splitlines():
        r=json.loads(l);n=r['n'];gpath=ROOT/r['graph'];els=[tuple(map(int,x.split())) for x in gpath.read_text().splitlines()[1:]]
        deg=[0]*n;assert len(els)==n*r['d']//2;assert len(set(tuple(sorted(e)) for e in els))==len(els)
        for u,v in els:assert u!=v;deg[u]+=1;deg[v]+=1
        assert deg==[r['d']]*n
        trace=[json.loads(x) for x in (ROOT/r['trace']).read_text().splitlines()]
        for row in trace:
            s=row['spin'];assert len(s)==n and s.count('1')==n//2
            assert row['cut']==sum(s[u]!=s[v] for u,v in els)
            assert row['cut']%2==(r['d']*n//2)%2
            witnesses+=1
        assert r['min']==min(x['cut'] for x in trace if x['objective']=='min')
        assert r['max']==max(x['cut'] for x in trace if x['objective']=='max')
        if 'exact' in r:
            exact=r['exact'];assert exact['partitions']==math.comb(n-1,n//2)
            for objective in ['min','max']:
                s=exact[objective+'_spin'];assert s.count('1')==n//2
                assert exact[objective]==sum(s[u]!=s[v] for u,v in els)
                assert r[objective]==exact[objective]
            certified+=1
        elif all(x['status']==0 for x in r.get('milp',[])) and r.get('milp'):
            for x in r['milp']:assert r[x['objective']]==x['cut'] and abs(x['dual_bound']-x['cut'])<1e-5
            certified+=1
        records+=1
result={'finite_formula_checks':checks,'recorded_experiments_checked':records,'witnesses_checked':witnesses,'graphs_with_both_optima_certified':certified,'nice':os.getpriority(os.PRIO_PROCESS,0)}
(ROOT/'data'/'audit_math.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='finite_formula_checks'},indent=2))
