# Exact quenched evolution of the randomly oriented Manhattan walk on Z^2, on a cropped (2W+2)^2 window instead of the
# full (2T+2)^2 grid, so T=8000 fits in 8 GB. Same dynamics as manhattan_exact_torch.py. The window is exact as long as
# no mass reaches its edge: every 50 steps the mass in the outer band of width 64 is measured, and the run records the
# largest value seen (edge_max). A result with edge_max above 1e-12 is not used. Array arithmetic only, no training.
# usage: manhattan_exact_torch_w.py T W B nbatch seed0 out.npz
import os, sys, time
import numpy as np
import torch

torch.set_num_threads(1)

T, W, B, NB, SEED0 = (int(a) for a in sys.argv[1:6])
OUT = sys.argv[6]
STOP = OUT + ".STOP"
BAND = 64
dev = torch.device("cuda")
L = 2 * W + 2
c = W
coord = torch.arange(L, device=dev, dtype=torch.float32) - c
X2 = (coord ** 2).view(1, 1, L)
Y2 = (coord ** 2).view(1, L, 1)


def step(p, E, F):
    h = 0.5 * p
    he, hf = h * E, h * F
    return (torch.roll(he, 1, 2) + torch.roll(h - he, -1, 2)
            + torch.roll(hf, 1, 1) + torch.roll(h - hf, -1, 1))


def edge_mass(p):
    q = p.double()
    m = (q[:, :BAND, :].sum((1, 2)) + q[:, L - BAND:, :].sum((1, 2))
         + q[:, BAND:L - BAND, :BAND].sum((1, 2)) + q[:, BAND:L - BAND, L - BAND:].sum((1, 2)))
    return m.max().item()


ret_all, msd_all, mass_all, edge_all = [], [], [], []
msd_t = np.arange(10, T + 1, 10)
with torch.no_grad():
    for b in range(NB):
        if os.path.exists(STOP):
            break
        rng = np.random.default_rng(SEED0 + b)
        # drawn on the full (2T+2) grid and cropped, so a window run sees the same environment as the full-grid run
        LF, lo = 2 * T + 2, T - W
        E = torch.tensor(rng.integers(0, 2, size=(B, LF, 1))[:, lo:lo + L], device=dev, dtype=torch.float32)
        F = torch.tensor(rng.integers(0, 2, size=(B, 1, LF))[:, :, lo:lo + L], device=dev, dtype=torch.float32)
        p = torch.zeros((B, L, L), device=dev, dtype=torch.float32)
        p[:, c, c] = 1.0
        ret = torch.zeros((B, T + 1), device=dev, dtype=torch.float64)
        ret[:, 0] = 1.0
        msd = torch.zeros((B, len(msd_t)), device=dev, dtype=torch.float64)
        emax = 0.0
        t0 = time.time()
        for t in range(1, T + 1):
            p = step(p, E, F)
            ret[:, t] = p[:, c, c]
            if t % 10 == 0:
                msd[:, t // 10 - 1] = (p * X2).sum((1, 2)) + (p * Y2).sum((1, 2))
            if t % 50 == 0:
                emax = max(emax, edge_mass(p))
        mass = p.sum((1, 2)).cpu().numpy()
        ret_all.append(ret.cpu().numpy()); msd_all.append(msd.cpu().numpy()); mass_all.append(mass)
        edge_all.append(emax)
        del p
        np.savez(OUT, T=T, W=W, ret=np.concatenate(ret_all), msd=np.concatenate(msd_all), msd_t=msd_t,
                 mass=np.concatenate(mass_all), edge_max=np.array(edge_all),
                 seeds=np.arange(SEED0, SEED0 + len(ret_all)))
        mm = np.concatenate(msd_all).mean(0)
        k = msd_t >= T // 8
        sm = np.polyfit(np.log(msd_t[k]), np.log(mm[k]), 1)[0]
        print(f"batch {b} envs {len(ret_all)*B} {time.time()-t0:.0f}s edge_max {emax:.2e} rms {np.sqrt(mm[-1]):.1f} "
              f"slope_msd {sm:.4f}", flush=True)
