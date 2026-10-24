"""Bounded CPU-only checks; algebraic proofs are in the Markdown, not this script."""
import cmath
import itertools
import json
import math
import time
import tracemalloc
from datetime import datetime, timezone
from pathlib import Path

folder = Path(__file__).resolve().parent
gate = {
    "gate_id": "w529-p0309-small-check-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "purpose": "Sanity-check the independent counterexamples and harmonic/reduction constants",
    "authorized_scope": "Fresh small CPU-only checks in this worker folder",
    "max_evaluations": 5000,
    "max_cpu_seconds": 5,
    "max_wall_seconds": 60,
    "max_python_allocation_bytes": 16 * 1024 * 1024,
    "gpu": False, "training": False, "child_agents": False,
    "external_data_loads": False, "status": "fresh"
}
(folder / "COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2), encoding="utf-8")
start_wall, start_cpu = time.perf_counter(), time.process_time()
tracemalloc.start()
evaluations = 0

def tick(n=1):
    global evaluations
    evaluations += n
    assert evaluations <= gate["max_evaluations"]
    assert time.process_time() - start_cpu <= gate["max_cpu_seconds"]
    assert time.perf_counter() - start_wall <= gate["max_wall_seconds"]
    assert tracemalloc.get_traced_memory()[1] <= gate["max_python_allocation_bytes"]

def dist2(x, y, period):
    tick()
    return sum(min((a-b) % period, (b-a) % period) ** 2 for a, b in zip(x, y))

translations = []
for size in (2, 3):
    points = list(itertools.product(range(0, 2*size, 2), repeat=3))
    shifted = [((x[0]+1) % (2*size), x[1], x[2]) for x in points]
    nearest = [min(dist2(x, y, 2*size) for y in points) for x in shifted]
    assert all(v == 1 for v in nearest)
    for i, j in itertools.combinations(range(len(points)), 2):
        assert dist2(points[i], points[j], 2*size) == dist2(shifted[i], shifted[j], 2*size)
    translations.append({"L": size, "particles": len(points), "bad_sites_delta_0_1": len(points), "squared_nearest_distance": 0.25, "energy_difference_for_any_periodic_pair_kernel": 0})

acoustic = []
for size in (3, 4, 8, 16, 32, 64):
    values = [math.cos(2*math.pi*j/size) for j in range(size)]
    tick(size)
    ratio = 0.5 * sum((values[(j+1) % size]-values[j])**2 for j in range(size)) / sum(x*x for x in values)
    expected = 2 * math.sin(math.pi/size)**2
    assert math.isclose(ratio, expected, rel_tol=2e-12, abs_tol=1e-14)
    acoustic.append({"L": size, "H_over_displacement_square_kappa_1": ratio, "formula_absolute_error": abs(ratio-expected)})

harmonic = []
for size in (3, 4, 5, 6, 8):
    total = 0.0
    for k in itertools.product(range(size), repeat=3):
        if k == (0, 0, 0):
            continue
        tick()
        total += 1 / (4 * sum(math.sin(math.pi*j/size)**2 for j in k))
    trace = total / size**3
    assert 0 < trace <= 13/16
    harmonic.append({"L": size, "normalized_inverse_trace": trace, "proved_upper_bound": 13/16})

matching = []
for n, m, phase, offset in itertools.product((4, 8), (0, 1, 2), (0.0, 0.125, 0.5), (0.0, 0.05)):
    tick()
    projection = 2*math.pi*offset
    positions = [j+phase+offset for j in range(n-m)] + [j+phase+0.5 for j in range(n-m, n)]
    amplitude = sum(cmath.exp(2j*math.pi*x) for x in positions)/n
    registered = cmath.exp(-2j*math.pi*phase) * amplitude
    lower = 1-2*m/n-(n-m)*projection**2/(2*n)
    assert registered.real >= lower-1e-13
    if lower >= 0:
        assert abs(amplitude)**2 >= lower**2-1e-13
    matching.append({"n": n, "m": m, "phase": phase, "offset": offset, "lower": lower, "registered_real": registered.real})

random_phase = [cmath.exp(2j*math.pi*phase) for phase in (0, 0.25, 0.5, 0.75)]
tick(4)
assert abs(sum(random_phase)/4) < 1e-14
assert all(math.isclose(abs(z)**2, 1.0) for z in random_phase)

entropy = []
for n in (1, 2, 3, 4, 6, 8, 12):
    tick()
    ell = math.exp(-n*n)
    probability = (1-ell)/(math.exp(-n*n+n)+1-ell)
    jacobian = ell/(1-ell)
    repair_bound = math.exp(-n)/jacobian
    assert probability <= repair_bound + 1e-14
    entropy.append({"n": n, "beta_tau": 1, "bad_probability": probability, "naive_energy_factor": math.exp(-n), "valid_bound_including_jacobian": repair_bound})

claims = [json.loads(line) for line in (folder / "CLAIMS.jsonl").read_text(encoding="utf-8").splitlines() if line]
assert len({row["claim_id"] for row in claims}) == len(claims)
assert all(row["remaining_gap"] and row["assumptions"] for row in claims)
tick()
result = {
    "checks_passed": True,
    "command": "python -X utf8 ~/brain_workers/w529/verify_math.py",
    "evaluations": evaluations,
    "runtime_cpu_seconds": time.process_time()-start_cpu,
    "runtime_wall_seconds": time.perf_counter()-start_wall,
    "peak_python_allocations_bytes": tracemalloc.get_traced_memory()[1],
    "translation_cases": translations,
    "acoustic_cases": acoustic,
    "harmonic_cases": harmonic,
    "matching_cases_count": len(matching),
    "matching_minimum_slack": min(x["registered_real"]-x["lower"] for x in matching),
    "random_phase": {"unregistered_mean_amplitude": abs(sum(random_phase)/4), "mean_squared_amplitude": 1.0},
    "entropy_cases": entropy,
    "claim_rows_before_session": 0,
    "claim_rows_after_checks": len(claims),
    "independently_checked_claims": [x["claim_id"] for x in claims if x["status"] == "independently checked proof"],
    "scope": "Finite sanity checks; not a formal proof or a measured live-brain improvement"
}
(folder / "MEASUREMENTS.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
gate.update(status="consumed", evaluations=evaluations, runtime_cpu_seconds=result["runtime_cpu_seconds"], runtime_wall_seconds=result["runtime_wall_seconds"])
(folder / "COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2), encoding="utf-8")
print(json.dumps({k: v for k,v in result.items() if k not in ("matching_cases",)}, indent=2))
