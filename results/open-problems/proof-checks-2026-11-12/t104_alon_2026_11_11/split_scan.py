"""Polyhedral split for m.  WLOG x sorted decreasing, sum 0, x_1 + x_n >= 0 (else negate).
R1 = {x_2 + x_(n-1) >= 0}: there x_1 x_2 >= x_n x_(n-1), so m T = A = x_1 x_2 (if x_2 >= 0).
R2 = {x_2 + x_(n-1) <= 0}: test whether Psi_B (m replaced by B/T, B = x_n x_(n-1)) is >= 0 on all of R2.
Random samples + local search minimising Psi_B inside R2.  an agent, 11 Nov 2026."""
import random

def parts(xs):
    n = len(xs)
    T = sum(v * v for v in xs)
    q = sum(v**4 for v in xs) / T**2
    p3 = sum(v**3 for v in xs) ** 2 / T**3
    base = (n - 4) * (2 * q - 1) - 2 * (n - 3) * p3
    C = (n - 1) * (n * n - 6 * n + 6 + 2 * n * q)
    A, B = xs[0] * xs[1], xs[-1] * xs[-2]
    return base, C, A / T, B / T

def norm(x):
    n = len(x)
    s = sum(x) / n
    xs = sorted((v - s for v in x), reverse=True)
    if xs[0] + xs[-1] < 0:
        xs = sorted((-v for v in xs), reverse=True)
    return xs

def inR2(xs):
    return xs[1] + xs[-2] <= 0

def sample(rnd, n):
    mode = rnd.randint(0, 5)
    if mode == 0:
        x = [rnd.gauss(0, 1) for _ in range(n)]
    elif mode == 1:
        x = [rnd.gauss(0, 1) ** 3 for _ in range(n)]
    elif mode == 2:  # star-like with extra positives
        x = [1.0] + [rnd.random() * rnd.choice([0.01, 0.1, 0.5]) for _ in range(rnd.randint(1, 3))]
        x += [-rnd.random() * rnd.choice([0.05, 0.3, 1]) for _ in range(n - len(x))]
    elif mode == 3:  # edge-like
        x = [1.0, -1.0 * rnd.random()] + [rnd.gauss(0, 1) * rnd.choice([0.01, 0.1, 0.3]) for _ in range(n - 2)]
    elif mode == 4:  # few values
        vals = [rnd.gauss(0, 1) for _ in range(rnd.randint(2, 4))]
        x = [rnd.choice(vals) for _ in range(n)]
    else:
        k = rnd.randint(1, n - 1)
        x = [rnd.random() for _ in range(k)] + [-rnd.random() for _ in range(n - k)]
    return x

rnd = random.Random(314)
for n in (5, 6, 7, 8, 10, 12, 14, 17, 20, 30, 40, 60):
    cnt = r2 = a_bigger = 0
    best = None
    best_true = None
    for _ in range(40000):
        xs = norm(sample(rnd, n))
        if xs[0] <= 0:
            continue
        cnt += 1
        base, C, a, b = parts(xs)
        tv = base + C * max(a, b)
        if best_true is None or tv < best_true:
            best_true = tv
        if not inR2(xs):
            continue
        r2 += 1
        if a > b:
            a_bigger += 1
        v = base + C * b
        if best is None or v < best[0]:
            best = (v, xs, a, b)
    v, x, a, b = best
    step = 0.05
    for it in range(20000):
        y = x[:]
        k, l = rnd.randrange(n), rnd.randrange(n)
        d = step * rnd.gauss(0, 1) * x[0]
        y[k] += d
        y[l] -= d
        ys = norm(y)
        if not inR2(ys):
            continue
        base, C, a2, b2 = parts(ys)
        val = base + C * b2
        if val < v:
            v, x, a, b = val, ys, a2, b2
        elif it % 1000 == 999:
            step *= 0.7
    sc = x[0]
    print(f"n={n}: samples {cnt}, in R2 {r2} (A > B in {a_bigger}); least true Psi {best_true:.4g}; least Psi_B on R2 after search {v:.6g} (A/B there {a / b if b else float('inf'):.3g})", flush=True)
    if v < -1e-9:
        print("    at", [round(t / sc, 4) for t in x][:10], "...", [round(t / sc, 4) for t in x][-4:])
