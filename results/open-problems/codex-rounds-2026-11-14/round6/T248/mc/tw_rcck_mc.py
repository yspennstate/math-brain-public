"""Monte Carlo check of the Tracy-Widom law for the row-centered conjugate kernel (T248), on the Apple GPU.

Y = sigma(W X / sqrt d), W m x d Gaussian, columns of X uniform on the sphere of radius sqrt d,
K_P = Y P Y^T / N with P removing the mean of each row over the N columns.
Statistic: s = b^(1/6) / (v (1 + sqrt b)^(4/3)) N^(2/3) (lambda_max(K_P) - v (1 + sqrt b)^2), b = m / N, v = 1.
Also the finite-size form with c = (N - 1) / N: centre v (sqrt b + sqrt c)^2, scale c^(1/6) b^(1/6) / (v (sqrt b + sqrt c)^(4/3)).
TW1: mean -1.2065, sd 1.2680.
The top eigenvalue is found by Lanczos with full reorthogonalization on the GPU (float32) and checked against
numpy eigvalsh in float64 on the first batch of every configuration.
Usage: python3 tw_rcck_mc.py OUTDIR
"""
import json
import math
import os
import sys
import time

import numpy as np
import torch

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
dev = torch.device("mps")
torch.manual_seed(20261115)
np.random.seed(20261115)

SQ2, SQ6, SQ24 = math.sqrt(2.0), math.sqrt(6.0), math.sqrt(24.0)
ACT = {
    "he2": lambda x: (x * x - 1.0) / SQ2,
    "he3": lambda x: (x * x * x - 3.0 * x) / SQ6,
    "he2he3": lambda x: ((x * x - 1.0) / SQ2 + (x * x * x - 3.0 * x) / SQ6) / SQ2,
    "he4": lambda x: (x ** 4 - 6.0 * x * x + 3.0) / SQ24,
}


def randn(*shape):
    """torch.randn on the Apple GPU returns |z| > 7 at a rate of about 2^-23 per draw (max seen 14.4 in 2e8
    draws; a Gaussian gives 2.6e-12): the Box-Muller step meets a float32 uniform at its smallest grid value.
    Redraw every value beyond 6 (true probability 2e-9 per draw)."""
    z = torch.randn(*shape, device=dev)
    bad = z.abs() > 6
    while bool(bad.any()):
        z = torch.where(bad, torch.randn(*shape, device=dev), z)
        bad = z.abs() > 6
    return z


def lanczos_top(matvec, B, n, k):
    """Largest eigenvalue of B symmetric n x n operators given by matvec, k Lanczos steps."""
    Q = torch.zeros(B, k, n, device=dev)
    q = torch.randn(B, n, device=dev)
    q = q / q.norm(dim=1, keepdim=True)
    alphas, betas = [], []
    for j in range(k):
        Q[:, j] = q
        w = matvec(q)
        a = (w * q).sum(1)
        alphas.append(a)
        for _ in range(2):  # full reorthogonalization, twice
            c = torch.bmm(Q[:, : j + 1], w.unsqueeze(2))
            w = w - torch.bmm(Q[:, : j + 1].transpose(1, 2), c).squeeze(2)
        bnorm = w.norm(dim=1)
        betas.append(bnorm)
        q = w / bnorm.clamp_min(1e-30).unsqueeze(1)
    A = torch.stack(alphas, 1).cpu().double().numpy()
    Bt = torch.stack(betas, 1).cpu().double().numpy()
    out = []
    for i in range(B):
        T = np.diag(A[i]) + np.diag(Bt[i, :-1], 1) + np.diag(Bt[i, :-1], -1)
        out.append(np.linalg.eigvalsh(T)[-1])
    return np.array(out)


def run(N, m, d, act, samples, batch, k, n_uncentered, kind="net"):
    f = ACT[act]
    b = m / N
    c = (N - 1) / N
    vals, vals_unc, checks = [], [], []
    t0 = time.time()
    done = 0
    while done < samples:
        B = min(batch, samples - done)
        if kind == "iid":
            X = W = None
            Y = f(randn(B, m, N))
        else:
            X = randn(B, d, N)
            X = X * (math.sqrt(d) / X.norm(dim=1, keepdim=True))
            W = randn(B, m, d)
            Y = f(torch.bmm(W, X) / math.sqrt(d))
        Yc = Y - Y.mean(dim=2, keepdim=True)
        if m <= N:
            G = torch.bmm(Yc, Yc.transpose(1, 2)) / N
        else:
            G = torch.bmm(Yc.transpose(1, 2), Yc) / N
        n = G.shape[1]
        lam = lanczos_top(lambda q: torch.bmm(G, q.unsqueeze(2)).squeeze(2), B, n, k)
        if done == 0:
            ex = np.linalg.eigvalsh(G[0].cpu().double().numpy())[-1]
            checks.append(float(lam[0] - ex))
        vals.extend(lam.tolist())
        if len(vals_unc) < n_uncentered:
            Gu = torch.bmm(Y, Y.transpose(1, 2)) / N if m <= N else torch.bmm(Y.transpose(1, 2), Y) / N
            lu = lanczos_top(lambda q: torch.bmm(Gu, q.unsqueeze(2)).squeeze(2), B, Gu.shape[1], 40)
            vals_unc.extend(lu.tolist())
        done += B
        del X, W, Y, Yc, G
    lam = np.array(vals)
    s = b ** (1 / 6) / (1 + math.sqrt(b)) ** (4 / 3) * N ** (2 / 3) * (lam - (1 + math.sqrt(b)) ** 2)
    sc = (c * b) ** (1 / 6) / (math.sqrt(b) + math.sqrt(c)) ** (4 / 3) * N ** (2 / 3) * (lam - (math.sqrt(b) + math.sqrt(c)) ** 2)
    se = lambda x: float(np.std(x, ddof=1) / math.sqrt(len(x)))
    res = dict(kind=kind, N=N, m=m, d=d, act=act, b=b, samples=len(lam), lanczos_k=k,
               lanczos_minus_eigvalsh=checks,
               mean=float(s.mean()), mean_se=se(s), sd=float(s.std(ddof=1)),
               mean_finite=float(sc.mean()), sd_finite=float(sc.std(ddof=1)),
               q05=float(np.quantile(s, 0.05)), q50=float(np.quantile(s, 0.5)), q95=float(np.quantile(s, 0.95)),
               edge=(1 + math.sqrt(b)) ** 2, lam_mean=float(lam.mean()),
               uncentered_lam_mean=float(np.mean(vals_unc)) if vals_unc else None,
               uncentered_n=len(vals_unc), qN_over_d_ratio=N / d,
               seconds=round(time.time() - t0, 1))
    tag = f"{kind}_{act}_N{N}_m{m}_d{d}"
    np.save(os.path.join(OUT, tag + ".npy"), lam)
    with open(os.path.join(OUT, tag + ".json"), "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res), flush=True)
    torch.mps.empty_cache()


CONFIGS = [
    # N, m, d, act, samples, batch, lanczos k ; each runs for the network and for iid entries of the same law
    (500, 250, 375, "he2", 4000, 32, 70),
    (1000, 500, 750, "he2", 4000, 16, 80),
    (2000, 1000, 1500, "he2", 3000, 8, 100),
    (4000, 2000, 3000, "he2", 1500, 2, 120),
    (8000, 4000, 6000, "he2", 400, 1, 140),
    (1000, 2000, 1500, "he2", 2000, 8, 80),
    (2000, 4000, 3000, "he2", 1000, 2, 100),
    (1000, 500, 750, "he2he3", 2000, 16, 80),
    (4000, 2000, 3000, "he2he3", 1000, 2, 120),
]
if len(sys.argv) > 2 and sys.argv[2] == "smoke":
    CONFIGS = [(200, 100, 150, "he2he3", 32, 16, 60), (100, 200, 150, "he2", 32, 16, 60)]
for cfg in CONFIGS:
    N, m, d, act, samples, batch, k = cfg
    for kind in ("net", "iid"):
        run(N, m, d, act, samples, batch, k, n_uncentered=64, kind=kind)
print("DONE", flush=True)
