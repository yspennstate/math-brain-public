"""Rerun every C8 piece from its logged r_in and compare every segment row and the final line with logs/."""
import sys, json
sys.path[:0] = ['../C8_eta_cell/scripts', '.']
import entry_eta as E
E.setup('1/2', '1/5000')
L = 'T240/C8_eta_cell/logs/'
for q in sys.argv[1:]:
    theirs = [json.loads(l) for l in open(L + q + '.jsonl')]
    h = theirs[0]; rows = {r['k']: r for r in theirs if 'k' in r}
    k0, k1 = h['piece'][0], max(rows) + 1
    out = 'rerun_all_%s.jsonl' % q  # written beside the script
    E.run_piece('1600', '0.004', out, k0, k1, h['r_in'])
    mine = [json.loads(l) for l in open(out)]
    mrows = {r['k']: r for r in mine if 'k' in r}
    keys = ('d', 'mu', 'R', 'r', 'sw', 'Xw')
    diff = [k for k in rows if k not in mrows or any(rows[k][x] != mrows[k][x] for x in keys)]
    end_t = [r for r in theirs if 'piece_done' in r]; end_m = [r for r in mine if 'piece_done' in r]
    print(q, 'segments', len(rows), 'differing rows', len(diff), diff[:5],
          'final line', ('identical' if end_t == end_m else 'DIFFERENT') if end_t else '(partial piece, no final line)', flush=True)
