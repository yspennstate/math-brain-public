import math
import random

rng = random.Random(20260924)
trials = 0
max_ratio = 0.0

# Check the fixed-copy overlap inequality used in Theorem 2.1
# for the model density 1_[0,1] under arbitrary signed affine scales.
for m in range(2, 8):
    for _ in range(4000):
        scales = []
        intervals = []
        for _j in range(m):
            a = 10.0 ** rng.uniform(-3.0, 2.0)
            if rng.random() < 0.5:
                a = -a
            r = rng.uniform(-5.0, 5.0)
            lo = min(r, r + a)
            hi = max(r, r + a)
            scales.append(abs(a))
            intervals.append((lo, hi))

        lo = max(x[0] for x in intervals)
        hi = min(x[1] for x in intervals)
        overlap = max(0.0, hi - lo)
        exact_integral = overlap / math.prod(scales)

        ordered = sorted(scales)
        rhs = 1.0 / math.prod(ordered[1:])
        ratio = exact_integral / rhs
        max_ratio = max(max_ratio, ratio)
        assert exact_integral <= rhs * (1.0 + 1e-12)
        trials += 1

C0 = 8.0 * math.sqrt(2.0) / math.sqrt(63.0)
l2sq = 16.0 * math.sqrt(2.0) / math.sqrt(63.0)
partner_pair = 2048.0 * math.sqrt(2.0 / 7.0)
partner_null = 3.0 * 2.0 ** (2.0 / 3.0) * math.e ** (2.0 / 3.0)

expected = {
    2: 1.6884272505498108,
    3: 2.301478330659152,
    4: 2.8873793290227456,
    6: 4.022545894656383,
    8: 5.133137961153773,
    10: 6.230423133514697,
}
for m, target in expected.items():
    got = math.factorial(m) ** (1.0 / m) * C0 ** (1.0 - 1.0 / m)
    assert abs(got - target) < 1e-12

assert abs(C0 - 1.4253932901995967) < 1e-12
assert abs(l2sq - 2.8507865803991934) < 1e-12
assert abs(partner_pair - 1094.7020468732903) < 1e-9
assert abs(partner_null - 9.275505197173393) < 1e-12

print("trials", trials)
print("max_ratio", repr(max_ratio))
print("C0", repr(C0))
print("L2sq_nearcoloop", repr(l2sq))
for m in expected:
    got = math.factorial(m) ** (1.0 / m) * C0 ** (1.0 - 1.0 / m)
    print("Cm", m, repr(got))
print("partner_pair_area", repr(partner_pair))
print("partner_null_scalar", repr(partner_null))
print("QFORM_B11_R46_BANK_HYPERBOLIC_LM_CHECK_PASS")
