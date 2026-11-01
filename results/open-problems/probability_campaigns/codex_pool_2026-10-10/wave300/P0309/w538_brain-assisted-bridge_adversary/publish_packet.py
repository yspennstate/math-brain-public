import ast,datetime,json,pathlib,subprocess
w=pathlib.Path('~/brain_workers/w538')
for name in ['measure.py','riesz_scope_guard.py','prepare_packet.py','validate_packet.py']:
 ast.parse((w/name).read_text(encoding='utf-8-sig'),filename=name)
validation=json.loads((w/'VALIDATION.json').read_text(encoding='utf-8'))
assert validation['patch_validation']['check_returncode']==0 and validation['patch_validation']['content_matches']
assert not validation['patch_validation']['apply_stderr']
locator=pathlib.Path('~/math-research-brain/src/math_brain/build_signal_cache.py')
line=next((r for r in locator.read_text(encoding='utf-8').splitlines()[18:29] if r.startswith('STORE =')),None)
assert line and 'math-brain-build' in line and 'population' in line
(w/'CANONICAL_STORE_LOCATOR.json').write_text(json.dumps({'canonical_code':str(locator),'line':24,'exact_locator':line,'store_access':'The referenced population SQLite store was opened with mode=ro and PRAGMA query_only=ON; full selected cards are in math_brain_probe.json.','no_separate_store_assumed':True},indent=2),encoding='utf-8')
ss=json.loads((w/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
ss['canonical_store_check']={'code_locator':str(locator)+':24','locator':line,'referenced_store_used_read_only':True,'distinct_store_assumption':False}
ss['direct_store_writes']=False
ss['mathematical_proof_complete']=False
ss['states']={'submitted':False,'reviewed':False,'ingested':False,'retrievable':False}
coverage=json.loads((w/'PEER_COVERAGE.json').read_text(encoding='utf-8'))
pp=pathlib.Path('~/brain_workers/w537')
coverage['final_inspection_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
coverage['files_at_final_inspection']=[p.name for p in pp.iterdir() if p.is_file()] if pp.is_dir() else []
(w/'PEER_COVERAGE.json').write_text(json.dumps(coverage,indent=2),encoding='utf-8')
if any(n in coverage['files_at_final_inspection'] for n in ['ATTEMPT.md','PROOF.md','CLAIMS.jsonl']) and not coverage.get('paired_proof_audited'):
 print('PAIRED_PROOF_NOW_AVAILABLE',coverage['files_at_final_inspection']);raise SystemExit(7)
inbox=pathlib.Path('~/math-brain-inbox/w538')
inbox.mkdir(exist_ok=True)
target=inbox/'bundle_001.json'
data=(w/'bundle_001.json').read_bytes()
if target.exists():
 assert target.read_bytes()==data,'Do not overwrite a different existing draft.'
else:
 part=inbox/'bundle_001.part'
 with part.open('xb') as f:f.write(data);f.flush()
 part.rename(target)
ss['states']['submitted']=True
ss['submitted_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
ss['draft_submission_path']=str(target)
(w/'SOURCE_STATUS.json').write_text(json.dumps(ss,ensure_ascii=False,indent=2),encoding='utf-8')
packet=w/'REVIEW_PACKET.md'
ptext=packet.read_text(encoding='utf-8').replace('proposed inbox destination ~/math-brain-inbox/w538/bundle_001.json','submitted atomically to ~/math-brain-inbox/w538/bundle_001.json (unreviewed; not ingested)')
ptext=ptext.replace('No live recall code or SQLite store is changed.','The helper changes no live recall code or mathematical store; measurements are local.')
packet.write_text(ptext,encoding='utf-8')
rp=w/'REPORT.md'
rtext=rp.read_text(encoding='utf-8').replace('No global recall control or live store was edited.','No direct writes to the math stores or global recall code were made.')
rtext+='\nValidation: eight entries, nine relations, acyclic dependencies and all three cross-bundle targets resolved. The corrected LF new-file patch checked and applied without warnings in a fresh worker-only fixture; installed helper content matched. This structural receipt is not mathematical review. Draft submitted atomically to the w538 inbox; reviewed/ingested/retrievable remain false. The canonical repository code points to the population store used read-only (CANONICAL_STORE_LOCATOR.json).\n'
rp.write_text(rtext,encoding='utf-8')
mesh='~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
messages=[
 ('w537','request','Independent P0309 checkpoint and review packet saved at ~/brain_workers/w538/REVIEW_PACKET.md. I claim the disjoint vector-Hessian/Dirichlet covariance/coherent-phase bridge. I audited C1-C5 and separately derived C5; KEEP_CONDITIONAL. O3 blocks direct global finite Riesz convexity; O4 preserves circular symmetry but exponentially rare chart mass gives no cusp. Audit at w538/PAIRED_AUDIT.md. Draft submitted to math-brain-inbox/w538/bundle_001.json; no P0309 proof claimed.'),
 ('w539','request','Concrete P0309 review packet ready: ~/brain_workers/w538/REVIEW_PACKET.md. Please independently check B1, O1-O4 and the paired C5 derivation; especially beta, Dirichlet Green inverse, positivity before squaring and phase centering. All new mathematical bundle entries remain DRAFT concepts pending you. Measurements flag 3/3 actual homonym hits with 5/5 silent controls; recall remains 0/3. w537 C1-C5 audited with KEEP_CONDITIONAL; see PAIRED_AUDIT.md. O3 blocks full-space convexity and O4 tests conditional/full-law transfer. Your own new results require w542.')
]
receipts=[]
for to,kind,body in messages:
 command=['python','-X','utf8',mesh,'send','--agent','w538','--to',to,'--topic','probability-P0309-w538-bridge','--kind',kind,'--body',body,'--idempotency-key','w538-p0309-packet-20261010-'+to]
 r=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',timeout=60)
 receipts.append({'to':to,'kind':kind,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
 (w/'MESH_RECEIPTS.json').write_text(json.dumps(receipts,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(receipts[-1],ensure_ascii=False))
read=subprocess.run(['python','-X','utf8','~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py','read','--as','w538','--max','8'],capture_output=True,text=True,encoding='utf-8',timeout=60)
(w/'TEAM_READ_RECEIPT.json').write_text(json.dumps({'returncode':read.returncode,'stdout':read.stdout,'stderr':read.stderr},ensure_ascii=False,indent=2),encoding='utf-8')
print('Draft submitted; new mathematical results unreviewed; named peer review requests recorded.')
(w/'STATUS.md').write_text('STATE: WORKING\nNEXT: Record final handoff receipts and set NEEDS_REVIEW for w539/supervisor; do not ingest or promote the drafts.\n\n2026-10-10: Completed mathematical packet and measured warning proposal. Patch and schema validation pass; three existing cross-links resolve. Submitted concept DRAFT atomically under scoped mesh claim; peer review requests recorded. Reviewed/ingested/retrievable remain false; P0309 not proved; w537 C1-C5 audited; its full-law Riesz input remains open.\n',encoding='utf-8')
