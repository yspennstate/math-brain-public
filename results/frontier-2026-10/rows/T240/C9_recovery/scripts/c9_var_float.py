"""Float diagnostic: true spread of the face set along the reference (variational equation), vs the block bound."""
import json, numpy as np, sys
sys.path[:0] = ['.']
from scipy.integrate import solve_ivp
import fdrive, c9_cone
from fractions import Fraction as F
U, KAP = 1/20000, 1/100
xs = c9_cone.plateau_float()
P, Pinv, par, w = c9_cone.adapted_frame(xs)
P = np.array([[float(v) for v in r] for r in P])
d = json.load(open('kraw_cache.json')); S = 2**160
X = np.array([[a/S, b/S] for a, b in d['X']]); xc = np.array([float(F(v)) for v in d['xc']])
zo = np.abs(np.linalg.inv(P) @ ((X[:,1]-X[:,0])/2))
p0 = xc + P[:,0]*U
def rhs(t, y):
    x = y[:7]; Phi = y[7:].reshape(7,7)
    return np.concatenate([fdrive.f(x, 0.5), (fdrive.jac(x, 0.5) @ Phi).ravel()])
sol = solve_ivp(rhs, [0, 760], np.concatenate([p0, np.eye(7).ravel()]), method='DOP853', rtol=1e-11, atol=1e-14, dense_output=True)
for t in [0, 50, 100, 150, 186, 200, 225, 250, 300, 400, 500, 600, 742]:
    y = sol.sol(t); x = y[:7]; Phi = y[7:].reshape(7,7)
    Pk = np.linalg.eig(fdrive.jac(x, 0.5))[1]
    M = np.abs(Phi @ P)
    spread_u = M[:,0]*zo[0]; spread_s = M[:,1:] @ (zo[1:] + KAP*U)
    sp = np.linalg.norm(spread_u + spread_s)
    print(t, 'speed %.2e' % np.linalg.norm(fdrive.f(x,0.5)), 'u-part %.2e' % np.linalg.norm(spread_u), 's-part %.2e' % np.linalg.norm(spread_s),
          'max|Phi P_s| %.1f' % M[:,1:].max(), '|Phi P_u| %.1f' % M[:,0].max())
print('zo', zo)
