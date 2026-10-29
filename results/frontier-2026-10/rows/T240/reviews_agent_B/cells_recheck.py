# re-run the C6 cell test on the first, a middle and the last plateau cell from their recorded float centres and radius floors
import sys, json; sys.path[:0] = ['scripts']
from fractions import Fraction as F
import widen_eta as W
cells = [r for r in map(json.loads, open('logs/plateau_cells.jsonl')) if r.get('result') == 'pass']
cells.sort(key=lambda r: F(r['eta_lo']))
for r in (cells[0], cells[len(cells) // 2], cells[-1]):
    why, info = W.cell(F(r['eta_lo']), F(r['eta_hi']), [F(v) for v in r['center']], F(r['radius_floor']))
    print(r['eta_lo'], r['eta_hi'], why, 'box half-width %.4e (log %.4e)' % (info[0], r['info'][0]) if info else '')
