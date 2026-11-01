"""Exact, independent checks for the two P0110 boundary packets."""
from fractions import Fraction
from itertools import product
import json
import time
from pathlib import Path


def main():
    gate = json.loads(Path("COMPUTE_GATE.json").read_text(encoding="utf-8"))["limits"]
    started = time.monotonic()
    # w379: three direct edges versus the five-edge upper detour, each weight 1 or 2.
    n, a, b = 3, 1, 2
    delta = n * (b - a) - 2 * a
    successful = 0
    assert 2 ** (2 * n + 2) <= gate["maximum_configurations"]
    for direct in product((a, b), repeat=n):
        for detour in product((a, b), repeat=n + 2):
            event = all(x == b for x in direct) and all(x == a for x in detour)
            saving = sum(direct) - min(sum(direct), sum(detour))
            assert saving >= delta * int(event)
            successful += int(event)
    q = Fraction(successful, 2 ** (2 * n + 2))
    gap_per_edge = delta * q / (n + 2)
    assert successful == 1 and q == Fraction(1, 256)
    assert gap_per_edge == Fraction(1, 1280)

    # w378: support [1,5/4], scales n=2 and Mn=4. Both axial paths are forced.
    epsilon = Fraction(1, 4)
    n, M = 2, 2
    assert M * n * epsilon < 2
    one_edge_variance = epsilon * epsilon / 12
    v_n = n * one_edge_variance
    v_mn = M * n * one_edge_variance
    ratio = v_mn / (M * v_n)
    assert ratio == 1
    # w378 L3: exact fixed-law certainty cutoff and the explicit upper-detour event.
    cutoff = Fraction(2, 1) / epsilon
    assert cutoff == 8 and 9 <= gate["maximum_integer_n"]
    n_above = 9
    margin = n_above * epsilon - 2
    delta_interval = margin / (4 * n_above + 4)
    event_probability = (delta_interval / epsilon) ** (2 * n_above + 2)
    minimum_saving = margin - (2 * n_above + 2) * delta_interval
    assert delta_interval == Fraction(1, 160)
    assert event_probability == Fraction(1, 40 ** 20)
    assert minimum_saving == Fraction(1, 8)
    assert time.monotonic() - started <= gate["wall_seconds"]
    result = {"checked_configurations": 256, "favorable_configurations": successful,
              "block_event_probability": str(q), "rigorous_linear_gap": str(gap_per_edge),
              "variance_ratio": str(ratio), "uniform_cutoff": str(cutoff),
              "above_cutoff_event_probability": str(event_probability),
              "above_cutoff_minimum_saving": str(minimum_saving), "status": "PASS"}
    Path("REPRODUCTION.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
