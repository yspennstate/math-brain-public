#!/usr/bin/env python3
"""Numerical calibration for the analytic B18 Sidon-frontier theorem.

The theorem does not depend on this script.  It only reproduces the inherited
r0,tau0,b0,lambda0 arithmetic and stress-checks the greedy influence split.
"""

from random import Random

r0 = 6.521845710923046575
tau0 = 0.17403165703250501666
b0 = 3.83174494462437254376
lambda0 = 0.87383598624439510519

alpha0 = b0 / (b0 + 2.0)
gamma0 = 2.0 / (b0 + 2.0)
split0 = tau0 * (b0 + 2.0) / (b0 - 2.0)
old_alpha0 = r0 / (r0 + 4.0)

print(f"alpha0={alpha0:.16f}")
print(f"gamma0={gamma0:.16f}")
print(f"split0={split0:.16f}")
print(f"old_alpha0={old_alpha0:.16f}")
print(f"threshold_gain={alpha0-old_alpha0:.16f}")

rng = Random(20260921)
checked = 0
for _ in range(10_000):
    m = rng.randint(4, 30)
    weights = [rng.random() * tau0 for _ in range(m)]
    total = sum(weights)
    if total <= split0:
        continue

    target = gamma0 * total
    acc = 0.0
    for w in weights:
        if acc > target:
            break
        acc += w

    assert acc > gamma0 * total
    assert acc < alpha0 * total + 1e-12
    assert total - acc > gamma0 * total - 1e-12
    assert total - acc < alpha0 * total + 1e-12
    checked += 1

print(f"random_partition_sanity_cases={checked}")
print("random_partition_sanity=PASS")
