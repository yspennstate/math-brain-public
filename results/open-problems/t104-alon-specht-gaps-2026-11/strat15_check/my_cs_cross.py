"""Cross-check STRAT15's q-split of the target against independently built targets (an agent).

c0 - c1 + c2 (q = -1, N = 5) must be a constant multiple of the STRAT8 face numerator
(zero_face.construct, a separate code path from STRAT10's construct). Also prints the
monomial supports and checks c2 is not identically zero.
Usage: python3 my_cs_cross.py STRAT15_DIR
"""
import sys
from fractions import Fraction as F
from pathlib import Path
S15 = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(S15))
import exact_bernstein as ex
targets, gs, cs = ex.chart_data()
c0, c1, c2 = cs
keys = set(c0) | set(c1) | set(c2)
alt = {m: F(c0.get(m, 0) - c1.get(m, 0) + c2.get(m, 0)) for m in keys}
alt = {m: c for m, c in alt.items() if c}
print('terms c0 c1 c2', len(c0), len(c1), len(c2), 'N=5 combo terms', len(alt))
assert c2, 'c2 identically zero'
import importlib.util; _sp = importlib.util.spec_from_file_location("face5", S15 / "STRAT14" / "STRAT8" / "zero_face.py"); _m = importlib.util.module_from_spec(_sp); sys.path.insert(0, str(S15 / "STRAT14" / "STRAT8")); _sp.loader.exec_module(_m)
construct = _m.construct
num = construct()[-1]
face = {tuple(m): F(int(c.numerator), int(c.denominator)) for m, c in num.terms()}
assert set(face) == set(alt), ('support differs', len(set(face) ^ set(alt)))
ratios = {alt[m] / face[m] for m in face}
print('distinct ratios', len(ratios), [str(r) for r in list(ratios)[:3]])
assert len(ratios) == 1, 'q=-1 combination is NOT proportional to the STRAT8 face target'
print('PASS: c0 - c1 + c2 =', str(ratios.pop()), 'x STRAT8 face numerator, coefficientwise')
# the three certified targets are the stated combinations
assert targets['c2'] == c2
d1 = {m: c1.get(m, 0) + 2 * c2.get(m, 0) for m in keys}; d1 = {m: c for m, c in d1.items() if c}
C1 = {m: c0.get(m, 0) + c1.get(m, 0) + c2.get(m, 0) for m in keys}; C1 = {m: c for m, c in C1.items() if c}
assert targets['d1'] == d1 and targets['C1'] == C1
print('PASS: targets c2, d1 = c1 + 2 c2, C1 = c0 + c1 + c2 as stated')
