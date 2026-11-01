"""Independent n=3 reconstruction by generating every binary substitution."""
from pathlib import Path
import json,itertools,time
OUT=Path(__file__).resolve().parents[1]/'out'
start=time.perf_counter(); checks=0
def ck(q):
    global checks
    assert q; checks+=1
def table(mask,n): return tuple((mask>>x)&1 for x in range(1<<n))
def essential(t,n): return all(any(t[x]!=t[x^(1<<i)] for x in range(1<<n)) for i in range(n))
generated=set()
for B in itertools.combinations(range(3),2):
    d=next(i for i in range(3) if i not in B)
    for hm in range(16):
        h=table(hm,2)
        for gm in range(16):
            g=table(gm,2); t=[]
            for x in range(8):
                a=((x>>B[0])&1)|(((x>>B[1])&1)<<1)
                t.append(g[h[a]|(((x>>d)&1)<<1)])
            if essential(t,3): generated.add(tuple(t))
ess=prime=0
for mask in range(256):
    t=table(mask,3)
    if not essential(t,3): continue
    ess+=1
    row_decomp=False
    for B in itertools.combinations(range(3),2):
        d=next(i for i in range(3) if i not in B)
        rows={tuple(t[(((a&1)<<B[0])|(((a>>1)&1)<<B[1])|(b<<d))] for b in range(2)) for a in range(4)}
        row_decomp|=(len(rows)==2)
    ck(row_decomp==(t in generated))
    prime+=not row_decomp
ck(ess==218); ck(len(generated)==114); ck(prime==104)
# Exact physical witness: first root child has probability 1/4.
vals=[int((x&3)==3) for x in range(16)]
ck(sum(vals)==4)
result={'helper':'A043-independent-generation-v1','generated_compositions':768,'n3_essential':ess,'n3_decomposable':len(generated),'n3_prime':prime,'assertions':checks,'runtime_seconds':time.perf_counter()-start,'arithmetic':'integers and exact table sets; no logarithms'}
(OUT/'independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
