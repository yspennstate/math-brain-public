import math

B1=(2+math.sqrt(math.pi))*(4*math.e)**0.25
Cpc=3*(6*B1)**(2/3)
num=Cpc*(3/4096)**(-1/3)*(1/64)**(-1/6)*(2**-16)**(-1/6)
L_live=B1*(1/64)**(-1/4)
psi_live=6*(2**-12)**0.25*L_live

print('B1',repr(B1))
print('Cpc',repr(Cpc))
print('all-small-diagonal gate',repr(num))
print('live r49 quarter Riesz',repr(L_live))
print('live r49 log-to-quarter delta=2^-12',repr(psi_live))

assert Cpc < 35.730
assert num < 5034
assert L_live < 19.376
assert psi_live < 14.532

# Pair gate algebra at the threshold d=1/64, c=1/32.
d=1/64
c=1/32
D=c*c-d*d
kappa_lower=D/(c+d)
print('pair D threshold',repr(D))
print('pair kappa lower threshold',repr(kappa_lower))
assert abs(D-3/4096) < 1e-18
assert abs(kappa_lower-1/64) < 1e-18
