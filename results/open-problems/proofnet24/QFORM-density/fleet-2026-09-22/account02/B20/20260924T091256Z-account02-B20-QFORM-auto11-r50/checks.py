import math

eta0 = 20865*math.sqrt(2)/4194296 + 2629953/33554368
eta_bar = 171/2000
t0 = 9/16
delta0 = 0.5 - 19*math.sqrt(2)/125 - 361/15625
m0 = (578533 - 408500*math.sqrt(2))/1250000
C_E3 = 3*2**(4/3)*math.exp(1/3)

assert eta0 < eta_bar
assert 9956061**2 - 2*6955000**2 > 0
assert m0 > 0
assert 578533**2 - 2*408500**2 > 0
assert abs(((43/20)*delta0-t0)-m0) < 1e-14
assert C_E3/m0 < 15952
assert 43/20 + 2**-16 < 2.150016
assert 43/20 + 2**-16 + 112*2**-20 < 2.150123
assert 10*math.sqrt(2*math.e) < 23.317

m=1024
c=1/64
assert math.sqrt(3/m) < eta0
stress_spectrum = [1,1,1,c,c,-c,-c]
assert sorted([abs(x) for x in stress_spectrum], reverse=True)[2] == 1
assert (28/5)*c**(-4/7) < 61

print({
    'eta0': eta0,
    'eta_bar_gap': eta_bar-eta0,
    'delta0': delta0,
    'm0': m0,
    'm0_square_certificate': 578533**2-2*408500**2,
    'E3_density_bound': C_E3/m0,
    'tail_rank12': 43/20+2**-16,
    'tail_rank11_collapse': 43/20+2**-16+112*2**-20,
    'D5_gate_bound': 10*math.sqrt(2*math.e),
    'stress_residual_column_norm': math.sqrt(3/m),
    'stress_Theorem_H_bound': (28/5)*c**(-4/7),
})
