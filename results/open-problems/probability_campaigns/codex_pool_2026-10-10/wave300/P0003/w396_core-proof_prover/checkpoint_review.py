from pathlib import Path
import ast
import json
import re
import time

root=Path(__file__).resolve().parent
state=json.loads((root/'DRAFT_STATE.json').read_text(encoding='utf-8'))
if not state['submitted']:raise ValueError('Draft was not submitted')
handoff=json.loads((root/'peer_review_receipt.json').read_text(encoding='utf-8'))
review=next(r for r in handoff if r['recipient']=='w398' and r['kind']=='review')
if review['returncode']!=0:raise ValueError('Review handoff failed')
message=review.get('result',{}).get('message_id')
if not message:raise ValueError('Missing mathematical-review request receipt')
bundle=json.loads(Path(state['draft_path']).read_text(encoding='utf-8'))
claims=[json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
if len({c['id'] for c in claims})!=len(claims):raise ValueError('Duplicate claim ids')
allowed_status={'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
for claim in claims:
    if claim['status'] not in allowed_status:raise ValueError(claim['status'])
    if claim['status']=='independently checked proof':raise ValueError('No independent proof verdict received')
    claim['review_state']='requested; no mathematical verdict received'
    claim['independent_reviewer']='w398 (assigned; request '+message+'; no verdict received)'
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')
keys={e['key'] for e in bundle['entries']}
if len(keys)!=len(bundle['entries']):raise ValueError('Duplicate draft keys')
dependencies={k:[] for k in keys}
for rel in bundle['relations']:
    if rel['from_key'] not in keys or rel['to_key'] not in keys:raise ValueError('Invalid relation endpoint')
    if rel['kind']=='depends_on':dependencies[rel['from_key']].append(rel['to_key'])
def visit(key,trail):
    if key in trail:raise ValueError('Cyclic dependencies')
    for child in dependencies[key]:visit(child,trail|{key})
for key in keys:visit(key,set())
compiled=[]
for path in sorted(root.glob('*.py')):
    ast.parse(path.read_text(encoding='utf-8'),filename=str(path))
    compiled.append(path.name)
finite=json.loads((root/'FINITE_CHECKS.json').read_text(encoding='utf-8'))
measure=json.loads((root/'measurements.json').read_text(encoding='utf-8'))
measure['numerical_regression']=finite
measure['claim_rows']=len(claims)
measure['review_request_message_id']=message
baseline=measure['canonical_read_only_baseline']
if baseline['matched_proposed_logicals'] is None:
    baseline['limitation']='A matching table/logical-id column was not resolved; no baseline node-count or recall-effect estimate is claimed.'
receipt={'status':'PASS_ARTIFACT_VALIDATION_ONLY','checked_at_unix':time.time(),'claim_rows':len(claims),'draft_entries':len(bundle['entries']),'relations':len(bundle['relations']),'acyclic_dependencies':True,'python_sources_ast_checked':compiled,'mathematical_regression_status':finite['status'],'mathematical_assertions_run':finite.get('assertions',0),'mathematical_independent_reviews':0,'formal_theorems_checked':0,'submitted':True,'review_requested':True,'review_request_message_id':message,'ingested':False,'retrievable':False}
(root/'ARTIFACT_VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
(root/'measurements.json').write_text(json.dumps(measure,indent=2)+'\n',encoding='utf-8')
source=json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source.update({'review_requested':True,'review_request_message_id':message,'reviewed':False,'ingested':False,'retrievable':False})
(root/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2)+'\n',encoding='utf-8')
review_path=root/'review_packet/REVIEW.md'
text=review_path.read_text(encoding='utf-8')
text=re.sub(r'Current check status: [^;\n]+; assertions run: \d+\.', 'Current check status: '+finite['status']+'; assertions run: '+str(finite.get('assertions',0))+'.',text)
text=text.replace('\nNEXT: Return a mathematical', '\nSubmission receipt: '+state['submitted_path']+'; seven entries and seven relations. Mathematical review requested from w398 as '+message+'. No verdict received; ingestion and retrieval remain unverified.\n\nNEXT: Return a mathematical')
review_path.write_text(text,encoding='utf-8')
report=root/'REPORT.md'
text=report.read_text(encoding='utf-8')
text=re.sub(r'Finite regression status is [^ ]+ with \d+ assertions;', 'Finite regression status is '+finite['status']+' with '+str(finite.get('assertions',0))+' assertions;',text)
text=text.replace('\nApply:', '\nSubmitted: '+state['submitted_path']+'. w398 received the complete packet under mesh request '+message+'. There are ten claim rows, seven draft entries and seven relations. Ingestion and retrieval are not verified.\n\nApply:')
report.write_text(text,encoding='utf-8')
status_path=root/'STATUS.md'
status=status_path.read_text(encoding='utf-8')
status=re.sub(r'^STATE: [^\n]+','STATE: NEEDS_REVIEW',status,count=1)
status=re.sub(r'^NEXT: [^\n]+',"NEXT: w398 audit L0', L1-L3 and (U); the next proof step is a mutually avoiding prefix/suffix estimate for H_disk.",status,count=1,flags=re.MULTILINE)
status+='\n2026-10-10: Completed packet: ten valid claim rows, seven draft cards, seven supported relations, AST checks and acyclic relation validation. Inbox draft submitted after exclusive mesh claim. w398 review request '+message+' delivered; w397 has the corrected packet. Latest numerical status '+finite['status']+' ('+str(finite.get('assertions',0))+' assertions). Full P0003, H_disk and further identification/tightness inputs remain unproved. No live store integration or retrieval-effect claim.\n'
status_path.write_text(status,encoding='utf-8')
print(json.dumps(receipt),flush=True)
