"""Bounded exact checks of examples and constants; these are not a theorem prover."""
import ctypes
import itertools
import json
import math
import shutil
import time
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
START = time.monotonic()
DEADLINE = START + 30


def budget():
    if time.monotonic() > DEADLINE:
        raise RuntimeError("30-second verification gate exceeded")


class MemoryStatus(ctypes.Structure):
    _fields_ = [("length", ctypes.c_ulong), ("load", ctypes.c_ulong)] + [
        (name, ctypes.c_ulonglong) for name in
        ("total_phys", "avail_phys", "total_page", "avail_page", "total_virt", "avail_virt", "avail_extended")
    ]


mem = MemoryStatus()
mem.length = ctypes.sizeof(mem)
if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem)):
    raise RuntimeError("fresh memory gate unavailable")
free_disk = shutil.disk_usage(ROOT).free
gate = {"at_utc": datetime.now(timezone.utc).isoformat(), "available_ram_bytes": mem.avail_phys,
        "free_disk_bytes": free_disk, "min_available_ram_bytes": 256 * 1024**2,
        "min_free_disk_bytes": 8 * 1024**2, "max_wall_seconds": 30,
        "max_chain_states": 9, "max_return_half_horizon": 32,
        "processes": 1, "parallel_threads": 0, "gpu": False, "training": False}
gate["passed"] = mem.avail_phys >= gate["min_available_ram_bytes"] and free_disk >= gate["min_free_disk_bytes"]
(ROOT / "COMPUTE_GATE.json").write_text(json.dumps(gate, indent=2) + "\n", encoding="utf-8")
if not gate["passed"]:
    raise RuntimeError("fresh compute gate rejected: bounded checks skipped")

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
KAPPA = F(1, 10)


def escape_radius(points):
    distances = []
    for start in points:
        frontier, seen, radius = {start}, {start}, 0
        while frontier:
            radius += 1
            nxt = set()
            for x in frontier:
                for step in DIRS:
                    y = tuple(x[i] + step[i] for i in range(2))
                    if y not in points:
                        break
                    if y not in seen:
                        nxt.add(y)
                else:
                    continue
                break
            else:
                frontier = nxt - seen
                seen |= frontier
                continue
            distances.append(radius)
            break
    return max(distances)


def solve(matrix, rhs):
    a = [list(row) + [b] for row, b in zip(matrix, rhs)]
    n = len(a)
    for i in range(n):
        pivot = next(j for j in range(i, n) if a[j][i])
        a[i], a[pivot] = a[pivot], a[i]
        denom = a[i][i]
        a[i] = [v / denom for v in a[i]]
        for j in range(n):
            if j != i:
                factor = a[j][i]
                a[j] = [u - factor * v for u, v in zip(a[j], a[i])]
    return [row[-1] for row in a]


sets = [
    {(0, 0)},
    {(-1, 0), (0, 0), (1, 0)},
    set(itertools.product(range(-1, 2), repeat=2)),
    {(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)},
    {(0, 0), (2, 0)},
]
chain_rows = []
tail_checks = 0
for points in sets:
    for mode in ("uniform", "inward", "east"):
        budget()
        states = sorted(points)
        index = {x: i for i, x in enumerate(states)}
        n = len(states)
        q = [[F(0) for _ in states] for _ in states]
        for x in states:
            favorite = min(range(4), key=lambda j: sum(abs(x[i] + DIRS[j][i]) for i in range(2)))
            if mode == "east":
                favorite = 0
            weights = [F(1, 4)] * 4 if mode == "uniform" else [KAPPA] * 4
            if mode != "uniform":
                weights[favorite] += 1 - 4 * KAPPA
            for step, prob in zip(DIRS, weights):
                y = tuple(x[i] + step[i] for i in range(2))
                if y in index:
                    q[index[x]][index[y]] += prob
        radius = escape_radius(points)
        assert radius**2 <= 2 * n
        matrix = [[F(i == j) - q[i][j] for j in range(n)] for i in range(n)]
        means = solve(matrix, [F(1)] * n)
        bound = radius / KAPPA**radius
        assert max(means) <= bound
        survival = [F(1)] * n
        for step in range(1, 5 * radius + 1):
            survival = [sum(q[i][j] * survival[j] for j in range(n)) for i in range(n)]
            if step % radius == 0:
                assert max(survival) <= (1 - KAPPA**radius)**(step // radius)
                tail_checks += n
        chain_rows.append({"states": n, "mode": mode, "radius": radius,
                           "exact_max_exit_mean": str(max(means)), "ER_bound": str(bound)})

return_checks = 0
for horizon in (4, 8, 16, 32):
    delta = F(1, 16 * horizon)
    for n in range(1, horizon + 1):
        budget()
        base = F(math.comb(2 * n, n), 4**n)**2
        assert base >= F(1, 4 * n)
        actual = sum(
            F(math.factorial(2 * n), math.factorial(k)**2 * math.factorial(n - k)**2)
            * (F(1, 16) - delta**2)**k * F(1, 16)**(n - k)
            for k in range(n + 1)
        )
        assert actual >= F(1, 8 * n)
        return_checks += 1

mgf_constant_checks = 0
for numerator in range(1, 33):
    a = F(numerator, 64)
    z = 1 / (1 - a / 4)
    denominator = 1 - (1 - a) * z
    assert denominator > 0
    assert a * z / denominator == F(4, 3)
    mgf_constant_checks += 1

# A deliberately future-dependent horizon and conditioning event in a bounded
# geometric-duration model. This is an example check, not an RWRE simulation.
probs = {1: F(1, 2), 2: F(1, 4), 3: F(1, 8), 4: F(1, 8)}
p = e_tau = e_count = F(0)
for durations in itertools.product(probs, repeat=3):
    probability = math.prod(probs[d] for d in durations)
    if max(durations) != 4:
        continue
    count = durations.index(max(durations)) + 1
    tau = sum(durations[:count])
    p += probability
    e_tau += probability * tau
    e_count += probability * count
L = math.ceil(16 * math.log(4 / 3))  # a=1/2, r=1
assert e_count / p <= e_tau / p <= L * (e_count / p + 3 / p)
budget()
result = {"command": "python -X utf8 ~/brain_workers/w447/verify_exact.py",
          "at_utc": datetime.now(timezone.utc).isoformat(), "passed": True,
          "finite_kernels": len(chain_rows), "statewise_tail_checks": tail_checks,
          "exact_return_probability_checks": return_checks,
          "exact_mgf_constant_checks": mgf_constant_checks,
          "anticipative_duration_outcomes": 4**3,
          "anticipative_condition_probability": str(p),
          "anticipative_conditional_mean_tau": str(e_tau / p),
          "anticipative_conditional_mean_count": str(e_count / p),
          "elapsed_seconds": time.monotonic() - START, "kernels": chain_rows,
          "limits": "Finite exact examples check constants and scope only; not a proof of C0041 or independent theorem audit."}
(ROOT / "VERIFICATION.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in result.items() if k != "kernels"}, indent=2))
