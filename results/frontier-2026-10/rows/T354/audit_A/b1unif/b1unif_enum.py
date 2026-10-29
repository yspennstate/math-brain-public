"""Independent check of NOTE 'Uniform in beta1' (agent A, 20 Oct 2026).
Exact enumeration over two independent epochs (all n!^2 orders) of
    e2 = E[(sum_q w_q b_pi(q)) F(eta)],  F(eta) = (1+eta)^(-1/2) - 1 + eta/2   (eps = 0),
    eta = sum_q a_q Z_pi(q),  a_q = (d/V) beta2^lag,  w_q = (1-beta1) beta1^lag,
against d*S, S = sum_e (1/n) sum_{q,r in e} (w_q-w_r)(a_q-a_r). The claim is |e2| <= C d S with C free of beta1.
Control: w one-hot at the lag where a_q is closest to the epoch mean of a (not comonotone): S ~ 0 but e2 is not.
No code shared with uniform_b1/transposition_check.py.
usage: python b1unif_enum.py   (prints a table)"""
import itertools, numpy as np

def run(b, d, beta2, wfun, label):
    b = np.asarray(b, float); n = len(b); assert abs(b.sum()) < 1e-12
    g2 = b**2; V = g2.mean(); Z = g2 - V
    perms = np.array(list(itertools.permutations(range(n))))          # n! x n
    lag = np.arange(2*n); a = (d/V)*beta2**lag; w = wfun(lag)
    # epoch 0 = lags 0..n-1, epoch 1 = lags n..2n-1, independent permutations
    eta0 = Z[perms] @ a[:n]; eta1 = Z[perms] @ a[n:]
    wb0 = b[perms] @ w[:n];  wb1 = b[perms] @ w[n:]
    eta = eta0[:, None] + eta1[None, :]
    F = (1 + eta)**-0.5 - 1 + eta/2
    T0 = (wb0[:, None]*F).mean(); T1 = (wb1[None, :]*F).mean()
    S = []
    for e in (0, 1):
        ww, aa = w[e*n:(e+1)*n], a[e*n:(e+1)*n]
        S.append(((ww[:, None]-ww[None, :])*(aa[:, None]-aa[None, :])).sum()/n)
    e2 = T0 + T1; St = S[0] + S[1]
    print(f"{label:28s} n {n} d {d:<6} b2 {beta2:<5} e2 {e2: .4e} S {St: .4e} "
          f"T0/(dS0) {T0/(d*S[0]) if S[0] else float('nan'): .4f} T1/(dS1) {T1/(d*S[1]) if S[1] else float('nan'): .4f} "
          f"e2/(dS) {e2/(d*St) if St else float('inf'): .4f}")
    return e2, St

if __name__ == "__main__":
    for b in ([4, -1, -1, -1, -1], [3, 1, -1, -1, -1, -1]):
        for d in (0.05, 0.01, 0.002):
            for beta2 in (0.8, 0.95):
                for b1 in (0, 0.5, 0.9, 0.99, 0.999, 0.9999):
                    run(b, d, beta2, lambda L, b1=b1: (1-b1)*b1**L, f"beta1 {b1}")
                n = len(b); a_ep = beta2**np.arange(n); q0 = int(np.argmin(abs(a_ep - a_ep.mean())))
                run(b, d, beta2, lambda L, q0=q0: (L == q0).astype(float), f"CONTROL one-hot lag {q0}")
