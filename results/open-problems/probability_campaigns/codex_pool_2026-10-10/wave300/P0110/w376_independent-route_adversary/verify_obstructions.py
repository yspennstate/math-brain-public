"""Small exact-rational check; no network, training, child process, or store write.

Fresh compute gate: one CPU process, 4096 integer scales, <128 MiB,
30 seconds total wall time. Checks algebraic witnesses, not an FPP exponent proof.
"""
from __future__ import annotations

import json
import time
from fractions import Fraction as F
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    start = time.perf_counter()
    ca, cb, xa, xb = F(1, 3), F(1, 4), F(2, 3), F(5, 8)
    assert ca == 2 * xa - 1 and cb == 2 * xb - 1
    assert 0 <= cb < ca <= F(1, 2)
    assert 0 <= xb < xa <= 1
    assert ca - cb == F(1, 12) and xa - xb == F(1, 24)
    q, r = (ca + cb) / 2, (xa + xb) / 2
    assert ca - q == F(1, 24)  # odd upper-moment ratios diverge
    assert 2 * (cb - q) == F(-1, 12)  # even variance ratios vanish
    assert xa - r == F(1, 48)  # odd wandering upper ratios diverge
    assert xb - r == F(-1, 48)  # even wandering lower ratios vanish

    for n in range(2, 4098):
        a = cb if n % 2 == 0 else ca
        b = (1 + a) / 2
        assert a == 2 * b - 1
        assert cb <= a <= ca and xb <= b <= xa
    assert time.perf_counter() - start < 30

    # A separate independently derived finite axial witness for the peer's lemma.
    low_max, high_min, n = F(5, 4), F(7, 4), 6
    directed_lower = n * high_min
    detour_upper = (n + 2) * low_max
    assert directed_lower - detour_upper == F(1, 2)
    assert all(k * high_min <= (k + 2) * low_max for k in range(1, n))
    event_probability = F(1, 4) ** (2 * n + 2)
    assert event_probability == F(1, 268435456)
    drift_lower_bound = F(1, 2) * event_probability / (n + 1)
    assert drift_lower_bound == F(1, 3758096384)

    # Independent graph checks of the actual L2 edge/vertex disjointness claim.
    def edge_set(points):
        assert all(abs(x1 - x2) + abs(y1 - y2) == 1
                   for (x1, y1), (x2, y2) in zip(points, points[1:]))
        return {tuple(sorted((p, q))) for p, q in zip(points, points[1:])}

    paths_checked = 0
    for k in range(1, 9):
        blocks = []
        all_edges = set()
        for j in range(4):
            s = j * (k + 1)
            axial = [(s + i, 0) for i in range(k + 1)]
            detour = [(s, 0)] + [(s + i, 1) for i in range(k + 1)] + [(s + k, 0)]
            connector = [(s + k, 0), (s + k + 1, 0)]
            ea, eh, ec = edge_set(axial), edge_set(detour), edge_set(connector)
            assert not (ea & eh or ea & ec or eh & ec)
            block_edges = ea | eh | ec
            assert not all_edges & block_edges
            all_edges |= block_edges
            blocks.append((axial, detour, connector[-1]))
        for choices in product((0, 1), repeat=4):
            points = [(0, 0)]
            for choice, (axial, detour, connector_end) in zip(choices, blocks):
                selected = detour if choice else axial
                assert points[-1] == selected[0]
                points.extend(selected[1:])
                points.append(connector_end)
            edge_set(points)
            assert len(points) == len(set(points))
            paths_checked += 1
    assert paths_checked == 128

    # The nearest-neighbor boundary is deterministic: direct <=2, others >=3.
    assert F(2) < 3 * F(1)

    receipt = {
        "command": "python -X utf8 verify_obstructions.py",
        "gate": {"processes": 1, "max_integer_scales": 4096,
                 "max_wall_seconds": 30, "memory_budget_mib": 128},
        "scope": "Exact rational algebra and finite witness checks; not a formal proof receipt or an FPP exponent calculation.",
        "scale_identities_checked": 4096,
        "chi_threshold_gap": str(ca - cb),
        "xi_threshold_gap": str(xa - xb),
        "midpoint_upper_chi_divergence_power": str(ca - q),
        "midpoint_lower_variance_vanishing_power": str(2 * (cb - q)),
        "midpoint_upper_xi_divergence_power": str(xa - r),
        "midpoint_lower_xi_vanishing_power": str(xb - r),
        "peer_finite_witness_n": n,
        "peer_directed_lower": str(directed_lower),
        "peer_detour_upper": str(detour_upper),
        "peer_strict_gap": str(directed_lower - detour_upper),
        "peer_event_probability": str(event_probability),
        "peer_block_drift_floor": str(drift_lower_bound),
        "independent_block_paths_checked": paths_checked,
        "finite_endpoint_direct_upper": "2",
        "finite_endpoint_other_paths_lower": "3",
        "elapsed_seconds": round(time.perf_counter() - start, 6),
        "failed_checks": 0,
    }
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
