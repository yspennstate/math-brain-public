from fractions import Fraction as Q


def alpha(d, e):
    return (Q(1, 2) - Q(1, 2**e)) / (Q(1) - Q(1, 2**e) - Q(1, 2**d))


def F_half(d, e, a):
    return a * Q(1, 2**d) + (1 - a) * (Q(1) - Q(1, 2**e))


def pivot_mean(d, e, a):
    return a * Q(d, 2**(d - 1)) + (1 - a) * Q(e, 2**(e - 1))


def R(r, d, e, a):
    return a * (r**d) + (1 - a) * (Q(1) - Q(1, 2**(e - 1)) + r**e)


# Exact source-counterexample arithmetic: d=2, e=3.
a = alpha(2, 3)
assert a == Q(3, 5)
assert 1 - a == Q(2, 5)
assert F_half(2, 3, a) == Q(1, 2)
assert pivot_mean(2, 3, a) == Q(9, 10)
assert R(Q(1, 4), 2, 3, a) == Q(11, 32)
assert R(Q(1, 2), 2, 3, a) == Q(1, 2)

# Independent finite stress-check of the two-parameter strengthening.
for d in range(2, 21):
    for e in range(2, 21):
        if d == e:
            continue
        a = alpha(d, e)
        assert Q(0) < a < Q(1)
        assert F_half(d, e, a) == Q(1, 2)
        assert pivot_mean(d, e, a) < 1
        assert R(Q(1, 2), d, e, a) == Q(1, 2)
        assert R(Q(1, 4), d, e, a) > Q(1, 4)
        assert R(Q(1, 4), d, e, a) < Q(1, 2)

print("P0033 independent exact audit")
print("d=2,e=3 alpha =", alpha(2, 3))
print("d=2,e=3 beta  =", 1 - alpha(2, 3))
print("d=2,e=3 pivot =", pivot_mean(2, 3, alpha(2, 3)))
print("d=2,e=3 R(1/4)=", R(Q(1, 4), 2, 3, alpha(2, 3)))
print("d=2,e=3 R(1/2)=", R(Q(1, 2), 2, 3, alpha(2, 3)))
print("grid d,e in [2,20], d != e: ALL_EXACT_CHECKS_PASS")
