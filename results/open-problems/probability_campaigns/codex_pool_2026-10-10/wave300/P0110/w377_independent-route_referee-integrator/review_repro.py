"""Small exact certificates for the P0110 referee packet (no random sampling)."""

from fractions import Fraction
from itertools import product


def main() -> None:
    # Bernoulli {1,2} edge weights, each with probability 1/2.
    # A has 3 axial edges; B has 5 disjoint detour edges.
    positive = 0
    total_saving = 0
    for bits in product((0, 1), repeat=8):
        axial = 3 + sum(bits[:3])
        detour = 5 + sum(bits[3:])
        saving = max(axial - detour, 0)
        positive += saving > 0
        total_saving += saving

    delta = Fraction(total_saving, 2**8)
    mu = Fraction(3, 2)
    block_mean = 4 * mu - delta
    asymptotic_gap = delta / 4
    assert positive == 1
    assert delta == Fraction(1, 256)
    assert block_mean == Fraction(1535, 256)
    assert asymptotic_gap == Fraction(1, 1024)
    print(f"L1 positive configurations: {positive}/256")
    print(f"L2 E[(S-H)+]: {delta}; block mean: {block_mean}; axial gap >= {asymptotic_gap}")

    # w376's independent one-index oscillation: the two endpoint identities hold.
    chi_a, chi_b = Fraction(1, 3), Fraction(1, 4)
    xi_a, xi_b = Fraction(2, 3), Fraction(5, 8)
    assert chi_a == 2 * xi_a - 1
    assert chi_b == 2 * xi_b - 1
    assert chi_a - chi_b == Fraction(1, 12)
    assert xi_a - xi_b == Fraction(1, 24)
    print(f"C002 exponent gaps: chi {chi_a-chi_b}; xi {xi_a-xi_b}")

    # L3: every one of the C(6,3)=20 directed paths for k=3 loses.
    directed_costs = []
    for steps in product(("R", "U"), repeat=6):
        if steps.count("R") != 3:
            continue
        x = y = cost = 0
        for step in steps:
            if step == "R":
                cost += 2  # all horizontal square edges high
                x += 1
            else:
                cost += 1 if x == 3 else 2
                y += 1
        assert (x, y) == (3, 3)
        directed_costs.append(cost)
    assert len(directed_costs) == 20
    assert min(directed_costs) == 9
    detour_cost = 8  # down, 3 across below square, up, 3 along right column
    assert detour_cost < min(directed_costs)
    print(f"L3 diagonal witness: {len(directed_costs)} directed paths, min cost {min(directed_costs)}, detour {detour_cost}")

    # L4: the {1,2} support threshold is n>2, agreeing with k=3 above.
    assert 2 * (2 - 1) <= 2 * 1
    assert 3 * (2 - 1) > 2 * 1
    print("L4 {1,2} strict-detour threshold: n=2 no, n=3 yes")


if __name__ == "__main__":
    main()
