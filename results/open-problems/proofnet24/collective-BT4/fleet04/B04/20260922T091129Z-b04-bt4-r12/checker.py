from itertools import product


def pivot(cycle, port, sink):
    """One tight light-support pivot; return new support, freed hole, forced local arcs."""
    i = cycle.index(port)
    first = cycle[(i + 1) % len(cycle)]
    second = cycle[(i + 2) % len(cycle)]
    new = cycle[:]
    new[(i + 1) % len(cycle)] = sink
    arcs = {(port, sink), (sink, first), (sink, second)}
    return new, first, arcs


def pred(cycle, v):
    i = cycle.index(v)
    return cycle[(i - 1) % len(cycle)]


# Start with c -> x -> y -> z -> c. P0 inserts sink t and frees x.
base = ["c", "x", "y", "z"]
S0, h0, A0 = pivot(base, "c", "t")
assert h0 == "x"
assert ("t", "x") in A0

rows = []
for first_break, second_break in product([0, 1], repeat=2):
    # A later pivot can break guard c->t only at c or pred(c).
    d = "c" if first_break == 0 else pred(S0, "c")
    S1, h1, A1 = pivot(S0, d, "v")

    # If x next pivots on this support and breaks the new guard d->v,
    # its port is d or pred(d).
    e = d if second_break == 0 else pred(S1, d)
    S2, h2, A2 = pivot(S1, e, "x")

    arcs = A0 | A1 | A2
    triangle = {("t", "x"), ("x", "v"), ("v", "t")}
    ok = triangle <= arcs
    rows.append((first_break, second_break, d, e, h1, h2, ok))
    assert ok, (S0, S1, S2, arcs)

print("cases=", len(rows))
for row in rows:
    print(row)
print("all_guard_break_cases_force_triangle=t->x->v->t")
