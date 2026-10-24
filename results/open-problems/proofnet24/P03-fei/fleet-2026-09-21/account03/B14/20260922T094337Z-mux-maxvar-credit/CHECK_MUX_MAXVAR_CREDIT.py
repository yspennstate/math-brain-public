#!/usr/bin/env python3
import math, random

LN2=math.log(2.0)

def h(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def H(ps):
    return -sum(p*math.log2(p) for p in ps if p>0.0)

def data(t,q0,q1):
    Vt=4*t*(1-t); V0=4*q0*(1-q0); V1=4*q1*(1-q1)
    d=q0+q1-2*q0*q1
    r=(1-t)*q0+t*q1
    a=(1-t)*V0; b=t*V1; c=1-a-b
    e=Vt*(q1-q0)**2
    masses=((1-2*r)**2,e,(1-t)**2*V0,t*t*V1,t*(1-t)*V0,t*(1-t)*V1)
    direct=d*h(Vt)+h(q0)+h(a)+h(q1)+h(b)-H(masses)
    tc=h(a)+h(b)-H((c,a,b))
    cond0=0.0 if c <= 1e-15 else c*h(e/c)
    closed=h(q0)+h(q1)+d*h(Vt)-(a+b)*h(t)-cond0+tc
    W=t*(1-t)*(V0+V1)/4
    om0=t*(1-t)*V0/4
    om1=t*(1-t)*V1/4
    return direct,closed,W,om0,om1

rng=random.Random(314159265)
max_credit_err=0.0
max_currency_err=0.0
min_central_ratio=float("inf")
min_arg=None
eps=0.25
bound=8*(2*h(eps)-1)+8*eps*(1-eps)/LN2
for k in range(200000):
    t=(k+0.5)/200000 if k<2000 else rng.random()
    q0=rng.random(); q1=rng.random()
    d,c,W,o0,o1=data(t,q0,q1)
    max_credit_err=max(max_credit_err,abs(d-c))
    max_currency_err=max(max_currency_err,abs(W-o0-o1))
    if k<100000:
        qc0=eps+(1-2*eps)*rng.random()
        qc1=eps+(1-2*eps)*rng.random()
        dc,_,Wc,_,_=data(t,qc0,qc1)
        if Wc>0:
            ratio=dc/Wc
            if ratio<min_central_ratio:
                min_central_ratio=ratio
                min_arg=(t,qc0,qc1)

print("samples=200000")
print("max_exact_credit_identity_error=%.3e" % max_credit_err)
print("max_currency_partition_error=%.3e" % max_currency_err)
print("proved_central_lower_bound=%.15f" % bound)
print("sampled_min_central_ratio=%.15f" % min_central_ratio)
print("sampled_min_arg=%r" % (min_arg,))
assert max_credit_err < 5e-13
assert max_currency_err < 5e-15
assert min_central_ratio + 1e-12 >= bound
print("PASS")
