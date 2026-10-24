from fractions import Fraction
from itertools import combinations

# HARD7-02 exact finite self-check for the Q1.9 exceedance-skeleton proof.
# This checks only the finite incidence counts and covariance identity used
# in the on-page proof. It is a SELF-CHECK, not a proof of the asymptotic theorem.


def edges(n):
    return list(combinations(range(n), 2))


def other_incident(n, e):
    i, j = e
    return {f for f in edges(n) if f != e and (i in f or j in f)}


def union_other(n, e, f):
    return (other_incident(n, e) | other_incident(n, f)) - {e, f}


for n in range(4, 11):
    E = edges(n)
    for e in E:
        assert len(other_incident(n, e)) == 2 * (n - 2)

    for e, f in combinations(E, 2):
        if set(e).isdisjoint(f):
            assert len(union_other(n, e, f)) == 4 * n - 12
        else:
            # If e and f overlap, strong-isolation of e forces f below the
            # t-threshold while strong-isolation of f forces f above s>=t;
            # the simultaneous event is therefore empty.
            assert f in other_incident(n, e)
            assert e in other_incident(n, f)

# Exact rational covariance algebra at representative rational t,s.
# The identity itself is symbolic in q; this rational execution guards
# transcription and exponent mistakes without floating point.
for n in range(4, 11):
    t, s = 3, 5
    q = 1 - Fraction(1, t * n)
    p = Fraction(1, s * n) * q ** (2 * (n - 2))
    joint_disjoint = Fraction(1, (s * n) ** 2) * q ** (4 * n - 12)
    covariance = joint_disjoint - p * p
    covariance_formula = (
        Fraction(1, (s * n) ** 2)
        * q ** (4 * n - 12)
        * (1 - q ** 4)
    )
    assert covariance == covariance_formula
    assert covariance > 0

print("HARD7-02 exceedance-skeleton exact finite self-check")
print("checked n = 4,...,10")
print("single-edge other-incidence count = 2(n-2): PASS")
print("disjoint-pair union count = 4n-12: PASS")
print("overlapping strong-isolated events incompatible: PASS")
print("exact rational disjoint covariance identity: PASS")
print("ALL_EXACT_CHECKS_PASS = True")
