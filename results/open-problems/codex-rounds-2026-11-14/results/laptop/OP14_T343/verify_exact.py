"""Verify Section 7 via a separate trigonometric calculation and network values.

Run: python -B verify_exact.py
No training or optimization. Writes exact_sphere_data.json beside this file.
"""
import os
for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"
import ctypes
import json
import math
from pathlib import Path
import time
if os.name == "nt":
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.GetCurrentProcess.restype = ctypes.c_void_p
    kernel32.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    assert kernel32.SetPriorityClass(kernel32.GetCurrentProcess(), 0x4000)
import numpy as np
from verify import peak_working_set


def formula(m, p, q):
    P, Q = max(p, q), min(p, q)
    penalty = max(0.0, P-math.sqrt(Q*(4*m-P)))
    return 4*m*(p+q)-penalty**2


def circle_calculation(m, p, q):
    # Independently parameterize the boundary U^2/P + V^2/Q = 1.
    P, Q = max(p, q), min(p, q)
    a = 1/(2*math.sqrt(m))
    if Q == 0:
        smallest_sum = P*a
    else:
        low = math.asin(math.sqrt(Q)*a)
        high = math.acos(math.sqrt(P)*a)
        assert low <= high+1e-14
        angle_of_equal_sums = math.atan2(math.sqrt(P), math.sqrt(Q))
        theta = max(low, min(high, angle_of_equal_sums))
        smallest_sum = abs(math.sqrt(P)*math.cos(theta)-math.sqrt(Q)*math.sin(theta))
    return 4*m*(p+q)-4*m*smallest_sum**2


def best(m, kp, km):
    choices = [(formula(m, p, q), p, q)
               for p in range(kp+1) for q in range(km+1)
               if 1 <= p+q < 4*m]
    return max(choices)


def actual_network_witness(m, kp, km):
    squared, p, q = best(m, kp, km)
    a, k, r = 1/(2*math.sqrt(m)), kp+km, p+q
    positive = list(range(p))
    negative = list(range(kp, kp+q))
    if p >= q:
        major, minor = positive, negative
    else:
        major, minor = negative, positive
    P, Q = len(major), len(minor)
    tstar = np.zeros(k)
    tstar[major] = a
    if Q:
        tstar[minor] = min(P*a/Q, math.sqrt((1-P*a*a)/Q))
    selected = np.array(sorted(positive+negative))
    b = (a+1/math.sqrt(r))/2
    blend = 1e-4
    coords = tstar.copy()
    coords[selected] = (1-blend)*coords[selected]+blend*b
    assert float(np.dot(coords, coords)) < 1
    x = np.append(coords, math.sqrt(1-float(np.dot(coords, coords))))
    signs = np.array([1]*kp+[-1]*km)
    g = np.zeros(k+1)
    g[selected] = 2*math.sqrt(m)*signs[selected]
    tangent = g-float(np.dot(g, x))*x
    slope = float(np.linalg.norm(tangent))
    exact = math.sqrt(squared)
    assert 0.99*exact < slope <= exact+1e-10
    assert np.array_equal(np.flatnonzero(x[:k] > a), selected)
    v = tangent/slope

    def f(z):
        return float(2*math.sqrt(m)*np.dot(signs, np.maximum(z[:k]-a, 0)))

    margin = min(coords[selected]-a)
    h = min(1e-6, float(margin)/8)
    plus, minus = math.cos(h)*x+math.sin(h)*v, math.cos(h)*x-math.sin(h)*v
    secant = abs(f(plus)-f(minus))/float(np.linalg.norm(plus-minus))
    assert math.isclose(secant, slope, rel_tol=1e-5)
    return {"m": m, "K_plus": kp, "K_minus": km,
            "maximizing_p": p, "maximizing_q": q,
            "exact_geodesic_squared": squared, "exact_geodesic": exact,
            "witness_tangent": slope, "network_chord_secant": secant,
            "ball_lipschitz": 2*math.sqrt(m*min(k, 4*m-1)),
            "chord_upper": min(math.pi/2*exact, 2*math.sqrt(m*min(k, 4*m-1))),
            "witness_active_coords": coords[selected].tolist(),
            "witness_complement_coord": float(x[-1]), "secant_step": h}


def main():
    start = time.monotonic()
    pair_checks, max_error = 0, 0.0
    sweep = []
    for m in [2, 3, 4, 8]:
        for kp in range(13):
            for km in range(13):
                if kp+km == 0:
                    continue
                independent = []
                for p in range(kp+1):
                    for q in range(km+1):
                        if not 1 <= p+q < 4*m:
                            continue
                        analytic = formula(m, p, q)
                        trigonometric = circle_calculation(m, p, q)
                        error = abs(analytic-trigonometric)
                        max_error = max(max_error, error)
                        assert error < 1e-10
                        pair_checks += 1
                        independent.append(trigonometric)
                squared, p, q = best(m, kp, km)
                assert math.isclose(squared, max(independent), abs_tol=1e-10)
                sweep.append({"m": m, "K_plus": kp, "K_minus": km,
                              "L_geodesic_squared": squared, "p": p, "q": q})
    closed_checks = 0
    for m in range(2, 41):
        for k in [1, m, 2*m-1, 2*m, 4*m-1, 4*m, 8*m]:
            s = min(k, 2*m)
            assert math.isclose(best(m, k, 0)[0], 4*m*s-s*s, abs_tol=1e-10)
            assert math.isclose(best(m, 0, k)[0], 4*m*s-s*s, abs_tol=1e-10)
            closed_checks += 2
        expected = 4*m*(4*m-1)-(2*m-math.sqrt(2*m*(2*m-1)))**2
        for kp, km in [(2*m, 2*m-1), (2*m-1, 2*m), (2*m, 2*m), (3*m, 4*m)]:
            assert math.isclose(best(m, kp, km)[0], expected, abs_tol=1e-10)
            closed_checks += 1
    witnesses = []
    for m in [2, 3, 8]:
        for kp, km in [(1, 0), (4*m, 0), (0, 4*m), (2*m, 2*m-1),
                       (2*m, 2*m), (1, 8), (8, 1), (7, 7)]:
            witnesses.append(actual_network_witness(m, kp, km))
    peak = peak_working_set()
    elapsed = time.monotonic()-start
    assert elapsed < 1200
    assert peak is None or peak < 1_000_000_000
    output = {"pair_checks": pair_checks, "sign_count_cases": len(sweep),
              "max_independent_squared_error": max_error,
              "closed_form_checks": closed_checks,
              "network_witnesses": witnesses, "sign_count_sweep": sweep,
              "elapsed_seconds": elapsed, "peak_working_set_bytes": peak}
    Path(__file__).resolve().with_name("exact_sphere_data.json").write_text(
        json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print(f"PASS: {pair_checks} pair checks across {len(sweep)} sign-count cases; "
          f"max independent squared error={max_error:.3g}")
    print(f"PASS: {closed_checks} closed-form checks; {len(witnesses)} actual network chord witnesses")
    for row in witnesses:
        if row["m"] == 8 and (row["K_plus"], row["K_minus"]) in [(32, 0), (16, 15)]:
            print("m={m} K_plus={K_plus} K_minus={K_minus}: exact_geodesic={exact_geodesic:.9f}, "
                  "network_secant={network_chord_secant:.9f}, ball={ball_lipschitz:.9f}".format(**row))
    print(f"elapsed_seconds={elapsed:.3f} peak_working_set_bytes={peak}")
    print("data: exact_sphere_data.json")


if __name__ == "__main__":
    main()
