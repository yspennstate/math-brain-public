#!/usr/bin/env python
"""B12 lead replay + lemma validation (run 20261011T225832Z-claude-B12-erasure-ledger-depth).
Identities: exact, as rational combinations of logs of primes (a zero vector is an exact proof of the finite identity).
Inequalities on exact cases: the prime-log vector is evaluated at 40 digits; a check passes only with margin
larger than tol = 1e-30 * (1 + sum |c_p ln p|), far above the rounding of 40-digit logs. Float sweeps: EVIDENCE.
Usage: python -X utf8 b12_verify.py OUTDIR"""
import itertools, math, json, sys, time, random
from fractions import Fraction as Fr
import numpy as np
from mpmath import mp
mp.dps = 40
OUT = sys.argv[1]; T0 = time.time(); RES = {}
def log(*a):
    print(' '.join(str(x) for x in a), flush=True)

_fc = {}
def factor(n):
    r = _fc.get(n)
    if r is not None: return r
    res = {}; m = n; p = 2
    while p * p <= m:
        while m % p == 0:
            res[p] = res.get(p, 0) + 1; m //= p
        p = 3 if p == 2 else p + 2
    if m > 1: res[m] = res.get(m, 0) + 1
    _fc[n] = res; return res
_lg = {}
def lnp(p):
    v = _lg.get(p)
    if v is None: v = mp.log(p); _lg[p] = v
    return v
class LL:
    __slots__ = ('d',)
    def __init__(self): self.d = {}
    def addlog(self, r, c):
        if c == 0: return self
        r = Fr(r)
        for p, e in factor(r.numerator).items(): self.d[p] = self.d.get(p, 0) + c * e
        for p, e in factor(r.denominator).items(): self.d[p] = self.d.get(p, 0) - c * e
        return self
    def addll(self, o, c=1):
        for p, v in o.d.items(): self.d[p] = self.d.get(p, 0) + c * v
        return self
    def iszero(self): return all(v == 0 for v in self.d.values())
    def ev(self):
        s = mp.mpf(0); a = mp.mpf(0)
        for p, v in self.d.items():
            v = Fr(v)
            if v != 0:
                t = mp.mpf(v.numerator) / v.denominator * lnp(p); s += t; a += abs(t)
        return s, mp.mpf('1e-30') * (1 + a)
def xlnx_into(acc, r, c=1):
    if r != 0: acc.addlog(r, c * r)
def phi_into(acc, p, q, c=1):
    xlnx_into(acc, p + q, c); xlnx_into(acc, p, -c); xlnx_into(acc, q, -c)

def val(x, k): return -1 if (x >> k) & 1 else 1
def wht_int(tt):
    a = list(tt); h = 1; N = len(a)
    while h < N:
        for i in range(0, N, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]; a[j] = x + y; a[j + h] = x - y
        h *= 2
    return a
def coefs(tt):
    n = len(tt).bit_length() - 1; W = wht_int(tt)
    return [Fr(w, 2 ** n) for w in W], n
def sq(C): return [c * c for c in C]
def H_ll(P):
    acc = LL()
    for p in P: xlnx_into(acc, p, -1)
    return acc
def B_i_ll(P, i):
    acc = LL(); bit = 1 << i
    for S in range(len(P)):
        if not S & bit: phi_into(acc, P[S], P[S | bit])
    return acc
def I_fr(P): return sum(bin(S).count('1') * p for S, p in enumerate(P))
def restrict(tt, i, b):
    n = len(tt).bit_length() - 1; out = []; bb = 0 if b == 1 else 1
    for y in range(2 ** (n - 1)):
        lo = y & ((1 << i) - 1); hi = y >> i
        out.append(tt[lo | (bb << i) | (hi << (i + 1))])
    return out
def balanced(n):
    N = 2 ** n
    for neg in itertools.combinations(range(N), N // 2):
        tt = [1] * N
        for x in neg: tt[x] = -1
        yield tt
def D_ll(tt, i):
    acc = LL().addll(H_ll(sq(coefs(tt)[0])))
    for b in (1, -1): acc.addll(H_ll(sq(coefs(restrict(tt, i, b))[0])), Fr(-1, 2))
    return acc

# ---------------- V1: A056 witness ----------------
def AND(u, v): return 1 if (u == 1 and v == 1) else -1
def maj(a, b, c): return 1 if a + b + c > 0 else -1
tt = [AND(maj(1, val(x, 0), val(x, 1)), val(x, 2)) for x in range(8)]
C, n = coefs(tt); P = sq(C); Hw = H_ll(P)
target = LL().addlog(2, 4).addlog(3, Fr(-9, 8))
RES['V1_A056_witness'] = dict(mean=str(C[0]), I=str(I_fr(P)), H_nats_equals_4ln2_minus_9_8_ln3=Hw.addll(target, -1).iszero())
log('V1', RES['V1_A056_witness'])

# ---------------- V2: A057 erasure split + J bounds + L1 on exact cases ----------------
def compose(g, m, h, nh):
    n = nh + m - 1; out = []
    for x in range(2 ** n):
        hv = h[x & ((1 << nh) - 1)]
        out.append(g[(1 if hv == -1 else 0) | ((x >> nh) << 1)])
    return out
gates = {m: list(balanced(m)) for m in (2, 3)}
inner = {nh: list(balanced(nh)) for nh in (2, 3)}
pairs = []
for m in (2, 3):
    for nh in (2, 3):
        ps = [(m, gi, nh, hi) for gi in range(len(gates[m])) for hi in range(len(inner[nh]))]
        if m == 3 and nh == 3: ps = random.Random(12).sample(ps, 600)
        pairs += ps
nid = nzc = 0; jmin = None; jmax = None; jviol = 0; L1viol = 0; nineq = 0
for (m, gi, nh, hi) in pairs:
    g = gates[m][gi]; h = inner[nh][hi]
    F = compose(g, m, h, nh); CF, nF = coefs(F); PF = sq(CF)
    Cg, _ = coefs(g); Ch, _ = coefs(h); Ph = sq(Ch)
    q = sum(Cg[T | 1] ** 2 for T in range(0, 2 ** m, 2))
    Bg0 = LL()
    for T in range(0, 2 ** m, 2): phi_into(Bg0, Cg[T] ** 2, Cg[T | 1] ** 2)
    for i in range(nh):
        x = Ch[1 << i] ** 2
        L = LL()
        for T in range(0, 2 ** m, 2): phi_into(L, Cg[T] ** 2, x * Cg[T | 1] ** 2)
        diff = LL().addll(B_i_ll(PF, i)).addll(B_i_ll(Ph, i), -q).addll(L, -1)
        nid += 1; nzc += (not diff.iszero())
        v, tol = LL().addll(Bg0).addll(L, -1).ev(); nineq += 1
        if v < -tol: L1viol += 1
        J = LL().addll(D_ll(F, i)).addll(D_ll(h, i), -q).addll(L, -1)
        v, tol = J.ev(); ub = mp.mpf((2 * q * x).numerator) / (2 * q * x).denominator
        if v < -tol or v > ub + tol: jviol += 1
        if q * x > 0:
            r = float(v / (q * x)); jmin = r if jmin is None else min(jmin, r); jmax = r if jmax is None else max(jmax, r)
    for t in range(1, m):
        Bgt = LL()
        for T in range(2 ** m):
            if not T & (1 << t): phi_into(Bgt, Cg[T] ** 2, Cg[T | (1 << t)] ** 2)
        diff = LL().addll(B_i_ll(PF, nh + t - 1)).addll(Bgt, -1)
        nid += 1; nzc += (not diff.iszero())
RES['V2_A057_split'] = dict(pairs=len(pairs), identity_checks=nid, identity_failures=nzc, L1_checks=nineq, L1_violations=L1viol,
                            J_violations_of_0_le_J_le_2qx=jviol, J_over_qx_min=jmin, J_over_qx_max=jmax)
log('V2', RES['V2_A057_split'], round(time.time() - T0, 1), 's')

# ---------------- float helpers ----------------
def hadamard(n):
    N = 2 ** n; Hm = np.empty((N, N))
    for S in range(N):
        for x in range(N): Hm[S, x] = -1.0 if bin(S & x).count('1') % 2 else 1.0
    return Hm
def xlogx(a):
    out = np.zeros_like(a); m = a > 0; out[m] = a[m] * np.log(a[m]); return out
def phi_np(u, v): return xlogx(u + v) - xlogx(u) - xlogx(v)
def all_bal_np(n):
    N = 2 ** n; rows = []
    for neg in itertools.combinations(range(N), N // 2):
        r = np.ones(N); r[list(neg)] = -1; rows.append(r)
    return np.array(rows)

# ---------------- V3: L1 sweep (evidence) ----------------
xs = np.linspace(0, 1, 65); v3 = {}
xl = np.zeros_like(xs); xl[1:] = xs[1:] * np.log(1 / xs[1:])
for n in (3, 4):
    TT = all_bal_np(n); N = 2 ** n; C = TT @ hadamard(n).T / N
    mono = cap = conc = 0; worst_cap = -1.0
    for j in range(n):
        Ts = [T for T in range(N) if not T & (1 << j)]
        A2 = C[:, Ts] ** 2; B2 = C[:, [T | (1 << j) for T in Ts]] ** 2; q = B2.sum(1)
        Lx = np.stack([phi_np(A2, x * B2).sum(1) for x in xs], 1)
        L1v = Lx[:, -1:]
        mono += int((np.diff(Lx, axis=1) < -1e-12).any(1).sum())
        cap += int((Lx > L1v + 1e-12).any(1).sum()); worst_cap = max(worst_cap, float((Lx - L1v).max()))
        conc += int((Lx > xs[None, :] * L1v + q[:, None] * xl[None, :] + 1e-12).any(1).sum())
    v3[n] = dict(functions=len(TT), monotone_failures=mono, cap_failures=cap, concavity_bound_failures=conc, max_L_minus_Bj=worst_cap)
RES['V3_L1_sweep'] = v3; log('V3', v3)

# ---------------- V4: L2 deficit bank ----------------
K2 = 4 + 6 / math.e
def lam_I(C, n):
    lv = C[:, [1 << i for i in range(n)]] ** 2
    Lam = -xlogx(lv).sum(1)
    sizes = np.array([bin(S).count('1') for S in range(2 ** n)])
    I = (C ** 2 * sizes[None, :]).sum(1)
    return Lam, I
v4 = {}; best = None
for n in (2, 3, 4):
    TT = all_bal_np(n); C = TT @ hadamard(n).T / 2 ** n; Lam, I = lam_I(C, n)
    d = I - 1; ok = d > 1e-12; ratio = np.zeros_like(d); ratio[ok] = Lam[ok] / d[ok]
    k = int(np.argmax(ratio))
    v4[n] = dict(functions=len(TT), violations=int((Lam > K2 * d + 1e-12).sum()), max_ratio=float(ratio.max()),
                 zero_deficit_with_positive_Lambda=int(((~ok) & (Lam > 1e-12)).sum()))
    if best is None or ratio[k] > best[0]: best = (float(ratio[k]), n, [int(v) for v in TT[k]])
rng = np.random.default_rng(7); n = 5; N = 32; NR = 30000
TT = np.ones((NR, N))
for r in range(NR): TT[r, rng.permutation(N)[:16]] = -1
C = TT @ hadamard(5).T / N; Lam, I = lam_I(C, 5); d = I - 1; ok = d > 1e-12
v4['5_random'] = dict(functions=NR, violations=int((Lam > K2 * d + 1e-12).sum()), max_ratio=float((Lam[ok] / d[ok]).max()))
rng = np.random.default_rng(8)
for n in (5, 6, 7):
    N = 2 ** n; X = np.array([[val(x, k) for k in range(n)] for x in range(N)], float)
    W = rng.standard_normal((6667, n)) * rng.choice([1.0, 0.2], size=(6667, n))
    TT = np.sign(W @ X.T); TT[TT == 0] = 1
    C = TT @ hadamard(n).T / N; Lam, I = lam_I(C, n); d = I - 1; ok = d > 1e-9
    v4[f'{n}_odd_LTF'] = dict(functions=len(TT), violations=int((Lam > K2 * d + 1e-9).sum()), max_ratio=float((Lam[ok] / d[ok]).max()) if ok.any() else None)
tt = best[2]; Cb, nb = coefs(tt); Pb = sq(Cb)
Lam_ll = LL()
for i in range(nb): xlnx_into(Lam_ll, Cb[1 << i] ** 2, -1)
Ib = I_fr(Pb); lamv, tol = Lam_ll.ev()
v4['best_small'] = dict(n=nb, truth_table=tt, ratio=float(lamv / (mp.mpf(Ib.numerator) / Ib.denominator - 1)), I=str(Ib),
                        Lambda=str(mp.nstr(lamv, 20)), certified_below_bound=bool(lamv + tol < (4 + 6 / mp.e) * (mp.mpf(Ib.numerator) / Ib.denominator - 1)))
RES['V4_L2'] = v4; log('V4', v4)

# ---------------- V5: chain family (R1) ----------------
def thr_gate(k):
    return [1 if ((k - 1) * val(x, 0) + sum(val(x, t) for t in range(1, k + 1))) > 0 else -1 for x in range(2 ** (k + 1))]
def chain_tt(k, d):
    g = thr_gate(k); n = 1 + d * k; out = []
    for x in range(2 ** n):
        v = val(x, 0)
        for t in range(d):
            v = g[(1 if v == -1 else 0) | (((x >> (1 + t * k)) & ((1 << k) - 1)) << 1)]
        out.append(v)
    return out
def lam_chain_ll(k, r):
    u = Fr(1, 2 ** (k - 1)); acc = LL(); xlnx_into(acc, (1 - u) ** (2 * r), -1)
    for l in range(r): xlnx_into(acc, ((1 - u) ** (r - 1 - l) * u) ** 2, -k)
    return acc
bf = []
for (k, d) in [(2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3)]:
    F = chain_tt(k, d); CF, nF = coefs(F); PF = sq(CF); u = Fr(1, 2 ** (k - 1))
    g = thr_gate(k); Cg, _ = coefs(g); Pg = sq(Cg)
    geo = sum((1 - u) ** s for s in range(d))
    Hpred = LL().addll(H_ll(Pg), geo)
    lev1_ok = CF[1] == (1 - u) ** d and all(CF[1 << (1 + t * k + i)] == (1 - u) ** (d - 1 - t) * u for t in range(d) for i in range(k))
    Bsum = LL()
    for i in range(nF): Bsum.addll(B_i_ll(PF, i))
    lamF = LL()
    for i in range(nF): xlnx_into(lamF, CF[1 << i] ** 2, -1)
    infy = sum(Cg[T | 1] ** 2 for T in range(0, 2 ** (k + 1), 2))
    bf.append(dict(k=k, d=d, n=nF, Inf_y_g_is_1_minus_u=(infy == 1 - u), H_matches_chain_rule=LL().addll(H_ll(PF)).addll(Hpred, -1).iszero(),
                   I_matches=(I_fr(PF) == 1 + (k - 1) * (1 - (1 - u) ** d)), level1_matches=lev1_ok,
                   B_total_zero=Bsum.iszero(), Lambda_matches_closed_sum=LL().addll(lamF).addll(lam_chain_ll(k, d), -1).iszero()))
log('V5 brute', bf)
def lam_closed(k, r):
    u = mp.mpf(1) / 2 ** (k - 1); a = (1 - u) ** 2
    t0 = -(a ** r) * mp.log(a ** r) if r > 0 else mp.mpf(0)
    S0 = (1 - a ** r) / (1 - a); S1 = a * (1 - r * a ** (r - 1) + (r - 1) * a ** r) / (1 - a) ** 2
    return t0 + k * u * u * (-2 * mp.log(u) * S0 - mp.log(a) * S1)
cf_err = max(abs(lam_closed(k, r) - lam_chain_ll(k, r).ev()[0]) for k in (2, 3, 4) for r in range(0, 7))
table = []
for k in range(2, 15):
    u = mp.mpf(1) / 2 ** (k - 1); d = 2 ** (k - 1)
    bank = mp.fsum((1 - u) ** s * (1 - u) * lam_closed(k, d - 1 - s) for s in range(d))
    I = 1 + (k - 1) * (1 - (1 - u) ** d)
    if k <= 12:
        Hg = float(H_ll(sq(coefs(thr_gate(k))[0])).ev()[0]) / math.log(2); HF = Hg * float((1 - (1 - u) ** d) / u)
    else:
        HF = None
    lb = mp.e ** (-2 - 2 * u) * (d - 1)
    table.append(dict(k=k, d=d, bank_nats=float(bank), I=float(I), H_bits=HF, B=0.0, bank_over_I=float(bank / I),
                      analytic_lower_bound=float(lb), lower_bound_holds=bool(bank >= lb)))
RES['V5_chain'] = dict(bruteforce=bf, closed_form_max_abs_err=float(cf_err), table=table)
log('V5 table', [(t['k'], round(t['bank_over_I'], 3), round(t['I'], 3), t['H_bits'] and round(t['H_bits'], 3), t['lower_bound_holds']) for t in table])

# ---------------- V6: A058 anchored overlap theorem ----------------
def P2(a, b): return -1 if (a == -1 and b == -1) else 1
v6 = {'example': []}
for kk in (1, 2, 3):
    n = 2 * kk + 2; tt = []
    for x in range(2 ** n):
        pz = P2(val(x, 2 * kk), val(x, 2 * kk + 1)); v = 1
        for l in range(kk): v *= P2(val(x, 2 * l) * pz, val(x, 2 * l + 1) * pz)
        tt.append(v)
    Pf = sq(coefs(tt)[0])
    v6['example'].append(dict(k=kk, H_is_2k_plus_1_bits=LL().addll(H_ll(Pf)).addlog(2, -(2 * kk + 1)).iszero(), I=str(I_fr(Pf))))
rr = random.Random(5); okH = okI = 0; NI = 200
for _ in range(NI):
    Ft = [rr.choice([1, -1]) for _ in range(8)]; A = [[rr.randint(0, 1) for _ in range(3)] for _ in range(2)]
    bs = [[rr.choice([1, -1]) for _ in range(4)] for _ in range(2)]
    tt = []
    for x in range(2 ** 7):
        bv = [bs[j][(x >> (3 + 2 * j)) & 3] for j in range(2)]
        ys = []
        for i in range(3):
            y = val(x, i)
            for j in range(2):
                if A[j][i]: y *= bv[j]
            ys.append(y)
        tt.append(Ft[sum((1 << i) for i in range(3) if ys[i] == -1)])
    Pf = sq(coefs(tt)[0]); PF = sq(coefs(Ft)[0])
    dj = [sum(PF[T] for T in range(8) if sum(A[j][i] for i in range(3) if T >> i & 1) % 2) for j in range(2)]
    Pb = [sq(coefs(b)[0]) for b in bs]
    Hp = LL().addll(H_ll(PF))
    for j in range(2): Hp.addll(H_ll(Pb[j]), dj[j])
    okH += LL().addll(H_ll(Pf)).addll(Hp, -1).iszero()
    okI += (I_fr(Pf) == I_fr(PF) + sum(dj[j] * I_fr(Pb[j]) for j in range(2)))
v6['random'] = dict(instances=NI, H_identity_exact=okH, I_identity_exact=okI)
RES['V6_A058'] = v6; log('V6', v6)
RES['runtime_s'] = round(time.time() - T0, 1)
json.dump(RES, open(OUT + '/results.json', 'w'), indent=1, default=str)
log('done', RES['runtime_s'])
