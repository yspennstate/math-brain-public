"""Standalone file-consuming verifier: no import of the producer or Walsh helper."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib
B=Path(__file__).resolve().parents[1]
raw=(B/'out/FACTOR_CERTIFICATE.json').read_bytes();cert=json.loads(raw)
assert 3**12>2**19 and cert['coefficient']=='7/4'
seen=set();counts=Counter();minslack=None
for row in cert['rows']:
 n=row['n'];v=row['values'];size=2**n
 assert 0<=n<=3 and len(v)==size and all(x in (-1,1) for x in v)
 truthcode=sum((x==1)<<i for i,x in enumerate(v))
 assert (n,truthcode) not in seen;seen.add((n,truthcode));counts[n]+=1
 ps=[]
 for mask in range(size):
  coefficient=F(sum(value*(-1)**((x&mask).bit_count()) for x,value in enumerate(v)),size)
  ps.append(coefficient**2)
 assert sum(ps)==1 and ps==list(map(F,row['spectrum']))
 # Conditional on a fixed coordinate, count undirected disagreeing edges.
 influence=sum((F(sum(v[x]!=v[x|(1<<i)] for x in range(size) if not x&(1<<i)),size//2) for i in range(n)),F(0))
 hup=F(0)
 for p in ps:
  if not p:continue
  if p==F(9,16):hup+=p*(4-2*F(19,12))
  else:
   exponent=next(k for k in (0,2,4) if p==F(1,2**k))
   hup+=p*exponent
 variance=1-ps[0];slack=4*influence-hup-F(7,4)*variance
 assert influence==F(row['I']) and variance==F(row['variance'])
 assert hup==F(row['H_upper']) and slack==F(row['slack']) and slack>=0
 if variance:minslack=slack if minslack is None else min(minslack,slack)
assert seen=={(n,code) for n in range(4) for code in range(2**(2**n))}
result={'status':'PASS','read_artifact':'out/FACTOR_CERTIFICATE.json','sha256':hashlib.sha256(raw).hexdigest(),'recomputed_rows':len(seen),'coverage_by_n':dict(counts),'minimum_nonconstant_rational_slack':str(minslack),'independence':'Direct character sums, undirected edges, independently evaluated entropy upper bound, exhaustive-domain identity; no producer/helper imports'}
(B/'out/CERTIFICATE_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(result))
