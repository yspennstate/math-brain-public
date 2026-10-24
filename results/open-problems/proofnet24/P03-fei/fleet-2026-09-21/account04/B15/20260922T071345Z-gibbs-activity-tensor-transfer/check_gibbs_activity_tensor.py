#!/usr/bin/env python3
"""Independent standard-library check of the exact Gibbs activity transfer.

Uses an actual Boolean seed f:{0,1}^2->{+-1}, f(00)=-1 and +1 elsewhere,
and its disjoint tensor square.  The potential is the harmless test potential
Gamma(p)=c*4p(1-p); the theorem checked is algebraic for every symmetric Gamma.
"""
import math

C = 1.7
TOL = 2e-12


def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p) - (1-p)*math.log2(1-p)


def V(p):
    return 4.0*p*(1.0-p)


def Gamma(p):
    return C*V(p)


def fwht(vals):
    a = [float(x) for x in vals]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    n = len(a).bit_length()-1
    den = float(1 << n)
    return [x/den for x in a]


def metrics(vals):
    n = len(vals).bit_length()-1
    coeff = fwht(vals)
    w = [x*x for x in coeff]
    q = sum(x < 0 for x in vals)/len(vals)
    v = V(q)

    # All physical inputs are uniform, so every coordinate has the same Gibbs cost.
    x = 2.0**(-C)
    Z = (1.0+x)**n
    nu = [(x**(s.bit_count()))/Z for s in range(1 << n)]

    KL = sum(p*math.log2(p/r) for p, r in zip(w, nu) if p > 0.0)
    D_full = KL - math.log2(Z) - Gamma(q)

    r = 1.0 - nu[0]
    wp = [w[s]/v for s in range(1, 1 << n)]
    nup = [nu[s]/r for s in range(1, 1 << n)]
    Kp = sum(p*math.log2(p/t) for p, t in zip(wp, nup) if p > 0.0)
    xq = 2.0**(-(Gamma(q)+h2(v))/v)
    L = math.log2((Z-1.0)/xq)
    D_cond = v*(Kp-L)

    assert abs(sum(w)-1.0) < TOL
    assert abs(sum(nu)-1.0) < TOL
    assert abs(D_full-D_cond) < TOL
    return dict(n=n, q=q, v=v, Z=Z, r=r, Kp=Kp, L=L,
                D=D_full, w=w, nu=nu)


seed = [-1, +1, +1, +1]
parent = [a*b for a in seed for b in seed]
M1 = metrics(seed)
M2 = metrics(parent)

# Three-state block-activity laws after conditioning on parent nonempty.
v1, v = M1['v'], M2['v']
r1, r = M1['r'], M2['r']
P = [v1*(1-v1)/v, (1-v1)*v1/v, v1*v1/v]
Q = [r1*(1-r1)/r, (1-r1)*r1/r, r1*r1/r]
Kact = sum(p*math.log2(p/q) for p, q in zip(P, Q))

# Conditional KL chain rule.
chain_err = M2['Kp'] - (Kact + 2.0*v1/v*M1['Kp'])
assert abs(chain_err) < TOL

# Activity-credit conservation equals the XOR-potential slack.
activity_ledger = v*Kact + 2.0*v1*M1['L'] - v*M2['L']
gamma_slack = 2.0*Gamma(M1['q']) - Gamma(M2['q'])
assert abs(activity_ledger-gamma_slack) < TOL

# Equivalent defect composition law.
defect_err = M2['D'] - (2.0*M1['D'] + gamma_slack)
assert abs(defect_err) < TOL

print('PASS')
print('seed_q', M1['q'], 'seed_v', M1['v'])
print('parent_q', M2['q'], 'parent_v', M2['v'])
print('activity_KL_bits', format(Kact, '.15f'))
print('activity_ledger_bits', format(activity_ledger, '.15f'))
print('gamma_XOR_slack_bits', format(gamma_slack, '.15f'))
print('max_abs_identity_error', format(max(abs(chain_err), abs(activity_ledger-gamma_slack), abs(defect_err)), '.3e'))
