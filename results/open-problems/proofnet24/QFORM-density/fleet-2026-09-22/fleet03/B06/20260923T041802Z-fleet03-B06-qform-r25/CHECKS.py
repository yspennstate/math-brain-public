import math
from scipy.integrate import quad

C3 = 3**1.5 * math.e**(2/3) / 2**(2/3)
Cinf = 4*math.sqrt(2*math.e)*3**(3/8)
Cpacket = Cinf * 2304**(1/12)
Ccollar = Cinf * 6400**(1/12)
Aconst = math.e**3 * 2**(-1.5) * math.pi**3
Iconst = 9*math.sqrt(2)*math.pi*math.e

print('QFORM_B06_R25_CHECK_PASS')
print('C3', repr(C3))
print('Cinf', repr(Cinf))
print('Cpacket_2304', repr(Cpacket))
print('Ccollar_6400', repr(Ccollar))
print('Iconst', repr(Iconst))

assert Cinf < 14.082
assert Cpacket < 26.845
assert Ccollar < 29.230

# Check the exact integral of the q=2 Fourier envelope for three scales of Delta_3.
for Z in [1e-6, 1.0, 1e6]:
    A = Aconst * Z**(-0.5)
    K = A**0.25
    t0 = K**(4/3)
    f = lambda t: min(1.0, K*t**(-0.75))**1.5
    val = 2*quad(f, 0.0, t0, epsabs=1e-11)[0] + 2*quad(f, t0, math.inf, epsabs=1e-11)[0]
    target = Iconst * Z**(-1/6)
    rel = abs(val-target)/target
    print('envelope', Z, repr(val), repr(target), repr(rel))
    assert rel < 1e-10
