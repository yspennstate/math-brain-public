"""Exhaustive scan over all Boolean functions on n<=4 bits (floating logs: EVIDENCE)."""
import numpy as np, json, sys
from feilib import *

def scan(n):
    T = all_tables(n).astype(np.int64)
    N = 1 << n
    Hd = hadamard(n)
    W = T @ Hd.T                      # W[f,S] exact integers
    p = (W.astype(np.float64) / N) ** 2
    H = entropy(p)
    inf = influences(p, n)
    I = inf.sum(-1)
    Bi = erasure_terms(p, n)
    B = Bi.sum(-1)
    # restriction entropies
    Hd1 = hadamard(n - 1)
    D = np.zeros_like(Bi)
    for i in range(n):
        tp = restrict(T, n, i, 0); tm = restrict(T, n, i, 1)
        pp = ((tp @ Hd1.T).astype(np.float64) / (N // 2)) ** 2
        pm = ((tm @ Hd1.T).astype(np.float64) / (N // 2)) ** 2
        D[:, i] = H - 0.5 * (entropy(pp) + entropy(pm))
    Var = 1 - p[:, 0]
    TCv = binh(inf).sum(-1) - H
    return dict(T=T, p=p, H=H, I=I, inf=inf, Bi=Bi, B=B, D=D, Var=Var, TC=TCv)

if __name__ == "__main__":
    out = {}
    for n in [2, 3, 4]:
        r = scan(n)
        nc = r['I'] > 0
        H, I, B, D, Bi, inf = r['H'][nc], r['I'][nc], r['B'][nc], r['D'][nc], r['Bi'][nc], r['inf'][nc]
        ratio = H / I
        k = int(np.argmax(ratio))
        # local constants: min over relevant coordinates
        with np.errstate(divide='ignore', invalid='ignore'):
            locB = np.where(inf > 1e-15, Bi / inf, np.inf).min(-1)
            locD = np.where(inf > 1e-15, D / inf, np.inf).min(-1)
            JS = D - Bi
        res = dict(
            n=n, count=int(nc.sum()),
            max_H_over_I=float(ratio.max()),
            argmax_table=r['T'][nc][k].tolist(),
            max_B_over_I=float((B / I).max()),
            K_loc=float(locB.max()), K_Delta=float(locD.max()),
            max_DTC_over_I=float(((H - B) / I).max()),
            min_JS=float(JS.min()), max_JS_over_inf=float(np.nanmax(np.where(inf>1e-15, JS/np.minimum(inf,1-inf+1e-300), 0))),
            max_Delta=float(D.max()),
        )
        out[n] = res
        print(json.dumps({k2: v for k2, v in res.items() if k2 != 'argmax_table'}))
        print('argmax table', res['argmax_table'])
    json.dump(out, open('../data/exhaust_n2_4.json', 'w'), indent=1)
