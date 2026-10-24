#!/usr/bin/env python3
"""Independent deterministic audit of B01 partial-star GU theorem.

Exact rational arithmetic is used for Walsh masses and influences.  Entropy
expressions are evaluated twice (90 and 140 decimal digits) from those exact
rationals; the analytic proof, not the numerical evaluation, establishes the
all-parameter result.
"""

from fractions import Fraction
from decimal import Decimal, localcontext


def fwht(vals):
    a = [Fraction(v) for v in vals]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    N = len(a)
    return [x/Fraction(N) for x in a]


def masses(vals):
    return [x*x for x in fwht(vals)]


def upper_u(vals, dps):
    with localcontext() as ctx:
        ctx.prec = dps
        p = masses(vals)
        caps = list(p)
        m = len(p).bit_length()-1
        for bit in range(m):
            mask = 1 << bit
            for s in range(len(p)):
                if not (s & mask):
                    caps[s] += caps[s | mask]
        out = Decimal(0)
        ln2 = Decimal(2).ln()
        for s, ps in enumerate(p):
            if not ps:
                continue
            cap = caps[s]
            x = Decimal(ps.numerator)/Decimal(ps.denominator)
            q = Decimal(cap.numerator)/Decimal(cap.denominator)
            out += x*(q/x).ln()/ln2
        return +out


def restrict(vals, i, bit):
    m = len(vals).bit_length()-1
    out = []
    for y in range(1 << (m-1)):
        lo = y & ((1 << i)-1)
        hi = y >> i
        out.append(vals[lo | (bit << i) | (hi << (i+1))])
    return out


def influence(vals, i):
    return Fraction(sum(vals[x] != vals[x ^ (1 << i)] for x in range(len(vals))), len(vals))


def loss(vals, i, dps):
    return upper_u(vals, dps) - (upper_u(restrict(vals, i, 0), dps)+upper_u(restrict(vals, i, 1), dps))/2


def partial_star(n, t):
    out = []
    for mask in range(1 << (n+1)):
        z = mask & 1
        xs = [(mask >> (j+1)) & 1 for j in range(n)]
        exponent = z*sum(xs[:t]) + int(not any(xs))
        out.append(1 if exponent % 2 == 0 else -1)
    return out


def shifted_defect(n, t):
    out = []
    for mask in range(1 << n):
        exponent = sum((mask >> j) & 1 for j in range(t)) + int(mask == 0)
        out.append(1 if exponent % 2 == 0 else -1)
    return out


checks = 0
small_base = []
max_ratio = (Decimal('-Infinity'), None)

# Truth-table reconstruction, exact spectra and exact physical influences.
for n in range(1, 8):
    delta = Fraction(1, 1 << n)
    e = 4*delta*delta
    a = (Fraction(1, 2)-2*delta)**2
    for t in range(1, n+1):
        vals = partial_star(n, t)
        got = sorted(x for x in masses(vals) if x)
        want = sorted(x for x in [Fraction(1,4), Fraction(1,4), a, a] + [e]*((1 << n)-2) if x)
        assert got == want
        checks += 1
        for i in range(n+1):
            inf = influence(vals, i)
            target = Fraction(1,2) if i == 0 or i <= t else 2*delta
            assert inf == target
            q90 = loss(vals, i, 90)
            q140 = loss(vals, i, 140)
            assert abs(q90-q140) < Decimal('1e-80')
            ratio = q140/(Decimal(inf.numerator)/Decimal(inf.denominator))
            assert ratio < 14
            if ratio > max_ratio[0]:
                max_ratio = (ratio, ('partial', n, t, i))
            if n <= 3:
                small_base.append((n,t,i,ratio))
            checks += 4

for n in range(1, 8):
    delta = Fraction(1, 1 << n)
    e = 4*delta*delta
    A = (1-2*delta)**2
    for t in range(0, n+1):
        vals = shifted_defect(n, t)
        got = sorted(x for x in masses(vals) if x)
        want = sorted(x for x in [A]+[e]*((1 << n)-1) if x)
        assert got == want
        checks += 1
        for i in range(n):
            inf = influence(vals, i)
            target = 1-2*delta if i < t else 2*delta
            assert inf == target
            if not inf:
                assert loss(vals, i, 140) == 0
                checks += 2
                continue
            q90 = loss(vals, i, 90)
            q140 = loss(vals, i, 140)
            assert abs(q90-q140) < Decimal('1e-80')
            ratio = q140/(Decimal(inf.numerator)/Decimal(inf.denominator))
            assert ratio < 14
            if ratio > max_ratio[0]:
                max_ratio = (ratio, ('boundary', n, t, i))
            if n <= 3:
                small_base.append((n,t,i,ratio))
            checks += 4

# Independent audit of every scalar inequality used for n>=4, far beyond the
# truth-table range.  These checks diagnose transcription mistakes; the report
# supplies the monotone endpoint arguments proving the inequalities for all n.
worst = {'partial_bracket': Decimal('-Infinity'), 'T0_over_delta': Decimal('-Infinity'),
         'TR_over_delta': Decimal('-Infinity'), 'boundary_bracket': Decimal('-Infinity'),
         'boundary_big_over_delta': Decimal('-Infinity')}
with localcontext() as ctx:
 ctx.prec = 110
 ln2 = Decimal(2).ln()
 log2 = lambda x: x.ln()/ln2
 for n in range(4, 65):
    d = Decimal(2) ** (-n)
    e = 4*d*d
    a = (Decimal('.5')-2*d)**2
    ap = (Decimal('.5')-4*d)**2
    phi = lambda x: x*log2(1/x)
    T0 = phi(a)+e*(n-1)-phi(ap)/2-Decimal('.25')
    worst['T0_over_delta'] = max(worst['T0_over_delta'], T0/d)
    assert T0 < 4*d
    checks += 1
    for t in range(1, n):
        k = n-t
        PR = Decimal('.5')-2*d+(2**k)*e
        PRp = Decimal('.5')-4*d+(2**(k+1))*e
        g = lambda x,P: x*log2(P/x)
        TR = g(a,PR)+e*(k-1)-g(ap,PRp)/2-Decimal('.125')
        worst['TR_over_delta'] = max(worst['TR_over_delta'], TR/d)
        assert TR < 13*d
        checks += 1
        for c in range(1,t):
            h = n-c-1
            P = Decimal('.5')-2*d+(2**(h+1))*e
            Pp = 2*P-Decimal('.5')
            bracket = h+4+log2(P*e/(Pp*Pp))
            worst['partial_bracket'] = max(worst['partial_bracket'], bracket)
            assert bracket <= 4
            checks += 1

    # Boundary analogues; t=0 has no proper active-support subsets.
    for t in range(0,n):
        k = n-t
        A = (1-2*d)**2
        PR = 1-4*d+(2**k)*e
        big = (PR-A)/ln2+e*(k-1)
        worst['boundary_big_over_delta'] = max(worst['boundary_big_over_delta'], big/d)
        assert big < 7*d
        checks += 1
        for c in range(1,t):
            h = n-c-1
            P = 1-4*d+(2**(h+1))*e
            Pp = 2*P-1
            bracket = h+4+log2(P*e/(Pp*Pp))
            worst['boundary_bracket'] = max(worst['boundary_bracket'], bracket)
            assert bracket <= 4
            checks += 1

print(f'PASS checks={checks}')
print('max reconstructed coordinate loss/influence =', str(max_ratio[0])[:32], 'at', max_ratio[1])
print('small-base max loss/influence =', str(max(x[3] for x in small_base))[:32])
for k,v in worst.items():
    print(k, '=', str(v)[:32])
print('exact Walsh/influence scope: partial stars and shifted defects n<=7')
print('scalar transcription audit: every n=4..64 and every admissible t,c')
