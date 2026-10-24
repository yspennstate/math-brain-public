from pathlib import Path
from fractions import Fraction as F
import json
r=json.loads(Path('directed_chain_result.json').read_text(encoding='utf8')); pi=[F(v) for v in r['stationary_at_1_over_4']]
Q=[[F(0) for j in range(8)] for i in range(8)]
for x in range(8):
 for i in range(3):
  rate=F(1) if x>>i&1 else (F(1,4) if i==0 or (x>>(i-1)&1) else F(0))
  Q[x][x^(1<<i)]+=rate;Q[x][x]-=rate
assert all(sum(Q[i][j]*pi[i] for i in range(8))==0 for j in range(8))
s='import Mathlib.Data.Rat.Lemmas\n\n-- Three-site immigration chain at per-edge infection rate 1/4.\n'
for i,p in enumerate(pi):s+=f'def p{i} : ℚ := {p.numerator} / {p.denominator}\n'
s+='\ntheorem normalization : '+' + '.join(f'p{i}' for i in range(8))+' = 1 := by decide +kernel\n'
s+='\ntheorem strictly_positive : '+' ∧ '.join(f'0 < p{i}' for i in range(8))+' := by decide +kernel\n'
eq=[]
for j in range(8):
 terms=[]
 for i in range(8):
  c=Q[i][j]
  if c:terms.append(f'(({c.numerator} : ℚ) / {c.denominator}) * p{i}')
 eq.append('('+' + '.join(terms)+' = 0)')
s+='\ntheorem all_stationarity_equations :\n    '+' ∧\n    '.join(eq)+' := by decide +kernel\n'
s+='\ntheorem exact_joint_probability : p6 + p7 = 2551 / 507375 := by decide +kernel\n'
s+='\ntheorem smallest_scale_obstruction : (1 : ℚ) / 3^25 < p6 + p7 := by decide +kernel\n'
Path('SecondChecks.lean').write_text(s,encoding='utf8')
runner=Path('run_lean.py').read_text(encoding='utf-8-sig').replace('CertificateChecks.lean','SecondChecks.lean').replace('lean_check.txt','second_lean_check.txt')
Path('run_second_lean.py').write_text(runner,encoding='utf8')
print('Generated five finite checks; all eight rational balances verified by Python fractions.')
