from pathlib import Path
from fractions import Fraction as F
import json,hashlib
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out'
spec={'helper':'A100-A008-auxiliary-factor-v1','family':'forced e-child assignment with e+1 width-two singleton draws and both endpoint orders',
      'domain':'e=0..4; symbolic multiplicative ratio proved for every e>=0','case_count':5,'symmetry':'none',
      'arithmetic':'exact Fraction and integer powers; code-cost difference is exact log2(2^(e+1))',
      'memory_estimate_MB':5,'max_runtime_seconds':10,'search':False}
(RUN/'AUXILIARY_CHECK_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
t_single=F(1,2)*F(1,2); assert t_single==F(1,4)
rows=[]
for e in range(5):
    right=t_single**(e+1); wrong=F(1,2)**(e+1)
    assert wrong/right==2**(e+1)
    rows.append({'e':e,'correct_subset_product':str(right),'wrong_subset_product':str(wrong),
                 'overstated_mass_factor':2**(e+1),'understated_full_code_cost_bits':e+1})
(OUT/'A008_AUXILIARY_FACTOR_CHECK.json').write_text(json.dumps({'status':'PASS','scope':'Formal A008 operator theorem retains t and is unaffected; complete evaluations using t=1/2 must be recomputed.','rows':rows},indent=2)+'\n',encoding='utf-8')
PREV=RUN.parent/'20261014T010218Z-fleet05-A100-release-and-continuation-ledger'
receipt=json.loads((PREV/'out/PERSISTENCE_RECEIPTS.json').read_text(encoding='utf-8'))
readback=[]
for x in receipt['files']:
    p=Path(x['path'])
    if not p.is_relative_to(PREV): continue # rolling files are intentionally mutable
    b=p.read_bytes(); actual=hashlib.sha256(b).hexdigest()
    readback.append({'path':str(p),'bytes':len(b),'sha256':actual,'matches_prior_receipt':len(b)==x['bytes'] and actual==x['sha256']})
assert all(x['matches_prior_receipt'] for x in readback)
(OUT/'PREVIOUS_STAGE_LOCAL_READBACK.json').write_text(json.dumps({'status':'PASS','prior_run':str(PREV),'matched_files':len(readback),'files':readback,
    'scope':'Fresh local readback of previous immutable private run; rolling files excluded; no current GitHub/private remote or public release verification.'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'auxiliary_factor_cases':5,'prior_immutable_files_read_back':len(readback),'status':'PASS'},indent=2),flush=True)
