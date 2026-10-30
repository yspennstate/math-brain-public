from pathlib import Path
from fractions import Fraction as Q
import sys,time,json
R=Path(__file__).resolve().parents[1];sys.dont_write_bytecode=True
sys.path.insert(0,str(R.parents[1]/'runs'/'20261014T094139Z-fleet05-A091-composition-referee'/'code'))
import check as a
import exact as e
start=time.perf_counter();cases=0
for mask in range(256):
 g=e.tab(mask,3);P=a.squares(g);I=sum(Q(s.bit_count())*q for s,q in enumerate(P))
 for i in range(3):
  assert time.perf_counter()-start<55
  kids=[a.cut(g,i,b) for b in (0,1)]
  p=sum(q for s,q in enumerate(P) if s>>i&1)
  h=tuple(int(u!=v) for u,v in zip(*kids));Ih=sum(Q(sum(h[x]!=h[x^(1<<j)] for x in range(4)),4) for j in range(2))
  e.check(Ih<=2*(I-p),True)
  e.nonnegative(e.add((1,a.const(Ih)),(-2,a.eta(p))))
  e.nonnegative(e.add((1,a.const(I-p)),(-1,a.eta(p))))
  D=e.add((1,e.entropy(P)),*[(-Q(1,2),e.entropy(a.squares(k))) for k in kids])
  e.nonnegative(e.add((1,a.const(Q(9,2)*I)),(-1,D)))
  e.check(sum(e.inf(a.squares(k)) for k in kids)/2,I-p)
  cases+=1
out={'status':'PASS','cases':cases,'assertions':e.COUNT,'runtime_seconds':time.perf_counter()-start,'scope':'all256 three-bit functions x3 queries; universal scope by independent ONESHOT_PROOF.md induction'}
(R/'out'/'oneshot.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
