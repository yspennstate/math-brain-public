import math

c1 = 0.5 * math.sqrt(3/5)
beta1 = (3/16) * math.sqrt(3/5)
eta0 = 1 - math.sqrt(0.97)
e0 = (4/5) * (2 * eta0)

assert 0.9 - 2*eta0 > c1
assert 0.2 + 2*eta0 < c1
assert 0.8 - e0 > beta1
assert 0.1 + e0 < beta1

bounds = {}
for k in (1, 2):
    base = 6 * ((4/5)**k * (3/5)**(3-k))**(-1/6)
    cond = base / 0.97
    bounds[k] = (base, cond)

sstar = 0.8 - e0
Delta = sstar**2
hhalf = 8 * Delta**(-1/4)
l3 = 6**(2/3) * Delta**(-1/3)

assert bounds[1][1] < 7.612
assert bounds[2][1] < 7.256
assert hhalf < 9.083
assert l3 < 3.911

print(f"c1={c1:.15f}")
print(f"beta1={beta1:.15f}")
print(f"eta0={eta0:.15f}")
print(f"e0={e0:.15f}")
print(f"child_high_floor={0.9-2*eta0:.15f}")
print(f"child_low_ceiling={0.2+2*eta0:.15f}")
print(f"cross_large_floor={sstar:.15f}")
print(f"cross_small_ceiling={0.1+e0:.15f}")
print(f"k1_unconditioned={bounds[1][0]:.15f}")
print(f"k1_conditioned={bounds[1][1]:.15f}")
print(f"k2_unconditioned={bounds[2][0]:.15f}")
print(f"k2_conditioned={bounds[2][1]:.15f}")
print(f"partner_Hhalf={hhalf:.15f}")
print(f"partner_L3={l3:.15f}")
print("QFORM_B08_R25_CHECK_PASS")
