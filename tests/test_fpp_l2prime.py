import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import fpp_l2prime_kurtosis as fpp  # noqa: E402


def test_constant_weights_give_manhattan_passage_time() -> None:
    n = 6
    weights = {e: 1.0 for e in fpp._edges(n)}
    mid = n // 2
    time, path = fpp.dijkstra(weights, n, (0, mid), (n, mid))
    assert time == 6.0
    assert len(path) == 6


def test_dijkstra_matches_brute_force_on_a_small_grid() -> None:
    # every monotone lattice path on a 2x2 grid from (0,0) to (2,2), against Dijkstra
    n = 2
    rng = random.Random(3)
    weights = {e: rng.uniform(1.0, 2.0) for e in fpp._edges(n)}
    best = None
    for order in ("RRUU", "RURU", "RUUR", "URRU", "URUR", "UURR"):
        x, y, total = 0, 0, 0.0
        for step in order:
            if step == "R":
                total += weights[(x, y, 0)]
                x += 1
            else:
                total += weights[(x, y, 1)]
                y += 1
        best = total if best is None else min(best, total)
    time, _ = fpp.dijkstra(weights, n, (0, 0), (2, 2))
    assert abs(time - best) < 1e-12


def test_block_edge_count_is_two_b_times_b_plus_one() -> None:
    n, b = 20, 3
    inside = fpp.block_edges(n, b, 5, 5)
    assert len(inside) == 2 * b * (b + 1)


def test_increment_positive_part_is_never_negative_and_run_is_seeded() -> None:
    rng = random.Random(11)
    seen = []
    for _ in range(8):
        s = fpp.one_sample(rng, 10, 3, 0, 1.0, 2.0)
        if s is not None:
            assert s["delta_plus"] >= 0.0
            assert s["occupation"] >= 1
            seen.append(s)
    assert seen
    a = fpp.measure(10, 3, 0, 6, 5, 1.0, 2.0)
    b = fpp.measure(10, 3, 0, 6, 5, 1.0, 2.0)
    assert a["m2"] == b["m2"] and a["m4"] == b["m4"]
