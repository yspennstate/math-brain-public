# the second high-z case again, fresh seed, smaller draws (the first recheck ran out of memory with commit at 97 pct)
exec(open('mc_drift.py', encoding='utf-8').read().split('for (q, c, r) in')[0].replace('20261018', '4242'))
q, c, r = 0.3677197, 0.3253855, 0.4143942
for eta in (0.4998, 0.5):
    m, s = mc(q, c, r, eta, n=500_000, reps=160); cl = cs.closed(q, c, r, eta)[3:]
    print('x=(%.4f,%.4f,%.4f) eta=%.4f MC' % (q, c, r, eta), np.round(m, 7), '+-', np.round(s, 7), 'closed', np.round(cl, 7), 'z', np.round((m - cl) / s, 2), flush=True)
