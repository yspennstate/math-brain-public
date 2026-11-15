# Exact quenched evolution of the randomly oriented Manhattan walk on Z^2 (evidence only), MLX, on a cropped (2W+2)^2
# window instead of the full (2T+2)^2 grid. The environment is drawn on the full grid and cropped, so a window run sees
# the same environment as a full-grid run with the same seed. The window is exact while no mass reaches its edge: every
# 50 steps the mass in the outer band of width 64 is summed, and the largest value is saved (edge_max). Rows with
# edge_max above 1e-9 are not used. Array arithmetic only, no training.
# usage: manhattan_exact_w.py T W B nbatch seed0 out.npz
import os, sys, time
import numpy as np
import mlx.core as mx

T, W, B, NB, SEED0 = (int(a) for a in sys.argv[1:6])
OUT = sys.argv[6]
STOP = OUT + ".STOP"
BAND = 64
L = 2 * W + 2
c = W
coord = (np.arange(L) - c).astype(np.float32)
X2 = mx.array((coord ** 2).reshape(1, 1, L))
Y2 = mx.array((coord ** 2).reshape(1, L, 1))
inner = np.zeros((1, L, L), np.float32)
inner[:, BAND:L - BAND, BAND:L - BAND] = 1.0
OUTER = mx.array(1.0 - inner)
del inner


def step(p, E, F):
    h = 0.5 * p
    return (mx.roll(h * E, 1, axis=2) + mx.roll(h - h * E, -1, axis=2)
            + mx.roll(h * F, 1, axis=1) + mx.roll(h - h * F, -1, axis=1))


cstep = mx.compile(step)
ret_all, msd_all, mass_all, edge_all = [], [], [], []
msd_t = np.arange(10, T + 1, 10)
LF, lo = 2 * T + 2, T - W
for b in range(NB):
    if os.path.exists(STOP):
        break
    rng = np.random.default_rng(SEED0 + b)
    e = rng.integers(0, 2, size=(B, LF, 1))[:, lo:lo + L].astype(np.float32)
    f = rng.integers(0, 2, size=(B, 1, LF))[:, :, lo:lo + L].astype(np.float32)
    E, F = mx.array(e), mx.array(f)
    p0 = np.zeros((B, L, L), np.float32)
    p0[:, c, c] = 1.0
    p = mx.array(p0)
    del p0
    ret = np.zeros((B, T + 1), np.float64)
    ret[:, 0] = 1.0
    msd = np.zeros((B, len(msd_t)), np.float64)
    emax = 0.0
    t0 = time.time()
    buf = []
    for t in range(1, T + 1):
        p = cstep(p, E, F)
        buf.append(p[:, c, c])
        if t % 10 == 0:
            m = mx.sum(p * X2, axis=(1, 2)) + mx.sum(p * Y2, axis=(1, 2))
            vals = mx.stack(buf, axis=1)
            if t % 50 == 0:
                em = mx.max(mx.sum(p * OUTER, axis=(1, 2)))
                mx.eval(p, m, vals, em)
                emax = max(emax, float(np.array(em)))
            else:
                mx.eval(p, m, vals)
            ret[:, t - 9:t + 1] = np.array(vals)
            msd[:, t // 10 - 1] = np.array(m)
            buf = []
        elif t % 2 == 0:
            mx.eval(p)
    mass = np.array(mx.sum(p, axis=(1, 2)))
    ret_all.append(ret); msd_all.append(msd); mass_all.append(mass); edge_all.append(emax)
    np.savez(OUT, T=T, W=W, ret=np.concatenate(ret_all), msd=np.concatenate(msd_all), msd_t=msd_t,
             mass=np.concatenate(mass_all), edge_max=np.array(edge_all),
             seeds=np.arange(SEED0, SEED0 + len(ret_all)))
    mm = np.concatenate(msd_all).mean(0)
    k = msd_t >= T // 8
    sm = np.polyfit(np.log(msd_t[k]), np.log(mm[k]), 1)[0]
    print(f"batch {b} envs {len(ret_all)*B} {time.time()-t0:.0f}s edge_max {emax:.2e} rms {np.sqrt(mm[-1]):.1f} "
          f"slope_msd {sm:.4f}", flush=True)
