import itertools


def interval_vertices(order, start, end):
    pos = {x: i for i, x in enumerate(order)}
    out = [start]
    k = (pos[start] + 1) % len(order)
    while order[k] != end:
        out.append(order[k])
        k = (k + 1) % len(order)
    out.append(end)
    return set(out)


def disjoint_intervals(order, pairs):
    return interval_vertices(order, *pairs[0]).isdisjoint(
        interval_vertices(order, *pairs[1])
    )


def rotations_fixed(items, fixed):
    for tail in itertools.permutations([x for x in items if x != fixed]):
        yield (fixed,) + tail


def has_compatible_2x2(OA, OB):
    for FI in itertools.combinations((1, 2, 3), 2):
        for GJ in itertools.combinations((1, 2, 3), 2):
            for gp in itertools.permutations(GJ):
                A_pairs = [(f"D{gp[t]}", f"A{FI[t]}") for t in (0, 1)]
                B_pairs = [(f"B{FI[t]}", f"G{gp[t]}") for t in (0, 1)]
                if disjoint_intervals(OA, A_pairs) and disjoint_intervals(OB, B_pairs):
                    return True
    return False


OA_all = list(
    rotations_fixed(["A1", "A2", "A3", "D1", "D2", "D3"], "A1")
)
OB_all = list(
    rotations_fixed(["B1", "B2", "B3", "G1", "G2", "G3"], "B1")
)
bad = []
for OA in OA_all:
    for OB in OB_all:
        if not has_compatible_2x2(OA, OB):
            bad.append((OA, OB))

print("cyclic_order_pairs_tested =", len(OA_all) * len(OB_all))
print("no_compatible_2x2 =", len(bad))
print("first_countermodel =", bad[0])
