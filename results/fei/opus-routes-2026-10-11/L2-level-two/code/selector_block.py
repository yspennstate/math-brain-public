"""Blocks with signed-character fibers (NOTES section 5e), by brute force (n <= 20).

Coordinates split into an address block X and a data block Y. The block Y has signed-character fibers if for every x
the fiber y -> F(x, y) equals s(x) chi_{tau(x)}(y). Then, with R_T = P(tau(X) = T) and A_T = tau^{-1}(T):
  (a) sum_{t in Y} B_t <= sum_{t in Y} H(S_t | S_{Y - t}) <= H(S_Y)            (erasure entropy <= entropy)
  (b) H(S_Y) = H(tau(X))                                                       (S_Y has the law of tau(X))
  (c) E[|S_X| | S_Y = T] >= (1/2) log2(1/R_T), so H(S_Y) <= 2 I_X             (Harper on each fiber function s 1_{A_T})
  (d) B_X = sum_T R_T B(nu_T), nu_T the normalized spectral law of s 1_{A_T}  (S - x contains S_Y; B is 1-homogeneous)
For a general block only (a) holds, together with H(S_Y) = avg_x H(F_x) + I(X; tau-channel) <= avg_x H(F_x)
+ (2/ln 2) I_X (SEL-selector-interference NOTES 3.1 (i), (ii): the BR theorem); the general rows check that bound and
show that (c) fails without the fiber hypothesis.
Every quantity of (a)-(d) is computed twice: from the full Walsh spectrum of F and from the fiber functions
(Walsh transforms on X and on Y separately).
Usage: python -B selector_block.py OUTJSON
"""
import sys, os, json, math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import general_witness as gw   # noqa: E402  (constructors, walsh, phi_vec, popcount)
import pivotal_faces as pf     # noqa: E402  (selector constructors)

LN2 = math.log(2)


def ent(w):
    w = np.asarray(w, float)
    w = w[w > 0]
    return float(-(w * np.log2(w)).sum())


def compress(idx, bits):
    out = np.zeros_like(idx)
    for k, b in enumerate(bits):
        out |= ((idx >> b) & 1) << k
    return out


def walsh_rows(M):
    """Walsh transform (normalized as gw.walsh) of every row of M"""
    a = M.astype(float).copy()
    r, N = a.shape
    n = N.bit_length() - 1
    for k in range(n):
        a = a.reshape(r, -1, 2, 1 << k)
        u, w = a[:, :, 0, :].copy(), a[:, :, 1, :].copy()
        a[:, :, 0, :], a[:, :, 1, :] = u + w, u - w
        a = a.reshape(r, N)
    return a / N


def B_of_law(p, bits=None):
    """B = sum_i H(S_i | S - i) for a law p on subsets of len(p).bit_length()-1 coordinates (bits: which i to sum)"""
    N = len(p)
    n = N.bit_length() - 1
    idx = np.arange(N, dtype=np.int64)
    out = []
    for i in (range(n) if bits is None else bits):
        lo = idx[(idx >> i) & 1 == 0]
        out.append(float(gw.phi_vec(p[lo], p[lo | (1 << i)]).sum()))
    return out


def analyse(T, name, Y):
    N = len(T)
    n = N.bit_length() - 1
    Y = sorted(Y)
    X = [b for b in range(n) if b not in Y]
    idx = np.arange(N, dtype=np.int64)
    p = gw.walsh(T) ** 2
    Bs = B_of_law(p)
    BY = sum(Bs[t] for t in Y)
    BX = sum(Bs[x] for x in X)
    I = float((gw.popcount(idx) * p).sum())
    xc, yc = compress(idx, X), compress(idx, Y)
    IX = float((gw.popcount(xc) * p).sum())
    # marginal of S_Y and the erasure bound (a)
    RY = np.bincount(yc, weights=p, minlength=1 << len(Y))
    HSY = ent(RY)
    erasY = sum(B_of_law(RY))          # sum_t H(S_t | S_{Y - t}) under the marginal law of S_Y
    # fibers: M[x, y] = F(x, y), fiber spectra on Y, slice functions on X
    M = np.zeros((1 << len(X), 1 << len(Y)), dtype=np.int8)
    M[xc, yc] = T
    FW = walsh_rows(M)                 # FW[x, T] = fiber Walsh coefficient
    avgHfib = float(np.mean([ent(row ** 2) for row in FW]))
    nz = np.abs(FW) > 1e-9
    signed_char = bool(np.all(nz.sum(1) == 1) and np.all(np.abs(np.abs(FW[nz]) - 1) < 1e-9))
    row = dict(name=name, n=n, X=len(X), Y=len(Y), signed_char=signed_char, I=I, IX=IX, IY=I - IX, B=sum(Bs), BX=BX,
               BY=BY, erasY=erasY, HSY=HSY, avgHfib=avgHfib, sum_h2_Y=float(sum(pf.h2(float(RY[(np.arange(len(RY)) >> k) & 1 == 1].sum())) for k in range(len(Y)))))
    row["general_bound"] = avgHfib + 2 / LN2 * IX
    errs = {}
    if signed_char:
        tau = np.argmax(nz, axis=1)
        s = np.sign(FW[np.arange(len(FW)), tau])
        R = np.bincount(tau, minlength=1 << len(Y)) / len(tau)
        errs["H(tau) vs H(S_Y)"] = abs(ent(R) - HSY)
        # slice functions G_T = s 1_{A_T} on X: their spectra, Harper per fiber, and identity (d)
        harper_slack = math.inf
        BX_fib = 0.0
        IX_fib = 0.0
        joint_err = 0.0
        P2 = np.zeros((1 << len(X), 1 << len(Y)))
        P2[xc, yc] = p
        for Tv in np.nonzero(R)[0]:
            G = np.where(tau == Tv, s, 0.0)
            gh = gw.walsh(G) ** 2
            RT = float(R[Tv])
            lev = float((gw.popcount(np.arange(len(gh), dtype=np.int64)) * gh).sum()) / RT
            harper_slack = min(harper_slack, lev - 0.5 * math.log2(1 / RT))
            BX_fib += RT * sum(B_of_law(gh / RT))
            IX_fib += RT * lev
            # the full spectrum restricted to S_Y = T must equal gh, coefficient by coefficient
            joint_err = max(joint_err, float(np.abs(P2[:, Tv] - gh).max()))
        errs["mass off the support of tau"] = float(P2[:, R == 0].sum())
        errs["B_X vs sum_T R_T B(nu_T)"] = abs(BX - BX_fib)
        errs["I_X vs fibers"] = abs(IX - IX_fib)
        errs["p(U,T) vs slice spectra"] = joint_err
        row["harper_min_slack"] = harper_slack
        row["lemma_ratio"] = BY / (2 * IX) if IX > 0 else float("nan")
    row["err"] = errs
    return row


def and2_power(N):
    """F(y, t) = prod_k (-1)^{t_k (1 - y_k)}: y = bits 0..N-1, t = bits N..2N-1"""
    idx = np.arange(1 << (2 * N), dtype=np.int64)
    par = np.zeros(len(idx), dtype=np.int64)
    for k in range(N):
        par ^= ((idx >> (N + k)) & 1) & (1 - ((idx >> k) & 1))
    return (1 - 2 * par).astype(np.int8)


def product(T1, T2):
    """F(u, v) = T1(u) T2(v), u = low bits"""
    return (np.outer(T2.astype(np.int64), T1.astype(np.int64)).reshape(-1)).astype(np.int8)


def dummy(T, d):
    """T on the high bits, d dummy low bits"""
    return np.repeat(T, 1 << d).astype(np.int8)


def main():
    out = sys.argv[1]
    cases = [
        ("X009 m6", lambda: gw.x009(6), [6]), ("X009 m10", lambda: gw.x009(10), [10]), ("X009 m14", lambda: gw.x009(14), [14]),
        ("sel cube m12 k4", lambda: pf.sel_cube(12, 4), [12]), ("sel cube m12 k8", lambda: pf.sel_cube(12, 8), [12]),
        ("sel rand m12 eps2^-4", lambda: pf.sel_random(12, 4, 1), [12]), ("sel rand m14 eps2^-6", lambda: pf.sel_random(14, 6, 3), [14]),
        ("sel many m6 N8 eps2^-2", lambda: pf.sel_many(6, 8, 2, 4), list(range(6, 14))),
        ("sel many m8 N8 eps2^-3", lambda: pf.sel_many(8, 8, 3, 5), list(range(8, 16))),
        ("sel many m8 N12 eps2^-4", lambda: pf.sel_many(8, 12, 4, 6), list(range(8, 20))),
        ("X009 m4 x X009 m4", lambda: product(gw.x009(4), gw.x009(4)), [4, 9]),
        ("X009 m6 x X009 m6", lambda: product(gw.x009(6), gw.x009(6)), [6, 13]),
        ("address 3", lambda: gw.address(3), list(range(3, 11))), ("address 4", lambda: gw.address(4), list(range(4, 20))),
        ("AND2^4", lambda: and2_power(4), list(range(4, 8))), ("AND2^6", lambda: and2_power(6), list(range(6, 12))),
        ("AND2^8", lambda: and2_power(8), list(range(8, 16))),
        ("x0*bent m4", lambda: gw.x0bent(4), [0]),
        ("majority 9, Y={0}", lambda: gw.majority(9), [0]), ("tribes 3x3, Y={0}", lambda: gw.tribes(3, 3), [0]),
        # general blocks (fibers not signed characters): only (a) and the SEL/BR form apply
        ("tribes 3x3, Y=tribe 0", lambda: gw.tribes(3, 3), [0, 1, 2]),
        ("majority 9, Y={0,1,2}", lambda: gw.majority(9), [0, 1, 2]),
        ("andor d3, Y=subtree", lambda: gw.andor(3), [0, 1, 2, 3]),
        ("X009 m6, Y=bent block", lambda: gw.x009(6), list(range(6))),
        ("MAJ3(y) + 3 dummies", lambda: dummy(gw.majority(3), 3), [3, 4, 5]),
    ]
    rows = []
    for name, mk, Y in cases:
        r = analyse(mk(), name, Y)
        rows.append(r)
        e = max(r["err"].values()) if r["err"] else 0.0
        tail = (f"lemma B_Y/(2I_X)={r['lemma_ratio']:.4f} harper_slack={r['harper_min_slack']:.4f}"
                if r["signed_char"] else f"general bound={r['general_bound']:.4f} 2I_X={2 * r['IX']:.4f}")
        print(f"{name:24s} n={r['n']:2d} |Y|={r['Y']:2d} sc={int(r['signed_char'])} I={r['I']:.4f} I_X={r['IX']:.4f} "
              f"B={r['B']:.4f} B_X={r['BX']:.4f} B_Y={r['BY']:.4f} eras_Y={r['erasY']:.4f} H(S_Y)={r['HSY']:.4f} "
              f"sum_h2_Y={r['sum_h2_Y']:.4f} avgH(F_x)={r['avgHfib']:.4f} | {tail} maxerr={e:.1e}", flush=True)
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(dict(rows=rows), fh, indent=1)
    print("wrote", out, len(rows), "functions")


if __name__ == "__main__":
    main()
