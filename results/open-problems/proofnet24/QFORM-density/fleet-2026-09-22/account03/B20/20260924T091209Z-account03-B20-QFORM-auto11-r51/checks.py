import math

rho0 = 2.157910236855737e-5
a0 = rho0/512
d0 = 1/1024
D0 = d0*d0 - (1/64)*a0
F0 = math.sqrt((1/64)**2 + a0*a0 + 2*d0*d0)
kappa0 = D0/F0
Cpc = 35.72978950364268

tau = 2**-20
nu = tau/18
t0 = 9*tau
epsilon = 2/81
delta = 1-(1/math.sqrt(2)+math.sqrt(epsilon))**2

Ccross = Cpc*D0**(-1/3)*kappa0**(-1/6)*nu**(-1/6)
Csquare = 2**(13/4)*(D0*kappa0*tau)**(-1/4)
Cstar = 12.714*D0**(-1/3)*kappa0**(-1/6)*tau**(-1/6)

schur_cross_lower = delta*(36*tau)-t0
rank6_tail = 36*tau
rank6_s3 = 1-rank6_tail
column_tail = math.sqrt(2)*tau

assert D0 > 0
assert kappa0 > 0
assert abs(delta-41/162) < 1e-15
assert abs(schur_cross_lower-tau/9) < 1e-18
assert schur_cross_lower > nu
assert Ccross < 298800
assert Csquare < 110364
assert Cstar < 65678
assert max(Ccross, Csquare, Cstar) < 300000
assert abs(rank6_tail-9/262144) < 1e-18
assert rank6_s3 > 0.999965

print(f"a0={a0:.17g}")
print(f"D0={D0:.17g}")
print(f"kappa0={kappa0:.17g}")
print(f"tau={tau:.17g}")
print(f"nu={nu:.17g}")
print(f"delta={delta:.17g}")
print(f"Ccross={Ccross:.12f}")
print(f"Csquare={Csquare:.12f}")
print(f"Cstar={Cstar:.12f}")
print(f"schur_cross_lower={schur_cross_lower:.17g}")
print(f"rank6_tail={rank6_tail:.17g}")
print(f"rank6_s3={rank6_s3:.17g}")
print(f"column_tail={column_tail:.17g}")
print("all checks passed")
