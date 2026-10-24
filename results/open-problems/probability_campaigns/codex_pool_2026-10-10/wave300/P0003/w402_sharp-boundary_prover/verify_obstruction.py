"""Bounded exact-arithmetic reproduction; no store writes or formal-proof claim."""
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
import json
import time

START = time.monotonic()
CPU_START = time.process_time()
LIMITS = {"max_radius": 16, "max_vertices": 1800, "max_edges": 2800,
          "max_rank_vertices": 60, "max_cpu_seconds": 12, "max_wall_seconds": 120}


def gate(vertices=0, edges=0):
    if vertices > LIMITS["max_vertices"] or edges > LIMITS["max_edges"]:
        raise RuntimeError("fresh size gate exceeded")
    if time.process_time() - CPU_START > LIMITS["max_cpu_seconds"]:
        raise RuntimeError("fresh CPU gate exceeded")
    if time.monotonic() - START > LIMITS["max_wall_seconds"]:
        raise RuntimeError("fresh wall-time gate exceeded")


@dataclass(frozen=True)
class Z:
    """a + b*sqrt(-3), with rational a,b."""
    a: Q = Q(0)
    b: Q = Q(0)

    @staticmethod
    def convert(value):
        return value if isinstance(value, Z) else Z(Q(value), Q(0))

    def __add__(self, value):
        value = Z.convert(value)
        return Z(self.a + value.a, self.b + value.b)

    __radd__ = __add__

    def __neg__(self):
        return Z(-self.a, -self.b)

    def __sub__(self, value):
        return self + -Z.convert(value)

    def __mul__(self, value):
        value = Z.convert(value)
        return Z(self.a * value.a - 3 * self.b * value.b,
                 self.a * value.b + self.b * value.a)

    __rmul__ = __mul__

    def norm2(self):
        return self.a * self.a + 3 * self.b * self.b

    def __truediv__(self, value):
        value = Z.convert(value)
        if not value.norm2():
            raise ZeroDivisionError
        return (self * Z(value.a, -value.b)) * (1 / value.norm2())


ZERO, ONE = Z(), Z(Q(1))
HEX = [(2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1), (1, -1)]


def edge(u, v):
    return tuple(sorted((u, v)))


def neighbors(v):
    x, y = v
    ds = [(2, 0), (-1, 1), (-1, -1)] if x % 3 == 2 else [(-2, 0), (1, 1), (1, -1)]
    return [(x + dx, y + dy) for dx, dy in ds]


def coord(v, delta):
    return Z(Q(v[0]) * delta / 2, Q(v[1]) * delta / 2)


def patch(radius):
    assert 0 <= radius <= LIMITS["max_radius"]
    faces = [(q, r) for q in range(-radius, radius + 1)
             for r in range(-radius, radius + 1) if abs(q + r) <= radius]
    vertices = {(3 * q + a, q + 2 * r + b) for q, r in faces for a, b in HEX}
    edges = {edge(u, v) for u in vertices for v in neighbors(u) if v in vertices}
    boundary = {edge(u, v) for u in vertices for v in neighbors(u) if v not in vertices}
    gate(len(vertices), len(edges))
    assert len(vertices) == 6 * (radius + 1) ** 2
    assert len(edges) == 9 * radius ** 2 + 15 * radius + 6
    return sorted(vertices), sorted(edges), boundary, len(faces)


def midpoint(e, delta):
    return (coord(e[0], delta) + coord(e[1], delta)) * Q(1, 2)


def loop_mode(delta):
    return {edge(HEX[j], HEX[(j + 1) % 6]):
            Z(delta) / (coord(HEX[(j + 1) % 6], delta) - coord(HEX[j], delta))
            for j in range(6)}


def residuals(vertices, fields, delta):
    return {v: sum(((midpoint(edge(v, w), delta) - coord(v, delta)) *
                    fields[edge(v, w)] for w in neighbors(v)), ZERO) for v in vertices}


def exact_rank(vertices, edges):
    assert len(vertices) <= LIMITS["max_rank_vertices"]
    index = {v: i for i, v in enumerate(vertices)}
    rows = [[Q(0) for _ in edges] for _ in vertices]
    for j, (u, v) in enumerate(edges):
        rows[index[u]][j] = Q(1)
        rows[index[v]][j] = Q(-1)
    rank = 0
    for j in range(len(edges)):
        p = next((i for i in range(rank, len(rows)) if rows[i][j]), None)
        if p is None:
            continue
        rows[rank], rows[p] = rows[p], rows[rank]
        d = rows[rank][j]
        rows[rank] = [x / d for x in rows[rank]]
        for i in range(rank + 1, len(rows)):
            if rows[i][j]:
                scale = rows[i][j]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[rank])]
        rank += 1
        gate()
    return rank


def run():
    rank_checks = []
    for radius in [0, 1, 2]:
        vertices, edges, _, faces = patch(radius)
        rank = exact_rank(vertices, edges)
        assert rank == len(vertices) - 1
        assert len(edges) - rank == faces
        rank_checks.append({"radius": radius, "vertices": len(vertices), "edges": len(edges),
                            "rank_over_Q": rank, "kernel_dimension": len(edges) - rank,
                            "bounded_faces": faces})

    meshes = []
    for radius in [1, 2, 4, 8, 16]:
        vertices, edges, boundary, faces = patch(radius)
        delta = Q(1, radius + 1)
        mode = loop_mode(delta)
        assert len(mode) == 6 and all(x.norm2() == 1 for x in mode.values())
        fields = {e: ONE + mode.get(e, ZERO) for e in set(edges) | boundary}
        assert all(fields[e] == ONE for e in boundary)
        residual = residuals(vertices, fields, delta)
        assert all(x == ZERO for x in residual.values())
        assert max(x.norm2() for x in fields.values()) == 4
        p_edge = edge(HEX[0], HEX[1])
        q_edge = edge(HEX[0], (4, 0))
        jump2 = (fields[p_edge] - fields[q_edge]).norm2()
        distance2 = (midpoint(p_edge, delta) - midpoint(q_edge, delta)).norm2()
        assert jump2 == 1 and distance2 == 3 * delta * delta / 4
        circulation = sum(((coord(HEX[(j + 1) % 6], delta) - coord(HEX[j], delta)) *
                           mode[edge(HEX[j], HEX[(j + 1) % 6])] for j in range(6)), ZERO)
        assert circulation == Z(6 * delta)
        broken = dict(fields)
        broken[p_edge] = ONE - mode[p_edge]
        bad_vertices = sum(x != ZERO for x in residuals(vertices, broken, delta).values())
        assert bad_vertices == 2
        constant = {e: ONE for e in set(edges) | boundary}
        assert all(x == ZERO for x in residuals(vertices, constant, delta).values())
        assert (constant[p_edge] - constant[q_edge]).norm2() == 0
        meshes.append({"radius": radius, "delta": str(delta), "vertices": len(vertices),
                       "interior_edges": len(edges), "boundary_mid_edges": len(boundary),
                       "local_equations_failed": 0, "boundary_mismatches": 0,
                       "sup_norm_squared": 4, "jump_squared": str(jump2),
                       "separation_squared": str(distance2), "loop_circulation": str(6 * delta),
                       "circulation_divided_by_delta": 6, "broken_sign_failed_vertices": bad_vertices})
        gate()

    return {"status": "PASS", "arithmetic": "exact Q(sqrt(-3)); rational incidence ranks",
            "formal_proof": False, "independent_math_audit": False, "fresh_compute_gate": LIMITS,
            "rank_checks": rank_checks, "meshes": meshes,
            "naive_identity_boundary_bound_accepts_counterexamples": len(meshes),
            "oscillation_witness_detects_counterexamples": len(meshes),
            "constant_control_false_flags": 0,
            "cpu_seconds": round(time.process_time() - CPU_START, 6),
            "wall_seconds": round(time.monotonic() - START, 6)}


if __name__ == "__main__":
    result = run()
    destination = Path(__file__).with_name("MEASUREMENTS.json")
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
