from fractions import Fraction as F


def b(n, d, lam):
    n, d, lam = F(n), F(d), F(lam)
    return (d - 1) / ((d - lam) * (n + lam * (d - n - 1) / d))


def a(n, d, D, lam):
    n, d, D, lam = F(n), F(d), F(D), F(lam)
    return (D - 1) / ((D - lam) * (n + lam * (D - n - 1) / D))


def g(n, d, D, lam):
    return F(n) * a(n, d, D, lam)


def chord(x0, x1, y0, y1):
    s = (y1 - y0) / (F(x1) - F(x0))
    return y0 - s * F(x0), s


def max_quad(A, B, C, lo, hi):
    lo, hi = F(lo), F(hi)
    candidates = [(A*lo*lo+B*lo+C, lo), (A*hi*hi+B*hi+C, hi)]
    if A < 0:
        r = -B/(2*A)
        if lo <= r <= hi:
            candidates.append((A*r*r+B*r+C, r))
    return max(candidates, key=lambda z: z[0])


def cert(d, D, L):
    L = F(L)
    bd, bD = b(d,d,L), b(D,d,L)
    gd, gD = g(d,d,D,L), g(D,d,D,F(1))
    b0, bs = chord(d,D,bd,bD)
    g0, gs = chord(d,D,gd,gD)
    A = L*bs
    B = L*b0 - L*gs - 1
    C = -L*g0
    mx, rstar = max_quad(A,B,C,d,D)
    delta = -mx
    margin = None if delta <= 0 else 2*delta/(F(D)+L)**2
    monotone_guard = F(D-2*d-1) - 2*L*F(D-d-1,D)
    return dict(A=A,B=B,C=C,mx=mx,rstar=rstar,delta=delta,margin=margin,
                monotone_guard=monotone_guard,bd=bd,bD=bD,gd=gd,gD=gD)

for name,d,D,L,clean in [
    ('deep_d3_D61_L9/5',3,61,F(9,5),F(1,1_100_000)),
    ('deeper_d3_D12_L19/10',3,12,F(19,10),F(1,3000)),
]:
    c=cert(d,D,L)
    assert c['monotone_guard'] > 0
    assert c['mx'] < 0 and c['delta'] < d
    assert c['margin'] > clean
    fail=cert(d,D+1,L)
    assert fail['mx'] > 0
    print(name)
    for k in ['bd','bD','gd','gD','A','B','C','rstar','mx','delta','margin','monotone_guard']:
        print(' ',k,'=',c[k],'~',float(c[k]))
    print(' clean_margin >',clean,'~',float(clean))
    print(' next_D',D+1,'maxpsi =',fail['mx'],'~',float(fail['mx']))

# Both 9/5 and 19/10 lie above theta_3 because theta_3<5/3 already.
assert F(2,3) > F(16,25)
print('ALL_EXACT_CHECKS_PASS')
