"""Two or more coordinates of each sign: A = x_1 x_2 >= 0, B = x_n x_(n-1) >= 0, m T = max(A, B) >=
(A^(p+1) + B^(p+1)) / (A^p + B^p).  Psi_p := Psi with m replaced by that bound.  Is Psi_p >= 0 on the cone
K = {sorted, sum 0, x_2 >= 0 >= x_(n-1)}?  Random and few-valued samples plus a crude local search, n = 5..40.
an agent, 11 Nov 2026."""
import random

def psis(x):
    n = len(x)
    xs = sorted(x, reverse=True)
    T = sum(v * v for v in xs)
    q = sum(v**4 for v in xs) / T**2
    p3 = sum(v**3 for v in xs) ** 2 / T**3
    A, B = xs[0] * xs[1], xs[-1] * xs[-2]
    base = (n - 4) * (2 * q - 1) - 2 * (n - 3) * p3
    C = (n - 1) * (n * n - 6 * n + 6 + 2 * n * q)
    out = [base + C * max(A, B) / T]
    for p in (0, 1, 2, 4):
        if A + B <= 0:
            out.append(base)
        else:
            out.append(base + C * (A ** (p + 1) + B ** (p + 1)) / (A**p + B**p) / T)
    return out

def make(rnd, n):
    p = rnd.randint(2, n - 2)
    def side(k):
        mode = rnd.randint(0, 4)
        if mode == 0:
            return [rnd.random() for _ in range(k)]
        if mode == 1:
            return [rnd.random() ** 6 for _ in range(k)]
        if mode == 2:
            vals = [rnd.random() for _ in range(rnd.randint(1, 2))]
            return [rnd.choice(vals) for _ in range(k)]
        if mode == 3:
            big = rnd.random() * 20
            return [big] + [rnd.random() ** 3 for _ in range(k - 1)]
        big = rnd.random() * 20
        return [big, big * rnd.random()] + [rnd.random() ** 3 * rnd.choice([0, 1]) for _ in range(k - 2)]
    a, b = side(p), side(n - p)
    sa, sb = sum(a), sum(b)
    if sa <= 0 or sb <= 0:
        return None
    return [v / sa for v in a] + [-v / sb for v in b]

def project(x, n):
    # keep sum zero and at least two of each sign
    s = sum(x) / n
    x = [v - s for v in x]
    pos = sum(1 for v in x if v > 0)
    neg = sum(1 for v in x if v < 0)
    return x if pos >= 2 and neg >= 2 else None

rnd = random.Random(77)
names = ["true", "p=0", "p=1", "p=2", "p=4"]
for n in (5, 6, 8, 10, 12, 14, 16, 20, 30, 40):
    mins = [None] * 5
    arg = [None] * 5
    for trial in range(30000):
        x = make(rnd, n)
        if x is None:
            continue
        v = psis(x)
        for i in range(5):
            if mins[i] is None or v[i] < mins[i]:
                mins[i], arg[i] = v[i], x
    # crude local search on each bound from its best sample
    for i in range(5):
        x, best = arg[i][:], mins[i]
        step = 0.05
        for it in range(6000):
            y = x[:]
            k = rnd.randrange(n)
            l = rnd.randrange(n)
            d = step * rnd.gauss(0, 1) * max(abs(v) for v in x)
            y[k] += d
            y[l] -= d
            y = project(y, n)
            if y is None:
                continue
            val = psis(y)[i]
            if val < best:
                x, best = y, val
            elif it % 500 == 499:
                step *= 0.6
        mins[i], arg[i] = best, x
    print(f"n={n}: least " + "  ".join(f"{names[i]} {mins[i]:.5g}" for i in range(5)), flush=True)
    for i in (2, 3):
        if mins[i] < -1e-9:
            xs = sorted(arg[i], reverse=True)
            sc = max(abs(v) for v in xs)
            print(f"   {names[i]} negative at", [round(v / sc, 3) for v in xs][:16])
