from fractions import Fraction

# Exact rational part of the canonical nonsyndetic pulse example.
tau = Fraction(1, 2)
eta = Fraction(1, 40)
lo = Fraction(-1, 10)
hi = Fraction(1, 10)
pad_lo = lo - 2 * eta
pad_hi = hi + 2 * eta
Ilo = Fraction(-1, 4)
Ihi = Fraction(1, 4)
assert Ilo <= pad_lo < pad_hi <= Ihi

d = Ihi - Ilo
M = max(abs(Ilo), abs(Ihi))

# Analytic inequalities proved in the report: pi^2 > 9 and exp(-1/32) > 31/32.
pi2_lower = Fraction(9, 1)
exp_lower = Fraction(31, 32)
lambda_lower = pi2_lower * exp_lower / (2 * d * d)
kappa_lower = tau * lambda_lower

assert lambda_lower == Fraction(279, 16)
assert kappa_lower == Fraction(279, 32)
assert kappa_lower > 1

# Finite exact sanity only (not the proof of density): the deleted desert blocks
# [m^3, m^3+m-1] are pairwise separated over this large range.
for m in range(2, 10000):
    assert m**3 + m - 1 < (m + 1)**3

print("PASS")
print(f"twice_padded=[{pad_lo},{pad_hi}] subset [{Ilo},{Ihi}]")
print(f"d={d} M={M}")
print(f"lambda_lower={lambda_lower}")
print(f"kappa_lower={kappa_lower}")
print("desert_disjointness_checked_m=2..9999")
