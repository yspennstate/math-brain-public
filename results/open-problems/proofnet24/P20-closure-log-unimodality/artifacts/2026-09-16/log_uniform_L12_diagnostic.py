#!/usr/bin/env python3
"""High-precision self-check for the explicit P20 I0081 L=12 witness.

This is diagnostic only; the theorem uses the exact symbolic proof and the
separate rational checker.  No numerical value below is used as proof.
"""

import mpmath as mp

mp.mp.dps = 80
L = mp.mpf(12)
a = mp.e ** (-L)


def P(phi):
    return (1 - a*a) / (1 - 2*a*mp.cos(phi) + a*a)


def beta(phi):
    z = (mp.e**(1j*phi) - a) / (1 - a*mp.e**(1j*phi))
    b = mp.arg(z)
    if b < 0:
        b += 2*mp.pi
    return b


def Phi(t):
    return 2*mp.pi - 2*t - 2*beta(L/mp.tan(t))


t0 = mp.atan(L/mp.pi)
tstar = mp.findroot(Phi, (t0 + mp.mpf('0.05'), mp.pi/2 - mp.mpf('0.05')))
phi = L/mp.tan(tstar)
D = 1 - 2*a*mp.cos(phi) + a*a
A = L/(mp.sin(tstar)**2) * (1-a*a)/D - 1
T = L**2*a*(1-a*a)*mp.sin(phi)/(D**2*mp.sin(tstar)**4)
J = -1/mp.tan(tstar) + T
g0 = (1/mp.pi) * mp.im(1/(1-mp.e**(2j*tstar)))
gpp = -(1/mp.sin(tstar)**2)/(4*mp.pi*A**3) * J
C = a*(1-a*a)*(L**2+mp.pi**2)**2/(L*(1-a)**4)

for name, val in [
    ('a', a), ('t0', t0), ('t*', tstar), ('phi', phi), ('A', A),
    ('T', T), ('J', J), ('g0', g0), ('gpp', gpp), ('C', C),
    ('Phi(t*)', Phi(tstar)),
]:
    print(name, mp.nstr(val, 30))

assert A > 0
assert J < 0
assert gpp > 0
assert C < 1
