import json, sys, numpy as np
from multiprocessing import Pool
from adam_scalar_drift import xstar
def job(c):
    n, b2, b1, eps, iid = c
    b = np.array([n - 1.0] + [-1.0] * (n - 1)); a = np.ones(n)
    V, m3 = np.mean(b ** 2), np.mean(b ** 3); pred = (1 - b2) * m3 / (4 * V)
    xs = xstar(a, b, b1, b2, eps, -1e-4, 1.5, it=24, iid=iid, chains=2000)
    return dict(n=n, beta2=b2, beta1=b1, eps=eps, sampling="iid" if iid else "RR", n1mb2=n * (1 - b2), xstar=xs, pred_first_order=pred, ratio=xs / pred)
if __name__ == "__main__":
    cs = [(10, b2, b1, 0.0, iid) for iid in (False, True) for b1 in (0.0, 0.9) for b2 in (0.999, 0.99, 0.95, 0.9, 0.5)]
    with Pool(4) as p, open("sweep_n10.jsonl", "a") as f:
        for r in p.imap_unordered(job, cs):
            f.write(json.dumps(r) + "\n"); f.flush()
