"""Preserve v1; apply peer scope/namespace FIX and publish a concept-only v2."""
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
old_hashes = json.loads((ROOT / 'FILE_HASHES.json').read_text(encoding='utf-8'))
archive = ROOT / 'archive' / 'v1'
archive.mkdir(parents=True, exist_ok=True)
for name in list(old_hashes['files']) + ['FILE_HASHES.json','FINAL_VALIDATION.json','HANDOFF_RECEIPTS.json']:
    src, dest = ROOT / name, archive / name
    dest.parent.mkdir(parents=True,exist_ok=True)
    if not dest.exists():
        shutil.copyfile(src,dest)
    else:
        assert dest.read_bytes()==src.read_bytes(), 'Do not overwrite v1 evidence'

attempt = (ROOT / 'ATTEMPT.md').read_text(encoding='utf-8')
old = 'A volume limit at each positive eta is necessary before using this infinite-volume criterion.'
new = 'A fixed finite box cannot supply (LG). A valid infinite-volume proof must justify either successive limits or a joint volume/regulator scheme with its own uniform bound and convergence control.'
assert old in attempt
attempt = attempt.replace(old,new)
attempt = attempt.replace('Any proposed certificate must control that exact quantity after the infinite-volume limit.', 'Any proposed certificate must control the exact infinite-volume quantity through a justified transfer, which may use successive limits or a controlled joint volume/regulator scheme.')
attempt = attempt.replace('Author w480, 2026-10-10. Author proof only; independent review pending. No parent-problem solved claim. Current openness UNKNOWN.', 'Author w480, 2026-10-10, corrected revision 2. Scoped mathematical KEEP received from w481/w482; limit-scope FIX applied and served-model/provenance gates remain open. No parent-problem solved claim. Current openness UNKNOWN.')
attempt += '\n## Peer correction in revision 2\n\nThe L3 finite-volume divergence theorem is unchanged. Its original final sentence overstated what the theorem implies about limit order. w481 supplied a separate joint-limit witness in JOINT_LIMIT_COUNTEREXAMPLE.md: finite self-adjoint cavities at eta_N=N^(-1/4) can have a bounded logarithmic functional while every fixed-size cavity diverges as eta->0. That witness requires its own w482 review; it is not an Anderson proof. The corrected conclusion excludes fixed-size certification, while allowing a controlled joint scheme. w482 separately requested placement in the existing probability.random-matrices namespace. Both fixes are applied in this revision; they do not close LG or GOE.\n'
(ROOT / 'ATTEMPT.md').write_text(attempt,encoding='utf-8')
statement = (ROOT / 'STATEMENT_FOR_ADVERSARY.md').read_text(encoding='utf-8')
statement = statement.replace('A finite box at fixed size cannot satisfy (LG) uniformly as eta->0; do not interchange these limits.', 'A finite box at fixed size cannot satisfy (LG) uniformly as eta->0. A controlled joint volume/regulator scheme remains possible but needs its own uniform estimate and convergence argument.')
(ROOT / 'STATEMENT_FOR_ADVERSARY.md').write_text(statement,encoding='utf-8')

sections = {}
for block in attempt.split('\n## ')[1:]:
    heading, _, body = block.partition('\n')
    sections[heading.split(':')[0]] = '## '+heading+'\n'+body.strip()
claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
for row in claims:
    short = row['claim_id'].rsplit('-',1)[-1]
    if short in ['L1','L2','L3','C1','L4','L5']:
        row['proof_or_counterexample'] = sections[short]
        row['independent_reviewer'] = 'w482 scoped mathematical KEEP; corrected-scope recheck/provenance gate pending'
        row['scoped_math_reviewers'] = ['w481','w482']
        row['status_detail'] = 'Author proof with scoped mathematical KEEP; not an admitted independently checked proof without served-model/provenance evidence.'
        row['revision'] = '2026-10-10-v2'
        row['source']['revision'] = '2026-10-10-author-draft-v2'
claims.append({
    'claim_id':'C0056-W480-S2','kind':'proof_scope_correction',
    'statement':'The finite-size logarithmic divergence theorem excludes a fixed-size eta-uniform certificate but does not force successive volume and regulator limits. A coupled limiting scheme is admissible only with its own uniform estimate and convergence control. The theorem itself is unchanged.',
    'assumptions':['Do not promote the separate joint-limit witness to an Anderson theorem.'],
    'source':{'path':'~/brain_workers/w481/VERDICT_W480.md','witness_path':'~/brain_workers/w481/JOINT_LIMIT_COUNTEREXAMPLE.md','corrected_author_path':str(ROOT / 'ATTEMPT.md')},
    'proof_or_counterexample':'The original necessity claim was stronger than the fixed-N conclusion. The author withdraws that sentence; w481 supplied a distinct joint-limit witness for independent w482 review.',
    'independent_reviewer':'w482; witness/correction recheck requested',
    'remaining_gap':'No uniform fixed-lambda infinite-volume LG estimate or GOE result follows from this scope correction.',
    'status':'sketch','parent_problem_solved':False,'supersedes_scope_sentence_in':'C0056-W480-L3-v1',
})
assert len(claims)==11 and len({r['claim_id'] for r in claims})==11
(ROOT / 'CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in claims),encoding='utf-8')

bundle = json.loads((ROOT / 'bundle_001.json').read_text(encoding='utf-8'))
bundle['bundle_slug'] = 'probability300-c0056-log-cavity-w480-002'
for entry in bundle['entries']:
    entry['namespace'] = 'probability.random-matrices'
    entry['source']['revision'] = '2026-10-10-author-draft-v2-scope-fixed'
    entry['statement'] = entry['statement'].replace('UNREVIEWED CAMPAIGN DRAFT; author proof saved, independent review pending.', 'CAMPAIGN DRAFT; scoped mathematical KEEP received; corrected-scope and served-model/provenance rechecks pending.')
    if entry['key']=='l3':
        entry['statement'] += ' This excludes fixed-size certification; it does not rule out a controlled joint volume/regulator scheme.'
    assert entry['kind']=='concept' and entry['proof_text'] is None
new_local = ROOT / 'bundle_002.json'
new_local.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
inbox = Path('~/math-brain-inbox/w480')
dest, part = inbox / 'bundle_002.json', inbox / 'bundle_002.part'
assert not dest.exists(), 'Never overwrite a prior corrected draft'
part.write_bytes(new_local.read_bytes())
part.rename(dest)

entries = {e['key']:e for e in bundle['entries']}
relations = bundle['relations']
support = [dict(r,from_statement=entries[r['from_key']]['statement'],to_statement=entries[r['to_key']]['statement'],status='DRAFT v2; scoped KEEP, provenance/recheck pending') for r in relations]
(ROOT / 'RELATION_SUPPORT.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in support),encoding='utf-8')
(ROOT / 'BUNDLE_VALIDATION.json').write_text(json.dumps({'status':'LOCAL_SCHEMA_PASS','active_bundle':'bundle_002.json','superseded_bundle':'bundle_001.json (preserved; HOLD sent to coordinator)','entries':7,'relations':6,'all_entries_concept':True,'namespace':'probability.random-matrices','namespace_basis':'Existing namespace requested by w482 after live read-only store probe','depends_on_acyclic':True,'scoped_math_keep_received':True,'full_review_gate_passed':False,'integration_run':False,'ingested':False,'retrievable':False},indent=2)+'\n',encoding='utf-8')

status = json.loads((ROOT / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
status['review_state'] = 'Scoped mathematical KEEP from w481/w482; two FIXes applied in v2, recheck and served-model/provenance gates pending'
status['bundle_state'] = {'prepared':True,'submitted':True,'reviewed':False,'scoped_mathematical_keep_received':True,'corrected_scope_recheck_pending':True,'ingested':False,'retrievable':False,'active_bundle':str(dest),'superseded_bundle':'bundle_001.json (HOLD, preserved)'}
status['peer_verdict_sources'] = [{'agent':'w481','path':'~/brain_workers/w481/VERDICT_W480.md','served_model':'UNAVAILABLE'},{'agent':'w482','path':'~/brain_workers/w482/REVIEW_PACKET.md','served_model':'UNAVAILABLE'}]
(ROOT / 'SOURCE_STATUS.json').write_text(json.dumps(status,indent=2)+'\n',encoding='utf-8')

packet = (ROOT / 'REVIEW_PACKET.md').read_text(encoding='utf-8')
packet = packet.replace('~/math-brain-inbox/w480/bundle_001.json','~/math-brain-inbox/w480/bundle_002.json')
packet += '\nRevision 2: w481/w482 scoped KEEP received. The false necessity of successive limits is withdrawn; a controlled joint limit may be used with its own estimates and convergence proof. Namespace is now existing probability.random-matrices. Old bundle_001 is preserved but superseded and on HOLD; coordinator received the hold notice. Please recheck the corrected sentence and bundle placement; the mathematics, LG gap, scalar measurements, and no-parent/no-GOE scope are unchanged. Serve-model evidence remains unavailable, so no admission or theorem promotion is claimed. v1 proof/artifact evidence is preserved in archive/v1/.\n'
(ROOT / 'REVIEW_PACKET.md').write_text(packet,encoding='utf-8')
report = (ROOT / 'REPORT.md').read_text(encoding='utf-8').replace('bundle_001.json','bundle_002.json')
report += '\nRevision 2 fixes: scoped mathematical KEEP received from w481/w482. Corrected an overstatement after L3: fixed-size divergence does not preclude a controlled joint limit. Changed the draft to existing probability.random-matrices per w482. Current CLAIMS contains 11 rows; v1 evidence and old draft are preserved, with bundle_001 on HOLD. Numerical lemmas/assumptions are unchanged, so the already-passing scalar checks were not repeated. Recheck/provenance and all live integration gates remain open.\n'
(ROOT / 'REPORT.md').write_text(report,encoding='utf-8')
(ROOT / 'REVIEW_FIXES.md').write_text('Applied w481 FIX: withdrew necessity of successive limits; retained the fixed-size divergence theorem and allowed controlled joint schemes.\nApplied w482 FIX: seven concept drafts now use probability.random-matrices.\nPreserved archive/v1 and old draft; sent HOLD for bundle_001.\nNo new Anderson, LG, GOE, served-model or formal-check claim.\nNEXT: w482 rechecks corrected scope/placement; LG low-b tail below the perturbative cutoff is still unproved.\n',encoding='utf-8')
print(json.dumps({'revision':2,'claims':11,'concept_entries':7,'relations':6,'namespace':'probability.random-matrices','active_bundle':str(dest),'v1_preserved':True,'store_written':False}))
