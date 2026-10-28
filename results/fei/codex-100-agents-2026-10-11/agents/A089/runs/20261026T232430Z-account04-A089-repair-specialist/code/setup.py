from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
for d in ['code','out']: (R/d).mkdir(exist_ok=True)
old=R.parent/'20261023T130925Z-account03-A089-repair-specialist/code'
for a,b in [('audit.py','prior.py'),('arithmetic.py','arithmetic.py')]:
 (R/'code'/b).write_bytes((old/a).read_bytes())
spec={'helper_version':'A089-owner-repair-v1; own prior.py/arithmetic.py preserved bytewise',
 'family':'all labelled 2-input outer gates, 2-bit first cores, 1-bit second cores; all Boolean tables n<=3 for owner checks; fixed parity/gated parity',
 'domain':'16*16*4 circuits; rates 0,1,2,3,10; signed rational transport grid',
 'case_count':{'circuits':1024,'query_rows':3072,'Boolean_tables_n0to3':278,'rates':5,'transport_grid':625},
 'symmetry':'none','arithmetic':'Fraction, exact prime-log vectors and directed 192-bit positive-series log enclosures; rational transport',
 'memory_estimate_mb':100,'maximum_runtime_seconds':55,'pilot_max_seconds':55,
 'no_automatic_dimension_escalation':True,'formal_check':'Mathlib exceeds 1.5GB job cap; only guarded core check if admitted'}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
(R.parents[1]/'STATUS.md').write_text('STATE: A089 stage21 ACTIVE: repairing own debit-sign proof using A080 counterexample; independently reconstructing A075 whole-row drift; FEI OPEN.\nNEXT: Exact signed-owner/whole-row checks, source-bound erratum and corrected conditional theorem; initial arbitrary-core influence funding remains unpaid.\n',encoding='utf-8')
print('frozen spec and checkpoint saved')
