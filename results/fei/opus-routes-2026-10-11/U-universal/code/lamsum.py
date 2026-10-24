"""Global lift sum sum_i Lambda_i / I (Lambda_i = sum_T m_T r_T in the full law), next to G/I and U/I."""
import numpy as np, json
from feilib import *
from dU_exact import local_decomp
from upward import Uprime
from sweepG import compose
from families import *
g5 = np.array(json.load(open("../data/anneal_G.json"))["5"]["table"])
maj3 = np.array([1 if bin(x).count('1') < 2 else -1 for x in range(8)])
sel = json.load(open("../data/anneal_sel2.json"))["9"]; gs = np.array(sel['g']); hs = np.array(sel['h'])
f9 = np.empty(2 * len(gs), dtype=np.int64); f9[0::2] = gs; f9[1::2] = hs
cases = {'g5': g5, 'maj3 o g5': compose(maj3, 3, g5, 5), 'sel9': f9, 'tribes2x4': tribes(2, 4), 'pd10': pointdefect(10), 'x003_k6r6': x003(6, 6), 'bent8': bent(4), 'maj9': maj(9)}
for k, t in cases.items():
    t = np.asarray(t); n = nbits(len(t)); p = spectrum(t); I = float(total_influence(p, n)); U = float(Uprime(p, n))
    L = G = KL = 0.0
    for i in range(n):
        d = local_decomp(t, i); L += d['Lam']; G += d['total']; KL += d['KL']
    print(f"{k:10s} sumLambda/I={L/I:.3f}  G/I={G/I:.3f}  KL/I={KL/I:.3f}  U/I={U/I:.3f}")
