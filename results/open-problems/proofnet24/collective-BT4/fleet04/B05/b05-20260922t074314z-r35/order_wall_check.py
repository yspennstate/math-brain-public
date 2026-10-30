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
    a = interval_vertices(order, *pairs[0])
    b = interval_vertices(order, *pairs[1])
    return a.isdisjoint(b)


def legal_matchings(OA, OB, f_sources, f_targets):
    good = []
    for pi in [(0, 1), (1, 0)]:
        A_pairs = [(f"D{pi[i] + 1}", f_sources[i]) for i in (0, 1)]
        B_pairs = [(f_targets[i], f"G{pi[i] + 1}") for i in (0, 1)]
        if disjoint_intervals(OA, A_pairs) and disjoint_intervals(OB, B_pairs):
            good.append(pi)
    return good


def rotations_fixed(items, fixed):
    for tail in itertools.permutations([x for x in items if x != fixed]):
        yield (fixed,) + tail


# Original F_i: A_i -> B_i; reverse G_j: G_j -> D_j.
initial = []
for OA in rotations_fixed(["D1", "D2", "A1", "A2"], "D1"):
    for OB in rotations_fixed(["G1", "G2", "B1", "B2"], "G1"):
        pa = []
        pb = []
        for pi in [(0, 1), (1, 0)]:
            if disjoint_intervals(
                OA, [(f"D{pi[i] + 1}", f"A{i + 1}") for i in (0, 1)]
            ):
                pa.append(pi)
            if disjoint_intervals(
                OB, [(f"B{i + 1}", f"G{pi[i] + 1}") for i in (0, 1)]
            ):
                pb.append(pi)
        if len(pa) == 1 and len(pb) == 1 and pa[0] != pb[0]:
            initial.append((OA, OB, pa[0], pb[0]))

bad = []
extended = 0
for OA0, OB0, _, _ in initial:
    for OA in rotations_fixed(["D1", "D2", "A1", "A2", "A3"], "D1"):
        if tuple(x for x in OA if x != "A3") != OA0:
            continue
        for OB in rotations_fixed(
            ["G1", "G2", "B1", "B2", "B3", "B4"], "G1"
        ):
            if tuple(x for x in OB if x not in ("B3", "B4")) != OB0:
                continue
            extended += 1
            resolved = False
            for keep in (1, 2):
                for target in ("B3", "B4"):
                    if legal_matchings(
                        OA,
                        OB,
                        [f"A{keep}", "A3"],
                        [f"B{keep}", target],
                    ):
                        resolved = True
                        break
                if resolved:
                    break
            if not resolved:
                bad.append((OA, OB))

print("initial_parity_mismatch_orders =", len(initial))
print("extended_fresh_fan_orders =", extended)
print("unresolved_by_pure_cyclic_order =", len(bad))
print("first_unresolved =", bad[0])
