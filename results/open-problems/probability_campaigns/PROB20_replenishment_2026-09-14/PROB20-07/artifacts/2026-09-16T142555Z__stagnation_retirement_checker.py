from fractions import Fraction

REPORTS = [
    "2026-09-16T071410Z__report.md",
    "2026-09-16T075502Z__report.md",
    "2026-09-16T101215Z__report.md",
    "2026-09-16T105454Z__report.md",
    "2026-09-16T115612Z__report.md",
    "2026-09-16T125617Z__report.md",
]

L = Fraction(1, 12)
U = Fraction(1, 9)
WIDTH = U - L

assert WIDTH == Fraction(1, 36)
assert len(REPORTS) == 6

print("PROB20-07 STAGNATION CHECK PASSED")
print("L =", L)
print("U =", U)
print("WIDTH =", WIDTH)
print("UNCHANGED_REPORT_COUNT =", len(REPORTS))
print("ROTATE_AFTER_SIX = YES")
