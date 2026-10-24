import itertools, math
from compose_rec import compose_step, X, AND, OR
def chain(pattern, n):
    cur = dict(X); res = None
    for t in range(n - 1):
        gate = AND if pattern[t % len(pattern)] == 'A' else OR
        try: res = compose_step(gate, [dict(X), cur])
        except ZeroDivisionError: return None
        if res['Var'] < 1e-9: return None
        cur = res
    return res
best = []
for L in range(1, 11):
    for pat in itertools.product('AO', repeat=L):
        pat = ''.join(pat); r = chain(pat, 300)
        if r is None: continue
        best.append((r['H'] / r['I'], pat, r['U'] / r['I'], (r['H'] - 2 * (r['I'] - r['Var'])) / (2 * r['U'])))
best.sort(reverse=True)
for b in best[:10]: print('pattern %-10s H/I=%.4f U/I=%.4f  H/(2(I-V)+2U)=%.4f' % (b[1], b[0], b[2], (b[0]) / (2*(1) + 0) if False else b[3]))
