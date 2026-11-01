from fractions import Fraction as F
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();cases=checks=0
spec={'helper_version':'direct-source-v1','family':'all278 Boolean cores on0..3 data bits, both activation signs;556 selectors on at most4 physical bits','case_count':556,'symmetry':'none','arithmetic':'integer character sums and all-vertex physical pivot counts; Fraction identities','memory_MB':80,'max_seconds':55}
(R/'out/SOURCE_AUDIT_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
def coefficients(vals):
 return [F(sum(v*(-1)**((x&t).bit_count()) for x,v in enumerate(vals)),len(vals)) for t in range(len(vals))]
def influence(vals,n):
 return F(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals)) for i in range(n)),len(vals))
for n in range(4):
 for table in range(1<<(1<<n)):
  core=[1 if table>>x&1 else -1 for x in range(1<<n)]
  a=coefficients(core);mu=a[0];ig=influence(core,n)
  for s in (-1,1):
   cases+=1
   # Bit0 is x; actual truth table, not a selector spectral formula.
   vals=[s if u%2==0 else core[u//2] for u in range(2*len(core))]
   actual=coefficients(vals)
   for t in range(len(core)):
    for c in range(2):
     assert actual[2*t+c]==F(s*(t==0)+(-1)**c*a[t],2)
     checks+=1
   assert influence(vals,n+1)==F(1-s*mu,2)+ig/2;checks+=1
   assert sum(v*v for v in actual)==1;checks+=1
   assert time.perf_counter()-start<55
out={'status':'PASS','cases':cases,'assertions':checks,'seconds':time.perf_counter()-start,'independence':'standalone direct truth-table Fourier coefficients and physical pivot counts; no imports from main checker'}
(R/'out/SOURCE_AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
