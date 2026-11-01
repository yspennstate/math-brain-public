import json
from pathlib import Path

root = Path(__file__).parent
receipts = [json.loads(line) for line in (root/'COMMUNICATIONS.jsonl').read_text(encoding='utf-8').splitlines() if line]
review = next((row for row in reversed(receipts) if row['to']=='w365' and row['topic']=='P0104-referee-packet'), None)
if not review:
    raise SystemExit('No referee submission receipt; keep WORKING.')
measurement = json.loads((root/'MEASUREMENTS.json').read_text(encoding='utf-8'))
bundle = json.loads((root/'BUNDLE_VALIDATION.json').read_text(encoding='utf-8'))
assert measurement['status']=='PASS' and bundle['status']=='STRUCTURAL_PASS'
assert Path(bundle['bundle_path']).is_file()
for name in ['SOURCE_STATUS.json','BUNDLE_VALIDATION.json']:
    path = root/name
    obj = json.loads(path.read_text(encoding='utf-8'))
    obj['states']['submitted_for_review'] = True
    obj['states']['independently_reviewed'] = False
    obj['states']['ingested'] = False
    obj['states']['retrievable'] = False
    obj['referee_submission_receipt'] = review['receipt']
    path.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
prior_path = root/'PRIOR_RECORDS.json'
prior = json.loads(prior_path.read_text(encoding='utf-8'))
prior['historical_path_exists'] = {path:Path(path).exists() for path in prior['files']}
prior_path.write_text(json.dumps(prior,indent=2)+'\n',encoding='utf-8')
claims = [json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
assert len(claims)==8
assert all(row['review_state']=='pending' for row in claims)
assert next(row for row in claims if row['claim_id']=='w363-C007')['status']=='conjecture'
status = root/'STATUS.md'
old = status.read_text(encoding='utf-8').splitlines()
old[0] = 'STATE: NEEDS_REVIEW'
old[1] = 'NEXT: w365 audit C004-C006; next proof step bound F_n(k) for k<=n^(1/3), beginning with pq sum_e(E delta_e T_n)^2.'
old += ['2026-10-10: Review packet submitted to w365; 8 saved claim rows and 5 draft concept cards with 4 supported relations. G1 unproved; no theorem promotion, ingestion or retrievability claim.']
status.write_text('\n'.join(old)+'\n',encoding='utf-8')
result = {'status':'NEEDS_REVIEW','claim_rows':len(claims),'draft_cards':bundle['entries'],
          'supported_relations':bundle['relations'],'review_message':review['receipt']['message_id'],
          'bundle_path':bundle['bundle_path'],'remaining_gap':'G1: E_nu_n[1/K]=n^(-1/3+o(1))',
          'ingested':False,'retrievable':False}
(root/'FINAL_CHECKPOINT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
