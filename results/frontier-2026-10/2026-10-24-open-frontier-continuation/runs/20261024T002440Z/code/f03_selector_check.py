"""Reproduce the frozen-orbit check for the mixed-sign cone selector.

This checks a closed-form terminal-gate rule against literal Euler iteration.
The random sample is deterministic and is not part of the proof.
"""

import math
import random


def selected_by_formula(rho, gamma, r1, r2, z, x, y):
    assert -1 < rho < 0 and gamma > 0 and r1 < 0 < r2 and z != 0
    if z > 0:
        if y > 0:
            return 2
        if x < 0:
            return 0
        nx = math.ceil(x / (gamma * z * abs(r1)))
        return 2 if y + gamma * abs(rho) * z * abs(r1) * nx > 0 else 0
    if x > 0:
        return 1
    if y < 0:
        return 0
    ny = math.ceil(y / (gamma * abs(z) * r2))
    return 1 if x + gamma * abs(rho) * abs(z) * r2 * ny > 0 else 0


def selected_by_iteration(rho, gamma, r1, r2, z, x, y):
    for n in range(100_000):
        sector = int(x > 0) + 2 * int(y > 0)
        if sector == 0:
            return 0, n
        if z > 0 and sector == 2:
            return 2, n
        if z < 0 and sector == 1:
            return 1, n
        active1 = r1 if x > 0 else 0.0
        active2 = r2 if y > 0 else 0.0
        dx = gamma * z * (active1 + rho * active2)
        dy = gamma * z * (rho * active1 + active2)
        x += dx
        y += dy
    raise RuntimeError("orbit failed to settle within 100000 steps")


def main():
    rng = random.Random(451)
    count = 100_000
    terminal_counts = {0: 0, 1: 0, 2: 0}
    longest = 0
    for _ in range(count):
        rho = -rng.uniform(0.01, 0.99)
        gamma = rng.uniform(0.05, 3.0)
        r1 = -rng.uniform(0.05, 3.0)
        r2 = rng.uniform(0.05, 3.0)
        z = rng.choice((-1, 1)) * rng.uniform(0.05, 3.0)
        x, y = rng.uniform(-3.0, 3.0), rng.uniform(-3.0, 3.0)
        predicted = selected_by_formula(rho, gamma, r1, r2, z, x, y)
        actual, steps = selected_by_iteration(rho, gamma, r1, r2, z, x, y)
        if predicted != actual:
            raise AssertionError((predicted, actual, rho, gamma, r1, r2, z, x, y))
        terminal_counts[actual] += 1
        longest = max(longest, steps)

    example = selected_by_iteration(-0.5, 1.0, -1.0, 1.0, 1.0, 0.1, -0.1)
    assert example[0] == selected_by_formula(-0.5, 1.0, -1.0, 1.0, 1.0, 0.1, -0.1) == 2
    print(f"seed=451 samples={count} mismatches=0")
    print(f"terminal_counts={terminal_counts} max_steps={longest}")
    print("overshoot_example: z=1 rho=-0.5 r=(-1,1) gamma=1 v0=(0.1,-0.1) selector=2")


if __name__ == "__main__":
    main()
