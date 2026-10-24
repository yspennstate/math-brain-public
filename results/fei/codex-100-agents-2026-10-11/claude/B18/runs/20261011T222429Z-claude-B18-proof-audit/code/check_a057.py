"""B18 lead check of A057-COHERENT-ERASURE-SPLIT (nats):
 B_i(F) = q B_i(h_j) + L_j(x),  L_j(x) = sum_T (a_T^2 + x b_T^2) h_nat(x b_T^2/(a_T^2 + x b_T^2)),
 0 <= L_j <= x B_j(g) + q x ln(1/x),  where g = a + y_j b, q = Inf_j(g) = sum_T b_T^2, x = hhat_j({i})^2.
Domain (frozen): outer g = every Boolean function on 2 or 3 inputs (16 + 256 tables; constants skipped);
inner balanced h in {dictator(1 bit), Maj3, Mux3, parity2 (two bits), x1 XOR Maj... }; block j=0 carries h, other
blocks carry dictators (fresh single bits). Total bits <= 3 + 2 = 5. Float64 evidence, exact Walsh sums.
Also checks the summed form B(F) <= sum_j q_j B(h_j) + sum_j W1(h_j) B_j(g) + (2/e) I(F).
"""
import numpy as np, math, json, sys, itertools
def walsh(vals, nb):
    N = 1 << nb; h = np.array(vals, dtype=float)
    step = 1
    while step < N:
        for s in range(0, N, 2 * step):
            a = h[s:s + step].copy(); b = h[s + step:s + 2 * step].copy()
            h[s:s + step] = a + b; h[s + step:s + 2 * step] = a - b
        step *= 2
    return h / N
def hnat(x):
    return 0.0 if x <= 0 or x >= 1 else -(x * math.log(x) + (1 - x) * math.log(1 - x))
def Bi(coef, nb, i):
    bit = 1 << i; s = 0.0
    for T in range(1 << nb):
        if T & bit: continue
        pa, pb = coef[T] ** 2, coef[T | bit] ** 2
        m = pa + pb
        if m > 0: s += m * hnat(pb / m)
    return s
def Inf(coef, nb, i):
    return sum(coef[T] ** 2 for T in range(1 << nb) if T >> i & 1)
inner = {
    'dict': (1, lambda x: 1 - 2 * (x & 1)),
    'maj3': (3, lambda x: 1 if bin(x & 7).count('1') <= 1 else -1),
    'mux3': (3, lambda x: (1 - 2 * ((x >> 1) & 1)) if (x & 1) else (1 - 2 * ((x >> 2) & 1))),
    'par2': (2, lambda x: 1 - 2 * (bin(x & 3).count('1') & 1)),
    'and_or_bal': (3, lambda x: 1 - 2 * (((x & 1) and ((x >> 1) & 1)) or (((x >> 2) & 1) and not (x & 1)))),
}
worst_id = 0.0; worst_ub = -1e9; worst_lb = 1e9; worst_sum = -1e9; ncase = 0; bad = []
for k in (2, 3):
    for gt in range(1 << (1 << k)):
        gv = [1 - 2 * ((gt >> y) & 1) for y in range(1 << k)]
        if len(set(gv)) == 1: continue
        gc = walsh(gv, k)
        for hname, (mh, hf) in inner.items():
            hv = [hf(x) for x in range(1 << mh)]
            hc = walsh(hv, mh)
            if abs(hc[0]) > 1e-12: continue  # must be balanced
            nb = mh + (k - 1)
            # block 0: bits 0..mh-1 -> h ; gate input j>=1 is bit mh + j - 1
            def F(x):
                ys = [hf(x & ((1 << mh) - 1))] + [1 - 2 * ((x >> (mh + j - 1)) & 1) for j in range(1, k)]
                yi = sum(((1 - ys[j]) // 2) << j for j in range(k))
                return gv[yi]
            Fc = walsh([F(x) for x in range(1 << nb)], nb)
            # decompose g in its input 0: a_T = gc[T], b_T = gc[T|1] for T not containing input 0
            Ts = [T for T in range(1 << k) if not T & 1]
            q = sum(gc[T | 1] ** 2 for T in Ts)
            Bjg = Bi(gc, k, 0)
            Ftot = 0.0; rhs_sum_terms = 0.0
            for i in range(mh):
                x = hc[1 << i] ** 2
                L = 0.0
                for T in Ts:
                    aa, bb = gc[T] ** 2, x * gc[T | 1] ** 2
                    m = aa + bb
                    if m > 0: L += m * hnat(bb / m)
                lhs = Bi(Fc, nb, i)
                pred = q * Bi(hc, mh, i) + L
                worst_id = max(worst_id, abs(lhs - pred))
                ub = (x * Bjg + (q * x * math.log(1 / x) if x > 0 else 0.0))
                worst_ub = max(worst_ub, L - ub); worst_lb = min(worst_lb, L)
                if abs(lhs - pred) > 1e-9: bad.append([k, gt, hname, i, lhs, pred])
                ncase += 1
            # summed form over all blocks: B(F) <= sum_j q_j B(h_j) + sum_j W1(h_j) B_j(g) + (2/e) I(F)
            BF = sum(Bi(Fc, nb, i) for i in range(nb))
            IF = sum(Inf(Fc, nb, i) for i in range(nb))
            rhs = 0.0
            for j in range(k):
                qj = sum(gc[T | (1 << j)] ** 2 for T in range(1 << k) if not T >> j & 1)
                Bjgj = Bi(gc, k, j)
                if j == 0:
                    Bh = sum(Bi(hc, mh, i) for i in range(mh)); W1 = sum(hc[1 << i] ** 2 for i in range(mh))
                else:
                    Bh = 0.0; W1 = 1.0
                rhs += qj * Bh + W1 * Bjgj
            rhs += (2 / math.e) * IF
            worst_sum = max(worst_sum, BF - rhs)
res = {'cases': ncase, 'max_abs_identity_dev': worst_id, 'max_L_minus_upper': worst_ub, 'min_L': worst_lb,
       'max_BF_minus_summed_rhs': worst_sum, 'identity_failures': bad[:10], 'n_identity_failures': len(bad)}
json.dump(res, open(sys.argv[1], 'w'), indent=1)
print(json.dumps(res, indent=0)[:3000])
