import numpy as np, json
from feilib import *
from upward import Uprime, upper_sets
from anneal_dU import local_ratios
d = json.load(open("../data/anneal_dU.json"))
for key in ["5_max", "6_max", "7_max"]:
    t = np.array(d[key]["table"]); n = nbits(len(t)); p = spectrum(t); inf = influences(p, n)
    r = local_ratios(t, n); i = int(np.argmax(r))
    # decomposition at coordinate i
    idx = np.arange(1 << n); lo = idx[(idx >> i) & 1 == 0]; hi = lo | (1 << i)
    u2 = p[lo]; v2 = p[hi]; m = u2 + v2; pi = upper_sets(p, n)
    with np.errstate(divide='ignore', invalid='ignore'):
        Bi = float(np.where(m > 0, m * binh(np.where(m > 0, v2 / np.where(m>0,m,1), 0)), 0).sum())
        Gam = float(np.where(v2 > 0, v2 * np.log2(pi[lo] / np.where(pi[hi] > 0, pi[hi], 1)), 0).sum())
    print(key, 'i=', i, 'ratio', round(r[i], 3), 'Inf_i', round(inf[i], 4), 'B_i/Inf', round(Bi / inf[i], 3), 'Gamma/Inf', round(Gam / inf[i], 3),
          'H/I', round(float(entropy(p)) / inf.sum(), 3), 'U/I', round(float(Uprime(p, n)) / inf.sum(), 3), 'infs', np.round(inf, 3))
    print('   table', ''.join('1' if v == 1 else '0' for v in t))
