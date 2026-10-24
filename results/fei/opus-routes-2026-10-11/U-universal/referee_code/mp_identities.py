"""50-digit mpmath checks of the identities claimed in U-loc on random laws / real vectors.

(a) Chain rule for ANY probability law P on subsets of [n]:  U(P) = B_i(P) - Gamma_i(P) + U(m_i),
    H(P) = B_i(P) + H(m_i), and the full chains along random orders.
(b) Theorem U-loc for genuine Boolean f (random, n = 5, 6), all coordinates:
    U(f) - (U(f+)+U(f-))/2 = sum_T m_T [ s log2(r/s) + (1-s) log2(1/(1-s)) + D2((1+eta)/2 || (1+x)/2) ].
(c) Structure of Lambda:  E_m R = 1,  Lambda_i = E_m[s R] = sum_T m_T r_T,  B_i - Gamma_i <= log2(e) Lambda_i,
    and sum_T m_T x_T^2 <= sum_T m_T eta_T^2 R(T) <= 4 Lambda_i.
"""
import random, json
import mpmath as mp

mp.mp.dps = 50
random.seed(4242)
L2 = mp.log(2)


def log2(x):
    return mp.log(x) / L2


def plog(p, q):
    return mp.mpf(0) if p == 0 else p * log2(q)


def upper(P, n):
    N = 1 << n
    return [mp.fsum(P[T] for T in range(N) if (T & S) == S) for S in range(N)]


def Hof(P):
    return -mp.fsum(plog(p, p) for p in P if p > 0)


def Uof(P, n):
    pi = upper(P, n)
    return mp.fsum(plog(P[S], pi[S] / P[S]) for S in range(1 << n) if P[S] > 0)


def Bi(P, n, i):
    N = 1 << n; tot = mp.mpf(0)
    for T in range(N):
        if (T >> i) & 1:
            continue
        a = P[T]; b = P[T | (1 << i)]; m = a + b
        if m > 0:
            s = b / m
            tot += m * (-(plog(s, s)) - plog(1 - s, 1 - s))
    return tot


def Gam(P, n, i):
    pi = upper(P, n); N = 1 << n
    return mp.fsum(plog(P[T | (1 << i)], pi[T] / pi[T | (1 << i)]) for T in range(N) if not (T >> i) & 1 and P[T | (1 << i)] > 0)


def merge(P, n, i):
    """law of S minus i, kept on the full index set (mass at sets containing i is moved down)."""
    Q = list(P)
    for T in range(1 << n):
        if not (T >> i) & 1:
            Q[T] = P[T] + P[T | (1 << i)]
            Q[T | (1 << i)] = mp.mpf(0)
    return Q


out = {}
# (a) random non-Boolean laws
worst_U = mp.mpf(0); worst_H = mp.mpf(0); worst_chain = mp.mpf(0)
for trial in range(25):
    n = random.randint(2, 5); N = 1 << n
    w = [mp.mpf(random.random()) ** 3 for _ in range(N)]
    for _ in range(random.randint(0, N // 2)):
        w[random.randrange(N)] = mp.mpf(0)
    if sum(w) == 0:
        w[0] = mp.mpf(1)
    Z = mp.fsum(w); P = [x / Z for x in w]
    for i in range(n):
        m = merge(P, n, i)
        worst_U = max(worst_U, abs(Uof(P, n) - (Bi(P, n, i) - Gam(P, n, i) + Uof(m, n))))
        worst_H = max(worst_H, abs(Hof(P) - (Bi(P, n, i) + Hof(m))))
    order = list(range(n)); random.shuffle(order)
    cur = P; sU = mp.mpf(0); sH = mp.mpf(0)
    for i in order:
        sU += Bi(cur, n, i) - Gam(cur, n, i); sH += Bi(cur, n, i); cur = merge(cur, n, i)
    worst_chain = max(worst_chain, abs(sU - Uof(P, n)), abs(sH - Hof(P)))
out['a_chain_one_step_U_err'] = mp.nstr(worst_U, 5)
out['a_chain_one_step_H_err'] = mp.nstr(worst_H, 5)
out['a_full_chain_err'] = mp.nstr(worst_chain, 5)


# (b) Boolean f, exact rational coefficients -> mp
def walsh_int(f, n):
    N = 1 << n
    return [sum(f[x] * (-1) ** bin(S & x).count('1') for x in range(N)) for S in range(N)]


worst_loc = mp.mpf(0); worst_lam = mp.mpf(0); lam_viol = 0; jensen_viol = 0; ER_err = mp.mpf(0)
for trial in range(12):
    n = random.choice([4, 5, 6]); N = 1 << n
    f = [random.choice([-1, 1]) for _ in range(N)]
    if trial % 3 == 1:
        f = [1] * N
        for _ in range(random.randint(1, 3)):
            f[random.randrange(N)] = -1
    W = walsh_int(f, n)
    a = [mp.mpf(w) / N for w in W]
    P = [x * x for x in a]
    pi = upper(P, n)
    U = Uof(P, n)
    for i in range(n):
        # restrictions: coefficients u +- v on the (n-1)-cube, represented on sets without i
        lo = [T for T in range(N) if not (T >> i) & 1]
        Pp = [mp.mpf(0)] * N; Pm = [mp.mpf(0)] * N
        for T in lo:
            Pp[T] = (a[T] + a[T | (1 << i)]) ** 2; Pm[T] = (a[T] - a[T | (1 << i)]) ** 2
        dU = U - (Uof(Pp, n) + Uof(Pm, n)) / 2
        # formula
        Cvec = [mp.mpf(0)] * N
        for T in lo:
            Cvec[T] = a[T] * a[T | (1 << i)]
        Cup = upper(Cvec, n)
        tot = mp.mpf(0); Lam = mp.mpf(0); EmR = mp.mpf(0); EmsR = mp.mpf(0)
        # rho and R for the merged law m
        mlaw = {T: a[T] ** 2 + a[T | (1 << i)] ** 2 for T in lo}
        rho = {T: (mlaw[T] / pi[T] if pi[T] > 0 else mp.mpf(0)) for T in lo}
        R = {Tp: mp.fsum(rho[T] for T in lo if (T & Tp) == T) for Tp in lo}
        lhs_j = mp.mpf(0); mid_j = mp.mpf(0)
        Infi = mp.fsum(P[T | (1 << i)] for T in lo)
        BmG = mp.mpf(0)
        for T in lo:
            u = a[T]; v = a[T | (1 << i)]; m = u * u + v * v
            if m == 0:
                continue
            s = v * v / m; r = pi[T | (1 << i)] / pi[T]
            eta = 2 * u * v / m; x = 2 * Cup[T] / pi[T]
            A = (1 + eta) / 2; Bq = (1 + x) / 2
            D2 = plog(A, A / Bq if Bq > 0 else 1) + plog(1 - A, (1 - A) / (1 - Bq) if 1 - Bq > 0 else 1)
            part = (plog(s, r / s) if s > 0 else 0) + plog(1 - s, 1 / (1 - s) if 1 - s > 0 else 1)
            tot += m * (part + D2)
            BmG += m * part
            Lam += m * r
            EmR += m * R[T]; EmsR += m * s * R[T]
            lhs_j += m * x * x; mid_j += m * eta * eta * R[T]
        worst_loc = max(worst_loc, abs(dU - tot))
        worst_lam = max(worst_lam, abs(EmR - 1), abs(EmsR - Lam))
        if BmG > Lam / L2 + mp.mpf(10) ** -40:
            lam_viol += 1
        if lhs_j > mid_j + mp.mpf(10) ** -40 or mid_j > 4 * Lam + mp.mpf(10) ** -40:
            jensen_viol += 1
        ER_err = max(ER_err, abs(BmG - (Bi(P, n, i) - Gam(P, n, i))))
out['b_Uloc_identity_err'] = mp.nstr(worst_loc, 5)
out['c_EmR_and_Lambda_err'] = mp.nstr(worst_lam, 5)
out['c_BminusGamma_le_log2e_Lambda_violations'] = lam_viol
out['c_jensen_chain_violations'] = jensen_viol
out['c_BminusGamma_formula_err'] = mp.nstr(ER_err, 5)
print(json.dumps(out, indent=1))
with open('mp_identities_results.json', 'w', encoding='utf-8') as fh:
    json.dump(out, fh, indent=1)
