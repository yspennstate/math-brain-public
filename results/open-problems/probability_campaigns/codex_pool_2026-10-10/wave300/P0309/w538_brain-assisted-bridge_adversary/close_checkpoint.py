import json,pathlib,subprocess
w=pathlib.Path('~/brain_workers/w538')
coverage=json.loads((w/'PEER_COVERAGE.json').read_text(encoding='utf-8'))
coverage['blind_checkpoint_scope']='O1/B1 independent checkpoint predates paired proof access.'
coverage['c5_rederivation_blind']=False
coverage['statement_only_messages_timing']='w537 statement-only messages were read in the final team receipt after ATTEMPT.md C1-C5 had already been read. C5 is a separate adversarial proof check, not a blind statement-only derivation.'
(w/'PEER_COVERAGE.json').write_text(json.dumps(coverage,indent=2),encoding='utf-8')
for name in ['PAIRED_AUDIT.md','REVIEW_PACKET.md','REPORT.md']:
 with (w/name).open('a',encoding='utf-8') as f:f.write('\nProvenance: the initial O1/B1 checkpoint preceded access to w537. The separate C5 derivation followed reading the paired proof; it is not a blind statement-only check. Final mathematical referee review remains pending.\n')
ss=json.loads((w/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
assert ss['states']=={'submitted':True,'reviewed':False,'ingested':False,'retrievable':False}
ss['response_side_served_model_evidence']={'author':'UNKNOWN; no response-side served-model receipt available','referee':'UNKNOWN; review and served-model evidence pending'}
ss['integration_contact_from_team_notice']='codex-01a12190; local INTEGRATION_HANDOFF.json prepared, no extra recipient messaged'
(w/'SOURCE_STATUS.json').write_text(json.dumps(ss,ensure_ascii=False,indent=2),encoding='utf-8')
(w/'INTEGRATION_HANDOFF.json').write_text(json.dumps({'integration_contact':'codex-01a12190','author':'w538','target':'P0309','packet':str(w/'REVIEW_PACKET.md'),'audit':str(w/'PAIRED_AUDIT.md'),'claims':str(w/'CLAIMS.jsonl'),'bundle':ss['draft_submission_path'],'edges':str(w/'DRAFT_EDGES.jsonl'),'paired_source_sha256':coverage['source_sha256'],'scoped_verdict':'KEEP_CONDITIONAL for w537 C1-C5; new B1/O1-O4 still pending w539','remaining_gap':'Subexponential full-Riesz crystal-region mass, law transfer, local tightness/UI and Gibbs closure; no crystal identification','states':ss['states'],'served_model_evidence':ss['response_side_served_model_evidence'],'no_parent_problem_solved_claim':True},ensure_ascii=False,indent=2),encoding='utf-8')
body='Provenance for the completed P0309 audit: your statement-only messages were read after your ATTEMPT C1-C5. My O1/B1 checkpoint predates that proof, but the C5 re-derivation is not blind. KEEP_CONDITIONAL under the written full-law premises; clarify that C3 uses a bounded fundamental cell. O3/O4 and proof details are saved in ~/brain_workers/w538/PAIRED_AUDIT.md; w539 check pending.'
mesh='~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
r=subprocess.run(['python','-X','utf8',mesh,'send','--agent','w538','--to','w537','--topic','probability-P0309-w538-bridge','--kind','answer','--body',body,'--idempotency-key','w538-p0309-audit-provenance-20261010'],capture_output=True,text=True,encoding='utf-8',timeout=60)
(w/'AUDIT_REPLY_RECEIPT.json').write_text(json.dumps({'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr},indent=2),encoding='utf-8')
print('Audit reply:',r.returncode)
r=subprocess.run(['python','-X','utf8',mesh,'release','--agent','w538','--all'],capture_output=True,text=True,encoding='utf-8',timeout=60)
(w/'CLAIM_RELEASE_RECEIPT.json').write_text(json.dumps({'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr},indent=2),encoding='utf-8')
print('Scoped claim release:',r.returncode)
(w/'STATUS.md').write_text('STATE: NEEDS_REVIEW\nNEXT: w539 independently check O3/O4, B1 and the C5 derivation; then prove a zero-exponential-cost bound for a controlled crystal region under the unrestricted Riesz law.\n\n2026-10-10: Completed ten result rows S1.1-S1.10, independent derivation/obstructions, exact source recovery, and paired C1-C5 adversary audit (KEEP_CONDITIONAL). Submitted eight-entry/nine-edge concept DRAFT atomically under a scoped claim. Reviewer w539 and paired prover w537 notified; own claims released.\n2026-10-10: Real recall had 0/3 gas-relevant hits; warning replay flags 3/3 product-only hits with 5/5 silent controls. Fresh gate and 38,860 small spectral terms: 0.316454 s; matrix-vs-gap loss 552.23 at 63^3. Corrected LF patch check/apply/content checks pass. No live math-store mutation or recall-code deployment.\n2026-10-10: O3 refutes finite full-space Riesz convexity; O4 refutes substituting a conditional circular Bragg moment for the full-law C5 input. P0309 not proved; current openness UNKNOWN. New results unreviewed; submitted=true, reviewed/ingested/retrievable=false. C5 check was not blind; O1/B1 independent checkpoint was. Exact packet and integration routing are on disk; global hook/progress rows staged locally under the write restriction.\n',encoding='utf-8')
print((w/'STATUS.md').read_text(encoding='utf-8').splitlines()[0])
