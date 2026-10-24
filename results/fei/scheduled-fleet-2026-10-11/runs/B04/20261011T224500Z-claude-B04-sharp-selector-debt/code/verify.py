# B04-lead-verify-v1 : checks for the sharp selector-only debt theorem and an independent check of A017.
# Run: python -X utf8 verify.py  (writes ../out/verify_results.json)
import numpy as np, json, math, random, time, os, sys, hashlib
from fractions import Fraction
from collections import Counter
import mpmath
from mpmath import iv

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'out')
LN2 = math.log(2.0)
T0 = time.time()
res = {"helper_version": "B04-lead-verify-v1"}

def fwht(a):
    """Unnormalized Walsh-Hadamard transform along the last axis (int64, exact)."""
    a = np.array(a, dtype=np.int64, copy=True)
    n = a.shape[-1]
    lead = a.shape[:-1]
    h = 1
    while h < n:
        a = a.reshape(lead + (n // (2 * h), 2, h))
        x = a[..., 0, :].copy(); y = a[..., 1, :].copy()
        a[..., 0, :] = x + y; a[..., 1, :] = x - y
        a = a.reshape(lead + (n,))
        h *= 2
    return a

def ent(p, axis=-1):
    with np.errstate(divide='ignore', invalid='ignore'):
        t = np.where(p > 0, -p * np.log2(np.where(p > 0, p, 1.0)), 0.0)
    return t.sum(axis=axis)

def h2(t):
    t = np.clip(t, 0.0, 1.0)
    with np.errstate(divide='ignore', invalid='ignore'):
        a = np.where(t > 0, -t * np.log2(np.where(t > 0, t, 1.0)), 0.0)
        b = np.where(t < 1, -(1 - t) * np.log2(np.where(t < 1, 1 - t, 1.0)), 0.0)
    return a + b

POP = np.array([bin(i).count('1') for i in range(1 << 16)], dtype=np.int64)

def analyse(G, a, m):
    """G: int array shape (P, 2^a, 2^m) of +-1, G[:, b, y] = g_b(y). F(x,y)=g_x(y), index x + (y<<a)."""
    P = G.shape[0]; N = 1 << a; M = 1 << m; n = a + m
    F = np.transpose(G, (0, 2, 1)).reshape(P, N * M)          # index y*N + x
    W = fwht(F)                                               # index T*N + S
    W2 = W * W
    p = W2.astype(np.float64) / float(4 ** n)
    pTS = p.reshape(P, M, N)
    R = pTS.sum(axis=2)
    HF = ent(p); HR = ent(R)
    Gb = fwht(G)                                              # (P, N, M)
    q = (Gb * Gb).astype(np.float64) / float(4 ** m)
    Hb = ent(q, axis=2).mean(axis=1)
    BW = HF - HR; MW = HR - Hb; Delta = HF - Hb
    # identity M_W = a - sum_T R_T H(r_T)
    with np.errstate(divide='ignore', invalid='ignore'):
        r = np.where(R[:, None, :] > 0, q / (N * np.where(R[:, None, :] > 0, R[:, None, :], 1.0)), 0.0)
    HrT = ent(r, axis=1)
    MW2 = a - (R * HrT).sum(axis=1)
    # exact selector influence, spectral and physical
    popS = POP[np.arange(N)]
    Isel_num = (W2.reshape(P, M, N) * popS[None, None, :]).sum(axis=(1, 2))   # / 4^n
    phys = np.zeros(P, dtype=np.int64)
    Fr = F.reshape(P, M, N)
    for i in range(a):
        idx = np.arange(N) ^ (1 << i)
        phys += (Fr != Fr[:, :, idx]).sum(axis=(1, 2))
    # physical: count over (x,y) of F(x,y)!=F(x^e_i,y), total 2^n per coordinate => Isel = phys/2^n
    exact_inf_ok = bool(np.all(Isel_num * 1 == phys * (2 ** n)))      # Isel_num/4^n == phys/2^n
    Isel = Isel_num.astype(np.float64) / float(4 ** n)
    # data influence (exact), for I(F)
    Itot_num = (W2 * POP[np.arange(N * M)][None, :]).sum(axis=1)
    Itot = Itot_num.astype(np.float64) / float(4 ** n)
    boundM = np.minimum(a, 2.0 / LN2 * Isel)
    boundB = a * h2(Isel / a)
    return dict(HF=HF, HR=HR, Hb=Hb, BW=BW, MW=MW, MW2=MW2, Delta=Delta, Isel=Isel, Itot=Itot,
                boundM=boundM, boundB=boundB, exact_inf_ok=exact_inf_ok)

def summarize(name, d, a, m, extra=None):
    tol = 1e-9
    P = len(d['Delta'])
    Phi = d['boundM'] + d['boundB']
    okM = bool(np.all(d['MW'] <= d['boundM'] + tol)) and bool(np.all(d['MW'] >= -tol))
    okB = bool(np.all(d['BW'] <= d['boundB'] + tol)) and bool(np.all(d['BW'] >= -tol))
    okId = float(np.max(np.abs(d['MW'] - d['MW2'])))
    zero = d['Isel'] == 0
    okZero = bool(np.all(np.abs(d['Delta'][zero]) < tol))
    pos = Phi > 1e-12
    ratio = np.where(pos, d['Delta'] / np.where(pos, Phi, 1.0), 0.0)
    j = int(np.argmax(ratio))
    # worst ratio at moderate energy: Isel/a in [0.05,0.5]
    mod = pos & (d['Isel'] / a >= 0.05)
    jm = int(np.argmax(np.where(mod, ratio, -1))) if np.any(mod) else -1
    s = dict(cases=P, a=a, m=m, M_W_bound_holds=okM, B_W_bound_holds=okB, identity_MW_maxerr=okId,
             zero_energy_zero_debt=okZero, exact_influence_spectral_equals_physical=d['exact_inf_ok'],
             max_ratio_Delta_over_bound=float(ratio[j]), at_Isel=float(d['Isel'][j]), at_Delta=float(d['Delta'][j]),
             min_slack=float(np.min(Phi - d['Delta'])),
             max_Delta_over_Isel=float(np.max(np.where(d['Isel'] > 0, d['Delta'] / np.where(d['Isel'] > 0, d['Isel'], 1), 0))),
             max_ratio_moderate_energy=(float(ratio[jm]) if jm >= 0 else None),
             moderate_at_Isel=(float(d['Isel'][jm]) if jm >= 0 else None))
    if extra: s.update(extra)
    res[name] = s
    print(name, json.dumps(s))

def all_funcs(m):
    M = 1 << m
    k = np.arange(1 << M, dtype=np.int64)
    bits = (k[:, None] >> np.arange(M)[None, :]) & 1
    return (1 - 2 * bits).astype(np.int64)     # (2^(2^m), 2^m)

# ---------------- P1: exhaustive a=1 ----------------
for m in (1, 2, 3):
    fs = all_funcs(m); K = fs.shape[0]
    i0, i1 = np.meshgrid(np.arange(K), np.arange(K), indexing='ij')
    G = np.stack([fs[i0.ravel()], fs[i1.ravel()]], axis=1)
    summarize(f"P1_a1_m{m}", analyse(G, 1, m), 1, m)

# ---------------- P2: exhaustive a=2 ----------------
for m in (1, 2):
    fs = all_funcs(m); K = fs.shape[0]
    grids = np.meshgrid(*[np.arange(K)] * 4, indexing='ij')
    G = np.stack([fs[g.ravel()] for g in grids], axis=1)
    summarize(f"P2_a2_m{m}", analyse(G, 2, m), 2, m)

# ---------------- P3: low-energy random a=1, m=4 ----------------
rng = np.random.default_rng(20261011)
m = 4; Mm = 1 << m; P = 20000
g0 = 1 - 2 * rng.integers(0, 2, size=(P, Mm))
g1 = g0.copy()
for t in range(P):
    k = int(rng.integers(1, 4))
    pos = rng.choice(Mm, size=k, replace=False)
    g1[t, pos] *= -1
G = np.stack([g0, g1], axis=1).astype(np.int64)
summarize("P3_a1_m4_lowenergy", analyse(G, 1, m), 1, m)

# ---------------- P4: bent splice, certified intervals ----------------
iv.dps = 60; mpmath.mp.dps = 60

def ip_bent(m):
    y = np.arange(1 << m)
    s = np.zeros_like(y)
    for i in range(0, m, 2):
        s ^= ((y >> i) & 1) & ((y >> (i + 1)) & 1)
    return (1 - 2 * s).astype(np.int64)

def entropy_iv(W2counts, denom):
    """exact masses w/denom with multiplicities -> interval entropy in bits"""
    tot = iv.mpf(0)
    for w, c in W2counts.items():
        if w == 0: continue
        pm = iv.mpf(w) / iv.mpf(denom)
        tot += c * pm * (iv.log(iv.mpf(denom)) - iv.log(iv.mpf(w))) / iv.log(2)
    return tot

def h2_iv(t):
    return -(t * iv.log(t) + (1 - t) * iv.log(1 - t)) / iv.log(2)

def splice_record(G, a, m):
    """G: (2^a, 2^m) branches; certified Delta, Isel, bound."""
    N = 1 << a; M = 1 << m; n = a + m
    F = np.transpose(G, (1, 0)).reshape(N * M)
    W = fwht(F[None, :])[0]; W2 = W * W
    HF = entropy_iv(Counter(W2.tolist()), 4 ** n)
    Gb = fwht(G); Hb = iv.mpf(0)
    for b in range(N):
        Hb += entropy_iv(Counter((Gb[b] * Gb[b]).tolist()), 4 ** m)
    Hb = Hb / N
    popS = POP[np.arange(N)]
    Isel = Fraction(int((W2.reshape(M, N) * popS[None, :]).sum()), 4 ** n)
    Itot = Fraction(int((W2 * POP[np.arange(N * M)]).sum()), 4 ** n)
    Delta = HF - Hb
    Is = iv.mpf(Isel.numerator) / iv.mpf(Isel.denominator)
    bound = 2 / iv.log(2) * Is + a * h2_iv(Is / a)
    return dict(Delta=Delta, Isel=Isel, Itot=Itot, bound=bound, HF=HF, Hb=Hb)

def ivs(x):
    return [mpmath.nstr(x.a, 25), mpmath.nstr(x.b, 25)]

def closed_form(m):
    mpmath.mp.dps = 60
    u = mpmath.mpf(2) ** (-mpmath.mpf(m) / 2)
    A = 0; B = 0
    for e in (1, -1):
        w = (1 + e * u) / 2
        A += -2 * w * (1 - e * u) ** 2 * mpmath.log(abs(1 - e * u), 2)
        x = 1 - 2 * e * u
        B += 0 if x == 0 else w * x ** 2 * mpmath.log(abs(x), 2)
    return m * u ** 2 + A + B

bent = {}
for m in (2, 4, 6, 8, 10, 12):
    g0 = ip_bent(m); g1 = g0.copy(); g1[0] *= -1
    rec = splice_record(np.stack([g0, g1]), 1, m)
    I = rec['Isel']
    third = 3 / iv.log(2)
    slack = rec['bound'] - rec['Delta']
    cf = closed_form(m)
    bent[m] = dict(Isel=str(I), Isel_is_2_pow_minus_m=(I == Fraction(1, 2 ** m)), I_total=str(rec['Itot']),
                   Delta=ivs(rec['Delta']), bound=ivs(rec['bound']),
                   bound_minus_Delta_positive=bool(slack.a > 0),
                   Delta_over_Isel_minus_m_minus_3_over_ln2=ivs(rec['Delta'] / iv.mpf(I.numerator) * I.denominator - m - third),
                   bound_minus_Delta_over_Isel=ivs(slack / iv.mpf(I.numerator) * I.denominator),
                   bound_minus_Delta_over_Isel_squared=ivs(slack / (iv.mpf(I.numerator) / I.denominator) ** 2),
                   Delta_over_bound=ivs(rec['Delta'] / rec['bound']),
                   closed_form_Delta=mpmath.nstr(cf, 30),
                   closed_form_inside_enclosure=bool(rec['Delta'].a <= cf <= rec['Delta'].b),
                   Delta_over_Itotal=ivs(rec['Delta'] / (iv.mpf(rec['Itot'].numerator) / rec['Itot'].denominator)))
    print('bent m', m, json.dumps(bent[m]))
res['P4_bent_splice_a1'] = bent

# tensor squares (a=2): F2(x1,x2,y1,y2) = F(x1,y1) F(x2,y2), selector (x1,x2), data (y1,y2)
tens = {}
for m in (2, 4):
    g0 = ip_bent(m); g1 = g0.copy(); g1[0] *= -1
    Gs = np.stack([g0, g1])
    M = 1 << m
    G2 = np.zeros((4, M * M), dtype=np.int64)
    for x1 in range(2):
        for x2 in range(2):
            b = x1 + 2 * x2
            G2[b] = (Gs[x1][:, None] * Gs[x2][None, :]).T.reshape(M * M)  # index y1 + M*y2
    r2 = splice_record(G2, 2, 2 * m)
    r1 = splice_record(Gs, 1, m)
    tens[m] = dict(Delta2=ivs(r2['Delta']), twice_Delta1=ivs(2 * r1['Delta']), Isel2=str(r2['Isel']), Isel1=str(r1['Isel']),
                   Isel_additive=(r2['Isel'] == 2 * r1['Isel']),
                   bound2=ivs(r2['bound']), twice_bound1=ivs(2 * r1['bound']),
                   Delta_additive_within_1e_40=bool(abs(mpmath.mpf((r2['Delta'] - 2 * r1['Delta']).mid)) < mpmath.mpf(10) ** -40))
    print('tensor m', m, json.dumps(tens[m]))
res['P4_bent_splice_tensor_square_a2'] = tens

# ---------------- P4s: symbolic series of G(u) = bound - Delta for the one-bit bent splice ----------------
import sympy as sp
u = sp.symbols('u', positive=True)
A = 0; B = 0
for e in (1, -1):
    w = (1 + e * u) / 2
    A += -2 * w * (1 - e * u) ** 2 * sp.log(1 - e * u) / sp.log(2)
    B += w * (1 - 2 * e * u) ** 2 * sp.log(1 - 2 * e * u) / sp.log(2)
Gfun = 2 / sp.log(2) * u ** 2 - (1 - u ** 2) * sp.log(1 - u ** 2) / sp.log(2) - A - B
serG = sp.series(Gfun, u, 0, 9).removeO()
serAB = sp.series((A + B) / u ** 2, u, 0, 7).removeO()
res['P4_symbolic'] = dict(
    note="u = 2^(-m/2); Delta = m u^2 + A(u) + B(u); bound - Delta = G(u) (no log u terms)",
    series_bound_minus_Delta=str(sp.nsimplify(sp.simplify(serG))),
    series_AplusB_over_u2=str(sp.simplify(serAB)),
    coeff_u2_of_G=str(sp.simplify(serG.coeff(u, 2))),
    coeff_u4_of_G=str(sp.simplify(serG.coeff(u, 4))),
    coeff_u4_of_G_float=float(serG.coeff(u, 4)),
    limit_AplusB_over_u2=str(sp.simplify(sp.limit((A + B) / u ** 2, u, 0))))
print('symbolic', json.dumps(res['P4_symbolic']))

# ---------------- P5: independent check of A017's quadratic reused-address ledger ----------------
def rank2(rows, ncols):
    rows = [r for r in rows]; r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, len(rows)):
            if (rows[i] >> c) & 1: piv = i; break
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and (rows[i] >> c) & 1: rows[i] ^= rows[r]
        r += 1
    return r

def kernel_basis(Mcols, n):
    # Mcols[i] = column i of M as int (a bits). Kernel of x -> sum x_i Mcols[i].
    basis = []
    # brute force small n
    vecs = []
    for x in range(1, 1 << n):
        s = 0
        for i in range(n):
            if (x >> i) & 1: s ^= Mcols[i]
        if s == 0: vecs.append(x)
    # extract a basis by greedy rank
    cur = []
    for v in vecs:
        if rank2(cur + [v], n) > len(cur): cur.append(v)
    return cur

rnd = random.Random(7)
fails = []; cases = 0
for trial in range(300):
    n = rnd.randint(1, 5); a = rnd.randint(0, 3)
    Mcols = [rnd.randrange(1 << a) if a > 0 else 0 for _ in range(n)]
    if rnd.random() < 0.3:
        for i in range(n):
            if rnd.random() < 0.5: Mcols[i] = 0
    Q = {(i, j): rnd.randint(0, 1) for i in range(n) for j in range(i + 1, n)}
    l = [rnd.randint(0, 1) for _ in range(n)]; c0 = rnd.randint(0, 1)
    D = 1 << a; ntot = n + D; size = 1 << ntot
    idx = np.arange(size)
    x = idx & ((1 << n) - 1); y = idx >> n
    qv = np.full(size, c0)
    for (i, j), v in Q.items():
        if v: qv ^= ((x >> i) & 1) & ((x >> j) & 1)
    for i in range(n):
        if l[i]: qv ^= (x >> i) & 1
    Mx = np.zeros(size, dtype=np.int64)
    for i in range(n):
        Mx ^= np.where((x >> i) & 1, Mcols[i], 0)
    ybit = (y >> Mx) & 1
    F = ((1 - 2 * qv) * (1 - 2 * ybit)).astype(np.int64)
    W = fwht(F[None, :])[0]; W2 = W * W
    nz = W2[W2 > 0]
    # statistics
    r = rank2(list(Mcols), a) if a > 0 else 0
    Bm = [[0] * n for _ in range(n)]
    for (i, j), v in Q.items():
        Bm[i][j] = Bm[j][i] = v
    Kb = kernel_basis(Mcols, n)
    # polar form on kernel: matrix K^T B K
    def bform(u_, v_):
        s = 0
        for i in range(n):
            if (u_ >> i) & 1:
                for j in range(n):
                    if (v_ >> j) & 1: s ^= Bm[i][j]
        return s
    rowsK = []
    for ui in Kb:
        rv = 0
        for jj, vj in enumerate(Kb):
            if bform(ui, vj): rv |= (1 << jj)
        rowsK.append(rv)
    k = rank2(rowsK, len(Kb)) if Kb else 0
    cc = sum(1 for i in range(n) if Mcols[i] != 0)
    bb = sum(1 for i in range(n) if Mcols[i] == 0 and any(Bm[i]))
    dd = sum(1 for i in range(n) if Mcols[i] == 0 and not any(Bm[i]) and l[i] == 1)
    flat = (len(set(nz.tolist())) == 1)
    count_ok = (len(nz) == 2 ** (2 * r + k))
    mass_ok = flat and (int(nz[0]) * 2 ** (2 * r + k) == 4 ** ntot)
    I = Fraction(int((W2 * POP[idx]).sum()), 4 ** ntot)
    I_ok = (I == 1 + Fraction(cc + bb, 2) + dd)
    ineq_ok = (2 * r + k) <= 4 * (I - 1 - dd)
    cases += 1
    if not (flat and count_ok and mass_ok and I_ok and ineq_ok):
        fails.append(dict(n=n, a=a, Mcols=Mcols, r=r, k=k, c=cc, b=bb, d=dd, I=str(I), flat=flat, count_ok=count_ok, I_ok=I_ok))
res['P5_A017_independent'] = dict(cases=cases, failures=len(fails), first_failures=fails[:5],
                                  note="independent numpy/F2 implementation; flat spectrum count 2^(2r+k) and exact influence 1+(c+b)/2+d")
print('A017 check', cases, 'failures', len(fails))

res['runtime_seconds'] = round(time.time() - T0, 2)
txt = json.dumps(res, indent=1, default=str)
open(os.path.join(OUT, 'verify_results.json'), 'w', encoding='utf8').write(txt)
print('sha256', hashlib.sha256(txt.encode()).hexdigest(), 'runtime', res['runtime_seconds'])
