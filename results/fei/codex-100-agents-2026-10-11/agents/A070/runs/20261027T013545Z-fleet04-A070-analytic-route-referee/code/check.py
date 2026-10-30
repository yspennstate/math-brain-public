from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
import json, time, sys, hashlib

ROOT = Path(__file__).resolve().parents[1]
START = time.monotonic()
checks = 0

def ck(v):
    global checks
    assert v
    checks += 1
    if time.monotonic() - START > 55:
        raise TimeoutError('frozen 55-second arithmetic cap')

def fwht(v):
    v = list(v)
    step = 1
    while step < len(v):
        for i in range(0, len(v), 2 * step):
            for j in range(i, i + step):
                a, b = v[j], v[j + step]
                v[j], v[j + step] = a + b, a - b
        step *= 2
    return v

def product_values(m):
    n = m*m
    den = (n+1)**(n//2)
    vals = []
    for mask in range(1 << n):
        re, im = 1, 0
        for j in range(n):
            y = -1 if mask >> j & 1 else 1
            re, im = m*re-y*im, m*im+y*re
        ck(re*re+im*im == (n+1)**n)
        ck(im*im <= den*den)
        vals.append(F(im,den))
    return vals

def liftmask(s,b):
    return sum(((1 << b)-1) << (j*b) for j in range(5) if s >> j & 1)

def run_fixture(b,eps):
    h = product_values(2)
    vals = [(1 if not (x & 1) else -1)+eps*h[x >> 1] for x in range(32)]
    a = [v/F(32) for v in fwht(vals)]
    z = sum(v*v for v in a)
    ck(z == 1+eps*eps*F(272,625))
    sq = [v/F(32)/z for v in fwht([v*v for v in vals])]
    ck(sq[0] == 1)
    # Direct convolution, no author code or symbolic coefficient constructor.
    for t in range(32):
        ck(sum(a[s]*a[s^t] for s in range(32))/z == sq[t])
    lifted = {liftmask(s,b):v for s,v in enumerate(a) if v}
    sq_lift = {liftmask(s,b):v for s,v in enumerate(sq) if v}
    ck(min(s.bit_count() for s in sq_lift if s) == 2*b)
    ck(sum(v*v for v in lifted.values()) == z)
    ck(sum(s.bit_count()*v*v for s,v in lifted.items()) == b*sum(s.bit_count()*v*v for s,v in enumerate(a)))
    dim = 5*b
    shallow_states = 0
    # A restriction norm is the evaluation of precisely the square-spectrum
    # coefficients supported in the fixed mask. Test every mask and assignment.
    for r in range(2*b):
        for fixed in combinations(range(dim),r):
            mask = sum(1 << j for j in fixed)
            terms = {s:v for s,v in sq_lift.items() if s & ~mask == 0}
            ck(terms == {0:F(1)})
            for signs in range(1 << r):
                neg = sum(1 << j for q,j in enumerate(fixed) if signs >> q & 1)
                norm = sum(v*(-1 if (s&neg).bit_count()%2 else 1) for s,v in terms.items())
                ck(norm == 1)
                shallow_states += 1
    # Every physical value: parity construction, exact sign, and squared error.
    lifted_vals = []
    for x in range(1 << dim):
        old = sum((((x >> (j*b)) & ((1 << b)-1)).bit_count()%2) << j for j in range(5))
        u = vals[old]
        ck((u > 0) == (not (old & 1)))
        ck(abs(u*u/z-1) <= 2*eps+eps*eps)
        lifted_vals.append(u)
    # Independent full physical Walsh square verifies the lifted square support.
    direct_sq = fwht([v*v for v in lifted_vals])
    for s,v in enumerate(direct_sq):
        ck(v/F(1 << dim)/z == sq_lift.get(s,F(0)))
    # Exact first failure: fix the dictator block and one y block positive.
    fixed_mask = (1 << (2*b))-1
    norm = sum(v*v for x,v in enumerate(lifted_vals) if x & fixed_mask == 0)/F(1 << (dim-2*b))/z
    ck(norm == 1+2*eps*F(8,25)/z)
    ck(norm > 1)
    return {'b':b,'epsilon':str(eps),'Z':str(z),'shallow_states':shallow_states,'first_nonunit_norm':str(norm),'dimension':dim}

pilot = '--pilot' in sys.argv
fixtures = [run_fixture(b,e) for b in ([1] if pilot else [1,2,3]) for e in ([F(1,2)] if pilot else [F(1,2),F(1,4)])]
binomial_rows=[]
for m in ([2] if pilot else [2,4,8]):
    n=m*m
    p=F(1,n+1)
    r=1-2*p
    mass=sum(F(comb(n,s))*p**s*(1-p)**(n-s) for s in range(1,n+1,2))
    energy=sum(F(s*comb(n,s))*p**s*(1-p)**(n-s) for s in range(1,n+1,2))
    ck(mass == (1-r**n)/2)
    ck(mass > F(1,3))
    ck(energy == n*p*(1+r**(n-1))/2)
    ck(energy <= 1)
    for s in range(1,n+1,2):
        ck(p**s*(1-p)**(n-s) <= p)
    for b in ([1] if pilot else [1,2,3]):
        for eps in ([F(1,2)] if pilot else [F(1,2),F(1,4)]):
            z=1+eps*eps*mass
            j=b*(1+eps*eps*energy)/z
            ck(j > 0)
            ck(j <= b*(1+eps*eps))
            ck((eps*eps*mass/z)/j > eps*eps/(3*b*(1+eps*eps)))
            ck(eps*eps*p/z < p)
    binomial_rows.append({'n':n,'mass':str(mass),'energy':str(energy)})
result={'status':'PASS','checks':checks,'runtime_seconds':time.monotonic()-START,'pilot':pilot,'fixtures':fixtures,'binomial_rows':binomial_rows,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out=ROOT/'out'/('pilot.json' if pilot else 'results.json')
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','checks':checks,'runtime_seconds':result['runtime_seconds'],'output':str(out)}))
