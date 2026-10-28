"""Frozen direct-character sum audit: five fixed ordered widths, n<=6.
No fast Walsh implementation, no shared helper, no tree search; <20MB,<60s.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,time
start=time.monotonic(); checks=0; cases=[]
for a,b in [(1,1),(1,2),(2,1),(2,2),(2,3)]:
    d=1+a+b; N=2**d; U=((1<<a)-1)<<1; V=((1<<b)-1)<<(1+a)
    vals=[1-2*int(bool(x&1) and ((x&U).bit_count()%2) and ((x&V).bit_count()%2)) for x in range(N)]
    support={i^j^k for i in [0,1] for j in [0,U] for k in [0,V]}
    for t in range(N):
        coefficient=F(sum(vals[x]*(-1)**((x&t).bit_count()%2) for x in range(N)),N)
        assert coefficient**2==(F(9,16) if t==0 else F(1,16) if t in support else 0)
        checks+=1
    for i in range(d):
        physical=F(sum(vals[x]!=vals[x^(1<<i)] for x in range(N)),N)
        assert physical==F(1,4); checks+=1
    assert len(support)==8; checks+=1
    cases.append({'widths':[a,b],'physical_dimension':d,'support':sorted(support)})
assert 14**28<2**107 and 27<32; checks+=2
# Root scalar certificates and non-source-equal inherited sparse normalization.
assert F(4,19)+3*F(5,19)==1 and F(4,19)!=F(1,4); checks+=2
assert F(16,35)+F(19,35)==1; checks+=1
result={'status':'PASS','assertions':checks,'cases':cases,'elapsed_seconds':time.monotonic()-start,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).resolve().parents[1].joinpath('out/independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
