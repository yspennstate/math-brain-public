"""Lightweight draft/provenance checks; this is NOT a mathematical proof checker."""
import json
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
started=time.perf_counter()
checks=[]
def check(name,ok):
    checks.append({'name':name,'passed':bool(ok)})
    if not ok:
        raise AssertionError(name)

bundle=json.loads((ROOT/'bundle_001.json').read_text(encoding='utf-8'))
entries=bundle['entries']; rels=bundle['relations']; keys={e['key'] for e in entries}
check('draft spec',bundle['spec']=='mathbrain-draft-v1')
check('author',bundle['author_agent']=='w543')
check('entry cap',0<len(entries)<=200)
check('unique keys',len(keys)==len(entries))
check('unique logical names',len({e['logical_name'] for e in entries})==len(entries))
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
for e in entries:
    check(e['key']+': required fields',required<=set(e))
    check(e['key']+': pending material not promoted',e['kind'] in ('concept','definition') and e['proof_text'] is None)
    check(e['key']+': owner source tag',e['source']['license'].startswith('owner-own-work'))
    check(e['key']+': complete statement',len(e['statement'])>150 and bool(e['assumptions']))
    check(e['key']+': review state explicit',e['kind']=='definition' or 'DRAFT' in e['title'])
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
graph={k:[] for k in keys}
for i,r in enumerate(rels):
    check('relation %d: allowed kind'%i,r['kind'] in allowed)
    check('relation %d: exact local ends'%i,r['from_key'] in keys and (r.get('to_key') in keys or 'to_existing_logical' in r))
    check('relation %d: rationale'%i,len(r.get('rationale',''))>40)
    if r['kind']=='depends_on' and 'to_key' in r:
        graph[r['from_key']].append(r['to_key'])
seen=set(); active=set()
def visit(k):
    if k in active: raise AssertionError('cyclic dependency')
    if k in seen: return
    active.add(k)
    for v in graph[k]:visit(v)
    active.remove(k);seen.add(k)
for k in keys:visit(k)
check('dependency graph acyclic',len(seen)==len(keys))
claims=[json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
claim_required={'claim_id','exact_statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap','status'}
check('claim rows nonempty',bool(claims))
for c in claims:
    check(c['claim_id']+': complete claim',claim_required<=set(c))
    audited=c['status']=='independently checked proof'
    check(c['claim_id']+': no independent-check inflation',not audited or (len(c.get('independent_audits',[]))==2 and all(a['verdict']=='KEEP' for a in c['independent_audits'])))
    check(c['claim_id']+': review state recorded',('UNVERIFIED' in c['independent_reviewer']) if audited else ('pending' in c['independent_reviewer'] or 'not yet checked' in c['independent_reviewer']))
source=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
check('openness stays unknown',source['current_openness']=='UNKNOWN')
check('no full target proof claim',not source['microscopic_solution_claim'])
check('missing exact target stated',not source['complete_rigorous_source_statement_recovered'])
check('no formal receipt invented',source['formal_check_receipt'] is None)
hook=json.loads((ROOT/'HOOK_PROPOSAL.jsonl').read_text(encoding='utf-8').strip())
check('hook text budget',len(hook['text'])<=300)
check('hook fire and silent controls',bool(hook['fire_when']) and bool(hook['silent_when']) and bool(hook['evidence']))
for p in (ROOT/'patches').glob('*.diff'):
    lines=p.read_text(encoding='utf-8').splitlines()
    check(p.name+': live-path diff header',lines[0].startswith('--- a/~/') and lines[1].startswith('+++ b/~/'))
result={'command':'python -X utf8 validate_packet.py','checks_passed':len(checks),'checks_failed':0,
    'claim_rows':len(claims),'proved_auxiliary_lemmas':sum(c['status'] in ('proved special case','independently checked proof') for c in claims),
    'independently_checked_auxiliary_claims':sum(c['status']=='independently checked proof' for c in claims),
    'bundle_entries':len(entries),'relations':len(rels),'unreviewed_theorem_or_lemma_entries':0,
    'elapsed_seconds':time.perf_counter()-started,'scope':'schema/provenance only; not mathematical proof or numerical experiment',
    'numerical_quadrature':'withheld if the fresh compute gate denies; no numerical pass claimed','checks':checks}
(ROOT/'VALIDATION.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
