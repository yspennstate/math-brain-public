"""Independent cut recurrence for A064's before/after information order."""
from pathlib import Path
from fractions import Fraction as F
import json,time
import check as C
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();count=0
def ck(b,label):
    global count
    count+=1
    if not b:raise AssertionError(label)
def add(*x):return C.plus(*x)
def pos(x):return C.maximum({},x)
def avg(a,b):return add((F(1,2),a),(F(1,2),b))
def cuts(costs,floor):
    if len(costs)==1:return C.maximum(floor,costs[0])
    n=len(costs)//2
    return C.maximum(floor,avg(cuts(costs[:n],floor),cuts(costs[n:],floor)))
for table in range(256):
    t=tuple(1 if table>>x&1 else -1 for x in range(8))
    p,d,H,M,q=C.stats(t);T=add((1,M),(-1,H))
    for depth in range(5):
        size=2**depth
        # One success leaf among fair outcomes; includes epsilon=1 and zero-T.
        terminal=[add((1,H),(1,T))]+[H]*(size-1)
        before=cuts(terminal,add((1,H),(1,C.const(2))))
        target_before=add((1,H),(1,C.const(2)),(F(1,size),pos(add((1,T),(-1,C.const(2))))))
        ck(before==target_before,'before-order every adapted cut Bellman value')
        after=C.maximum(add((1,H),(1,C.const(2))),cuts(terminal,H))
        target_after=add((1,H),(1,C.maximum(C.const(2),add((F(1,size),T)))))
        ck(after==target_after,'after-order every adapted cut Bellman value')
        C.nn(add((1,before),(-1,after)),'nonnegative order penalty')
        # Complete terminal always keeps H, even at reset failure.
        ck(add((1,H),(F(1,size),T))==add(*[(F(1,size),c) for c in terminal]),'both FULL terminal laws')
# Explicit unbounded-reserve mechanism at finite source.
T=add((64,C.plus((1,C.M(3)),(-1,C.H(3)))))
before=add((F(1,8),pos(add((1,T),(-1,C.const(2))))))
after=pos(add((F(1,8),T),(-1,C.const(2))))
ck(not after,'64 point3 factors epsilon1/8 have zero AFTER extra')
C.nn(add((1,before),(-1,C.const(F(11,8)))),'strict lower source before extra')
C.nn(add((1,C.const(F(3,2))),(-1,before)),'strict upper source before extra')
out={'status':'PASS','direct_core_tables':256,'lottery_depths':[0,1,2,3,4],'independent_cut_predicates':count,'interval_predicates':C.COUNT,'seconds':time.perf_counter()-start,'A064_verdict':'HOLDS at stated no-data-query scope; no repair; no arbitrary initial entropy price','before_extra':C.show(before),'after_extra':C.show(after)}
(R/'out/AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(out)
