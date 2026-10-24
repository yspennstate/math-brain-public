import numpy as np, json
from feilib import *
from upward import Uprime
from dU_exact import local_decomp
d = json.load(open("../data/anneal_sel.json"))
for n in ["6", "7", "8"]:
    g = np.array(d[n]["g"]); h = np.array(d[n]["h"]); M = len(g); nn = int(n)
    f = np.empty(2 * M, dtype=np.int64); f[0::2] = g; f[1::2] = h
    dd = local_decomp(f, 0)
    print(n, {k: round(v / dd['Inf'], 3) for k, v in dd.items() if k != 'Inf'}, 'Inf', dd['Inf'])
    pg = spectrum(g); ph = spectrum(h)
    print('  U(g)=', round(float(Uprime(pg, nn - 1)), 3), 'U(h)=', round(float(Uprime(ph, nn - 1)), 3), 'U(f)=', round(float(Uprime(spectrum(f), nn)), 3),
          'H(g)', round(float(entropy(pg)), 3), 'H(h)', round(float(entropy(ph)), 3), 'I(g)', round(float(total_influence(pg, nn-1)), 3), 'I(h)', round(float(total_influence(ph, nn-1)), 3))
    print('  g', ''.join('1' if v == 1 else '0' for v in g)); print('  h', ''.join('1' if v == 1 else '0' for v in h))
    print('  g!=h at', [x for x in range(M) if g[x] != h[x]])
