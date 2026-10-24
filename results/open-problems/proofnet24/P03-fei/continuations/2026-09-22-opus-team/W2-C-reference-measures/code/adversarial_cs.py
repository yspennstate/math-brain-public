"""Adversarial hill-climbing over truth tables: maximize (CSopt - H)/I, and CSopt/I, at n = 6, 7, 8.
Moves: flip one truth-table entry (sometimes two). Restarts from random, biased random, and structured seeds."""
import sys, time, json
import numpy as np
import wlib as W, csdp

W.set_polite()
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 23)


def evaluate(tt, n):
    p = W.spectrum(tt)
    I = W.I_of(p, n)
    if I < 0.25:
        return None
    H = W.H_of(p)
    cs, _ = csdp.cs_opt(p, n)
    return H, I, cs


def climb(n, obj, steps, seed_tt):
    tt = seed_tt.copy()
    v = evaluate(tt, n)
    while v is None:
        tt = rng.choice(np.array([-1, 1], dtype=np.int8), size=1 << n)
        v = evaluate(tt, n)
    cur = obj(*v)
    best = (cur, tt.copy(), v)
    T = 0.02
    for s in range(steps):
        t2 = tt.copy()
        k = 1 if rng.uniform() < 0.7 else 2
        idx = rng.integers(0, 1 << n, size=k)
        t2[idx] = -t2[idx]
        v2 = evaluate(t2, n)
        if v2 is None:
            continue
        o2 = obj(*v2)
        if o2 >= cur or rng.uniform() < np.exp((o2 - cur) / T):
            tt, cur = t2, o2
            if cur > best[0]:
                best = (cur, tt.copy(), v2)
        T *= 0.9995
    return best


def main():
    out = open(f"../logs/adversarial_cs_{sys.argv[1] if len(sys.argv) > 1 else 23}.log", "w")
    objs = {"(CS-H)/I": lambda H, I, cs: (cs - H) / I, "CS/I": lambda H, I, cs: cs / I, "CS-H bits": lambda H, I, cs: cs - H}
    for n, steps, restarts in ((6, 4000, 6), (7, 3000, 5), (8, 1500, 4)):
        for oname, obj in objs.items():
            overall = None
            t0 = time.time()
            for r in range(restarts):
                if r % 3 == 0:
                    seed = rng.choice(np.array([-1, 1], dtype=np.int8), size=1 << n)
                elif r % 3 == 1:
                    seed = np.where(rng.uniform(size=1 << n) < 0.2, -1, 1).astype(np.int8)
                else:
                    seed = W.fam_majority(n) if n % 2 else W.fam_majority(n - 1).repeat(2)[:1 << n].astype(np.int8)
                b = climb(n, obj, steps, seed)
                if overall is None or b[0] > overall[0]:
                    overall = b
            val, tt, (H, I, cs) = overall
            line = (f"n={n} objective {oname}: best {val:.5f}  H={H:.5f} I={I:.5f} H/I={H/I:.5f} CSopt={cs:.5f} "
                    f"CSopt/I={cs/I:.5f} CS-H={cs-H:.5f}  [{time.time()-t0:.0f}s]")
            print(line, flush=True); print(line, file=out, flush=True)
            print("   table:", tt.tolist(), file=out, flush=True)


if __name__ == "__main__":
    main()
