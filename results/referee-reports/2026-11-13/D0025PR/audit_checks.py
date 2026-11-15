"""Finite, deterministic checks for the referee report; not a proof of a limit theorem."""

from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib
import math
import os


def all_paths(k, end):
    @lru_cache(None)
    def paths(i, j):
        if j < 0 or j + k * i < 0:
            return ()
        if (i, j) == (0, 0):
            return (((0, 0),),)
        return tuple(
            path + ((i, j),)
            for prev in ((i, j - 1), (i - 1, j), (i + 1, j - k))
            for path in paths(*prev)
        )

    return paths(*end)


def diamond(k, m):
    @lru_cache(None)
    def vertices(i, j):
        if j < 0 or j + k * i < 0:
            return frozenset()
        if (i, j) == (0, 0):
            return frozenset({(0, 0)})
        result = set()
        for prev in ((i, j - 1), (i - 1, j), (i + 1, j - k)):
            before = vertices(*prev)
            if before:
                result.update(before)
                result.add((i, j))
        return frozenset(result)

    return vertices(0, m)


def main():
    out = [f"Inherited nice level: {os.getpriority(os.PRIO_PROCESS, 0)}"]
    count = rays = 0
    for k in (1, 2, 3, 4, 8):
        for j in range(6):
            for i in range(-3, 4):
                if j + k * i < 0:
                    continue
                paths = all_paths(k, (i, j))
                assert paths
                rays += 1
                mandatory = set(range(1, i + 1) if i > 0 else range(i, 0))
                for path in paths:
                    count += 1
                    assert len(set(path)) == len(path)
                    assert len(path) - 1 <= abs(i) + 2 * j
                    assert mandatory <= {a for a, b in path[1:]}
                    reflected = tuple((-a, b + k * a) for a, b in path)
                    assert all(b >= 0 and b + k * a >= 0 for a, b in reflected)
                    assert all(
                        (v[0] - u[0], v[1] - u[1]) in {(0, 1), (1, 0), (-1, k)}
                        for u, v in zip(reflected, reflected[1:])
                    )
    out.append(f"Enumerated {count} paths to {rays} endpoints, K=1,2,3,4,8: no repeated vertices; length, mandatory columns and reflection all pass.")

    checks = 0
    for k in (1, 2, 3, 4, 8, 100):
        for m in range(1, 13):
            lower = diamond(k, m)
            upper = {(i, j + m) for i, j in lower}
            assert lower & upper == {(0, m)}
            assert (lower - {(0, 0)}).isdisjoint(upper - {(0, m)})
            assert all(abs(i) <= m // k for i, j in lower)
            for a in (-17, -1, 0, 1, 17):
                b, d = k * max(-a, 0), k * max(a, 0)
                assert b + d == k * abs(a)
                shifted = {(i + a, j + b) for i, j in lower}
                assert all(j >= 0 and j + k * i >= 0 for i, j in shifted)
            checks += 1
    out.append(f"{checks} diamonds, K through 100, m=1,...,12: adjacent weighted sets disjoint; strip width and both-sign connector heights pass.")

    checks = 0
    for r in (F(1, 100), F(1, 5), F(4, 5)):
        for a in (r, (r + 1) / 2, F(1)):
            for s in (F(0), F(1, 7), F(2), F(20)):
                lhs = a / (a + s) * (r / a + (1 - r / a) * r / (r + s))
                assert lhs == r / (r + s)
                assert (1 - r / a) / r == 1 / r - 1 / a >= 0
                checks += 1
    out.append(f"{checks} exact-rational Laplace identities, including a=r and s=0: pass.")

    laws = 0
    for r in (F(1, 1000), F(1, 5), F(999, 1000)):
        for s in ((r + 1) / 2, F(1)):
            for p in (F(1, 1000), F(1, 4), F(999, 1000)):
                mean_inv = p / r + (1 - p) / s
                mu = 1 / r - mean_inv
                coefficient = mu * r
                assert coefficient == (1 - p) * (1 - r / s)
                assert 0 < coefficient < 1
                k1_width = coefficient / 4
                assert k1_width == mu * r / 4
                assert F(0) < F(1, 2) - k1_width <= F(1, 2) + k1_width < 1
                for k in (2, 3, 100, 10000):
                    assert coefficient < 1 <= F(k, 2)
                laws += 1
    out.append(f"{laws} binary laws, including rare slow/fast sites and r near 0 or 1: positive width, corollary, K=1 normalization and [0,K] containment pass.")

    r, p = F(1, 5), F(1, 4)
    mu = 1 / r - (p / r + 1 - p)
    out.append(f"Exact example Q=(1/4) delta_(1/5)+(3/4) delta_1: mu={mu}; K=1 current={r/4}, guaranteed interval=[{F(1,2)-mu*r/4},{F(1,2)+mu*r/4}].")
    for r in (0.001, 0.2, 0.999):
        coefficient = 1 + r * math.log(r) / (1 - r)
        assert 0 < coefficient < 1
    out.append("Atom-free uniform[r,1]: mu*r=1+r*log(r)/(1-r), between 0 and 1 for the tested r. Existence of every fixed slow block also follows directly from its positive probability.")

    for path in (Path("paper/main.tex"), Path("paper/main.pdf")):
        out.append(f"SHA256 {path}: {hashlib.sha256(path.read_bytes()).hexdigest()}")
    result = "\n".join(out) + "\n"
    Path("AUDIT_CHECKS.txt").write_text(result)
    print(result, end="")


if __name__ == "__main__":
    main()
