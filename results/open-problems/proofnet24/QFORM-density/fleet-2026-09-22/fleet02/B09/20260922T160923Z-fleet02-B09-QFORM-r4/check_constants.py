import math

r = 1.5
p = 3.0
C_r = r**(1/(2*r)) / p**(1/(2*p))
P_r = 1 + (1-r/2)**(-1/r)
C0 = 3 * P_r * math.sqrt(math.e/2) * C_r**(r/2)
cS = 2/(3+math.sqrt(5))
target_branch = C0 * math.sqrt(312/cS)

# Walsh stress family: theta=6, q=2, gamma=1, D=2^12.
beta = 6/4
z = beta*r
D = 2**12
t0 = math.pi*math.e/2 * D**(-1/(2*6))
family_exact = P_r * (2*math.pi)**(-0.5) * C_r**(r/2) * math.sqrt(2*t0*z/(z-1))

print(f"C_r={C_r:.15f}")
print(f"P_r={P_r:.15f}")
print(f"C0={C0:.15f}")
print(f"cS={cS:.15f}")
print(f"target_branch={target_branch:.15f}")
print(f"family_exact={family_exact:.15f}")
