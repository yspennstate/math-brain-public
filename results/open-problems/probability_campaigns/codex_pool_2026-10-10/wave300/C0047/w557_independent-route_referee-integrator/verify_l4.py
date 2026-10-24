"""Independent finite-state check of w555's cycle-block offspring mean."""

from fractions import Fraction
from itertools import product


def exhaustive_mean(m: int, p: Fraction) -> Fraction:
    result = Fraction(0)
    for bits in product((0, 1), repeat=m):
        weight = p ** sum(bits) * (1 - p) ** (m - sum(bits))
        seen = {0}
        frontier = [0]
        while frontier:
            v = frontier.pop()
            for edge, neighbor in ((v, (v + 1) % m), ((v - 1) % m, (v - 1) % m)):
                if bits[edge] and neighbor not in seen:
                    seen.add(neighbor)
                    frontier.append(neighbor)
        result += weight * (len(seen) - 1) * p
    return result


def formula(m: int, p: Fraction) -> Fraction:
    return p * (2 * sum((p ** k for k in range(1, m)), Fraction(0)) - (m - 1) * p ** m)


if __name__ == "__main__":
    for m in (3, 4, 5):
        for p in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
            measured, predicted = exhaustive_mean(m, p), formula(m, p)
            assert measured == predicted, (m, p, measured, predicted)
            print(f"m={m}, p={p}: offspring mean = {measured}")
    print("9/9 exact finite-state comparisons passed")
