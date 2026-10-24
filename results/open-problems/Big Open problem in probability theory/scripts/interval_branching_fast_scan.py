"""Fast floating-point interval branching scans for T_3 x Z.

The exact interval_branching_bound.py enumerates horizontal seed masks and
vertical edge masks.  This diagnostic computes the same transition law in
floating point by scanning vertical open components.  It is not a certificate;
it is used to decide whether a larger cap is worth an exact rational
certificate.
"""

from __future__ import annotations

import argparse


def finalize_component(
    distribution: dict[tuple[int, int, int, int], float],
    comp_len: int,
    parent_sites: int,
    p: float,
) -> dict[tuple[int, int, int, int], float]:
    output: dict[tuple[int, int, int, int], float] = {}
    seed_probability = 0.0 if parent_sites == 0 else 1.0 - (1.0 - p) ** parent_sites

    for (best, run, _old_len, _old_parent), mass in distribution.items():
        if seed_probability:
            next_run = run + comp_len
            next_best = max(best, next_run)
            output[(next_best, next_run, 0, 0)] = (
                output.get((next_best, next_run, 0, 0), 0.0)
                + mass * seed_probability
            )
        unseeded_probability = 1.0 - seed_probability
        if unseeded_probability:
            output[(best, 0, 0, 0)] = (
                output.get((best, 0, 0, 0), 0.0)
                + mass * unseeded_probability
            )

    return output


def capped_add_state(
    output: dict[tuple[int, int, int, int], float],
    best: int,
    run: int,
    comp_len: int,
    parent_sites: int,
    mass: float,
    cap: int,
) -> None:
    key = (min(cap, best), min(cap, run), min(cap, comp_len), min(cap, parent_sites))
    output[key] = output.get(key, 0.0) + mass


def transition_probabilities(m: int, cap: int, p: float) -> list[float]:
    left = -(cap - 1)
    right = (m - 1) + (cap - 1)

    def is_parent_site(site: int) -> int:
        return 1 if 0 <= site < m else 0

    states: dict[tuple[int, int, int, int], float] = {
        (0, 0, 1, is_parent_site(left)): 1.0
    }
    q = 1.0 - p

    for site in range(left, right):
        next_site = site + 1
        next_parent = is_parent_site(next_site)
        next_states: dict[tuple[int, int, int, int], float] = {}

        for (best, run, comp_len, parent_sites), mass in states.items():
            capped_add_state(
                next_states,
                best,
                run,
                comp_len + 1,
                parent_sites + next_parent,
                mass * p,
                cap,
            )

            finalized = finalize_component(
                {(best, run, comp_len, parent_sites): mass * q},
                comp_len,
                parent_sites,
                p,
            )
            for (final_best, final_run, _zero_len, _zero_parent), final_mass in finalized.items():
                capped_add_state(
                    next_states,
                    final_best,
                    final_run,
                    1,
                    next_parent,
                    final_mass,
                    cap,
                )

        states = next_states

    final_distribution: dict[int, float] = {}
    for (best, run, comp_len, parent_sites), mass in states.items():
        finalized = finalize_component(
            {(best, run, comp_len, parent_sites): mass},
            comp_len,
            parent_sites,
            p,
        )
        for (final_best, _final_run, _zero_len, _zero_parent), final_mass in finalized.items():
            final_type = min(cap, final_best)
            final_distribution[final_type] = (
                final_distribution.get(final_type, 0.0) + final_mass
            )

    probabilities = [0.0] * (cap + 1)
    for child_type, probability in final_distribution.items():
        probabilities[child_type] += probability
    total = sum(probabilities)
    if abs(total - 1.0) > 1e-9:
        raise ArithmeticError(f"transition probabilities sum to {total}")
    return probabilities


def mean_matrix(cap: int, p: float, forward_degree: int) -> list[list[float]]:
    return [
        [
            forward_degree * transition_probabilities(m, cap, p)[child_type]
            for child_type in range(1, cap + 1)
        ]
        for m in range(1, cap + 1)
    ]


def perron_lower(matrix: list[list[float]], iterations: int) -> float:
    size = len(matrix)
    vector = [1.0 / size] * size
    for _ in range(iterations):
        image = [sum(matrix[row][col] * vector[col] for col in range(size)) for row in range(size)]
        total = sum(image)
        vector = [entry / total for entry in image]
    image = [sum(matrix[row][col] * vector[col] for col in range(size)) for row in range(size)]
    return min(image[row] / vector[row] for row in range(size))


def spectral_lower(cap: int, p: float, forward_degree: int, iterations: int) -> float:
    return perron_lower(mean_matrix(cap, p, forward_degree), iterations)


def find_threshold(cap: int, forward_degree: int, iterations: int) -> float:
    lo = 0.0
    hi = 0.5
    for _ in range(50):
        mid = (lo + hi) / 2.0
        if spectral_lower(cap, mid, forward_degree, iterations) > 1.0:
            hi = mid
        else:
            lo = mid
    return hi


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cap", type=int, default=10)
    parser.add_argument("--p", type=float)
    parser.add_argument("--forward-degree", type=int, default=2)
    parser.add_argument("--iterations", type=int, default=1000)
    parser.add_argument("--threshold", action="store_true")
    args = parser.parse_args()

    if args.threshold:
        threshold = find_threshold(args.cap, args.forward_degree, args.iterations)
        print(f"cap={args.cap}")
        print(f"threshold_upper={threshold:.12g}")
        print(
            "spectral_lower_at_threshold="
            f"{spectral_lower(args.cap, threshold, args.forward_degree, args.iterations):.12g}"
        )
        return

    if args.p is None:
        raise SystemExit("--p is required unless --threshold is set")

    matrix = mean_matrix(args.cap, args.p, args.forward_degree)
    print(f"cap={args.cap}")
    print(f"p={args.p:.12g}")
    print(f"forward_degree={args.forward_degree}")
    print(f"spectral_lower_float={perron_lower(matrix, args.iterations):.12g}")
    print("row_sums=[" + ", ".join(f"{sum(row):.12g}" for row in matrix) + "]")


if __name__ == "__main__":
    main()
