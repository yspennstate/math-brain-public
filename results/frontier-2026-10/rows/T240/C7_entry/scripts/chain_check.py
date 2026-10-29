"""Check the run2 chain exactly: every junction r_out(j) <= r_in(j+1), coverage 0..K, trap r_end >= last r_out,
and the C6 root box inside the trap ball. Usage: python chain_check.py run2 p1 p2 p3b p4 p5 p6"""
import sys, json
sys.path[:0] = ['scripts', '.']
from fractions import Fraction as F
from iv_exact import I, S
import entry

d = sys.argv[1]; names = sys.argv[2:]
pieces = []
for n in names:
    rows = [json.loads(l) for l in open('%s/%s.jsonl' % (d, n))]
    head, last = rows[0], rows[-1]
    assert 'piece_done' in last, (n, 'not finished')
    assert not any(r.get('fail') for r in rows), (n, 'fail row')
    ks = [r['k'] for r in rows if 'k' in r]
    assert ks == list(range(head['piece'][0], head['piece'][1])), (n, 'segment gap')
    pieces.append((n, head['piece'], F(head['r_in']), F(last['r_out']), max(r['mu'] for r in rows if 'k' in r)))
ok = True
assert pieces[0][1][0] == 0 and pieces[0][2] == 0
for (a, pa, ia, oa, _), (b, pb, ib, ob, _) in zip(pieces, pieces[1:]):
    good = pa[1] == pb[0] and oa <= ib
    ok &= good
    print('%-4s -> %-4s node %4d  r_out %.6e  <=  r_in %.6e  %s' % (a, b, pa[1], float(oa), float(ib), 'OK' if good else 'BROKEN'))
K = pieces[-1][1][1]
tr = [json.loads(l) for l in open('%s/trap.jsonl' % d)][-1]
assert 'PASS' in tr and tr['K'] == K
good = pieces[-1][3] <= F(tr['r_end'])
ok &= good
print('last r_out %.6e <= trap r_end %s (rho %s, mu* %.4e) %s' % (float(pieces[-1][3]), tr['r_end'], tr['PASS']['rho'], float(F(tr['PASS']['mu'])), 'OK' if good else 'BROKEN'))
# C6 root box (x0 + [-1e-7,1e-7]^3 hull) inside the trap ball |P*^-1 (x - x0)| <= rho
Ps, Pinvs = entry.frame(entry.jac_f(entry.fl(entry.XSTAR)))
box = [entry.pm(F(11, 10 ** 8)) for _ in range(3)]
rad = entry.norm2_up(entry.matvec_rat(Pinvs, box))
good = rad < F(tr['PASS']['rho'])
ok &= good
print('C6 box (half width 1.1e-7) maps into z-radius %.3e < rho %s %s' % (float(rad), tr['PASS']['rho'], 'OK' if good else 'BROKEN'))
print('max mu over pieces', ['%s %.4f' % (p[0], float(p[4])) for p in pieces])
print('CHAIN', 'CLOSED' if ok else 'OPEN')
