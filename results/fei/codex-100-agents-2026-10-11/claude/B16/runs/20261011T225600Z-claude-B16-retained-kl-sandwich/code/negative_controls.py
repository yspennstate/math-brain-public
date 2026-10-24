"""Negative controls: the Part-1 checks must trip on deliberately wrong constants (n=3 and n=4, all functions, root nodes)."""
import math, json, sys
import numpy as np

LN2 = math.log(2.0)


def fwht(a):
    a = a.astype(np.int64).copy(); n = a.shape[-1]; h = 1
    while h < n:
        a = a.reshape(a.shape[0], -1, 2, h)
        x = a[:, :, 0, :].copy(); y = a[:, :, 1, :].copy()
        a[:, :, 0, :] = x + y; a[:, :, 1, :] = x - y
        a = a.reshape(a.shape[0], n); h *= 2
    return a


def ent(p):
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(p > 0, -p * np.log2(np.where(p > 0, p, 1.0)), 0.0).sum(axis=1)


res = {}
for n in (3, 4):
    L = 2 ** n; N = 2 ** L
    idx = np.arange(N, dtype=np.int64)[:, None]
    tt = (1 - 2 * ((idx >> np.arange(L, dtype=np.int64)[None, :]) & 1)).astype(np.int64)
    g = tt[:, 0::2]; h = tt[:, 1::2]
    A = fwht(g); Bh = fwht(h)
    U2 = (A + Bh) ** 2 / float(4 ** n); V2 = (A - Bh) ** 2 / float(4 ** n)
    q = U2 + V2; mm = np.minimum(U2, V2)
    with np.errstate(divide="ignore", invalid="ignore"):
        Q = np.where(mm > 0, mm * np.log2(np.where(mm > 0, q / np.where(mm > 0, mm, 1), 1)), 0).sum(axis=1)
        rest = q - mm
        B = Q + np.where(rest > 0, rest * np.log2(np.where(rest > 0, q / np.where(rest > 0, rest, 1), 1)), 0).sum(axis=1)
    M = mm.sum(axis=1)
    P = (A / 2.0 ** (n - 1)) ** 2; Qc = (Bh / 2.0 ** (n - 1)) ** 2
    JS = ent((P + Qc) / 2) - (ent(P) + ent(Qc)) / 2
    Delta = ent(np.concatenate([U2, V2], axis=1)) - (ent(P) + ent(Qc)) / 2
    res[n] = {
        "true: max(B-Q-M/ln2) (expect <=0)": float(np.max(B - Q - M / LN2)),
        "false: max(B-Q-0.5M/ln2) (expect >0)": float(np.max(B - Q - 0.5 * M / LN2)),
        "false: max(Q-B+0.01M) (expect >0)": float(np.max(Q - B + 0.01 * M)),
        "true: max(JS-2M/ln2) (expect <=0)": float(np.max(JS - 2 * M / LN2)),
        "false: max(JS-M/ln2) (expect >0)": float(np.max(JS - M / LN2)),
        "false: max(Delta-Q-2M/ln2) (expect >0)": float(np.max(Delta - Q - 2 * M / LN2)),
        "true: max(Delta-Q-3M/ln2) (expect <=0)": float(np.max(Delta - Q - 3 * M / LN2)),
        "tightness: max (Delta-Q)/(M/ln2) over M>0": float(np.max(np.where(M > 0, (Delta - Q) / np.where(M > 0, M / LN2, 1), 0))),
    }
out = sys.argv[1] if len(sys.argv) > 1 else "."
with open(f"{out}/negative_controls.json", "w", encoding="utf-8") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1))
