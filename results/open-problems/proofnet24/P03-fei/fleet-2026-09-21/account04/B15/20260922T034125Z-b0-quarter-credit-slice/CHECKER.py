#!/usr/bin/env python3
"""Independent numerical falsification check for the B0 quarter-complement slice theorem.
The theorem itself is analytic; this checker reconstructs the Boolean gate directly.
Standard library only.
"""
import itertools, math

C0 = 6.4548

def h_atom(x):
    return 0.0 if x <= 0.0 else -x*math.log2(x)

def entropy(masses):
    return sum(h_atom(x) for x in masses)

def b0(bits):
    x1,x2,x3,x4 = bits
    return int((not (x2 and x3)) and (not (x3 and x4)) and (not (x4 and x1)))

def b0_branch0(bits):
    x1,x2,x4 = bits
    return int(not (x1 and x4))

def b0_branch1(bits):
    x1,x2,x4 = bits
    return int((not x2) and (not x4))

def biased_spectrum(fn, ps):
    n = len(ps)
    coeff = []
    for mask in range(1 << n):
        total = 0.0
        for bits in itertools.product((0,1), repeat=n):
            prob = 1.0
            basis = 1.0
            for i,(x,p) in enumerate(zip(bits, ps)):
                prob *= p if x else (1-p)
                if (mask >> i) & 1:
                    basis *= (x-p)/math.sqrt(p*(1-p))
            total += prob * (2*fn(bits)-1) * basis
        coeff.append(total)
    return [x*x for x in coeff]

def closed_delta(r):
    u = abs(2*r-1)
    if u == 0.0:
        return 1.0
    y = 1-u*u
    num = ((1+u)**2*math.log(1+u)
           +(1-u)**2*math.log(1-u)
           -2*u*u*math.log(u))
    return (1-2*u*u)/y + num/(4*y*math.log(2))

def endpoint_delta():
    return 0.75*math.log2(3)

max_err = 0.0
max_delta = -1.0
max_cloc = -1e99
min_local = 10.0
for k in range(1,1000):
    r = 0.25 + 0.5*k/1000.0
    p = 1/(4*r)
    q = 1 - 1/(4*(1-r))
    t = 0.5
    Hp = entropy(biased_spectrum(b0, [p,q,t,r]))
    H0 = entropy(biased_spectrum(b0_branch0, [p,q,r]))
    H1 = entropy(biased_spectrum(b0_branch1, [p,q,r]))
    deltaH = Hp - 0.5*(H0+H1)
    closed = closed_delta(r)
    max_err = max(max_err, abs(deltaH-closed))
    max_delta = max(max_delta, deltaH)
    local = C0/2 - 2 - deltaH
    min_local = min(min_local, local)
    max_cloc = max(max_cloc, -16*local)

ep = endpoint_delta()
ep_credit = 2-ep
ep_local = C0/2 - 2 - ep
ep_cloc = -16*ep_local

print("PASS")
print("max direct-vs-closed Delta_H error =", format(max_err, ".3e"))
print("dense-grid max Delta_H =", format(max_delta, ".15f"))
print("analytic endpoint max =", format(ep, ".15f"))
print("analytic credit floor =", format(ep_credit, ".15f"))
print("analytic local base floor =", format(ep_local, ".15f"))
print("analytic local margin ceiling =", format(ep_cloc, ".15f"))
print("grid local base min =", format(min_local, ".15f"))
print("grid local margin max =", format(max_cloc, ".15f"))
assert max_err < 5e-13
assert max_delta < ep
assert ep_local > 0
assert ep_cloc < 0
