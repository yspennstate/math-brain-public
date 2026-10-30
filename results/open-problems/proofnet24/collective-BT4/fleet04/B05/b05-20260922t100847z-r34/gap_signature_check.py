from itertools import product

# Exact finite check for the distinct-endpoint, fully alternating direct-3x3 state.
# Normalize the reverse ports on A as d1,d2,d3 and on B as c1,c2,c3.
# A forward arc Fi has source ai on A and target bi on B.

SIGMAS = [
    {1: 2, 2: 3, 3: 1},
    {1: 3, 3: 2, 2: 1},
]
BLOCK_ORDERS = [(1, 2, 3), (1, 3, 2)]


def A_order(block_order):
    out = []
    for i in block_order:
        out += [f"d{i}", f"a{i}"]
    return out


def B_order(block_order, sigma):
    out = []
    for i in block_order:
        out += [f"b{i}", f"c{sigma[i]}"]
    return out


def insert_after_gap(order, item, gap):
    return order[: gap + 1] + [item] + order[gap + 1 :]


def alternate(seq, left_prefix):
    bits = [x.startswith(left_prefix) for x in seq]
    return all(bits[i] != bits[(i + 1) % len(bits)] for i in range(len(bits)))


def prev_d(seq, x):
    p = seq.index(x)
    for t in range(1, len(seq)):
        y = seq[(p - t) % len(seq)]
        if y.startswith("d"):
            return int(y[1:])
    raise AssertionError


def next_c(seq, x):
    p = seq.index(x)
    for t in range(1, len(seq)):
        y = seq[(p + t) % len(seq)]
        if y.startswith("c"):
            return int(y[1:])
    raise AssertionError


def cycle_count(mapping, domain):
    seen = set()
    ans = 0
    for x in domain:
        if x in seen:
            continue
        ans += 1
        y = x
        while y not in seen:
            seen.add(y)
            y = mapping[y]
    return ans


def classify(A, B, chosen):
    src = {1: "a1", 2: "a2", 3: "a3", "s": "as"}
    tar = {1: "b1", 2: "b2", 3: "b3", "s": "bs"}
    Akeep = {src[i] for i in chosen} | {"d1", "d2", "d3"}
    Bkeep = {tar[i] for i in chosen} | {"c1", "c2", "c3"}
    As = [x for x in A if x in Akeep]
    Bs = [x for x in B if x in Bkeep]
    if len(As) != 6 or len(Bs) != 6:
        return None
    if not alternate(As, "d") or not alternate(Bs, "b"):
        return None
    piA = {i: prev_d(As, src[i]) for i in chosen}
    piB = {i: next_c(Bs, tar[i]) for i in chosen}
    invA = {v: k for k, v in piA.items()}
    monodromy = {i: invA[piB[i]] for i in chosen}
    return cycle_count(monodromy, chosen)


classes = 0
insertions = 0
alternating_replacements = 0
three_cycle_replacements = 0
identity_or_transposition = 0

for sigma, ao, bo in product(SIGMAS, BLOCK_ORDERS, BLOCK_ORDERS):
    classes += 1
    A0 = A_order(ao)
    B0 = B_order(bo, sigma)
    assert classify(A0, B0, [1, 2, 3]) == 1
    for ga in range(6):
        A = insert_after_gap(A0, "as", ga)
        for gb in range(6):
            insertions += 1
            B = insert_after_gap(B0, "bs", gb)
            for drop in (1, 2, 3):
                chosen = [i for i in (1, 2, 3) if i != drop] + ["s"]
                cc = classify(A, B, chosen)
                if cc is None:
                    continue
                alternating_replacements += 1
                if cc == 1:
                    three_cycle_replacements += 1
                else:
                    identity_or_transposition += 1

print("normalized_3cycle_classes =", classes)
print("fresh_source_target_gap_insertions =", insertions)
print("one_for_one_replacements_preserving_full_alternation =", alternating_replacements)
print("still_3cycle_monodromy =", three_cycle_replacements)
print("identity_or_transposition_after_one_replacement =", identity_or_transposition)
