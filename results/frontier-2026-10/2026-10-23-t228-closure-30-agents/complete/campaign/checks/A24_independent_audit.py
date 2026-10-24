#!/usr/bin/env python3
"""Exact rational post-check and fail-closed tests for the A13 certificate.

This does not replace the audited interval quadrature.  It independently
checks its constants and reported signs, pins the source bytes, compares the
full replay, and tests the optimization guard.  All checks survive -O.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "checks/A13_tail_index_certificate.py"
HISTORY = ROOT / "history/A13_tail_index_certificate_v1.py"
AUTHOR = ROOT / "checks/A13_tail_index_certificate.json"
REPLAY = ROOT / "checks/A24_replayed_certificate.json"
FALSE_PASS = ROOT / "checks/A24_optimized_falsepass.json"
PROOF = ROOT / "proofs/T228_EXPLICIT_CLOSURE.md"
EXPECTED = {
    "historical_script": "f3b81bb6b7b3520c842e21dfa7faa919c104e0ff21b68e44d85864b66d359ff4",
    "guarded_script": "ce9e6b42e901d7ffa06c11cbc6e35e6f2ad8b3216e957896374a9e4527a0bb58",
    "author_json": "4e7aecd1c9c5f0f74461105ed874da598713dcff4aa41f1e62a863074a05844b",
    "proof": "a1dbdbb1e99a85749143f44dd8b7d7e264fb550d285c5667f69f1a35ff87c38f",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def arctan_interval(n, terms=80):
    # Independent recurrence, rather than the author's exponent-per-term sum.
    numerator_power = F(1, n)
    total = F(0)
    ratio = -F(1, n * n)
    for k in range(terms):
        total += numerator_power / (2 * k + 1)
        numerator_power *= ratio
    endpoint = total + numerator_power / (2 * terms + 1)
    return min(total, endpoint), max(total, endpoint)


def main():
    hashes = {
        "historical_script": digest(HISTORY),
        "guarded_script": digest(SCRIPT),
        "author_json": digest(AUTHOR),
        "proof": digest(PROOF),
    }
    require(hashes == EXPECTED, "Audited source/output bytes changed")
    require(REPLAY.read_bytes() == AUTHOR.read_bytes(), "Full replay differs")
    guard = '''if not __debug__:
    raise RuntimeError(
        "Certificate checks require assertions enabled; run without -O/-OO "
        "and without PYTHONOPTIMIZE. No certificate was produced."
    )

'''
    require(SCRIPT.read_text().count(guard) == 1, "Expected guard absent")
    require(SCRIPT.read_text().replace(guard, "") == HISTORY.read_text(),
            "Numerical algorithm changed with guard")

    data = json.loads(AUTHOR.read_text())
    require(data["status"] == "PASS", "Author result not PASS")
    require(data["script_sha256"] == EXPECTED["historical_script"],
            "Historical output script identity mismatch")
    require(data["source_proof_sha256"] == EXPECTED["proof"],
            "Historical output proof identity mismatch")

    # Machin branch: 0 < 4 atan(1/5)-atan(1/239) < 4/5 < 1 < pi/2.
    # The last inequality follows independently from atan(1)>1/2.
    branch_lower = 4 * (F(1, 5) - F(1, 375)) - F(1, 239)
    require(0 < branch_lower < F(4, 5) < 1, "Machin branch check failed")
    t = F(1, 5)
    for _ in range(2):
        require(1 - t * t > 0, "Unexpected doubling branch")
        t = 2 * t / (1 - t * t)
    require((t - F(1, 239)) / (1 + t * F(1, 239)) == 1,
            "Machin tangent identity failed")
    a_lo, a_hi = arctan_interval(5)
    b_lo, b_hi = arctan_interval(239)
    pi_lo, pi_hi = 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo
    constants = data["constants"]
    dec_pi_lo, dec_pi_hi = map(F, constants["pi_interval"])
    c_lo, c_hi = map(F, constants["normalizer_interval"])
    require(dec_pi_lo <= pi_lo < pi_hi <= dec_pi_hi,
            "Reported pi interval fails independent 80-term enclosure")
    require(0 < c_lo < c_hi < 1, "Normalizer signs/order failed")
    require(c_lo * c_lo <= 2 / pi_hi and 2 / pi_lo <= c_hi * c_hi,
            "Reported normalizer fails independent rational squaring")

    b, c = F(101, 100), F(13, 10)
    require(pi_hi / 2 < c * c and 2 * b < F(3, 2) ** 2,
            "Gaussian mass/cusp constants failed")
    derivative_terms = [12, 8 * b * b * c, 4 * b * c * (2 + b),
                        8 * b * c * (2 + 3 * b), c * (4 + 8 * b + 18 * b * b)]
    derivative_total = sum(derivative_terms, F(0))
    require(derivative_total == F(6541351, 50000) < 140,
            "Derivative bound algebra failed")
    require(F(constants["derivative_L1_bound_exact"]) == derivative_total,
            "Reported derivative constant differs")
    require(F(constants["derivative_L1_bound_used"]) == 140,
            "Reported quadrature constant differs")
    partial_e = sum((F(1, math.factorial(k)) for k in range(7)), F(0))
    require(partial_e == F(1957, 720) > F(1359, 500) > F(8, 3),
            "Rational exponential bounds failed")
    require(pi_lo > F(157, 50), "Rational pi fallback failed")
    require(16 / (2 * F(157, 50) * F(1359, 500)) < F(97, 100) ** 2,
            "Independent h(1) bound failed")
    require(1 - 2 * F(99, 100) + 3 * F(99, 100) ** 2 == F(19603, 10000) > 1,
            "Independent h(2) bound failed")
    tail = 2 * (10 ** 3 + 3 * 10 + F(3, 10)) * F(3, 8) ** 50
    require(F(constants["normalized_tail_bound_exact"]) == tail < F(1, 10 ** 17),
            "Rational tail bound failed")
    require(F(constants["normalized_tail_bound_up"]) >= tail,
            "Tail conversion is not outward")

    q = data["grid_denominator"]
    require(q == 10000 and data["radius"] == 10, "Unexpected mesh/radius")
    expected = [(F(99, 100), "1.10928", "1.10929"),
                (F(1), "1.09082", "1.09083"),
                (F(101, 100), "1.07272", "1.07273")]
    require(len(data["cases"]) == 3, "Wrong number of cases")
    signs = []
    for case, (eta, p_lo, p_hi) in zip(data["cases"], expected):
        require(F(case["eta"]) == eta, "Eta mismatch")
        require(case["strict_root_bracket"] == [p_lo, p_hi], "Bracket mismatch")
        require(F(p_hi) - F(p_lo) == F(case["bracket_width"]) == F(1, 100000),
                "Incorrect bracket width")
        endpoints = case["endpoint_certificates"]
        require(len(endpoints) == 2, "Wrong endpoint count")
        for endpoint, p in zip(endpoints, [p_lo, p_hi]):
            require(endpoint["p"] == p and 1 < F(p) < 2, "Exponent mismatch")
            lo, hi = map(F, endpoint["h_interval"])
            trap_lo, trap_hi = map(F, endpoint["normalized_trapezoid_interval"])
            error, tail_up = F(endpoint["quadrature_error_up"]), F(endpoint["tail_error_up"])
            require(0 < lo <= hi and 0 < trap_lo <= trap_hi, "Invalid intervals")
            require(error >= F(140, 8 * q * q) and tail_up >= tail,
                    "Understated analytic error")
            require(lo <= trap_lo - error and hi >= trap_hi + error + tail_up,
                    "Final enclosure fails directed error composition")
            m_lo, m_hi = map(F, endpoint["h_minus_one_interval"])
            require(m_lo <= lo - 1 and m_hi >= hi - 1, "h-1 bounds not outward")
            reported_width = F(endpoint["normalized_rounding_width_up"])
            require(trap_hi - trap_lo <= reported_width < F("6.5e-35"),
                    "Rounding width mismatch")
            require(endpoint["nodes"] == 10 * q + 1, "Node count mismatch")
        left_upper = F(endpoints[0]["h_interval"][1])
        right_lower = F(endpoints[1]["h_interval"][0])
        require(left_upper < 1 < right_lower, "Strict endpoint sign check failed")
        signs.append({"eta": str(eta), "bracket": [p_lo, p_hi],
                      "lower_endpoint_gap_below_one_exact": str(1 - left_upper),
                      "upper_endpoint_gap_above_one_exact": str(right_lower - 1)})
    cal_lo, cal_hi = map(F, data["calibration"]["h_interval"])
    require(cal_lo <= 2 <= cal_hi, "Gaussian moment calibration failed")

    false = json.loads(FALSE_PASS.read_text())
    require(false["status"] == "PASS" and false["grid_denominator"] == 10,
            "Missing historical false-PASS counterexample")
    require(all(F(endpoint["h_interval"][0]) < 1 < F(endpoint["h_interval"][1])
                for case in false["cases"] for endpoint in case["endpoint_certificates"]),
            "Historical counterexample does not straddle one")
    guard_results = []
    configurations = [("-O", ["-O"], None), ("-OO", ["-OO"], None),
                      ("PYTHONOPTIMIZE=1", [], "1"), ("PYTHONOPTIMIZE=2", [], "2")]
    for label, flags, opt in configurations:
        environment = dict(os.environ)
        environment.pop("PYTHONOPTIMIZE", None)
        if opt is not None:
            environment["PYTHONOPTIMIZE"] = opt
        run = subprocess.run([sys.executable, *flags, str(SCRIPT),
                              "--grid-denominator", "10"], env=environment,
                             capture_output=True, text=True, timeout=20)
        require(run.returncode != 0 and not run.stdout and
                "No certificate was produced." in run.stderr,
                "Optimization guard did not reject " + label)
        guard_results.append({"mode": label, "returncode": run.returncode,
                              "stdout_empty": not run.stdout, "rejected": True})
    normal_env = dict(os.environ)
    normal_env.pop("PYTHONOPTIMIZE", None)
    coarse = subprocess.run([sys.executable, str(SCRIPT), "--grid-denominator", "10"],
                            env=normal_env, capture_output=True, text=True, timeout=20)
    require(coarse.returncode != 0 and not coarse.stdout and "AssertionError" in coarse.stderr,
            "Unoptimized invalid coarse-grid signs did not fail closed")
    require(digest(PROOF) == EXPECTED["proof"] and digest(SCRIPT) == EXPECTED["guarded_script"],
            "Audited files changed during independent post-check")
    result = {
        "status": "PASS",
        "scope": "A13 scalar numerical certificate; no renewal/tail-theorem audit",
        "source_hashes": hashes,
        "full_normal_replay_byte_identical_to_original_json": True,
        "guard_only_change_to_original_numerical_source": True,
        "normalizer_checked_by_independent_80_term_Machin_rationals": True,
        "machin_branch_lower_exact": str(branch_lower),
        "derivative_L1_terms_exact": list(map(str, derivative_terms)),
        "derivative_L1_sum_exact": str(derivative_total),
        "tail_bound_exact": str(tail),
        "strict_signs": signs,
        "historical_false_pass_reproduced": True,
        "guard_tests": guard_results,
        "normal_coarse_grid_rejected": True,
        "arithmetic_trust_boundary": "Audited analytic inequalities; Python int/Fraction; documented Decimal arithmetic and correctly rounded ln/exp; runtime/hardware. Not proof-assistant verified.",
    }
    out = ROOT / "checks/A24_independent_audit.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
