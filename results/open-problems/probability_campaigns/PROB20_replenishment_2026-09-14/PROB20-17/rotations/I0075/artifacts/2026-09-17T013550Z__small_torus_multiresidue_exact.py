#!/usr/bin/env python3
"""I0075 finite obstruction checker.

Scope proved by this script, together with the elementary reduction stated in the
run report: among n x n periodic, edge-disjoint center-star square-replacement
patterns with n <= 7 and selected-square density > 1/8, every pattern violates
the Aldous--Lando source stretch bound.  The script enumerates every pattern
that survives the necessary toroidal L1-separation >= 3 condition.  A floating
Dijkstra is used only to *select* a candidate violating city pair; every
accepted violation is then independently verified by exact arithmetic in
Z[sqrt(2)].  If the heuristic ever selects a false witness the script aborts.
"""

from functools import total_ordering
from heapq import heappop, heappush
import math

SQRT2 = math.sqrt(2.0)
RDISP = 5
BOX = 8


def sign_qsqrt2(p, q):
    """Sign of p + q sqrt(2), p,q integers."""
    if p == 0:
        return (q > 0) - (q < 0)
    if q == 0:
        return (p > 0) - (p < 0)
    if p > 0 and q > 0:
        return 1
    if p < 0 and q < 0:
        return -1
    if p > 0 and q < 0:
        c = p * p - 2 * q * q
        return (c > 0) - (c < 0)
    c = 2 * q * q - p * p
    return (c > 0) - (c < 0)


def alg_lt(x, y):
    return sign_qsqrt2(x[0] - y[0], x[1] - y[1]) < 0


def route_leq_source(a, b, r2):
    """Exact test (a+b sqrt(2))^2 <= 2*r2 for a,b >= 0."""
    c = 2 * r2 - (a * a + 2 * b * b)
    return c >= 0 and c * c >= 8 * a * a * b * b


@total_ordering
class QItem:
    __slots__ = ("a", "b", "x", "y")

    def __init__(self, a, b, x, y):
        self.a, self.b, self.x, self.y = a, b, x, y

    def __lt__(self, other):
        s = sign_qsqrt2(self.a - other.a, self.b - other.b)
        return s < 0 if s else (self.x, self.y) < (other.x, other.y)

    def __eq__(self, other):
        return (self.a, self.b, self.x, self.y) == (
            other.a,
            other.b,
            other.x,
            other.y,
        )


def shift(mask, n, amount):
    amount %= n
    if amount == 0:
        return mask
    return ((mask << amount) | (mask >> (n - amount))) & ((1 << n) - 1)


def row_masks_sep3(n):
    """Row masks whose selected cells have cyclic horizontal distance >= 3."""
    out = []
    for mask in range(1 << n):
        if mask & shift(mask, n, 1):
            continue
        if mask & shift(mask, n, 2):
            continue
        out.append(mask)
    return out


def comp_adj(r, s, n):
    """Rows one apart: no selected pair at horizontal distance 0 or 1."""
    return (r & (s | shift(s, n, 1) | shift(s, n, -1))) == 0


def openpack_patterns(n, min_count):
    """Enumerate all n x n torus patterns with toroidal L1 distance >= 3."""
    rows = row_masks_sep3(n)
    seq = [0] * n

    def rec(y, total):
        if y == n:
            if not comp_adj(seq[-1], seq[0], n):
                return
            if n >= 3 and ((seq[-2] & seq[0]) or (seq[-1] & seq[1])):
                return
            if total >= min_count:
                mask = 0
                for yy, r in enumerate(seq):
                    mask |= r << (yy * n)
                yield mask
            return

        for r in rows:
            if y >= 1 and not comp_adj(seq[y - 1], r, n):
                continue
            if y >= 2 and (seq[y - 2] & r):
                continue
            seq[y] = r
            yield from rec(y + 1, total + r.bit_count())

    yield from rec(0, 0)


DISPS = sorted(
    (dx * dx + dy * dy, dx, dy)
    for dx in range(-RDISP, RDISP + 1)
    for dy in range(-RDISP, RDISP + 1)
    if (dx or dy) and dx * dx + dy * dy <= RDISP * RDISP
)


def selectors(mask, n):
    def selected(a, b):
        return bool((mask >> ((b % n) * n + (a % n))) & 1)

    def deleted(x, y, nx, ny):
        assert abs(x - nx) + abs(y - ny) == 1
        if y == ny:
            a, b = min(x, nx), y
            return selected(a, b) or selected(a, b - 1)
        a, b = x, min(y, ny)
        return selected(a, b) or selected(a - 1, b)

    return selected, deleted


def heuristic_violation(mask, n):
    """Fast witness selector only; never used as the final certificate."""
    selected, deleted = selectors(mask, n)
    maxneed = SQRT2 * RDISP + 1e-8

    for sy in range(n):
        for sx in range(n):
            xmin, xmax = sx - BOX, sx + BOX
            ymin, ymax = sy - BOX, sy + BOX
            dist = {(sx, sy): 0.0}
            pq = [(0.0, sx, sy)]

            while pq:
                d, x, y = heappop(pq)
                if d != dist.get((x, y)):
                    continue
                if d > maxneed:
                    break

                for ux, uy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + ux, y + uy
                    if (
                        xmin <= nx <= xmax
                        and ymin <= ny <= ymax
                        and not deleted(x, y, nx, ny)
                    ):
                        nd = d + 1.0
                        if nd < dist.get((nx, ny), 1e99) - 1e-12:
                            dist[(nx, ny)] = nd
                            heappush(pq, (nd, nx, ny))

                # Passing through one selected-square centre between any two
                # of its city corners costs exactly sqrt(2).
                for a in (x, x - 1):
                    for b in (y, y - 1):
                        if selected(a, b):
                            for nx, ny in (
                                (a, b),
                                (a + 1, b),
                                (a, b + 1),
                                (a + 1, b + 1),
                            ):
                                if (
                                    (nx, ny) != (x, y)
                                    and xmin <= nx <= xmax
                                    and ymin <= ny <= ymax
                                ):
                                    nd = d + SQRT2
                                    if nd < dist.get((nx, ny), 1e99) - 1e-12:
                                        dist[(nx, ny)] = nd
                                        heappush(pq, (nd, nx, ny))

            for r2, dx, dy in DISPS:
                if dist[(sx + dx, sy + dy)] > math.sqrt(2 * r2) + 1e-9:
                    return sx, sy, dx, dy, r2

    return None


def exact_violation_cert(mask, n, witness):
    """Prove no route to the selected target meets the source stretch budget.

    Every explored distance is an exact pair (a,b) representing a+b*sqrt(2).
    We explore precisely the paths whose current length is <= sqrt(2)*|d|.
    Since |d| <= 5, the threshold is <= 5*sqrt(2) < 8.  A qualifying path
    cannot leave the city box of radius 8: reaching a city outside it already
    has Euclidean distance at least 9 from the source, and reaching an exterior
    star centre is even farther than the threshold.  Thus the bounded exact
    search is also a global search for every potentially qualifying route.
    """
    sx, sy, dx, dy, r2 = witness
    selected, deleted = selectors(mask, n)
    xmin, xmax = sx - BOX, sx + BOX
    ymin, ymax = sy - BOX, sy + BOX
    src = (sx, sy)
    target = (sx + dx, sy + dy)
    dist = {src: (0, 0)}
    pq = [QItem(0, 0, sx, sy)]

    while pq:
        h = heappop(pq)
        v = (h.x, h.y)
        if dist.get(v) != (h.a, h.b):
            continue

        # Heap order is exact in Q(sqrt(2)).  Once the least label exceeds
        # the allowed threshold, no later path can qualify.
        if not route_leq_source(h.a, h.b, r2):
            break
        if v == target:
            return False

        x, y = v
        for ux, uy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + ux, y + uy
            if (
                xmin <= nx <= xmax
                and ymin <= ny <= ymax
                and not deleted(x, y, nx, ny)
            ):
                nd = (h.a + 1, h.b)
                if (nx, ny) not in dist or alg_lt(nd, dist[(nx, ny)]):
                    dist[(nx, ny)] = nd
                    heappush(pq, QItem(nd[0], nd[1], nx, ny))

        for a in (x, x - 1):
            for b in (y, y - 1):
                if selected(a, b):
                    for nx, ny in (
                        (a, b),
                        (a + 1, b),
                        (a, b + 1),
                        (a + 1, b + 1),
                    ):
                        if (
                            (nx, ny) != (x, y)
                            and xmin <= nx <= xmax
                            and ymin <= ny <= ymax
                        ):
                            nd = (h.a, h.b + 1)
                            if (nx, ny) not in dist or alg_lt(nd, dist[(nx, ny)]):
                                dist[(nx, ny)] = nd
                                heappush(pq, QItem(nd[0], nd[1], nx, ny))

    return True


def main():
    summaries = []
    total_patterns = 0

    for n in range(3, 8):
        # Density strictly larger than 1/8 means count > n^2/8.
        min_count = n * n // 8 + 1
        count = 0
        exact_bad = 0
        weights = set()

        for mask in openpack_patterns(n, min_count):
            count += 1
            total_patterns += 1
            weights.add(mask.bit_count())
            witness = heuristic_violation(mask, n)
            assert witness is not None, ("LOCAL_SURVIVOR", n, mask)
            assert exact_violation_cert(mask, n, witness), (
                "EXACT_WITNESS_FAILED",
                n,
                mask,
                witness,
            )
            exact_bad += 1

        assert exact_bad == count
        summaries.append((n, min_count, count, exact_bad, sorted(weights)))

    assert summaries == [
        (3, 2, 0, 0, []),
        (4, 3, 0, 0, []),
        (5, 4, 60, 60, [4, 5]),
        (6, 5, 1068, 1068, [5, 6]),
        (7, 7, 11984, 11984, [7, 8]),
    ]
    assert total_patterns == 13112

    print("I0075_SMALL_TORUS_MULTIRESIDUE_EXACT")
    print("class: n x n periodic edge-disjoint centre-star patterns, n=3..7")
    print("density target: selected-square density > 1/8")
    print("necessary filter: toroidal L1 separation >= 3 (proved in run report)")
    print("finite witness radius: Euclidean city displacement <= 5")
    print("exact verification ring: Z[sqrt(2)]")
    print("float use: witness selection only; every counted pattern rechecked exactly")
    for row in summaries:
        print(
            "n=%d min_selected=%d enumerated_after_filter=%d exact_source_violations=%d weights=%s"
            % row
        )
    print("total_enumerated_after_filter=%d" % total_patterns)
    print("local_survivors=0")
    print("ALL_ASSERTIONS_PASSED")


if __name__ == "__main__":
    main()
