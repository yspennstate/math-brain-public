"""Local structural checks only; never a theorem or runtime-lock receipt."""
import ast
import hashlib
import json
from pathlib import Path
import re

R=Path(__file__).resolve().parent
results=[]
def check(name,condition):
    if not condition:
        raise AssertionError(name)
    results.append(name)
required=['STATUS.md','SOURCE_STATUS.json','ATTEMPT.md','CLAIMS.jsonl','REPORT.md','review/REVIEW_PACKET.md',
          'INDEPENDENT_BRIDGE.md','AUDIT_w369.md','drafts/bundle_001.json','drafts/STATE.json',
          'patches/01_readonly_attachment_lock.diff','patches/01_provenance.json']
check('all required deliverables exist',all((R/p).is_file() for p in required))
b=json.loads((R/'drafts/bundle_001.json').read_text(encoding='utf-8'))
check('draft schema and author',b['spec']=='mathbrain-draft-v1' and b['author_agent']=='w370' and len(b['entries'])<=200)
keys={e['key'] for e in b['entries']}
check('unique entry keys',len(keys)==len(b['entries']))
for e in b['entries']:
    check('complete entry '+e['key'],all(x in e for x in ['key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source']))
    check('no promotion '+e['key'],e['kind'] in ['concept','definition'] and e['proof_text'] is None)
    check('accepted source tag '+e['key'],e['source']['license'].startswith('owner-own-work'))
    check('logical name '+e['key'],re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name']) is not None)
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
for rel in b['relations']:
    check('relation '+rel['kind'],rel['from_key'] in keys and rel['kind'] in allowed and
          ((rel.get('to_key') in keys) or rel.get('to_existing_logical','').startswith('math:')))
dep={k:[] for k in keys}
for rel in b['relations']:
    if rel['kind']=='depends_on' and 'to_key' in rel:
        dep[rel['from_key']].append(rel['to_key'])
def visit(k,path):
    check('acyclic dependency '+k,k not in path)
    for dest in dep[k]:visit(dest,path|{k})
for k in keys:visit(k,set())
claims=[json.loads(s) for s in (R/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
statuses={'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
for c in claims:
    check('claim fields '+c['id'],all(k in c for k in ['statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap','status']) and c['status'] in statuses)
state=json.loads((R/'drafts/STATE.json').read_text(encoding='utf-8'))
check('states kept separate',state['prepared'] and all(state[k] is False for k in ['submitted','reviewed','ingested','retrievable']))
before=(R/'copies/brain_node_documents.py').read_text(encoding='utf-8')
after=(R/'prototype/brain_node_documents.py').read_text(encoding='utf-8')
ba=ast.parse(before)
aa=ast.parse(after)
def func(tree,name):return next(x for x in tree.body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef)) and x.name==name)
check('writer protocol unchanged',ast.dump(func(ba,'_attachment_write_lock'))==ast.dump(func(aa,'_attachment_write_lock')))
check('document integrity verifier unchanged',ast.dump(func(ba,'_load_documents_unlocked'))==ast.dump(func(aa,'_load_documents_unlocked')))
check('candidate reader opens read-only','os.O_RDONLY' in ast.get_source_segment(after,func(aa,'_attachment_read_lock')))
check('live path in diff header',(R/'patches/01_readonly_attachment_lock.diff').read_text(encoding='utf-8').startswith('--- a/~/.claude/dreaming/brain_node_documents.py'))
provenance=json.loads((R/'patches/01_provenance.json').read_text(encoding='utf-8'))
live_hash=hashlib.sha256(Path(provenance['live_path']).read_bytes()).hexdigest()
baseline_hash=hashlib.sha256((R/'copies/brain_node_documents.py').read_bytes()).hexdigest()
check('archived source matches pinned baseline',baseline_hash==provenance['source_sha256'])
if provenance.get('deployment_permitted') is False:
    observed=(R/'copies/brain_node_documents_resume.py').read_bytes()
    observed_hash=hashlib.sha256(observed).hexdigest()
    check('stale patch explicitly superseded',provenance['deployment']=='superseded; do not apply' and (R/'patches/01_STATUS.md').is_file())
    check('live drift snapshot matches receipt',observed_hash==provenance['observed_current_source_sha256'] and observed_hash!=baseline_hash)
    oa=ast.parse(observed.decode('utf-8'))
    check('observed fallback present',all(any(isinstance(x,ast.FunctionDef) and x.name==name for x in oa.body) for name in ['_lock_writable','_load_documents_snapshot']))
    check('observed fallback preserves verifier',ast.dump(func(oa,'_load_documents_unlocked'))==ast.dump(func(ba,'_load_documents_unlocked')))
else:
    observed_hash=baseline_hash
    check('live source remains the copied baseline',live_hash==provenance['source_sha256'])
receipt={'scope':'structural packet and Python AST checks only','checks_passed':len(results),'checks':results,
         'runtime_lock_tests_executed':False,'formal_mathematical_proof':False,'live_source_unchanged':live_hash==baseline_hash,
         'code_proposal_status':provenance['deployment'],'live_source_sha256':live_hash,
         'live_source_matches_observed_snapshot':live_hash==observed_hash,
         'draft_entries':len(b['entries']),'draft_relations':len(b['relations']),'claims':len(claims)}
(R/'validation_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt))
