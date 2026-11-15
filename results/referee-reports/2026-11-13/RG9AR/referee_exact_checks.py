"""Exact marked-product balance, exponent audit, and initial-state counterexample.

All computations are independent of code/. Standard library, serial execution.
"""
import itertools
import json
import math
import random
import signal
import statistics
import time
from fractions import Fraction as F
from pathlib import Path


def timeout(signum, frame):
    raise TimeoutError("120 second wall-clock budget")


signal.signal(signal.SIGALRM, timeout)
signal.alarm(120)
START = time.monotonic()


LAW = {F(1): F(4, 5), F(4): F(1, 5)}
M = sum(b * p for b, p in LAW.items())
HMARK = {b: b * p / M for b, p in LAW.items()}
RHO = F(4, 5)
RATE = RHO / M


def shares(n, rule):
    out = [F(0)] * n
    if rule == "LCFS":
        out[-1] = F(1)
    elif rule == "middle":
        out[(n - 1) // 2] = F(1)
    elif rule == "mixed_ends":
        out[0] += F(1, 2)
        out[-1] += F(1, 2)
    elif rule == "sparse_rank":
        # Depends strongly on n and includes zero shares.
        out[n // 3] += F(2, 7)
        out[(2 * n) // 3] += F(5, 7)
    else:
        raise ValueError(rule)
    assert sum(out) == 1
    return out


def test_function(marks, residuals):
    # The b_i weight makes the pair term sensitive to the ordered marks.
    # At x_k=0 deletion leaves precisely f_{n-1} on the surviving sequence.
    return sum(residuals) + sum(marks[i] * residuals[i] * residuals[j]
                                for i in range(len(marks))
                                for j in range(i + 1, len(marks)))


def derivative(marks, residuals, k):
    return 1 + sum(marks[k] * residuals[j] for j in range(k + 1, len(marks))) + sum(
        marks[i] * residuals[i] for i in range(k))


def states(n):
    for marks in itertools.product(LAW, repeat=n):
        probability = math.prod(HMARK[b] for b in marks)
        yield list(marks), [b / 2 for b in marks], probability


def balance_checks():
    count = 0
    boundary_checks = 0
    for rule in ("LCFS", "middle", "mixed_ends", "sparse_rank"):
        for n in range(1, 7):
            gamma = shares(n, rule)
            service = F(0)
            for marks, xs, prob in states(n):
                service -= prob * sum(gamma[k] * derivative(marks, xs, k) for k in range(n))
                for k in range(n):
                    at_zero = xs.copy()
                    at_zero[k] = F(0)
                    assert test_function(marks, at_zero) == test_function(
                        marks[:k] + marks[k + 1:], xs[:k] + xs[k + 1:])
                    boundary_checks += 1
            insertion = F(0)
            for marks, xs, prob in states(n - 1):
                old = test_function(marks, xs)
                for b, p in LAW.items():
                    for k in range(n):
                        new = test_function(marks[:k] + [b] + marks[k:], xs[:k] + [b] + xs[k:])
                        insertion += prob * p * gamma[k] * (new - old)
            cancellation = (1 - RHO) * RHO ** n * service + (
                (1 - RHO) * RHO ** (n - 1) * RATE * insertion)
            assert cancellation == 0, (rule, n, cancellation)
            count += 1
    return dict(service_law="B=1(4/5),4(1/5)", m=str(M),
                H_original_mark={str(k): str(v) for k, v in HMARK.items()},
                level_balance_identities=count, exact_residual="0",
                deletion_boundary_checks=boundary_checks,
                note="Finite exact diagnostics; general proof is the integration-by-parts identity.")


def exponent_checks():
    q = 2 ** (-0.25)
    eps, C, m, m2 = 0.7, 3.0, 1.0, 1.8
    worst_error = 0.0
    checked = 0
    c = eps ** 2 * (1 - q) ** 2 / (4 * (C * m2 / m + eps / 3))
    for r in (128, 1024, 2 ** 20):
        for j in range(40):
            b = r * 2 ** (-j - 1)
            a = (1 - q) * q ** j
            x = eps * r * a
            for w in (0.0, 0.001, m2):
                variance = (C / m) * r * b * w
                exponent = x * x / (8 * (variance + b * x / 3))
                bound = c * 2 ** (j / 2)
                assert exponent >= bound * (1 - 1e-13)
                ratio = x / (4 * b)
                exact_ratio = eps * (1 - q) * 2 ** (3 * j / 4 - 1)
                worst_error = max(worst_error, abs(ratio / exact_ratio - 1))
                checked += 1
    # Ratios of the dominating sequence 4^{j+1} exp(-c 2^{j/2}) tend to zero.
    log_ratios = {j: math.log(4) - c * (math.sqrt(2) - 1) * 2 ** (j / 2)
                  for j in (10, 20, 40, 60)}
    return dict(inequality_checks=checked, largest_ratio_relative_error=worst_error,
                c=c, dominating_sequence_log_successive_ratios=log_ratios,
                powers=dict(cycles="r", arrivals_per_cycle="r*p_j*pi(S_j)",
                            union="r^2*p_j*pi(S_j)",
                            mark_bound="r^2*p_j <= 4^(j+1)*w_j",
                            x_j="epsilon*(1-q)*r*2^(-j/4)",
                            variance="<= (C/m)*r*b_j*w_j",
                            exponent=">= c*2^(j/2), independent of r",
                            conclusion="o_P(r), with no general polynomial rate"))


def cohort_counterexample():
    # PS, subsequent service requirements 1; h=1/2. Initially r old jobs,
    # each original size 1 and residual 1/2. Before they all complete, no new
    # job can have completed: every new job receives less than 1/2 service.
    rows = []
    for r in (64, 256, 1024, 4096):
        vals = []
        for rep in range(256):
            rng = random.Random(811000 + r * 1000 + rep)
            t, virtual_age, new = 0.0, 0.0, 0
            while True:
                wait = rng.expovariate(1 - 1 / r)
                to_cohort_completion = (0.5 - virtual_age) * (r + new)
                if wait >= to_cohort_completion:
                    t += to_cohort_completion
                    break
                t += wait
                virtual_age += wait / (r + new)
                new += 1
            workload = r / 2 + new - t
            before = (workload - (r + new) / 2) / r
            after = (workload - new / 2) / r
            assert abs(after - before - 0.5) < 1e-12
            vals.append((t / r, before, after))
        rows.append(dict(r=r, repetitions=256,
                         mean_departure_time_over_r=statistics.mean(x[0] for x in vals),
                         mean_D_before_over_r=statistics.mean(x[1] for x in vals),
                         mean_D_after_over_r=statistics.mean(x[2] for x in vals)))
    return dict(model="PS; arriving B=1; r initial jobs with residual 1/2",
                initial_collapse_exact=True, all_initial_jobs_leave="O_P(r)",
                limiting_departure_time_over_r=math.exp(0.5) - 1,
                limiting_D_before_over_r=(1 - math.exp(0.5)) / 2,
                limiting_D_after_over_r=1 - math.exp(0.5) / 2,
                deterministic_jump_over_r=0.5, simulations=rows)


if __name__ == "__main__":
    result = dict(marked_balance=balance_checks(), exponents=exponent_checks(),
                  initial_state_remark=cohort_counterexample())
    result["elapsed_seconds"] = time.monotonic() - START
    text = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("referee_exact_checks.json").write_text(text)
    print(text, end="")
