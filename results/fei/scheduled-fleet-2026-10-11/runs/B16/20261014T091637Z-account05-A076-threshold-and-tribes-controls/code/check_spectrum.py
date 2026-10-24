"""Independent direct Walsh reconstruction, not a second reviewer."""
from fractions import Fraction as Q
from pathlib import Path
import json,time
root=Path(__file__).resolve().parents[1];beg=time.perf_counter();checks=0
def assert_eq(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1
def walsh(table,freq):return Q(sum(value*(-1 if (point&freq).bit_count()%2 else 1) for point,value in enumerate(table)),len(table))
roots=0
for n in [0,1,2]:
    size=1<<n
    for label in range(1<<size):
        values=[1-2*((label>>j)&1) for j in range(size)]
        table=[]
        for point in range(16*size):
            s=point//size;x=point%size
            h=(-1)**(((s&1)*((s>>1)&1))+(((s>>2)&1)*((s>>3)&1)))
            table.append(h*(values[x] if s==0 else 1))
        influence=Q(0)
        for s in range(16):
            # Independent product of the exact two-bit bent coefficient table.
            hhat=Q((-1)**(((s&1)*((s>>1)&1))+(((s>>2)&1)*((s>>3)&1))),4)
            for xfreq in range(size):
                actual=walsh(table,s*size+xfreq)
                vhat=walsh(values,xfreq)
                expected=hhat-Q(1-vhat,16) if xfreq==0 else vhat/16
                assert_eq(actual,expected)
                influence+=(s.bit_count()+xfreq.bit_count())*actual*actual
        physical=Q(sum(table[x]!=table[x^(1<<i)] for x in range(len(table)) for i in range(n+4)),len(table))
        assert_eq(influence,physical)
        roots+=1
# A028's exact data-query release-only obstruction, retained as an admission guard.
table=[-1,1,1,1]
assert_eq([walsh(table,j)**2 for j in range(4)],[Q(1,4)]*4)
assert_eq(Q(2)-Q(1,2),Q(3,2))
assert_eq((Q(2)-Q(1,2))/Q(1,2),Q(3))
result=dict(status='PASS',roots=roots,exact_assertions=checks,elapsed_seconds=time.perf_counter()-beg,
 scope='Independent implementation of coefficients and edge influences; not an independent agent review. A028 release-only counterexample rechecked.')
(root/'out/REPRODUCTION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
