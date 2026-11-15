import numpy as np, math
d = np.load('mom_16000.npz'); N = 12000
z = math.pi**2/6; z3 = 1.2020569031595942; kap = (2*z3-z)/z**2
res = {}
for k in 'SC':
    mu, va = d['mu'+k], d['va'+k]
    u3 = np.zeros(N+1); h = 0.0
    for m in range(2, N+1):
        h += 1.0/(m-1); i = np.arange(1, m); p = m/(2*h*i*(m-i))
        t = np.full(m-1, float(m)) if k == 'S' else np.abs(2.0*i-m)
        Bn = t + mu[i] + mu[m-i] - mu[m]
        u3[m] = p @ (u3[i] + u3[m-i]) + 3*(p @ (Bn*(va[i]+va[m-i]))) + p @ Bn**3
    ns = np.unique(np.geomspace(1000, N, 25).astype(int)); L = np.log(ns)
    y = u3[ns]/(ns**3.0*L**3); sk = u3[ns]/va[ns]**1.5
    for deg in (1, 2, 3):
        X = np.vstack([L**-j for j in range(deg+1)]).T
        print(k, 'u3/(n3L3) deg', deg, 'c0=%.4f' % np.linalg.lstsq(X, y, rcond=None)[0][0], 'skew c0=%.4f' % np.linalg.lstsq(X, sk, rcond=None)[0][0])
    print(k, 'last n', N, 'u3/(n3L3)=%.4f' % y[-1], 'skew=%.4f' % sk[-1], 'targets a3=0.1076 skew=0.7240')
