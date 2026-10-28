"""Second representation: direct characters; independently reconstruct saved certificates."""
from pathlib import Path
from fractions import Fraction as Q
import json, time, hashlib
from math import prod

root=Path(__file__).resolve().parents[1]
start=time.perf_counter();checked=0
def chk(b):
    global checked
    checked+=1
    assert b,checked
def chars(v):
    return [sum(z*(-1 if (x&s).bit_count()%2 else 1) for x,z in enumerate(v)) for s in range(len(v))]
cache={}
records=json.loads((root/'out/SOURCE_CERTIFICATES.json').read_text(encoding='utf-8'))
for row in records:
    r=row['r'];n=2*r+1;N=2**n
    if r not in cache:
        v=[(-1)**sum(not (x&1) and not(x&(3<<(2*j+1))) for j in range(r)) for x in range(N)]
        cache[r]=(v,chars(v))
    v,full=cache[r];coords=row['essential'];a=row['assignment']
    vc=[]
    for y in range(1<<len(coords)):
        x=sum((z if z!=-1 else 0)<<i for i,z in enumerate(a))
        x+=sum(((y>>j)&1)<<i for j,i in enumerate(coords))
        vc.append(v[x])
    chk(vc==row['truth']);w=chars(vc);D=len(vc)**2
    nums=[0]*len(vc)
    for s,z in enumerate(full):
        t=sum(bool(s&(1<<i))<<j for j,i in enumerate(coords));nums[t]+=z*z
    chk([[Q(z,N*N).numerator,Q(z,N*N).denominator] for z in nums]==row['reference'])
    inf=sum(sum(vc[x]!=vc[x^(1<<j)] for x in range(len(vc))) for j in range(len(coords)))
    exponent=Q(4*inf*D,len(vc));chk(exponent.denominator==1)
    # One common original denominator, rather than multiplying reduced fractions.
    odd=1;twos=0
    for z,c in zip(nums,w):
        if c:
            chk(z>0)
            power=(z&-z).bit_length()-1
            twos+=power*c*c;odd*=pow(z>>power,c*c)
    rhs_exp=(2*n)*D-int(exponent)-twos
    chk(rhs_exp<=0 or odd>=1<<rhs_exp)
    chk(sum(c*c for c in w)==D)
result={'status':'PASS','records':len(records),'checks':checked,
        'widths':sorted(cache),'seconds':time.perf_counter()-start,
        'independence':'Direct character sums; direct physical truth and edges; unreduced common-denominator integer product; no first-checker imports',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'out/AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
