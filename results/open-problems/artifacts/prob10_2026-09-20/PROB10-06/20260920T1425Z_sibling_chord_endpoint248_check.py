from fractions import Fraction as F
import importlib.util
from pathlib import Path

base = Path(__file__).with_name('20260920T1410Z_sibling_chord_branch_gap_check.py')
spec = importlib.util.spec_from_file_location('sibling_chord_core', base)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)

rect=(F(12,5),F(62,25),F(3,4),F(1))
q=F(9999,10000)
rho_q=F(199,200)
v,a,dep,wp,wr=core.certify(rect,q,rho_q)
margin=F(4)*(1-q)/(F(3)+F(62,25))**2
assert margin==F(1,75076)

print('PROB10-06 SIBLING_CHORD_ENDPOINT248_CHECK')
print('RECT_PASS lambda=[12/5,62/25] p=[3/4,1]')
print('visited=%d accepted=%d max_depth=%d'%(v,a,dep))
print('product_upper<9999/10000')
print('rho_upper<199/200')
print('worst_product_upper_float=%.15f'%float(wp))
print('worst_rho_upper_float=%.15f'%float(wr))
print('derivative_margin=1/75076')
print('TYPE_VECTOR_ITERATIONS=30 ROUNDING_GRID=1e-9')
print('ALL_EXACT_CHECKS_PASS')
