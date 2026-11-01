# Largest density of a linear form cos(t) U + sin(t) V for a density given on a square grid (rows: v, cols: u),
# by integrating the grid density along the level lines with linear interpolation (the same rule as the curved
# integrals), over ndir directions. A histogram of projected grid points is NOT used: grid columns that land on
# a bin edge are counted twice there and the estimate can double (seen at t = 0: 1.83 against the bound sqrt 2).
import math
import numpy as np

def line_max(rho, x0, d, ndir=360, x0v=None):
    # rho[j, k] is the density at (u, v) = (x0 + k d, x0v + j d); x0v defaults to x0
    G = rho.shape[0]
    gu = x0 + d*np.arange(G)
    gv = (x0 if x0v is None else x0v) + d*np.arange(G)
    best = (0.0, None)
    # levels r of ct u + st v covering the middle of the grid's range in that direction
    rhoT = rho.T.copy()                      # rows: u, cols: v
    for t in np.linspace(0, math.pi, ndir, endpoint=False):
        ct, st = math.cos(t), math.sin(t)
        cu, cv = gu[G//2], gv[G//2]
        r0 = ct*cu + st*cv
        r_vals = r0 + d*np.arange(-3*G//8, 3*G//8)
        acc = np.zeros(len(r_vals))
        if abs(ct) >= abs(st):
            # level line ct u + st v = r: u = (r - st v)/ct, integrate over v, Jacobian 1/|ct|
            for j in range(G):
                acc += np.interp((r_vals - st*gv[j])/ct, gu, rho[j], left=0.0, right=0.0)
            acc *= d/abs(ct)
        else:
            for k in range(G):
                acc += np.interp((r_vals - ct*gu[k])/st, gv, rhoT[k], left=0.0, right=0.0)
            acc *= d/abs(st)
        k = int(np.argmax(acc))
        if acc[k] > best[0]:
            best = (float(acc[k]), float(t))
    return best
