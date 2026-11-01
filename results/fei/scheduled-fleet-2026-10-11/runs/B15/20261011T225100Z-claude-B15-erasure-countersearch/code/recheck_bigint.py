"""Second, independent exact path for the two witnesses: direct big-integer powers (b15_engine.exact_parts),
compared with K* and with rational lower bounds 539/200 (n=5) and 368/125 (n=6)."""
import sys, json, numpy as np
sys.path.insert(0, sys.argv[1])
from b15_engine import hadamard, exact_sign_Bi_minus_Kstar, exact_sign_Bi_minus_rational
W5 = {'n': 5, 'support': [2, 6, 22], 'rat': (539, 200)}
W6 = {'n': 6, 'support': [0, 1, 2, 4, 6, 8, 16, 17, 32, 40], 'rat': (368, 125)}
out = []
for w in (W5, W6):
    n = w['n']; D = 1 << n
    f = np.array([-1 if x in w['support'] else 1 for x in range(D)], dtype=np.int64)
    W = f @ hadamard(n)
    sk = [exact_sign_Bi_minus_Kstar(W, n, i) for i in range(n)]
    p, q = w['rat']
    sr = [exact_sign_Bi_minus_rational(W, n, i, p, q) for i in range(n)]
    out.append(dict(n=n, support=w['support'], walsh=[int(v) for v in W], sign_vs_Kstar=sk, rational=f'{p}/{q}', sign_vs_rational=sr))
    print(n, w['support'], 'vsK*', sk, f'vs {p}/{q}', sr)
json.dump(out, open(sys.argv[2], 'w', encoding='utf-8'), indent=1)
