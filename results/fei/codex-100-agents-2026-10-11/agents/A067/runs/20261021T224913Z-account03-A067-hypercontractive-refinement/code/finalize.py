from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parent.parent
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
cid='A067-POSTCORE-BENT-FLAG-SAME-CHILD-BANK'
statement='For every integer m>=2, let b_m(Y)=(-1)^(sum_j Y_(2j-1)Y_(2j)) on 2m bits, G_m(w,Y,z)=b_m(Y)+1{w=0,Y=0}(z-1), c_m=b_m-2*1{w=0,Y=0}, and delta=2^(-(2m+1)). In bits, with both actual z terminals retained, D_z=H(G_m)-(H(b_m)+H(c_m))/2=B_z+JS_z and S_2=(2I(b_m)-H(b_m)+2I(c_m)-H(c_m))/2 satisfy S_2-D_z>delta/4. In particular both terminals and G_m satisfy H<=2I. For every C>=2 the same payment holds with S_C, including any independent spectator q with available H(q)<=C I(q), retaining its full terminal entropy. No assertion about arbitrary cores or already debited ancestor banks is made.'
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':['Uniform finite Boolean signs; actual specified quadratic bent phase and marked all-zero vertex','m>=2; full core Fourier label including w; both actual terminals retained','Spectator extension requires actual unused C-certified independent spectator; no reset of an inherited bank'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['account03/A067; A088 credited for physical post-core obstruction family'],'proof_source':str(R/'DERIVATION.md'),'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROOF_WITH_EXACT_BOUNDARY_CERTIFICATES_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A088','A070','A094','A096','B14','B20']}
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B14','packet_id':'A067','gap_id':'G-R-MISMATCH-POSTCORE-UNUSED-CHILD-RESERVE','attempt_id':'A067-stage17-same-C2-bent-flag-bank','method':'Exact actual-child-bank cancellation, four-cell entropy bound, rational boundary certificates and independent integer Walsh/physical edges','mathematical_delta':'Entire flag plus channel paid from actual C2 edited-child surplus on A088 post-core G_m for all m>=2; residual>delta/4; no fresh query allowance. Arbitrary inherited history bank remains open.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_ANALYTIC_PROOF_PENDING_REVIEW_FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':[cid+'@1'],'source_artifacts':['DERIVATION.md','REPORT.md','FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/SOURCE_RECEIPTS.json','out/LEAN.json'],'next_consumers':['A088','A070','A094','A096','B14','B20'],'next_action':'Carry SAME residual through one more actual Y query, keeping incoming terminal references and booked z debit; independent A088/A070/A094 reconstruction.','stagnant_substantive_attempts':0,'blockers':['Full FEI unresolved','Independent review and supervisor adoption unverified','Lean compiler not started: fresh memok exits1, commit free5.5GB below8GB threshold'],'packet_ids':['A067']}
wantclaim=set(protocol['required_per_run']['claim_fields']);wantprog={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(claim)==wantclaim,(set(claim)^wantclaim)
assert set(progress)==wantprog,(set(progress)^wantprog)
(R/'CLAIMS.json').write_text(json.dumps([claim],indent=2)+'\n',encoding='utf-8')
blob=json.dumps(progress,indent=2)+'\n'
for n in ('PROGRESS.json','PACKET_DELTA.json'):(R/n).write_text(blob,encoding='utf-8')
note='\n## 2026-10-22 stage17 (account03; scheduled run 20261021T224913Z)\nA088 post-core G_m: entire conditional flag+channel D_z paid from SAME actual C2 terminal bank, residual>delta/4 for all m>=2. Four-cell entropy proof m>=4, exact rational m2/m3 boundaries; direct Walsh and physical edges retain BOTH terminals. No fresh 2I_X reserve; clean bent child has zero bank. A096 lossy-quotient price-five obstruction unaffected. Formal algebra compiler blocked by fresh memok exit1 (commit free5.5GB<8GB), not a Lean certificate. Independent review/full FEI remain open. NEXT: carry unchanged source/reference and old z debit through one more Y query; do not renew bank.\n'
for name in ('WORKLOG.md','LEARNED.md'):
    with (A/name).open('a',encoding='utf-8') as f:f.write(note)
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
report=(R/'REPORT.md').read_text(encoding='utf-8').replace('98 exact assertions pass in 0.089 seconds','99 exact assertions pass; actual elapsed time is in out/CHECK.json').replace('Formal checking is attempted only after memok exits0, and does not certify the entropy proof.','Fresh memok exited1: commit free5.5GB was below8GB. The Lean compiler was not started; out/LEAN.json records the blocker, not a certificate.')
(R/'REPORT.md').write_text(report,encoding='utf-8')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
receipts=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        b=p.read_bytes();assert len(b)<20*1024*1024
        receipts.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
receipt={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'schema_exact':True,'progress_delta_byte_identical':True,'status_two_lines':True,'all_files_under_20MB':True,'compiler_started':False,'artifacts':receipts}
(R/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'SAVED_AND_READ_BACK','claims':1,'artifacts':len(receipts),'run':str(R)}))
