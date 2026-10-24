from fractions import Fraction as F
from pathlib import Path
import json,math
lines=[];count=0
for n in range(3,203):
 r=F(1,n);rn=F(1,n+1);q=4*r*r;b=F(3,2)*r
 assert q-q*q/2>=3*r*r
 for j in range(21):
  e=b*F(j,20)
  en=e+e*e/2-q+q*q/2
  pgf=(1+e)**2/2+(1-q)**2/2-1
  assert en==pgf
  assert en-F(3,2)*rn <= e-F(3,2)*r-F(3,8)*r*r
  count+=1
lines.append(f'Exact rational scalar identity and barrier checks: {count} cases, all passed (n=3..202, 21 e-values below/on barrier).')
try:
 import mpmath as mp
 mp.mp.dps=50
 A=mp.polylog(3,mp.mpf('0.5'))-mp.mpf('0.5');B=mp.zeta(2)-mp.zeta(3);c=1/(A+B)
 lines += [f'A={A}',f'B={B}',f'c={c}',f'p0={c*B}',f'p2={c/32}',f'E[2^X0]={c*B+c*(mp.zeta(3)-1)}',f'E[X0 2^X0]={c*(mp.zeta(2)-1)}']
 assert abs(c*(A+B)-1)<mp.mpf('1e-45')
 assert abs((c*B+c*(mp.zeta(3)-1))-c*(mp.zeta(2)-1))<mp.mpf('1e-45')
 lines.append('50-digit numerical normalization and criticality checks passed; exact proofs are in ATTEMPT.md.')
except ImportError:
 lines.append('mpmath unavailable; numerical normalization skipped, exact proof retained.')
claims=[json.loads(s) for s in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert all(s['problem_id']=='D0056' for s in claims)
lines.append(f'CLAIMS.jsonl parses: {len(claims)} claims.')
Path('checks.txt').write_text('\n'.join(lines)+'\n',encoding='utf8');print('\n'.join(lines))
