"""Check completed local receipts and atomically checkpoint NEEDS_REVIEW."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parent
required=['SOURCE_STATUS.json','ATTEMPT.md','CLAIMS.jsonl','REVIEW.md','REPORT.md',
    'INDEPENDENT_OBSTRUCTION.md','CONDITIONAL_EXPONENTIAL_UPGRADE.md',
    'SMALL_DISPLACEMENT_OBSTRUCTION.md','review_packet.json','draft_bundle/bundle_001.json',
    'EDGE_SUPPORT.jsonl','BUNDLE_STATE.json','patches/01_recall_retracted_tag_override.diff',
    'PATCH_RECEIPT.json','DISPLAY_TEST_RECEIPT.json','PATCH_APPLICATION_RECEIPT.json','BUNDLE_VALIDATION_RECEIPT.json']
for name in required: assert (ROOT/name).is_file(), name
load=lambda name: json.loads((ROOT/name).read_text(encoding='utf-8'))
display=load('DISPLAY_TEST_RECEIPT.json')
application=load('PATCH_APPLICATION_RECEIPT.json')
validation=load('BUNDLE_VALIDATION_RECEIPT.json')
patch_receipt=load('PATCH_RECEIPT.json')
assert application['passed'] and validation['passed']
assert validation['claims']==7 and validation['entries']==6 and validation['relations']==5
assert display['observed_live_row']['stale_label_after']==0
assert display['observed_live_row']['unsafe_snippet_after']==0
assert display['synthetic_cases']==25 and display['active_or_unavailable_cases_unchanged']==12
assert hashlib.sha256((ROOT/'copies'/'brain.before.py').read_bytes()).hexdigest()==patch_receipt['baseline_sha256']
assert hashlib.sha256((ROOT/'copies'/'brain.after.py').read_bytes()).hexdigest()==application['applied_candidate_sha256']==patch_receipt['candidate_sha256']
assert b'\r\n' not in (ROOT/'patches'/'01_recall_retracted_tag_override.diff').read_bytes()
bundle_state=load('BUNDLE_STATE.json')
assert bundle_state['prepared'] and not any(bundle_state[field] for field in ('submitted','reviewed','ingested','retrievable'))
assert load('SOURCE_STATUS.json')['target_solved'] is False
packet=load('review_packet.json')
for name in ('check_patch_application.py','PATCH_APPLICATION_RECEIPT.json','BUNDLE_VALIDATION_RECEIPT.json'):
    if name not in packet['brain_change']: packet['brain_change'].append(name)
(ROOT/'review_packet.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
old='The structural bundle check passed in 0.009289 seconds with six entries, five exact-supported relations, one existing target resolved, and zero theorem nodes.'
new='The final structural bundle check passed with seven claim rows, six entries, five exact-supported relations, one existing target resolved, and zero theorem nodes. BUNDLE_VALIDATION_RECEIPT.json records its timing and limited scope.'
report=report.replace(old,new)
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
old_status=(ROOT/'STATUS.md').read_text(encoding='utf-8').splitlines()
log='\n'.join(line for line in old_status[2:] if line.strip())
next_step='NEXT: w383 verify the Uniform[1,2] adjacent-vertex obstruction against Auffinger--Damron (2.2), then check the conditional exponential upgrade; the engineering reviewer reproduces and applies the recall diff.'
status='STATE: NEEDS_REVIEW\n'+next_step+'\n\n'+log+'\n2026-10-10: RESOLVED: command-scoped core.autocrlf=false preserves the tested LF bytes; final isolated Git application passed byte for byte. Seven claim rows and all required artifacts checked. New mathematical deductions remain drafts. No live deployment, submission or ingestion.\n'
part=ROOT/'STATUS.part'
part.write_text(status,encoding='utf-8')
part.replace(ROOT/'STATUS.md')
result={'state':'NEEDS_REVIEW','claims':validation['claims'],'draft_entries':validation['entries'],
    'draft_relations':validation['relations'],'display_controls':display['synthetic_cases'],
    'patch_application_passed':True,'patch_application_seconds':application['elapsed_seconds'],
    'target_solved':False,'submitted':False,'deployed':False,'report':str(ROOT/'REPORT.md')}
(ROOT/'FINAL_CHECK_RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
