#!/usr/bin/env python3
"""Exact, one-thread checks for PROOF.md. Standard library only."""
import json
import math
import os
import resource
import time
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path

K = 8
started = time.monotonic()
priority = os.getpriority(os.PRIO_PROCESS, 0)

def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return trim(out)

def trim(a):
    while len(a) > 1 and not a[-1]: a.pop()
    return a

def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return trim(out)

def scale(a, x): return trim([x*y for y in a])

def power(a, d):
    out = [F(1)]
    for _ in range(d): out = mul(out, a)
    return out

def evaluate(a, z):
    out = F(0)
    for x in reversed(a): out = out*z+x
    return out

def dfact(j): return math.prod(range(1, 2*j, 2))

mu = [F(1)] + [F(2**(j-1)*dfact(j)) for j in range(1, K+1)]
lam = [F(0)]*(K+1)
for j in range(1, K+1):
    lam[j] = mu[j] - sum(F(math.comb(j-1, r-1))*lam[r]*mu[j-r] for r in range(1, j))

# Independently derive lambda from (log M_Y)' = Catalan(s)/(1-4s).
catalan = [math.comb(2*j, j)//(j+1) for j in range(K)]
for j in range(1, K+1):
    assert lam[j] == math.factorial(j-1)*sum(catalan[a]*4**(j-1-a) for a in range(j))

# A_j(z): sample-mean moments, by the moment/cumulant recurrence.
a = [[F(1)]]
for j in range(1, K+1):
    value = [F(0)]
    for r in range(1, j+1):
        value = add(value, [F(0)]*(r-1) + scale(a[j-r], F(math.comb(j-1,r-1))*lam[r]))
    a.append(value)

# Independent exact conditioning: B~Bin(n,1/2), F_n = (2/n) chi^2_B.
checks_binomial = 0
for n in range(1, 13):
    for j in range(1, K+1):
        conditional = sum(F(math.comb(n,b), 2**n)*math.prod(b+2*s for s in range(j)) for b in range(n+1))
        conditional *= F(2,n)**j
        assert conditional == evaluate(a[j], F(1,n))
        checks_binomial += 1

# Logarithmic coefficients, independently by A' = A (log A)'.
log_coeffs = []
for j in range(K+1):
    aj = a[j]
    ll = [F(0)] * 4
    for m in range(1, 4):
        am = aj[m] if m < len(aj) else F(0)
        ll[m] = am - sum(F(r,m)*ll[r]*(aj[m-r] if m-r < len(aj) else 0) for r in range(1,m))
    assert ll[1] == 5*math.comb(j,2)
    assert ll[2] == -F(25,2)*math.comb(j,2)-31*math.comb(j,3)
    log_coeffs.append(ll)

def cumulant_polys(moments):
    kap = [[F(0)]]
    for j in range(1,len(moments)):
        value = moments[j][:]
        for r in range(1,j):
            value = add(value,scale(mul(kap[r], moments[j-r]),-math.comb(j-1,r-1)))
        kap.append(value)
    return kap

fixed_checks = 0
majorant_checks = 0
for d in range(1,5):
    kap = cumulant_polys([power(aj,d) for aj in a])
    for k in range(2,K+1):
        assert all(x == 0 for x in kap[k][:k-1])
        assert all(x >= 0 for x in kap[k])
        fixed_checks += 1
        S = [F(0)] + [math.comb(k,r)*lam[r] for r in range(2,k+1)]
        s = [F(1)]
        for h in range(1,len(kap[k])):
            s.append(sum(r*S[r]*s[h-r] for r in range(1,min(h,k-1)+1))/h)
        assert all(coef <= d**h*s[h] for h,coef in enumerate(kap[k]))
        majorant_checks += 1

# Derive scalar output cumulants directly from its even moments, separately
# from extracting formal Gaussian-mixture coefficients.
qmom = [evaluate(aj,F(1,7))**3 for aj in a]
qkap = [F(0)]*(K+1)
for j in range(1,K+1):
    qkap[j] = qmom[j]-sum(math.comb(j-1,r-1)*qkap[r]*qmom[j-r] for r in range(1,j))
xmom = [F(0)]*(2*K+1)
xmom[0] = F(1)
for j in range(1,K+1): xmom[2*j] = dfact(j)*qmom[j]
xkap = [F(0)]*(2*K+1)
for j in range(1,2*K+1):
    xkap[j] = xmom[j]-sum(math.comb(j-1,r-1)*xkap[r]*xmom[j-r] for r in range(1,j))
for j in range(1,K+1):
    assert xkap[2*j] == dfact(j)*qkap[j]
    assert xkap[2*j-1] == 0

# Enumerate set partitions, then independently enumerate connected layered hypergraphs.
def partitions(items):
    if not items:
        yield []
        return
    first, *rest = items
    for pi in partitions(rest):
        yield [(first,)] + pi
        for b in range(len(pi)):
            yield pi[:b] + [(first,)+pi[b]] + pi[b+1:]

import itertools
hyper_checks = 0
for k in range(2,5):
    ps = list(partitions(list(range(k))))
    for d in range(1,4):
        coeff = [F(0)]*(d*(k-1)+1)
        for layers in itertools.product(ps, repeat=d):
            parent = list(range(k))
            def root(x):
                while parent[x] != x: x = parent[x]
                return x
            cost, weight = 0, F(1)
            for pi in layers:
                for block in pi:
                    cost += len(block)-1
                    weight *= lam[len(block)]
                    for v in block[1:]: parent[root(v)] = root(block[0])
            if len({root(v) for v in range(k)}) == 1: coeff[cost] += weight
        expected = cumulant_polys([power(aj,d) for aj in a[:k+1]])[k]
        assert trim(coeff) == expected
        hyper_checks += 1

# Leading width coefficients for k=2,3,4: independently fit d-polynomials.
leading = {}
for k in range(2,5):
    vals = []
    for d in range(1,6):
        kap = cumulant_polys([power(aj,d) for aj in a[:k+1]])[k]
        vals.append(kap[k-1])
        expected = {2:5*d, 3:75*d*d-31*d, 4:2000*d**3-1860*d*d+418*d}[k]
        assert kap[k-1] == expected
    leading[str(k)] = [str(x) for x in vals]

# Partition formulas at t=d/n: Decimal avoids catastrophic cumulant cancellation.
def dec(x): return Decimal(x.numerator)/Decimal(x.denominator)

def moments_to_cumulants(m):
    kap = [Decimal(0)]*len(m)
    for j in range(1,len(m)):
        kap[j] = m[j] - sum(Decimal(math.comb(j-1,r-1))*kap[r]*m[j-r] for r in range(1,j))
    return kap

rows = []
with localcontext() as ctx:
    ctx.prec = 90
    for t in (F(1,10), F(1,2), F(1)):
        for n in (512,1024,2048,4096):
            # t=1/10 requires integer d. Use multiples of 10 in that row.
            nn = n*5 if t == F(1,10) else n
            d = int(t*nn)
            assert F(d,nn) == t
            td = dec(t)
            exact_m = [dec(evaluate(aj,F(1,nn)))**d for aj in a[:5]]
            exact = moments_to_cumulants(exact_m)
            # Direct partition coefficients, separate from the recurrence above.
            for k in (2,3,4):
                b0 = b1 = b2 = Decimal(0)
                for pi in partitions(list(range(k))):
                    p = len(pi)
                    mob = Decimal((-1)**(p-1)*math.factorial(p-1))
                    hs = [sum((log_coeffs[len(block)][r] for block in pi),F(0)) for r in (1,2,3)]
                    ex = (td*dec(hs[0])).exp()
                    b0 += mob*ex
                    b1 += mob*ex*td*dec(hs[1])
                    b2 += mob*ex*(td*dec(hs[2])+(td*dec(hs[1]))**2/2)
                err0 = abs(exact[k]-b0)
                err1 = abs(exact[k]-b0-b1/nn)
                err2 = abs(exact[k]-b0-b1/nn-b2/(nn*nn))
                et = lambda a: (a*td).exp()
                f0 = {2: et(5)-1, 3: et(15)-3*et(5)+2,
                      4: et(30)-4*et(15)-3*et(10)+12*et(5)-6}[k]
                f1 = {2:-Decimal(25)/2*td*et(5),
                      3:td/2*(-137*et(15)+75*et(5)),
                      4:td*(-199*et(30)+274*et(15)+75*et(10)-150*et(5))}[k]
                assert abs(f0-b0) < Decimal('1e-65')
                assert abs(f1-b1) < Decimal('1e-65')
                rows.append(dict(k=k,t=str(t),n=nn,d=d,
                    exact=str(exact[k]),B0=str(b0),B1=str(b1),B2=str(b2),
                    n_error0=str(nn*err0),n2_error1=str(nn*nn*err1),n3_error2=str(nn**3*err2)))

result = dict(Y_cumulants=[str(x) for x in lam[1:]],
    moment_polynomials=[[str(x) for x in aj] for aj in a],
    binomial_checks=checks_binomial, fixed_depth_checks=fixed_checks,
    hypergraph_checks=hyper_checks, leading_coefficient_values=leading,
    expansion_checks=rows, coefficient_majorant_checks=majorant_checks,
    scalar_output_checks=K,
    resources=dict(nice_priority=priority, elapsed_seconds=time.monotonic()-started,
                   max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
Path('verification.json').write_text(json.dumps(result, indent=2)+'\n')
print('Y cumulants:', ', '.join(str(x) for x in lam[1:]))
print('a_2, a_3, a_4:', [[str(x) for x in aj] for aj in a[2:5]])
print(f'PASS: {checks_binomial} exact binomial/chi-square moment comparisons')
print(f'PASS: {K} Catalan checks and {K+1} logarithmic-coefficient checks')
print(f'PASS: {fixed_checks} fixed-depth cancellation/positivity checks')
print(f'PASS: {majorant_checks} exact coefficientwise depth-uniform majorant checks')
print(f'PASS: {K} independent scalar-output cumulant/pairing-factor checks')
print(f'PASS: {hyper_checks} independent connected-hypergraph comparisons')
print('PASS: leading coefficients P_2=5d, P_3=75d^2-31d, P_4=2000d^3-1860d^2+418d')
print('Resummed errors for k=4, t=1/2:')
for row in rows:
    if row['k'] == 4 and row['t'] == '1/2':
        print(' n={n}: n|err0|={e0:.9g}, n^2|err1|={e1:.9g}, n^3|err2|={e2:.9g}'.format(n=row['n'],e0=float(row['n_error0']),e1=float(row['n2_error1']),e2=float(row['n3_error2'])))
print('Data: verification.json')
print('Resources:', result['resources'])
