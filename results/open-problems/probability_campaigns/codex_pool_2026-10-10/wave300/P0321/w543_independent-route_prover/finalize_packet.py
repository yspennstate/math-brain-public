"""Record the measured submitted packet and leave supervisor review state."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
v=json.loads((ROOT/'VALIDATION.json').read_text(encoding='utf-8'))
p=json.loads((ROOT/'PUBLICATION_STATUS.json').read_text(encoding='utf-8'))
a=json.loads((ROOT/'AUDIT_RECEIPTS.json').read_text(encoding='utf-8'))
n=json.loads((ROOT/'NUMERICAL_CHECKS.json').read_text(encoding='utf-8'))
assert v['checks_failed']==0 and v['independently_checked_auxiliary_claims']==4
assert p['submitted']['state']=='submitted' and not p['live_store_mutated_by_worker']
assert a['author_proof_matches_audited_snapshot_byte_for_byte'] and not a['store_or_source_admission']
submitted=Path(p['bundle_path'])
assert submitted.read_bytes()==(ROOT/'bundle_001.json').read_bytes()
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
report=report.replace('the first measured run took 0.00521 seconds','the final check body took %.6f seconds'%v['elapsed_seconds'])
report=report.replace('Brain submission: the six cards remain','Brain submission: `%s` was submitted at %s with exact readback; the six cards remain'%(p['bundle_path'],p['submitted']['timestamp_utc']))
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
source=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source['auxiliary_audit_status']={'H1_H4':'scoped KEEP by w544 and w545','receipt':'AUDIT_RECEIPTS.json','different_login_provenance':'UNVERIFIED','not_a_P0321_solution':True}
source['population_read_only_query']={'receipt':'population_store_p0321.json','matched_nodes':2,'query_only':True}
source['canonical_lookup_limit']='The named math-research-brain checkout had no live-store locator in the bounded README/store/local reads; no separate current P0321 solution record was recovered. This does not certify absence of an owner solution.'
(ROOT/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2),encoding='utf-8')
previous=(ROOT/'STATUS.md').read_text(encoding='utf-8').splitlines()
log='\n'.join(line for line in previous[2:] if not line.startswith('NEXT:')).strip()
status='STATE: NEEDS_REVIEW\nNEXT: Coordinator checks admission/login provenance for bundle_001; next proof step is a defect-aware microscopic angle approximation with error o(C6(r)).\n\n'+log+'\n\n2026-10-10: Delivered complete packet to w545 (msg-cbf4132688); H1-H4 scoped KEEP by w544 and w545, audited proof byte match true. Submitted six definition/concept drafts and six typed relations to '+p['bundle_path']+' with exact readback. Final integrity checks: '+str(v['checks_passed'])+' pass, zero fail. Numerical checker: '+n['status']+', zero cases. Full P0321 remains unresolved, current openness UNKNOWN; no cross-account admission, ingestion or retrieval claim.\n'
(ROOT/'STATUS.md').write_text(status,encoding='utf-8')
print(json.dumps({'state':'NEEDS_REVIEW','bundle_path':p['bundle_path'],'checks_passed':v['checks_passed'],
                  'auxiliary_claims_kept_by_two_workers':4,'numerical_status':n['status'],
                  'full_P0321_solution':False,'ingested':p['ingested']['state'],'retrievable':p['retrievable']['state']},indent=2))
