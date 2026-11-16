"""Numerical checks for the FA-1f paper (not part of any proof).

1. drift: the generator inequality of Lemma 3.1,
       L theta^{D_x} <= -lambda theta^{D_x} + b,
   checked in floating point on every configuration of a window of n sites whose exterior is frozen infected
   (the finite-volume chains used in the proof of the lemma), for several q > 1/2.
2. seed: exact continuous-time simulation from a single infection at the origin; the estimated
   P(eta_0(t) = 0) and P(eta_{-1} = eta_0 = eta_1 = 1) are compared with their equilibrium values q and p^3.

Spin 0 is an infection, spin 1 is healthy, p = 1 - q. Pure Python 3, no dependencies.
Run from the repository root:  python code/checks.py   (about a minute; writes data/checks.json).
"""
import itertools
import json
import math
import os
import random


def dist_to_zero(conf, x):
    # conf is a tuple over window sites 0..n-1; sites -1 and n are frozen zeros
    n = len(conf)
    best = min(x + 1, n - x)
    for y in range(n):
        if conf[y] == 0:
            best = min(best, abs(x - y))
    return best


def drift_check(n, q, theta):
    p = 1.0 - q
    lam = (theta - 1.0) * (q / theta - p)
    b = q * (theta - 1.0) / theta
    worst = -math.inf
    for conf in itertools.product((0, 1), repeat=n):
        for x in range(n):
            d0 = dist_to_zero(conf, x)
            gen = 0.0
            for y in range(n):
                left = conf[y - 1] if y > 0 else 0
                right = conf[y + 1] if y < n - 1 else 0
                if left * right == 1:
                    continue  # constraint not satisfied
                new = 0 if conf[y] == 1 else 1
                rate = q if new == 0 else p
                c2 = list(conf)
                c2[y] = new
                gen += rate * (theta ** dist_to_zero(c2, x) - theta ** d0)
            slack = gen - (-lam * theta ** d0 + b)
            worst = max(worst, slack)
    return worst


def simulate_seed(q, L, T, times, rng):
    """One path on {-L..L} with healthy exterior, single infection at 0. Returns observables at given times."""
    p = 1.0 - q
    size = 2 * L + 1
    eta = [1] * size
    eta[L] = 0
    # active sets: facilitated healthy sites (flip at rate q) and facilitated infected sites (flip at rate p)
    act = [[], []]          # act[0]: infected facilitated, act[1]: healthy facilitated
    pos = [-1] * size

    def facilitated(i):
        l = eta[i - 1] if i > 0 else 1
        r = eta[i + 1] if i < size - 1 else 1
        return l == 0 or r == 0

    def refresh(i):
        if i < 0 or i >= size:
            return
        want = facilitated(i)
        if pos[i] >= 0:
            lst = act[cur[i]]
            j = pos[i]
            last = lst.pop()
            if last != i:
                lst[j] = last
                pos[last] = j
            pos[i] = -1
        if want:
            cur[i] = eta[i]
            act[eta[i]].append(i)
            pos[i] = len(act[eta[i]]) - 1

    cur = [0] * size
    for i in (L - 1, L, L + 1):
        refresh(i)
    t = 0.0
    out = []
    k = 0
    while k < len(times):
        r0 = p * len(act[0])
        r1 = q * len(act[1])
        total = r0 + r1
        dt = rng.expovariate(total)
        while k < len(times) and t + dt > times[k]:
            out.append((1 if eta[L] == 0 else 0, 1 if (eta[L - 1] and eta[L] and eta[L + 1]) else 0))
            k += 1
        if k >= len(times):
            break
        t += dt
        if rng.random() * total < r0:
            i = act[0][rng.randrange(len(act[0]))]
        else:
            i = act[1][rng.randrange(len(act[1]))]
        eta[i] = 1 - eta[i]
        for j in (i - 1, i, i + 1):
            refresh(j)
        if eta[0] == 0 or eta[size - 1] == 0:
            raise RuntimeError("infection reached the boundary; enlarge L")
    return out


def main():
    res = {"drift": [], "seed": []}
    for q in (0.55, 0.6, 0.75, 0.9):
        theta = math.sqrt(q / (1.0 - q))
        for n in (6, 9, 12):
            w = drift_check(n, q, theta)
            res["drift"].append({"q": q, "theta": theta, "n": n, "max_slack": w})
            print(f"drift q={q} n={n} max(L theta^D - (-lambda theta^D + b)) = {w:.3e}")
    rng = random.Random(20261113)
    for q, T in ((0.6, 120.0), (0.75, 80.0)):
        times = [T * j / 8 for j in range(1, 9)]
        L = int(1.2 * q * T) + 40
        paths = 300
        acc = [[0, 0] for _ in times]
        for _ in range(paths):
            for j, (a, b) in enumerate(simulate_seed(q, L, T, times, rng)):
                acc[j][0] += a
                acc[j][1] += b
        p = 1.0 - q
        for j, t in enumerate(times):
            m0 = acc[j][0] / paths
            m1 = acc[j][1] / paths
            row = {"q": q, "t": t, "paths": paths, "P_infected_0": m0, "se0": math.sqrt(m0 * (1 - m0) / paths),
                   "equilibrium_q": q, "P_healthy_-1_0_1": m1, "se1": math.sqrt(m1 * (1 - m1) / paths),
                   "equilibrium_p3": p ** 3}
            res["seed"].append(row)
            print(f"seed q={q} t={t:6.1f} P(eta0=0)={m0:.3f}+-{row['se0']:.3f} (q={q})  "
                  f"P(111)={m1:.3f}+-{row['se1']:.3f} (p^3={p**3:.3f})")
    os.makedirs("data", exist_ok=True)
    with open(os.path.join("data", "checks.json"), "w") as fh:
        json.dump(res, fh, indent=1)


if __name__ == "__main__":
    main()
