"""Small, single-threaded checks of PROOF.md; no optimization or training.

Run: python -B verify.py
Writes only verification_data.json in this script's directory.
"""
import os
for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
import ctypes
import json
import math
from fractions import Fraction as Q
from pathlib import Path
import time

if os.name == "nt":
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.GetCurrentProcess.restype = ctypes.c_void_p
    kernel32.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    assert kernel32.SetPriorityClass(kernel32.GetCurrentProcess(), 0x4000)

import numpy as np


def exact_constants():
    # Derive through fractions rather than the rounded matrix bounds in the proof.
    lo, hi = Q(3, 4) / Q(5, 4), Q(5, 4) / Q(3, 4)
    selected_lo, selected_hi = lo * lo, hi * hi
    assert lo == Q(3, 5) and hi == Q(5, 3)
    assert selected_lo >= Q(1, 3) and selected_hi <= 3
    xnorm_at_largest_r = Q(3, 4)**2 * Q(1, 8) / Q(1, 3)
    # Compute slope coefficient twice: exact eigenvalue, then rounded one.
    slope_exact = 4 * selected_lo - 4 * Q(3, 4)**2 / 8
    slope_rounded = 4 * Q(1, 3) - 4 * Q(3, 4)**2 / 8
    assert xnorm_at_largest_r == Q(27, 128) < 1
    assert slope_exact > slope_rounded == Q(101, 96) > 1
    tail = Q(1, 2)**2 / (2 * Q(5, 3))
    assert tail == Q(3, 40)
    for m in range(8, 10001):
        r = m // 8
        assert 16 * r >= m and 8 * r <= m
    # Independently exhaust the two possible label counts, including remainders.
    count = 0
    for m in range(8, 41):
        r = m // 8
        for n in [m*(2*r+1), m*(2*r+1)+1, m*(2*r+2)-1]:
            for nplus in range(n+1):
                nminus = n-nplus
                full = nplus//m + nminus//m
                width = (nplus+m-1)//m + (nminus+m-1)//m
                assert full >= 2*r
                assert Q(n, m) <= width < Q(n, m)+2
                count += 1
    return {"normalized_gram": [str(lo), str(hi)],
            "selected_gram": [str(selected_lo), str(selected_hi)],
            "max_x0_squared": str(xnorm_at_largest_r),
            "tangent_coefficient_exact": str(slope_exact),
            "tangent_coefficient_rounded": str(slope_rounded),
            "spherical_tail_coefficient": str(tail),
            "label_count_checks": count}


def orthogonal_checks():
    results = []
    for m in [2, 3, 8, 16, 32]:
        for k in sorted({1, 2*m-1, 2*m, 4*m-1, 4*m, 4*m+1, 8*m}):
            # Enumeration derives the largest feasible count without the formula.
            feasible = [a for a in range(k+1) if Q(a, 4*m) < 1]
            a = max(feasible)
            claimed = 2*math.sqrt(m*min(k, 4*m-1))
            enumerated = math.sqrt(sum(4*m for _ in range(a)))
            assert claimed == enumerated
            threshold = 1/(2*math.sqrt(m))
            c = (threshold + 1/math.sqrt(a))/2
            point = np.zeros(k+1)
            point[:a] = c
            assert np.linalg.norm(point) < 1
            signs = np.array([1 if j % 2 else -1 for j in range(k)])
            grad = np.zeros(k+1)
            grad[:a] = 2*math.sqrt(m)*signs[:a]

            def f(x):
                return float(2*math.sqrt(m)*np.dot(signs, np.maximum(x[:k]-threshold, 0)))

            direction = grad/np.linalg.norm(grad)
            h = min(1e-5, (1-np.linalg.norm(point))/4,
                    (c-threshold)/4)
            secant = abs(f(point+h*direction)-f(point-h*direction))/(2*h)
            assert math.isclose(secant, claimed, rel_tol=2e-8)
            row = {"m": m, "K": k, "max_active": a,
                   "ball_formula": claimed, "ball_secant": secant}
            if k >= 2*m:
                # All-positive signs are permitted; use the first m groups.
                eps = 1e-4
                p = np.zeros(k+1)
                p[:m] = (0.5+eps)/math.sqrt(m)
                p[-1] = math.sqrt(1-(0.5+eps)**2)
                g = np.zeros(k+1)
                g[:m] = 2*math.sqrt(m)
                tangent = g-np.dot(g, p)*p
                tangent_norm = float(np.linalg.norm(tangent))
                by_identity = m*math.sqrt(4-(1+2*eps)**2)
                assert math.isclose(tangent_norm, by_identity, rel_tol=1e-13)

                def fp(x):
                    return float(2*math.sqrt(m)*np.sum(np.maximum(x[:k]-threshold, 0)))

                v = tangent/tangent_norm
                h = 1e-6
                plus, minus = math.cos(h)*p+math.sin(h)*v, math.cos(h)*p-math.sin(h)*v
                sec = abs(fp(plus)-fp(minus))/float(np.linalg.norm(plus-minus))
                assert math.isclose(sec, tangent_norm, rel_tol=2e-8)
                row.update(sphere_tangent=tangent_norm, sphere_secant=sec,
                           limiting_lower=math.sqrt(3)*m)
            results.append(row)
    return results


def random_case(m, n, d, seed):
    rng = np.random.default_rng(seed)
    labels = rng.choice([-1, 1], size=n)
    groups, signs = [], []
    for sign in [-1, 1]:
        indices = np.flatnonzero(labels == sign)
        for start in range(0, len(indices), m):
            groups.append(indices[start:start+m])
            signs.append(sign)
    signs = np.array(signs)
    k, r = len(groups), m//8
    # The only large allocation is X; worst case here is about 154 MB.
    assert n*d*8 < 200_000_000
    X = rng.standard_normal((n, d))
    X /= np.linalg.norm(X, axis=1)[:, None]
    normals = np.empty((k, d))
    group_eigenvalues = []
    for j, indices in enumerate(groups):
        block = X[indices]
        gram = block @ block.T
        eig = np.linalg.eigvalsh(gram)
        group_eigenvalues.extend([float(eig[0]), float(eig[-1])])
        normals[j] = np.linalg.solve(gram, np.ones(len(indices))) @ block
    assert min(group_eigenvalues) >= 3/5 and max(group_eigenvalues) <= 5/3
    full = np.array([len(g) == m for g in groups])
    chosen_sign = max([-1, 1], key=lambda s: np.count_nonzero(full & (signs == s)))
    chosen = np.flatnonzero(full & (signs == chosen_sign))[:r]
    assert len(chosen) == r
    W = normals[chosen]
    gram = W @ W.T
    eig = np.linalg.eigvalsh(gram)
    assert eig[0] >= m/3 and eig[-1] <= 3*m
    x0 = W.T @ np.linalg.solve(gram, np.full(r, 3/4))
    z = np.zeros(d)
    z[0] = 1
    z -= W.T @ np.linalg.solve(gram, W[:, 0])
    z /= np.linalg.norm(z)
    witness = x0 + math.sqrt(1-float(np.dot(x0, x0))) * z
    assert abs(float(np.linalg.norm(witness))-1) < 1e-12
    act = normals @ witness
    active = np.flatnonzero(act > 1/2)
    assert np.array_equal(active, chosen)
    values = 2*np.maximum(X @ normals.T-1/2, 0) @ signs
    interpolation_error = float(np.max(np.abs(values-labels)))
    assert interpolation_error < 1e-10
    gradient = 2*normals[active].T @ signs[active]
    tangent = gradient-np.dot(gradient, witness)*witness
    slope = float(np.linalg.norm(tangent))
    assert slope >= math.sqrt(m*r) >= m/4

    def f(x):
        return float(2*np.dot(signs, np.maximum(normals@x-1/2, 0)))

    v = tangent/slope
    secants = []
    for h in [1e-4, 1e-5]:
        plus = math.cos(h)*witness+math.sin(h)*v
        minus = math.cos(h)*witness-math.sin(h)*v
        sec = abs(f(plus)-f(minus))/float(np.linalg.norm(plus-minus))
        assert math.isclose(sec, slope, rel_tol=1e-8)
        secants.append(sec)
    failure_bound = (2*(k+1)*math.exp(m*math.log(9)-d/512)
                     + 2*k*(n+1)*math.exp(-3*d/(40*m)))
    delta = 0.05
    sufficient_d = max(512*(m*math.log(9)+math.log(4*(k+1)/delta)),
                       40*m/3*math.log(4*k*(n+1)/delta))
    assert d >= sufficient_d and failure_bound <= delta
    return {"seed": seed, "m": m, "n": n, "d": d, "K": k, "r": r,
            "group_sizes": [len(g) for g in groups], "group_signs": signs.tolist(),
            "selected_groups": chosen.tolist(),
            "group_gram_min": min(group_eigenvalues),
            "group_gram_max": max(group_eigenvalues),
            "selected_gram_eigen_min": float(eig[0]),
            "selected_gram_eigen_max": float(eig[-1]),
            "x0_squared_norm": float(np.dot(x0, x0)),
            "max_interpolation_error": interpolation_error,
            "witness_preactivations": act.tolist(),
            "gradient_squared": float(np.dot(gradient, gradient)),
            "radial_squared": float(np.dot(gradient, witness)**2),
            "tangent_norm": slope, "network_chord_secants": secants,
            "proved_lower": m/4, "desired_scale": math.sqrt(n/k),
            "failure_probability_bound": failure_bound,
            "sufficient_dimension_for_delta_005": math.ceil(sufficient_d)}


def peak_working_set():
    if os.name != "nt":
        return None
    class Counters(ctypes.Structure):
        _fields_ = [("cb", ctypes.c_ulong), ("PageFaultCount", ctypes.c_ulong),
                    ("PeakWorkingSetSize", ctypes.c_size_t),
                    ("WorkingSetSize", ctypes.c_size_t),
                    ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                    ("PagefileUsage", ctypes.c_size_t),
                    ("PeakPagefileUsage", ctypes.c_size_t)]
    counters = Counters()
    counters.cb = ctypes.sizeof(counters)
    psapi = ctypes.WinDLL("psapi", use_last_error=True)
    psapi.GetProcessMemoryInfo.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong]
    assert psapi.GetProcessMemoryInfo(kernel32.GetCurrentProcess(), ctypes.byref(counters), counters.cb)
    return counters.PeakWorkingSetSize


def main():
    started = time.monotonic()
    output = {"exact_constants": exact_constants(),
              "orthogonal_cases": orthogonal_checks(), "random_cases": []}
    for m, n, d, seed in [(8, 80, 20000, 34308),
                          (16, 256, 40000, 34316),
                          (32, 320, 60000, 34332)]:
        row = random_case(m, n, d, seed)
        output["random_cases"].append(row)
        print("random m={m} n={n} d={d} K={K}: error={max_interpolation_error:.3g}, "
              "slope={tangent_norm:.9f}, lower={proved_lower:.3f}, "
              "desired={desired_scale:.6f}, failure<={failure_probability_bound:.3g}".format(**row),
              flush=True)
    output["elapsed_seconds"] = time.monotonic()-started
    output["peak_working_set_bytes"] = peak_working_set()
    assert output["elapsed_seconds"] < 1200
    if output["peak_working_set_bytes"] is not None:
        assert output["peak_working_set_bytes"] < 1_000_000_000
    path = Path(__file__).resolve().parent / "verification_data.json"
    path.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print("PASS: exact constants;", len(output["orthogonal_cases"]),
          "orthogonal cases;", output["exact_constants"]["label_count_checks"],
          "label-count cases; 3 random cases", flush=True)
    print("elapsed_seconds={:.3f} peak_working_set_bytes={}".format(
        output["elapsed_seconds"], output["peak_working_set_bytes"]), flush=True)
    print("data: verification_data.json", flush=True)


if __name__ == "__main__":
    main()
