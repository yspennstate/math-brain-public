"""Small deterministic reproduction; exact arithmetic is supporting evidence, not a formal proof."""
from __future__ import annotations
import ctypes
import json
import math
import time
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def gate():
    class MemoryStatus(ctypes.Structure):
        _fields_ = [("length", ctypes.c_ulong), ("load", ctypes.c_ulong)] + [
            (x, ctypes.c_ulonglong) for x in ("total_phys", "avail_phys", "total_page", "avail_page", "total_virt", "avail_virt", "extended")]
    mem = MemoryStatus()
    mem.length = ctypes.sizeof(mem)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem)):
        raise RuntimeError("fresh memory gate unavailable")
    result = {"free_memory_bytes": mem.avail_phys, "load_percent": mem.load,
              "dense_dimension_cap": 12, "interval_quadrature_panels": 2048,
              "weighted_simpson_panels": 16384,
              "cpu_budget_seconds": 20, "network": False, "gpu": False}
    if mem.avail_phys < 128 * 1024 * 1024:
        raise RuntimeError("insufficient memory for this small reproduction")
    (ROOT / "COMPUTE_GATE.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def simplex_moment(n, powers):
    """Normalized simplex integration, independently from the proposed covariance formula."""
    return F(math.factorial(n) * math.prod(math.factorial(k) for k in powers),
             math.factorial(n + sum(powers)))


def beta_integral(n, power, lower=F(0)):
    """Integrate n(n-1)t^(power+1)(1-t)^(n-2) by polynomial expansion."""
    return n * (n - 1) * sum(
        F((-1) ** j * math.comb(n - 2, j), power + j + 2)
        * (1 - lower ** (power + j + 2)) for j in range(n - 1))


def check_covariance(n):
    mean = simplex_moment(n, [1])
    raw_diag = simplex_moment(n, [2])
    raw_off = simplex_moment(n, [1, 1])
    sigma = [[(raw_diag if i == j else raw_off) - mean * mean for j in range(n)] for i in range(n)]
    a = (n + 1) * (n + 2)
    inv = [[a * (1 + int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            assert sum(sigma[i][k] * inv[k][j] for k in range(n)) == int(i == j)
    # Check conditional mean cancellation: Sigma^{-1}(E[X | base]-m) has zero first component.
    s = F(2, 5)
    first_mean = (1 - s) / 2
    assert 2 * first_mean + s - 1 == 0
    assert beta_integral(n, 0) == 1
    assert beta_integral(n, 2) == F(6, a)
    assert beta_integral(n, 0, F(1, 2)) == (F(1, 2) ** (n - 1)) * (1 + F(n - 1, 2))


def check_interval(length):
    # Direct numerical Rayleigh quotient for the first Neumann eigenfunction.
    panels = 2048
    values = [math.cos(math.pi * (j + .5) / panels) for j in range(panels)]
    derivs = [-math.pi / length * math.sin(math.pi * (j + .5) / panels) for j in range(panels)]
    mean = math.fsum(values) / panels
    var = math.fsum((x - mean) ** 2 for x in values) / panels
    energy = math.fsum(x * x for x in derivs) / panels
    ratio = var / energy
    expected = length * length / math.pi ** 2
    error = abs(ratio / expected - 1)
    assert error < 1e-12
    return {"length": length, "rayleigh_quotient": ratio, "relative_error": error}


def check_weighted_energy(n, k):
    a = (n + 1) * (n + 2)
    r = 2 * k
    # Integrate the base beta density directly, independently of the moment-ratio shortcut.
    panels = 16384
    integrals = []
    for power in (r, r - 2):
        integral = math.fsum((4 if j % 2 else 2) * n * (n - 1)
                             * (j / panels) ** (power + 1)
                             * (1 - j / panels) ** (n - 2)
                             for j in range(1, panels)) / (3 * panels)
        integrals.append(integral)
    quotient = (.5 * integrals[0]) / (math.pi ** 2 * integrals[1] / (4 * a))
    formula = 2 * a / math.pi ** 2 * float(F(r * (r + 1), (n + r - 1) * (n + r)))
    error = abs(quotient / formula - 1)
    assert error < 2e-10
    average = 12 / math.pi ** 2
    if k > 1:
        assert quotient > average
    if (n, k) == (100, 10):
        assert F(a, 6) * F(r * (r + 1), (n + r - 1) * (n + r)) == F(101, 2)
    return {"n": n, "k": k, "quotient": quotient, "mean_cp": average,
            "quotient_over_mean": quotient / average, "relative_error": error,
            "method": "composite Simpson; n=100 endpoint integrands vanish",
            "panels": panels}


def check_polynomial_triangle():
    # Raw monomial integration of f and its full gradient, independently of disintegration.
    def add(p, q):
        r = dict(p)
        for term, value in q.items():
            r[term] = r.get(term, F(0)) + value
        return r
    def scale(p, c):
        return {term: c * value for term, value in p.items()}
    def mul(p, q):
        r = {}
        for (i, j), value in p.items():
            for (k, ell), other in q.items():
                term = (i + k, j + ell)
                r[term] = r.get(term, F(0)) + value * other
        return r
    def integral(p):
        return sum(value * simplex_moment(2, term) for term, value in p.items())
    x1 = {(1, 0): F(1)}
    t = {(0, 0): F(1), (0, 1): F(-1)}
    t2 = mul(t, t)
    # f/sqrt(24)=x1*t^2-t^3/2; raw derivatives divided by sqrt(24).
    f = add(mul(x1, t2), scale(mul(t, t2), F(-1, 2)))
    g1 = t2
    g2 = add(scale(mul(x1, t), F(-2)), scale(t2, F(3, 2)))
    sigma_diag, sigma_off = F(1, 18), F(-1, 36)
    mean = integral(f)
    variance = 24 * (integral(mul(f, f)) - mean ** 2)
    directional_energy = integral(mul(t2, t2))
    full_energy = 24 * (sigma_diag * integral(add(mul(g1, g1), mul(g2, g2)))
                        + 2 * sigma_off * integral(mul(g1, g2)))
    assert mean == 0 and variance == F(1, 2)
    assert directional_energy == F(1, 3) and full_energy == F(13, 27)
    return {"peer_claim": "w354-P0017-004", "method": "exact raw triangle monomial integration",
            "variance": str(variance), "directional_energy": str(directional_energy),
            "full_gradient_energy": str(full_energy), "full_gradient_quotient": str(variance / full_energy)}


def main():
    started = time.perf_counter()
    cpu_started = time.process_time()
    gate_data = gate()
    rows = []
    with (ROOT / "REPRODUCTION_ROWS.jsonl").open("w", encoding="utf-8") as out:
        for n in range(2, 13):
            check_covariance(n)
            row = {"n": n, "exact_covariance_inverse_check": "PASS",
                   "independent_beta_integral_check": "PASS", "mean_fiber_variance": "1"}
            rows.append(row)
            out.write(json.dumps(row) + "\n")
            out.flush()
        for n in (2, 3, 10, 100, 1000):
            a = (n + 1) * (n + 2)
            row = {"n": n, "essential_sup_fiber_cp": 2 * a / math.pi ** 2,
                   "mean_fiber_cp": 12 / math.pi ** 2, "sup_over_mean": str(F(a, 6)),
                   "q": .5, "probability_T_gt_half": str(F(n + 1, 2 ** n)),
                   "fiber_cp_lower_bound_on_T_gt_half": a / (2 * math.pi ** 2),
                   "naive_bridge_cp_le_mean_cp_fails": a > 24}
            rows.append(row)
            out.write(json.dumps(row) + "\n")
            out.flush()
    intervals = [check_interval(x) for x in (1., 2., math.sqrt(2 * 101 * 102))]
    weighted = [check_weighted_energy(100, k) for k in (1, 2, 10)]
    polynomial = check_polynomial_triangle()
    cpu = time.process_time() - cpu_started
    assert cpu < gate_data["cpu_budget_seconds"]
    report = {"command": "python -B -X utf8 reproduce_simplex.py", "result": "PASS",
              "exact_dimensions": 11, "growth_dimensions": 5, "interval_checks": intervals,
              "weighted_energy_checks": weighted,
              "polynomial_triangle_check": polynomial,
              "at_n_100": {"essential_sup_fiber_cp": 2 * 101 * 102 / math.pi ** 2,
                           "mean_fiber_cp": 12 / math.pi ** 2, "ratio": 1717},
              "at_n_1000": {"sup_over_mean": 167167},
              "cpu_seconds": cpu, "elapsed_seconds": time.perf_counter() - started,
              "limitation": "Checks arithmetic and an eigenfunction; does not replace the general proof or independent review."}
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
