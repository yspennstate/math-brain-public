"""Hull the strip's certified per-slab enclosures over a 2varfn slab:
alpha from certified_intervals*.csv, (q, psi) from the located
endpoint enclosures in results/box/result_*.json, all padded outward.
Prints the pilot arguments for direct-enclosure mode and refuses gaps.

Usage: python slab_windows.py <kappa_lo> <kappa_hi>
"""
import csv
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, 'results')
ARB = re.compile(r'\[([-+0-9.eE]+) \+/- ([0-9.eE+-]+)\]')


def arb_bounds(s):
    """Outward float bounds of an arb interval string (or plain number)."""
    m = ARB.match(s.strip())
    if m:
        mid, rad = float(m.group(1)), float(m.group(2))
    else:
        mid, rad = float(s), 0.0
    pad = max(1e-15 * max(1.0, abs(mid)), rad * 1e-6)
    return mid - rad - pad, mid + rad + pad


def windows(klo, khi):
    eps = 1e-9
    # alpha from the interval CSVs
    arows = []
    for name in ('certified_intervals.csv', 'certified_intervals_nak.csv'):
        p = os.path.join(R, name)
        if os.path.exists(p):
            arows += [r for r in csv.DictReader(open(p, newline=''))
                      if float(r['kappa_hi']) > klo + eps
                      and float(r['kappa_lo']) < khi - eps]
    if not arows:
        raise SystemExit('no certified alpha rows in range')
    # (q, psi) from the box result jsons
    qlo = plo = float('inf')
    qhi = phi = float('-inf')
    edges = []
    for f in glob.glob(os.path.join(R, 'box', 'result_*.json')):
        try:
            data = json.load(open(f))
        except ValueError:
            continue
        for rec in data:
            slab = rec.get('slab')
            if not isinstance(slab, dict) or not rec.get('ok'):
                continue
            slo, shi = float(slab['kappa_lo']), float(slab['kappa_hi'])
            if not (shi > klo + eps and slo < khi - eps):
                continue
            edges.append((slo, shi))
            for key in ('q_located_alb', 'q_located_aub'):
                for s in rec.get(key, []):
                    a, b = arb_bounds(s)
                    qlo, qhi = min(qlo, a), max(qhi, b)
            for key in ('psi_located_alb', 'psi_located_aub'):
                for s in rec.get(key, []):
                    a, b = arb_bounds(s)
                    plo, phi = min(plo, a), max(phi, b)
    if not edges:
        raise SystemExit('no box slab records in range')
    edges.sort()
    if edges[0][0] > klo + eps or edges[-1][1] < khi - eps:
        raise SystemExit('box slabs do not span the requested range')
    for (a, b), (c, d) in zip(edges, edges[1:]):
        if c > b + eps:
            raise SystemExit('gap in box slabs at [%.6f, %.6f]' % (b, c))
    alo = min(float(r['alpha_lb']) for r in arows) - 5e-7
    ahi = max(float(r['alpha_ub']) for r in arows) + 5e-7
    return dict(kappa_lo=klo, kappa_hi=khi,
                alpha_lo='%.9f' % alo, alpha_hi='%.9f' % ahi,
                q_lo='%.6f' % (qlo - 1e-6), q_hi='%.6f' % (qhi + 1e-6),
                psi_lo='%.6f' % (plo - 1e-6), psi_hi='%.6f' % (phi + 1e-6),
                n_alpha_rows=len(arows), n_box_slabs=len(edges))


if __name__ == '__main__':
    w = windows(float(sys.argv[1]), float(sys.argv[2]))
    for k, v in w.items():
        print('%s = %s' % (k, v))
