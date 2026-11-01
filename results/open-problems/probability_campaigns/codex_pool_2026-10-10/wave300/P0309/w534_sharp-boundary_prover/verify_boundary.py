"""Small independent scalar checks; no GPU, models, services, or store writes.

Run: python -B -X utf8 verify_boundary.py
Exact rational Hessian sums use outward-rounded Decimal arithmetic and an
analytic tail bound. A separate Gaussian integral checks the normalization.
The mathematical proofs are in ATTEMPT.md, not supplied by this program.
"""
import json
import math
import time
from datetime import datetime, timezone
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATE = Path("~/.claude/compute/compute_state.json")
DOWN = Context(prec=40, rounding=ROUND_FLOOR)
UP = Context(prec=40, rounding=ROUND_CEILING)
START_CPU = time.process_time()
START_WALL = time.monotonic()
ROWS = []
N = 8
LS = (4, 8, 16, 32)


def save(row):
    row = {"utc": datetime.now(timezone.utc).isoformat(), **row}
    with (ROOT / "verification.jsonl").open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    ROWS.append(row)


def gate(unit):
    state = json.loads(STATE.read_text(encoding="utf-8-sig"))
    age = time.time() - STATE.stat().st_mtime
    selected = {k: state.get(k) for k in (
        "ts", "status", "mode", "cpu_pct", "mem_avail_mb", "commit_eff_avail_mb", "hung_windows"
    )}
    allowed = (
        0 <= age <= 120
        and state.get("status") in ("ok", "warn", "warning")
        and state.get("mode") in ("throttle", "owner_present_polite", "owner_away_open", "open")
        and not state.get("hung_windows")
        and time.process_time() - START_CPU < 4
        and time.monotonic() - START_WALL < 45
    )
    save({"kind": "fresh_compute_gate", "unit": unit, "allowed": allowed,
          "snapshot_age_seconds": age, "selected_state": selected,
          "work_cap": "one process; N=8; <=728 octant vectors per exponent; <=1024 log-quadrature panels; total CPU cap 4s"})
    if not allowed:
        raise RuntimeError("Fresh compute gate did not allow this small CPU unit; no heavy fallback.")


def rational_interval(numerator, denominator):
    return (DOWN.divide(Decimal(numerator), Decimal(denominator)),
            UP.divide(Decimal(numerator), Decimal(denominator)))


def add_interval(acc, term):
    return DOWN.add(acc[0], term[0]), UP.add(acc[1], term[1])


def widen(acc, bound):
    _, upper = rational_interval(bound.numerator, bound.denominator)
    return DOWN.subtract(acc[0], upper), UP.add(acc[1], upper)


def odd_count(low, high):
    return 0 if high < low else (high + 1) // 2 - low // 2


def hessian_enclosures(s):
    gate(f"rational-hessian-s{s}")
    zero = (Decimal(0), Decimal(0))
    period = zero
    finite = {ell: zero for ell in LS}
    counts = {ell: (2 * ell + 1) ** 2 * odd_count(-ell, ell) for ell in LS}
    volumes = {ell: (2 * ell + 1) ** 3 for ell in LS}
    for x in range(N + 1):
        for y in range(N + 1):
            for z in range(N + 1):
                q = x*x + y*y + z*z
                if not q:
                    continue
                multiplicity = (2 if x else 1) * (2 if y else 1) * (2 if z else 1)
                numerator = s * ((s + 2) * x*x - q) * multiplicity
                denominator = q ** (s // 2 + 2)
                if z % 2:
                    period = add_interval(period, rational_interval(numerator, 2 * denominator))
                for ell in LS:
                    width = 2 * ell + 1
                    overlap = 0 if z % 2 else (
                        max(0, width - x) * max(0, width - y)
                        * odd_count(-ell, ell - z)
                    )
                    difference_count = 2 * counts[ell] - 2 * overlap
                    finite[ell] = add_interval(finite[ell], rational_interval(
                        numerator * difference_count, 2 * denominator * volumes[ell]
                    ))
    # max-norm shell has 24*k^2+2 sites; |h_s(r)|<=s*(s+1)*|r|^(-s-2).
    shell_integral = Fraction(24, (s - 1) * N ** (s - 1)) + Fraction(2, (s + 1) * N ** (s + 1))
    period_tail = Fraction(s * (s + 1), 2) * shell_integral
    finite_tail = s * (s + 1) * shell_integral
    period = widen(period, period_tail)
    finite = {ell: widen(bounds, finite_tail) for ell, bounds in finite.items()}
    assert period[1] < 0, (s, period)
    assert finite[32][1] < 0, (s, finite[32])
    save({"kind": "rational_hessian_enclosure", "s": s, "max_norm_cutoff": N,
          "periodic_curvature": [str(v) for v in period],
          "periodic_tail_bound": str(period_tail),
          "finite_K_L_per_volume": {str(ell): [str(v) for v in bounds] for ell, bounds in finite.items()},
          "finite_tail_bound": str(finite_tail), "passed": True,
          "trusted_arithmetic": "stdlib Decimal floor/ceiling rounding of integer rational terms; analytic shell tail; no formal theorem receipt"})
    return period


def energy_enclosure(s):
    gate(f"rational-energy-s{s}")
    acc = (Decimal(0), Decimal(0))
    p = s // 2
    for x in range(-N, N + 1):
        for y in range(N + 1):
            for z in range(1, N + 1, 2):
                q = x*x + y*y + z*z
                shifted_q = (4*x + 1) ** 2 + 16 * (y*y + z*z)
                multiplicity = (2 if y else 1) * 2
                numerator = multiplicity * (16 ** p * q ** p - shifted_q ** p)
                denominator = 2 * shifted_q ** p * q ** p
                acc = add_interval(acc, rational_interval(numerator, denominator))
    # |a|=1/4; mean-value bound, then integrate the max-norm shells.
    factor = Fraction(4 * N, 4 * N - 1) ** (s + 1)
    tail = Fraction(s, 8) * factor * (
        Fraction(24, (s - 2) * N ** (s - 2)) + Fraction(2, s * N ** s)
    )
    acc = widen(acc, tail)
    assert acc[1] < 0, (s, acc)
    save({"kind": "rational_energy_difference_enclosure", "s": s, "a": "1/4",
          "max_norm_cutoff": N, "bounds": [str(v) for v in acc],
          "tail_bound": str(tail), "passed": True})
    return acc


def theta_zero(t):
    if t < 1:
        return math.sqrt(math.pi/t) * (1 + 2 * sum(
            math.exp(-math.pi**2*k*k/t) for k in range(1, 4)
        ))
    cutoff = max(1, math.ceil(math.sqrt(42/t)))
    return 1 + 2 * sum(math.exp(-t*m*m) for m in range(1, cutoff + 1))


def odd_theta(t):
    cutoff = max(1, math.ceil(math.sqrt(42/t)))
    return 2 * sum(math.exp(-t*n*n) for n in range(1, cutoff + 1, 2))


def theta_difference(t, a):
    if a % 1 == 0:
        return 0.0
    if t < 3:
        return -4 * math.sqrt(math.pi/t) * sum(
            math.exp(-math.pi**2*k*k/t) * math.sin(math.pi*k*a)**2
            for k in range(1, 5)
        )
    cutoff = max(2, math.ceil(math.sqrt(42/t)) + 1)
    return sum(math.exp(-t*(m+a)**2) - math.exp(-t*m*m)
               for m in range(-cutoff, cutoff + 1))


def theta_curvature(t):
    if t < 3:
        return -8 * math.pi**2 * math.sqrt(math.pi/t) * sum(
            k*k*math.exp(-math.pi**2*k*k/t) for k in range(1, 5)
        )
    cutoff = max(2, math.ceil(math.sqrt(42/t)) + 1)
    return -2*t + 2 * sum((4*t*t*m*m-2*t)*math.exp(-t*m*m)
                         for m in range(1, cutoff + 1))


def heat_integral(s, panels, curvature=False, a=0.25):
    lo, hi = math.log(0.04), math.log(90)
    step = (hi-lo)/panels
    total = 0.0
    for i in range(panels + 1):
        t = math.exp(lo + i*step)
        delta = theta_curvature(t) if curvature else theta_difference(t, a)
        value = t**(s/2) * theta_zero(t) * odd_theta(t) * delta
        weight = 1 if i in (0, panels) else (4 if i % 2 else 2)
        total += weight * value
    return total * step / (6 * math.gamma(s/2))


def main():
    hessians = {s: hessian_enclosures(s) for s in (4, 6, 12)}
    energies = {s: energy_enclosure(s) for s in (6, 12)}
    gate("independent-heat-quadrature")
    for s in (0.5, 1, 3, 4, 6, 12):
        coarse = heat_integral(s, 512)
        fine = heat_integral(s, 1024)
        assert fine < 0
        assert abs(coarse-fine) < 1e-8
        if s in energies:
            lower, upper = energies[s]
            assert float(lower) < fine < float(upper)
        curvature = None
        if s in hessians:
            curvature = heat_integral(s, 1024, curvature=True)
            lower, upper = hessians[s]
            assert float(lower) < curvature < float(upper)
        save({"kind": "independent_heat_quadrature", "s": s, "a": 0.25,
              "D_s_a": fine, "refinement_difference": abs(coarse-fine),
              "curvature_at_zero": curvature, "passed": True,
              "scope": "numerical normalization/sign check, not mathematical proof"})
    for a in (0.0, 1.0, -1.0):
        assert theta_difference(1, a) == 0
    save({"kind": "equality_controls", "integral_a": [0, 1, -1], "passed": True})


if __name__ == "__main__":
    exit_code = 0
    try:
        main()
        outcome = "passed"
    except Exception as error:
        outcome = "incomplete"
        save({"kind": "error", "type": type(error).__name__, "message": str(error)})
        exit_code = 1
    result = {"command": "python -B -X utf8 verify_boundary.py", "outcome": outcome,
              "cpu_seconds": time.process_time()-START_CPU,
              "wall_seconds": time.monotonic()-START_WALL,
              "rows": ROWS, "independent_mathematical_review": "pending"}
    (ROOT / "VERIFICATION.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "rows"}, indent=2))
    raise SystemExit(exit_code)
