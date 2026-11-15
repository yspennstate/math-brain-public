# Exact quenched evolution of the randomly oriented Manhattan walk on Z^2 (evidence only), CUDA port of manhattan_exact.py.
# Row y carries orientation e_y in {+1,-1}, column x carries f_x. Each step: with prob 1/2 move to (x+e_y, y),
# with prob 1/2 to (x, y+f_x). Full distribution from the origin for T steps on a (2T+2)^2 grid (nothing wraps);
# records p_t(0,0) every step and the mean-square displacement every 10 steps. Array arithmetic only, no training.
# usage: manhattan_exact_torch.py T B nbatch seed0 out.npz
import os, sys, time
import numpy as np
import torch

# Normal priority on purpose: at BelowNormal on a saturated laptop the single CPU thread that launches the
# GPU kernels starved (4.6 s of CPU in five minutes, GPU at 0 pct). One CPU thread is all this uses.
torch.set_num_threads(1)

T, B, NB, SEED0 = (int(a) for a in sys.argv[1:5])
OUT = sys.argv[5]
STOP = OUT + ".STOP"
dev = torch.device("cuda")
L = 2 * T + 2
c = T
coord = torch.arange(L, device=dev, dtype=torch.float32) - c
X2 = (coord ** 2).view(1, 1, L)
Y2 = (coord ** 2).view(1, L, 1)


def step(p, E, F):
    h = 0.5 * p
    he, hf = h * E, h * F
    return (torch.roll(he, 1, 2) + torch.roll(h - he, -1, 2)
            + torch.roll(hf, 1, 1) + torch.roll(h - hf, -1, 1))


ret_all, msd_all, mass_all = [], [], []
msd_t = np.arange(10, T + 1, 10)
with torch.no_grad():
    for b in range(NB):
        if os.path.exists(STOP):
            break
        rng = np.random.default_rng(SEED0 + b)
        E = torch.tensor(rng.integers(0, 2, size=(B, L, 1)), device=dev, dtype=torch.float32)
        F = torch.tensor(rng.integers(0, 2, size=(B, 1, L)), device=dev, dtype=torch.float32)
        p = torch.zeros((B, L, L), device=dev, dtype=torch.float32)
        p[:, c, c] = 1.0
        ret = torch.zeros((B, T + 1), device=dev, dtype=torch.float64)
        ret[:, 0] = 1.0
        msd = torch.zeros((B, len(msd_t)), device=dev, dtype=torch.float64)
        t0 = time.time()
        for t in range(1, T + 1):
            p = step(p, E, F)
            ret[:, t] = p[:, c, c]
            if t % 10 == 0:
                msd[:, t // 10 - 1] = (p * X2).sum((1, 2)) + (p * Y2).sum((1, 2))
        mass = p.sum((1, 2)).cpu().numpy()
        ret_all.append(ret.cpu().numpy()); msd_all.append(msd.cpu().numpy()); mass_all.append(mass)
        del p
        np.savez(OUT, T=T, ret=np.concatenate(ret_all), msd=np.concatenate(msd_all), msd_t=msd_t,
                 mass=np.concatenate(mass_all), seeds=np.arange(SEED0, SEED0 + len(ret_all)))
        r = np.concatenate(ret_all).mean(0)
        ev = np.arange(2 * (T // 16), T + 1, 2)
        sl = np.polyfit(np.log(ev), np.log(r[ev]), 1)[0]
        mm = np.concatenate(msd_all).mean(0)
        k = msd_t >= T // 8
        sm = np.polyfit(np.log(msd_t[k]), np.log(mm[k]), 1)[0]
        print(f"batch {b} envs {len(ret_all)*B} {time.time()-t0:.0f}s mass {mass.min():.6f}..{mass.max():.6f} "
              f"p_T(0,0) {r[T if T%2==0 else T-1]:.3e} slope_p {sl:.4f} slope_msd {sm:.4f}", flush=True)
