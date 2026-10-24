import math

alpha = 1.0/8.0
beta_116_116 = math.gamma(1.0/16.0)**2 / math.gamma(1.0/8.0)
C_R = ((math.pi*math.e/2.0)**alpha /
       (2.0*math.gamma(alpha)*math.cos(math.pi*alpha/2.0))) * beta_116_116
K = ((2*alpha+1) * (2*alpha)**(-2*alpha/(2*alpha+1)) *
     (2*math.sqrt(2))**(2*alpha/(2*alpha+1)) *
     (2**alpha/(alpha*math.e))**(1/(2*alpha+1)))
C_pow = K * C_R**(1/(2*alpha+1))
C_log = 2 + 8*C_R

assert 0 < alpha < 1.0/4.0
assert abs(1/(2*(2*alpha+1)) - 2.0/5.0) < 1e-15
assert abs(alpha/(2*alpha+1) - 1.0/10.0) < 1e-15
assert abs(1/(2*alpha+1) - 4.0/5.0) < 1e-15
assert C_R < 2.581
assert C_pow < 11.021
assert C_log < 22.648
# Scaling: D -> lambda^2 D, kappa -> |lambda| kappa, F -> |lambda| F.
scaling_power = 2*(-2.0/5.0) + (-1.0/10.0) + (-1.0/10.0)
assert abs(scaling_power + 1.0) < 1e-15

print(f"C_R={C_R:.15f}")
print(f"K_1/8={K:.15f}")
print(f"C_pow={C_pow:.15f}")
print(f"C_log={C_log:.15f}")
print(f"scaling_power={scaling_power:.15f}")
print("STATUS=PASS")
