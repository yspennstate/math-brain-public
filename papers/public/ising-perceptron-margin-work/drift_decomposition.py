"""Decompose each strip slab's alpha-enclosure width into DRIFT (the
motion of alpha*(kappa) across the slab, estimated from neighboring
slabs' midpoints) and SLACK (the bisection's stopping allowance) -
the two components the interval program must treat differently:
tightening removes slack, only narrower slabs remove drift.

Then translate: a tightened strip's residual (q, psi) spread per slab
gives the Region-I origin-ball radius, to compare against the star
(T_LONG = 0.012).  Reads certified_intervals*.csv; diagnostics.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, 'results')


def main():
    rows = []
    for name in ('certified_intervals.csv', 'certified_intervals_nak.csv'):
        p = os.path.join(R, name)
        if os.path.exists(p):
            rows += list(csv.DictReader(open(p, newline='')))
    rows.sort(key=lambda r: float(r['kappa_lo']))
    mids = [(0.5 * (float(r['kappa_lo']) + float(r['kappa_hi'])),
             0.5 * (float(r['alpha_lb']) + float(r['alpha_ub'])),
             float(r['alpha_ub']) - float(r['alpha_lb']),
             float(r['q_ub']) - float(r['q_lb']))
            for r in rows]
    print('%d slabs' % len(mids))
    print('%8s %10s %10s %10s %10s %8s' %
          ('kappa', 'width', 'drift', 'slack', 'slack/w', 'q_width'))
    worst_ratio = None
    samples = []
    for i in range(1, len(mids) - 1):
        k, a, w, qw = mids[i]
        drift = abs(mids[i + 1][1] - mids[i - 1][1]) / 2
        slack = max(0.0, w - drift)
        samples.append((k, w, drift, slack, qw))
        if worst_ratio is None or slack / w < worst_ratio[0]:
            worst_ratio = (slack / w, k)
    for j in range(0, len(samples), max(1, len(samples) // 12)):
        k, w, drift, slack, qw = samples[j]
        print('%8.4f %10.2e %10.2e %10.2e %10.2f %8.2e'
              % (k, w, drift, slack, slack / w, qw))
    slacks = [s[3] / s[1] for s in samples]
    drifts = [s[2] for s in samples]
    print('\nslack fraction: min %.2f median %.2f max %.2f'
          % (min(slacks), sorted(slacks)[len(slacks) // 2], max(slacks)))
    print('drift per slab: min %.2e median %.2e max %.2e'
          % (min(drifts), sorted(drifts)[len(drifts) // 2], max(drifts)))
    # residual tube after removing slack: drift stays; the (q, psi)
    # spread scales with the alpha spread at dq/dalpha ~ 2, and the
    # a1-ball radius ~ 0.55 * psi-spread + 1.3 * q-spread (the trial's
    # observed scale factors at the left end)
    med_drift = sorted(drifts)[len(drifts) // 2]
    q_spread = 2 * med_drift
    a1_ball = 0.5 * (0.55 * 6 * med_drift + 1.3 * q_spread)
    print('\ntightened-strip estimate at median drift: alpha spread '
          '%.2e -> q spread %.2e -> a1 ball ~%.2e vs star 0.012 (%s)'
          % (med_drift, q_spread, a1_ball,
             'FITS' if a1_ball < 0.006 else 'DOES NOT FIT'))


if __name__ == '__main__':
    main()
