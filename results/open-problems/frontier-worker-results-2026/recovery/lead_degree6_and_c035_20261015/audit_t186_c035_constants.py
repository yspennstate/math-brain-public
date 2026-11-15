from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
import json,hashlib
H=Path(__file__).resolve().parent;W=Path('~/brain_workers/w674/T186')
out=[]
for c in [11,12]:
 p=W/f'logs/t3_cascade_rate_k4_c{c}.json';r=json.loads(p.read_bytes());D=int(r['scale']);assert D==10**60
 h=[F(int(x),D) for x in r['h_scaled']];U=[[F(int(x[1]),D) for x in row] for row in r['matrix']]
 assert len(h)==len(U)==24 and all(len(row)==24 for row in U)
 assert min(h)>=1 and min(x for row in U for x in row)>=0
 drift=[h[i]-sum(h[j]*U[j][i] for j in range(24)) for i in range(24)];assert min(drift)>=1
 Hbound=int(r['H']);q=F(int(r['p_numerator']),int(r['p_denominator']));assert max(h)<=Hbound
 eta=q*q/(108*Hbound*(c*c+c));target={11:F(1,1360313450496),12:F(1,6289241407488)}[c];assert eta==target
 # Re-derive uniform row bound of the tilted moment matrix.
 perturbation=eta*54*Hbound*(c*c+c);assert perturbation==q*q/2
 assert 1+3*eta*c/q<=2 and 0<eta<=1
 contraction=1-F(1,2*Hbound);moment=12*Hbound**2
 assert moment=={11:99372,12:95052}[c]
 assert 6*Hbound+contraction*moment==moment
 A=(3*Hbound**2/q)*(9*c*c+9*c+1)*3**(2*c)
 assert A==int(r['A']) and 2*A==int(r['theta_denominator']) and 12*A==int(r['gamma_denominator'])
 out.append({'c':c,'H':Hbound,'q':str(q),'eta':str(eta),'moment':moment,'contraction':str(contraction),'drift_rows':24,'minimum_drift':str(min(drift)),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
p=W/'proofs/C035_quantitative_reverse_ancestry_moment.md';assert hashlib.sha256(p.read_bytes()).hexdigest()=='5756545619823225aa5702f4aa25880187d7bc8da056e58595d36c66d67c778b'
r={'at':datetime.now().astimezone().isoformat(),'status':'PASS conditional exact witness/constant audit; matrix entry enclosures and tree assumptions retained premises, no finite transfer','proof_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'cases':out,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(H/'T186_C035_CONSTANT_AUDIT_RECEIPT.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in r.items() if k!='cases'}));print([(x['c'],x['eta'],x['moment']) for x in out])
