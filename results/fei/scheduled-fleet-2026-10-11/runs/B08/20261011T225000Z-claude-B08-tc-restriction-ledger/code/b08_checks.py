# B08 lead run, exact checks.  Usage: python -X utf8 b08_checks.py <outdir>
# Part A  TC restriction ledger  TC(f) = I(S_i;S_-i) - JS_i + Gamma_i + avg_s TC(f|x_i=s),
#         plus C005 H(f) = B_i + JS_i + avg_s H(f|x_i=s); exact on all 65,536 Boolean f on 4 bits, every i.
#         Exactness: every log is an integer vector over log2(p), p prime <= 61 (all values are k/64, k<=64);
#         logs of distinct primes are linearly independent over Q, so vector equality is equality of reals.
# Part B  exhaustive n=4 calibration of H/I, B/I, M_edge/I, TC/I, M/I and max_f min_i B_i/Inf_i.
#         Max values evaluated at 60 digits from the exact vectors; floating bound with error margin for all f.
# Part C  independent re-check of A036's point-defect collision profile (exact Fractions, m=2..7),
#         Z(3)=319/256, and A036's linear inequalities per factor (mpmath 80 digits, m=2..40: evidence).
# Part D  independent re-check of A037's physical common lift on all 256 3-bit functions and all 12
#         depth-2 coordinate trees: fair branches and H(S_0|L) = sum_h p_h B_h + sum_l p_l H(f_l), exact.
# Part E  AND_n (point defect) values of Gamma_1, JS_1, Inf_1 (mpmath 50 digits): evidence for the
#         analytic bound Gamma_1 >= (n-1) Inf_1, which refutes Gamma_i <= c (Inf_i + JS_i).
import sys, json, math, time, itertools
from fractions import Fraction
import numpy as np
import mpmath as mp

t0 = time.time()
OUT = sys.argv[1]
res = {}
PR = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
NP = len(PR)


def ivec(m):
    v = np.zeros(NP, dtype=np.int64)
    for k, p in enumerate(PR):
        while m % p == 0:
            v[k] += 1
            m //= p
    assert m == 1
    return v


LOG = np.zeros((65, NP), dtype=np.int32)
XLX = np.zeros((65, NP), dtype=np.int32)
for x in range(1, 65):
    LOG[x] = ivec(x)
    XLX[x] = x * LOG[x]
E2 = np.zeros(NP, dtype=np.int32)
E2[0] = 1
mp.mp.dps = 60
LOG2P_MP = [mp.log(p, 2) for p in PR]
LOG2P = np.array([float(x) for x in LOG2P_MP])
EPS = 2.0 ** -52


def popc(x):
    return bin(x).count('1')


def sum_xlx(arr):
    acc = np.zeros((arr.shape[0], NP), dtype=np.int32)
    for c in range(arr.shape[1]):
        acc += XLX[arr[:, c]]
    return acc


def h64(Aj):        # 64*h2(Aj/64)
    return 384 * E2[None, :] - XLX[Aj] - XLX[64 - Aj]


def h16_64(B):      # 64*h2(B/16)
    return 4 * (64 * E2[None, :] - XLX[B] - XLX[16 - B])


def h32_64(C):      # 64*h2(C/32)
    return 2 * (160 * E2[None, :] - XLX[C] - XLX[32 - C])


n = 4
N = 16
HAD = np.array([[(-1) ** popc(S & x) for x in range(N)] for S in range(N)], dtype=np.int64)
H8 = np.array([[(-1) ** popc(T & y) for y in range(8)] for T in range(8)], dtype=np.int64)
allF = np.arange(1 << N, dtype=np.int64)
TT = 1 - 2 * ((allF[:, None] >> np.arange(N)[None, :]) & 1)    # f(x) = +-1, x = bit index
W = TT @ HAD.T                                                   # 16 * fhat
assert np.all(W % 2 == 0)
a = (W // 2) ** 2                                                # P(S) = a/64
assert np.all(a.sum(1) == 64)
Sbits = np.array([[(S >> j) & 1 for j in range(n)] for S in range(N)], dtype=np.int64)
A = a @ Sbits                                                    # 64 * Inf_j
H64 = 384 * E2[None, :] - sum_xlx(a)                             # 64 * H(P)
M64 = sum(h64(A[:, j]) for j in range(n))                        # 64 * M, M = sum_j h2(Inf_j)
TC64 = M64 - H64                                                 # 64 * TC
Tbits = np.array([[(T >> k) & 1 for k in range(3)] for T in range(8)], dtype=np.int64)
part_a = {}
Bi_list = []
for i in range(n):
    rest = [j for j in range(n) if j != i]
    xs = {}
    for s in (0, 1):
        idx = []
        for y in range(8):
            x = s << i
            for k, j in enumerate(rest):
                x |= ((y >> k) & 1) << j
            idx.append(x)
        xs[s] = idx
    bc, Bc, Hc64, Mc64, TCc64 = {}, {}, {}, {}, {}
    for s in (0, 1):
        Wc = TT[:, xs[s]] @ H8.T                                 # 8 * ghat
        assert np.all(Wc % 2 == 0)
        bc[s] = (Wc // 2) ** 2                                   # P_child = b/16
        assert np.all(bc[s].sum(1) == 16)
        Bc[s] = bc[s] @ Tbits                                    # 16 * Inf_rest[k](child)
        Hc64[s] = 4 * (64 * E2[None, :] - sum_xlx(bc[s]))
        Mc64[s] = sum(h16_64(Bc[s][:, k]) for k in range(3))
        TCc64[s] = Mc64[s] - Hc64[s]
    assert np.all((Hc64[0] + Hc64[1]) % 2 == 0) and np.all((TCc64[0] + TCc64[1]) % 2 == 0)
    G64 = np.zeros_like(H64)
    TVsum = np.zeros(1 << N, dtype=np.int64)
    for k in range(3):
        G64 += h32_64(Bc[0][:, k] + Bc[1][:, k]) - (h16_64(Bc[0][:, k]) + h16_64(Bc[1][:, k])) // 2
        TVsum += np.abs(Bc[0][:, k] - Bc[1][:, k])               # 16 * sum_j |Inf_j(g0)-Inf_j(g1)|
    e = bc[0] + bc[1]                                            # mixture = e/32
    JS64 = 2 * (160 * E2[None, :] - sum_xlx(e)) - (Hc64[0] + Hc64[1]) // 2
    Ti = [S for S in range(N) if not (S >> i) & 1]
    cT = a[:, Ti] + a[:, [S | (1 << i) for S in Ti]]             # law of S \ {i}, scaled 64
    HSmi64 = 384 * E2[None, :] - sum_xlx(cT)
    MI64 = h64(A[:, i]) + HSmi64 - H64                           # I(S_i ; S_-i)
    rhs = MI64 - JS64 + G64 + (TCc64[0] + TCc64[1]) // 2
    nbad = int(np.count_nonzero(np.any(TC64 - rhs != 0, axis=1)))
    Bi64 = H64 - HSmi64
    Bi_list.append(Bi64)
    d2 = H64 - (Bi64 + JS64 + (Hc64[0] + Hc64[1]) // 2)
    nbad2 = int(np.count_nonzero(np.any(d2 != 0, axis=1)))
    Gf = (G64 @ LOG2P) / 64.0
    Gerr = 30 * EPS * (np.abs(G64) @ LOG2P) / 64.0
    TVf = TVsum / 16.0
    part_a[str(i)] = dict(ledger_identity_failures=nbad, C005_identity_failures=nbad2,
                          gamma_min_float=float(Gf.min()),
                          max_gamma_minus_sum_TV_upper=float((Gf + Gerr - TVf).max()))
res['partA_tc_ledger_all_4bit'] = dict(functions=int(1 << N), coordinates=n, per_coordinate=part_a,
                                       note='exact integer vectors over log2(primes<=61), all quantities scaled by 64')
print('Part A', json.dumps(res['partA_tc_ledger_all_4bit']), flush=True)

# Part B: calibration on all 4-bit functions
Itot = A.sum(1)
nonc = Itot > 0
B64 = sum(Bi_list)
Medge64 = np.zeros((1 << N, NP), dtype=np.int64)
for S in range(N):
    for i in range(n):
        if (S >> i) & 1:
            aS = a[:, S]
            aT = a[:, S ^ (1 << i)]
            pos = aS > 0
            term = aS[:, None] * (LOG[np.where(pos, aS + aT, 1)] - LOG[np.where(pos, aS, 1)])
            Medge64 += np.where(pos[:, None], term, 0)


def fl_and_err(V):
    return V @ LOG2P, 30 * EPS * (np.abs(V) @ LOG2P) + 1e-300


def exact_val(vec):
    return mp.fsum(int(vec[q]) * LOG2P_MP[q] for q in range(NP))


calib = {}
# sanity: M_edge <= B <= M_edge + I log2 e on every f (float with margins)
mv, me = fl_and_err(Medge64)
bv, be = fl_and_err(B64)
calib['check_Medge_le_B_violations'] = int(np.count_nonzero(mv - me > bv + be))
calib['max_B_minus_Medge_over_I'] = float(((bv - mv) / np.maximum(Itot, 1))[nonc].max())
calib['check_B_le_Medge_plus_Ilog2e_violations'] = int(np.count_nonzero(bv - be > mv + me + Itot * math.log2(math.e) * (1 + 1e-12)))
for name, V in [('H', H64), ('B', B64), ('M_edge', Medge64), ('TC', TC64), ('M', M64)]:
    val, err = fl_and_err(V[nonc])
    r = val / Itot[nonc]
    rerr = err / Itot[nonc]
    k = int(np.argmax(r))
    fidx = int(allF[nonc][k])
    exact = exact_val(V[fidx]) / int(Itot[fidx])
    calib[name] = dict(max_ratio_to_I=mp.nstr(exact, 20), argmax_truth_table=format(fidx, '016b'),
                       float_upper_bound_all_f=float((r + rerr).max()),
                       I_at_argmax=str(Fraction(int(Itot[fidx]), 64)))
gcr = np.full(int(nonc.sum()), np.inf)
for i in range(n):
    val, err = fl_and_err(Bi_list[i][nonc])
    Ai = A[nonc, i]
    ri = np.where(Ai > 0, (val + err) / np.maximum(Ai, 1), np.inf)
    gcr = np.minimum(gcr, ri)
k = int(np.argmax(gcr))
fidx = int(allF[nonc][k])
vals = [exact_val(Bi_list[i][fidx]) / int(A[fidx, i]) for i in range(n) if A[fidx, i] > 0]
calib['good_coordinate_K'] = dict(max_f_min_i_Bi_over_Infi=mp.nstr(min(vals), 20),
                                  argmax_truth_table=format(fidx, '016b'),
                                  float_upper_bound=float(gcr.max()),
                                  per_coordinate=[mp.nstr(v, 12) for v in vals])
res['partB_calibration_n4'] = calib
print('Part B', json.dumps(calib), flush=True)

# Part C: A036 point-defect re-check
partC = {}
for m in range(2, 8):
    Nn = 1 << m
    f = [1] * Nn
    f[0] = -1
    fh = [Fraction(sum(f[x] * (-1) ** popc(S & x) for x in range(Nn)), Nn) for S in range(Nn)]
    d = Fraction(2, Nn)
    assert fh[0] == 1 - d and all(fh[S] == -d for S in range(1, Nn))
    aa = 4 * d * (1 - d)
    sg = [1 if x > 0 else -1 for x in fh]
    ok = True
    Z = Fraction(0)
    for U in range(Nn):
        k = popc(U)
        R = sum(sg[S] * sg[S ^ U] * d ** popc(S & ~U & (Nn - 1)) * (1 - d) ** (m - k - popc(S & ~U & (Nn - 1)))
                for S in range(Nn))
        vU = (d * (1 - d)) ** k * R * R
        pred = Fraction(1) if k == 0 else aa ** k * (1 - Fraction(2) ** (2 - k) * (1 - d) ** (m - k)) ** 2
        ok = ok and (vU == pred)
        Z += vU
    partC[str(m)] = dict(profile_formula_exact=ok, Z=str(Z))
assert partC['3']['Z'] == '319/256'
mp.mp.dps = 80
ineq = {}
for m in range(2, 41):
    d = mp.mpf(2) ** (1 - m)
    aa = 4 * d * (1 - d)
    I1 = m * d
    vk = [mp.mpf(1)] + [aa ** k * (1 - mp.mpf(2) ** (2 - k) * (1 - d) ** (m - k)) ** 2 for k in range(1, m + 1)]
    Z = mp.fsum(mp.binomial(m, k) * vk[k] for k in range(m + 1))
    L = mp.fsum(mp.binomial(m, k) * vk[k] * (-mp.log(vk[k], 2)) for k in range(1, m + 1) if vk[k] > 0)
    T = L / Z
    H = -(1 - d) ** 2 * mp.log((1 - d) ** 2, 2) + (2 ** m - 1) * d ** 2 * (-mp.log(d ** 2, 2))
    M = m * (-d * mp.log(d, 2) - (1 - d) * mp.log(1 - d, 2))
    K = M - H
    ineq[str(m)] = dict(H_over_I=float(H / I1),
                        margin_K_ge_T4_minus_8I_over_I=float((K - T / 4 + 8 * I1) / I1),
                        margin_M_le_T4_plus_8I_over_I=float((T / 4 + 8 * I1 - M) / I1),
                        T_over_I=float(T / I1))
partC['inequalities_mpmath80_evidence'] = ineq
partC['min_margin_K_ge_T4_minus_8I'] = min(v['margin_K_ge_T4_minus_8I_over_I'] for v in ineq.values())
partC['min_margin_M_le_T4_plus_8I'] = min(v['margin_M_le_T4_plus_8I_over_I'] for v in ineq.values())
partC['max_H_over_I'] = max(v['H_over_I'] for v in ineq.values())
partC['m7_integer_comparison_2x1087^6<3x1024^6'] = bool(2 * 1087 ** 6 < 3 * 1024 ** 6)
res['partC_A036'] = partC
print('Part C', json.dumps({k: partC[k] for k in partC if k != 'inequalities_mpmath80_evidence'}), flush=True)


# Part D: A037 physical common lift, all 256 3-bit functions, all 12 depth-2 trees, exact
def fvec(r):
    v = {}
    for x, sgn in ((r.numerator, 1), (r.denominator, -1)):
        p = 2
        while x > 1:
            while x % p == 0:
                v[p] = v.get(p, 0) + sgn
                x //= p
            p += 1
    return v


def addv(acc, v, c):
    for p, e_ in v.items():
        acc[p] = acc.get(p, 0) + c * e_


def ent(dist):
    acc = {}
    for r in dist:
        if r > 0:
            addv(acc, fvec(r), -r)
    return acc


def spec(tt, coords):
    out = {}
    pts = list(tt.keys())
    for r in range(len(coords) + 1):
        for S in itertools.combinations(coords, r):
            s = sum(tt[x] * (-1) ** sum(x[coords.index(j)] for j in S) for x in pts)
            out[frozenset(S)] = Fraction(s, len(pts))
    return out


def restrict(tt, coords, i, s):
    k = coords.index(i)
    nc = [c for c in coords if c != i]
    return {tuple(x[q] for q in range(len(coords)) if q != k): v for x, v in tt.items() if x[k] == s}, nc


trees = []
for r0 in range(3):
    rest = [c for c in range(3) if c != r0]
    for c0 in rest:
        for c1 in rest:
            trees.append({(): r0, (0,): c0, (1,): c1})
nfail = nfair = ncases = 0
for code in range(256):
    tt0 = {x: 1 - 2 * ((code >> (x[0] + 2 * x[1] + 4 * x[2])) & 1) for x in itertools.product((0, 1), repeat=3)}
    for rule in trees:
        nodes = {(): (tt0, [0, 1, 2])}
        for path in [(), (0,), (1,)]:
            g, gc = nodes[path]
            for s in (0, 1):
                nodes[path + (s,)] = restrict(g, gc, rule[path], s)
        sp = {p: spec(*nodes[p]) for p in nodes}
        rhs = {}
        for path in [(), (0,), (1,)]:
            gh = sp[path]
            i = rule[path]
            ph = Fraction(1, 2 ** len(path))
            marg = {}
            for S, c in gh.items():
                marg[S - {i}] = marg.get(S - {i}, 0) + c * c
            addv(rhs, ent([c * c for c in gh.values()]), ph)
            addv(rhs, ent(list(marg.values())), -ph)
        for path in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            addv(rhs, ent([c * c for c in sp[path].values()]), Fraction(1, 4))
        joint = {}
        for S0, c0 in sp[()].items():
            if c0 == 0:
                continue
            stack = [((), S0, c0 * c0)]
            while stack:
                path, Sh, pr = stack.pop()
                if len(path) == 2:
                    joint[(S0, path)] = joint.get((S0, path), 0) + pr
                    continue
                i = rule[path]
                gh = sp[path]
                T = Sh - {i}
                q = gh[T] ** 2 + gh[T | {i}] ** 2
                assert q > 0
                for s in (0, 1):
                    kk = Fraction(1, 2) * sp[path + (s,)][T] ** 2 / q
                    if kk > 0:
                        stack.append((path + (s,), T, pr * kk))
        PL = {}
        for (S0, path), pr in joint.items():
            PL[path] = PL.get(path, 0) + pr
        if len(PL) != 4 or any(v != Fraction(1, 4) for v in PL.values()):
            nfair += 1
        lhs = ent(list(joint.values()))
        addv(lhs, ent(list(PL.values())), -1)
        addv(lhs, rhs, -1)
        if any(c != 0 for c in lhs.values()):
            nfail += 1
        ncases += 1
res['partD_A037_lift'] = dict(functions=256, trees_per_function=len(trees), cases=ncases,
                              identity_failures=nfail, fair_branch_failures=nfair)
print('Part D', res['partD_A037_lift'], flush=True)

# Part E: AND_n = point defect on n bits; restrict coordinate 1
mp.mp.dps = 50


def h2m(x):
    x = mp.mpf(x)
    if x <= 0 or x >= 1:
        return mp.mpf(0)
    return -x * mp.log(x, 2) - (1 - x) * mp.log(1 - x, 2)


def Hpd(m):
    d = mp.mpf(2) ** (1 - m)
    p0 = (1 - d) ** 2
    rest = (2 ** m - 1) * d ** 2 * (-mp.log(d ** 2, 2))
    return rest + (-p0 * mp.log(p0, 2) if p0 > 0 else 0)


partE = {}
for nn in range(3, 41):
    d = mp.mpf(2) ** (1 - nn)
    m = nn - 1
    dm = mp.mpf(2) ** (1 - m)
    q0 = (1 - dm) ** 2
    qs = dm ** 2
    mix0 = (1 + q0) / 2
    Hmix = -mix0 * mp.log(mix0, 2) + (2 ** m - 1) * (qs / 2) * (-mp.log(qs / 2, 2))
    JS1 = Hmix - Hpd(m) / 2
    B1 = Hpd(nn) - JS1 - Hpd(m) / 2
    I1 = h2m(d) - B1
    G1 = (nn - 1) * (h2m(d) - h2m(2 * d) / 2)
    TCf = nn * h2m(d) - Hpd(nn)
    TCg = m * h2m(2 * d) - Hpd(m)
    ledger_resid = TCf - (I1 - JS1 + G1 + TCg / 2)
    partE[str(nn)] = dict(Gamma1_over_n1_Inf1=float(G1 / ((nn - 1) * d)),
                          Gamma1_over_Inf1_plus_JS1=float(G1 / (d + JS1)),
                          JS1_over_Inf1=float(JS1 / d), Gamma1_over_h2Inf1=float(G1 / h2m(d)),
                          I1_over_h2Inf1=float(I1 / h2m(d)), ledger_residual=float(ledger_resid))
res['partE_AND_gamma'] = partE
print('Part E (n=3,10,20,40)', {k: partE[k] for k in ('3', '10', '20', '40')}, flush=True)
res['runtime_seconds'] = round(time.time() - t0, 2)
try:
    import psutil
    res['peak_working_set_MB'] = round(psutil.Process().memory_info().peak_wset / 2**20, 1)
except Exception as ex:
    res['peak_working_set_MB'] = 'unavailable: ' + repr(ex)
with open(OUT + '/checks.json', 'w', encoding='utf-8') as fo:
    json.dump(res, fo, indent=1, default=str)
print('done', res['runtime_seconds'], 's; peak MB', res['peak_working_set_MB'], flush=True)
