"""P0108 numerics, Metal-kernel solver: same model and output rows as fpp_cyl_c.py (site FPP with Exp(1) weights on the
cylinder Z_W x {0..n-1}, T = min passage time from column 0 to column n-1, widths W = n^a or W = c n^(2/3)).
The relaxation step D <- min(D, min(four neighbours) + w) is one mx.fast.metal_kernel instead of four rolls, two
concatenations and three minimums: the same floating-point operations in the same order, so the fixed point and T are
bit-identical, with far fewer temporaries alive (a roll step held about 20 arrays at once on MLX 0.29).
  python fpp_cyl_k.py --selftest        compare against the roll version on small cylinders (exact equality)
  python fpp_cyl_k.py OUT.jsonl SECONDS  run, env FPP_NS, FPP_CS or FPP_AS, FPP_ELEMS as in fpp_cyl_c.py
"""
import sys, os, json, time, math
import mlx.core as mx

INF = float("inf")
SRC = """
    uint i = thread_position_in_grid.x;
    uint total = BB * WW * NN;
    if (i >= total) return;
    uint x = i % NN;
    uint y = (i / NN) % WW;
    uint base = i - y * NN - x;
    float up = D[base + ((y + WW - 1) % WW) * NN + x];
    float dn = D[base + ((y + 1) % WW) * NN + x];
    float lf = (x > 0) ? D[i - 1] : INFINITY;
    float rt = (x + 1 < NN) ? D[i + 1] : INFINITY;
    float nb = metal::min(metal::min(up, dn), metal::min(lf, rt));
    out[i] = metal::min(D[i], nb + w[i]);
"""
_kern = mx.fast.metal_kernel(name="fpp_relax", input_names=["D", "w"], output_names=["out"], source=SRC)


def relax_k(D, w):
    B, W, n = D.shape
    tot = B * W * n
    return _kern(inputs=[D, w], template=[("BB", B), ("WW", W), ("NN", n)], grid=(tot, 1, 1), threadgroup=(256, 1, 1),
                 output_shapes=[D.shape], output_dtypes=[mx.float32])[0]


def relax_roll(D, w):
    up = mx.roll(D, 1, axis=1)
    dn = mx.roll(D, -1, axis=1)
    B, W, n = D.shape
    pad = mx.full((B, W, 1), INF, dtype=mx.float32)
    left = mx.concatenate([pad, D[:, :, :-1]], axis=2)
    right = mx.concatenate([D[:, :, 1:], pad], axis=2)
    nb = mx.minimum(mx.minimum(up, dn), mx.minimum(left, right))
    return mx.minimum(D, nb + w)


def one_batch(B, W, n, key, relax=relax_k):
    u = mx.random.uniform(low=1e-12, high=1.0, shape=(B, W, n), key=key)
    w = -mx.log(u)
    D = mx.concatenate([w[:, :, :1], mx.full((B, W, n - 1), INF, dtype=mx.float32)], axis=2)
    mx.eval(w, D)
    it, cap = 0, 30 * n + 1000
    while it < cap:
        prev = D
        for _ in range(64):
            D = relax(D, w)
        it += 64
        same = mx.all(D == prev)
        mx.eval(D, same)
        if bool(same.item()):
            break
    T = mx.min(D[:, :, -1], axis=1)
    mx.eval(T)
    return [round(float(x), 5) for x in T.tolist()], it, it >= cap


def selftest():
    ok = True
    for (B, W, n, s) in [(3, 5, 17, 1), (4, 12, 64, 2), (2, 40, 256, 3), (1, 101, 512, 4)]:
        t = time.time(); a = one_batch(B, W, n, mx.random.key(s), relax_roll); ta = time.time() - t
        t = time.time(); b = one_batch(B, W, n, mx.random.key(s), relax_k); tb = time.time() - t
        same = a[0] == b[0] and a[1] == b[1]
        ok &= same
        print("B=%d W=%d n=%d  roll %.2fs  kernel %.2fs  iters %d/%d  T equal: %s" % (B, W, n, ta, tb, a[1], b[1], same))
    # negative control: the comparison must be able to fail. A kernel run on weights scaled by 1.001 has to give a different T.
    B, W, n = 2, 12, 64
    u = mx.random.uniform(low=1e-12, high=1.0, shape=(B, W, n), key=mx.random.key(9))
    w = -mx.log(u)
    def solve(wt, relax):
        D = mx.concatenate([wt[:, :, :1], mx.full((B, W, n - 1), INF, dtype=mx.float32)], axis=2)
        for i in range(30 * n + 1000):
            D = relax(D, wt)
            if i % 64 == 63:
                mx.eval(D)
        return mx.min(D[:, :, -1], axis=1).tolist()
    base, pert = solve(w, relax_roll), solve(w * 1.001, relax_k)
    ctrl = base != pert
    print("negative control (scaled weights differ):", ctrl)
    ok &= ctrl
    print("selftest", "PASS" if ok else "FAIL")
    return ok


def main():
    OUT = sys.argv[1]
    BUDGET = float(sys.argv[2]) if len(sys.argv) > 2 else 6 * 3600.0
    CS = [float(x) for x in os.environ.get("FPP_CS", "").split(",") if x]
    NS = [int(x) for x in os.environ.get("FPP_NS", "256,512,1024,2048").split(",")]
    AS = [float(x) for x in os.environ.get("FPP_AS", "0.33,0.5,0.6,0.667,0.75,0.85,1.0").split(",")]
    ELEMS = int(os.environ.get("FPP_ELEMS", str(24 * 1024 * 1024)))
    configs = []
    for n in NS:
        for a in (CS if CS else AS):
            W = max(3, int(round(a * n ** (2.0 / 3.0)))) if CS else max(3, int(round(n ** a)))
            B = int(max(1, min(512, ELEMS // (W * n))))
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
                                    "secs": round(time.time() - s, 2), "seed": seed, "k": k, "T": T, "solver": "metal_kernel"}) + "\n")
                f.flush()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        sys.exit(0 if selftest() else 1)
    main()
