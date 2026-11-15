"""Independent descending-overlap recurrence and exact checks of proof bounds."""
import json
import math
import os
import resource
import time
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS,0)>=15
start=time.monotonic()

def e(j):
    return j*(j-1)//2

def make_n(exponent,t):
    # Newton inversion in Decimal, independent of verify_moments.py's
    # double-precision bisection. The integer needs fewer than 100 digits.
    with localcontext() as ctx:
        ctx.prec=140
        ell=Decimal(2).ln()
        c=1+ell.ln()
        y=Decimal(exponent)*ell
        f=2/ell*(y-y.ln()+c)-1
        m=int(f)
        target=Decimal(m)+Decimal(t)
        z=(target+1)*ell/2-c
        for _ in range(20):
            y-=(y-y.ln()-z)/(1-1/y)
        assert abs(2/ell*(y-y.ln()+c)-1-target)<Decimal('1e-120')
        return int(y.exp().to_integral_value()),m

def audit_pair(n,K,l):
    # Start at full containment, descend via exact integer recurrence.
    c=math.comb(K,l)
    h_end=c
    S=0
    raw_low=raw_high=0
    m=l//2
    for j in range(l,-1,-1):
        # This identity checks the recurrence against direct counting.
        assert c==math.comb(K,j)*math.comb(n-K,l-j)
        S+=c*(2**e(j)-1)
        if 2<=j<=m:
            raw_low+=c*2**e(j)
        elif m<j<l:
            raw_high+=c*2**e(j)
        if j:
            num=c*j*(n-K-l+j)
            den=(K-j+1)*(l-j+1)
            c,rem=divmod(num,den)
            assert rem==0

    # Directly audit both convexity bounds, as exact rational inequalities.
    A=Fraction(K*l,n-l)
    def v(j):
        return A**j*2**e(j)
    low_bound=m*max(v(2),v(m))
    assert Fraction(raw_low,math.comb(n,l))<=low_bound
    B=Fraction(K*n,2**l)
    def w(s):
        return B**s*2**(s*(s+1)//2)
    mp=(l+1)//2
    high_bound=mp*max(w(1),w(mp))
    assert Fraction(raw_high,h_end*2**e(l))<=high_bound
    assert v(m)<v(2)
    assert w(mp)<w(1)
    normalized=Fraction(S,h_end*2**e(l))
    return dict(K=K,l=l,normalized_moment=float(normalized),
                excess_over_one=float(normalized-1),
                low_bound_ratio=float(Fraction(raw_low,math.comb(n,l))/low_bound),
                high_bound_ratio=float(Fraction(raw_high,h_end*2**e(l))/high_bound))

rows=[]
for phase in ('0.25','0.5','0.75'):
    n,k=make_n(320,phase)
    pairs=[audit_pair(n,k,k),audit_pair(n,k-1,k-1),audit_pair(n,k,k-1)]
    # Double-count containment pairs in both directions, without logs.
    assert math.comb(n,k)*k==math.comb(n,k-1)*(n-k+1)
    rows.append(dict(target_phase=phase,log2_n=math.log2(n),k=k,pairs=pairs))

result=dict(status='all exact audits passed',nice=os.getpriority(os.PRIO_PROCESS,0),
            rows=rows,elapsed_seconds=time.monotonic()-start,
            peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path('extension_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
