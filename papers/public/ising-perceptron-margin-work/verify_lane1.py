"""Acceptance pass for the negative lane: record-level verification + trend.

Covers the tranche shards (lane1_*.jsonl) and the wall-gap slabs
(lane_gap_*.jsonl), together [-1.05, -0.9455].  Checks per record: ok flag
true, 8 sub-balls x 9 checks = 72 checks, every check's serialized endpoints
actually satisfy its want direction, slab kappa coverage is contiguous and
abuts the rectangle strip edge at -0.9455.  Then the located-lambda trend:
per slab the max (worst) lambda hi endpoint over sub-balls, linear fit vs
kappa midpoint, projected zero.
"""
import glob
import json
import re

EDGE = -0.9455          # rectangle strip's negative edge the lane must reach
LANE_LO = -1.05         # certified lane bottom (tranche 1)


def ball_bounds(s):
    """'[mid +/- rad]' or plain float string -> (lo, hi), outward."""
    m = re.match(r'\[([-\d.e+]+) \+/- ([-\d.e+]+)\]', s)
    if m:
        mid, rad = float(m.group(1)), float(m.group(2))
        return mid - rad, mid + rad
    v = float(s)
    return v, v

recs = []
for f in (sorted(glob.glob('results/box/lane1_*.jsonl'))
          + sorted(glob.glob('results/box/lane_gap_*.jsonl'))):
    for line in open(f):
        recs.append(json.loads(line))

print('records:', len(recs))
bad = 0
n_checks = set()
for r in recs:
    if not r['ok']:
        bad += 1
        print('NOT-OK slab', r['kappa_lo'], r['kappa_hi'])
    n_checks.add(len(r['checks']))
    for c in r['checks']:
        lo = ball_bounds(c['lo'])[0]
        hi = ball_bounds(c['hi'])[1]
        good = lo > 0 if c['want'] == '>0' else hi < 0
        if not good or not c['ok']:
            bad += 1
            print('CHECK-BAD', r['kappa_lo'], c['name'], c['want'], c['lo'], c['hi'])
print('check-counts per record:', sorted(n_checks))
print('bad total:', bad)

# coverage: sort by kappa_lo, confirm contiguity
recs.sort(key=lambda r: float(r['kappa_lo']))
gaps = 0
for a, b in zip(recs, recs[1:]):
    if abs(float(a['kappa_hi']) - float(b['kappa_lo'])) > 1e-12:
        gaps += 1
        print('GAP', a['kappa_hi'], '->', b['kappa_lo'])
print('coverage: [%s, %s] gaps=%d' % (recs[0]['kappa_lo'], recs[-1]['kappa_hi'], gaps))
lo_ok = abs(float(recs[0]['kappa_lo']) - LANE_LO) < 1e-12
edge_ok = abs(float(recs[-1]['kappa_hi']) - EDGE) < 1e-12
print('bottom at %s: %s ; abuts strip edge %s: %s'
      % (LANE_LO, 'yes' if lo_ok else 'NO', EDGE, 'yes' if edge_ok else 'NO'))

# lambda trend: per slab, worst (max) hi over the 8 lambda checks
xs, ys = [], []
for r in recs:
    lam_his = [ball_bounds(c['hi'])[1] for c in r['checks']
               if c['name'].startswith('lambda')]
    if len(lam_his) != 8:
        print('LAM-COUNT', r['kappa_lo'], len(lam_his))
    k_mid = 0.5 * (float(r['kappa_lo']) + float(r['kappa_hi']))
    xs.append(k_mid)
    ys.append(max(lam_his))

n = len(xs)
sx = sum(xs); sy = sum(ys)
sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
intercept = (sy - slope * sx) / n
resid = [y - (slope * x + intercept) for x, y in zip(xs, ys)]
rms = (sum(e * e for e in resid) / n) ** 0.5
zero = -intercept / slope
print('lambda trend: slope=%.6g intercept=%.6g rms=%.3g' % (slope, intercept, rms))
print('worst lambda at kappa=%.4f: %.6g ; at %.4f: %.6g' % (xs[0], ys[0], xs[-1], ys[-1]))
print('projected lane wall (lambda hi = 0): kappa = %.4f' % zero)
print('max lambda hi anywhere: %.6g' % max(ys))

ok = (bad == 0 and gaps == 0 and len(recs) == 209
      and sorted(n_checks) == [72] and lo_ok and edge_ok
      and max(ys) < 0)
print('LANE ACCEPTANCE: %s' % ('PASS' if ok else 'FAIL'))
import sys
sys.exit(0 if ok else 1)
