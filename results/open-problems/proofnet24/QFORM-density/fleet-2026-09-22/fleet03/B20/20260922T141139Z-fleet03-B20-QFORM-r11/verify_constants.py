#!/usr/bin/env python3
import math

K0 = math.sqrt(math.pi) * math.gamma(0.25) / math.gamma(0.75)
Cstar = 32.0 * (128.0 ** 0.25) * math.sqrt(K0 * math.e / (7.0 * math.sqrt(2.0)))
partner_prefactor = 2.0 ** 4.5

print(f"K0={K0:.15f}")
print(f"Cstar={Cstar:.15f}")
print(f"Cstar_lt_130={Cstar < 130.0}")
print(f"partner_prefactor={partner_prefactor:.15f}")
assert Cstar < 130.0
