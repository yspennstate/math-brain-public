"""Independent bounded arithmetic controls for the peer audit."""
import itertools
import json
import math
import time
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
gate = json.loads((ROOT / "PEER_COMPUTE_GATE.json").read_text(encoding="utf-8"))
started = time.monotonic()


def choose(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


incidence_cases = 0
equality = []
for q in range(1, gate["max_q"] + 1):
    for p in range(1, min(q, gate["max_p"]) + 1):
        n = p + q
        assert n <= gate["max_tensor_slots"]
        psets = [frozenset(s) for s in itertools.combinations(range(n), p)]
        qsets = [frozenset(s) for s in itertools.combinations(range(n), q)]
        for f in psets:
            for g in psets:
                overlap = len(f & g)
                actual_left = sum(f | g <= e for e in qsets)
                actual_right = sum(
                    choose(q - p, p - s) * choose(overlap, s)
                    for s in range(p + 1)
                )
                assert actual_left == actual_right
                incidence_cases += 1

        bits = list(itertools.product((0, 1), repeat=n))
        tensors = {
            b: Fraction((-1) ** sum(b[:p]), choose(q, p - sum(b[:p])))
            if sum(b) == p else Fraction(0)
            for b in bits
        }
        permutations = list(itertools.permutations(range(q)))
        projected = {}
        for b in bits:
            projected[b] = sum(
                (tensors[tuple(b[i] for i in perm) + b[q:]]
                 for perm in permutations), Fraction(0)
            ) / len(permutations)
        t_squared = sum((v * v for v in tensors.values()), Fraction(0))
        pt_squared = sum((v * v for v in projected.values()), Fraction(0))
        assert pt_squared > 0
        ratio = t_squared / pt_squared
        assert ratio == choose(q, p) ** 2
        equality.append({"p": p, "q": q, "squared_ratio": str(ratio)})

gram_cases = 0
for j in range(1, gate["max_degree"] + 1):
    for k in range(1, gate["max_degree"] + 1):
        # Direct four-term raw-moment integration of P_j P_k.
        val = (
            Fraction(math.factorial(j + k), math.factorial(j) * math.factorial(k))
            - Fraction(math.factorial(j + k - 1), math.factorial(j) * math.factorial(k - 1))
            - Fraction(math.factorial(j + k - 1), math.factorial(j - 1) * math.factorial(k))
            + Fraction(math.factorial(j + k - 2), math.factorial(j - 1) * math.factorial(k - 1))
        )
        assert val == choose(j + k - 2, j - 1)
        gram_cases += 1


def positive_compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for first in range(1, total - count + 2):
            for rest in positive_compositions(total - first, count - 1):
                yield (first,) + rest


traces = []
for d in range(1, gate["max_degree"] + 1):
    for s in range(1, d + 1):
        trace = Fraction(0)
        for alpha in positive_compositions(d, s):
            weight = Fraction(math.prod(math.factorial(a) for a in alpha), math.factorial(d))
            trace += weight * math.prod(choose(2 * a - 2, a - 1) for a in alpha)
        bound = choose(2 * d - 2, d - 1)
        assert trace <= bound
        if s == 1:
            assert trace == bound
        traces.append({"d": d, "support_size": s, "trace": str(trace), "bound": bound})

elapsed = time.monotonic() - started
result = {
    "command": "python -X utf8 verify_peer.py",
    "incidence_ordered_pair_checks": incidence_cases,
    "exact_projection_equality_cases": equality,
    "raw_moment_gram_checks": gram_cases,
    "support_trace_cases": len(traces),
    "largest_degree": gate["max_degree"],
    "trace_cases": traces,
    "pareto_domain_counterexample": {
        "mean": 0, "variance": "1", "fourth_moment": "9/5",
        "nonzero_real_exponential_moments": "infinite (symbolic tail argument)"
    },
    "elapsed_seconds": elapsed,
    "within_compute_gate": elapsed <= gate["max_wall_seconds"],
    "full_KLS_proof": False
}
(ROOT / "PEER_MEASUREMENTS.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({k: v for k, v in result.items() if k != "trace_cases"}, indent=2))
if not result["within_compute_gate"]:
    raise RuntimeError("fresh compute gate exceeded")
