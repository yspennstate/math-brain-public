from fractions import Fraction


def decompose(a):
    a = tuple(Fraction(x) for x in a)
    assert sum(a).denominator == 1
    assert all(Fraction(0) <= x <= Fraction(1) for x in a)

    def rec(v):
        fractional = [i for i, x in enumerate(v) if x not in (0, 1)]
        if not fractional:
            return {tuple(int(x) for x in v): Fraction(1)}
        assert len(fractional) >= 2
        i, j = fractional[:2]
        eps_plus = min(1 - v[i], v[j])
        eps_minus = min(v[i], 1 - v[j])
        assert eps_plus > 0 and eps_minus > 0

        vp = list(v)
        vm = list(v)
        vp[i] += eps_plus
        vp[j] -= eps_plus
        vm[i] -= eps_minus
        vm[j] += eps_minus
        theta = eps_minus / (eps_plus + eps_minus)

        out = {}
        for vertex, weight in rec(tuple(vp)).items():
            out[vertex] = out.get(vertex, Fraction(0)) + theta * weight
        for vertex, weight in rec(tuple(vm)).items():
            out[vertex] = out.get(vertex, Fraction(0)) + (1 - theta) * weight
        return out

    return rec(a)


cases = [
    [Fraction(1, 2), Fraction(1, 2), Fraction(1), Fraction(0)],
    [Fraction(1, 3), Fraction(2, 3), Fraction(1, 4), Fraction(3, 4)],
    [Fraction(2, 5), Fraction(3, 5), Fraction(4, 5), Fraction(1, 5), Fraction(1), Fraction(0)],
    [Fraction(1, 7)] * 7 + [Fraction(6, 7)] * 7,
]

for case_index, a in enumerate(cases):
    decomposition = decompose(a)
    total_weight = sum(decomposition.values(), Fraction(0))
    selected_cells = sum(a)
    assert total_weight == 1
    for vertex, weight in decomposition.items():
        assert weight > 0
        assert sum(vertex) == selected_cells
        assert all(bit in (0, 1) for bit in vertex)
    reconstruction = [
        sum(weight * vertex[i] for vertex, weight in decomposition.items())
        for i in range(len(a))
    ]
    assert reconstruction == [Fraction(x) for x in a]
    print(case_index, len(decomposition), int(selected_cells))

print("QFORM_B13_R18_HYPERSIMPLEX_CHECK_PASS")
