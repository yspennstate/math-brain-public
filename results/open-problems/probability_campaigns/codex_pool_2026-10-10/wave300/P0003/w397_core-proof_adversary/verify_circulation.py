"""Exact, bounded arithmetic check of the hexagon obstruction; no SAW simulation."""
from __future__ import annotations

import argparse
import json
import time
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path


@dataclass(frozen=True)
class E:
    """a+b*w, w=exp(i*pi/3), w*w=w-1; exact rational arithmetic."""

    a: Q = Q(0)
    b: Q = Q(0)

    def __add__(self, other: E) -> E:
        return E(self.a + other.a, self.b + other.b)

    def __neg__(self) -> E:
        return E(-self.a, -self.b)

    def __sub__(self, other: E) -> E:
        return self + (-other)

    def __mul__(self, other: E) -> E:
        return E(self.a * other.a - self.b * other.b,
                 self.a * other.b + self.b * other.a + self.b * other.b)

    def norm2(self) -> Q:
        return self.a * self.a + self.a * self.b + self.b * self.b

    def inverse(self) -> E:
        n = self.norm2()
        if not n:
            raise ZeroDivisionError
        return E((self.a + self.b) / n, -self.b / n)

    def __truediv__(self, other: E) -> E:
        return self * other.inverse()

    def conjugate(self) -> E:
        return E(self.a + self.b, -self.b)


ZERO, ONE, TWO, W = E(), E(Q(1)), E(Q(2)), E(Q(0), Q(1))


def matrix_rank(rows: list[list[E]]) -> int:
    """Gaussian elimination over Q(w), independently checking the linear system."""
    a = [row[:] for row in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col] != ZERO), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][col]
        a[rank] = [v / scale for v in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col] != ZERO:
                scale = a[i][col]
                a[i] = [v - scale * p for v, p in zip(a[i], a[rank])]
        rank += 1
    return rank


def check_face(delta: Q, rotation: int, reflection: bool) -> dict:
    center = E(Q(7, 3), Q(-2, 5))
    roots = [ONE]
    for _ in range(5):
        roots.append(roots[-1] * W)
    roots = roots[rotation:] + roots[:rotation]
    if reflection:
        roots = [v.conjugate() for v in roots]
    vertices = [center + E(delta) * v for v in roots]
    mid = [(vertices[j] + vertices[(j + 1) % 6]) / TWO for j in range(6)]
    values = [E(delta) / (vertices[(j + 1) % 6] - vertices[j]) for j in range(6)]
    # The third edge at each face vertex goes radially outward; its value is zero.
    radial_mid = [center + E(Q(3, 2)) * (v - center) for v in vertices]
    assert all(p not in mid for p in radial_mid)
    rows = [[ZERO for _ in range(6)] for _ in range(6)]
    residuals = []
    for j, vertex in enumerate(vertices):
        rows[j][(j - 1) % 6] = mid[(j - 1) % 6] - vertex
        rows[j][j] = mid[j] - vertex
        residuals.append(sum((c * h for c, h in zip(rows[j], values)), ZERO))
    assert residuals == [ZERO] * 6
    assert all(h.norm2() == 1 for h in values)
    assert all((values[(j + 1) % 6] - values[j]).norm2() == 1 for j in range(6))
    assert all((mid[(j + 1) % 6] - mid[j]).norm2() == Q(3, 4) * delta * delta
               for j in range(6))
    rank = matrix_rank(rows)
    assert rank == 5
    broken = values[:]
    broken[0] = broken[0] + ONE
    failed = sum(sum((c * h for c, h in zip(row, broken)), ZERO) != ZERO for row in rows)
    assert failed == 2
    return {"delta": str(delta), "rotation": rotation, "reflection": reflection,
            "vertex_equations_zero": 6, "cycle_matrix_rank": rank,
            "cycle_nullity": 6 - rank, "squared_amplitude": "1",
            "squared_adjacent_jump": "1",
            "squared_midpoint_distance": str(Q(3, 4) * delta * delta),
            "boundary_values": "0", "negative_control_nonzero_equations": failed}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--gate", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    gate = json.loads(args.gate.read_text(encoding="utf-8"))
    assert gate["worker"] == "w397" and gate["max_cases"] == 96
    assert gate["mode"] == "single-process exact arithmetic; no network; no model loads"
    assert gate["consumed"] is False
    gate["consumed"] = True
    args.gate.write_text(json.dumps(gate, indent=2) + "\n", encoding="utf-8")
    assert W * W == W - ONE and (W * W * W * W * W * W) == ONE
    cases = [check_face(Q(1, 2 ** k), r, reflected)
             for k in [0, 2, 4, 8, 16, 24, 32, 40]
             for r in range(6) for reflected in [False, True]]
    elapsed = time.perf_counter() - started
    assert elapsed < gate["max_wall_seconds"]
    result = {"worker": "w397", "claim_id": "w397.P0003.001",
              "arithmetic": "exact rational field Q(exp(i*pi/3)); no floating-point residuals",
              "cases": len(cases), "zero_vertex_equations": 6 * len(cases),
              "negative_controls_detected": len(cases), "all_passed": True,
              "elapsed_seconds": elapsed, "before": {"zero_boundary_solution": "zero field",
              "nonzero_modes_recorded": 0}, "after": {"nonzero_modes_recorded": 1,
              "bounded_amplitude": 1, "adjacent_jump": 1,
              "smallest_mesh": "1/1099511627776", "boundary_change": 0},
              "limits": "Finite algebra checks support the written proof; not a formal theorem receipt, independent review, actual SAW estimate, or deployed brain improvement.",
              "details": cases}
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "details"}, indent=2))


if __name__ == "__main__":
    main()
