from fractions import Fraction


def partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    if cap is None or cap > n:
        cap = n
    for a in range(cap, 0, -1):
        for tail in partitions(n-a, a):
            yield (a,) + tail


allp = list(partitions(5))
nonsimple = [p for p in allp if len(p) >= 2 and p != (1, 1, 1, 1, 1)]
covered = {(4, 1), (3, 2), (2, 2, 1)}

print("integer_partitions_5 =", allp)
print("degree5_nonsimple_types =", nonsimple)
print("count =", len(nonsimple))
print("covered_this_run =", sorted(covered, reverse=True))
print("C5 =", len(covered), "/", len(nonsimple))
print("line_type_checks:")
for a in range(1, 5):
    mu2 = a * (5 - a)
    print(f"  a={a}: mu^2={mu2}, target_mu^2=4, pass={mu2 >= 4}")

# This is a self-check of the cycle-block algebra, not a substitute for the proof
# in the R06 report.  Every term is exact rational arithmetic.
ok = True
cases = 0
for L in range(3, 101):
    for r in range(1, L):
        val = ((2 ** r) * Fraction(1, 2) ** (r + 1)
               + (2 ** (L - r)) * Fraction(1, 2) ** (L - r + 1))
        cases += 1
        ok &= (val == 1)
print(f"cycle_block_z_half_cases={cases}, all_equal_1={ok}")
print("SELF_CHECK_PASS" if ok and len(nonsimple) == 5 else "SELF_CHECK_FAIL")
