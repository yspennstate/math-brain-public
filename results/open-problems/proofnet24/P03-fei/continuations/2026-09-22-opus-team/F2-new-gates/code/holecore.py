"""Partial cores with holes filled by fresh dictators.

A partial core is c0 : {0,1}^m -> {-1,0,+1}, sum c0 = 0.  The cells with c0 = 0 are
holes; each connected component A of the hole set (in the hypercube graph) is filled
by one fresh variable y_A (value y_A on every cell of A).  The resulting Boolean
function F on m + #components variables is balanced and

  H(F) = sum_S phi(W0(S)/N) + sum_A sum_S phi(W_A(S)/N),     phi(t) = t^2 log2(1/t^2)
  I(F) = [ sum_{edges xy} (c0(x)-c0(y))^2 + sum_A ((m+2)|A| - 2 e(A)) ] / (2N)

with N = 2^m, W0 = Walsh(c0), W_A = Walsh(1_A), e(A) = number of hypercube edges inside A.
(Derivation and exact check against Numaro's 18-variable table: decompose_numaro.py.)

This module gives float evaluation and a numba simulated-annealing search over
balanced two-cell moves.
"""
import numpy as np
import numba as nb
from math import log2


@nb.njit(cache=True)
def fwht_int(a):
    a = a.copy()
    n = a.shape[0]
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x = a[j]; y = a[j + h]
                a[j] = x + y; a[j + h] = x - y
        h *= 2
    return a


@nb.njit(cache=True)
def make_phi(N):
    # phi_tab[v] = (v/N)^2 log2(N^2/v^2)
    t = np.zeros(N + 1)
    for v in range(1, N + 1):
        p = (v / N) ** 2
        t[v] = -p * np.log2(p)
    return t


@nb.njit(cache=True)
def make_par(N):
    par = np.zeros(N, dtype=np.int64)
    for v in range(N):
        x = v; c = 0
        while x:
            c ^= 1; x &= x - 1
        par[v] = c
    return par


@nb.njit(cache=True)
def core_I2(c0, m):
    N = c0.shape[0]
    s = 0
    for x in range(N):
        for i in range(m):
            y = x ^ (1 << i)
            if y > x:
                d = c0[x] - c0[y]
                s += d * d
    return s


@nb.njit(cache=True)
def aux_part(c0, m, phi, par):
    """Return (Haux, Iaux2, ncomp, maxcomp) for the hole components of c0."""
    N = c0.shape[0]
    lab = -np.ones(N, dtype=np.int64)
    stack = np.empty(N, dtype=np.int64)
    comp = np.empty(N, dtype=np.int64)
    Haux = 0.0
    Iaux2 = 0
    ncomp = 0
    maxc = 0
    for x0 in range(N):
        if c0[x0] != 0 or lab[x0] >= 0:
            continue
        # BFS
        top = 0; stack[top] = x0; top += 1; lab[x0] = ncomp
        k = 0
        while top > 0:
            top -= 1
            x = stack[top]
            comp[k] = x; k += 1
            for i in range(m):
                y = x ^ (1 << i)
                if c0[y] == 0 and lab[y] < 0:
                    lab[y] = ncomp
                    stack[top] = y; top += 1
        # internal edges
        e = 0
        for a in range(k):
            x = comp[a]
            for i in range(m):
                y = x ^ (1 << i)
                if y > x and c0[y] == 0:
                    e += 1
        Iaux2 += (m + 2) * k - 2 * e
        if k == 1:
            Haux += 2.0 * m / N
        elif k == 2:
            Haux += 4.0 * (m - 1) / N
        elif k <= 2 * m:
            h = 0.0
            for S in range(N):
                w = 0
                for a in range(k):
                    w += 1 - 2 * par[S & comp[a]]
                if w < 0:
                    w = -w
                h += phi[w]
            Haux += h
        else:
            ind = np.zeros(N, dtype=np.int64)
            for a in range(k):
                ind[comp[a]] = 1
            Wc = fwht_int(ind)
            h = 0.0
            for S in range(N):
                h += phi[abs(Wc[S])]
            Haux += h
        if k > maxc:
            maxc = k
        ncomp += 1
    return Haux, Iaux2, ncomp, maxc


@nb.njit(cache=True)
def evaluate(c0, m, phi, par):
    N = c0.shape[0]
    W = fwht_int(c0)
    Hc = 0.0
    for S in range(N):
        v = W[S]
        if v < 0:
            v = -v
        Hc += phi[v]
    I2c = core_I2(c0, m)
    Ha, I2a, nc, mx = aux_part(c0, m, phi, par)
    H = Hc + Ha
    I = (I2c + I2a) / (2.0 * N)
    return H, I, Hc, I2c, Ha, I2a, nc, mx


@nb.njit(cache=True)
def local_I2_delta(c0, m, x, newx, y, newy):
    """Change of sum_{edges}(c0(u)-c0(v))^2 when x->newx, y->newy (x != y)."""
    d = 0
    ox = c0[x]; oy = c0[y]
    for i in range(m):
        u = x ^ (1 << i)
        if u == y:
            continue
        cu = c0[u]
        d += (newx - cu) ** 2 - (ox - cu) ** 2
    for i in range(m):
        u = y ^ (1 << i)
        if u == x:
            continue
        cu = c0[u]
        d += (newy - cu) ** 2 - (oy - cu) ** 2
    if (x ^ y) & ((x ^ y) - 1) == 0:  # adjacent
        d += (newx - newy) ** 2 - (ox - oy) ** 2
    return d


@nb.njit(cache=True)
def anneal(c0_init, m, iters, T0, T1, seed, phi, par, max_holes, allow_holes):
    np.random.seed(seed)
    N = c0_init.shape[0]
    c0 = c0_init.copy()
    W = fwht_int(c0)
    phiW = np.empty(N)
    Hc = 0.0
    for S in range(N):
        v = abs(W[S]); phiW[S] = phi[v]; Hc += phiW[S]
    I2c = core_I2(c0, m)
    Ha, I2a, nc, mx = aux_part(c0, m, phi, par)
    nholes = 0
    for x in range(N):
        if c0[x] == 0:
            nholes += 1
    R = (Hc + Ha) / ((I2c + I2a) / (2.0 * N) - 1.0)
    best = c0.copy(); bestR = R
    acc = 0
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        x = np.random.randint(N)
        a = c0[x]
        if allow_holes:
            r = np.random.randint(2)
            na = -1 if a != -1 else 0
            if a == -1:
                na = 0 if r == 0 else 1
            elif a == 0:
                na = -1 if r == 0 else 1
            else:
                na = -1 if r == 0 else 0
        else:
            if a == 0:
                continue
            na = -a
        dlt = na - a
        y = np.random.randint(N)
        if y == x:
            continue
        b = c0[y]
        nb_ = b - dlt
        if nb_ < -1 or nb_ > 1:
            continue
        # hole count
        dh = 0
        if a == 0: dh -= 1
        if na == 0: dh += 1
        if b == 0: dh -= 1
        if nb_ == 0: dh += 1
        if nholes + dh > max_holes:
            continue
        # core entropy delta
        dH = 0.0
        db = nb_ - b
        for S in range(N):
            v = W[S] + dlt * (1 - 2 * par[S & x]) + db * (1 - 2 * par[S & y])
            if v < 0:
                v = -v
            dH += phi[v] - phiW[S]
        dI2 = local_I2_delta(c0, m, x, na, y, nb_)
        # aux part
        if a == 0 or na == 0 or b == 0 or nb_ == 0:
            c0[x] = na; c0[y] = nb_
            Ha2, I2a2, nc2, mx2 = aux_part(c0, m, phi, par)
            c0[x] = a; c0[y] = b
        else:
            Ha2 = Ha; I2a2 = I2a
        Hn = Hc + dH + Ha2
        In = (I2c + dI2 + I2a2) / (2.0 * N)
        if In <= 1.0:
            continue
        Rn = Hn / (In - 1.0)
        if Rn >= R or np.random.random() < np.exp((Rn - R) / T):
            c0[x] = na; c0[y] = nb_
            for S in range(N):
                W[S] += dlt * (1 - 2 * par[S & x]) + db * (1 - 2 * par[S & y])
                phiW[S] = phi[abs(W[S])]
            Hc += dH; I2c += dI2; Ha = Ha2; I2a = I2a2; nholes += dh
            R = Rn
            acc += 1
            if R > bestR:
                bestR = R; best[:] = c0
    return best, bestR, acc


def summarize(c0, m):
    N = 1 << m
    phi = make_phi(N); par = make_par(N)
    H, I, Hc, I2c, Ha, I2a, nc, mx = evaluate(np.asarray(c0, dtype=np.int64), m, phi, par)
    return dict(H=H, I=I, R=H / (I - 1), Hc=Hc, Icore=I2c / (2 * N), Ha=Ha, Iaux=I2a / (2 * N),
                ncomp=int(nc), maxcomp=int(mx), holes=int((np.asarray(c0) == 0).sum()), nvars=m + int(nc))


@nb.njit(cache=True)
def scan_2cell(c0_in, m, phi, par, max_holes, topk):
    """Exhaustive scan of balanced two-cell moves. Returns arrays of the topk
    (R, x, newx, y, newy) by resulting ratio."""
    N = c0_in.shape[0]
    c0 = c0_in.copy()
    W = fwht_int(c0)
    phiW = np.empty(N)
    Hc = 0.0
    for S in range(N):
        phiW[S] = phi[abs(W[S])]; Hc += phiW[S]
    I2c = core_I2(c0, m)
    Ha, I2a, nc, mx = aux_part(c0, m, phi, par)
    nholes = 0
    for x in range(N):
        if c0[x] == 0:
            nholes += 1
    outR = np.full(topk, -1e9); outm = np.zeros((topk, 4), dtype=np.int64)
    for x in range(N):
        a = c0[x]
        for na in (-1, 0, 1):
            if na == a:
                continue
            dlt = na - a
            for y in range(x + 1, N):
                b = c0[y]
                nb_ = b - dlt
                if nb_ < -1 or nb_ > 1 or nb_ == b:
                    continue
                dh = 0
                if a == 0: dh -= 1
                if na == 0: dh += 1
                if b == 0: dh -= 1
                if nb_ == 0: dh += 1
                if nholes + dh > max_holes:
                    continue
                db = nb_ - b
                dH = 0.0
                for S in range(N):
                    v = W[S] + dlt * (1 - 2 * par[S & x]) + db * (1 - 2 * par[S & y])
                    if v < 0:
                        v = -v
                    dH += phi[v] - phiW[S]
                dI2 = local_I2_delta(c0, m, x, na, y, nb_)
                if a == 0 or na == 0 or b == 0 or nb_ == 0:
                    c0[x] = na; c0[y] = nb_
                    Ha2, I2a2, nc2, mx2 = aux_part(c0, m, phi, par)
                    c0[x] = a; c0[y] = b
                else:
                    Ha2 = Ha; I2a2 = I2a
                In = (I2c + dI2 + I2a2) / (2.0 * N)
                if In <= 1.0:
                    continue
                Rn = (Hc + dH + Ha2) / (In - 1.0)
                # insert into top list
                if Rn > outR[topk - 1]:
                    j = topk - 1
                    while j > 0 and outR[j - 1] < Rn:
                        outR[j] = outR[j - 1]; outm[j] = outm[j - 1]; j -= 1
                    outR[j] = Rn
                    outm[j, 0] = x; outm[j, 1] = na; outm[j, 2] = y; outm[j, 3] = nb_
    return outR, outm


@nb.njit(cache=True)
def enum_orbits(rep, sgn, orbit_list, m, phi, par, topk, need_balance):
    """Exhaustive enumeration of v in {-1,0,1}^k on the listed orbits (other orbits 0).
    Returns top-k ratios and the value vectors."""
    N = 1 << m
    k = orbit_list.shape[0]
    no = 0
    for x in range(N):
        if rep[x] + 1 > no:
            no = rep[x] + 1
    v = np.zeros(no, dtype=np.int64)
    digits = np.zeros(k, dtype=np.int64)  # 0,1,2 -> -1,0,1
    for j in range(k):
        digits[j] = 0
        v[orbit_list[j]] = -1
    outR = np.full(topk, -1e9); outV = np.zeros((topk, no), dtype=np.int64)
    total = 1
    for j in range(k):
        total *= 3
    c0 = np.zeros(N, dtype=np.int64)
    for t in range(total):
        # build c0
        s = 0
        for x in range(N):
            c0[x] = sgn[x] * v[rep[x]]
            s += c0[x]
        ok = True
        if need_balance and s != 0:
            ok = False
        if ok:
            W = fwht_int(c0)
            Hc = 0.0
            for S in range(N):
                Hc += phi[abs(W[S])]
            I2c = core_I2(c0, m)
            Ha, I2a, nc, mx = aux_part(c0, m, phi, par)
            I = (I2c + I2a) / (2.0 * N)
            if I > 1.0 + 1e-12:
                R = (Hc + Ha) / (I - 1.0)
                if R > outR[topk - 1]:
                    j = topk - 1
                    while j > 0 and outR[j - 1] < R:
                        outR[j] = outR[j - 1]; outV[j] = outV[j - 1]; j -= 1
                    outR[j] = R; outV[j] = v
        # increment
        j = 0
        while j < k:
            digits[j] += 1
            if digits[j] < 3:
                v[orbit_list[j]] = digits[j] - 1
                break
            digits[j] = 0
            v[orbit_list[j]] = -1
            j += 1
    return outR, outV


@nb.njit(cache=True)
def aux_part2(c0, m, phi, par, Ct):
    """Like aux_part, but each connected hole component is either one group or split by a greedy edge matching into
    pairs (+ singletons), whichever has larger H - Ct*I.  Returns (Haux, Iaux2, ngroups, grp) where grp[x] is the
    group id of hole x (-1 for non-holes)."""
    N = c0.shape[0]
    lab = -np.ones(N, dtype=np.int64)
    grp = -np.ones(N, dtype=np.int64)
    stack = np.empty(N, dtype=np.int64)
    comp = np.empty(N, dtype=np.int64)
    mate = -np.ones(N, dtype=np.int64)
    Haux = 0.0
    Iaux2 = 0
    ng = 0
    ncomp = 0
    for x0 in range(N):
        if c0[x0] != 0 or lab[x0] >= 0:
            continue
        top = 0; stack[top] = x0; top += 1; lab[x0] = ncomp
        k = 0
        while top > 0:
            top -= 1
            x = stack[top]
            comp[k] = x; k += 1
            for i in range(m):
                y = x ^ (1 << i)
                if c0[y] == 0 and lab[y] < 0:
                    lab[y] = ncomp
                    stack[top] = y; top += 1
        e = 0
        for a in range(k):
            x = comp[a]
            for i in range(m):
                y = x ^ (1 << i)
                if y > x and c0[y] == 0:
                    e += 1
        # option A: whole component (only evaluated up to 64 cells; larger components are matched)
        IA = (m + 2) * k - 2 * e
        if k == 1:
            HA = 2.0 * m / N
        elif k == 2:
            HA = 4.0 * (m - 1) / N
        elif k > 64:
            HA = -1e9
        else:
            ind = np.zeros(N, dtype=np.int64)
            for a in range(k):
                ind[comp[a]] = 1
            Wc = fwht_int(ind)
            HA = 0.0
            for S in range(N):
                HA += phi[abs(Wc[S])]
        # option B: greedy matching
        npairs = 0
        if k > 2:
            for a in range(k):
                x = comp[a]
                if mate[x] >= 0:
                    continue
                for i in range(m):
                    y = x ^ (1 << i)
                    if c0[y] == 0 and mate[y] < 0 and y != x:
                        mate[x] = y; mate[y] = x; npairs += 1
                        break
            nsing = k - 2 * npairs
            HB = npairs * 4.0 * (m - 1) / N + nsing * 2.0 * m / N
            IB = npairs * (2 * (m + 2) - 2) + nsing * (m + 2)
        else:
            HB = -1e9; IB = 0
        if k > 2 and HB - Ct * IB / (2.0 * N) > HA - Ct * IA / (2.0 * N):
            Haux += HB; Iaux2 += IB
            for a in range(k):
                x = comp[a]
                if grp[x] < 0:
                    if mate[x] >= 0:
                        grp[x] = ng; grp[mate[x]] = ng
                    else:
                        grp[x] = ng
                    ng += 1
        else:
            Haux += HA; Iaux2 += IA
            for a in range(k):
                grp[comp[a]] = ng
            ng += 1
        for a in range(k):
            mate[comp[a]] = -1
        ncomp += 1
    return Haux, Iaux2, ng, grp


def groups_of(c0, m, Ct=6.52):
    N = 1 << m
    Ha, I2a, ng, grp = aux_part2(np.asarray(c0, dtype=np.int64), m, make_phi(N), make_par(N), Ct)
    groups = [[] for _ in range(ng)]
    for x in range(N):
        if grp[x] >= 0:
            groups[grp[x]].append(int(x))
    return groups, Ha, I2a


def summarize2(c0, m, Ct=6.52):
    N = 1 << m
    c0 = np.asarray(c0, dtype=np.int64)
    phi = make_phi(N); par = make_par(N)
    W = fwht_int(c0)
    Hc = 0.0
    for S in range(N):
        Hc += phi[abs(W[S])]
    I2c = core_I2(c0, m)
    Ha, I2a, ng, grp = aux_part2(c0, m, phi, par, Ct)
    H = Hc + Ha; I = (I2c + I2a) / (2.0 * N)
    return dict(H=H, I=I, R=H / (I - 1), Hc=Hc, Ha=Ha, holes=int((c0 == 0).sum()), ngroups=int(ng), nvars=m + int(ng),
                balance=int(c0.sum()))
