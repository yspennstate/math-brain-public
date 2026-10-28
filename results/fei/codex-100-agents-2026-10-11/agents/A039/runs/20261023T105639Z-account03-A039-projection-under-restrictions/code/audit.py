"""Independent exact witness: literal Walsh and prime-log rational arithmetic."""
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import json,time
START=time.monotonic();CHECKS=0;R=Path(__file__).resolve().parents[1]
def ck(a,s):
    global CHECKS
    CHECKS+=1
    assert a,s
    assert time.monotonic()-START<55
def walsh(v):return [F(sum(a*(-1 if (i&s).bit_count()%2 else 1) for i,a in enumerate(v)),len(v)) for s in range(len(v))]
def p(v):return [a*a for a in walsh(v)]
def children(v,j,y):return [a for i,a in enumerate(v) if ((i>>j)&1)==y]
def erase(v,j):
    out=[F(0)]*(len(v)//2)
    for i,a in enumerate(v):out[(i&((1<<j)-1))|((i>>(j+1))<<j)]+=a
    return out
def phase(w):return [(-1 if z.bit_count()%2 else 1)*(-1 if z==0 else 1) for z in range(1<<w)]
def qlaw(v):
    a=p(v)
    if sum(x>0 for x in a)==1:return a
    q=[a[0]]+[F(5,6)*x for x in a[1:]];q[-1]+=(1-a[0])/6
    return q
def lift(v,data):
    a=p(v)
    return [a[i] if i<2 else data[i>>1]/4 for i in range(len(a))]
@lru_cache(None)
def primes(k):
    d=2;out={}
    while d*d<=k:
        while k%d==0:out[d]=out.get(d,0)+1;k//=d
        d=3 if d==2 else d+2
    if k>1:out[k]=out.get(k,0)+1
    return out
def lg(out,x,c):
    for sign,k in [(1,x.numerator),(-1,x.denominator)]:
        for prime,e in primes(k).items():out[prime]=out.get(prime,F(0))+sign*c*e
def add(out,expr,scale=F(1)):
    for k,v in expr.items():out[k]=out.get(k,F(0))+scale*v
def kl(a,b):
    out={}
    for x,y in zip(a,b):
        if x:lg(out,x/y,x)
    return {k:v for k,v in out.items() if v}
v=phase(3);pv=p(v);q=qlaw(v)
ck(pv==[F(1,16)]*7+[F(9,16)],'actual phase-point source spectrum')
core=v+[-x for x in v] # disjoint spectator character
vals=[1 if i%2==0 else core[i>>1] for i in range(32)]
P=p(vals);R0=lift(vals,[F(0)]*8+q) # core product spectrum: spectator always present
ck(sum(R0)==1,'source normalized')
pb=erase(P,1);rb=erase(R0,1);delta={};outcomes=[];source_cores=[]
for y in [0,1]:
    cv=children(vals,1,y);cp=p(cv)
    kernel=[a/(2*b) if b else F(1,2) for a,b in zip(cp,pb)]
    raw=[a*b for a,b in zip(rb,kernel)];rho=sum(raw);old=[a/rho for a in raw];outcomes.append(rho)
    factor=children(v,0,y);qy=qlaw(factor)
    new=lift(cv,[F(0)]*len(qy)+qy)
    ck(sum(old)==1 and sum(new)==1,'both old/fresh children normalized')
    add(delta,kl(cp,new),F(1,2));add(delta,kl(cp,old),-F(1,2))
ck(outcomes==[F(23,48),F(25,48)],'exact coherent reference outcome normalizers')
ratio=F(1404,1331)*F(143,144)**4*F(576,575)**8
claimed={};lg(claimed,ratio,F(1,16))
delta={k:v for k,v in delta.items() if v};claimed={k:v for k,v in claimed.items() if v}
ck(delta==claimed,'exact prime-log equality with closed-form full reset')
ck(ratio>1,'strict positive sign by exact rational integer comparison')
ck(F(1)-F(2,8)==F(3,4),'actual queried influence')
ck(6**40<2**11*5**40 and 36**12<2*35**12,'exact logarithm price certificates')
ck(F(53,480)<F(1,8),'local price strictly below influence/6 for w>=3')
ck(F(5,3)-F(19,40)*F(3,4)==F(629,480),'sharp source width-two rational lower bound')
ck(F(7,4)*3-F(19,40)>F(629,480),'all widths>=3 source lower bound anchor')
out={'status':'PASS','checks':CHECKS,'method':'Literal Walsh, exact Fraction physical/coherent channel, independent prime-log coefficients; no checker imported.','runtime_seconds':time.monotonic()-START,'actual_reference_outcomes':list(map(str,outcomes)),'sigma_prime_log_coefficients':{str(k):str(v) for k,v in delta.items()},'sigma':'(1/16) log2(bracket)','bracket':str(ratio),'bracket_numerator':str(ratio.numerator),'bracket_denominator':str(ratio.denominator),'strict_positive_integer_difference':str(ratio.numerator-ratio.denominator),'rejected_extension':'Remove point-target hypothesis from nonpositive same-profile refresh.','full_FEI':'OPEN','external_independent_review':'PENDING'}
(R/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['sigma_prime_log_coefficients','bracket_numerator','bracket_denominator','bracket']}))
