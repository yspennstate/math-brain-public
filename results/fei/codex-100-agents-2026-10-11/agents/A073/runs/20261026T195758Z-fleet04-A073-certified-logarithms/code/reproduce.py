"""Independent representation: butterfly Walsh transform and raw denominator 64."""
from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
R=Path(__file__).resolve().parents[1];start=time.monotonic();count=0
(R/'out/REPRODUCTION_FROZEN.json').write_text(json.dumps({'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'all three-bit Boolean functions','domain':'truth masks 0..255','case_count':256,'symmetry':'none','arithmetic':'integer butterfly Walsh; Fraction physical edge influence; integer logarithm products','memory_estimate_MB':40,'maximum_runtime_seconds':55},indent=2)+'\n',encoding='utf-8')
rows=json.loads((R/'out/FACTOR_CERTIFICATES.json').read_text(encoding='utf-8'))
assert len(rows)==256 and {r['truth_mask'] for r in rows}==set(range(256))
for r in rows:
    mask=r['truth_mask'];v=[1-2*((mask>>x)&1) for x in range(8)];w=v.copy()
    step=1
    while step<8:
        for a in range(0,8,2*step):
            for j in range(step):
                c,d=w[a+j],w[a+j+step];w[a+j]=c+d;w[a+j+step]=c-d
        step*=2
    assert w==r['walsh_numerators']
    I=F(sum(v[x]!=v[x+(1<<j)] for j in range(3) for x in range(8) if not x&(1<<j)),4)
    assert I==F(r['influence'])
    mu=F(sum(v),8)
    A=64*(4*I-6-F(25,8)*(1-abs(mu)))
    assert A.denominator==1
    product=1
    for z in w:
        square=z*z
        if square:product*=square**square
    left=product*2**max(int(A),0);right=2**max(-int(A),0)
    assert left>=right
    assert (left>right)==r['strict']
    assert int(r['integer_lhs'])>=int(r['integer_rhs'])
    count+=6
signs=json.loads((R/'out/INTEGER_SIGNS.json').read_text(encoding='utf-8'))
for s in signs:
    a,b,c=(int(s[k],16) for k in ['lhs','rhs','integer_margin'])
    assert a-b==c>0;count+=1
assert (2**25*6**112)>7**112
assert (2**67*6**300)>7**300
assert 2*7**5>8**5
assert 3**36>2**57
count+=4
result={'status':'PASS','representation':'butterfly/raw Walsh denominator64 versus direct sum/reduced denominator16',
        'truth_tables':256,'checks':count,'runtime_seconds':time.monotonic()-start,
        'independence':'separate implementation by A073; no independent-agent acceptance'}
(R/'out/REPRODUCTION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
