"""A028-check-v1: independent integer/rational reconstruction, no floating signs."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json, time

ROOT = Path(__file__).resolve().parents[1]
START = time.monotonic()
checks = 0

def check(x):
    global checks
    assert x
    checks += 1

def walsh(table):
    a = list(table)
    step = 1
    while step < len(a):
        for base in range(0, len(a), 2*step):
            for j in range(base, base+step):
                u, v = a[j], a[j+step]
                a[j], a[j+step] = u+v, u-v
        step *= 2
    return a

def factors(n):
    result = {}
    q = 2
    while q*q <= n:
        while n % q == 0:
            result[q] = result.get(q, 0)+1
            n //= q
        q += 1
    if n > 1:
        result[n] = result.get(n, 0)+1
    return result

def plus(*terms):
    result = {}
    for term in terms:
        for k, v in term.items():
            result[k] = result.get(k, F(0))+v
    return {k:v for k,v in result.items() if v}

def scale(a, c):
    return {k:v*c for k,v in a.items() if v*c}

def log(q):
    q = F(q)
    assert q > 0
    return plus({k:F(v) for k,v in factors(q.numerator).items()},
                {k:F(-v) for k,v in factors(q.denominator).items()})

def eta(q):
    return {} if not q else scale(log(q), -q)

def entropy(ps):
    return plus(*(eta(q) for q in ps))

def hb(q):
    return entropy([q, 1-q])

def spectrum(table):
    N = len(table)
    return [F(c*c, N*N) for c in walsh(table)]

def influence(ps):
    return sum((q*s.bit_count() for s,q in enumerate(ps)), F(0))

def edges(table):
    n = (len(table)-1).bit_length()
    return sum((F(sum(table[x] != table[x^(1<<i)] for x in range(len(table))),len(table))
                for i in range(n)), F(0))

def activated(g, r):
    return [val if z == 0 else 1 for z in range(1<<r) for val in g]

activation_cases = 0
for n in range(4):
    N = 1<<n
    for code in range(1<<N):
        g = [1 if (code>>x)&1 else -1 for x in range(N)]
        ps = spectrum(g)
        Hg = entropy(ps)
        Ig = influence(ps)
        delta = F(g.count(-1), N)
        m, v = 1-2*delta, 4*delta*(1-delta)
        check(Ig == edges(g))
        last = Hg
        path = {}
        mismatch_path = {}
        for r in range(1,5):
            p = F(1,1<<r)
            table = activated(g,r)
            pf = spectrum(table)
            Hf = entropy(pf)
            check(influence(pf) == edges(table) == p*Ig+2*r*p*delta)
            # Spectrum independently compared with direct coefficient law.
            for s,q in enumerate(pf):
                T = s % N
                check(q == ((1-2*p*delta)**2 if s == 0 else
                            p*p*ps[T] if T else 4*p*p*delta*delta))
            bill = plus(Hf, scale(Hg,-p))
            formula = plus(eta((1-2*p*delta)**2), scale(eta(m*m),-p),
                           scale(eta(4*p*p*delta*delta), (1-p)/p),
                           {2:2*r*p*v})
            check(bill == formula)
            # Physical sequential control tree: each failure is constant.
            step_bill = plus(Hf,scale(last,F(-1,2)))
            path = plus(step_bill,scale(path,F(1,2)))
            check(path == bill)
            # Construct the actual children and their magnitude mismatch law.
            child = activated(g,r-1)
            child_a = [F(a,len(child)) for a in walsh(child)]
            qlaw = [(F(int(i==0))+a*a)/2 for i,a in enumerate(child_a)]
            mlaw = [(F(int(i==0))-abs(a))**2/4 for i,a in enumerate(child_a)]
            mu = sum(mlaw)
            check(mu == (2*p*delta if r>=2 else min(delta,1-delta)))
            m0 = mu*mu
            check(mlaw[0] == m0)
            J = plus(*(scale(log(q/m),m) for q,m in zip(qlaw,mlaw) if m))
            closed_J = plus({2:mu-m0},scale(log(qlaw[0]/m0),m0) if m0 else {})
            check(J == closed_J)
            mismatch_path = plus(J,scale(mismatch_path,F(1,2)))
            check(sum(mlaw) <= 2*p*delta)
            # Independent core-block conditional entropy and A027 transport.
            groups = [pf[u*N:(u+1)*N] for u in range(1<<r)]
            B = plus(*(plus(entropy(qs),scale(eta(sum(qs)), -1)) for qs in groups))
            R0 = 1-4*p*delta+4*p*p*delta
            L = entropy([q/v for q in ps[1:]]) if v else {}
            rhs = plus(scale(L,p*v),scale(hb(delta),4*p*delta*(1-p)),
                       scale(hb(p*p*v/R0),R0) if R0 else {})
            check(B == rhs)
            check(influence(pf) == p*Ig+2*r*p*delta)
            last = Hf
            activation_cases += 1

# Independent complete proxy reconstruction, global sign quotient only.
census = []
for n in range(1,5):
    N = 1<<n
    worst = F(0)
    witness = None
    reps = 1<<(N-1)
    for code in range(reps):
        table = [1]+[1 if (code>>(x-1))&1 else -1 for x in range(1,N)]
        a = walsh(table)
        candidates = []
        for i in range(n):
            bit = 1<<i
            den = sum(a[s]**2 for s in range(N) if s&bit)
            if den:
                num = 2*sum(abs(a[s]*a[s|bit]) for s in range(N) if not s&bit)
                candidates.append(F(num,den))
        val = min(candidates) if candidates else F(0)
        check(val <= [0,0,2,3,F(7,2)][n])
        if val > worst:
            worst,witness = val,code
    check(worst == [0,0,2,3,F(7,2)][n])
    census.append({'n':n,'representatives':reps,'max_min_proxy':str(worst),'witness':witness})

# Review A026 threshold obstruction by combinatorial Walsh coefficients.
n,t = 32,24
coeff = []
for k in range(n+1):
    val = sum((1 if j>=t else -1)*sum((-1)**ell*comb(k,ell)*comb(n-k,j-ell)
              for ell in range(max(0,j-(n-k)),min(k,j)+1)) for j in range(n+1))
    coeff.append(val)
den = sum(comb(n-1,j)*coeff[j+1]**2 for j in range(n))
num = 2*sum(comb(n-1,j)*abs(coeff[j]*coeff[j+1]) for j in range(n))
ratio = F(num,den)
check(ratio == F(2220940451,536870912))
check(ratio > 4)

out = {'helper':'A028-check-v2','arithmetic':'integer/Fraction/prime-log coefficient vectors',
       'activation_cases':activation_cases,'census':census,'threshold_proxy_ratio':str(ratio),
       'assertions_passed':checks,'compute_seconds':time.monotonic()-START,
       'finite_scope':'Equalities and proxy order are exact. Infinite activation upper bound is analytic in REPORT.md.'}
(ROOT/'out'/'validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
