"""(a) restrictions and derivatives of the J-maximisers: for each coordinate, the two restrictions (prime? read-once
over AND/OR?  bias, H/I) and the derivative's support size; monotone form (up to input negations) and minimal true sets."""
import sys, json, itertools
import numpy as np
sys.path.insert(0, '.')
from core import polite, stats, is_prime, decompose, relevant, compress
from structure import max_coin_set
polite()
out = open('../logs/profile_maximisers.log', 'w')
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n'); out.flush()
def tab(s):
    return np.array([-1 if ch == '1' else 1 for ch in s], dtype=np.int8)

def monotone_form(t):
    """Find input negations (and output negation) making t monotone (true=-1 increasing in bits); return minimal true sets."""
    N = t.shape[0]; n = int(round(np.log2(N)))
    x = np.arange(N)
    for outneg in (1, -1):
        for neg in range(1 << n):
            u = outneg * t[x ^ neg]
            ok = True
            for i in range(n):
                lo = x[((x >> i) & 1) == 0]
                # monotone: true (-1) at lo implies true at lo|bit
                if np.any((u[lo] == -1) & (u[lo | (1 << i)] == 1)):
                    ok = False; break
            if ok:
                tr = [int(y) for y in x if u[y] == -1]
                mins = [y for y in tr if not any((z != y) and (z & y) == z for z in tr)]
                return neg, outneg, [[i for i in range(n) if (m >> i) & 1] for m in mins]
    return None

def is_read_once(t):
    d = decompose(t)
    return 'P' not in d.replace('(', ' ').split('[')[0] and '[' not in d

cands = {'P4 path 2-DNF (J=6)': '1100000011101110'}
rows = json.load(open('../logs/search_J_n6_s1.json'))
cands['n=6 J-max (6.347)'] = rows[0]['table']
for name, s in cands.items():
    t = tab(s); st = stats(t); n = st['n']
    mf = monotone_form(t)
    log('== %s  H=%.6f I=%.6f J=%.6f prime=%s' % (name, st['H'], st['I'], st['H'] / (st['I'] - 1), is_prime(t)))
    log('   monotone up to NPN: %s' % ('no' if mf is None else 'yes, input negation mask %s, minimal true sets %s' % (format(mf[0], '0%db' % n), mf[2])))
    x = np.arange(1 << n)
    for i in range(n):
        for bit in (0, 1):
            r = t[x[((x >> i) & 1) == bit]]
            sr = stats(r)
            log('   x%d=%d: %-60s mean=%+.4f H/I=%.4f prime=%s' % (i, bit, decompose(r), sr['mean'], sr['ratio'] if sr['I'] > 0 else float('nan'), is_prime(r)))
        lo = x[((x >> i) & 1) == 0]
        dsup = int((t[lo] != t[lo | (1 << i)]).sum())
        log('   D_x%d f support: %d of %d points; Delta/Inf=%.4f' % (i, dsup, 1 << (n - 1), st['Delta'][i] / st['Inf'][i]))
