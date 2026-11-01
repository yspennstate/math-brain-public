"""Outward rational boxes. No floating arithmetic in certified decisions."""
from fractions import Fraction as R
from functools import lru_cache
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
BITS=48; N=20; SCALE=1<<BITS
def down(x): return R(x.numerator*SCALE//x.denominator,SCALE)
def up(x): return -down(-x)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def mul(a,b):
    v=[x*y for x in a for y in b];return (min(v),max(v))
def sub(a,b):return add(a,neg(b))
def sq(a):return (R(0) if a[0]<=0<=a[1] else min(a[0]**2,a[1]**2),max(a[0]**2,a[1]**2))
def series(x):
    z=(x-1)/(x+1); z2=z*z; t=z; s=R(0)
    for j in range(N):s+=t/R(2*j+1);t*=z2
    tail=2*abs(t)/(R(2*N+1)*(1-z2))
    return (2*s-tail,2*s+tail)
L2=series(R(2))
@lru_cache(maxsize=12000)
def log2(x):
    assert x>0
    k=0
    while x<1:x*=2;k-=1
    while x>2:x/=2;k+=1
    a=series(x);v=[u/v+ k for u in a for v in L2]
    return down(min(v)),up(max(v))
def phi_point(x):
    if x==0 or x==1:return (R(0),R(0))
    return mul((-x,-x),log2(x))
def phi(x):
    lo,hi=x
    assert 0<=lo<=hi<=1
    if lo==hi:return phi_point(lo)
    if lo==0:
        if hi<=R(1,4):return (R(0),phi_point(hi)[1])
        return (R(0),R(1))
    return mul((-hi,-lo),(log2(lo)[0],log2(hi)[1]))
def hpoint(x):return add(phi_point(x),phi_point(1-x))
def h(x):
    a=hpoint(x[0]);b=hpoint(x[1])
    low=min(a[0],b[0])
    high=R(1) if x[0]<=R(1,2)<=x[1] else max(a[1],b[1])
    return low,high
ONE=(R(1),R(1)); FOUR=(R(4),R(4)); TWO=(R(2),R(2))
def bound(box):
    p=(box[0],box[1]);q=(box[2],box[3]);pc=sub(ONE,p);qc=sub(ONE,q)
    # Concavity gives tighter interval for 4q(1-q).
    endpoints=[4*x*(1-x) for x in q]
    r=(min(endpoints), R(1) if q[0]<=R(1,2)<=q[1] else max(endpoints))
    t=mul(p,r)
    a=sq(sub(ONE,mul(TWO,mul(p,q))))
    b=mul(FOUR,mul(mul(p,pc),sq(q)))
    c=mul(sq(p),r);d=mul(mul(p,pc),r)
    # Intervals may exceed 1 by dependency; intersect valid atom range.
    masses=[(max(R(0),x[0]),min(R(1),x[1])) for x in [a,b,c,d]]
    entropy=(R(0),R(0))
    for x in masses:entropy=add(entropy,phi(x))
    return sub(sub(mul(TWO,h(t)),mul(p,h(r))),entropy)
def serialize_box(box,iv):return {'box':[str(x) for x in box],'F_interval':[str(x) for x in iv]}
def cover(box,depth):
    stack=[(box,0)];leaves=[];visited=0
    while stack:
        b,d=stack.pop();visited+=1;v=bound(b)
        if v[0]>0 or v[1]<0 or d==depth:
            z=serialize_box(b,v);z['sign']='positive' if v[0]>0 else 'negative' if v[1]<0 else 'unresolved';leaves.append(z)
        else:
            j=0 if b[1]-b[0]>=b[3]-b[2] else 2;m=(b[j]+b[j+1])/2
            c=list(b);e=list(b);c[j+1]=m;e[j]=m
            stack.extend([(tuple(c),d+1),(tuple(e),d+1)])
    return {'initial_box':[str(x) for x in box],'max_depth':depth,'visited':visited,'leaves':leaves,'counts':{s:sum(z['sign']==s for z in leaves) for s in ['positive','negative','unresolved']}}
def main():
    start=time.perf_counter();(ROOT/'out').mkdir(exist_ok=True)
    targeted=cover((R(1,10),R(3,20),R(1,5),R(3,10)),8)
    (ROOT/'out'/'POSITIVE_RECTANGLE.json').write_text(json.dumps(targeted,indent=2),encoding='utf-8')
    print('target rectangle:',targeted['counts'],flush=True)
    assert targeted['counts']['unresolved']==0 and targeted['counts']['negative']==0
    compact=cover((R(1,16),R(15,16),R(1,16),R(15,16)),10)
    (ROOT/'out'/'COMPACT_COVER.json').write_text(json.dumps(compact,indent=2),encoding='utf-8')
    print('compact cover:',compact['counts'],flush=True)
    result={'runtime_seconds':time.perf_counter()-start,'exact_arithmetic':'Fraction; atanh log series N=20; range reduction [1,2]; outward 48-bit rational endpoints','target_rectangle':targeted['counts'],'compact':compact['counts'],'compact_visited':compact['visited'],'global_sign_map':'OPEN: unresolved boxes retained'}
    (ROOT/'out'/'RESULT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result),flush=True)
if __name__=='__main__':main()
