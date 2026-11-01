import math

Cmix = 12 * 2**(1/3)
Cenv = 128 * math.sqrt(15)
delta_star = (Cmix/Cenv)**3
eta = math.sqrt(delta_star)
c_edge = (3/2)**(1/3)
near_mass = 1 - eta - c_edge * eta**(1/3)
Ctime = (48/5) * math.sqrt(math.pi) * 2**(1/6)

assert abs(Cmix - 15.119052598738477) < 1e-12
assert abs(Cenv - 495.7418683145494) < 1e-12
assert abs(delta_star - 2.83665772427301e-5) < 1e-17
assert abs(eta - 0.005326028280316403) < 1e-15
assert abs(near_mass - 0.7947653266046167) < 1e-14
assert abs(Ctime - 19.099316928203915) < 1e-12

# Envelope integration identities for |phi| <= min(1,K t^{-3/2}).
# With crossover T=K^(2/3):
# int_R |phi| <= 6 K^(2/3)
# int_R |phi|^2 <= 3 K^(2/3)
# int_R |t|^-1/2 |phi|^2 <= 24/5 K^(1/3).
K = 7.3
T = K**(2/3)
L1 = 2*(T + 2*K*T**(-1/2))
L2 = 2*(T + (K*K/2)*T**(-2))
W = 2*(2*T**0.5 + (2/5)*K*K*T**(-2.5))
assert abs(L1 - 6*K**(2/3)) < 1e-12
assert abs(L2 - 3*K**(2/3)) < 1e-12
assert abs(W - (24/5)*K**(1/3)) < 1e-12

print('QFORM_B03_MIXED_BASIS_TRIPLE_FRESNEL_PASS')
print('Cmix=', Cmix)
print('delta_star=', delta_star)
print('eta=', eta)
print('near_mass=', near_mass)
print('Ctime=', Ctime)
