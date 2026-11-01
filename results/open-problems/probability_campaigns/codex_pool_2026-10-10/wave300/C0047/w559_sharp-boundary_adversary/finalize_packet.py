"""Verify review artifacts and record the authorized mesh/progress handoff."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json
import os
import sqlite3
import subprocess
import sys

root=Path(__file__).resolve().parent
now=datetime.now(timezone.utc).isoformat()

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        while chunk:=f.read(65536):
            h.update(chunk)
    return 'sha256:'+h.hexdigest()

def write(path,value):
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

# Update documentary status only; the independent proof remains frozen.
claims=[json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
for row in claims:
    if row['claim_id']=='w559-C0047-source-001':
        row['remaining_gap']='Original graph/model quantifiers are now recovered in SOURCE_STATUS.json. Current full-result proof status and the independent source KEEP remain unverified.'
    if row['claim_id']=='w559-C0047-source-002':
        row['source']['quote']='ρ(G)kp < 1'
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')
source=json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source['recent_status_flag']='The public scope note claims a full result. Comparator placeholders are templates; the named solution module and actual comparator proof receipt remain unchecked. No evidence of mathematical failure is inferred.'
source['stuck_notes']=['STUCK: two raw CayleyPercolation.lean fetch attempts failed; switched to the accessible BenjaminiSchramm comparator and configuration. No further status search or formal run was attempted.']
source['updated_utc']=now
write(root/'SOURCE_STATUS.json',source)

hashes=json.loads((root/'ARTIFACT_HASHES.json').read_text(encoding='utf-8'))
documentary_updates={str(root/'CLAIMS.jsonl'),str(root/'SOURCE_STATUS.json')}
for row in hashes['files']:
    p=Path(row['path'])
    if str(p) not in documentary_updates:
        assert digest(p)==row['sha256'],f'Frozen artifact changed: {p}'
    row.update(sha256=digest(p),bytes=p.stat().st_size)
write(root/'ARTIFACT_HASHES.json',hashes)

patch_inputs=json.loads((root/'PATCH_INPUTS.json').read_text(encoding='utf-8'))
for item in patch_inputs:
    p=Path(item['path'])
    assert digest(p)==item['sha256'],f'Original source changed; rebase patch: {p}'
    with p.open(encoding='utf-8') as f:
        line=next(line for i,line in enumerate(f,1) if i==item['line'])
    assert line.rstrip('\r\n')==item['old_statement_line']

correction=json.loads((root/'STORE_CORRECTION.json').read_text(encoding='utf-8'))
c=sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True)
observed=c.execute('SELECT digest FROM nodes WHERE id=?',(correction['target_id'],)).fetchone()
c.close()
assert observed and observed[0]==correction['expected_node_digest']

global_hook=Path('~/primary_directive/hooks1000/proposals/math-w559.jsonl')
local_hooks=[json.loads(line) for line in (root/'HOOK_PROPOSALS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
global_rows={row['id']:row for row in (json.loads(line) for line in global_hook.read_text(encoding='utf-8').splitlines() if line.strip())}
assert all(global_rows[h['id']]==h for h in local_hooks)

proof_hash=digest(root/'ATTEMPT.md')
bundle=Path('~/math-brain-inbox/w559/bundle_001.json')
bundle_hash=digest(bundle)
audit=json.loads((root/'AUDIT_W558.json').read_text(encoding='utf-8'))
assert audit['independent_derivation_sha256']==proof_hash
assert digest(root/'review_inputs/w558_ATTEMPT.md')==audit['proof_sha256']
validation={
    'status':'PASS','checked_utc':now,'claim_rows':len(claims),'entries':5,'relations':6,
    'artifact_hashes_verified':len(hashes['files']),'source_patch_inputs_verified':len(patch_inputs),
    'live_node_expected_digest_verified':True,'global_hook_rows_match':True,
    'independent_proof_still_frozen':True,'source_mutations':0,'store_mutations':0,
    'formal_proof_receipt':False,'referee_review_pending':True,
    'submission':'DRAFT concepts only','ingested':False,'retrievable':False}
write(root/'FINAL_VALIDATION.json',validation)

mesh='~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
messages=[
    ('w558','message',
     f'Scoped adversarial KEEP saved: ~/brain_workers/w559/AUDIT_W558.json; proof snapshot {audit["proof_sha256"]}. Independent two-type derivation recovers p(2chi_N-1)=1; arbitrary-Cayley extension needs disjoint factor/bridge premises. Source multiplicity supplement distinguishes simple C2*C3 pc=.6372776105 from parallel-a pc=.5199490766 (128 states PASS). Model conventions are in w559/MODEL_CONVENTIONS.md; normalization correction duplicates yours and should be deduplicated at integration.'),
    ('w560','request',
     f'Frozen review packet: ~/brain_workers/w559/REVIEW_PACKET.md. Independent ATTEMPT.md {proof_hash}. Exact 32/128-state checks PASS; please check infinite block-tree proof, h_E=1/3, pu=1, 3*rho*pc>1.26, and single/parallel bond conventions. AUDIT_W558.json is scoped KEEP for the F2 family. Five DRAFT concepts, six quoted-end relations; no full solution or novelty. Response-side served identity unavailable; different-model gate remains pending.'),
    ('codex-01a12190','message',
     f'C0047 packet: ~/brain_workers/w559/REVIEW_PACKET.md; file hashes ARTIFACT_HASHES.json. Inbox ~/math-brain-inbox/w559/bundle_001.json {bundle_hash}: 5 DRAFT concepts/6 supported relations. One digest-bound live-card degree/rho correction plus two source diff hunks. w559 scoped KEEP of w558 family; w560 proof check pending. Author response-side served identity absent (requested settings not evidence). Current full-result status UNKNOWN; no theorem promotion/parent solution; deduplicate w558 source correction.')
]
receipts=[]
for recipient,kind,body in messages:
    result=subprocess.run([sys.executable,'-X','utf8',mesh,'send','--agent','w559','--to',recipient,
                           '--topic','probability300/C0047','--kind',kind,'--body',body],
                          capture_output=True,text=True,encoding='utf-8',env=env,
                          creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    row={'to':recipient,'kind':kind,'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr}
    receipts.append(row)
    write(root/'MESH_HANDOFF.json',receipts)
    print(json.dumps({'recipient':recipient,'returncode':result.returncode,'receipt':result.stdout.strip(),'error':result.stderr.strip()}))

progress=subprocess.run([sys.executable,'-X','utf8','~/primary_directive/pd_progress.py',
    '--event','C0047 complete review packet: 32/128-state checks PASS, exact triangle boundary, scoped paired-proof KEEP, digest-bound source correction, 5 DRAFT concepts and 6 supported relations',
    '--agent','w559','--row','S1.C0047.w559.4','--evidence',str(root/'REVIEW_PACKET.md')],
    capture_output=True,text=True,encoding='utf-8',env=env,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
write(root/'PROGRESS_RECEIPT.json',{'returncode':progress.returncode,'stdout':progress.stdout,'stderr':progress.stderr})
print(json.dumps({'progress_returncode':progress.returncode,'progress':progress.stdout.strip(),'error':progress.stderr.strip()}))

failed=[r['to'] for r in receipts if r['returncode']]
if failed or progress.returncode:
    (root/'STATUS.md').write_text('STATE: WORKING\nNEXT: Retry the failed protocol handoff named in MESH_HANDOFF.json/PROGRESS_RECEIPT.json; artifacts and math checks are complete.\n\n'
        +f'{now}: Final packet validation PASS; pending protocol delivery only: {failed}; progress rc={progress.returncode}. Proof and source/model review remain w560\'s next step.\n',encoding='utf-8')
    raise SystemExit(2)

(root/'STATUS.md').write_text(
    'STATE: NEEDS_REVIEW\n'
    'NEXT: w560 independently checks the frozen C_2*C_3 proof and multiplicity convention; integration verifies served-model evidence, deduplicates the source correction, and ingests only reviewed material.\n\n'
    '2026-10-10: Read the primary directive and scoped C0047 prior records, recovered original quantifiers, and read the named scar after a 60s recall timeout. No assigned hook audits or open votes.\n'
    '2026-10-10 07:01 UTC: Saved ATTEMPT.md independently before reading w558\'s proof: exact quartic p_c, p_u=1, h_E=1/3, spectral product>1.26.\n'
    '2026-10-10: Exact 32-state check passed in 0.004845s; fresh gated 128-state multiplicity check passed in 0.010378s.\n'
    '2026-10-10: Kept w558\'s original proof within the F_2 power-generator family; separately derived its critical equation and named the missing general-Cayley premise.\n'
    '2026-10-10: Prepared two one-line archival source patches and a live-node digest-bound superseding-correction proposal. Submitted five DRAFT concepts with six quoted-end relations and two narrow hook proposals. No live store/source mutation, theorem promotion, novelty claim, or parent-problem solution.\n'
    '2026-10-10: STUCK on two raw CayleyPercolation fetches; accessible comparator configuration identifies the actual solution module and permitted axioms. No mathematical or formal check receipt for the public September 2026 full-result claim; current openness UNKNOWN.\n'
    +f'{now}: Final validation PASS; exact artifact/source hashes and live node digest checked. Review/integration notices delivered to w558, w560, codex-01a12190; progress event logged. Required w560 independent check and response-side served-model evidence remain pending.\n',encoding='utf-8')
print(json.dumps({'state':'NEEDS_REVIEW','validation':validation,'proof_sha256':proof_hash,'bundle_sha256':bundle_hash},indent=2))
