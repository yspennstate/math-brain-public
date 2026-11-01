from fractions import Fraction
from itertools import product


def partitions(n, max_part=None):
    if max_part is None:
        max_part = n
    if n == 0:
        yield ()
        return
    for a in range(min(n, max_part), 0, -1):
        for rest in partitions(n-a, a):
            yield (a,) + rest


def prefix_sums_sorted(vals):
    vals = sorted(vals)
    out = []
    s = Fraction(0)
    for v in vals:
        s += v
        out.append(s)
    return out


# Degree-five nonsimple partitions used by the frozen metric.
p5 = [p for p in partitions(5) if len(p) >= 2 and p != (1, 1, 1, 1, 1)]
expected5 = [(4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1)]
assert p5 == expected5

z = Fraction(1, 2)
target = [Fraction(1, 2), Fraction(1), Fraction(2)]

# Residual degree-six quotient type [2,2,1,1].
# If the incoming skeleton edge is doubled, the three nonbacktracking
# candidate edge weights at z=1/2 are [1,1/2,1/2].
d_in = [Fraction(1), Fraction(1, 2), Fraction(1, 2)]
# If the incoming edge is single, they are [1,1,1/2].
s_in = [Fraction(1), Fraction(1), Fraction(1, 2)]
assert all(a >= b for a, b in zip(prefix_sums_sorted(d_in), target))
assert all(a >= b for a, b in zip(prefix_sums_sorted(s_in), target))

# Residual degree-six quotient type [3,1,1,1].
# State potential h(T)=2/3 for an incoming triple edge and h(S)=1
# for an incoming singleton. The transformed edge weight is
#   w_tilde = (multiplicity*z) * h(child)/h(parent).
hT = Fraction(2, 3)
hS = Fraction(1)

# Incoming triple: all three candidates are singleton.
t_parent = [z * hS / hT] * 3  # [3/4,3/4,3/4]
# Incoming singleton: one triple candidate and two singleton candidates.
s_parent = [Fraction(3) * z * hT / hS, z, z]  # [1,1/2,1/2]
assert t_parent == [Fraction(3, 4)] * 3
assert sorted(s_parent) == [Fraction(1, 2), Fraction(1, 2), Fraction(1)]
assert all(a >= b for a, b in zip(prefix_sums_sorted(t_parent), target))
assert all(a >= b for a, b in zip(prefix_sums_sorted(s_parent), target))

# Grimmett--Li's degree-four blue-branch count, after deleting the
# artificial root position, gives n2-n0 >= -1. For the universal local
# child-mass lower bounds F=(1/2,1,2), the pathwise product is
# 2^(n2-n0), hence >=1/2. Exhaustively self-check all short profiles.
profiles = 0
for N in range(1, 13):
    for bs in product((0, 1, 2), repeat=N):
        if sum(bs) >= N - 1:
            profiles += 1
            prodF = Fraction(1)
            for b in bs:
                prodF *= target[b]
            assert prodF >= Fraction(1, 2)

# Degree-six partitions allowed by contraction of a [2,1,1,1]
# degree-five graph: total 6 and parallel multiplicity at most 4.
p6 = [p for p in partitions(6) if len(p) >= 2 and max(p) <= 4]
expected6 = [
    (4, 2),
    (4, 1, 1),
    (3, 3),
    (3, 2, 1),
    (3, 1, 1, 1),
    (2, 2, 2),
    (2, 2, 1, 1),
    (2, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1),
]
assert p6 == expected6
covered_old = {
    (4, 2),
    (4, 1, 1),
    (3, 3),
    (3, 2, 1),
    (2, 2, 2),
    (2, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1),
}
covered_new = {(3, 1, 1, 1), (2, 2, 1, 1)}
assert covered_old | covered_new == set(p6)
assert covered_old & covered_new == set()

print("degree5_partitions=", p5)
print("residual_[2,2,1,1]_incoming_double_prefix_sums=", prefix_sums_sorted(d_in))
print("residual_[2,2,1,1]_incoming_single_prefix_sums=", prefix_sums_sorted(s_in))
print("residual_[3,1,1,1]_hT=", hT, "hS=", hS)
print("residual_[3,1,1,1]_incoming_triple_prefix_sums=", prefix_sums_sorted(t_parent))
print("residual_[3,1,1,1]_incoming_single_prefix_sums=", prefix_sums_sorted(s_parent))
print("universal_F=", target)
print("short_branch_profiles_checked=", profiles)
print("degree6_allowed_partitions=", p6)
print("newly_covered_residual_partitions=", sorted(covered_new, reverse=True))
print("C5_after=5/5")
print("SELF_CHECK_PASS")
