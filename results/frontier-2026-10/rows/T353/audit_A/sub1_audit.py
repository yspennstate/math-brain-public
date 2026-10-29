# Independent audit of agent B's sub-1 Renyi certificates (T353, T = 2). agent A, 20 Oct 2026.
# Written from the stated p, q only (no import of the peer's code). Lane 1: mpmath quad at 30 digits.
# Lane 2: Arb exact-cover recertification with my own tail bound (pairwise subadditivity, Mills).
import sys, mpmath as mp
from flint import arb, acb, ctx
ctx.prec = 128; mp.mp.dps = 30
def comps(g, s, same, qp, Nf):
    wa, w0, wc = Nf(g, -1, s) / 2, Nf(g, 0, s) / 2, Nf(g, 1, s) / 2
    if same: P, Q = [(wa + wc, 1)], [(w0, 1), (wc, 0)]
    else:    P, Q = [(wa, -1), (wc, 1)], [(w0, -1), (wc, 0)]
    return (Q, P) if qp else (P, Q)
def Nm(x, mu, s): return mp.exp(-(x - mu) ** 2 / (2 * s * s)) / (mp.sqrt(2 * mp.pi) * s)
def Jmp(g, s, a, same, qp):
    P, Q = comps(mp.mpf(g), mp.mpf(s), same, qp, Nm)
    f = lambda z: sum(w * Nm(z, m, s) for w, m in P) ** a * sum(w * Nm(z, m, s) for w, m in Q) ** (1 - a)
    L = 40 * s + 2
    return mp.quad(f, mp.linspace(-L, L, 41))
def Na(x, mu, s): return (-(x - mu) ** 2 / (2 * s * s)).exp() / ((2 * arb.pi()).sqrt() * s)
def Jarb(g, s, a, same, qp):
    P, Q = comps(g, s, same, qp, Na)
    L = 32 * s + 3
    def f(z, an):
        p = sum((w * Na(z, m, s) for w, m in P), acb(0)); q = sum((w * Na(z, m, s) for w, m in Q), acb(0))
        return p.pow(acb(a), analytic=an) * q.pow(acb(1 - a), analytic=an)
    v = acb.integral(f, -L, L).real
    t = arb(0)
    for w, m in P:
        for u, n in Q:
            c = abs(a * m + (1 - a) * n).upper(); d = L - c
            t += w ** a * u ** (1 - a) * (-a * (1 - a) * (m - n) ** 2 / (2 * s * s)).exp() * 2 * s * s * Na(d, 0, s) / d
    return v + arb(0, t.upper())
if __name__ == "__main__":
    mode = sys.argv[1]; s = float(sys.argv[2]); A = sys.argv[3]; qp = sys.argv[4] == "QP"
    num, den = map(int, A.split("/"))
    if mode == "mp":
        a = mp.mpf(num) / den
        for x in sys.argv[5].split(","):
            S_, T_ = Jmp(x, s, a, True, qp), Jmp(x, s, a, False, qp)
            print("mp sigma %g order %s %s g1 %s SAME %s ANTI %s ANTI-SAME %s" % (s, A, sys.argv[4], x, mp.nstr(S_, 11), mp.nstr(T_, 11), mp.nstr(T_ - S_, 8)), flush=True)
    else:
        a = arb(num) / den; S = arb(s); lo, hi, n = sys.argv[5], sys.argv[6], int(sys.argv[7])
        LO, HI = arb(lo), arb(hi); gain = arb(0); mn = None
        for i in range(n):
            l, h = LO + (HI - LO) * i / n, LO + (HI - LO) * (i + 1) / n
            g = arb(l.lower()).union(arb(h.upper()))
            d = Jarb(g, S, a, False, qp) - Jarb(g, S, a, True, qp)
            if not d > 0: print("ball %d NOT certified %s" % (i, d.str(5)), flush=True); sys.exit(1)
            gain += (h - l) * arb(d.lower()); mn = d.lower() if mn is None else min(mn, d.lower())
        print("RECERT sigma %g order %s %s [%s, %s] n %d: CERTIFIED, min lower %s, gain >= %s" % (s, A, sys.argv[4], lo, hi, n, arb(mn).str(5), gain.lower().str(6)), flush=True)
