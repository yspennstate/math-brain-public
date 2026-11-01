"""Read-only artifact integrity and draft-scope checks; not mathematical certification."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
ALLOWED_RELATIONS={'depends_on','defines','proves','refutes','generalizes','specializes',
                  'analogous_to','cites','semantic_association'}
ALLOWED_CLAIMS={'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}

def main() -> None:
    checks=[]
    def check(condition: bool, label: str) -> None:
        if not condition:
            raise AssertionError(label)
        checks.append(label)
    bundle=json.loads((ROOT/'bundle_001.json').read_text(encoding='utf-8'))
    packet=json.loads((ROOT/'REVIEW_PACKET.json').read_text(encoding='utf-8'))
    check(bundle['spec']=='mathbrain-draft-v1','draft spec')
    check(bundle['author_agent']=='w492','author identity')
    entries=bundle['entries']
    check(0<len(entries)<=200,'bounded entry count')
    keys={entry['key'] for entry in entries}
    check(len(keys)==len(entries),'unique entry keys')
    lookup={entry['key']:entry for entry in entries}
    for entry in entries:
        check(entry['kind'] in {'concept','definition'},'no theorem promotion '+entry['key'])
        check(entry['proof_text'] is None,'draft proof text stays null '+entry['key'])
        check(entry['source']['license'].startswith('owner-own-work'),'accepted source tag '+entry['key'])
        check(bool(entry['statement']) and isinstance(entry['assumptions'],list),'complete statement '+entry['key'])
    graph={key:[] for key in keys}
    evidence=[]
    for relation in bundle['relations']:
        check(relation['from_key'] in keys,'relation source exists')
        check(relation['kind'] in ALLOWED_RELATIONS,'allowed relation kind')
        if 'to_key' in relation:
            check(relation['to_key'] in keys,'relation target exists')
            if relation['kind']=='depends_on':
                graph[relation['from_key']].append(relation['to_key'])
            target_quote=lookup[relation['to_key']]['statement']
        else:
            check(relation['to_existing_logical'].startswith('math:probability.gaussian:'),'scoped existing target')
            target_quote=('Var(log Z_n) = O(n/log n)' if 'open-problem-' in relation['to_existing_logical']
                          else 'no new input')
        evidence.append({'relation':relation,'from_quote':lookup[relation['from_key']]['statement'],
                         'to_quote':target_quote,'status':'draft relation; audit pending'})
    visiting=set()
    visited=set()
    def visit(key: str) -> None:
        check(key not in visiting,'acyclic dependency '+key)
        if key in visited:
            return
        visiting.add(key)
        for target in graph[key]:
            visit(target)
        visiting.remove(key)
        visited.add(key)
    for key in sorted(keys):
        visit(key)
    claims=[json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
    check(len({r['id'] for r in claims})==len(claims),'unique claim IDs')
    for claim in claims:
        check(claim['status'] in ALLOWED_CLAIMS,'allowed status '+claim['id'])
        check(all(key in claim for key in ('statement','assumptions','source','proof_or_counterexample',
              'independent_reviewer','remaining_gap')),'claim provenance '+claim['id'])
    check(next(r for r in claims if r['id']=='w492-G1')['status']=='conjecture','hard gap remains conjecture')
    check(packet['parent_problem_solved'] is False,'no solved parent flag')
    check(packet['served_identity']['status']=='UNVERIFIED','no invented served-model receipt')
    for name,item in packet['files'].items():
        check(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==item['sha256'],'packet SHA256 '+name)
    original=json.loads((ROOT/'source_records/C0120_original.json').read_text(encoding='utf-8'))
    corrected=json.loads((ROOT/'source_records/C0120_corrected.json').read_text(encoding='utf-8'))
    check({k for k in original if original[k]!=corrected[k]}=={'statement','status_search'},'only source scope fields patched')
    check(original['problem_id']==corrected['problem_id']=='C0120','patch candidate unchanged')
    patch=(ROOT/'patches/01_c0120_source_scope.diff').read_text(encoding='utf-8').splitlines()
    plus=json.loads(next(line[1:] for line in patch if line.startswith('+{')))
    minus=json.loads(next(line[1:] for line in patch if line.startswith('-{')))
    check(plus==corrected and minus==original,'exact original and corrected patch rows')
    check('@@ -120 +120 @@' in patch,'targeted intake line hunk')
    gate=json.loads((ROOT/'COMPUTE_GATE.json').read_text(encoding='utf-8'))
    receipt=json.loads((ROOT/'CHECK_RECEIPT.json').read_text(encoding='utf-8'))
    check(receipt['elapsed_seconds']<=gate['wall_budget_seconds'],'fresh compute wall budget')
    check(gate['max_grid_points']==7*(8192+4096+2),'fresh compute grid accounting')
    check(receipt['checks_passed']==21,'21 numerical consistency checks')
    check(len(receipt['rows'])==7,'seven corridor sizes')
    check(max(r['refinement_difference'] for r in receipt['rows'])<1e-6,'refinement consistency')
    (ROOT/'RELATION_EVIDENCE.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in evidence),encoding='utf-8')
    result={'command':'python -X utf8 verify_packet.py','checks_passed':len(checks),
            'checks':checks,'mathematical_proof_certified':False,'different_model_gate_passed':False}
    (ROOT/'VALIDATION_RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'checks_passed':len(checks),'draft_entries':len(entries),'draft_relations':len(evidence),
                     'parent_problem_solved':False,'proof_audit':'pending'}))

if __name__=='__main__':
    main()
