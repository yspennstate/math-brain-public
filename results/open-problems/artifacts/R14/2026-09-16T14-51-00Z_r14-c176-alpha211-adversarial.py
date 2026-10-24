#!/usr/bin/env python3
"""Exact adversarial check: alpha=2.11 is NOT certified by the frozen C176
16-mode / degree-17-tail / 7-term-log / 12-term-entropy Bernstein envelope.
This is a route-specific failure only, not a perceptron counterexample.
"""
from fractions import Fraction
import runpy, contextlib, io

buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    d=runpy.run_path('artifacts/R14/2026-09-16T14-51-00Z_r14-c176-weighted-lower_checker.py')

padd=d['padd']; pscale=d['pscale']; affine_power=d['affine_power']; bernstein_coeffs=d['bernstein_coeffs']
ent=d['entropy_lower']; logu=d['log_upper']
alpha=Fraction(211,100)
P=padd(ent,pscale(logu,-alpha))
assert P[0]==0 and P[1]==0
H=P[2:]
bad=[]
for s in range(20):
    a=Fraction(s,20); b=Fraction(s+1,20)
    beta=bernstein_coeffs(affine_power(H,a,b))
    for j,v in enumerate(beta):
        if v <= 0:
            bad.append((s,j,v))
assert bad
s,j,v=bad[0]
print('R14 C176 adversarial alpha=211/100 route test: PASS')
print('  first nonpositive Bernstein coefficient at interval',s,'basis',j)
print('  sign:', 'negative' if v<0 else 'zero')
print('  exact numerator digits:', len(str(abs(v.numerator))))
print('  exact denominator digits:', len(str(v.denominator)))
print('  decimal rendering:', float(v))
print('  conclusion: frozen certificate does not prove alpha=2.11; no model-level refutation claimed')
