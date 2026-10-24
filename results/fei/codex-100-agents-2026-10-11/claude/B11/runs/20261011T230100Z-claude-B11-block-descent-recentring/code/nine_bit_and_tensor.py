"""Block-descent phi and ratio for (i) the nine-bit component control f = 1 - 2*1_{A u B},
A = {(y,z): wt(y)<=1} in {0,1}^5 x {0,1}^4, B = {(11111,0000)}, and its two components alone;
(ii) a tensor product check phi(g x h) <= min(phi g, phi h, ratio g, ratio h). float64 evidence."""
import sys, json, numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from descent_scan import analyze, descent
def phi_ratio(f, n):
    r = analyze(f[None, :], n); H, I = r['H'][0], r['I'][0]
    phi, phi1, argA = descent(r, n)
    return dict(H=float(H), I=float(I), ratio=float(H / I), phi=float(phi[0]), phi_single=float(phi1[0]), argblock=int(argA[0]))
out = {}
n = 9; N = 1 << n
def y_of(x): return x & 31
def z_of(x): return x >> 5
inA = np.array([bin(y_of(x)).count('1') <= 1 for x in range(N)])
inB = np.array([(y_of(x) == 31 and z_of(x) == 0) for x in range(N)])
for name, S in (('A', inA), ('B', inB), ('AuB', inA | inB)):
    out['nine_' + name] = phi_ratio(np.where(S, -1.0, 1.0), n); print(name, out['nine_' + name], flush=True)
# tensor check: g = 3-bit point defect, h = 2-bit point defect (AND)
g = np.ones(8); g[0] = -1; h = np.ones(4); h[0] = -1
gh = np.array([g[x & 7] * h[x >> 3] for x in range(32)])
out['tensor'] = dict(g=phi_ratio(g, 3), h=phi_ratio(h, 2), gh=phi_ratio(gh, 5)); print(out['tensor'])
json.dump(out, open(sys.argv[1], 'w'), indent=1)
