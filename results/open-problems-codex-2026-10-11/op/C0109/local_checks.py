from fractions import Fraction as F
from pathlib import Path
import json

cases=[]
for h in [F(1,4),F(1,10),F(1,31),F(1,1000)]:
 for i in range(-5500,5501,11):
  left=F(i,1000)
  right=left+h
  if right<-5 or left>5:continue
  m=left//h
  assert -7<=m*h<=7
  assert m*h<=left and right<=(m+3)*h
  assert max(abs(m*h),abs((m+3)*h))<8 and F(6)**2+F(8)**2<F(20)**2
  cases.append([str(h),str(left),m])

expo=[]
for rho in [F(1,100),F(1,16),F(1,2)]:
 for Q in [F(2),F(10)]:
  Q0=Q+rho+3
  assert Q0-2-rho>Q
  D=1
  assert Q0/2-rho/2>=D
  requested=Q+rho+2
  assert requested-rho>Q
  expo.append({'rho':str(rho),'Q':str(Q),'Q0':str(Q0)})
out={'scope':'Exact finite covering and failure-exponent checks only. The local stochastic lemma is proved in DIRECT_UPPER.md G.','covering_cases':len(cases),'exact_bad_area_and_union_exponents':expo,'covering_first_cases':cases[:12]}
Path('local_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print('Exact local checks passed:',len(cases),'coverings and',len(expo),'failure-exponent balances.')
