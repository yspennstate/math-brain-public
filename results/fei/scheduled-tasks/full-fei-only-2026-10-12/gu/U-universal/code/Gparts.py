"""Split G = sum_i Delta_i U into L_up, (L_down - Gamma) and sum_i KL_i (exact local formula)."""
import numpy as np, json
from feilib import *
from dU_exact import local_decomp
from sweepG import compose
from families import *
g5 = np.array(json.load(open("../data/anneal_G.json"))["5"]["table"])
maj3 = np.array([1 if bin(x).count('1') < 2 else -1 for x in range(8)])
cases = {'g5': g5, 'maj3 o g5': compose(maj3, 3, g5, 5), 'tribes2x4': tribes(2, 4), 'pd10': pointdefect(10), 'x003_k6r6': x003(6, 6), 'bent8': bent(4)}
for k, t in cases.items():
    t = np.asarray(t); n = nbits(len(t)); I = float(total_influence(spectrum(t), n))
    tot = dict(slogrs=0.0, tail=0.0, KL=0.0)
    for i in range(n):
        d = local_decomp(t, i)
        for kk in tot: tot[kk] += d[kk]
    print(f"{k:10s} I={I:.3f}  [s log(r/s)]/I={tot['slogrs']/I:.3f}  L_up/I={tot['tail']/I:.3f}  KL/I={tot['KL']/I:.3f}  G/I={(sum(tot.values()))/I:.3f}")
