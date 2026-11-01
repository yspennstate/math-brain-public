"""Check the eta-cell chain exactly: pieces cover 0..K with r_out(j) <= r_in(j+1), trap r_end >= last r_out,
the plateau cells cover the eta cell, and every certified plateau box lies inside the trap ball around c(eta).
Usage: python chain_check_eta.py DIR TRAPFILE CELLFILE q1 q2 ..."""
import sys, json
sys.path[:0] = ['scripts', '.']
from fractions import Fraction as F
from iv_exact import I
import entry_eta as E, entry

d, trapf, cellf = sys.argv[1:4]; names = sys.argv[4:]
E.setup('1/2', '1/5000')
pieces = []
for n in names:
    rows = [json.loads(l) for l in open('%s/%s.jsonl' % (d, n))]
    head, last = rows[0], rows[-1]
    assert head['eta0'] == '1/2' and head['we'] == '1/5000', (n, 'wrong cell')
    assert not any(r.get('fail') for r in rows), (n, 'fail row')
    ks = [r['k'] for r in rows if 'k' in r]
    if 'piece_done' in last:
        assert ks == list(range(head['piece'][0], head['piece'][1])), (n, 'segment gap')
        span, r_out = head['piece'], F(last['r_out'])
    else:
        # A piece cut short (the 16 Oct 13:51 crash): every completed segment row is certified on its own, so the
        # piece ends at the node after its last row. Rows keep r only as float(r), and float(Fraction) is correctly
        # rounded, so r_exact <= float(r) * (1 + 2^-52); a factor 1 + 1e-12 is used. The next piece's r_in must clear it.
        assert ks == list(range(head['piece'][0], ks[-1] + 1)), (n, 'segment gap')
        span, r_out = [head['piece'][0], ks[-1] + 1], F(last['r']) * (1 + F(1, 10 ** 12))
        print('%s: PARTIAL piece, ends at node %d (r_out from the last segment row, %.6e)' % (n, span[1], float(r_out)))
    pieces.append((n, span, F(head['r_in']), r_out, max(r['mu'] for r in rows if 'k' in r)))
ok = pieces[0][1][0] == 0 and pieces[0][2] == 0
for (a, pa, ia, oa, _), (b, pb, ib, ob, _) in zip(pieces, pieces[1:]):
    good = pa[1] == pb[0] and oa <= ib
    ok &= good
    print('%-4s -> %-4s node %4d  r_out %.6e  <=  r_in %.6e  %s' % (a, b, pa[1], float(oa), float(ib), 'OK' if good else 'BROKEN'))
K = pieces[-1][1][1]
tr = [json.loads(l) for l in open(trapf)][-1]
good = 'PASS' in tr and tr['K'] == K and tr['eta0'] == '1/2' and tr['we'] == '1/5000' and pieces[-1][3] <= F(tr['r_end'])
ok &= good
rho = F(tr['PASS']['rho'])
print('last r_out %.6e <= trap r_end %s (need_rho %.4e, rho %s, mu* %.4e) %s' % (
    float(pieces[-1][3]), tr['r_end'], tr['need_rho'], tr['PASS']['rho'], float(F(tr['PASS']['mu'])), 'OK' if good else 'BROKEN'))

# plateau cells: contiguous cover of [eta0 - we, eta0 + we]; each certified box inside the trap ball for every eta in its cell
xs0 = [F(v) for v in tr['xs0']]; ysx = [F(v) for v in tr['ys']]
Ps, Pinvs = entry.frame(entry.jac_f(entry.fl(xs0)))
cells = sorted({(F(r['eta_lo']), F(r['eta_hi'])): r for r in map(json.loads, open(cellf)) if r.get('result') == 'pass'}.items())
lo, hi = E.ETA0 - E.WE, E.ETA0 + E.WE
iv_list = [c[0] for c in cells]
cover = iv_list[0][0] <= lo and iv_list[-1][1] >= hi and all(a[1] >= b[0] for a, b in zip(iv_list, iv_list[1:]))
ok &= cover
print('plateau cells: %d, cover [%s, %s] contiguously: %s' % (len(cells), iv_list[0][0], iv_list[-1][1], 'OK' if cover else 'BROKEN'))
worst = F(0)
for (a, b), r in cells:
    if b <= lo or a >= hi: continue
    rad = F(r['info'][0]) + F(1, 10 ** 12)
    de = entry.iv(a - E.ETA0, b - E.ETA0)
    diff = [I.of(F(r['center'][i])) + entry.pm(rad) - I.of(xs0[i]) - de * I.of(ysx[i]) for i in range(3)]
    z = entry.norm2_up(entry.matvec_rat(Pinvs, diff))
    worst = max(worst, z)
good = worst < rho
ok &= good
print('largest z-radius of a plateau box about c(eta): %.4e < rho %s %s' % (float(worst), tr['PASS']['rho'], 'OK' if good else 'BROKEN'))
print('max mu over pieces', ['%s %.4f' % (p[0], float(p[4])) for p in pieces])
print('CHAIN', 'CLOSED' if ok else 'OPEN')
