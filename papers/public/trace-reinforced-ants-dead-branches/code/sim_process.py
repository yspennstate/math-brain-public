# Direct simulation of the trace-reinforced ant process (not the ODE): W_e(n)/n at checkpoints.
# Usage: python3 sim_process.py NANTS SEED
import sys, random
def run(name, n, E, N, F, nants, seed, pred=None):
    rnd = random.Random(seed)
    adj = [[] for _ in range(n)]
    for k, (u, v) in enumerate(E): adj[u].append((v, k)); adj[v].append((u, k))
    W = [1.0] * len(E); marks = [10 ** k for k in range(3, 9)]
    print(name, "edges", E, "N", N, "F", F)
    if pred: print("   ODE limit      ", " ".join(f"{x:7.4f}" for x in pred))
    for t in range(1, nants + 1):
        x = N; crossed = set()
        while x != F:
            nb = adj[x]; tot = 0.0
            for (_, k) in nb: tot += W[k]
            r = rnd.random() * tot
            for (z, k) in nb:
                r -= W[k]
                if r <= 0: break
            crossed.add(k); x = z
        for k in crossed: W[k] += 1.0
        if t in marks or t == nants:
            print(f"   n={t:<10d}", " ".join(f"{w / t:7.4f}" for w in W), flush=True)
nants = int(sys.argv[1]); seed = int(sys.argv[2])
run("c4detour (N=0,a=1,F=2,b=3,y=4)", 5, [(0, 1), (1, 2), (2, 3), (3, 0), (4, 1), (4, 2)], 0, 2, nants, seed, [0.707107, 0.5, 0.5, 0.707107, 0, 0])
run("shadow5 (N=0,a=1,b=2,F=3,c=4)", 5, [(0, 1), (0, 2), (1, 3), (2, 3), (4, 1), (4, 2), (4, 3)], 0, 3, nants, seed + 1, [0.721727, 0.721727, 0.5, 0.5, 0.320915, 0.320915, 0])
E = [(i, j) for i in (1, 2, 3) for j in (0, 4, 5)] + [(5, 4)]
run("K33+xF (N=0,F=4,x=5)", 6, E, 0, 4, nants, seed + 2, [0.614318, 0.333333, 0.366516] * 3 + [0])
run("paw (N=0,x=1,y=2,F=3)", 4, [(0, 1), (1, 2), (1, 3), (2, 3)], 0, 3, nants, seed + 3, [1, 0, 1, 0])
