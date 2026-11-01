# Exact finite checker for the non-dominant swap obstruction in R12/D0011.
# Pure integer arithmetic; no floating point.

weights = (4, 3, 2, 2)
old_high = (1, 0, 1, 0)
old_low  = (0, 1, 0, 1)
new_high = (1, 0, 0, 0)
new_low  = (0, 1, 1, 1)


def weighted_sum(atom):
    return sum(w * b for w, b in zip(weights, atom))

old = (weighted_sum(old_high), weighted_sum(old_low))
new = (weighted_sum(new_high), weighted_sum(new_low))

print("weights", weights)
print("old_atoms", old_high, old_low, "old_sums", list(old))
print("new_atoms", new_high, new_low, "new_sums", list(new))
print("sum_preserved", sum(old), sum(new))
print("old_sq_sum", sum(x*x for x in old))
print("new_sq_sum", sum(x*x for x in new))

assert old == (6, 5)
assert new == (4, 7)
assert sum(old) == sum(new) == 11
assert sum(x*x for x in old) == 61
assert sum(x*x for x in new) == 65
# Thus the overlap-reducing coordinate swap increases the convex objective phi(x)=x^2.
print("ALL_EXACT_CHECKS_PASS")
