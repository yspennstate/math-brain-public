import math

C0 = 2**(-0.5) * math.pi**0.75 * math.e**(5/8)
G = math.e**(1/8) * 2**(1/8) * math.gamma(1/8) / math.sqrt(2*math.pi)
B = G*C0
base = 6*math.sqrt(math.e)
R = 6*B**8/base**6
Lstar = math.log1p(R)
paid = base**0.75 * math.exp(Lstar/8)
hub = B * (6/(1-math.exp(-Lstar)))**(1/8)
Cpot = 4*math.sqrt(math.pi/(2*math.sqrt(3)))
Cfinal = Cpot * 6.787**0.75

assert abs(paid-hub) < 1e-12
assert paid < 14.486
assert Cfinal < 16.018

# Integral identity for lambda=1 in the half-Riesz dual kernel.
beta = math.gamma(0.5)*math.gamma(2.5)/math.gamma(3.0)
I = 4*beta
assert abs(I-3*math.pi/2) < 1e-12

print('QFORM_B13_R22_CHECK_PASS')
print('C0=', repr(C0))
print('G=', repr(G))
print('B=', repr(B))
print('R=', repr(R))
print('Lstar=', repr(Lstar))
print('smallball_constant=', repr(paid))
print('half_riesz_constant=', repr(Cpot))
print('scalar_schur_Linf_constant=', repr(Cfinal))
print('kernel_integral=', repr(I))
