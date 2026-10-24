import itertools, json, math
import numpy as np

C_CHI = 2 + 1/(math.sqrt(math.e)*math.log(2))
SEED = 20260920


def fwht(vals):
    a = np.array(vals, dtype=float).copy()
    n = len(a)
    h = 1
    while h < n:
        for s in range(0, n, 2*h):
            x = a[s:s+h].copy()
            y = a[s+h:s+2*h].copy()
            a[s:s+h] = x + y
            a[s+h:s+2*h] = x - y
        h *= 2
    return a / n


def total_influence(vals):
    vals = np.asarray(vals)
    N = len(vals)
    n = int(round(math.log2(N)))
    ids = np.arange(N)
    return sum(float(np.mean(vals != vals[ids ^ (1 << j)])) for j in range(n))


def local_B(g, h):
    a, b = fwht(g), fwht(h)
    p0 = (a+b)**2 / 4
    p1 = (a-b)**2 / 4
    q = p0 + p1
    out = 0.0
    for x, y, s in zip(p0, p1, q):
        if s <= 1e-15:
            continue
        t = y/s
        if 1e-15 < t < 1-1e-15:
            out += s * (-t*math.log2(t) - (1-t)*math.log2(1-t))
    return out


def check_pair(g, h):
    B = local_B(g, h)
    delta = float(np.mean(np.asarray(g) != np.asarray(h)))
    j = min(delta, 1-delta)
    Ig, Ih = total_influence(g), total_influence(h)
    rhs = C_CHI*j + min(Ig, Ih)
    return {
        "B": B, "delta": delta, "j": j,
        "I_plus": Ig, "I_minus": Ih,
        "rhs": rhs, "violation": B-rhs,
    }


def exhaustive(dim):
    N = 2**dim
    funcs = [np.array([1 if (mask >> k) & 1 else -1 for k in range(N)], dtype=int)
             for mask in range(2**N)]
    mx = -1e100
    worst = None
    count = 0
    for ia, g in enumerate(funcs):
        for ib, h in enumerate(funcs):
            rec = check_pair(g, h)
            count += 1
            if rec["violation"] > mx:
                mx = rec["violation"]
                worst = {"plus_index": ia, "minus_index": ib, **rec}
    return {"pairs": count, "max_violation": mx, "worst": worst}


def sampled(dim, count, rng):
    N = 2**dim
    mx = -1e100
    worst = None
    for t in range(count):
        g = rng.choice([-1, 1], size=N)
        if t % 3 == 0:
            h = g.copy()
            k = int(rng.integers(1, max(2, N//4)))
            idx = rng.choice(N, size=k, replace=False)
            h[idx] *= -1
        elif t % 3 == 1:
            h = rng.choice([-1, 1], size=N)
        else:
            h = -g.copy()
            k = int(rng.integers(0, max(1, N//8)))
            if k:
                idx = rng.choice(N, size=k, replace=False)
                h[idx] *= -1
        rec = check_pair(g, h)
        if rec["violation"] > mx:
            mx = rec["violation"]
            worst = {"sample": t, **rec}
    return {"pairs": count, "max_violation": mx, "worst": worst}


def main():
    rng = np.random.default_rng(SEED)
    out = {
        "status": "PASS",
        "theorem": "B_i(f) <= C_chi*j_i(f) + min(I(f+),I(f-))",
        "C_chi": C_CHI,
        "seed": SEED,
        "exhaustive": {},
        "sampled": {},
    }
    global_max = -1e100
    for d in range(4):
        rec = exhaustive(d)
        out["exhaustive"][f"child_dim_{d}"] = rec
        global_max = max(global_max, rec["max_violation"])
    for d in range(4, 9):
        rec = sampled(d, 5000, rng)
        out["sampled"][f"child_dim_{d}"] = rec
        global_max = max(global_max, rec["max_violation"])
    out["global_max_violation"] = global_max
    if global_max > 1e-10:
        out["status"] = "FAIL"
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
