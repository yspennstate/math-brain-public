from pathlib import Path
import json
p=Path(__file__).resolve().parents[1]/'out/REVIEW.json'
d=json.loads(p.read_text(encoding='utf-8'))
a=d['integer_comparison']
assert a['lhs']==7**4<2*6**4==a['rhs']
assert a['strict_margin']==a['rhs']-a['lhs']==191
print('PASS exact first-reset logarithm sign; analytic review in PROOF.md')
