import json,itertools,time
from fractions import Fraction as F
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
start=time.monotonic()
census=json.loads((BASE/'out'/'census_n4.json').read_text())
eq4={m for n,m in census['possible_maximizers'] if n==4 and all(any(((m>>x)^(m>>(x^(1<<i))))&1 for x in range(16)) for i in range(4))}
hist={}; representatives={}
for mask in sorted(eq4):
    table=[1 if mask>>x&1 else -1 for x in range(16)]
    w=[sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(table)) for s in range(16)]
    assert all(abs(v)==4 for v in w)
    a=[int(v==-1) for v in table]
    for i in range(4):
        for s in range(16):
            if s>>i&1:a[s]^=a[s^(1<<i)]
    assert all(not a[s] for s in range(16) if s.bit_count()>2)
    degrees=[sum(a[(1<<i)|(1<<j)] for j in range(4) if j!=i) for i in range(4)]
    key=','.join(map(str,sorted(degrees)))
    hist[key]=hist.get(key,0)+1; representatives.setdefault(key,mask)

edges=list(itertools.combinations(range(4),2)); generated=set(); rankfull=0
for graph in range(64):
    rows=[sum(1<<j for j in range(4) if j!=i and graph>>edges.index(tuple(sorted((i,j))))&1) for i in range(4)]
    rank=0
    for col in range(4):
        pivot=next((j for j in range(rank,4) if rows[j]>>col&1),None)
        if pivot is None:continue
        rows[pivot],rows[rank]=rows[rank],rows[pivot]
        for j in range(4):
            if j!=rank and rows[j]>>col&1:rows[j]^=rows[rank]
        rank+=1
    if rank!=4:continue
    rankfull+=1
    for affine in range(32):
        mask=0
        for x in range(16):
            bit=(affine>>4)&1
            bit^=(affine&x).bit_count()%2
            for j,(a,b) in enumerate(edges):
                if graph>>j&1:bit^=((x>>a)&1)&((x>>b)&1)
            mask|=(1-bit)<<x
        generated.add(mask)
assert generated==eq4 and len(eq4)==896 and rankfull==28
b05=[]
for k in range(4,41,2):
    delta=F(1,2**k); p=F(1,2**(2*k)); lower=p*(k-3-delta*(3*k+F(1,2)))
    assert lower>0
    b05.append({'k':k,'D4_parent_certified_lower':[lower.numerator,lower.denominator]})
out={'status':'PASS','bent_equality_cases':896,'nonsingular_quadratic_graphs':28,
     'degree_multiset_counts':hist,'representatives':representatives,'B05_rational_checks':b05,
     'elapsed_seconds':time.monotonic()-start}
(BASE/'out'/'structure.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
