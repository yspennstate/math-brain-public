#!/usr/bin/env python3
import math

CSTAR = 6.5218512
C0 = 6.4548
A_STAR = 0.2682048


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x) - (1.0-x)*math.log2(1.0-x)


def fwht(vals):
    a = [float(v) for v in vals]
    n = len(a)
    step = 1
    while step < n:
        for i in range(0, n, 2*step):
            for j in range(i, i+step):
                u, v = a[j], a[j+step]
                a[j], a[j+step] = u+v, u-v
        step *= 2
    return [z/n for z in a]


def closed_credit(t, delta):
    q = 1.0-t
    b = 1.0-2.0*delta
    D = q + t*b*b
    V = 4.0*t*q
    m = V*delta
    HB = D*h2(t*b*b/D) if D > 0 else 0.0
    u = 4.0*t*q*delta*delta
    IJ = h2(m) - D*h2(u/D) - 4.0*t*delta*(1.0-delta)*h2(t)
    return HB, IJ


def direct_credit(vals, t):
    coeff = fwht(vals)
    q = 1.0-t
    HB = 0.0
    condJ = 0.0
    totalJ = 0.0
    parseval = 0.0
    for i, bb in enumerate(coeff):
        aa = 1.0 if i == 0 else 0.0
        parseval += bb*bb
        T = q*aa*aa + t*bb*bb
        if T <= 1e-30:
            continue
        pB1 = t*bb*bb/T
        HB += T*h2(pB1)
        jmass = t*q*(bb-aa)*(bb-aa)
        totalJ += jmass
        condJ += T*h2(jmass/T)
    IJ = h2(totalJ)-condJ
    delta = sum(v < 0 for v in vals)/len(vals)
    return delta, HB, IJ, totalJ, parseval


def balanced_margin(delta, C):
    b = 1.0-2.0*delta
    D = 1.0+b*b
    HB = 0.5*D*h2(b*b/D)
    VT = 0.5*D*h2(2.0*delta*delta/D)
    exact = C*delta - 1.0 + HB - VT - 2.0*delta*(1.0-delta)
    extra = 2.0*delta*delta*(4.0*delta*delta-2.0*delta+1.0)/(2.0*delta*delta-2.0*delta+1.0)
    lower = (C-6.0)*delta + extra
    return exact, lower


def scalar_old(delta, C):
    b1 = (1.0-2.0*delta)**2
    b2 = 1.0-2.0*math.sqrt(delta*(1.0-delta))
    return C*delta - 1.0 - h2(delta) + max(b1,b2)


max_err = 0.0
cases = 0
for k in range(0, 4):
    M = 1 << k
    for mask in range(1 << M):
        vals = [-1 if ((mask >> i) & 1) else 1 for i in range(M)]
        for t in (1/8, 1/4, 1/2, 3/4, 7/8):
            d, HB, IJ, m, par = direct_credit(vals, t)
            cHB, cIJ = closed_credit(t, d)
            max_err = max(max_err, abs(HB-cHB), abs(IJ-cIJ),
                          abs(m-4*t*(1-t)*d), abs(par-1.0))
            assert abs(HB-cHB) < 2e-12
            assert abs(IJ-cIJ) < 2e-12
            assert abs(m-4*t*(1-t)*d) < 2e-12
            assert abs(par-1.0) < 2e-12
            cases += 1

lb_min = 10.0
for k in range(0, 13):
    M = 1 << k
    for j in range(M+1):
        d = j/M
        exact, lower = balanced_margin(d, 6.0)
        assert exact + 2e-12 >= lower
        assert lower >= -2e-12
        lb_min = min(lb_min, lower)

ineq_gap = 10.0
tube_gap = 10.0
for i in range(1, 100000):
    u = i/100000.0
    ineq_gap = min(ineq_gap, h2(u)-4*u*(1-u),
                   2*math.sqrt(u*(1-u))-h2(u))
    d = i/100000.0
    exact, lower = balanced_margin(d, C0)
    tube_gap = min(tube_gap, exact-lower)
    assert exact + 5e-12 >= lower

d = 1.0/64.0
actual, lower = balanced_margin(d, CSTAR)
old = scalar_old(d, CSTAR)
assert old < 0 < lower <= actual

base, _ = balanced_margin(d, C0)
assert abs((actual-base) - A_STAR*d/4.0) < 1e-12

BSTAR = 8.0 - 4.0/math.log(2.0)
def infinitesimal_barrier(t):
    V = 4*t*(1-t)
    return -h2(V) - 4*t*math.log2(t) + 4*t*h2(t)
ratios = [infinitesimal_barrier(2.0**(-k))/(2.0**(-k)) for k in range(8, 25)]
assert abs(ratios[-1]-BSTAR) < 2e-5

print("PASS")
print("direct_credit_cases", cases)
print("max_direct_formula_error", max_err)
print("dense_entropy_inequality_gap", ineq_gap)
print("dense_tube_exact_minus_lower_gap", tube_gap)
print("delta_1_over_64_old_scalar", old)
print("delta_1_over_64_exact_margin", actual)
print("delta_1_over_64_proved_lower", lower)
print("bstar", BSTAR)
print("boundary_ratio_last", ratios[-1])
