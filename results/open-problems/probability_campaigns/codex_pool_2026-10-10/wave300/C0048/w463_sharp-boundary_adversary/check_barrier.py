"""Small reproducible arithmetic checks; the written analytic proof carries the theorem."""
from decimal import Decimal, localcontext
import json
import math
from pathlib import Path


def energy(x, coupling):
    return sum(t * math.log(t) if t else 0.0 for t in x) - coupling * sum(t * t for t in x) / 2


def run():
    with localcontext() as ctx:
        ctx.prec = 70
        log2 = Decimal(2).ln()
        log3 = Decimal(3).ln()
        delta = log3 - Decimal(19) * log2 / Decimal(12)
        j0 = 4 * log2
        assert delta > 0
        assert 3**12 - 2**19 == 7153
        u = [1/3] * 3
        v = [2/3, 1/6, 1/6]
        saddle = [1/2, 1/4, 1/4]
        coupling = float(j0)
        base = energy(u, coupling)
        assert abs(energy(v, coupling) - base) < 1e-14
        assert abs(energy(saddle, coupling) - base - float(delta)) < 1e-14
        max_excess = -math.inf
        maximizing_m = None
        n = 2000
        for k in range(n + 1):
            m = k / (2*n)
            x = [(1+2*m)/3, (1-m)/3, (1-m)/3]
            excess = energy(x, coupling) - base
            if excess > max_excess:
                max_excess, maximizing_m = excess, m
            assert excess <= float(delta) + 1e-14
        assert maximizing_m == 0.25
        section_min = min(energy([0.5, k/(2*n), 0.5-k/(2*n)], coupling) for k in range(n+1))
        assert abs(section_min - energy(saddle, coupling)) < 1e-14
        result = {
            "coupling_J0": str(j0),
            "exact_barrier": "log(3) - (19/12)*log(2)",
            "barrier_decimal_70_digit_context": str(delta),
            "exact_positivity_integer_difference": 7153,
            "path_samples": n+1,
            "path_maximizing_m": maximizing_m,
            "path_max_excess_float": max_excess,
            "section_samples": n+1,
            "section_min_matches_saddle": True,
            "proof_status": "analytic proof saved; independent review pending",
            "finite_sampling_is_not_proof": True,
        }
        allowance_lower = 4 * log2 / 9
        necessary_dimension_ratio = 4 * log2 / (3 * delta)
        assert not 3**(12*818) > 2**(19*818+16)
        assert 3**(12*819) > 2**(19*819+16)
        result.update({
            "preprint_normalization": {"n": 2, "kappa": "2/3", "allowance": "(J*n*kappa/2)*I_d", "I_d_lower_bound": "1/(2d)"},
            "d3_allowance_lower_bound": str(allowance_lower),
            "d3_allowance_lower_bound_over_barrier": str(allowance_lower/delta),
            "necessary_dimension_ratio": str(necessary_dimension_ratio),
            "exact_integer_dimension_check": {"d818_passes_necessary_inequality": False, "d819_passes_necessary_inequality": True},
            "interpretation": "Allowance lower bound, not actual Gibbs error; dimension 819 is necessary only for this criterion, not sufficient and not a lattice phase threshold.",
        })
    Path(__file__).with_name("MEASUREMENTS.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run()
