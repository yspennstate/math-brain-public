#!/usr/bin/env python3
import math

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x) - (1.0-x)*math.log2(1.0-x)

def H(v):
    return sum(-x*math.log2(x) for x in v if x > 0.0)

def vals(t,q0,q1):
    Vt=4*t*(1-t); V0=4*q0*(1-q0); V1=4*q1*(1-q1)
    r=(1-t)*q0+t*q1
    d=q0+q1-2*q0*q1
    a=V0*(1-t); b=V1*t
    w=((1-2*r)**2, Vt*(q1-q0)**2,
       (1-t)**2*V0, t*t*V1,
       t*(1-t)*V0, t*(1-t)*V1)
    C=d*h2(Vt)+h2(q0)+h2(a)+h2(q1)+h2(b)-H(w)
    L=d*h2(Vt)+h2(q0)+h2(q1)-h2(Vt*d)
    W=Vt*(V0+V1)/16
    return w,C,L,W

max_mass_err=0.0
min_credit_gap=1e9
min_central_margin=1e9
kappa=8*(2*h2(0.25)-h2(0.375))
count=0
for it in range(1,100):
    t=it/100
    for i in range(1,100):
        q0=i/100
        for j in range(1,100):
            q1=j/100
            w,C,L,W=vals(t,q0,q1)
            max_mass_err=max(max_mass_err,abs(sum(w)-1.0))
            min_credit_gap=min(min_credit_gap,C-L)
            if 0.25 <= q0 <= 0.75 and 0.25 <= q1 <= 0.75:
                min_central_margin=min(min_central_margin,C/W-kappa)
            count += 1

assert max_mass_err < 2e-14
assert min_credit_gap > -2e-12
assert min_central_margin > -2e-12
print("cases", count)
print("max_mass_error", format(max_mass_err,'.17g'))
print("min_exact_minus_marginal_bound", format(min_credit_gap,'.17g'))
print("kappa_central", format(kappa,'.17g'))
print("min_sampled_exact_ratio_minus_kappa", format(min_central_margin,'.17g'))
print("PASS")
