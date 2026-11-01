import ast
import datetime
import json
import pathlib

root=pathlib.Path(__file__).resolve().parent
validation=json.loads((root/'validation_receipt.json').read_text(encoding='utf-8'))
review=json.loads((root/'review_packet_receipt.json').read_text(encoding='utf-8'))
assert validation['result']==review['result']=='PASS'
assert validation['entries']==review['draft_entries']==15
assert validation['quoted_edges']==27
assert review['hook_fire_controls']==review['hook_silent_controls']==6
packet=json.loads((root/'REVIEW_PACKET.json').read_text(encoding='utf-8'))
assert packet['independent_keeps_recorded']==0
assert len(packet['entries'])==15
assert len((root/'AUDIT_REQUEST.jsonl').read_text(encoding='utf-8').splitlines())==10
for item in packet['entries']:
    assert all(pathlib.Path(item[key]).is_file() for key in ('bundle','proof','checks'))
for path in root.glob('*.py'):
    ast.parse(path.read_text(encoding='utf-8'),filename=str(path))

def parse_new_file_diff(path):
    chunks=[]
    current=None
    for line in path.read_text(encoding='utf-8').splitlines(keepends=True):
        if line.startswith('--- a/'):
            if current:
                chunks.append(current)
            current={'old':line[6:].strip(),'new':None,'payload':[]}
        elif line.startswith('+++ b/'):
            current['new']=line[6:].strip()
        elif line.startswith('@@ '):
            assert '-0,0 ' in line
        else:
            assert current is not None and line.startswith('+')
            current['payload'].append(line[1:])
    if current:
        chunks.append(current)
    for chunk in chunks:
        assert chunk['old']==chunk['new']
    return chunks

bundle_chunks=parse_new_file_diff(root/'patches'/'01_math_bundle_drafts.diff')
assert len(bundle_chunks)==10
for chunk in bundle_chunks:
    filename=pathlib.Path(chunk['new']).name
    assert ''.join(chunk['payload'])==(root/'bundles'/filename).read_text(encoding='utf-8')
hook_chunks=parse_new_file_diff(root/'patches'/'02_math_hooks.diff')
assert len(hook_chunks)==1
assert ''.join(hook_chunks[0]['payload'])==(root/'hooks'/'math-w335.jsonl').read_text(encoding='utf-8')

inbox=pathlib.Path('~/math-brain-inbox/w335')
visible=0
for local in (root/'bundles').glob('bundle_*.json'):
    shared=inbox/local.name
    if shared.is_file():
        assert shared.read_bytes()==local.read_bytes()
        visible+=1
    rejected=shared.with_suffix('.rejected-note')
    assert not rejected.is_file(), 'Integrator rejection requires review: '+str(rejected)
report=(root/'REPORT.md').read_text(encoding='utf-8')
assert 'NEXT:' in report and 'literature_check_pending' in report
assert 'Lean-checked' in report and 'SETUP_UNVERIFIED' in report
rows=[json.loads(line) for line in (root/'results.jsonl').read_text(encoding='utf-8').splitlines() if line]
assert len({row['row_id'] for row in rows})==len(rows)
assert sum(row.get('result_type')=='bounded_status_receipt' for row in rows)==10

for hook in (json.loads(line) for line in (root/'hooks'/'math-w335.jsonl').read_text(encoding='utf-8').splitlines()):
    row_id='w335-'+hook['id']+'-hook-proposal'
    if not any(row['row_id']==row_id for row in rows):
        with (root/'results.jsonl').open('a',encoding='utf-8') as stream:
            stream.write(json.dumps({'row_id':row_id,'result_type':'measured_hook_proposal','hook_id':hook['id'],'proposal_path':str(root/'hooks'/'math-w335.jsonl'),'evidence':hook['evidence'],'controls_path':str(root/'hook_controls.json'),'label':'proposed; fire and silent controls passed; no independent KEEP','audit_status':'pending_pair_audit'})+'\n')
receipt={'command':'python -X utf8 seal_review.py','result':'PASS','draft_nodes':15,'quoted_edges':27,'bundles':10,'hook_proposals':6,'inbox_copies_visible_and_matching':visible,'full_problem_solution_claims':0,'independent_keeps_recorded':0,'lean_checked':False,'patch_content_checks':'10 bundle file additions and one hook file addition match saved payloads','created':datetime.datetime.now().astimezone().isoformat()}
(root/'FINAL_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
status=(root/'STATUS.md').read_text(encoding='utf-8').splitlines()
status[0]='STATE: NEEDS_REVIEW'
status=[('NEXT: w347 audits REVIEW_PACKET.json; claude-4a88bc43 integrates only KEEP entries and records the receipts in the brain.' if line.startswith('NEXT:') else line) for line in status]
status.append('2026-10-10: Finished and measured: 10 bundles, 15 draft lemmas, 27 quoted edges, 10 bounded literature-status receipts, six hook proposals with six fire/silent pairs. Review packet, unified diffs, source-alignment audit and cost receipt saved. PRIMARY_DIRECTIVE reread at 101 minutes; no open votes or local feedback. Final checks passed; independent KEEP and full-solution counts remain zero.')
(root/'STATUS.md').write_text('\n'.join(status)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2),flush=True)
