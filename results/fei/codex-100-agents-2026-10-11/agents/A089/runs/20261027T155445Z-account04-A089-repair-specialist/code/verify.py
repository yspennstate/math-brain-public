"""Independent original-edge certificate: integer characters, no prior imports."""
from pathlib import Path
from fractions import Fraction as Q
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();rows=[]
for mask in range(16):
 g=[1 if mask>>x&1 else -1 for x in range(4)]
 Ig=Q(sum(g[x]!=g[x^(1<<i)] for x in range(4) for i in range(2)),4)
 D0=sum(g[0]!=g[1<<i] for i in range(2));D1=sum(g[1<<j]!=g[(1<<i)|(1<<j)] for i in range(2) for j in range(2) if i!=j)
 for k in [2,3]:
  n=k+2;N=1<<n;t=[g[x&3]*(-1 if x.bit_count()<=1 else 1) for x in range(N)]
  W=[sum(t[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
  assert sum(w*w for w in W)==N*N
  Ifourier=Q(sum(s.bit_count()*w*w for s,w in enumerate(W)),N*N)
  Iedges=Q(sum(t[x]!=t[x^(1<<i)] for x in range(N) for i in range(n)),N)
  formula=Ig+Q(n*(n-1)-2*k*D0-2*D1,1<<(n-1))
  assert Ifourier==Iedges==formula
  rows.append({'seed_mask':mask,'k':k,'I':str(Iedges),'D0':D0,'D1':D1})
out={'status':'PASS','cases':32,'method':'integer direct Walsh characters vs directed edges vs original cancellation formula; no prior helper','runtime_seconds':time.perf_counter()-start,'rows':rows}
(R/'out/INDEPENDENT_ORIGINAL_OWNER.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
