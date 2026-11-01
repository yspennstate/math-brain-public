import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
REPO=Path('~/<private-repo>')
bundle=json.loads((ROOT/'review/bundle_001.json').read_text(encoding='utf-8'))
submitted=json.loads(Path('~/math-brain-inbox/w564/bundle_001.json').read_text(encoding='utf-8'))
assert bundle==submitted
entries={e['key']:e for e in bundle['entries']}
allowed={'depends_on','defines','proves','refutes','generalizes','specializes',
         'analogous_to','cites','semantic_association'}
rows=[]
for relation in bundle['relations']:
    assert relation['kind'] in allowed
    source,target=entries[relation['from_key']],entries[relation['to_key']]
    rows.append({'row_id':'w564-C0029-E'+str(len(rows)+1),'status':'DRAFT',
                 'from_key':source['key'],'from_card_quote':source['statement'],
                 'to_key':target['key'],'to_card_quote':target['statement'],
                 'relation':relation['kind'],'rationale':relation['rationale'],
                 'mathematical_evidence':'ATTEMPT.md L1/L2 for depends_on; L3 for refutes',
                 'independent_reviewer':'w566 pending','remaining_gap':'H is unproved; concept edges only'})
with (ROOT/'review/EDGE_ROWS.jsonl').open('w',encoding='utf-8') as stream:
    for row in rows:
        stream.write(json.dumps(row,ensure_ascii=False)+'\n')
patch=(ROOT/'patches/01_gaussian_limit_scope.diff').read_text(encoding='utf-8').splitlines()
matched=0
target=None
line_number=None
valid_targets={'06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl',
               '06_math_research/probability_1000_intake_claude_20260907/brain_bundle_C004b.json'}
for line in patch:
    if line.startswith('--- a/'):
        target=line[6:]
        assert target in valid_targets
    elif line.startswith('@@ '):
        line_number=int(line.split()[1][1:].split(',')[0])
    elif line.startswith('-') and not line.startswith('---'):
        with (REPO/target).open(encoding='utf-8-sig') as stream:
            actual=next(s for i,s in enumerate(stream,1) if i==line_number).rstrip('\r\n')
        assert actual==line[1:], 'Live source row changed; patch must be regenerated without overriding peers.'
        matched+=1
assert matched==2
for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines():
    claim=json.loads(line)
    assert claim['status'] in {'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
    assert all(k in claim for k in ('statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap'))
assert all(e['kind']=='concept' and e['proof_text'] is None for e in entries.values())
hook=json.loads((ROOT/'review/hooks.jsonl').read_text(encoding='utf-8'))
assert any(json.loads(line)==hook for line in Path('~/primary_directive/hooks1000/proposals/math-w564.jsonl').read_text(encoding='utf-8').splitlines() if line.strip())
receipt={'submitted_bundle_matches':True,'concepts':len(entries),'supported_edge_rows':len(rows),
         'source_patch_current_rows_match':matched,'submitted_hook_matches':True,
         'mathematical_review':'pending','live_store_write':False,'parent_estimate_H':'UNPROVED'}
(ROOT/'evidence/artifact_validation.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
old_manifest=json.loads((ROOT/'review/packet_hashes.json').read_text(encoding='utf-8'))
names=list(old_manifest)+['REPORT.md','review/REVIEW_PACKET.md','review/EDGE_ROWS.jsonl',
                          'evidence/artifact_validation.json','prepare_deliverables.py','validate_artifacts.py']
manifest={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in names}
(ROOT/'review/packet_hashes.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'validation':receipt,'ATTEMPT.md_sha256':manifest['ATTEMPT.md'],
                  'patch_sha256':manifest['patches/01_gaussian_limit_scope.diff']},indent=2))
