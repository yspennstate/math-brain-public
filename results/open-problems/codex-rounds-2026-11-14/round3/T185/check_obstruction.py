"""Exact checks; standard library only, no simulation or numerical workers."""

import json
import math
import os
import resource
import time
from fractions import Fraction as Q
from pathlib import Path


def cap_limits(kind, requested):
    soft, hard = resource.getrlimit(kind)
    bounds = [requested]
    bounds.extend(x for x in (soft, hard) if x != resource.RLIM_INFINITY)
    resource.setrlimit(kind, (min(bounds), min(bounds)))


cap_limits(resource.RLIMIT_CPU, 60)
try:
    cap_limits(resource.RLIMIT_DATA, 64 * 1024**2)
    DATA_LIMIT_NOTE = "64 MiB cap applied"
except (ValueError, OSError) as exc:
    DATA_LIMIT_NOTE = f"data cap unavailable: {exc}"
os.environ["OMP_NUM_THREADS"] = "1"
RHO = (Q(1, 5), Q(1, 2), Q(1, 2))


def add(p, q, scale=Q(1)):
    out = dict(p)
    for exponent, coefficient in q.items():
        out[exponent] = out.get(exponent, Q(0)) + scale * coefficient
    return {e: c for e, c in out.items() if c}


def shift(p, exponent, coefficient=Q(1)):
    return {e + exponent: c * coefficient for e, c in p.items()}


def derivative(p, i):
    out = {}
    for powers, c in p.items():
        if powers[i]:
            reduced = list(powers)
            reduced[i] -= 1
            out[tuple(reduced)] = c * powers[i]
    return out


def value(p, w):
    return sum((c * math.prod(wi**ei for wi, ei in zip(w, powers))
                for powers, c in p.items()), Q(0))


def substitute(p, j, arrival=None):
    """Expand P(N e0 + N^-1 ej + e_arrival) as a Laurent polynomial.

    Uses the binomial theorem on the original monomials, independently of
    the gradient/Taylor limit used in the proof.
    """
    out = {}
    for powers, c in p.items():
        term = {0: c}
        for i, exponent in enumerate(powers):
            factor = {}
            for k in range(exponent + 1):
                # (W_i + delta_i)^exponent
                delta_power = exponent - k
                if delta_power and arrival != i:
                    continue
                if k and i not in (0, j):
                    continue
                n_power = k if i == 0 else (-k if i == j else 0)
                factor[n_power] = factor.get(n_power, Q(0)) + math.comb(exponent, k)
            product = {}
            for a, ca in term.items():
                for b, cb in factor.items():
                    product[a + b] = product.get(a + b, Q(0)) + ca * cb
            term = product
        out = add(out, term)
    return out


def laurent_value(p, n):
    return sum((c * Q(n)**e for e, c in p.items()), Q(0))


def cubic_linear(coefficients):
    out = {}
    for a in range(4):
        for b in range(4 - a):
            c = 3 - a - b
            out[(a, b, c)] = Q(math.factorial(3),
                                math.factorial(a) * math.factorial(b) * math.factorial(c)) * math.prod(
                x**p for x, p in zip(coefficients, (a, b, c)))
    return out


def main():
    started = time.monotonic()
    # Earlier claim: direct loads and a separate convex-combination witness.
    link_loads = (RHO[0] + RHO[1], RHO[0] + RHO[2])
    assert link_loads == (Q(7, 10), Q(7, 10))
    assert sum(RHO) == Q(6, 5)
    earlier_checked = 0
    for a in range(1, 7):
        for b in range(1, 7):
            for c in range(1, 7):
                w = (Q(a), Q(b), Q(c))
                drift = sum(ri * wi for ri, wi in zip(RHO, w)) - min(w)
                assert drift >= min(w) / 5
                earlier_checked += 1

    polynomials = {
        "total_work": {(1, 0, 0): Q(1), (0, 1, 0): Q(1), (0, 0, 1): Q(1)},
        "sum_squares": {(2, 0, 0): Q(1), (0, 2, 0): Q(1), (0, 0, 2): Q(1)},
        "sum_squared_link_workloads": {
            (2, 0, 0): Q(2), (1, 1, 0): Q(2), (1, 0, 1): Q(2),
            (0, 2, 0): Q(1), (0, 0, 2): Q(1)},
        "asymmetric_cubic": cubic_linear((Q(1), Q(2), Q(3))),
        "negative_local_derivative": {
            (2, 0, 0): Q(2), (1, 1, 0): Q(-3), (1, 0, 1): Q(1),
            (0, 2, 0): Q(5), (0, 0, 2): Q(5)},
    }

    # Ratios a_j/a_0; weights kappa_i=a_i^alpha give exact KKT checks.
    effective_weights = (Q(2), Q(3), Q(5))
    kkt_checks = 0
    output = {}
    for name, p in polynomials.items():
        degree, = {sum(e) for e in p}
        f_axis = value(p, (Q(1), Q(0), Q(0)))
        grad = [value(derivative(p, i), (Q(1), Q(0), Q(0))) for i in range(3)]
        assert grad[0] == degree * f_axis > 0
        limits = [sum(ri * gi for ri, gi in zip(RHO, grad)) - grad[j] for j in (1, 2)]
        assert sum(limits) == Q(2, 5) * grad[0]
        assert max(limits) >= grad[0] / 5
        local_output = []

        for j in (1, 2):
            ratio = effective_weights[j] / effective_weights[0]
            base = substitute(p, j)
            input_poly = {}
            for i in range(3):
                increment = add(substitute(p, j, i), base, Q(-1))
                input_poly = add(input_poly, increment, RHO[i])

            # Exact numerator of G V after multiplying by 1+ratio*N^2.
            numerator = add(input_poly, shift(input_poly, 2, ratio))
            numerator = add(numerator, substitute(derivative(p, 0), j), Q(-1))
            numerator = add(numerator, shift(substitute(derivative(p, j), j), 2, ratio), Q(-1))
            assert max(numerator, default=-100) <= degree + 1
            expanded_limit = numerator.get(degree + 1, Q(0)) / ratio
            assert expanded_limit == limits[j - 1]

            last_scaled = None
            for n in (16, 256, 4096, 65536):
                w = [Q(n), Q(0), Q(0)]
                w[j] = Q(1, n)
                service0 = Q(1) / (1 + ratio * n**2)
                servicej = 1 - service0
                for alpha in (1, 2, 3):
                    kappa0 = effective_weights[0]**alpha
                    kappaj = effective_weights[j]**alpha
                    assert kappa0 * Q(n)**alpha / service0**alpha == kappaj * Q(n**3)**alpha / servicej**alpha
                    kkt_checks += 1

                direct_input = Q(0)
                for i in range(3):
                    after = list(w)
                    after[i] += 1
                    direct_input += RHO[i] * (value(p, after) - value(p, w))
                direct_drift = direct_input - service0 * value(derivative(p, 0), w) - servicej * value(derivative(p, j), w)
                expanded_drift = laurent_value(numerator, n) / (1 + ratio * n**2)
                assert direct_drift == expanded_drift
                last_scaled = direct_drift * Q(n)**(1 - degree)
            assert abs(last_scaled - expanded_limit) < Q(1, 100)
            if expanded_limit > 0:
                assert last_scaled > 0
            local_output.append({
                "local_route": j,
                "expanded_limit": str(expanded_limit),
                "scaled_drift_at_N_65536": str(last_scaled),
            })

        output[name] = {"degree": degree, "F_e0": str(f_axis),
                        "gradient_e0": list(map(str, grad)), "branches": local_output}

    # Independent exact accessibility estimates, including the smallest N.
    for n in (2, 3, 16, 256):
        k, r, eta = n**3, Q(1, n**4), Q(1, n**8)
        assert r - eta - eta / k > 0
        assert k * (r - eta - eta / k) == Q(1, n) - k * eta - eta
        assert Q(1, n) - k * eta - eta > 0

    result = {
        "earlier_recheck": {"link_loads": list(map(str, link_loads)),
                            "beta": str(sum(RHO)), "coefficient_vectors": earlier_checked},
        "polynomial_checks": output,
        "exact_KKT_checks": kkt_checks,
        "status": "all exact checks passed",
        "elapsed_seconds": round(time.monotonic() - started, 4),
        "peak_RSS_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "process_nice": os.getpriority(os.PRIO_PROCESS, 0),
        "data_limits_bytes": resource.getrlimit(resource.RLIMIT_DATA),
        "data_limit_note": DATA_LIMIT_NOTE,
    }
    assert result["peak_RSS_bytes_macos"] < 1024**3
    rendered = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("obstruction_checks.json").write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
