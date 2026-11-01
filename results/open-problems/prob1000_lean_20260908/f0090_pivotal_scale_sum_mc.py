"""Monte Carlo control for the scale sum in the F0090 argument, on the PIVOTAL set (2026-09-10, claude-prob1000-0910).

Critical bond percolation on the R x R site square, f = left-right crossing. An edge e = (u,v) with dual edge
e* = (d1,d2) is pivotal iff (A) u <-> L and v <-> R (or reversed) in the open graph, and (B) d1 <-> T and d2 <-> B
(or reversed) in the closed dual graph: planar duality, both directions checked in the memo's companion note.
For each sample: |P| and |P_r| = number of dyadic r-squares (site grid) containing a pivotal edge, r = 1,2,4,...
Reported: E|P| (= I(f) up to the pivotal/influence normalisation), E|P_r|/E|P| per scale, and
    ratio = sum_{r>=2} E|P_r| / E|P|,
which the argument says stays bounded as R grows (on the triangular lattice it would tend to about 1/(2^{3/4}-1)).
Runs BelowNormal, single process.
"""
import sys, time
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

def build(R):
    # sites (i,j), 0<=i,j<R; horizontal edges h(i,j): (i,j)-(i,j+1); vertical v(i,j): (i,j)-(i+1,j)
    H = [(i, j) for i in range(R) for j in range(R - 1)]
    V = [(i, j) for i in range(R - 1) for j in range(R)]
    E = [((i, j), (i, j + 1)) for (i, j) in H] + [((i, j), (i + 1, j)) for (i, j) in V]
    nE = len(E)
    site = lambda i, j: i * R + j
    L, Rn = R * R, R * R + 1                       # virtual left/right nodes
    pu = np.array([site(*a) for a, b in E]); pv = np.array([site(*b) for a, b in E])
    # dual sites: faces (i,j) for 0<=i<R-1, 0<=j<R-1, plus T (top) and B (bottom) virtual nodes
    F = R - 1
    face = lambda i, j: i * F + j
    T, Bt = F * F, F * F + 1
    du = np.empty(nE, dtype=np.int64); dv = np.empty(nE, dtype=np.int64)
    k = 0
    for (i, j) in H:                              # horizontal edge (i,j)-(i,j+1) separates face (i-1,j) above and (i,j) below
        du[k] = T if i == 0 else face(i - 1, j); dv[k] = Bt if i == R - 1 else face(i, j); k += 1
    for (i, j) in V:                              # vertical edge (i,j)-(i+1,j) separates face (i,j-1) left and (i,j) right
        du[k] = face(i, j - 1) if j > 0 else -1; dv[k] = face(i, j) if j < R - 1 else -1; k += 1
    # vertical boundary edges (j=0 or j=R-1) have one side outside: they never lie on a T-B dual path, mark -1
    ei = np.array([a[0] for a, b in E]); ej = np.array([a[1] for a, b in E])
    return dict(nE=nE, pu=pu, pv=pv, du=du, dv=dv, L=L, R=Rn, T=T, B=Bt, nS=R * R + 2, nF=F * F + 2, ei=ei, ej=ej, size=R)

def sample(g, rng):
    return pivotal(g, rng.random(g["nE"]) < 0.5)

def pivotal(g, w):
    R = g["size"]
    # open primal graph with L/R virtual nodes attached to column 0 / column R-1
    op = np.flatnonzero(w)
    rows = np.concatenate([g["pu"][op], np.full(R, g["L"]), np.full(R, g["R"])])
    cols = np.concatenate([g["pv"][op], np.arange(R) * R, np.arange(R) * R + (R - 1)])
    A = coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(g["nS"], g["nS"]))
    _, cp = connected_components(A, directed=False)
    # closed dual graph
    cl = np.flatnonzero(~w & (g["du"] >= 0) & (g["dv"] >= 0))
    Ad = coo_matrix((np.ones(len(cl)), (g["du"][cl], g["dv"][cl])), shape=(g["nF"], g["nF"]))
    _, cd = connected_components(Ad, directed=False)
    condA = ((cp[g["pu"]] == cp[g["L"]]) & (cp[g["pv"]] == cp[g["R"]])) | ((cp[g["pv"]] == cp[g["L"]]) & (cp[g["pu"]] == cp[g["R"]]))
    ok = (g["du"] >= 0) & (g["dv"] >= 0)
    dU = np.where(ok, g["du"], 0); dV = np.where(ok, g["dv"], 0)
    condB = ok & (((cd[dU] == cd[g["T"]]) & (cd[dV] == cd[g["B"]])) | ((cd[dV] == cd[g["T"]]) & (cd[dU] == cd[g["B"]])))
    piv = condA & condB
    crossing = cp[g["L"]] == cp[g["R"]]
    return piv, crossing

def main(R, n):
    rng = np.random.default_rng(12345 + R)
    g = build(R)
    scales = [1]
    while scales[-1] * 2 <= R: scales.append(scales[-1] * 2)
    tot = np.zeros(len(scales)); totP = 0.0; ncross = 0
    t0 = time.time()
    for s in range(n):
        piv, crossing = sample(g, rng); ncross += crossing
        totP += piv.sum()
        if piv.any():
            ii = g["ei"][piv]; jj = g["ej"][piv]
            for a, r in enumerate(scales):
                tot[a] += len(set(zip(ii // r, jj // r)))
    EP = totP / n
    per = tot / n
    ratio = per[1:].sum() / EP if EP > 0 else float("nan")
    print(f"R={R} n={n} P(cross)={ncross/n:.3f} E|P|={EP:.3f}  E|P_r|/E|P| by r={{ {', '.join(f'{r}:{v/EP:.3f}' for r, v in zip(scales, per))} }}  sum_(r>=2)/E|P| = {ratio:.3f}  ({time.time()-t0:.0f}s)", flush=True)

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    for R, n in [(16, 4000), (32, 4000), (64, 2000), (128, 1000), (256, 400)]:
        main(R, n)
