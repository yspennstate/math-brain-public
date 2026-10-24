"""Administrative final checkpoint; no mathematical experiment or live ingestion."""
from pathlib import Path
from datetime import datetime
import difflib
import json
import os
from prepare_review import validate

root=Path(__file__).parent
dest=Path('~/math-brain-inbox/w358/bundle_001.json')
old=(root/'bundle_001.json').read_text(encoding='utf-8')
assert dest.read_text(encoding='utf-8')==old, 'Preserve changed published draft'
bundle=json.loads(old)
for e in bundle['entries']:
    if e['key']=='strict-gap':
        e['statement']=e['statement'].replace('Let X~mu, G~N(0,I) independent,',
            'Let X~mu be centered, isotropic and log-concave, let G~N(0,I) be independent,',1)
    if e['key'] in {'parseval-route','appell-calibration'}:
        e['review_note']='w359 independent KEEP: coefficient norms in REVIEW_w358.md and exact Gram obstruction in REVIEW_w358_POSTERIOR.md; both under ~/brain_workers/w359/. Full tensor/general-law bridge not proved.'
receipt=validate(bundle,json.loads((root/'brain_target_lookup.json').read_text(encoding='utf-8')))
payload=json.dumps(bundle,indent=2,ensure_ascii=False)+'\n'
(root/'bundle_001.json').write_text(payload,encoding='utf-8')
part=dest.with_suffix('.part')
assert str(part.resolve()).lower().startswith(str(dest.parent.resolve()).lower()+'\\')
part.write_text(payload,encoding='utf-8')
assert dest.read_text(encoding='utf-8')==old
part.replace(dest)
assert dest.read_text(encoding='utf-8')==payload
(root/'STRUCTURAL_VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
target='math-brain-inbox/w358/bundle_001.json'
diff=''.join(difflib.unified_diff([],payload.splitlines(True),fromfile='a/'+target,tofile='b/'+target))
(root/'patches/01_p0017_boundary_bundle.diff').write_text(diff,encoding='utf-8')
key_map={e['key']:e for e in bundle['entries']}
edges=[json.loads(s) for s in (root/'EDGE_REVIEW.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
for r in edges:
    r['from_quote']=key_map[r['from_key']]['statement']
    if 'to_key' in r:r['to_quote']=key_map[r['to_key']]['statement']
(root/'EDGE_REVIEW.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in edges),encoding='utf-8')
claims=[json.loads(s) for s in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
for c in claims:
    if c['id']=='w358-S1.6':
        c['status']='independently checked proof'
        c['independent_reviewer']='w359 KEEP Gram obstruction; ~/brain_workers/w359/REVIEW_w358_POSTERIOR.md'
        c['remaining_gap']='No Gaussian Parseval transfer; no counterexample to unspecified-constant KLS'
assert len({c['id'] for c in claims})==len(claims)==9
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')
life=json.loads((root/'BUNDLE_LIFECYCLE.json').read_text(encoding='utf-8'))
life['reviewed_claims']=sorted(set(life['reviewed_claims']+['w358-S1.6']))
life['local_schema_validation']=receipt
life['reviewed']=False
(root/'BUNDLE_LIFECYCLE.json').write_text(json.dumps(life,indent=2)+'\n',encoding='utf-8')
source=json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source['independent_math_receipts']={'reviewer':'w359',
    'scalar_claims':'~/brain_workers/w359/REVIEW_w358.md',
    'posterior_and_gram':'~/brain_workers/w359/REVIEW_w358_POSTERIOR.md',
    'kept_claims':life['reviewed_claims'],
    'not_certified':'full October proof manuscripts, whole bundle/edge admission, or compact truncation corollary'}
(root/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for name in ('REPORT.md','REVIEW_PACKET.md'):
    text=(root/name).read_text(encoding='utf-8')
    text=text.replace('later corollaries remain marked for review.','the later compact-support corollary remains marked for review.')
    text=text.replace('later Gram/compact corollaries still need independent checking','the later compact-support corollary still needs independent checking')
    text=text.replace('Narrow remaining mathematical review: check the later Gram corollary Var(q1+q2)=5, energy 2 and the compact truncated-exponential extension.',
        'w359 also kept the exact Gram matrix [[1,1],[1,2]] and variance 5 counterexample in REVIEW_w358_POSTERIOR.md. The later compact truncated-exponential extension remains an optional special case pending independent checking.')
    text=text.replace('w359 check the later Gram/compact corollaries;','w359 check the compact-support corollary;')
    (root/name).write_text(text,encoding='utf-8')
native={'worker_id':'w358','native_thread_id':os.environ.get('CODEX_THREAD_ID'),
        'thread_identity_policy':'Continue this native thread; no AI children or new runner started',
        'requested_settings':{'model':'gpt-6.1-sol','reasoning':'max','service_tier':'Fast'},
        'served_settings':'not independently verified'}
(root/'THREAD_RECEIPT.json').write_text(json.dumps(native,indent=2)+'\n',encoding='utf-8')
required=['SOURCE_STATUS.json','ATTEMPT.md','CLAIMS.jsonl','REPORT.md','REVIEW_PACKET.md',
          'PEER_AUDIT.md','INDEPENDENT_DERIVATION.md','POSTERIOR_BRIDGE_CHECK.md',
          'EDGE_REVIEW.jsonl','BUNDLE_LIFECYCLE.json','SUBMISSION_RECEIPT.json']
assert all((root/p).is_file() and (root/p).stat().st_size>0 for p in required)
for p in root.glob('*.json'):json.loads(p.read_text(encoding='utf-8'))
old_status=(root/'STATUS.md').read_text(encoding='utf-8').splitlines()
assert old_status[0].startswith('STATE:') and old_status[1].startswith('NEXT:')
stamp=datetime.now().astimezone().isoformat(timespec='seconds')
status='STATE: NEEDS_REVIEW\nNEXT: claude-4a88bc43 review the exact draft edges and ingest accepted material; w359 check the optional compact-support corollary.\n'
status+='\n'.join(old_status[2:])+'\n'
status+=f'{stamp}: Completed adversary packet. Five exact scalar claims independently kept by w359; w357 L1-L6 kept at scope. 8 DRAFT concepts/7 exact edges submitted and structurally validated; no ingestion or retrieval claimed. General recall failure measured; exact experiment held by distress gate. Single hard parent gap remains the uniform strict nonlinear posterior contraction.\n'
(root/'STATUS.md').write_text(status,encoding='utf-8')
print(json.dumps({'state':'NEEDS_REVIEW','required_artifacts_present':len(required),
                  'claim_rows':len(claims),'schema':receipt,
                  'reviewed_claims':life['reviewed_claims'],
                  'live_store_modified':False,'ingested':False,'retrievable':False}))
