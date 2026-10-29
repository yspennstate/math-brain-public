"""T240 C9 block-wise tube (agent H, 18 Oct 2026). Same reference, defect and a priori box as c9_flow.segment,
but the error z = P^{-1}(x - xhat) is bounded block by block (a block = one real eigen-direction or one complex pair):
v_b = |z_b| obeys D+ v <= A v + d with A Metzler: A_bb = log norm of the diagonal block, A_bc = norm of the off block
(both over the a priori box E). With B = A + cI >= 0, v(h) <= e^{-ch} e^{Bh} v0 + h e^{Bh} d (entrywise).
Why: from the exit face the true spread lies in the stable block; a single Euclidean ball would grow at the
unstable rate as a whole and reach ~kappa at O(1) displacement."""
import math
from fractions import Fraction as F
import numpy as np
from c9_flow import (N, I, S, up, hi, lo, iv, pm, maxabs, norm2_up, matvec, mm_rat_iv, mm_iv_rat, lognorm_up,
                     invert_rational, posdef, f_point, jac_box, jv_box, hermite_coeffs, poly_range, deriv, fdrive, fl, ETA_F,
                     drv, hull)

def flow_adapt(P, blocks, x):
    """C9_FLOWCOL=1: the flow direction g = f(x)/|g| becomes block 0 of its own. It replaces the column (of the block
    carrying most of P^{-1} g) with the largest |P^{-1} g| entry; the rest of that block stays as one block. Why: the
    eigenvector of the unstable eigenvalue is not parallel to the flow after t ~ 270, so a reset along g cannot remove
    the radius that piles up on it (brst10/brst40 died at t ~ 405 with 30 resets that each cut |v| by under 0.5 pct)."""
    g = np.array(fdrive.f(fl(x), ETA_F), dtype=float); g = g / np.linalg.norm(g)
    a = np.linalg.solve(np.array(P, dtype=float), g)
    bs = max(range(len(blocks)), key=lambda b: np.linalg.norm(a[blocks[b]]))
    j = max(blocks[bs], key=lambda i: abs(a[i]))
    cols = [g] + [np.array(P, dtype=float)[:, i] for b in blocks for i in b if i != j]
    nb, pos = [[0]], 1
    for b in blocks:
        rest = [i for i in b if i != j]
        if rest:
            nb.append(list(range(pos, pos + len(rest)))); pos += len(rest)
    return np.column_stack(cols), nb

def frame_b(Jf, x=None):
    import os
    if os.environ.get('C9_CLUSTER') == '1':
        # clustered frame (c9_cluster.py): eigenvalues within DELTA share one block spanned by an orthonormal basis of
        # their invariant subspace; stays well conditioned where the unstable and a stable eigenvalue collide (t ~ 331)
        import c9_cluster
        P, blocks = c9_cluster.frame_c(Jf)
        if os.environ.get('C9_FLOWCOL') == '1' and x is not None:
            P, blocks = flow_adapt(P, blocks, x)
        Pr = [[F(float(P[a][b])) for b in range(N)] for a in range(N)]
        return Pr, invert_rational(Pr), blocks
    w, V = np.linalg.eig(Jf)
    cols, blocks, used = [], [], set()
    for k in np.argsort(-w.real):
        if k in used: continue
        if abs(w[k].imag) < 1e-12:
            v = np.real(V[:, k]); blocks.append([len(cols)]); cols.append(v / np.linalg.norm(v)); used.add(k)
        else:
            kk = [j for j in range(len(w)) if j not in used and j != k and abs(w[j] - np.conj(w[k])) < 1e-9][0]
            v = V[:, k]; sc = np.linalg.norm(np.concatenate([v.real, v.imag])) / math.sqrt(2)
            blocks.append([len(cols), len(cols) + 1]); cols += [v.real / sc, v.imag / sc]; used |= {k, kk}
    P = np.column_stack(cols)
    Pr = [[F(float(P[a][b])) for b in range(N)] for a in range(N)]
    return Pr, invert_rational(Pr), blocks

def opnorm_rect_up(M):
    """Upper bound of the spectral norm of an exact rational (possibly rectangular) matrix."""
    m, n = len(M), len(M[0])
    G = [[sum(M[k][i] * M[k][j] for k in range(m)) for j in range(n)] for i in range(n)]
    lam = float(max(np.linalg.eigvalsh(np.array([[float(G[i][j]) for j in range(n)] for i in range(n)]))))
    lu = F(max(lam, 0.0)) * (1 + F(1, 10 ** 12)) + F(1, 10 ** 30)
    while not posdef([[(lu if i == j else 0) - G[i][j] for j in range(n)] for i in range(n)]):
        lu = lu * (1 + F(1, 10 ** 9)) + F(1, 10 ** 20)
    lu = up(lu)
    r = F(math.sqrt(float(lu)) * (1 + 1e-14))
    while r * r < lu: r *= 1 + F(1, 10 ** 12)
    return up(r)

def ivnorm_up(Mb):
    """Frobenius upper bound of an interval matrix block (>= spectral norm)."""
    s2 = sum(v.maxabs() ** 2 for row in Mb for v in row)
    from math import isqrt
    root = isqrt(s2)
    if root * root < s2: root += 1
    return F(root, S)

def sub(M, rows, cols): return [[M[i][j] for j in cols] for i in rows]

def metzler(Miv, blocks):
    nb = len(blocks)
    return [[lognorm_up(sub(Miv, blocks[b], blocks[b])) if b == c else ivnorm_up(sub(Miv, blocks[b], blocks[c]))
             for c in range(nb)] for b in range(nb)]

def expB_up(B, h, K=12):
    """Entrywise upper bound of e^{Bh} for B >= 0 (rational): scale by 2^-s until the infinity norm is < 1/2,
    Taylor to K terms plus a geometric tail, then square s times (entries nonnegative, so bounds compose)."""
    nb = len(B)
    nrm0 = max(sum(up(B[i][j] * h) for j in range(nb)) for i in range(nb))
    s = 0
    while nrm0 / 2 ** s >= F(1, 2): s += 1
    hs = h / 2 ** s
    Bh = [[up(B[i][j] * hs) for j in range(nb)] for i in range(nb)]
    nrm = max(sum(r) for r in Bh)
    term = [[F(int(i == j)) for j in range(nb)] for i in range(nb)]
    tot = [row[:] for row in term]
    for k in range(1, K):
        term = [[up(sum(term[i][l] * Bh[l][j] for l in range(nb)) / k) for j in range(nb)] for i in range(nb)]
        tot = [[tot[i][j] + term[i][j] for j in range(nb)] for i in range(nb)]
    tail = up(nrm ** K / math.factorial(K) / (1 - nrm))
    E = [[up(tot[i][j] + tail) for j in range(nb)] for i in range(nb)]
    for _ in range(s):
        E = [[up(sum(E[i][l] * E[l][j] for l in range(nb))) for j in range(nb)] for i in range(nb)]
    return E

def mv(M, v): return [up(sum(M[i][j] * v[j] for j in range(len(v)))) for i in range(len(M))]

def emc(x):   # upper bound of e^{-x}, x >= 0: 1 / (Taylor lower bound of e^x)
    t, tot = F(1), F(1)
    for k in range(1, 30):
        t = t * x / k; tot += t
    return up(1 / tot)

def segment_b(x0, x1, m0, m1, h, P, Pinv, blocks, v0, nsub):
    A = hermite_coeffs(x0, x1, m0, m1, h)
    A1 = [deriv(a) for a in A]; A2 = [deriv(a) for a in A1]
    w = F(1, 2 * nsub); nb = len(blocks); dvec = [F(0)] * nb; boxes = []
    # one full Jacobian over the hull of the reference on [0, h]; per sub-interval J(X) V is split as
    # J(X) Vc (one-direction AD with the rational centre seed) + Jhull (V - Vc), V - Vc of width ~ |xhat''| w h
    Xh = [poly_range(A[i], F(1, 2), F(1, 2))[0] for i in range(N)]
    Jh = jac_box(Xh)
    for j in range(nsub):
        sc = F(2 * j + 1, 2 * nsub)
        X = []; xc = []; V = []; vc = []; Acc = []
        for i in range(N):
            rX, cX = poly_range(A[i], sc, w); X.append(rX); xc.append(cX)
            rV, cV = poly_range(A1[i], sc, w); V.append(rV * I.of(1 / h)); vc.append(cV / h)
            rA, _ = poly_range(A2[i], sc, w); Acc.append(rA * I.of(1 / (h * h)))
        fc = f_point(xc)
        dc = [I.of(vc[i]) - fc[i] for i in range(N)]
        Vc = [I.of(vc[i]) for i in range(N)]
        JV = jv_box(X, Vc)
        dV = [V[k] - Vc[k] for k in range(N)]
        dprime = [Acc[i] - JV[i] - sum((Jh[i][k] * dV[k] for k in range(N)), I.of(0)) for i in range(N)]
        drange = [dc[i] + dprime[i] * pm(w * h) for i in range(N)]
        zd = matvec(Pinv, drange)
        dvec = [max(dvec[b], norm2_up([zd[i] for i in blocks[b]])) for b in range(nb)]
        boxes.append(X)
    G = int(os.environ.get('C9_LNSUB', '1'))
    if G > 1:
        # log-norm matrix per group of sub-intervals (agent H, 18 Oct): one Jacobian over the hull of the whole
        # segment adds |J'| h |f| to every block's log norm (about +0.026 at t ~ 421, more than the -0.0215 contraction).
        # The comparison argument is applied group by group: on group g (length h/G) the deviation obeys the same block
        # inequality with Am_g enclosed over E_g = (reference over that group) + P R_g, and the defect bound dvec holds on
        # the whole segment; R_g is validated by the same a priori test, so v propagates group to group.
        assert nsub % G == 0, (nsub, G)
        hg = h / G; v = list(v0); Rmax = [F(0)] * nb; dmax = [None] * nb; omax = F(-10 ** 9); cmax = F(0); wmax = 0.0
        for g in range(G):
            bx = boxes[g * nsub // G:(g + 1) * nsub // G]
            Xg = [I(min(b[i].lo for b in bx), max(b[i].hi for b in bx)) for i in range(N)]
            Rg = [up(F(13, 10) * (v[b] + dvec[b] * hg) * (1 + hg / 10) + F(1, 10 ** 18)) for b in range(nb)]
            last = None; done = False
            for attempt in range(12):
                E = [Xg[i] + sum((I.of(P[i][k]) * pm(Rg[b]) for b in range(nb) for k in blocks[b]), I.of(0)) for i in range(N)]
                try:
                    Miv = mm_iv_rat(mm_rat_iv(Pinv, jac_box(E)), P)
                except ValueError as exc:
                    segment_b.last_fail = {'R': [float(x) for x in Rg], 'domain': str(exc), 'group': g}
                    return None
                Am = metzler(Miv, blocks)
                c = max(F(0), max(-Am[b][b] for b in range(nb)))
                B = [[Am[b][e] + (c if b == e else 0) for e in range(nb)] for b in range(nb)]
                eB = expB_up(B, hg)
                vmax = mv(eB, [v[b] + dvec[b] * hg for b in range(nb)])
                if all(vmax[b] < Rg[b] for b in range(nb)):
                    ec = emc(c * hg)
                    v = [up(ec * a + hg * b2) for a, b2 in zip(mv(eB, v), mv(eB, dvec))]
                    done = True; break
                last = {'R': [float(x) for x in Rg], 'vmax': [float(x) for x in vmax], 'diag': [float(Am[b][b]) for b in range(nb)], 'group': g}
                Rg = [up(F(13, 10) * max(vmax[b], Rg[b])) for b in range(nb)]
            if not done:
                segment_b.last_fail = last
                return None
            Rmax = [max(a, b) for a, b in zip(Rmax, Rg)]
            dmax = [Am[b][b] if dmax[b] is None else max(dmax[b], Am[b][b]) for b in range(nb)]
            omax = max([omax] + [Am[b][e] for b in range(nb) for e in range(nb) if b != e]); cmax = max(cmax, c)
            wmax = max(wmax, max(float(hi(q) - lo(q)) for q in Xg))
        return {'d': [float(x) for x in dvec], 'v1': v, 'R': [float(x) for x in Rmax], 'c': float(cmax),
                'offmax': float(omax if nb > 1 else 0), 'diag': [float(x) for x in dmax], 'Xw': wmax}
    X = [I(min(b[i].lo for b in boxes), max(b[i].hi for b in boxes)) for i in range(N)]
    R = [up(F(13, 10) * (v0[b] + dvec[b] * h) * (1 + h / 10) + F(1, 10 ** 18)) for b in range(nb)]
    last = None
    for attempt in range(12):
        # E = X + P z with |z_b| <= R_b: componentwise sum over blocks of |P_ib| R_b (column-wise bound)
        E = [X[i] + sum((I.of(P[i][k]) * pm(R[b]) for b in range(nb) for k in blocks[b]), I.of(0)) for i in range(N)]
        try:
            Miv = mm_iv_rat(mm_rat_iv(Pinv, jac_box(E)), P)
        except ValueError as exc:      # the box left the drift's domain (e.g. sqrt of a negative): a failed segment, not a crash
            segment_b.last_fail = {'R': [float(x) for x in R], 'domain': str(exc)}
            return None
        Am = metzler(Miv, blocks)
        c = max(F(0), max(-Am[b][b] for b in range(nb)))
        B = [[Am[b][e] + (c if b == e else 0) for e in range(nb)] for b in range(nb)]
        eB = expB_up(B, h)
        vmax = mv(eB, [v0[b] + dvec[b] * h for b in range(nb)])
        if all(vmax[b] < R[b] for b in range(nb)):
            ec = emc(c * h)
            v1 = [up(ec * a + h * b2) for a, b2 in zip(mv(eB, v0), mv(eB, dvec))]
            return {'d': [float(x) for x in dvec], 'v1': v1, 'R': [float(x) for x in R], 'c': float(c),
                    'offmax': float(max([Am[b][e] for b in range(nb) for e in range(nb) if b != e] or [0])),
                    'diag': [float(Am[b][b]) for b in range(nb)], 'Xw': max(float(hi(v) - lo(v)) for v in X)}
        last = {'R': [float(x) for x in R], 'vmax': [float(x) for x in vmax], 'diag': [float(Am[b][b]) for b in range(nb)],
                'offmax': float(max(Am[b][e] for b in range(nb) for e in range(nb) if b != e)), 'c': float(c)}
        R = [up(F(13, 10) * max(vmax[b], R[b])) for b in range(nb)]
    segment_b.last_fail = last
    return None

def switch(Pn_inv, blocks_n, P, blocks, v):
    T = [[sum(Pn_inv[i][l] * P[l][j] for l in range(N)) for j in range(N)] for i in range(N)]
    return [up(sum(opnorm_rect_up(sub(T, bn, bo)) * v[c] for c, bo in enumerate(blocks))) for bn in blocks_n]

import os
RESET_EVERY = int(os.environ.get('C9_RESET', '0')); RESET_T0 = F(os.environ.get('C9_RESET_T0', '0'))

def run_chain_b(tq, nodes, slopes, P0, Pinv0, blocks0, v_in, k0, k1, out, nsub=6):
    run_chain_b.shift = getattr(run_chain_b, 'shift', F(0))
    import json, time
    v = list(v_in); P, Pinv, blocks = P0, Pinv0, blocks0
    t0 = time.time()
    with open(out, 'w') as fh:
        fh.write(json.dumps({'piece': [k0, k1], 'v_in': [str(x) for x in v], 'blocks_in': blocks,
                             't0': float(tq[k0]), 't1': float(tq[k1])}) + '\n')
        for k in range(k0, k1):
            h = tq[k + 1] - tq[k]
            res = segment_b(nodes[k], nodes[k + 1], slopes[k], slopes[k + 1], h, P, Pinv, blocks, v, nsub)
            if res is None:
                fh.write(json.dumps({'k': k, 'fail': True, 't': float(tq[k]), 'v': [float(x) for x in v],
                                     'diag_fail': getattr(segment_b, 'last_fail', None)}) + '\n'); return None
            Pn, Pinvn, bn = frame_b(fdrive.jac(fl(nodes[k + 1]), ETA_F), nodes[k + 1])
            v = switch(Pinvn, bn, P, blocks, res['v1']); P, Pinv, blocks = Pn, Pinvn, bn
            rs = None
            if RESET_EVERY and tq[k + 1] >= RESET_T0 and (k + 1) % RESET_EVERY == 0:
                rr = reset_b(nodes[k + 1], P, Pinv, blocks, v)
                if rr is not None and norm_v(rr[0]) < norm_v(v):
                    rs = [float(norm_v(v)), float(norm_v(rr[0])), float(rr[1])]; v = rr[0]; run_chain_b.shift += rr[1]
            fh.write(json.dumps({'k': k, 't': float(tq[k]), 'h': float(h), 'v': [float(x) for x in v], 'vx': [str(x) for x in v],
                                 'reset': rs, 'shift': float(run_chain_b.shift), 'R': res['R'],
                                 'diag': res['diag'], 'd': res['d'], 'off': res['offmax'], 'nb': len(blocks), 'Xw': res['Xw'],
                                 'el': round(time.time() - t0, 1)}) + '\n'); fh.flush()
        fh.write(json.dumps({'piece_done': [k0, k1], 'v_out': [str(x) for x in v], 'blocks_out': blocks,
                             'r_out_f': float(norm_v(v)), 'P_sha': frame_sha(P)}) + '\n')
    return v, P, Pinv, blocks

def frame_sha(P):
    # hash of the exact rational frame at a piece boundary: the next piece must rebuild the same frame
    import hashlib
    return hashlib.sha256(';'.join(','.join(str(x) for x in row) for row in P).encode()).hexdigest()

def norm_v(v):
    from math import isqrt
    s = sum(x * x for x in v)
    r = F(math.sqrt(float(s)) * (1 + 1e-12))
    while r * r < s: r *= 1 + F(1, 10 ** 9)
    return up(r)

def reset_b(xr, P, Pinv, blocks, v):
    """Section reset (flow-direction quotient). Tube S = {xr + P z : |z_b| <= v_b} at one node. With g = f(xr), n ~ g/|g|^2
    and tau(x) = -<n, x - xr>, every x in S satisfies phi_tau(x) - xr = (I - g n^T)(x - xr) + int_0^tau (f(phi_s x) - g) ds.
    Returns block radii v' of a set S' with phi_tau(x)(x) in S' for all x in S, |tau| <= tau_m, or None if the a priori box
    does not validate. Valid for the trap: the teacher ball is forward invariant, so a bounded time shift per trajectory is free."""
    nb = len(blocks)
    g = f_point(xr)
    gf = np.array([g[i].mid_float() for i in range(N)]); gn = float(gf @ gf)
    n = [F(float(gf[i] / gn)) for i in range(N)]
    if os.environ.get('C9_FLOWCOL') == '1':
        # any n works in the identity; n = s * (row 0 of P^{-1}) makes n^T P = s e_0 exactly, so the reset leaves the
        # other blocks alone and (nearly) zeroes block 0, the flow direction
        sc = F(1 / float(sum(F(float(gf[i])) * Pinv[0][i] for i in range(N))))
        n = [sc * Pinv[0][i] for i in range(N)]
    c = [sum(n[i] * P[i][k] for i in range(N)) for k in range(N)]                 # n^T P, exact
    tau_m = up(sum(norm_v([c[k] for k in blocks[b]]) * v[b] for b in range(nb)))
    sbox = [I.of(xr[i]) + sum((I.of(P[i][k]) * pm(v[b]) for b in range(nb) for k in blocks[b]), I.of(0)) for i in range(N)]
    T = pm(tau_m)
    Fc = [gi + pm(maxabs(gi) + F(1, 10 ** 12)) for gi in g]                       # first guess: 2|g|
    for attempt in range(8):
        B = [sbox[i] + T * Fc[i] for i in range(N)]
        try:
            fB = [r.v for r in drv(B)]
        except ValueError:
            return None
        new = [sbox[i] + T * fB[i] for i in range(N)]
        if all(B[i].lo < new[i].lo and new[i].hi < B[i].hi for i in range(N)):
            break
        Fc = [hull(Fc[i], fB[i]) + pm(maxabs(fB[i]) / 2 + F(1, 10 ** 12)) for i in range(N)]
    else:
        return None
    rz = matvec(Pinv, [T * (fB[i] - g[i]) for i in range(N)])                     # remainder in frame coordinates
    a = matvec(Pinv, g)
    amid = [F(x.lo + x.hi, 2 * S) for x in a]
    aerr = [maxabs(a[i] - I.of(amid[i])) for i in range(N)]
    Mmid = [[(1 if i == j else 0) - amid[i] * c[j] for j in range(N)] for i in range(N)]
    vn = []
    for cb, bc in enumerate(blocks):
        acc = norm2_up([rz[i] for i in bc])
        ae = norm_v([aerr[i] for i in bc]) if any(aerr[i] for i in bc) else F(0)
        for b, bo in enumerate(blocks):
            if v[b] == 0: continue
            acc += (opnorm_rect_up(sub(Mmid, bc, bo)) + ae * norm_v([c[k] for k in bo])) * v[b]
        vn.append(up(acc))
    return vn, tau_m
