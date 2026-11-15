"""STRAT15 cs vs STRAT10 zero_face numerator split by the power of q (an agent).
STRAT14 verify_targets proved STRAT10 num at q=-1 = 2 x STRAT8 face; this closes the chain to STRAT15's targets.
Usage: python3 my_cs_cross2.py STRAT15_DIR"""
import sys, importlib.util
from fractions import Fraction as F
from pathlib import Path
S15 = Path(sys.argv[1]).resolve(); sys.path.insert(0, str(S15))
import exact_bernstein as ex
targets, gs, cs = ex.chart_data()
spec = importlib.util.spec_from_file_location('faceN', S15/'STRAT14/STRAT13/STRAT12/STRAT10/zero_face.py')
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
b = mod.construct()
split = [{}, {}, {}]
for m, c in b[-1].items():
    split[m[-1]][tuple(m[:6])] = F(str(c))
print('STRAT10 terms by q power', [len(s) for s in split], 'STRAT15', [len(c) for c in cs])
for k in range(3):
    mine = {m: F(c) * 8 for m, c in cs[k].items()}
    if mine == split[k]: print('PASS q^%d: STRAT15 c%d x 8 == STRAT10 numerator coefficient exactly' % (k, k))
    else:
        d = set(mine) ^ set(split[k]); print('MISMATCH q^%d support diff %d; samples' % (k, len(d)), list(mine)[:2], list(split[k])[:2])
