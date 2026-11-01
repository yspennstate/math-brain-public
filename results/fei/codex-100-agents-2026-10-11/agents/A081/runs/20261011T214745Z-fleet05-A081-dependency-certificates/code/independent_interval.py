"""Independent small rational certificate using dyadic range reduction."""
from fractions import Fraction as Q
from pathlib import Path
import json,time
RUN=Path(__file__).resolve().parents[1]
spec={'helper_version':'independent_interval.py v1','family':'One actual Boolean gate g=(-1)^(XY), independent p=1/8,q=1/4','domain':'physical block A={X}; exactly one case','case_count':1,'symmetry':'none','arithmetic':'Fraction, dyadic logarithm range reduction, 32 atanh terms and proved tail','memory_estimate_MB':16,'maximum_runtime_seconds':60}
(RUN/'out/INTERVAL_FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
started=time.perf_counter()
def ln_small(x):
    assert 1<=x<=2
    z=(x-1)/(x+1); power=z; total=Q(0)
    for j in range(32):
        total+=2*power/(2*j+1); power*=z*z
    tail=2*power/(65*(1-z*z))
    return total,total+tail
LN2=ln_small(Q(2))
def log2(x):
    assert x>0
    m=0
    while x<1: x*=2; m-=1
    while x>=2: x/=2; m+=1
    lo,hi=ln_small(x)
    return Q(m)+lo/LN2[1],Q(m)+hi/LN2[0]
def entropy(ps):
    assert sum(ps)==1 and all(p>=0 for p in ps)
    lo=hi=Q(0)
    for p in ps:
        if not p: continue
        a,b=log2(p); lo-=p*b; hi-=p*a
    return lo,hi
def sub(a,b): return a[0]-b[1],a[1]-b[0]
def binary(p): return entropy([p,1-p])
def outward(a,digits=18):
    b=10**digits
    def s(n):
        sign='-' if n<0 else ''; n=abs(n)
        return f'{sign}{n//b}.{n%b:0{digits}d}'
    return [s(a[0].numerator*b//a[0].denominator),s(-((-a[1].numerator*b)//a[1].denominator))]
# Derive the squares directly from the biased gate, rather than copying them.
p=Q(1,8); q=Q(1,4)
masses=[(1-2*p*q)**2,4*q*q*p*(1-p),4*p*p*q*(1-q),4*p*(1-p)*q*(1-q)]
assert masses==[Q(v,256) for v in (225,7,3,21)]
H=entropy(masses); B=binary(Q(3,32)); child=binary(Q(3,4))
M=sub(H,B); J=sub(B,(child[0]/8,child[1]/8)); gap=sub(J,M)
assert gap[0]>Q(1195,10000)
assert Q(119545016024424957,10**18)<=gap[0]<=gap[1]<=Q(119545016024424958,10**18)
for k in range(-16,17):
    a,b=log2(Q(2)**k); assert a<=k<=b
assert time.perf_counter()-started<60
result={'status':'PASS','M_interval':outward(M),'J_interval':outward(J),'gap_interval':outward(gap),'gap_lower_exact':str(gap[0]),'gap_upper_exact':str(gap[1]),'terms':32,'exact_power_log_cases':33,'elapsed_seconds':time.perf_counter()-started,'proof_of_error':'After multiplying x by 2^(-m) into [1,2), z=(x-1)/(x+1)<=1/3. ln(x)=2 sum z^(2j+1)/(2j+1), omitted tail between 0 and 2z^65/(65(1-z^2)). Quotient numerator nonnegative; add exact integer m after division.','full_FEI':'OPEN'}
(RUN/'out/INDEPENDENT_INTERVAL.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if not k.endswith('_exact')},indent=2))
