import json
import math
from pathlib import Path
import random
import time

base = Path(__file__).resolve().parent
gate = json.loads((base / 'COMPUTE_GATE.json').read_text(encoding='utf-8'))
started = time.perf_counter()
rng = random.Random(499120)

def logsumexp(values):
    peak = max(values)
    return peak + math.log(math.fsum(math.exp(x - peak) for x in values))

def functional(layers, beta=None):
    width = len(layers[0])
    current = [0.0] * width
    for layer in layers:
        new = []
        for j in range(width):
            # A deterministic ring path family: each site can be entered
            # from itself or its preceding neighbor. Count W=1 only once.
            parents = [current[j]] if width == 1 else [current[j], current[(j - 1) % width]]
            if beta is None:
                new.append(layer[j] + max(parents))
            else:
                new.append(layer[j] + logsumexp([beta * x for x in parents]) / beta)
        current = new
    return max(current) if beta is None else logsumexp([beta * x for x in current]) / beta

errors = {'max': [], 'normalized_logZ': []}
naive_errors = []
cases = []
for width in [1, 2, 3, 4, 7]:
    for n in [1, 2, 8, 64]:
        assert width <= gate['max_width'] and n <= gate['max_layers']
        layers = [[rng.gauss(0, 1) for _ in range(width)] for _ in range(n)]
        means = [math.fsum(layer) / width for layer in layers]
        residual = [[x - mean for x in layer] for layer, mean in zip(layers, means)]
        for beta in [None, 0.3, 1.0, 2.0]:
            original = functional(layers, beta)
            centered = functional(residual, beta)
            delta = math.fsum(means)
            corrected = abs(original - centered - delta)
            naive_errors.append(abs(original - centered))
            label = 'max' if beta is None else 'normalized_logZ'
            errors[label].append(corrected)
            cases.append({'n': n, 'width': width, 'beta': beta, 'identity_error': corrected, 'analytic_floor': n / width})
            assert corrected < 1e-10
            assert len(cases) <= gate['max_cases']
            assert time.perf_counter() - started < gate['max_runtime_seconds']

result = {
    'command': 'python -X utf8 ~/brain_workers/w499/validate_boundary.py',
    'cases': len(cases),
    'max_error_before_adding_common_mode': max(naive_errors),
    'max_error_after_adding_common_mode': max(max(values) for values in errors.values()),
    'by_functional_max_error': {key: max(values) for key, values in errors.items()},
    'single_path_exact_variance_n64_beta2': 256,
    'single_path_bad_n2thirds_ratio_n64': 64 / (64 ** (2 / 3)),
    'elapsed_seconds': time.perf_counter() - started,
    'status': 'PASS',
    'interpretation': 'Finite arithmetic identity checks only; no Monte Carlo variance estimate and no parent proof.',
    'cases_detail': cases,
}
(base / 'MEASUREMENTS.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({key: value for key, value in result.items() if key != 'cases_detail'}, indent=2))
