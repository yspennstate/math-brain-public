"""Near-rank-one limit of the Schmidt-entropy defect ratio for M = [[a, 1],[0, b]] (normalised), a = lam*t, b = t,
t -> 0, in 60-digit arithmetic.  Also M = [[a, 1],[c, b]] scans."""
import mpmath as mp
mp.mp.dps = 60
def H(ps): return -mp.fsum([p*mp.log(p, 2) for p in ps if p > 0])
def defect(M):
    A = mp.matrix(M); nrm = mp.sqrt(sum(A[i, j]**2 for i in range(A.rows) for j in range(A.cols))); A = A/nrm
    U, S, V = mp.svd_r(A)
    s = [S[k]**2 for k in range(len(S))]
    lhs = H([A[i, j]**2 for i in range(A.rows) for j in range(A.cols)])
    rhs = H(s) + mp.fsum([s[k]*(H([U[i, k]**2 for i in range(A.rows)]) + H([V[k, j]**2 for j in range(A.cols)])) for k in range(len(s))])
    B = mp.fsum([x*(1-x) for x in s])
    return (lhs - rhs)/B
for lam in (0.25, 0.5, 0.8, 1.0, 1.25, 2.0):
    vals = [defect([[lam*t, 1], [0, t]]) for t in (mp.mpf('1e-3'), mp.mpf('1e-5'), mp.mpf('1e-8'), mp.mpf('1e-12'))]
    print('lam=%.2f' % lam, [mp.nstr(v, 10) for v in vals])
print('--- M = [[a,1],[c,b]] with c = a b (1 - eta) ---')
best = (-9, None)
for la in (0.5, 1.0, 2.0):
    for eta in (-3, -1, -0.5, 0.1, 0.5, 0.9, 1.5, 2, 3, 5):
        for t in (mp.mpf('1e-3'), mp.mpf('1e-6')):
            a = la*t; b = t; c = a*b*(1 - eta)
            v = defect([[a, 1], [c, b]])
            if v > best[0]: best = (v, la, eta, t)
        print('lam=%.1f eta=%5.2f ratio(t=1e-6)=%s' % (la, eta, mp.nstr(v, 8)))
print('best', best)
