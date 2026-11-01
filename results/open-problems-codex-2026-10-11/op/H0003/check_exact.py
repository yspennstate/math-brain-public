from fractions import Fraction as F
import json
from pathlib import Path
p=F(3,4)
f=lambda s:(1-p+p*s)**2
q=F(1,9)
assert f(q)==q
assert 1-q==F(8,9)
assert (1-p+p*q)**3==F(1,27)
x=F(0)
iterations=[]
for k in range(7):
    assert 0<=x<=q
    iterations.append({'generation':k,'extinction_by_generation':str(x),'decimal':float(x)})
    x=f(x)
# Verify the fixed-point factorization at finitely many rational points;
# the symbolic identity is proved separately, including in Lean when it passes.
for a in range(-5,16):
    s=F(a,7)
    assert f(s)-s==(s-1)*(9*s-1)/16
out={'p':str(p),'extinction':str(q),'survival':str(1-q),
     'ordinary_degree_three_root_survival':str(1-(1-p+p*q)**3),
     'iterations':iterations,'result':'ALL_EXACT_CHECKS_PASS'}
Path(__file__).with_name('exact_results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
