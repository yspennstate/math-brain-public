#!/usr/bin/env python3
"""Exact scalar and lattice audits of PROOF.md; standard library only.

env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
    PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py
"""
from fractions import Fraction as F
import itertools
import json
import math
import os
from pathlib import Path
import random
import resource
import sys
import time

START = time.monotonic()
ROOT = Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
PRIORITY = os.getpriority(os.PRIO_PROCESS, 0)
assert PRIORITY >= 15
for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    assert os.environ.get(name) == '1'


class Q3:
    """a+b sqrt(3), with exact arithmetic and exact sign comparisons."""
    __slots__ = ('a', 'b')

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(self, other):
        if not isinstance(other, Q3):
            other = Q3(other)
        return Q3(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Q3) else -F(other))

    def __mul__(self, other):
        if not isinstance(other, Q3):
            other = Q3(other)
        return Q3(self.a*other.a + 3*self.b*other.b,
                  self.a*other.b + self.b*other.a)

    __rmul__ = __mul__

    def sign(self):
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        comparison = (a*a > 3*b*b) - (a*a < 3*b*b)
        return comparison if a > 0 else -comparison

    def value(self):
        return float(self.a) + float(self.b)*math.sqrt(3)

    def pair(self):
        return [str(self.a), str(self.b)]


S, DELTA, G = F(101, 100), F(1, 400), F(101, 100)


def scalar_checks():
    # First route: rational bounds for each individual factor.
    lo, hi, radius_cap = F(303, 175), F(26, 15), F(7, 12)
    assert lo*lo < 3 < hi*hi
    assert S/lo == radius_cap
    density_floor = 2/(hi*S*S)
    height = 4 - 2*DELTA - 2*radius_cap
    width = 4 - 2*DELTA - G - 4*radius_cap
    lower = density_floor*height*width
    assert (density_floor, height, width) == (F(150000, 132613), F(1697, 600), F(391, 600))
    assert lower == F(3317635, 1591356) > 2
    assert lower - 2 == F(134923, 1591356)
    assert S - 2*DELTA == G - 2*DELTA == F(201, 200) > 1
    # Independent route: expand the original expression in Q(sqrt(3)),
    # then compare squares; no radius/density interval substitutions.
    radius = Q3(0, S/3)
    density = Q3(0, 2/(3*S*S))
    exact = density*(Q3(4-2*DELTA)-2*radius)*(Q3(4-2*DELTA-G)-4*radius)
    assert (exact - 2).sign() > 0
    assert (exact - lower).sign() > 0
    length = 4 - 2*DELTA
    c = length*(length-G) + F(8, 3)*S*S
    d = 2*S*(3*length-G)/3
    expanded = Q3(-2*d/(S*S), 2*c/(3*S*S))
    assert (exact - expanded).a == (exact - expanded).b == 0
    assert expanded.b > 0 and 2-expanded.a > 0
    assert 3*expanded.b**2 > (2-expanded.a)**2
    print(f'exact_rational_count_floor={lower}=2+{lower-2}; required_count>=3')
    print(f'independent_Qsqrt3_bound={exact.pair()}; decimal_for_orientation={exact.value():.12g}; exact_comparison_to_2=PASS')
    return dict(rational_lower=str(lower), excess_over_two=str(lower-2),
                exact_bound_Qsqrt3=exact.pair(), exact_bound_decimal=exact.value())


def cell_checks():
    # Independent finite check of shortest-vector list and cell vertices.
    vectors = [(m, n, m*m+m*n+n*n) for m in range(-5, 6)
               for n in range(-5, 6) if (m, n) != (0, 0)]
    shortest = {(m, n) for m, n, norm in vectors if norm == 1}
    assert shortest == {(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)}
    assert min(norm for m, n, norm in vectors if (m, n) not in shortest) == 3
    vertices = [(Q3(S/2), Q3(0, S/6)), (Q3(0), Q3(0, S/3)),
                (Q3(-S/2), Q3(0, S/6)), (Q3(-S/2), Q3(0, -S/6)),
                (Q3(0), Q3(0, -S/3)), (Q3(S/2), Q3(0, -S/6))]
    area_twice = Q3()
    for i, (x, y) in enumerate(vertices):
        square_norm = x*x+y*y
        assert square_norm.a == S*S/3 and square_norm.b == 0
        x_next, y_next = vertices[(i+1) % 6]
        area_twice += x*y_next-y*x_next
        for m, n, norm in vectors:
            vx, vy = Q3(S*(m+F(n, 2))), Q3(0, S*n/2)
            assert (Q3(S*S*norm/2) - (x*vx+y*vy)).sign() >= 0
    assert area_twice.a == 0 and area_twice.b == S*S
    print(f'cell_vertices=6; exact_shoelace_area=sqrt(3)*s^2/2; vector_checks={len(vectors)*6}; PASS')


def inside(x, low, high):
    return (x-low).sign() > 0 and (x-high).sign() < 0


def patch(phase_left, phase_right):
    # Every point required below lies in [-6,6] x [-3,7]. All phase
    # coordinates have absolute value <1. The inverse basis vectors have
    # norm 2/(s sqrt(3)), even after rotation. Thus |m|,|n|<16 suffices.
    assert (16*S)**2*3 > 4*(7*7+8*8)
    result = []
    for side, phase in ((-1, phase_left), (1, phase_right)):
        tx, ty = phase
        assert abs(tx) < 1 and abs(ty) < 1
        for m, n in itertools.product(range(-16, 17), repeat=2):
            if side == -1:
                x, y = Q3(tx+S*(m+F(n, 2))), Q3(ty, S*n/2)
            else:
                x, y = Q3(tx, S*m/2), Q3(ty+S*(F(m, 2)+n))
            if (x + G/2).sign() < 0 if side == -1 else (x-G/2).sign() > 0:
                if inside(x, -6, 6) and inside(y, -3, 7):
                    result.append((x, y, side))
    return result


def enumeration_checks():
    phases = [(F(0), F(0)), (S/3, S/5), (-S/4, S/7), (S/2, -S/3)]
    xstarts = [F(-6), F(-4), F(-5, 2), F(-2), F(-1), F(0), F(2)]
    ystarts = [F(-3), F(-7, 4), F(0), F(1, 3), F(3)]
    cases, minimum, witness = 0, 10**9, None
    for il, pl in enumerate(phases):
        for ir, pr in enumerate(phases):
            points = patch(pl, pr)
            assert len(points) < 200
            for x0, y0 in itertools.product(xstarts, ystarts):
                safe = [(x, y) for x, y, _ in points
                        if inside(x, x0+DELTA, x0+4-DELTA)
                        and inside(y, y0+DELTA, y0+4-DELTA)]
                assert len(safe) >= 3, (pl, pr, x0, y0, len(safe))
                cases += 1
                if len(safe) < minimum:
                    minimum = len(safe)
                    witness = [il, ir, str(x0), str(y0)]
    print(f'exact_phase_and_square_cases={cases}; minimum_certified_safe_sites_in_sample={minimum}; witness={witness}')
    return dict(exact_count_cases=cases, sample_minimum_safe_sites=minimum,
                sample_minimum_witness=witness)


def parameter_checks():
    # Split-width inequality, including boxes lying wholly on one side.
    split_cases = 0
    for length in [F(1, 2), F(1), F(3), F(4), F(10)]:
        for x0 in [F(-20), F(-5), -G/2, F(-1), F(0), G/2, F(10)]:
            left = max(F(0), min(x0+length, -G/2)-x0)
            right = max(F(0), x0+length-max(x0, G/2))
            radius_cap = F(7, 12)
            lhs = max(F(0), left-2*radius_cap)+max(F(0), right-2*radius_cap)
            rhs = max(F(0), length-G-4*radius_cap)
            assert left+right >= length-G and lhs >= rhs
            split_cases += 1
    # With fixed parameters the bound must fail when the box lies entirely
    # in a strip wider than itself. This detects omission of g from (5).
    wide_g, ell = F(10), F(4)
    assert max(F(0), ell-2*DELTA-wide_g-4*F(7, 12)) == 0
    # A square's nominal count cannot be used after arbitrary displacements
    # without erosion: a point near its face can move out.
    nominal = F(1, 1000)
    displacement = -F(1, 500)
    assert nominal > 0 > nominal+displacement and abs(displacement) < DELTA
    # The sufficient large-box scale is checked by exact expansion, using
    # conservative rational density and radius constants independently.
    rho_floor, rcap = F(150000, 132613), F(7, 12)
    a0, b0 = 2*DELTA+2*rcap, 2*DELTA+G+4*rcap
    scales = []
    for threshold in [F(1, 8), F(1, 2), F(1), F(11, 10)]:
        cutoff = (a0+b0)/(1-threshold/rho_floor)
        ell = math.floor(cutoff)+1
        lower = rho_floor*(ell-a0)*(ell-b0)
        assert ell > cutoff and lower > threshold*ell*ell
        scales.append(dict(threshold=str(threshold), sufficient_integer_side=ell))
    print(f'exact_split_width_cases={split_cases}; wide_strip_and_missing_erosion_negative_controls=PASS')
    print(f'conservative_large_box_examples={scales}')
    return dict(split_width_cases=split_cases, large_box_examples=scales)


def displacement_checks():
    # Supporting floating-point check of sampled simultaneous movements.
    # Exhaustive displacement validity comes from (2), not these samples.
    rng = random.Random(5080)
    sites = patch((F(0), F(0)), (S/3, S/5))
    all_min = math.inf
    for trial in range(3):
        moved = []
        for x, y, _ in sites:
            angle = rng.uniform(0, 2*math.pi)
            radius = float(DELTA)*math.sqrt(rng.random())
            moved.append((x.value()+radius*math.cos(angle), y.value()+radius*math.sin(angle)))
        minimum = min(math.hypot(x-x2, y-y2) for i, (x, y) in enumerate(moved)
                      for x2, y2 in moved[i+1:])
        assert minimum > 1
        all_min = min(all_min, minimum)
    print(f'jitter_trials=3; seed=5080; smallest_sampled_separation={all_min:.12g}; floating_point_support_only')
    return dict(jitter_trials=3, jitter_seed=5080, sampled_minimum_separation=all_min)


def main():
    print(f'nice_priority={PRIORITY}; thread_environment=1; CPU_limit_seconds=60')
    result = scalar_checks()
    cell_checks()
    result.update(enumeration_checks())
    result.update(parameter_checks())
    result.update(displacement_checks())
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_mib = rss/(1024**2 if sys.platform == 'darwin' else 1024)
    assert peak_mib < 128
    result.update(status='PASS', nice_priority=PRIORITY, elapsed_seconds=time.monotonic()-START,
                  peak_rss_mib=peak_mib)
    (ROOT/'verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(f"PASS; elapsed_seconds={result['elapsed_seconds']:.3f}; peak_rss_mib={peak_mib:.3f}")


if __name__ == '__main__':
    main()
