"""O5 seen from the other side: on tribes a one-block witness pays what the level statistic cannot.

Tribes_{w,s}: f = -1 iff some block of w coordinates is all ones.  Spectrum (closed form): with
alpha = (1 - 2^-w)^2, beta = 4^-w, q0 = 1 - 2^-w, p(S) = 4 prod_t (alpha if S misses block t else beta) for S != empty,
p(empty) = (2 q0^s - 1)^2 (Parseval: alpha + (2^w - 1) beta = q0).  For i in block t0 and the witness W_i = S cap (block - i):
  eps_i       = 2^{1-w} q0^{s-1},   y = 4 beta q0^{s-1} = eps_i / 2^{w-1}
  H(S_i|W_i)  = (2^{w-1} - 1) 2y + phi(Z, y),   Z = P(S misses block t0) = p(empty) + 4 alpha (q0^{s-1} - alpha^{s-1})
  B_i         = (2^{w-1} - 1) 2y + 4 phi(alpha, beta) (q0^{s-1} - alpha^{s-1}) + phi(p(empty), 4 beta alpha^{s-1})
Since W_i is a function of S - i, B_i = H(S_i | S - i) <= H(S_i | W_i).  Small cases are cross-checked by brute force on
the truth table (adversarial_check.analyse).  Usage: python witness_tribes.py OUTJSON
"""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np


def phi(x, y):
    if x <= 0 or y <= 0:
        return 0.0
    return (x * math.log1p(y / x) + y * math.log1p(x / y)) / math.log(2)


def closed(w, s):
    alpha, beta, q0 = (1 - 2.0 ** -w) ** 2, 4.0 ** -w, 1 - 2.0 ** -w
    p0 = (2 * q0 ** s - 1) ** 2
    eps = 2.0 ** (1 - w) * q0 ** (s - 1)
    y = 4 * beta * q0 ** (s - 1)
    Z = p0 + 4 * alpha * (q0 ** (s - 1) - alpha ** (s - 1))
    HW = (2 ** (w - 1) - 1) * 2 * y + phi(Z, y)
    Bi = (2 ** (w - 1) - 1) * 2 * y + 4 * phi(alpha, beta) * (q0 ** (s - 1) - alpha ** (s - 1)) + phi(p0, 4 * beta * alpha ** (s - 1))
    h2 = -(eps * math.log2(eps) + (1 - eps) * math.log2(1 - eps))
    return dict(w=w, s=s, n=w * s, eps=eps, B_over_I=Bi / eps, HW_over_I=HW / eps, h2_over_I=h2 / eps,
                log2_inv_eps=math.log2(1 / eps))


def brute(w, s):
    import adversarial_check as A
    R = A.analyse(A.tribes(w, s))
    p, n = R["p"], R["n"]
    idx = np.arange(p.size)
    HW = 0.0
    for i in range(n):
        blk = [(i // w) * w + u for u in range(w) if (i // w) * w + u != i]
        mask = sum(1 << b for b in blk)
        Si = (idx >> i) & 1
        Wv = idx & mask
        for wv in np.unique(Wv):
            m = Wv == wv
            HW += phi(float(p[m & (Si == 0)].sum()), float(p[m & (Si == 1)].sum()))
    return dict(B_over_I=float(R["B"].sum() / R["I"]), HW_over_I=HW / R["I"])


def main():
    out = dict(check=[], balanced=[])
    for (w, s) in ((2, 3), (3, 3), (2, 5), (3, 4), (4, 3), (2, 6)):
        c, b = closed(w, s), brute(w, s)
        out["check"].append(dict(w=w, s=s, closed_B=c["B_over_I"], brute_B=b["B_over_I"], closed_HW=c["HW_over_I"], brute_HW=b["HW_over_I"]))
        print(f"tribes({w},{s}) B/I closed {c['B_over_I']:.10f} brute {b['B_over_I']:.10f} | H(S_i|W_i)/eps closed {c['HW_over_I']:.10f} brute {b['HW_over_I']:.10f}")
    lvl = {}
    try:
        for r in json.load(open(os.path.join(os.path.dirname(__file__), "..", "data", "obstruction_tables2.json")))["O5b"]:
            lvl[(r["w"], r["s"])] = r.get("Hcond_level_sum_over_I")
    except Exception:
        pass
    for w in range(2, 21):
        s = round(2 ** w * math.log(2))
        c = closed(w, s)
        c["Hcond_level_over_I"] = lvl.get((w, s))
        out["balanced"].append(c)
        hl = c["Hcond_level_over_I"]
        print(f"w={w:2d} s={s:7d} log2(1/eps)={c['log2_inv_eps']:.3f}  B/I={c['B_over_I']:.4f}  H(S_i|W_i)/I={c['HW_over_I']:.4f}  "
              f"H(S_i||S-i|)/I={'%.4f' % hl if hl else '   -  '}  h2/I={c['h2_over_I']:.4f}")
    json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
