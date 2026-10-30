"""A046 v1: independent exact two-bit source and logarithmic certificates."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]
TERMS = 24

@lru_cache(None)
def ln_unit(x):
    assert Q(1) <= x <= Q(2)
    z = (x-1)/(x+1)
    part = 2*sum((z**(2*j+1)/Q(2*j+1) for j in range(TERMS)), Q(0))
    tail = 2*z**(2*TERMS+1)/(Q(2*TERMS+1)*(1-z*z))
    return part, part+tail

def log2(x):
    assert x > 0
    k = 0
    while x < 1:
        x *= 2
        k -= 1
    while x >= 2:
        x /= 2
        k += 1
    a,b = ln_unit(x)
    c,d = ln_unit(Q(2))
    corners = [a/c,a/d,b/c,b/d]
    return k+min(corners), k+max(corners)

def entropy(law):
    assert sum(law)==1 and all(0<=x<=1 for x in law)
    lo=hi=Q(0)
    for x in law:
        if x:
            a,b=log2(x)
            lo -= x*b
            hi -= x*a
    return lo,hi

def sub(a,b):
    return a[0]-b[1],a[1]-b[0]

def scale(c,a):
    return min(c*a[0],c*a[1]),max(c*a[0],c*a[1])

def add(a,b):
    return a[0]+b[0],a[1]+b[1]

def outward(a,digits=15):
    factor=10**digits
    def render(v):
        sign='-' if v<0 else ''
        v=abs(v)
        return f'{sign}{v//factor}.{v%factor:0{digits}d}'
    low=a[0].numerator*factor//a[0].denominator
    high=-((-a[1].numerator*factor)//a[1].denominator)
    return [render(low),render(high)]

def masses(p,q):
    biases=[p,q]
    result=[]
    for mask in range(4):
        numerator=Q(0)
        denominator=Q(1)
        for i,bias in enumerate(biases):
            if mask>>i&1:
                denominator *= bias*(1-bias)
        for x in range(2):
            for y in range(2):
                coords=[x,y]
                weight=Q(1)
                basis=Q(1)
                for i,bias in enumerate(biases):
                    weight *= bias if coords[i] else 1-bias
                    if mask>>i&1:
                        basis *= coords[i]-bias
                numerator += (-1)**(x*y)*weight*basis
        result.append(numerator*numerator/denominator)
    assert sum(result)==1
    return result

def main():
    start=time.perf_counter()
    rows=[]
    # Known integer logarithms check both numerator sign domains and range reduction.
    for k in range(-8,9):
        a,b=log2(Q(2)**k)
        assert a<=k<=b
    for p in [Q(1,8),Q(1,16),Q(1,32),Q(1,64)]:
        q=Q(1,4)
        law=masses(p,q)
        expected=[(1-2*p*q)**2,4*p*(1-p)*q*q,
                  4*p*p*q*(1-q),4*p*(1-p)*q*(1-q)]
        assert law==expected
        r=4*p*q*(1-q)
        assert law[2]+law[3]==r
        hp=entropy(law)
        hr=entropy([r,1-r])
        hc=entropy([4*q*(1-q),1-4*q*(1-q)])
        M=sub(hp,hr)
        J=sub(hr,scale(p,hc))
        gap=sub(J,M)
        Delta=add(entropy([p,1-p]),log2(1-p))
        # Equivalent scalar tax identity, with interval containment sanity check.
        scalar=scale(p,log2((1-p)/p))
        assert max(Delta[0],scalar[0])<=min(Delta[1],scalar[1])
        assert gap[0]>0
        assert sub(Delta,gap)[0]>0
        if p==Q(1,8):
            assert law==[Q(225,256),Q(7,256),Q(3,256),Q(21,256)]
            assert gap[0]>Q(1195,10000)
        rows.append({'p':str(p),'q':str(q),'truth_table':[1,1,1,-1],
                     'masses':[str(x) for x in law],
                     'M_interval_bits':outward(M),'J_interval_bits':outward(J),
                     'J_minus_M_interval_bits':outward(gap),
                     'Delta_interval_bits':outward(Delta),
                     'gap_interval_rational':[str(x) for x in gap]})
    output={'status':'PASS','case_count':4,'arithmetic':'Fraction; rational atanh range reduction',
            'terms':TERMS,'no_floating_point_in_certificate':True,
            'runtime_seconds':time.perf_counter()-start,'rows':rows,
            'all_parameter_proof':'REPORT.md; not inferred from these four cases'}
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/'EXACT_CHECK.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in output.items() if k!='rows'},indent=2))

if __name__=='__main__':
    main()
