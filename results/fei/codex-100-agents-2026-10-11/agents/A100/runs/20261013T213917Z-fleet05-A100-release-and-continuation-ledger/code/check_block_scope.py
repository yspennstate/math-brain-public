from pathlib import Path
from fractions import Fraction as F
import json, hashlib
RUN = Path(__file__).resolve().parents[1]
OUT = RUN / 'out'
# Frozen analytic certificate, no cube enumeration or dimension escalation.
spec = {'helper':'A100-block-scope-v1','family':'Boolean point defect 1-2*indicator(all plus)',
        'domain':'n=128; one physical full-block query','case_count':1,'symmetry':'one named vertex',
        'arithmetic':'exact Fraction; three positive terms of rational atanh lower bound for ln2; e>8/3',
        'memory_estimate_MB':5,'max_runtime_seconds':10,'search':False}
(RUN/'BLOCK_SCOPE_FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
n=128
ln2_lower=2*sum((F(1,3)**(2*j+1)/F(2*j+1) for j in range(3)),F(0))
rate_lower=4*F(n-1,n)*(1-F(1,2**n))*ln2_lower
gap=rate_lower-F(11,4)
assert gap>0
pack=lambda x: {'numerator':str(x.numerator),'denominator':str(x.denominator)}
record={'n':n,'actual_boolean_family':spec['family'],'influence_exact':pack(F(2*n,2**n)),
        'off_empty_mass_each':pack(F(4,2**(2*n))),'off_empty_count':str(2**n-1),
        'channel_cost':0,'rate_formula':'4*(n-1)/n*(1-2^-n)*ln(2)',
        'ln2_lower':pack(ln2_lower),'rate_lower':pack(rate_lower),
        'claimed_rate_strict_upper':'11/4, since e>8/3','positive_gap':pack(gap),
        'assertions_passed':1,'failures':0,'scope':'Refutes unrestricted block-tree budget only; singleton-query scope and block identity survive.'}
(OUT/'A066_BLOCK_SCOPE_INDEPENDENT.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
audit=Path(r'~\brain_workers\FEI100_20261011\agents\A088\runs\20261012T024518Z-fleet05-A088-booleanity-referee\AUDIT.md')
receipts=json.loads((OUT/'SOURCE_RECEIPTS.json').read_text(encoding='utf-8'))
if not any(x['path']==str(audit) for x in receipts['files']):
    b=audit.read_bytes(); receipts['files'].append({'path':str(audit),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
    (OUT/'SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
print('PASS: one exact n=128 block-scope countercertificate; singleton scope preserved.')
