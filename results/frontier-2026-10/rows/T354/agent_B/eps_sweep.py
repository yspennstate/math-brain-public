# T354 with eps > 0 (agent B, 20 Oct 2026). First-order prediction: with s = sqrt(V),
# 1/(s sqrt(1+u) + eps) = 1/(s+eps) - (s/2) u/(s+eps)^2 + O(u^2), so D = [f' - (s/(s+eps)) d K C/(2V)]/(s+eps) + ...,
# x*(eps) = x*(0) * s/(s + eps). Test model n = 10, a = 1, b = (9, -1 x 9): mean b = 0, V(x) = 9 + x^2, s = 3 near x*.
# Check the ratio x*(eps)/x*(0) against 3/(3+eps) on RR and iid, beta1 0 and 0.9.
import json, os, numpy as np
from multiprocessing import Pool
from adam_scalar_drift import xstar
def job(c):
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception: pass
    b2, b1, eps, iid = c
    b = np.array([9.0] + [-1.0] * 9); a = np.ones(10)
    xs = xstar(a, b, b1, b2, eps, -1e-4, 0.1, it=24, iid=iid, chains=2000)
    return dict(beta2=b2, beta1=b1, eps=eps, sampling="iid" if iid else "RR", xstar=xs)
if __name__ == "__main__":
    cs = [(b2, b1, eps, iid) for iid in (False, True) for b1 in (0.0, 0.9) for b2 in (0.99,) for eps in (0.0, 1.0, 3.0, 10.0)]
    with Pool(4) as p, open("eps_sweep.jsonl", "a") as f:
        for r in p.imap_unordered(job, cs):
            f.write(json.dumps(r) + "\n"); f.flush(); print(r, flush=True)
