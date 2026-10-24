import math

D0 = 1001/12544
kappa0 = 13/112
C_pair = 4*math.sqrt(8*math.sqrt(2*math.e))
C_global = C_pair * kappa0**(-1/4) * D0**(-1/8) * (576/49)**(1/8)
nonultra = 6144*math.e**2
multiplier = C_global * nonultra**(-1/8)
cutoff = multiplier**2

print(f"D0={D0:.15f}")
print(f"kappa0={kappa0:.15f}")
print(f"C_pair={C_pair:.15f}")
print(f"C_global={C_global:.15f}")
print(f"nonultra={nonultra:.15f}")
print(f"multiplier={multiplier:.15f}")
print(f"cutoff={cutoff:.15f}")

assert abs(C_global - 55.24377123921466) < 1e-12
assert abs(multiplier - 14.459500707808527) < 1e-12
assert abs(cutoff - 209.07716071911528) < 1e-11
print("QFORM_B13_R49_DIFFUSE_SCHUR_CHECK_PASS")
