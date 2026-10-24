"""Small independent numerical checks. No numerical pass is a mathematical proof.

Use only after the live local compute gate permits this one-thread, sub-second job.
Every completed graph/field batch is persisted immediately. No live-store writes.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROWS = ROOT / "MEASUREMENTS.jsonl"
TOL = 2e-10


def save(row: dict) -> None:
    row["recorded_at_unix"] = time.time()
    with ROWS.open("a", encoding="utf-8") as out:
        out.write(json.dumps(row, ensure_ascii=False) + "\n")


def logsum(values: list[float]) -> float:
    pivot = max(values)
    return pivot + math.log(math.fsum(math.exp(x - pivot) for x in values))


def c_uniform(q: int, beta: float) -> float:
    return math.log1p(math.expm1(beta) / q) - beta / q


def divergence(probs: list[float], log_q: list[float]) -> float:
    return math.fsum(p * (math.log(p) - x) for p, x in zip(probs, log_q) if p)


def law(log_weights: list[float]) -> tuple[list[float], list[float], float]:
    log_z = logsum(log_weights)
    logs = [x - log_z for x in log_weights]
    return [math.exp(x) for x in logs], logs, log_z


def graph_cases(q: int, vertices: int, edges: list[tuple[int, int]],
                name: str, betas: list[float], boundary: list[int] | None = None) -> dict:
    states = list(itertools.product(range(q), repeat=vertices))
    agreements = [sum(s[a] == s[b] for a, b in edges) for s in states]
    histogram = dict(sorted(Counter(agreements).items()))
    all_pass = True
    rows = []
    for beta in betas:
        free_p, free_log, log_z = law([beta * a for a in agreements])
        uniform_d = log_z - vertices * math.log(q) - beta * len(edges) / q
        edge_bound = len(edges) * c_uniform(q, beta)
        forest = len(edges) == vertices - 1 and name == "path4"
        passed = uniform_d + TOL >= edge_bound
        if forest:
            passed &= abs(uniform_d - edge_bound) <= TOL
        row = {"batch": name, "q": q, "vertices": vertices, "edges": len(edges),
               "states_enumerated": len(states), "beta": beta,
               "uniform_relative_entropy": uniform_d, "all_edge_lower_bound": edge_bound,
               "forest_equality_control": forest, "pass": bool(passed)}
        if boundary is not None:
            m = sum(boundary)
            b1 = [sum(n for spin, n in zip(s, boundary) if spin == 0) for s in states]
            b2 = [sum(n for spin, n in zip(s, boundary) if spin == 1) for s in states]
            fixed_p, fixed_log, _ = law([beta * (a + b) for a, b in zip(agreements, b1)])
            color2_p, color2_log, _ = law([beta * (a + b) for a, b in zip(agreements, b2)])
            mixture_p = [(p + r) / 2 for p, r in zip(fixed_p, color2_p)]
            fixed_to_free = divergence(fixed_p, free_log)
            free_to_fixed = divergence(free_p, fixed_log)
            mixture_to_free = divergence(mixture_p, free_log)
            e_plus = math.fsum(p * a for p, a in zip(fixed_p, agreements)) / vertices
            e_minus = math.fsum(p * a for p, a in zip(free_p, agreements)) / vertices
            color2_e = math.fsum(p * a for p, a in zip(color2_p, agreements)) / vertices
            passed &= max(fixed_to_free, free_to_fixed, mixture_to_free) <= beta * m + TOL
            passed &= abs(e_plus - color2_e) <= TOL
            passed &= abs(sum(free_p) - 1) <= TOL
            certificates = []
            if beta > 0:
                for h in (min(0.02, beta / 2), min(0.1, beta / 2)):
                    _, _, log_right = law([(beta + h) * a for a in agreements])
                    _, _, log_left = law([(beta - h) * a for a in agreements])
                    secants = (log_right - 2 * log_z + log_left) / (vertices * h)
                    cert = e_plus - e_minus - fixed_to_free / (vertices * h)
                    passed &= secants + TOL >= cert
                    certificates.append({"h": h, "secant_difference": secants,
                                         "finite_entropy_certificate_rhs": cert})
            row.update({"crossing_bonds": m, "surface_entropy_upper_bound": beta * m,
                        "fixed_to_free": fixed_to_free, "free_to_fixed": free_to_fixed,
                        "mixture_to_free": mixture_to_free,
                        "color_permuted_energy_difference": e_plus - color2_e,
                        "finite_certificates": certificates, "pass": bool(passed)})
        rows.append(row)
        save(row)
        all_pass &= bool(passed)
    return {"name": name, "q": q, "states": len(states), "energy_histogram": histogram,
            "all_pass": all_pass, "rows": rows}


def compositions(total: int, q: int):
    if q == 1:
        yield (total,)
    else:
        for x in range(total + 1):
            for tail in compositions(total - x, q - 1):
                yield (x,) + tail


def pair_fields(betas: list[float]) -> dict:
    q = 3
    counts = list(compositions(5, q))
    distributions = ((1/3, 1/3, 1/3), (2/3, 1/6, 1/6), (0.5, 0.3, 0.2))
    minimum_uniform_margin = float("inf")
    minimum_nonuniform_margin = float("inf")
    cases = 0
    all_pass = True
    for beta in betas:
        for left in counts:
            for right in counts:
                logs_raw = [beta * ((i == j) + left[i] + right[j])
                            for i in range(q) for j in range(q)]
                pair_p, pair_log, _ = law(logs_raw)
                odds_log = pair_log[0] + pair_log[4] - pair_log[1] - pair_log[3]
                all_pass &= abs(odds_log - 2 * beta) <= TOL
                for pi in distributions:
                    product_p = [pi[i] * pi[j] for i in range(q) for j in range(q)]
                    entropy = divergence(product_p, pair_log)
                    bound = 2 * min(pi)**4 * math.tanh(beta/2)**2
                    minimum_nonuniform_margin = min(minimum_nonuniform_margin, entropy - bound)
                    all_pass &= entropy + TOL >= bound
                    if pi == distributions[0]:
                        minimum_uniform_margin = min(minimum_uniform_margin,
                                                     entropy - c_uniform(q, beta))
                        all_pass &= entropy + TOL >= c_uniform(q, beta)
                    cases += 1
    row = {"batch": "conditional_pair_fields", "endpoint_field_compositions": len(counts),
           "field_pairs_per_beta": len(counts)**2, "distribution_cases": cases,
           "minimum_uniform_margin": minimum_uniform_margin,
           "minimum_nonuniform_margin": minimum_nonuniform_margin,
           "pass": bool(all_pass), "factorization_basis": "induced matching only"}
    save(row)
    return row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate-receipt", required=True)
    args = parser.parse_args()
    gate_path = Path(args.gate_receipt).resolve()
    if gate_path.parent != ROOT:
        raise SystemExit("Gate receipt must be in the worker folder")
    gate = json.loads(gate_path.read_text(encoding="utf-8"))
    if not gate.get("permitted") or not 0 <= time.time() - gate["sampled_at_unix"] <= 120:
        raise SystemExit("Fresh permitting resource-gate receipt required (<=120 seconds)")
    start = time.perf_counter()
    q, d = 3, 3
    beta_mf = 2 * math.log(2) / 3
    uniform_pi, ordered_pi = (1/3, 1/3, 1/3), (2/3, 1/6, 1/6)
    def score(pi):
        return -sum(p * math.log(p) for p in pi) + beta_mf * d * sum(p*p for p in pi)
    naive_score_gap = score(ordered_pi) - score(uniform_pi)
    saddle_deficit = math.log(3) - 19 * math.log(2) / 12
    corrected_deficit_bound = d * c_uniform(q, beta_mf)
    improvement = {"batch": "mean_field_premise_check", "q": q, "d": d,
                   "beta_MF": beta_mf, "naive_product_score_gap": naive_score_gap,
                   "naive_asserted_trial_entropy_deficit": 0.0,
                   "corrected_limiting_entropy_deficit_lower_bound": corrected_deficit_bound,
                   "stationary_product_score_barrier": saddle_deficit,
                   "deficit_bound_over_barrier": corrected_deficit_bound / saddle_deficit,
                   "product_laws_passing_zero_deficit_after_check": 0,
                   "pass": abs(naive_score_gap) <= TOL and corrected_deficit_bound > 0,
                   "critical_parameter_identified": False}
    save(improvement)
    betas = [0.0, 0.1, beta_mf, 0.55, 1.0]
    path = graph_cases(3, 4, [(0,1),(1,2),(2,3)], "path4", betas)
    cycle = graph_cases(3, 4, [(0,1),(1,2),(2,3),(3,0)], "cycle4", betas)
    vertices = list(itertools.product(range(2), repeat=3))
    edges = [(i,j) for i,x in enumerate(vertices) for j,y in enumerate(vertices)
             if i < j and sum(abs(a-b) for a,b in zip(x,y)) == 1]
    cube3 = graph_cases(3, 8, edges, "cube2x2x2", betas, [3]*8)
    cube2 = graph_cases(2, 8, edges, "cube2x2x2", [0.0, beta_mf], [3]*8)
    fields = pair_fields([0.1, beta_mf, 1.0])
    summary = {"command": "python -X utf8 verify_entropy_route.py --gate-receipt compute_gate.json",
               "check_type": "exhaustive small-state floating-point checks; not formal verification",
               "measurement_improvement": improvement,
               "graph_batches": [path,cycle,cube3,cube2], "field_batch": fields,
               "graph_beta_cases": 17, "conditional_distribution_cases": fields["distribution_cases"],
               "all_pass": all(x["all_pass"] for x in (path,cycle,cube3,cube2))
                           and fields["pass"] and improvement["pass"],
               "elapsed_seconds": time.perf_counter()-start,
               "C0048_solved": False, "independent_review": "pending"}
    (ROOT / "MEASUREMENT_SUMMARY.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("graph_beta_cases","conditional_distribution_cases",
                                            "all_pass","elapsed_seconds","C0048_solved")}))
    print(json.dumps(improvement))
    return 0 if summary["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
