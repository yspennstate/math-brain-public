"""Random monotone hosts with coin completion (sites.py).  Families:
  grid:r:c   minimal true sets = a random set of partial transversals (injections rows -> columns) of the r x c grid
  hyp:m:k:b  minimal true sets = b random k-subsets of [m]
  lin:m:b    b random triples of [m], pairwise meeting in at most one point (partial Steiner triple systems)
Hosts with Pr[true] within WINDOW of 1/2 are completed; the best ratios are logged."""
import sys, os, time, itertools, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sites import complete
from pm_hosts import upset_table

WINDOW = 0.06


def gen_grid(r, c, rng, frac):
    perms = list(itertools.permutations(range(c), r))
    k = max(1, int(round(frac * len(perms))))
    sel = rng.choice(len(perms), size=k, replace=False)
    return [sum(1 << (i * c + perms[s][i]) for i in range(r)) for s in sel]


def gen_hyp(m, k, b, rng):
    return [int(sum(1 << int(v) for v in rng.choice(m, size=k, replace=False))) for _ in range(b)]


def gen_lin(m, b, rng, tries=2000):
    out = []
    for _ in range(tries):
        t = rng.choice(m, size=3, replace=False)
        mask = int(sum(1 << int(v) for v in t))
        if all(bin(mask & o).count('1') <= 1 for o in out):
            out.append(mask)
            if len(out) == b:
                break
    return out


def run(family, nsamples, seed, logpath, local_iters=150):
    rng = np.random.default_rng(seed)
    parts = family.split(':')
    best = []
    t0 = time.time()
    tried = kept = 0
    for s in range(nsamples):
        if parts[0] == 'grid':
            r, c = int(parts[1]), int(parts[2]); m = r * c
            frac = rng.uniform(0.15, 1.0)
            mins = gen_grid(r, c, rng, frac)
        elif parts[0] == 'hyp':
            m, k = int(parts[1]), int(parts[2])
            b = int(rng.integers(int(parts[3]), int(parts[4]) + 1))
            mins = gen_hyp(m, k, b, rng)
        elif parts[0] == 'lin':
            m = int(parts[1])
            b = int(rng.integers(int(parts[2]), int(parts[3]) + 1))
            mins = gen_lin(m, b, rng)
        tr = upset_table(m, mins)
        p = tr.mean()
        tried += 1
        if abs(p - 0.5) > WINDOW or p == 0.5:
            continue
        kept += 1
        ev, c0 = complete(tr, m, local_iters=local_iters, seed=s)
        best.append((ev['R'], s, len(mins), float(p), ev))
    best.sort(key=lambda t: -t[0])
    with open(logpath, 'a') as f:
        f.write(f"# {family}: samples={nsamples} in-window={kept} time={time.time()-t0:.0f}s\n")
        for R, s, nm, p, ev in best[:8]:
            f.write(f"  R={R:.9f} seed={seed} sample={s} nmin={nm} Pr={p:.4f} holes={ev['holes']} pairs={ev['pairs']} "
                    f"singles={ev['singles']} nvars={ev['nvars']} I={ev['I']:.5f} H={ev['H']:.5f} Tmax={ev['Tmax']}\n")
    print(f"{family}: kept {kept}/{tried}, best {best[0][0] if best else None}", flush=True)
    return best


if __name__ == '__main__':
    fam = sys.argv[1]; ns = int(sys.argv[2]); seed = int(sys.argv[3])
    run(fam, ns, seed, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs', 'random_hosts.log'))
