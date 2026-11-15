"""PLAN item 4 (an agent): STRAT15 bank + refinements cover the 9,370 input boxes exactly,
refinement trees partition their roots, and sampled certificates re-verify with my own Bernstein code.

Targets c2, d1, C1 come from exact_bernstein.chart_data() (checked against STRAT10 and STRAT8 by
my_cs_cross.py / my_cs_cross2.py). Constraints are my own formulas from my_check1b.py.
Usage: python3 my_check4.py STRAT15_DIR N_SAMPLE SEED [--partial]
"""
import sys, json, random, time
from fractions import Fraction as F
from pathlib import Path
S15 = Path(sys.argv[1]).resolve(); NS = int(sys.argv[2]); SEED = int(sys.argv[3])
PARTIAL = '--partial' in sys.argv
sys.path.insert(0, str(Path(__file__).resolve().parent))
import importlib.util
_sp = importlib.util.spec_from_file_location('mc1b', Path(__file__).resolve().parent / 'my_check1b_lib.py')
L = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(L)
sys.path.insert(0, str(S15))
import exact_bernstein as ex
targets, gs, cs = ex.chart_data()

def key(r): return (r['source'], int(r['node']), r.get('path', '') or '')
def fbox(b): return [tuple(map(F, x)) for x in b]
def vol(b):
    v = F(1)
    for a, c in b: v *= (c - a)
    return v

inv = json.loads((S15 / 'inventory.json').read_text())['records']
inv = [r for r in inv if r['old']['kind'] != 'collar'] if any(r['old']['kind'] == 'collar' for r in inv) else inv
need = json.loads((S15 / 'domain_audit.json').read_text())['need_new_sign']
inputs = {}
for r in inv + need:
    k = key(r); assert k not in inputs, ('duplicate input', k); inputs[k] = fbox(r['box'])
print('input boxes', len(inputs))
bank = json.loads((S15 / 'certificates.json').read_text())
refs = json.loads((S15 / 'refinements.json').read_text())['records']
print('bank', bank['processed'], '/', bank['total'], bank['counts'], 'refinements', len(refs))
seen = {}
for r in bank['records']:
    k = key(r); assert k not in seen, ('bank duplicate', k); seen[k] = r
    assert fbox(r['box']) == inputs[k], ('bank box differs from input', k)
refd = {key(r): r for r in refs}
problems = []

def walk(t, box, leaves, depth=0):
    assert fbox(t['box']) == box, 'tree box mismatch'
    if t['kind'] == 'split':
        ax = t['axis']; a, b = box[ax]; m = (a + b) / 2
        lb = list(box); rb = list(box); lb[ax] = (a, m); rb[ax] = (m, b)
        assert len(t['children']) == 2
        walk(t['children'][0], lb, leaves, depth + 1); walk(t['children'][1], rb, leaves, depth + 1)
    else:
        leaves.append((t, box, depth))

closed_bank = 0; leaves_all = []
for k, r in seen.items():
    certs = r['certificates']; excl = any(c['kind'] == 'exclusion' for c in certs.values())
    if not r['failed'] or excl:
        if not excl: assert set(certs) == {'c2', 'd1', 'C1'}, ('missing coefficient', k)
        closed_bank += 1; leaves_all.append(({'kind': 'certificates', 'certificates': certs}, inputs[k], 0, k))
    else:
        if k not in refd: problems.append(('unclosed, no refinement', k)); continue
        lv = []; walk(refd[k]['tree'], inputs[k], lv)
        assert sum(vol(b) for _, b, _ in lv) == vol(inputs[k]), ('volume', k)
        for t, b, d in lv:
            if t['kind'] == 'open': problems.append(('open leaf', k, d))
            leaves_all.append((t, b, d, k))
missing = [k for k in inputs if k not in seen]
print('closed in bank', closed_bank, 'refined roots', sum(1 for k in seen if k in refd),
      'missing from bank', len(missing), 'problems', len(problems))
for p in problems[:20]: print('  PROBLEM', p)
if not PARTIAL: assert not missing and not problems

# certificate re-verification
def check_cert(c, box):
    lam = c.get('lambda', {})
    if isinstance(lam, str): lam = json.loads(lam.replace("'", '"'))
    if c['kind'] == 'positivity':
        p = {m: F(v) for m, v in targets[c['coefficient']].items()}
        res, used = L.residual(box, lam); p = L.add(p, res)
    else:
        p, used = L.residual(box, lam)
    if used and L.bern_min(L.X, box) < 0: return 'GUARD'
    return L.bern_min(p, box, c.get('bernstein_degrees'))

cert_leaves = [(t, b, d, k) for t, b, d, k in leaves_all if t['kind'] == 'certificates']
coll = [(t, b, d, k) for t, b, d, k in leaves_all if t['kind'] == 'collar']
print('certificate leaves', len(cert_leaves), 'collar leaves', len(coll))
rng = random.Random(SEED)
ref_leaves = [x for x in cert_leaves if x[3] in refd]
sample = ref_leaves + rng.sample([x for x in cert_leaves if x[3] not in refd], min(NS, len(cert_leaves) - len(ref_leaves)))
ok = bad = 0; t0 = time.time()
for t, b, d, k in sample:
    for name, c in t['certificates'].items():
        assert fbox(c['box'] if not isinstance(c['box'], str) else json.loads(c['box'].replace("'", '"'))) == b, 'cert box'
        mn = check_cert(c, b)
        if mn != 'GUARD' and mn > 0: ok += 1
        else: bad += 1; print('FAIL', k, d, name, c['kind'], c.get('verification'), mn if mn == 'GUARD' else float(mn))
print('certificates checked', ok + bad, 'PASS', ok, 'FAIL', bad, 'seconds %.1f' % (time.time() - t0))
