# T354 eps sweep follow-up (agent B, 20 Oct 2026). In eps_sweep.jsonl every case fits x*(eps) = X*3/(3+eps) + delta
# with residual under 0.2% of X; delta is read as the common-random-number offset (all eps share seed 0). If so, delta changes
# with the seed while X does not. RR beta1 0.9 beta2 0.99 (delta -7.0e-4 at seed 0), seeds 1 and 2, eps 0 and 10.
import json, numpy as np
from multiprocessing import Pool
from adam_scalar_drift import xstar
def job(c):
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception: pass
    seed, eps = c
    b = np.array([9.0] + [-1.0] * 9); a = np.ones(10)
    xs = xstar(a, b, 0.9, 0.99, eps, -1e-4, 0.1, it=24, iid=False, chains=2000, seed=seed)
    return dict(beta2=0.99, beta1=0.9, eps=eps, sampling="RR", seed=seed, xstar=xs)
if __name__ == "__main__":
    with Pool(4) as p, open("eps_seed_check.jsonl", "a") as f:
        for r in p.imap_unordered(job, [(s, e) for s in (1, 2) for e in (0.0, 10.0)]):
            f.write(json.dumps(r) + "\n"); f.flush(); print(r, flush=True)
