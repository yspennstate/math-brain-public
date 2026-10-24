from fractions import Fraction
from functools import lru_cache
from math import factorial

# Exact checker for one-color-renewal excursion cylinders of the
# Holroyd--Liggett 1-dependent 4-coloring.
# Formula used: P_4(x)=B(x)/(2^n (n+1)!), with B the proper-building count.

@lru_cache(None)
def building(word):
    word = tuple(word)
    if any(word[i] == word[i + 1] for i in range(len(word) - 1)):
        return 0
    if len(word) <= 1:
        return 1
    total = 0
    for i in range(len(word)):
        # Deleting i preserves properness iff its new neighbors (if both exist)
        # are different.
        if i == 0 or i == len(word) - 1 or word[i - 1] != word[i + 1]:
            total += building(word[:i] + word[i + 1:])
    return total


def p4(word):
    word = tuple(word)
    n = len(word)
    return Fraction(building(word), (2 ** n) * factorial(n + 1))


c, a = 4, 1
p_c = p4((c,))
assert p_c == Fraction(1, 4)

# Under Palm conditioning X_0=c, let r=(a) denote the c-to-c excursion
# c,a,c (gap two).  Repeating r k times gives c,a,c,a,...,c.
palm = {}
for k in range(1, 4):
    word = tuple([c, a] * k + [c])
    palm[k] = p4(word) / p_c

assert palm[1] == Fraction(1, 12)
assert palm[2] == Fraction(1, 360)
assert palm[3] == Fraction(1, 20160)

independence_diff = palm[2] - palm[1] ** 2
markov_diff = palm[3] * palm[1] - palm[2] ** 2
assert independence_diff == Fraction(-1, 240)
assert markov_diff == Fraction(-13, 3628800)

# Finite exact check of the closed form used in the report.  The report
# proves it for every k by the building recurrence; here we verify k<=8.
for k in range(1, 9):
    word = tuple([c, a] * k + [c])
    n = len(word)
    assert building(word) == 2 ** (n - 1)
    assert p4(word) / p_c == Fraction(2, factorial(2 * k + 2))

print('HL_EXCURSION_EXACT_CHECK_PASS')
print('Palm r^1 =', palm[1])
print('Palm r^2 =', palm[2])
print('Palm r^3 =', palm[3])
print('independence_diff =', independence_diff)
print('first_order_markov_diff =', markov_diff)
print('general_formula_checked_k=1..8: P_Palm(r^k)=2/(2k+2)!')
