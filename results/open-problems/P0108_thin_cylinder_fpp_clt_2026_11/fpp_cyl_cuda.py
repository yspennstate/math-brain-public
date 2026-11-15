"""P0108 numerics, CUDA port of fpp_cyl.py (an agent, 13 Nov 2026): first-passage percolation across a thin
cylinder (Z_W x {0..n-1}), iid Exp(1) site weights, T = min over paths from column 0 to column n-1 of the summed site
weights (both ends included). Same solver (Bellman-Ford to its fixed point, 64 sweeps between checks), same row format
as the Mac (MLX) version plus "dev": "cuda", so fpp_agg.py combines both files. Monte Carlo only, no training.

  python fpp_cyl_cuda.py <rows.jsonl> <budget_s>      env FPP_NS, FPP_AS as in fpp_cyl.py; stops on ./STOP
  python fpp_cyl_cuda.py --check                      small exact check against a CPU Dijkstra
"""
import sys, os, json, time, heapq
import torch

DEV = "cuda"
NS = [int(x) for x in os.environ.get("FPP_NS", "256,512,1024,2048").split(",")]
AS = [float(x) for x in os.environ.get("FPP_AS", "0.33,0.5,0.6,0.667,0.75,0.85,1.0").split(",")]
ELEMS = 24 * 1024 * 1024
INF = float("inf")


def relax(D, w):
    nb = torch.minimum(torch.roll(D, 1, dims=1), torch.roll(D, -1, dims=1))
    nb[:, :, 1:] = torch.minimum(nb[:, :, 1:], D[:, :, :-1])
    nb[:, :, :-1] = torch.minimum(nb[:, :, :-1], D[:, :, 1:])
    return torch.minimum(D, nb + w)


def solve(w):
    B, W, n = w.shape
    D = torch.full_like(w, INF)
    D[:, :, 0] = w[:, :, 0]
    it, cap = 0, 30 * n + 1000
    while it < cap:
        prev = D
        for _ in range(64):
            D = relax(D, w)
        it += 64
        if torch.equal(D, prev):
            break
    return D[:, :, -1].min(dim=1).values, it, it >= cap


def one_batch(B, W, n, gen):
    u = torch.rand((B, W, n), generator=gen, device=DEV, dtype=torch.float32).clamp_(min=1e-12)
    T, it, capped = solve(-torch.log(u))
    return [round(float(x), 5) for x in T.tolist()], it, capped


def dijkstra(w):
    W, n = len(w), len(w[0])
    dist = {(y, 0): w[y][0] for y in range(W)}
    h = [(d, y, x) for (y, x), d in dist.items()]
    heapq.heapify(h)
    while h:
        d, y, x = heapq.heappop(h)
        if d > dist[(y, x)]:
            continue
        if x == n - 1:
            return d
        for yy, xx in (((y + 1) % W, x), ((y - 1) % W, x), (y, x - 1), (y, x + 1)):
            if 0 <= xx < n:
                nd = d + w[yy][xx]
                if nd < dist.get((yy, xx), INF):
                    dist[(yy, xx)] = nd
                    heapq.heappush(h, (nd, yy, xx))


def check():
    g = torch.Generator(device=DEV)
    g.manual_seed(7)
    worst = 0.0
    for (W, n) in ((3, 20), (7, 40), (16, 64), (5, 128)):
        u = torch.rand((6, W, n), generator=g, device=DEV, dtype=torch.float32).clamp_(min=1e-12)
        w = -torch.log(u)
        T, it, capped = solve(w)
        for b in range(6):
            ref = dijkstra(w[b].double().cpu().tolist())
            worst = max(worst, abs(float(T[b]) - ref) / ref)
        print("W %d n %d iters %d capped %s" % (W, n, it, capped))
    print("max rel err vs Dijkstra %.2e -> %s" % (worst, "PASS" if worst < 1e-5 else "FAIL"))
    return 0 if worst < 1e-5 else 1


def gpu_util():
    import subprocess
    try:
        return int(subprocess.run(["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"],
                                  capture_output=True, text=True, timeout=30).stdout.split()[0])
    except Exception:
        return 100


def wait_for_idle_gpu():
    # Never share a busy card: a WDDM card at ~100 pct shared by several contexts starves the desktop compositor (6 Sep
    # freeze). Start only after three quiet minutes in a row; give up at the budget or on ./STOP.
    quiet = 0
    while quiet < 3:
        if os.path.exists("STOP"):
            return False
        quiet = quiet + 1 if gpu_util() < 15 else 0
        time.sleep(60)
    return True


def main():
    out, budget = sys.argv[1], float(sys.argv[2])
    if os.environ.get("FPP_WAIT_IDLE", "1") != "0" and not wait_for_idle_gpu():
        return 3
    configs = []
    for n in NS:
        for a in AS:
            W = max(3, int(round(n ** a)))
            configs.append((n, a, W, int(max(4, min(512, ELEMS // (W * n))))))
    t0 = time.time()
    seed = 500000 + int(time.time()) % 100000   # disjoint from the Mac runs' seed range (0..99999)
    gen = torch.Generator(device=DEV)
    k = 0
    with open(out, "a", encoding="utf-8") as f:
        while time.time() - t0 < budget and not os.path.exists("STOP"):
            for (n, a, W, B) in configs:
                if time.time() - t0 >= budget or os.path.exists("STOP"):
                    break
                k += 1
                gen.manual_seed(seed * 1000003 + k)
                s = time.time()
                T, it, capped = one_batch(B, W, n, gen)
                f.write(json.dumps({"n": n, "a": a, "W": W, "B": B, "iters": it, "capped": capped,
                                    "secs": round(time.time() - s, 2), "seed": seed, "k": k, "dev": "cuda", "T": T}) + "\n")
                f.flush()


if __name__ == "__main__":
    sys.exit(check() if sys.argv[1:] == ["--check"] else main())
