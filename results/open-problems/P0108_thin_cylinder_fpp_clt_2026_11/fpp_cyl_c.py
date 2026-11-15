"""P0108 numerics: first-passage percolation across a thin cylinder (Z_W x {0..n-1}), iid Exp(1) site weights.
T = min over paths from the column x=0 to the column x=n-1 of the summed site weights (both ends included).
Question (ADH Q20): for which widths W = n^a does T satisfy a CLT? Conjecturally a < 2/3 in two dimensions.
Diagnostic: standardized skewness and excess kurtosis of T per (n, a); they go to 0 inside the CLT range.
Solver: Bellman-Ford relaxation on the GPU (MLX), a batch of B independent cylinders at once, run to its fixed point.
Rows: one JSON line per batch with the raw T values, so moments are combined exactly later. Stops on ./STOP or budget.
"""
import sys, os, json, time, math
import mlx.core as mx

OUT = sys.argv[1] if len(sys.argv) > 1 else "fpp_rows.jsonl"
BUDGET = float(sys.argv[2]) if len(sys.argv) > 2 else 6 * 3600.0
CS = [float(x) for x in os.environ.get("FPP_CS", "").split(",") if x]
NS = [int(x) for x in os.environ.get("FPP_NS", "256,512,1024,2048").split(",")]
AS = [float(x) for x in os.environ.get("FPP_AS", "0.33,0.5,0.6,0.667,0.75,0.85,1.0").split(",")]
ELEMS = int(os.environ.get("FPP_ELEMS", str(24 * 1024 * 1024)))  # elements per batch array (float32: 4 bytes each); a handful live at once
INF = float("inf")


def relax(D, w):
    up = mx.roll(D, 1, axis=1)
    dn = mx.roll(D, -1, axis=1)
    B, W, n = D.shape
    pad = mx.full((B, W, 1), INF, dtype=mx.float32)
    left = mx.concatenate([pad, D[:, :, :-1]], axis=2)
    right = mx.concatenate([D[:, :, 1:], pad], axis=2)
    nb = mx.minimum(mx.minimum(up, dn), mx.minimum(left, right))
    return mx.minimum(D, nb + w)


relax_c = mx.compile(relax)


def one_batch(B, W, n, key):
    u = mx.random.uniform(low=1e-12, high=1.0, shape=(B, W, n), key=key)
    w = -mx.log(u)
    D = mx.full((B, W, n), INF, dtype=mx.float32)
    D = mx.concatenate([w[:, :, :1], D[:, :, 1:]], axis=2)
    it = 0
    cap = 30 * n + 1000
    while it < cap:
        prev = D
        for _ in range(64):
            D = relax_c(D, w)
        it += 64
        same = mx.all(D == prev)
        mx.eval(D, same)
        if bool(same.item()):
            break
    T = mx.min(D[:, :, -1], axis=1)
    mx.eval(T)
    return [round(float(x), 5) for x in T.tolist()], it, it >= cap


def main():
    configs = []
    for n in NS:
        for a in (CS if CS else AS):
            # FPP_CS set: widths W = c * n^(2/3) (the KPZ transversal scale); a then holds c
            W = max(3, int(round(a * n ** (2.0 / 3.0)))) if CS else max(3, int(round(n ** a)))
            B = int(max(4, min(512, ELEMS // (W * n))))
            configs.append((n, a, W, B))
    t0 = time.time()
    seed = int(time.time()) % 100000
    k = 0
    with open(OUT, "a") as f:
        while time.time() - t0 < BUDGET and not os.path.exists("STOP"):
            for (n, a, W, B) in configs:
                if time.time() - t0 >= BUDGET or os.path.exists("STOP"):
                    break
                key = mx.random.key(seed * 1000003 + k)
                k += 1
                s = time.time()
                T, it, capped = one_batch(B, W, n, key)
                f.write(json.dumps({"n": n, "a": (round(math.log(W) / math.log(n), 4) if CS else a), "c": (a if CS else None), "W": W, "B": B, "iters": it, "capped": capped,
                                    "secs": round(time.time() - s, 2), "seed": seed, "k": k, "T": T}) + "\n")
                f.flush()


if __name__ == "__main__":
    main()
