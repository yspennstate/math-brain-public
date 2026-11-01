"""Measured per-band kappa-sensitivities across certified margins.

The interval program (sec:interval) needs one number per Region-I
band: how fast its certified worst value moves along the margin
axis.  The band lattice is shared across margins up to the wedge
rotation, so bands whose rectangles coincide exactly between two
margins give certified finite differences
|Delta worst / Delta kappa| - a mean drift over the gap, which sizes
the re-certification pitch (it bounds no local derivative; the
certified derivative enclosure remains the machinery an interval
theorem needs, as the paper states).

Reads every results/huang_region1_<tag>.json, pairs adjacent
margins, matches bands by exact rectangle, and writes
results/kappa_sensitivity_bands.csv plus a summary to stdout.

Run: python measure_kappa_sensitivity.py
"""
import csv
import json
import os

TAGS = [('n0p45', -0.45), ('n0p15', -0.15), ('n0p05', -0.05),
        ('0p05', 0.05), ('0p08', 0.08), ('0p0995', 0.0995),
        ('0p13', 0.13)]


def load(tag):
    path = 'results/huang_region1_%s.json' % tag
    if not os.path.exists(path):
        return None
    m = json.load(open(path))
    out = {}
    for rec in m['results']:
        if rec.get('ok') and rec.get('worst') is not None:
            out[tuple(str(x) for x in rec['band'])] = float(rec['worst'])
    return out


def main():
    loaded = [(t, k, load(t)) for t, k in TAGS]
    loaded = [(t, k, d) for t, k, d in loaded if d]
    rows = []
    print('%-18s %8s %8s %8s %8s %8s' % (
        'pair', 'shared', 'median', 'p90', 'max', 'min_m'))
    for (t1, k1, d1), (t2, k2, d2) in zip(loaded[:-1], loaded[1:]):
        shared = sorted(set(d1) & set(d2))
        dk = abs(k2 - k1)
        sens = []
        for b in shared:
            s = abs(d2[b] - d1[b]) / dk
            m1 = abs(d1[b])
            m2 = abs(d2[b])
            mb = min(m1, m2)
            sens.append((s, mb, b))
            rows.append(dict(pair='%s-%s' % (t1, t2), t0=b[0], t1=b[1],
                             th0=b[2], th1=b[3],
                             sens=round(s, 6),
                             margin_left=round(m1, 8),
                             margin_right=round(m2, 8),
                             radius_left=(round(m1 / s, 6) if s > 0
                                          else ''),
                             radius_right=(round(m2 / s, 6) if s > 0
                                           else ''),
                             radius_min=(round(mb / s, 6) if s > 0
                                         else '')))
        if not sens:
            print('%-18s %8d' % ('%s-%s' % (t1, t2), 0))
            continue
        ss = sorted(x[0] for x in sens)
        n = len(ss)
        # the summary statistic: the smallest margin-to-sensitivity
        # ratio over the THINNER endpoint of each band.  The
        # sensitivity is a finite-difference secant over the pair's
        # kappa gap, so this is a sizing indicator, not a certified
        # kappa-radius: no local derivative or Lipschitz bound is
        # claimed (that object is the interval program's).  Per-side
        # values are in the CSV.
        ratios = sorted(m / s for s, m, _ in sens if s > 0)
        print('%-18s %8d %8.3f %8.3f %8.1f %8.5f' % (
            '%s-%s' % (t1, t2), n, ss[n // 2], ss[int(n * 0.9)],
            ss[-1], ratios[0] if ratios else float('nan')))
    with open('results/kappa_sensitivity_bands.csv', 'w',
              newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print('wrote results/kappa_sensitivity_bands.csv (%d rows)'
          % len(rows))


if __name__ == '__main__':
    main()
