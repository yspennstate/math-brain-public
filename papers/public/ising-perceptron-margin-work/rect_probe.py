"""Probe the strip rectangle clause at three points spanning the
Nakajima lane, to see whether the thin-rectangle contraction clears 1
at the deep end (kappa ~ 0.19) where the wide-rectangle product
saturated.  Cheap decision input before the full 180-slab run.
"""
import csv

from core import dec
from rect_strip import one_slab

rows = list(csv.DictReader(open('results/certified_intervals_nak.csv')))
targets = [0.11, 0.15, 0.185]
delta = dec('0.002')
for t in targets:
    row = min(rows, key=lambda r: abs(float(r['kappa_lo']) - t))
    out = one_slab(row, delta)
    print('kappa [%s, %s]  ok=%s  pieces_ok=%d/%d  worst_contraction=%s'
          % (row['kappa_lo'], row['kappa_hi'], out['ok'],
             out['pieces_ok'], out['n_sub'],
             str(out['contraction_worst'])[:22]), flush=True)
    if not out['ok']:
        print('   failing checks:', out['checks'])
