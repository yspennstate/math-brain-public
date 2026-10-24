# -*- coding: utf-8 -*-
"""Exact finite-depth computation for the two-thirds Bernoulli measure (paper's prefix densities g_D).

Y = (1/3) sum_{k<D} B_k lam^k + lam^D * (1/3)*3*U', tail replaced by an independent Uniform[0,1] scaled so that
Y_D = S_p + lam^D * V with V ~ Unif[0,1] (the paper's g_D construction; the true tail lam^D Y' also lies in
[0, lam^D] since Y' in [0,1]).  Everything below is piecewise constant on a grid of R cells of [0,1).

Outputs per depth D:
  j_0(D)      = log 2 - H(H|Z) for U ~ g_D, 2U = H + Z             (should approach c = log(9/8) = 0.1177830)
  j_1(D)      = the same for U' ~ T_2 g_D                            (Monte Carlo: 0.00200)
  EVar_0(D)   = E_W Var((-1)^{floor 3Z} u_0(Z) | W = frac(3Z))       (Monte Carlo: 0.2087)
  L2(D)       = int g_D^2,  Linf(D) = max g_D                        (growth in D probes L^2 / bounded density)
Grid resolution R must resolve lam^D: cells per prefix interval = lam^D * R.
"""
import numpy as np, math, sys, time, json
D = int(sys.argv[1]) if len(sys.argv) > 1 else 18
R = int(sys.argv[2]) if len(sys.argv) > 2 else 1 << 20
lam = 2.0/3.0
t0 = time.time()

def prefix_starts(D):
    # all 2^D values of (1/3) sum_{k<D} b_k lam^k, built by doubling
    s = np.array([0.0])
    for k in range(D):
        s = np.concatenate([s, s + (lam**k)/3.0])
    return s

def density_on_grid(starts, length, R, weights=None):
    """Sum of uniform densities on [start, start+length) (each of mass w), on R cells of [0,1); returns cell masses."""
    if weights is None: weights = np.full(starts.shape, 1.0/starts.size)
    a = starts * R; b = (starts + length) * R
    # fractional-endpoint difference array: mass density per unit length = w/length; add over [a,b)
    dens = weights / length                      # mass per unit of [0,1)
    diff = np.zeros(R + 2)
    ia = np.floor(a).astype(np.int64); ib = np.floor(b).astype(np.int64)
    fa = a - ia; fb = b - ib
    # full cells strictly between ia+1 .. ib-1 get dens/R each; partial cells get the fractions
    np.add.at(diff, np.minimum(ia + 1, R + 1), dens / R)
    np.add.at(diff, np.minimum(ib, R + 1), -dens / R)
    cell = np.cumsum(diff)[:R]
    np.add.at(cell, np.minimum(ia, R - 1), dens * (1 - fa) / R)
    np.add.at(cell, np.minimum(ib, R - 1), dens * fb / R)
    return cell   # masses per cell, sum ~ 1

def fibre_stats(mass_cells_U):
    """Given cell masses of a law on [0,1) with R cells (R even), compute j = log2 - H(H|Z), u(Z), EVar over T_3 preimages."""
    R = mass_cells_U.size; half = R // 2
    m0 = mass_cells_U[:half]; m1 = mass_cells_U[half:]      # H = 0 for U < 1/2, H = 1 for U >= 1/2; Z = frac(2U) -> same cell index
    tot = m0 + m1
    p1 = np.where(tot > 0, m1 / np.maximum(tot, 1e-300), 0.5)
    with np.errstate(divide='ignore', invalid='ignore'):
        h = -(p1 * np.log(p1) + (1 - p1) * np.log(1 - p1)); h = np.nan_to_num(h)
    HcondZ = float(np.sum(tot * h)) / float(np.sum(tot))
    j = math.log(2) - HcondZ
    u = np.where(tot > 0, (m0 - m1) / np.maximum(tot, 1e-300), 0.0)      # u(Z) on half cells (Z grid of half cells)
    # W = frac(3Z): Z cell index z in [0,half); preimage i = z // (half//3), w = z % (half//3)  (half divisible by 3 required)
    q = half // 3
    if q * 3 != half: raise SystemExit("R/2 must be divisible by 3")
    tz = tot.reshape(3, q); uz = u.reshape(3, q)
    sign = np.array([1.0, -1.0, 1.0])[:, None]
    V = sign * uz
    massw = tz.sum(axis=0); p = tz / np.maximum(massw, 1e-300)
    var = (p * V**2).sum(axis=0) - ((p * V).sum(axis=0))**2
    EVar = float(np.sum(massw * var)) / float(np.sum(massw))
    Eu2 = float(np.sum(tot * u**2)) / float(np.sum(tot))
    Em2 = float(np.sum(massw * ((p * V).sum(axis=0))**2)) / float(np.sum(massw))
    return j, EVar, Eu2, Em2

starts = prefix_starts(D)
L = lam**D
if L * R < 4: raise SystemExit(f"grid too coarse: lam^D R = {L*R:.2f} cells per interval")
g = density_on_grid(starts, L, R)                   # law of Y_D on R cells
L2 = float(np.sum((g * R)**2) / R); Linf = float(np.max(g * R))
j0, EVar0, Eu2_0, Em2_0 = fibre_stats(g)
# T_2 g: cell masses of frac(2U): fold halves
g2 = g[:R//2] + g[R//2:]
# need R/2 cells with R/2 divisible by 6; use the same R (fold gives R/2 cells; fibre_stats needs its own half divisible by 3)
j1, EVar1, Eu2_1, Em2_1 = fibre_stats(g2)
g3 = g[:R//3] + g[R//3:2*R//3] + g[2*R//3:]          # T_3 g (same law as T_2 g up to the depth truncation)
j1b, _, _, _ = fibre_stats(g3)
g4 = g2[:R//4] + g2[R//4:]                            # T_2^2 g
j2, EVar2, Eu2_2, Em2_2 = fibre_stats(g4)
g8 = g4[:R//8] + g4[R//8:]                            # T_2^3 g
j3, EVar3, Eu2_3, Em2_3 = fibre_stats(g8)
seq = []; gg = g8; nn = 3
while gg.size >= 96 and (gg.size // 2) % 3 == 0 and nn < 8:
    nn += 1; gg = gg[:gg.size//2] + gg[gg.size//2:]
    jj, ev, e2, m2 = fibre_stats(gg); seq.append(dict(n=nn, j=jj, EVar=ev, Eu2=e2, Em2=m2, cells=int(gg.size)))
out = dict(D=D, R=R, cells_per_interval=L*R, j0=j0, c=math.log(9/8), EVar0=EVar0, Eu2_0=Eu2_0, Em2_0=Em2_0,
           j1_T2=j1, j1_T3=j1b, EVar1=EVar1, Eu2_1=Eu2_1, Em2_1=Em2_1,
           j2=j2, EVar2=EVar2, Eu2_2=Eu2_2, Em2_2=Em2_2, j3=j3, EVar3=EVar3, Eu2_3=Eu2_3, Em2_3=Em2_3,
           L2=L2, Linf=Linf, higher=seq, seconds=time.time()-t0)
print(json.dumps(out, indent=1))
