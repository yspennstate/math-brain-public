from pathlib import Path
import hashlib,json
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parent.parent
AGENT=ROOT.parent.parent
TEAM=AGENT.parent.parent
REPORTROOT=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def sha(b): return hashlib.sha256(b).hexdigest()
def save(name,obj): (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=json.loads((REPORTROOT/'EXECUTION_PROTOCOL.json').read_text())
sourcepaths=[REPORTROOT/'EXECUTION_PROTOCOL.json',TEAM/'BOARD.md',TEAM/'claude/B11/STREAM_NOTES.md',TEAM/'claude/B11/runs/20261011T230100Z-claude-B11-block-descent-recentring/REPORT.md',AGENT/'runs/20261011T214321Z-fleet05-A051-near-extremizer-definition/EXISTENCE_AND_LIMITS.md',AGENT/'runs/20261011T214321Z-fleet05-A051-near-extremizer-definition/CLAIMS.json',TEAM/'agents/A053/runs/20261011T221934Z-fleet05-A053-near-tensor-perturbations/REPORT.md',TEAM/'agents/A080/runs/20261011T231244Z-fleet05-A080-universal-counterexample-standard/FEI_DISPROOF_STANDARD.md']
sources=[]
for p in sourcepaths:
    b=p.read_bytes(); sources.append({'path':str(p),'sha256':sha(b),'bytes':len(b)})
save('out/SOURCE_MANIFEST.json',{'local_byte_pins':sources,'board_read_snapshot':'2026-10-11 23:29 UTC','lead_revision_read':'B11 v2, 2026-10-11 23:3xZ','external_primary_sources':[{'url':'https://arxiv.org/pdf/1711.00762','locator':'Section1.2, PDF page3, corrected g3/g3-prime/g4/g4-prime Boolean definitions','access':'Web PDF extraction; primary source; no local PDF hash claimed'}],'source_scope':'Definitions and universal bridge scope inspected; no latest literature bound or full paper audit asserted','brain_writes':False,'remote_mirror_verified':False})

statement1=('For every actual nonconstant Boolean sign f on the n-bit uniform cube, n>=2, with H in bits and phi=min over nonempty proper physical blocks A with I_A>0 of (H(f)-E H(f_a))/I_A, phi(f)<=H(f)/(I(f)-min_i Inf_i(f))<=n(H(f)/I(f))/(n-1). If M_n=max H/I over all nonconstant n-bit functions and K_desc(n)=max phi over the same finite domain, then M_n<=K_desc(n)<=n M_n/(n-1). Therefore lim_n K_desc(n)=sup_n M_n=C_* in the extended real sense, and bounded universal proper-block descent is equivalent in finiteness to FEI. No all-dimensional optimizer, independent uniform bound, or paid entropy estimate is asserted.')
statement2=('For the full family of 1150 unordered read-once NAND formula trees with no unary internal gate, arbitrary arity>=2, and6..9 disjoint literal leaves, exact orbit certificates cover117240 proper-block orbits representing470340 labelled blocks and certify phi<227/50 for every member. Dimensionwise maxima are certified by the rational intervals in out/AGGREGATE_CERTIFICATES.json. The eight-bit three-level complete binary NAND tree has exactly phi/(H/I)=8/7. Seven explicitly defined Hod corrected six/eight-bit seed and fresh NAND-extension controls also have phi<227/50. These are finite family results, not all Boolean functions, not all recursive lower-bound compositions, and not a universal block payment.')
claims=[]
cid1='A051-PROPER-BLOCK-DESCENT-SQUEEZE'; cid2='A051-NAND-SEED-DESCENT-CERTIFICATES'
for cid,s,file,dep,stat in [(cid1,statement1,'UNIVERSAL_DESCENT_SQUEEZE.md',[],'SOURCE_COMPLETE_ANALYTIC_PROOF_PENDING_INDEPENDENT_REVIEW'),(cid2,statement2,'COMPOSITION_CERTIFICATES.md',[{'claim_id':cid1,'version':1,'use':'Universal comparison and interpretation of exact8/7 finite sharpness'}],'EXACT_FINITE_CERTIFICATES_PENDING_INDEPENDENT_REVIEW')]:
    claims.append({'claim_id':cid,'version':1,'exact_statement':s,'hypotheses':['Actual Boolean signs; uniform physical cube; entropy in bits','n>=2 for universal squeeze; fixed frozen6..9 domain for census','phi uses only nonempty proper blocks with I_A>0; constants never divided by I'],'statement_sha256':sha(s.encode()),'contributors':['fleet05/A051'],'proof_source':{'path':str(ROOT/file),'sha256':sha((ROOT/file).read_bytes()),'certificate':str(ROOT/'out/AGGREGATE_CERTIFICATES.json') if cid==cid2 else None},'proof_dependencies':dep,'review_records':[],'status':stat,'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A052','A053','A055','A090','A094','B11 lead','B20']})
save('CLAIMS.json',claims)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B11','packet_id':'A051','gap_id':'FEI-B11-UNIVERSAL-PROPER-BLOCK-DESCENT','attempt_id':'A051-DESCENT-COMPOSITIONS-1','method':'Universal co-singleton/finite-optimizer squeeze; exhaustive read-once NAND formula and block-orbit certificates; independent physical-child reproduction','mathematical_delta':'Proved M_n<=K_desc(n)<=nM_n/(n-1), so the asymptotic block-descent constant equals C_* and phi/R<=1.33 at n>=4 is automatic. Exact1150-formula6..9 census covers470340 labelled blocks, all phi<4.54;8-bit binary NAND attains phi/R=8/7;7 repeated-variable seed controls also below4.54. Census140692 checks and independent reproduction4927 checks passed. No absolute universal payment obtained.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT_REVIEW_PENDING','mathematical_status':'UNIVERSAL_SUPPORTING_LEMMA_AND_EXACT_FINITE_CERTIFICATES_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':cid1,'version':1,'use':'Finite sharpness interpretation; intra-run acyclic dependency'}],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version']} for c in claims],'source_artifacts':['REPORT.md','UNIVERSAL_DESCENT_SQUEEZE.md','COMPOSITION_CERTIFICATES.md','CLAIMS.json','code/descent_compositions.py','code/check_seeded_and_replay.py','code/aggregate_certificates.py','out/FROZEN_CENSUS.json','out/AGGREGATE_CERTIFICATES.json','out/full_SUMMARY.json','out/SEEDED_FULL_SUMMARY.json','out/SOURCE_MANIFEST.json','out/RECEIPTS.json'],'next_consumers':['A052','A053','A055','A090','A094','B11 lead','B20'],'next_action':'A090/A094 reconstruct squeeze/orbit/log certificates; A052 derive a fixed-K recentred small/pivot-block payment on actual dimension-critical witnesses using beta_A, challenged by saved8/9-bit extrema and repeated-variable seed recursion, with terminal entropy retained.','stagnant_substantive_attempts':0,'blockers':['Independent review and supervisor mirror verification pending','No absolute bound on M_n or K_desc(n); finite NAND census cannot establish universal admission'],'packet_ids':['A051']}
save('PROGRESS.json',progress); save('PACKET_DELTA.json',progress)
(AGENT/'STATUS.md').write_text('STATE: A051 stage2 saved: universal M_n<=K_desc(n)<=nM_n/(n-1);1150 exact6..9 NAND formulas all phi<4.54; sharp8/7 example;140692+4927 checks; new review pending; full FEI OPEN.\nNEXT: A090/A094 review; A052 derive a fixed-K recentred pivot payment on dimension-critical witnesses using beta_A and saved8/9-bit non-point-defect controls; phi/R comparison is automatic.\n',encoding='utf-8')
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
report=(ROOT/'REPORT.md').read_text()
assert all('## '+x in report for x in protocol['required_per_run']['report_fields'])
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
receipts=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        b=p.read_bytes(); assert len(b)<20_000_000
        receipts.append({'path':str(p.relative_to(ROOT)),'sha256':sha(b),'bytes':len(b)})
for name in ('STATUS.md','WORKLOG.md','LEARNED.md'):
    p=AGENT/name; b=p.read_bytes(); receipts.append({'path':str(p),'sha256':sha(b),'bytes':len(b)})
save('out/RECEIPTS.json',{'saved_at':datetime.now(timezone.utc).isoformat(),'local_persistence_only':True,'remote_mirror_verified':False,'independent_acceptance':False,'schema_verified':True,'files':receipts})
print(json.dumps({'status':'SAVED_SCHEMA_AND_SIZE_CHECKED','claims':2,'receipt_files':len(receipts),'claim_fields':len(claims[0]),'progress_fields':len(progress),'max_artifact_bytes':max(r['bytes'] for r in receipts),'total_artifact_bytes':sum(r['bytes'] for r in receipts),'run_directory':str(ROOT)},indent=2))
