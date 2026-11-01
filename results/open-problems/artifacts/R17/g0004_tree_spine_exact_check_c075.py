from fractions import Fraction
from itertools import product


def tree_edges(d, h):
    edges = []
    for depth in range(h):
        for prefix in product(range(d), repeat=depth):
            for c in range(d):
                edges.append((prefix, prefix + (c,)))
    return edges


def verify(d, h, p):
    edges = tree_edges(d, h)
    edge_index = {e: i for i, e in enumerate(edges)}
    leaves = list(product(range(d), repeat=h))

    total = Fraction(0)
    connection_probability = Fraction(0)
    failure_probability = Fraction(0)
    q_expectations = {b: Fraction(0) for b in leaves}

    for bits in product([0, 1], repeat=len(edges)):
        k = sum(bits)
        prob = p**k * (1 - p)**(len(edges) - k)
        total += prob

        connected = []
        q = {}
        for b in leaves:
            is_connected = True
            for depth in range(h):
                if not bits[edge_index[(b[:depth], b[: depth + 1])]]:
                    is_connected = False
                    break
            if is_connected:
                connected.append(b)

            # q_b=1 iff every sibling edge along the root-to-b spine is closed.
            qb = 1
            for depth in range(h):
                parent = b[:depth]
                chosen_child = b[depth]
                for c in range(d):
                    if c == chosen_child:
                        continue
                    if bits[edge_index[(parent, parent + (c,))]]:
                        qb = 0
                        break
                if not qb:
                    break
            q[b] = qb
            if qb:
                q_expectations[b] += prob

        if connected:
            connection_probability += prob
            if min(q[b] for b in connected) == 1:
                failure_probability += prob

    epsilon_formula = (1 - p) ** ((d - 1) * h)
    failure_formula = (d * p * (1 - p) ** (d - 1)) ** h

    assert total == 1
    assert set(q_expectations.values()) == {epsilon_formula}
    assert failure_probability == failure_formula
    assert failure_probability <= connection_probability

    return {
        "d": d,
        "h": h,
        "p": p,
        "edges": len(edges),
        "epsilon": epsilon_formula,
        "failure_probability": failure_probability,
        "connection_probability": connection_probability,
        "conditional_failure_ratio": failure_probability / connection_probability,
    }


cases = [
    (2, 2, Fraction(2, 3)),
    (2, 3, Fraction(2, 3)),
    (3, 2, Fraction(1, 2)),
]

for case in cases:
    result = verify(*case)
    print(
        "d={d} h={h} p={p} edges={edges} epsilon={epsilon} "
        "failure={failure_probability} connection={connection_probability} "
        "R={conditional_failure_ratio}".format(**result)
    )

print("EXACT_TREE_SPINE_CHECK_PASS")
