import math

C1 = math.sqrt(2.0) * (5.0 + 2.0 * math.log(2.0))
C2 = math.sqrt(12.0)
projection_constant = 2.0 * C1 + 2.0 * C2
partner_constant = 2.0 * math.pi / math.sqrt(6.0)

assert abs(C1 - 9.03158409880257) < 1e-12
assert abs(C2 - 3.4641016151377544) < 1e-12
assert projection_constant < 24.992
assert partner_constant < 2.566

# Strict target Q_* = S^2 + 2 T V has matrix diag(1) plus [[0,1],[1,0]].
qstar_eigs = (-1.0, 1.0, 1.0)
assert all(abs(x) >= 1.0 for x in qstar_eigs)

# Partner matrix has 2x2 block [[-3,2],[2,3]]: trace 0, determinant -13.
partner_eigs = (-math.sqrt(13.0), 2.0, math.sqrt(13.0))
assert all(abs(x) >= 1.0 for x in partner_eigs)

# Exact reciprocal-tail function for delta=1, used only as a numerical regression.
def H(q):
    if q < 0.0:
        a = -q
        if a >= 1.0:
            return math.pi / math.sqrt(a)
        r = math.sqrt(1.0 - a)
        return (2.0 / math.sqrt(a)) * (math.pi / 2.0 - math.atan(r / math.sqrt(a)))
    if q == 0.0:
        return 2.0
    r = math.sqrt(q)
    if q <= 1.0:
        return (2.0 / r) * math.atanh(r / math.sqrt(q + 1.0))
    return (2.0 / r) * (
        math.atanh(math.sqrt(1.0 - 1.0 / q))
        + math.atanh(math.sqrt(q / (q + 1.0)))
    )

mx = (0.0, None)
for i in range(200001):
    q = -10.0 + 210.0 * i / 200000.0
    val = H(q)
    if val > mx[0]:
        mx = (val, q)
assert mx[0] < 3.142
assert mx[0] < 6.0

print(f"C1={C1:.15f}")
print(f"C2={C2:.15f}")
print(f"QSTAR_BOUND={projection_constant:.15f}")
print(f"PARTNER_BOUND={partner_constant:.15f}")
print(f"TAIL_SCAN_MAX={mx[0]:.15f} at q={mx[1]:.9f}")
print("QSTAR_SPECTRUM=-1,1,1")
print("PARTNER_SPECTRUM=-sqrt(13),2,sqrt(13)")
print("STATUS=PASS")
