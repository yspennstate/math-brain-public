#!/usr/bin/env python3
import math, random

C = 6.521851214
S = C/2.0 - 2.0
B = C/2.0 + 2.0

def h(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x) - (1.0-x)*math.log2(1.0-x)

def phi(x):
    return 0.0 if x <= 0.0 else x*math.log2(1.0/x)

def V(x):
    return 4.0*x*(1.0-x)

def weights(t,q0,q1):
    r = (1.0-t)*q0 + t*q1
    return (
        (1.0-2.0*r)**2,
        V(t)*(q1-q0)**2,
        (1.0-t)**2*V(q0),
        t*t*V(q1),
        t*(1.0-t)*V(q0),
        t*(1.0-t)*V(q1),
    )

def direct_entropy(t,q0,q1):
    return sum(phi(w) for w in weights(t,q0,q1))

def increment_formula(t,q0,q1):
    m0 = 1.0-2.0*q0
    m1 = 1.0-2.0*q1
    s = (1.0-t)*m0*m0 + t*m1*m1
    if s == 0.0:
        return 2.0*h(t)
    A = t*(1.0-t)*(m0-m1)**2/s
    theta = t*m1*m1/s
    return (2.0-s)*h(t) + s*(h(A)-h(theta))

def Ephi(u,v):
    return phi(u*u)+phi(v*v)-0.5*phi((u+v)**2)-0.5*phi((u-v)**2)

rng = random.Random(150922)
max_parseval = 0.0
max_increment_error = 0.0
max_half_error = 0.0
max_E_bound_violation = -1e100
min_R = 1e100
argmin_R = None

for _ in range(250000):
    t,q0,q1 = rng.random(), rng.random(), rng.random()
    ww = weights(t,q0,q1)
    max_parseval = max(max_parseval, abs(sum(ww)-1.0))
    child = (1.0-t)*h(V(q0)) + t*h(V(q1))
    inc = direct_entropy(t,q0,q1)-child
    max_increment_error = max(max_increment_error, abs(inc-increment_formula(t,q0,q1)))

    m0,m1 = 1.0-2.0*q0,1.0-2.0*q1
    u,v = 0.5*(m0+m1),0.5*(m0-m1)
    inc_half = increment_formula(0.5,q0,q1)
    Ef = Ephi(u,v)
    max_half_error = max(max_half_error, abs(inc_half-(2.0*(1-u*u-v*v)+Ef)))
    max_E_bound_violation = max(max_E_bound_violation, Ef-(2.0*abs(u*v)+4.0*v*v))
    R = S*(1.0-u*u)+B*v*v-Ef
    if R < min_R:
        min_R,argmin_R = R,(u,v)

print("candidate_C", C)
print("S=C/2-2", S)
print("B=C/2+2", B)
print("max_parseval_error", "%.3e" % max_parseval)
print("max_increment_identity_error", "%.3e" % max_increment_error)
print("max_balanced_address_identity_error", "%.3e" % max_half_error)
print("max_E_bound_violation", "%.3e" % max_E_bound_violation)
print("sample_min_nonpotential_reserve", "%.12g" % min_R, "at", argmin_R)

print("complementary_credit_table")
for q in (0.25,0.125,2**-4,2**-8,2**-12):
    v = 1.0-2.0*q
    Vq = V(q)
    credit = v*v
    print("q", "%.12g" % q, "V", "%.12g" % Vq,
          "negative_JS_credit", "%.12g" % credit,
          "credit_free_asymptotic_penalty", "%.12g" % credit)

assert max_parseval < 2e-14
assert max_increment_error < 2e-13
assert max_half_error < 2e-13
assert max_E_bound_violation < 2e-12
assert min_R > -2e-12
print("PASS")
