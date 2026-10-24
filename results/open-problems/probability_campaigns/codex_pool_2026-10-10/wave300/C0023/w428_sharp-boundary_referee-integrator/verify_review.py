"""Independent finite checks for the C0023 referee packet; no store writes."""
from fractions import Fraction
from itertools import product


def connected(open_edges, start, target):
    reached = {start}
    fringe = [start]
    while fringe:
        u = fringe.pop()
        for a, b in open_edges:
            if a == u and b not in reached:
                reached.add(b)
                fringe.append(b)
            elif b == u and a not in reached:
                reached.add(a)
                fringe.append(a)
    return target in reached


square = [("o", "a1"), ("a1", "v"), ("o", "a2"), ("a2", "v"), ("v", "b")]
terminal = hits = a1_to_b = 0
for state in product((False, True), repeat=5):
    open_edges = [e for e, active in zip(square, state) if active]
    terminal += connected(open_edges, "o", "b")
    hits += connected(open_edges, "o", "a1") or connected(open_edges, "o", "a2")
    a1_to_b += connected(open_edges, "a1", "b")
lhs = Fraction(terminal, 32)
product_bound = Fraction(hits, 32) * Fraction(a1_to_b, 32)
assert (lhs, Fraction(hits, 32), Fraction(a1_to_b, 32), lhs - product_bound) == (
    Fraction(7, 32), Fraction(3, 4), Fraction(9, 32), Fraction(1, 128)
)

path = [("o", "a2"), ("a2", "a1"), ("a1", "b")]
selected_a1 = selected_a2 = terminal = 0
for state in product((False, True), repeat=3):
    open_edges = [e for e, active in zip(path, state) if active]
    a1_hit = connected(open_edges, "o", "a1")
    a2_hit = connected(open_edges, "o", "a2")
    selected_a1 += a1_hit
    selected_a2 += a2_hit and not a1_hit
    terminal += connected(open_edges, "o", "b")
relay_sum = Fraction(selected_a1, 8) * Fraction(1, 2) + Fraction(selected_a2, 8) * Fraction(1, 4)
assert (Fraction(terminal, 8), relay_sum, relay_sum - Fraction(terminal, 8)) == (
    Fraction(1, 8), Fraction(3, 16), Fraction(1, 16)
)

a = Fraction(3, 100)
peierls = Fraction(4, 3) * a**4 * (4 - 3 * a) / (1 - a) ** 2
assert peierls == Fraction(10557, 2352250000)
assert peierls < Fraction(1, 100000)

print("square:", lhs, Fraction(hits, 32), Fraction(a1_to_b, 32), lhs - product_bound)
print("relay:", Fraction(terminal, 8), relay_sum, relay_sum - Fraction(terminal, 8))
print("Peierls finite-cluster upper bound at p=99/100:", peierls)
