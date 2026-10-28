"""Exact finite audit of the composition-prime perturbation theorem; v2."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import itertools
import json
import sys
import time

RUN = Path(__file__).resolve().parents[1]
START = time.monotonic()
COUNTS = {}

def check(ok, category):
    COUNTS[category] = COUNTS.get(category, 0) + 1
    if not ok:
        raise AssertionError(category)
    if time.monotonic() - START > 55:
        raise RuntimeError('Frozen runtime cap reached; incomplete is not pass')

def spectrum(v):
    a = list(v)
    step = 1
    while step < len(a):
        for j in range(0, len(a), 2*step):
            for t in range(step):
                u,w = a[j+t],a[j+t+step]
                a[j+t],a[j+t+step] = u+w,u-w
        step *= 2
    direct = [sum(y * (-1 if (x&s).bit_count()%2 else 1)
                  for x,y in enumerate(v)) for s in range(len(v))]
    check(a == direct, 'direct_Walsh_vs_butterfly')
    den = len(v)**2
    p = tuple(Q(x*x,den) for x in a)
    check(sum(p) == 1, 'Parseval')
    return p

def influences(v):
    n = len(v).bit_length()-1
    return [Q(sum(v[x] != v[x^(1<<i)] for x in range(len(v))), len(v))
            for i in range(n)]

def indices(mask):
    return [i for i in range(mask.bit_length()) if mask>>i&1]

def embed(x, coords):
    return sum(((x>>j)&1)<<i for j,i in enumerate(coords))

def rows(v, mask):
    n = len(v).bit_length()-1
    ac = indices(mask)
    bc = indices(((1<<n)-1)^mask)
    return [tuple(v[embed(a,ac)|embed(b,bc)] for b in range(1<<len(bc)))
            for a in range(1<<len(ac))]

def witness_rows(v, n, k, mask):
    N=n+k
    ac=indices(mask)
    bc=indices(((1<<N)-1)^mask)
    az=[i for i in ac if i>=n]
    bz=[i for i in bc if i>=n]
    if len(az)>=2:
        assignments=[0,1<<az[0],(1<<az[0])|(1<<az[1])]
        columns=[embed(b,bc) for b in range(1<<len(bc))]
    elif len(bz)>=2:
        assignments=[0,1<<ac[0],(1<<ac[0])|(1<<ac[1])]
        columns=[embed(b,bz) for b in range(1<<len(bz))]
    else:
        check(k==2 and len(az)==len(bz)==1, 'exhaustive_case_split')
        i=next(i for i in ac if i<n)
        assignments=[0,1<<az[0],1<<i,(1<<i)|(1<<az[0])]
        columns=[0,1<<bz[0]]
    return len({tuple(v[a|b] for b in columns) for a in assignments})

@lru_cache(None)
def ln_interval(x):
    assert x>0
    z=(x-1)/(x+1)
    assert 0<=z<=Q(1,3)
    total=Q(0)
    power=z
    for j in range(100):
        total+=2*power/(2*j+1)
        power*=z*z
    tail=2*power/(201*(1-z*z))
    return total,total+tail

@lru_cache(None)
def log_interval(x):
    assert x>0
    exponent=0
    while x<1:
        x*=2
        exponent-=1
    while x>=2:
        x/=2
        exponent+=1
    lo,hi=ln_interval(x)
    l2,u2=ln_interval(Q(2))
    return Q(exponent)+lo/u2,Q(exponent)+hi/l2

@lru_cache(None)
def entropy(p):
    lo=hi=Q(0)
    for x in p:
        if x:
            a,b=log_interval(x)
            lo-=x*b
            hi-=x*a
    return lo,hi

def seed(n,t):
    return tuple(-1 if t>>x&1 else 1 for x in range(1<<n))

def perturb(g,n,k):
    return tuple(g[x&((1<<n)-1)] * (-1 if x.bit_count()<=1 else 1)
                 for x in range(1<<(n+k)))

def run(pilot):
    count=blocks=0
    max_n=2 if pilot else 3
    for n in range(max_n+1):
        for k in (2,3):
            if n+k<3:
                continue
            N=n+k
            for t in range(1<<(1<<n)):
                g=seed(n,t)
                f=perturb(g,n,k)
                p=spectrum(f)
                base=tuple(g[x&((1<<n)-1)] for x in range(1<<N))
                q=spectrum(base)
                inf=influences(f)
                old=influences(base)
                check(all(z>0 for z in inf), 'all_physical_coordinates_relevant')
                check(sum(inf)==sum(s.bit_count()*p[s] for s in range(len(p))),
                      'physical_vs_spectral_influence')
                eps=Q(N+1,1<<N)
                check(Q(sum(a!=b for a,b in zip(f,base)),len(f))==eps,
                      'edit_probability')
                for a,b in zip(inf,old):
                    check(abs(a-b)<=2*eps, 'per_coordinate_influence_continuity')
                d=sum(abs(a-b) for a,b in zip(p,q))/2
                check(d*d<=4*eps,'spectral_TV_Cauchy_Schwarz')
                if d:
                    lo,hi=entropy(p)
                    a,b=entropy(q)
                    h,_=entropy((d,1-d))
                    check(max(hi-a,b-lo)<=h+N*d,'entropy_coupling_interval_sign')
                else:
                    check(sorted(p)==sorted(q),'zero_TV_boundary')
                for mask in range(1,1<<N):
                    if 2<=mask.bit_count()<=N-1:
                        check(len(set(rows(f,mask)))>=3,'all_proper_blocks')
                        check(witness_rows(f,n,k,mask)>=3,'independent_explicit_witness')
                        blocks+=1
                count+=1
    failures={}
    for k in (0,1):
        for n in range(4):
            N=n+k
            if N<3:
                continue
            for t in range(1<<(1<<n)):
                g=seed(n,t)
                f=perturb(g,n,k)
                found=False
                for mask in range(1,1<<N):
                    if 2<=mask.bit_count()<=N-1 and len(set(rows(f,mask)))<=2:
                        failures[str(k)]={'n':n,'k':k,'seed_negative_inputs':
                            [i for i,x in enumerate(g) if x<0],
                            'compressible_block_mask':mask,'rows':rows(f,mask)}
                        found=True
                        break
                if found:break
            if str(k) in failures:break
    check(set(failures)=={'0','1'},'missing_fresh_bits_actual_countercontrols')
    # The infinite inequalities are separately proved, not inferred from this grid.
    for n in range(1,33):
        for m in range(1,33):
            N=8*(n+m+2)
            eps=Q(N+1,1<<N)
            delta=Q(2,1<<(N//4))
            tol=Q(1,1<<m)
            imin=Q(2,1<<n)
            check(4*eps<=delta*delta,'schedule_TV_bound')
            check(0<delta<=Q(1,2),'schedule_entropy_domain')
            check(2*N*delta<=tol*imin,'uniform_relative_entropy_error')
            check(2*N*eps<=tol*imin,'uniform_relative_total_influence_error')
    out={'status':'PASS','proof_rung':'analytic proof plus exact finite validation; independent review pending',
         'cases':count,'proper_block_checks':blocks,'counts':COUNTS,
         'assertions':sum(COUNTS.values()),'boundary_countercontrols':failures,
         'runtime_seconds':time.monotonic()-START,
         'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'no_FEI_counterfamily_constructed':True}
    name='PILOT.json' if pilot else 'EXACT_RESULTS.json'
    (RUN/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:out[k] for k in ['status','cases','proper_block_checks','assertions','runtime_seconds']}))

if __name__=='__main__':
    run('--pilot' in sys.argv)
