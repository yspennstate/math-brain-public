"""Validate and publish the authorized w516 concept draft; request only the named peer reviews."""
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w516')
MESH = '~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
STAMP = datetime.now(timezone.utc).isoformat()


def mesh_call(arguments, output_name):
    command = ['python', '-X', 'utf8', MESH] + arguments
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace')
    receipt = {'command': command, 'exit_code': result.returncode, 'stdout': result.stdout,
               'stderr': result.stderr, 'recorded_at': datetime.now(timezone.utc).isoformat()}
    try:
        receipt['result'] = json.loads(result.stdout)
    except json.JSONDecodeError:
        pass
    (ROOT / output_name).write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    return receipt


bundle_path = ROOT / 'bundle_local_001.json'
bundle = json.loads(bundle_path.read_text(encoding='utf-8'))
existing_cards = json.loads((ROOT / 'EXISTING_P0297_CARDS.json').read_text(encoding='utf-8'))['rows']
target_logical = 'math:probability.core:open-problem-p0297-exact-hausdorff-dimension-of-liouville-quantum-gravity'
assert any(row['metadata'].get('logical_id') == target_logical for row in existing_cards)
cross_link = {'from_key': 'h', 'to_existing_logical': target_logical, 'kind': 'semantic_association',
              'rationale': 'The source target asks for d_gamma of the gamma-LQG metric. The H entry asks to evaluate mu; L5 plus the sourced Q=2/gamma+gamma/2 and d_gamma=gamma/xi bridge would compute that exact dimension. No solution is asserted.'}
if cross_link not in bundle['relations']:
    bundle['relations'].append(cross_link)
bundle_path.write_text(json.dumps(bundle, indent=2) + '\n', encoding='utf-8')

allowed_relations = {'depends_on', 'defines', 'proves', 'refutes', 'generalizes', 'specializes', 'analogous_to', 'cites', 'semantic_association'}
keys = {entry['key'] for entry in bundle['entries']}
assert len(keys) == len(bundle['entries']) == 8
assert bundle['author_agent'] == 'w516' and bundle['spec'] == 'mathbrain-draft-v1'
required = {'key', 'namespace', 'logical_name', 'kind', 'title', 'statement', 'proof_text', 'assumptions', 'domain', 'source'}
for entry in bundle['entries']:
    assert required <= entry.keys()
    assert entry['kind'] in ('definition', 'concept')
    assert entry['proof_text'] is None
    assert entry['statement'] and entry['source']['license'].startswith('owner-own-work')
    assert entry['source']['source_id'] and entry['source']['url']
    if entry['kind'] == 'concept':
        assert 'DRAFT' in entry['statement'] or entry['statement'].startswith('OPEN INPUT')
for relation in bundle['relations']:
    assert relation['from_key'] in keys and relation['kind'] in allowed_relations and relation['rationale']
    if 'to_key' in relation:
        assert relation['to_key'] in keys
    else:
        assert relation['to_existing_logical'] == target_logical
graph = {key: [] for key in keys}
for relation in bundle['relations']:
    if relation['kind'] == 'depends_on':
        graph[relation['from_key']].append(relation['to_key'])
active, done = set(), set()


def visit(key):
    assert key not in active, 'dependency cycle'
    if key in done:
        return
    active.add(key)
    for child in graph[key]:
        visit(child)
    active.remove(key)
    done.add(key)


for key in keys:
    visit(key)
validation = {'schema_checked': True, 'author': 'w516', 'entries': len(keys),
              'internal_relations': 7, 'source_checked_cross_relations': 1,
              'dependency_graph_acyclic': True, 'all_new_assertions_concept_drafts': True,
              'mathematical_audit': 'pending w518; structural validation is not a mathematical proof'}
(ROOT / 'BUNDLE_VALIDATION.json').write_text(json.dumps(validation, indent=2) + '\n', encoding='utf-8')

# The agent's own inbox is the only authorized shared-file destination. Assert its live claim first.
assertion = mesh_call(['assert', '--agent', 'w516', '--resource', 'path:' + INBOX.as_posix()], 'MESH_INBOX_ASSERT_RECEIPT.json')
if assertion['exit_code']:
    raise RuntimeError('Inbox claim assertion failed; no shared file written. See MESH_INBOX_ASSERT_RECEIPT.json.')
INBOX.mkdir(exist_ok=True)
destination = INBOX / 'bundle_001.json'
part = INBOX / 'bundle_001.part'
assert destination.resolve().parent == INBOX.resolve()
assert part.resolve().parent == INBOX.resolve()
if destination.exists():
    assert json.loads(destination.read_text(encoding='utf-8')) == bundle, 'existing artifact differs; never overwrite'
else:
    with part.open('x', encoding='utf-8') as file:
        json.dump(bundle, file, indent=2)
        file.write('\n')
        file.flush()
        os.fsync(file.fileno())
    part.rename(destination)
assert json.loads(destination.read_text(encoding='utf-8')) == bundle

states = {'worker':'w516','target':'P0297','prepared':{'state':'complete','local_path':str(bundle_path)},
          'submitted':{'state':'submitted_draft','path':str(destination),'at':STAMP,'entries':8,'relations':8},
          'reviewed':{'state':'pending','reviewer':'w518','independent_keep':False},
          'ingested':{'state':'not_verified','no_claim_made':True},
          'retrievable':{'state':'not_verified','no_claim_made':True},
          'parent_problem_solved':False}
(ROOT / 'BRAIN_STATES.json').write_text(json.dumps(states,indent=2)+'\n',encoding='utf-8')
source_path=ROOT/'SOURCE_STATUS.json'
source=json.loads(source_path.read_text(encoding='utf-8'))
source.update({'submitted':True,'reviewed':False,'ingested':None,'retrievable':None,
               'submission_receipt':'BRAIN_STATES.json','integration_note':'Draft-only submission. No store ingestion or retrieval is verified or asserted.',
               'peer_boundary':'w517 independently saved O1/O2 before reading w516; both warn against selected-path or marginal-Gaussian shortcuts. w516 L1 retains the full covariance and the optimizer-switching term.'})
source_path.write_text(json.dumps(source,indent=2)+'\n',encoding='utf-8')
report_path=ROOT/'REPORT.md'
report=report_path.read_text(encoding='utf-8').replace('seven-entry draft bundle','eight-entry draft bundle')
report += '\nSubmitted eight draft entries with seven internal relations and one exact-ID source-backed link to the existing P0297 problem. Structural checks passed; independent review, ingestion and retrieval are pending/not verified.\n'
report_path.write_text(report,encoding='utf-8')
packet_path=ROOT/'review'/'PROOF_PACKET.md'
packet=packet_path.read_text(encoding='utf-8')
packet += '\nSubmission receipt: BRAIN_STATES.json; eight definition/concept entries, seven internal relations and one verified existing-target association. w517 saved its independent Gaussian-selection obstructions before reading w516; these are peer results, not an audit of L1-L6. The full covariance and switching term are retained throughout the w516 reduction.\n'
packet_path.write_text(packet,encoding='utf-8')

measurements=json.loads((ROOT/'measurements.json').read_text(encoding='utf-8'))
numeric={'id':'w516.P0297.NUM01','statement':'The final bounded gate-004 reproduction passed four finite-beta Gaussian response cases, five two-edge beta values and two covariance controls. Maximum response identity residual was '+str(measurements['maximum_ibp_absolute_error'])+'. Two-edge zero-temperature derivative error changed from 0.5641895835477563 when switching was omitted to '+str(measurements['two_edge_cases'][-1]['corrected_absolute_error'])+' with the finite-beta switching term at beta=1250.',
         'assumptions':['Deterministic Simpson quadrature, finite models only; no interval-certified error bounds or LQG extrapolation'],
         'source':{'artifact':str(ROOT/'measurements.json'),'command':'python -X utf8 ./measure_response.py','gate':'COMPUTE_GATE_004.json'},
         'proof_or_counterexample':'Run receipt supports finite-model proofs L1/L3; numerical agreement is not a proof of the LQG scale limit.',
         'independent_reviewer':'w518 (pending)','remaining_gap':'Hard input H and independent mathematical audit remain open.','status':'numerical evidence','artifact_state':'local run receipt'}
with (ROOT/'CLAIMS.jsonl').open('a',encoding='utf-8') as file:
    file.write(json.dumps(numeric)+'\n')

handovers=[]
for recipient,topic,body in [
    ('w517','probability:P0297:proof-packet','Complete w516 proof packet: ~/brain_workers/w516/review/PROOF_PACKET.md. L1-L6 retain full Gaussian covariance and the zero-temperature optimizer-switching term; H (limiting response-defect measure) remains unproved. Your independently saved O1/O2 boundary was read after our proofs were saved. Please send any concrete counterexample/FIX to w518; no audit claimed.'),
    ('w518','probability:P0297:referee','Review w516 complete packet: ~/brain_workers/w516/review/PROOF_PACKET.md; ATTEMPT.md L1-L6, CLAIMS.jsonl, GAP.md and measurements.json. Eight concept/definition drafts submitted at ~/math-brain-inbox/w516/bundle_001.json; no ingestion claim. Check Gaussian switching identity, mean-median/finite approximation bridge and Stieltjes reduction. P0297 unresolved; H is explicit evaluation of mu. KEEP/FIX/DROP in your folder; own new results go to w521.')]:
    receipt=mesh_call(['send','--agent','w516','--to',recipient,'--topic',topic,'--kind','message','--body',body], 'HANDOFF_'+recipient.upper()+'.json')
    handovers.append({'recipient':recipient,'exit_code':receipt['exit_code'],'result':receipt.get('result'),'receipt':'HANDOFF_'+recipient.upper()+'.json'})
(ROOT/'REVIEW_REQUEST.json').write_text(json.dumps({'requested_at':STAMP,'proof_packet':str(packet_path),'reviewer':'w518','adversary':'w517','handovers':handovers,'independent_verdict':'not received','any_new_referee_result_reviewer':'w521'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'submitted':str(destination),'entries':8,'relations':8,'handovers':handovers,
                  'mathematical_review':'pending','ingestion':'not verified','gap':'H: explicit evaluation of mu'}))
