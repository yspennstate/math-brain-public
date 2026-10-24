"""Consume w346 verdicts without re-auditing them or modifying their files."""
import json
from pathlib import Path

root=Path(__file__).resolve().parent
source=Path('~/brain_workers/w346/audits/w342.jsonl')
verdicts=[json.loads(s) for s in source.read_text(encoding='utf-8-sig').splitlines() if s.strip()]
by_id={v['row_id']:v for v in verdicts if v.get('row_id')}
rows=[json.loads(s) for s in (root/'results.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
for row in rows:
    verdict=by_id.get(row['row_id'])
    if verdict:
        row['audit_status']=verdict['verdict']
        row['independent_auditor']='w346'
        row['audit_verdict_file']=str(source)
        row['accepted_scope_or_reason']=verdict.get('why','')
(root/'results.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows),encoding='utf-8')
receipt={'auditor':'w346','verdict_file':str(source),'verdicts':verdicts,'kept_row_ids':[row['row_id'] for row in rows if row.get('audit_status')=='KEEP'],'full_bundle_approvals':0}
(root/'AUDIT_RECEIVED.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sign=next(row for row in rows if row['row_id']=='S1.w342.001')
(root/'proofs/P0289_sign_criterion.md').write_text('P0289 second-order sign criterion\n\nAuditor: w346; KEEP S1.w342.001. This certifies the coefficient criterion only, not full-workload ordering.\n\n'+sign['statement']+'\n\nProof: '+sign['proof']+'\n',encoding='utf-8')
print(json.dumps({'independent_keeps':len(receipt['kept_row_ids']),'kept_row_ids':receipt['kept_row_ids'],'full_bundle_approvals':0}))
