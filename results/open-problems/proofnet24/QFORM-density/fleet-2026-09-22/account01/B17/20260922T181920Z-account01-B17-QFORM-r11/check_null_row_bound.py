#!/usr/bin/env python3
from math import pi, sqrt, log, atan, factorial

s1 = 13.0 / 4.0
s0 = 13.0 / 2.0

# a(t)=(1+t^2/36)^(-1/4)
def a(t):
    return (1.0 + (t/6.0)**2)**(-0.25)

# Integrated fourth-even Taylor majorant for F(t)=int_{-1/2}^{1/2} exp(-t^2 x^2/6) dx.
def coeff(k):
    return ((-1.0)**k) / (6.0**k * factorial(k) * (2*k+1) * 2.0**(2*k))

# Integral over [lo,hi] of T_4(t) times the chord majorant to a(t),
# where the chord is linear in x=t^2/36.
def chord_integral(lo, hi):
    xlo = (lo/6.0)**2
    xhi = (hi/6.0)**2
    flo = a(lo)
    fhi = a(hi)
    slope = (fhi-flo)/(xhi-xlo)
    intercept = flo-slope*xlo
    out = 0.0
    for k in range(5):
        c = coeff(k)
        out += c * (
            intercept*(hi**(2*k+1)-lo**(2*k+1))/(2*k+1)
            + (slope/36.0)*(hi**(2*k+3)-lo**(2*k+3))/(2*k+3)
        )
    return out

z0 = a(s0)
tail = 0.5*log((1.0+z0)/(1.0-z0)) + atan(z0)
finite = chord_integral(0.0, s1) + chord_integral(s1, s0)
upper = (finite + sqrt(6.0*pi)*tail)/pi
target = 3.0*sqrt(2.0)
gap = target-upper

print(f"finite_majorant_integral={finite:.15f}")
print(f"tail_integral={tail:.15f}")
print(f"certified_upper={upper:.15f}")
print(f"three_sqrt_two={target:.15f}")
print(f"gap={gap:.15f}")
assert gap > 0.017
print("PASS")
