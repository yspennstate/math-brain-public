from pathlib import Path
from fractions import Fraction as Q
import json,time
from exact import *
root=Path(__file__).resolve().parents[1]; start=time.perf_counter(); count=0; cases=0
def ck(ok):
    global count
    count+=1; assert ok,count
certs=[3**9>2**14,3**5<2**8,15**2>16*13,15**32>2**65*13**16,13**3>2**11,15**6>2**23]
for c in certs: ck(c)
l=lg(3); p=lg(13); q=lg(15)
for u in range(8):
    J=mul(l,-Q(7,4) if u==0 else Q(5,4)); s=sum(g(u)*g(u^(1<<i)) for i in range(3))
    ck(bounds(plus(mul(J,4),const(-8*s)))[1]<Q(118,9))
    for first in range(3):
        w1=mul(p,3) if (u>>first)&1 else {}
        Y1=plus(w1,const(-8*sum(g(u)*g(u^(1<<j)) for j in range(3) if j!=first)))
        ck(bounds(Y1)[1]<=16)
        for second in range(3):
            if second==first: continue
            rem=3-first-second
            Y2=plus(mul(q,2),const(-8*g(u)*g(u^(1<<rem))))
            ck(bounds(Y2)[1]<16)
for t in range(2,65):
    delta=Q(1,8**t)
    for r in range(t//2+1):
        n=t-r
        full=Q(3*n,4)-delta*(12*t+6+Q(118*n,9))-Q(t,64)
        part=Q(3*(n-1),4)+Q(5,6)-delta*(12*t+6+Q(118*(n-1),9)+16)-Q(t,64)
        ck(full>=Q(13*t,576)); ck(part>=Q(13*t,576)); cases+=3
obj={'status':'PASS','cases':cases,'assertions':count,'integer_log_certificates':6,'seconds':time.perf_counter()-start,
     'scope':'finite rational replay; all-t proof is PROOF equations8,10'}
(root/'out/scalar.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8',newline=''); print(json.dumps(obj))
