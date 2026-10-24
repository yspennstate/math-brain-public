import math

C0 = 2 * math.sqrt(math.pi) * 3**0.25
assert abs(C0 - 4.665360904668642) < 1e-14
print("C0", repr(C0))

for m in [2, 3, 5, 10, 100, 1000]:
    s = (m - 1) / (m * m)
    agg = s**(-0.25)
    fixed = math.sqrt(m)
    assert s > 0
    print({
        "m": m,
        "s_I": s,
        "aggregate_factor": agg,
        "fixed_factor": fixed,
        "ratio": agg / fixed,
    })

print("STATUS=PASS")
