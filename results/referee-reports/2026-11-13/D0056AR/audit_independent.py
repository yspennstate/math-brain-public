#!/usr/bin/env python3
"""Independent DR audit. No imports or execution from claim_files.

Small runs use Fraction convolutions. Long runs use FLINT integer polynomials,
128-bit quantization and a 256-bit upward-rounded transport error bound.
The support at time t is N-t+192, with a separately proved union bound.
"""
import os
for _key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'
import sys
from pathlib import Path
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).parent / 'audit_vendor'))
import argparse
import csv
import json
import math
import random
import resource
import time
from fractions import Fraction as F
from flint import arb, ctx, fmpq, fmpz_poly

ctx.threads = 1
ctx.prec = 320
BITS, EBITS, PAD = 128, 256, 192
S, R = 1 << BITS, 1 << EBITS
OUT = Path(__file__).parent / 'audit_results'


def ceildiv(x, y):
    return (x + y - 1) // y


def frac_convolve(p, q):
    a = [F(0)] * (len(p) + len(q) - 1)
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            a[i+j] += pi*qj
    return a


def exact_update(p, m, cutoff=None):
    a = [F(1)]
    for _ in range(m):
        a = frac_convolve(a, p)
    q = [a[0]+a[1]] + a[2:]
    if cutoff is not None and len(q) > cutoff+1:
        q[0] += sum(q[cutoff+1:])
        q = q[:cutoff+1]
    assert sum(q) == 1
    return q


def pgf(p, s):
    return sum(pk*s**k for k, pk in enumerate(p))


def defect(p, m):
    return sum(((m-1)*k-1)*pk*m**k for k, pk in enumerate(p))


def transport(p, q, m):
    """Exact W1 distance after x -> m**x, via cumulative probabilities."""
    cp = cq = ans = F(0)
    for k in range(max(len(p), len(q))-1):
        cp += p[k] if k < len(p) else 0
        cq += q[k] if k < len(q) else 0
        ans += abs(cp-cq)*(m**(k+1)-m**k)
    return ans


def survival_ceiling(a, m):
    v = 0
    for ak in reversed(a[1:]):
        v = ceildiv(v+ak, m)
    return v


def integer_update(a, m, cutoff, error):
    """All polynomial arithmetic exact. Only explicit floors lose precision."""
    zero = S-survival_ceiling(a, m)
    assert zero >= 0
    poly = fmpz_poly([zero]+a[1:])
    powered = poly.pow_trunc(m, cutoff+2)
    divisor = m * S**(m-1)
    new = [0]+[int(powered[k+1]//divisor) for k in range(1, cutoff+1)]
    # M <= 1 + sum(a)/S, and exact deleted-law moment <= M + error/R.
    mg = ((S+sum(a)) << (EBITS-BITS)) + error
    error = ceildiv(mg**(m-1)*error, R**(m-1))
    error += (cutoff+m) << (EBITS-BITS)
    return new, error


def small_checks():
    rng = random.Random(10091)
    rows = []
    identities = coupling_checks = bound_checks = quant_checks = 0
    for m in (2, 3):
        examples = []
        for k in (2, 5):
            pk = F(1, 1+((m-1)*k-1)*m**k)
            examples.append(('two'+str(k), [1-pk]+[F(0)]*(k-1)+[pk], True))
        examples += [('arbitrary', [F(1,2),F(1,3),F(1,6)], False)]
        for name, p, critical in examples:
            for n in range(4):
                new = exact_update(p, m)
                g = pgf(p, F(m)); gnew = pgf(new, F(m))
                q = 1-p[0]
                assert m*gnew == g**m+(m-1)*(1-q)**m
                assert defect(new,m) == defect(p,m)*g**(m-1)
                for s in (F(1,2),F(3,2),F(m)):
                    assert pgf(new,s) == pgf(p,s)**m/s+(1-1/s)*p[0]**m
                if critical:
                    assert defect(p,m) == 0
                identities += 5
                rows.append(dict(m=m,law=name,n=n,q=str(q),G=str(g),
                                 Gnext=str(gnew),support=len(p)-1))
                p = new
        # Small exact truncated trajectories versus independently quantized runs.
        for k in (2,5):
            pk=F(1,1+((m-1)*k-1)*m**k)
            p=[1-pk]+[F(0)]*(k-1)+[pk]
            cutoff=8
            a=[0]+[int((p[j] if j<len(p) else 0)*m**j*S)
                   for j in range(1,cutoff+1)]
            e=cutoff << (EBITS-BITS)
            for n in range(7):
                qp=1-p[0]; v=survival_ceiling(a,m)
                assert F(v-1,S)-F(e,R*(m-1)) <= qp <= F(v,S)+F(e,R*(m-1))
                quant_checks += 1
                p=exact_update(p,m,cutoff)
                a,e=integer_update(a,m,cutoff,e)
        # Exact check of the support-bound mechanism where deletion is nontrivial.
        pk=F(1,1+(2*(m-1)-1)*m**2)
        p=[1-pk,F(0),pk]; truncated=p[:]
        for n in range(4):
            error=(1-p[0])-(1-truncated[0])
            # Use rational B=m; this is slightly looser than the report's B.
            bound=F(m,m**9)*F(m**(n+1)-1,m-1)
            assert 0 <= error <= bound
            bound_checks+=1
            p=exact_update(p,m)
            truncated=exact_update(truncated,m,8)
        for _ in range(30):
            v=[rng.randrange(1,10) for _ in range(4)]
            w=[rng.randrange(1,10) for _ in range(4)]
            p=[F(x,sum(v)) for x in v]; q=[F(x,sum(w)) for x in w]
            d=transport(p,q,m); M=max(pgf(p,m),pgf(q,m))
            assert transport(exact_update(p,m),exact_update(q,m),m)<=M**(m-1)*d
            pp=[p[0]+p[3],p[1],p[2]]; qq=[q[0]+q[3],q[1],q[2]]
            assert transport(pp,qq,m)<=d
            assert abs(p[0]-q[0])<=d/(m-1)
            coupling_checks+=3
    OUT.mkdir(exist_ok=True)
    with (OUT/'exact_small.csv').open('w') as f:
        wr=csv.DictWriter(f,fieldnames=rows[0].keys());wr.writeheader();wr.writerows(rows)
    result=dict(identities=identities,quantized_enclosures=quant_checks,
                transport_inequalities=coupling_checks,truncation_enclosures=bound_checks)
    (OUT/'exact_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result,flush=True)


def floor_ball(x):
    ans=x.floor().unique_fmpz()
    if ans is None:
        raise ArithmeticError('initial coefficient floor not certified: '+str(x))
    return int(ans)


def initialize(m, law, cutoff):
    a=[0]*(cutoff+1)
    if law.startswith('two'):
        k=int(law[3:]); a[k]=S*m**k//(1+((m-1)*k-1)*m**k)
    elif law=='geom':
        c=1/(F(2*(m-1)-1)+F(1,2*m-1))
        for k in range(1,cutoff+1):
            a[k]=int(c*S/F(2)**k)
    elif law=='sparse':
        # Sum ten terms, bounding the entire remaining unweighted a_j sum by 1.
        t=sum(arb(m)**(-2**j)/(j*j*2**j) for j in range(1,11))
        t += arb(0,arb(m)**(-2**11))
        aa=(m-1)*arb(2).zeta()-(arb(1)/2).polylog(2)
        c=1/(aa+t)
        for j in range(1,cutoff.bit_length()):
            k=2**j
            if k<=cutoff:
                a[k]=floor_ball(c*S/(j*j*k))
    elif law.startswith('power'):
        b=arb(law[5:])
        c=1/((m-1)*(b-1).zeta()-b.zeta()+(arb(1)/m).polylog(b))
        for k in range(1,cutoff+1):
            a[k]=floor_ball(c*S/(arb(k)**b))
    else:
        raise ValueError(law)
    count=sum(x>0 for x in a)
    if law=='geom':
        # Some strictly positive exact geometric coefficients round to zero.
        # Check their combined loss too, rather than silently omitting them
        # from the initial error count. Here c is an exact Fraction.
        exact_tilted_sum=c*(1-F(1,2**cutoff))
        assert exact_tilted_sum-F(sum(a),S) <= F(count,S)
    return a,count << (EBITS-BITS)


def run(m, law, N):
    try:
        os.nice(15)
    except OSError:
        pass
    start=time.monotonic(); cutoff=N+PAD
    a,error=initialize(m,law,cutoff)
    rows=[]
    for n in range(N+1):
        if n<=10 or n%50==0 or ((n+1)&n)==0 or n==N:
            v=survival_ceiling(a,m)
            # Adaptive support bound, with rational B=m:
            # m*sum_{j=0}^n m^{n-j-(N-j+PAD+1)} = (n+1)*m^{n-N-PAD}.
            tail=F(n+1,m**(N+PAD-n))
            lo=F(v-1,S)-F(error,R*(m-1))
            hi=F(v,S)+F(error,R*(m-1))+tail
            rows.append(dict(n=n,n2q=format(n*n*v/S,'.17g'),
                             lower=str(lo*n*n),upper=str(hi*n*n),
                             quantization_bound=float(F(error,R*(m-1))),
                             support_bound=float(tail),cutoff=len(a)-1))
        if n==N:
            break
        a,error=integer_update(a,m,N-(n+1)+PAD,error)
        if (n+1)%1000==0:
            print(m,law,n+1,'seconds',round(time.monotonic()-start,2),flush=True)
    OUT.mkdir(exist_ok=True)
    stem=f'm{m}_{law}_N{N}'
    with (OUT/(stem+'.csv')).open('w') as f:
        wr=csv.DictWriter(f,fieldnames=rows[0].keys());wr.writeheader();wr.writerows(rows)
    metadata=dict(m=m,law=law,N=N,bits=BITS,error_bits=EBITS,pad=PAD,
                  seconds=time.monotonic()-start,threads=1,
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  exact_integer_convolution=True,
                  final_scaled_value=rows[-1]['n2q'],final_interval=[rows[-1]['lower'],rows[-1]['upper']])
    (OUT/(stem+'.json')).write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps(metadata),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--small',action='store_true')
    parser.add_argument('--m',type=int);parser.add_argument('--law');parser.add_argument('--N',type=int,default=10000)
    args=parser.parse_args()
    if args.small: small_checks()
    else: run(args.m,args.law,args.N)
