import numpy as np, math
d = np.load('mom_16000.npz'); z = math.pi**2/6; z3 = 1.2020569031595942
kap = (2*z3 - z)/z**2
ns = np.unique(np.geomspace(1000, 16000, 25).astype(int))
L = np.log(ns)
for name, y, target in [('VS/(n2L2)', d['vaS'][ns]/(ns**2*L**2), kap), ('VC/(n2L2)', d['vaC'][ns]/(ns**2*L**2), kap),
                        ('VQ/(n4L2)', d['vaQ'][ns]/(ns**4.0*L**2), 2/11), ('EQ/(n2L)', d['muQ'][ns]/(ns**2*L), 1.0)]:
    for deg in (1, 2, 3):
        X = np.vstack([L**-k for k in range(deg+1)]).T
        c = np.linalg.lstsq(X, y, rcond=None)[0]
        print(name, 'deg', deg, 'c0=%.5f' % c[0], 'target %.5f' % target, 'last %.5f' % y[-1])
