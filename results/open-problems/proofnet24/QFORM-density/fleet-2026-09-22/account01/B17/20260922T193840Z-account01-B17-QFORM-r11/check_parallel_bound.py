#!/usr/bin/env python3
import mpmath as mp

mp.iv.dps = 80
q = mp.iv.mpf
pi = mp.iv.pi

G = mp.iv.gamma(q(1)/4)
U = G*G/(mp.iv.power(2, q(5)/2)*mp.iv.sqrt(3)) - pi/12 + mp.iv.sqrt(pi/6)*mp.iv.exp(-3)/6
target = pi/(2*mp.iv.sqrt(2))
phys = 12*U/pi
phys_target = 3*mp.iv.sqrt(2)

print('Gamma(1/4)=', G)
print('U=', U)
print('pi/(2sqrt2)=', target)
print('gap=', target-U)
print('physical_upper=', phys)
print('3sqrt2=', phys_target)

assert U.b < target.a
assert phys.b < phys_target.a

mp.mp.dps = 60
I = mp.quad(lambda s: (1-s)*mp.besselk(0, 3*s*s), [0,1])
centered_phys = 12*I/mp.pi
print('I_centered=', I)
print('centered_physical_peak=', centered_phys)
print('PASS')
