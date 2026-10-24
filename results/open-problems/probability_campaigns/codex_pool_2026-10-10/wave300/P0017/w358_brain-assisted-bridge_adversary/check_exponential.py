"""Bounded exact algebra experiment; no model load, network or live-store writes."""
from fractions import Fraction
from math import comb, factorial, pi, sqrt, exp
from pathlib import Path
import json
import time


def mean(poly):
    return sum((c * factorial(k) for k, c in enumerate(poly)), Fraction())


def inner(left, right):
    return sum((a * b * factorial(i + j)
                for i, a in enumerate(left) if a
                for j, b in enumerate(right) if b), Fraction())


def primitive(poly):
    out = [Fraction()] + [c / (k + 1) for k, c in enumerate(poly)]
    out[0] = -mean(out)
    return out


def run():
    started = time.monotonic()
    # This experiment is held pending a fresh governor gate allowing execution.
    # It uses one Python process, exact degree <=64, no training/background work.
    gate_path = Path('~/.claude/compute/compute_state.json')
    gate = json.loads(gate_path.read_text(encoding='utf-8-sig'))
    if time.time() - gate_path.stat().st_mtime > 60 or gate.get('status') != 'ok':
        raise SystemExit('HELD: a fresh governor state with status ok is required')
    q = [Fraction(1)]
    rows = []
    polys = {}
    for d in range(1, 65):
        q = primitive(q)
        assert mean(q) == 0
        observed = inner(q, q)
        expected = comb(2 * d - 2, d - 1)
        assert observed == expected, (d, observed, expected)
        if d <= 2:
            polys[d] = q[:]
        if d in (1, 2, 3, 4, 8, 16, 32, 64):
            rows.append({"degree": d, "exact_squared_coefficient_norm": int(observed),
                         "norm_exponential_rate": float(observed) ** (1 / (2 * d))})
    q1, q2 = polys[1], polys[2]
    gram12 = inner(q1, q2)
    f = [a + b for a, b in zip(q1 + [Fraction()], q2)]
    fprime = [k * f[k] for k in range(1, len(f))]
    variance = inner(f, f) - mean(f) ** 2
    energy = inner(fprime, fprime)
    naive_diagonal = inner(q1, q1) + inner(q2, q2)
    assert (gram12, variance, energy, naive_diagonal) == (1, 5, 2, 3)
    result = {
        "scope": "independent exact polynomial recurrence under Exp(1); not a KLS proof",
        "degrees_checked": 64,
        "exact_identity_failures": 0,
        "coefficient_norms": rows,
        "reasoning_failure": {
            "statement": "Appell coefficients inherit Gaussian diagonal Parseval",
            "cross_gram_q1_q2": int(gram12),
            "before_predicted_variance": int(naive_diagonal),
            "after_full_gram_variance": int(variance),
            "exact_actual_variance": int(variance),
            "before_absolute_error": int(variance - naive_diagonal),
            "after_absolute_error": 0,
            "dirichlet_energy": int(energy),
            "rayleigh_quotient": str(variance / energy),
        },
        "linear_tilt_variances": [{"s": s, "variance": 1 / (1 - s) ** 2}
                                  for s in (0, 0.5, 0.9, 0.99)],
        "gaussian_damped_tilt_variances": [{"t": t, "theta": 1 - t,
                                             "variance": (1 - 2 / pi) / t}
                                            for t in (1, 0.1, 0.01, 0.001)],
        "compact_support_boundary": [{"L": L, "original_variance": (v := 1 - L * L * exp(-L) / (1 - exp(-L)) ** 2),
                                       "standardized_tilt_s": sqrt(v),
                                       "tilted_variance": L * L / (12 * v)}
                                      for L in (2, 10, 100)],
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "command": "python -X utf8 ~/brain_workers/w358/check_exponential.py",
    }
    (Path(__file__).parent / "exponential_measurements.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run()
