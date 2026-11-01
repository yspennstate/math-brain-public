import json
import math
import numpy as np


def eig_desc(M):
    return np.linalg.eigvalsh(M)[::-1]


def orth(rng, n):
    Q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    return Q


def ell(rho):
    return (math.sqrt(rho * rho + 4.0) - rho) / 2.0


def psd_with_tail(rng, m, r, tailcap):
    vals = np.empty(m)
    if r:
        vals[:r] = rng.uniform(10.0, 100.0, r)
    vals[r:] = rng.uniform(0.0, tailcap, m-r)
    rng.shuffle(vals)
    Q = orth(rng, m)
    return Q @ np.diag(vals) @ Q.T


def signed_tail_suite():
    rng = np.random.default_rng(360923)
    violations = 0
    min_pos = float('inf')
    min_neg = float('inf')
    requested = 5000
    used = 0
    while used < requested:
        m = int(rng.integers(6, 13))
        u = int(rng.integers(1, 4))
        v = int(rng.integers(1, 4))
        if u + v > m:
            continue
        rminus = int(rng.integers(0, max(1, m-u+1)))
        rplus = int(rng.integers(0, max(1, m-v+1)))
        rminus = min(rminus, m-u)
        rplus = min(rplus, m-v)
        need_pos = u + rminus
        need_neg = v + rplus
        if need_pos + need_neg > m:
            extra = need_pos + need_neg - m
            cut = min(extra, rminus)
            rminus -= cut
            need_pos -= cut
            extra -= cut
            cut = min(extra, rplus)
            rplus -= cut
            need_neg -= cut
            extra -= cut
            if extra:
                continue
        kp = 1.5 + rng.random()
        km = 1.5 + rng.random()
        spec = list(kp + 2*rng.random(need_pos))
        spec += list(-(km + 2*rng.random(need_neg)))
        spec += list(rng.uniform(-0.8, 0.8, m-len(spec)))
        spec = np.array(spec)
        rng.shuffle(spec)
        Q = orth(rng, m)
        H0 = Q @ np.diag(spec) @ Q.T
        e0 = eig_desc(H0)
        em0 = eig_desc(-H0)
        kappa_p = e0[u+rminus-1]
        kappa_m = em0[v+rplus-1]

        cap_n = 0.25*rng.random() + 0.05
        cap_p = 0.25*rng.random() + 0.05
        N = psd_with_tail(rng, m, rminus, cap_n)
        P = psd_with_tail(rng, m, rplus, cap_p)
        nvals = eig_desc(N)
        pvals = eig_desc(P)
        beta_p = nvals[rminus] if rminus < m else 0.0
        beta_m = pvals[rplus] if rplus < m else 0.0

        delta = 0.15*rng.random() + 0.02
        T = rng.normal(size=(m, m))
        T = (T + T.T) / 2.0
        T *= delta / np.linalg.norm(T, 2)
        H = H0 + P - N + T
        Lp = kappa_p - delta - beta_p
        Lm = kappa_m - delta - beta_m
        pos_margin = eig_desc(H)[u-1] - Lp
        neg_margin = eig_desc(-H)[v-1] - Lm
        min_pos = min(min_pos, float(pos_margin))
        min_neg = min(min_neg, float(neg_margin))
        if pos_margin < -1e-8 or neg_margin < -1e-8:
            violations += 1
        used += 1
    return {
        'cases': used,
        'violations': violations,
        'min_positive_margin': min_pos,
        'min_negative_margin': min_neg,
    }


def partner_suite():
    rng = np.random.default_rng(360925)
    pre_violations = 0
    final_violations = 0
    min_pre_pos = float('inf')
    min_pre_neg = float('inf')
    min_final_pos = float('inf')
    min_final_neg = float('inf')
    cases = 5000
    for _ in range(cases):
        s, d, m = 2, 5, 7
        mup = float(rng.uniform(1.5, 3.0))
        mun = float(rng.uniform(1.5, 3.0))
        dvals = np.array([mup+rng.random()*2 for _ in range(3)] +
                         [-(mun+rng.random()*2) for _ in range(2)])
        Qd = orth(rng, d)
        D = Qd @ np.diag(dvals) @ Qd.T
        Rsh = rng.normal(size=(s, d))
        target = float(rng.uniform(0.0, 0.5))
        Rsh *= target / np.linalg.norm(Rsh, 2)
        rho = np.linalg.norm(Rsh, 2)
        S = rng.normal(size=(s, s))
        S = (S + S.T) / 2.0
        L = np.block([[np.eye(s), Rsh], [np.zeros((d, s)), np.eye(d)]])
        H0 = L @ np.block([[S, np.zeros((s, d))],
                           [np.zeros((d, s)), D]]) @ L.T
        c = ell(rho)**2
        u, v, rminus, rplus = 2, 1, 1, 1
        dp = np.sort(dvals[dvals > 0])[::-1]
        dm = np.sort(-dvals[dvals < 0])[::-1]
        base_p = c * dp[u+rminus-1]
        base_m = c * dm[v+rplus-1]
        pre_p = eig_desc(H0)[u+rminus-1] - base_p
        pre_m = eig_desc(-H0)[v+rplus-1] - base_m
        min_pre_pos = min(min_pre_pos, float(pre_p))
        min_pre_neg = min(min_pre_neg, float(pre_m))
        if pre_p < -1e-8 or pre_m < -1e-8:
            pre_violations += 1

        N = psd_with_tail(rng, m, rminus, float(rng.uniform(0.02, 0.25)))
        P = psd_with_tail(rng, m, rplus, float(rng.uniform(0.02, 0.25)))
        beta_n = eig_desc(N)[rminus]
        beta_p = eig_desc(P)[rplus]
        delta = float(rng.uniform(0.01, 0.2))
        T = rng.normal(size=(m, m))
        T = (T + T.T) / 2.0
        T *= delta / np.linalg.norm(T, 2)
        H = H0 + P - N + T
        Lp = base_p - beta_n - delta
        Lm = base_m - beta_p - delta
        final_p = eig_desc(H)[u-1] - Lp
        final_m = eig_desc(-H)[v-1] - Lm
        min_final_pos = min(min_final_pos, float(final_p))
        min_final_neg = min(min_final_neg, float(final_m))
        if final_p < -1e-8 or final_m < -1e-8:
            final_violations += 1
    return {
        'cases': cases,
        'pre_violations': pre_violations,
        'final_violations': final_violations,
        'min_pre_positive_margin': min_pre_pos,
        'min_pre_negative_margin': min_pre_neg,
        'min_final_positive_margin': min_final_pos,
        'min_final_negative_margin': min_final_neg,
    }


if __name__ == '__main__':
    out = {
        'signed_tail_suite': signed_tail_suite(),
        'partner_congruence_suite': partner_suite(),
        'note': 'Finite deterministic numerical sanity checks only; analytic proof is in REPORT.md.'
    }
    print(json.dumps(out, indent=2, sort_keys=True))
