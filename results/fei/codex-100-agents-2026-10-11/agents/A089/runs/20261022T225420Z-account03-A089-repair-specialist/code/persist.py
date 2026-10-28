"""Protocol persistence and final source/receipt checks; no shared writes."""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];OWNER=Path(r'~')
def put(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def js(p,v):put(p,json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def main():
    protocol=OWNER/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json';p=read(protocol)
    prior=A/'runs/20261021T154748Z-account03-A089-repair-specialist'
    peerroot=OWNER/'brain_workers/FEI100_20261011/agents'
    peerpaths=[peerroot/'A071/runs/20261021T200238Z-account03-A071-search-space-design/REPORT.md',peerroot/'A072/runs/20261021T225156Z-account03-A072-exact-walsh-engine/REPORT.md',peerroot/'A075/runs/20261021T173628Z-account03-A075-search-to-theorem-bridge/REPORT.md',peerroot/'A075/runs/20261021T173628Z-account03-A075-search-to-theorem-bridge/CLAIMS.json']
    sources=[protocol,prior/'REPORT.md',prior/'CLAIMS.json',prior/'out/REPAIRED_CASES.json',prior/'out/THIRD_QUERY_CASES.json']+peerpaths
    sources +=[OWNER/'brain_workers/FEI100_20261011/BOARD.md',OWNER/'brain_workers/FEI100_20261011/claude/B18/STREAM_NOTES.md']
    sources +=[R/'code'/n for n in ['arithmetic.py','check.py','third_query.py','mixed.py','saturation.py','coupled.py','reproduce.py']]
    js(R/'out/SOURCE_INVENTORY.json',[{'path':str(s),'bytes':s.stat().st_size,'sha256':sha(s),'scope':'primary definitions/account or exact coordination source; no unreviewed universal premise'} for s in sources])
    js(R/'out/A075_REVIEW_SOURCE.json',{'path':str(peerpaths[-1]),'sha256':sha(peerpaths[-1]),'source_claims':read(peerpaths[-1]),'accepted_scope_only':'unchanged prior A089-CORRECTED-CAPACITY-SIBLING-TRANSFER@1; not new signed-terminal theorem'})
    sat=read(R/'out/SATURATION_SUMMARY.json');coupled=read(R/'out/COUPLED_VALIDATION.json');repro=read(R/'out/INDEPENDENT_REPRODUCTION.json')
    assert sat['labelled_states']==repro['states']==18 and sat['negative_states']==2
    assert coupled['physical_cases']==4 and coupled['scalar']['cases']==35 and coupled['parked_reserve_new_draw']=='0'
    assert coupled['failed']==repro['failed']==0
    validation={'saturation':{k:v for k,v in sat.items() if k in ['engine_assertions','explicit_recorded_predicates_including_runtime','runtime_seconds','labelled_states','negative_states']},'coupled':coupled,'independent_reproduction':{k:v for k,v in repro.items() if k!='cases'},'counts_are_per_job':'engine totals overlap across primary jobs; no grand total claimed','all_jobs_under55_seconds':all(x['runtime_seconds']<55 for x in [sat,coupled,repro])}
    assert validation['all_jobs_under55_seconds'];js(R/'out/VALIDATION_SUMMARY.json',validation)
    failures={'false_statement':'After twice-saturated continuation every full child from finishing block0 active bits4,5 has S4>=0.','actual_Boolean_witnesses':'J(-1, g|x0=b, g,g,g,g), b=0,1, with the inherited prefix and30 ambient physical bits','scope':'proposed extension of eligibility, not a theorem of A071/A072; not a counterexample to full FEI','exact_certificates':'SATURATION_STATES.json and INDEPENDENT_REPRODUCTION.json','repaired_by':'COUPLED_CASES.json: gross minimum transfer N=E(-S)_+, positive final sibling pays; old parked2tau untouched'}
    js(R/'out/FAILED_STATEMENT.json',failures)
    lean={'status':'SETUP_UNVERIFIED','actual_output':'Compute admission held (hung window or under5500 MB free); no new compiler process','core_only':True,'attempted_statement':'example (a b d e : Int) (h : 2 * (d + e) = b - a) : b - a - 2 * d - 2 * e = 0 := by omega','no_retry':True,'rung':'written proof and exact finite certificates; no Lean certification','translation_limit':'Even a future integer identity check would not certify the real-valued capacity theorem or Fourier proof.'}
    js(R/'out/LEAN_ATTEMPT.json',lean)
    statement='For finite weights w_b>=0 summing to1, signed real capacities s_b and a required nonnegative net debit T, nonnegative d_b and zero-mean transfers f_b with mean d=T and s_b+f_b-d_b>=0 exist iff T<=mean s. Writing P=E(s)_+, N=E(-s)_+, their minimum gross incoming transfer E(f)_+ is N. For P>0, k=(s)_+/P, d=T k, f=(-s)_+-N k attain it and transport every signed ancestor/new label L as L k, including T=0; P=0 has the stated zero-net boundary. On the actual twice-saturated J(g^6) history (block0 bits2,0,3 all0 then block1 bit0=b), all18 restrictions of block0 bits4,5 have exactly2 negative full S4 endpoints; both orders for each b admit this coupled payment at unchanged4, preserving all old labels and drawing zero from the old parked2tau reserve. Negative subsidies A_b lie in(55/1000,56/1000) and(45/1000,46/1000). No universal FEI bound.'
    cid='A089-SIGNED-TERMINAL-COMMON-KERNEL-REPAIR'
    claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':['finite weights and real signed capacities, nonnegative net booked debit, zero-mean allowed transfers','for the application: exact declared disjoint Boolean cores, uniform physical coordinates, entropy bits, unchanged inherited saturation labels','all capacities and physical profiles supplied explicitly; no assumption of universal parent FEI'],
      'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A089'],
      'proof_source':['REPORT.md sharp signed-capacity replacement and actual transfers','out/COUPLED_CASES.json','out/INDEPENDENT_REPRODUCTION.json','out/VALIDATION_SUMMARY.json'],
      'proof_dependencies':[{'path':str(prior/'REPORT.md'),'sha256':sha(prior/'REPORT.md'),'scope':'explicit prefix and old2tau; reconstructed locally'},{'path':str(peerpaths[1]),'sha256':sha(peerpaths[1]),'scope':'saturation optimizer as coordination; reconstructed physical identity used'}],
      'review_records':[{'reviewer':'A089 separate product-moment representation','independent_reviewer':False,'scope':'all18 full H/I/S states and two negative endpoint signs','verdict':'INTERNAL_REPRODUCTION_PASS_EXTERNAL_REVIEW_PENDING'}],
      'status':'SOURCE_COMPLETE_REVIEW_PENDING','supersedes':[],
      'refutes':['proposed twice-saturated full-child-positivity inheritance at rate4; not A071/A072 scoped previous theorems'],
      'first_unproved_line':'Derive aggregate terminal eligibility from Boolean signed component information on arbitrary inherited histories; actual next data query must carry A already received and donor A already spent.',
      'next_consumers':['A071','A072','A074','A075','A092']}
    assert set(claim)==set(p['required_per_run']['claim_fields']);js(R/'CLAIMS.json',[claim])
    progress={'protocol_revision':p['revision'],'run_id':R.name,'stream':'B18','packet_id':'A089','gap_id':'G-R-MISMATCH','attempt_id':'A089-stage7-signed-negative-terminal-repair','method':'consume A071/A072 completion and A075 review; exact negative-child test; sharp finite signed-flow construction and independent centered-moment reproduction',
      'mathematical_delta':'Twice-saturated child positivity is false:2 negative full S4 endpoints among18 restrictions. Sharp signed-capacity common-kernel repair pays both orders in both anchors, retains old labels at T=0, and needs no extra parked2tau draw. Gross flow across both anchors lies in(1/640,51/32000).',
      'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_PROOF_AND_EXACT_CERTIFICATES_REVIEW_PENDING_FULL_FEI_OPEN',
      'claim_versions_used':[{'source':str(prior/'CLAIMS.json'),'sha256':sha(prior/'CLAIMS.json'),'scope':'A089 corrected-capacity theorem; A075 independent acceptance consumed'},{'source':str(peerpaths[1]),'sha256':sha(peerpaths[1]),'scope':'saturation identity rederived'}],
      'claims_created_or_changed':[{'claim_id':cid,'version':1}],
      'source_artifacts':['REPORT.md','out/SATURATION_STATES.json','out/COUPLED_CASES.json','out/INDEPENDENT_REPRODUCTION.json','out/A075_REVIEW_SOURCE.json'],
      'next_consumers':['A071','A072','A074','A075','A092'],
      'next_action':'Query actual core1 data in the negative terminal with inherited subsidyA; preserve donor outgoingA, all old labels and complete terminal profiles; derive signed row eligibility without a fresh bank.',
      'stagnant_substantive_attempts':0,'blockers':['arbitrary-core aggregate terminal admission unpaid','new independent acceptance and supervisor mirror pending','Lean setup admission held; no compiler or formal certification'],
      'packet_ids':['A089']}
    if (R/'out/CHECKLIST_SAVE_BLOCKER.json').exists():progress['blockers'].append('Task completion checklist receipt unverified: lock held too long; local research persistence unaffected')
    expected={x.split(' (')[0] for x in p['required_per_run']['progress_fields']};assert set(progress)==expected
    js(R/'PROGRESS.json',progress);js(R/'PACKET_DELTA.json',progress)
    status='STATE: A089 stage7 complete locally:2 negative full K4 terminals refute twice-saturated positivity; sharp signed common-kernel transfer pays4 policies, all18 states independently reproduced; parked2tau untouched; review pending; FEI OPEN.\nNEXT: Query core1 data in negative terminal carrying incomingA and donorA already spent, both full terminals and old labels; A072/A074/A092 review; no fresh bank.\n'
    put(A/'STATUS.md',status)
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    work='\n'+now+' '+R.name+': board A071/A072 already closed spent-sibling60 cases; unexecuted30-case spec retired. Consumed A075 independent acceptance of stage6. Tested18 twice-saturated core0 restrictions:2 actual negative full S4 endpoints, approx-0.0552712 and-0.0451253. Proved sharp signed-capacity common-kernel theorem, min gross transfer E(-S)_+, T=0 safe; four physical policies pay from own positive sibling, no added parked2tau draw. Independent direct product-moment18-state reproduction PASS; scalar35 cases/245 exact predicates. Core-only Lean SETUP_UNVERIFIED before compiler; no retry. Protocol files and receipts saved; new external review pending; FEI OPEN.\n'
    lesson='\n'+now+' '+R.name+': Saturation does not preserve full child S4>=0. In J(g^6), after block0 bits2=0,0=0,3=0 then block1 bit0=b, finish block0 bits4=5=0: actual full S4 is in(-.056,-.055) for b0 and(-.046,-.045) for b1. Correct finite signed-capacity payment: with P=E(s)_+,N=E(-s)_+,T>=0, feasible iffT<=P-N; minimum mean positive transferN, achieved by k=(s)_+/P,d=T k,f=(-s)_+-N k. Every signed old/new labelL maps toLk, includingT0; handleP0 without division. Nonnegative NET debit is essential (allowing d=s at s=(-1,1),T0 removes need for any transfer). Actual last-query kernel(0,2), negative subsidyA is paid by positive sibling; old parked2tau account unchanged. Generic lemma spends supplied full capacities and is not a universal FEI admission theorem.\n'
    for path,text in [(A/'WORKLOG.md',work),(A/'LEARNED.md',lesson)]:
        current=path.read_text(encoding='utf-8-sig')
        if R.name not in current:
            with path.open('a',encoding='utf-8',newline='\n') as f:f.write(text)
    report=(R/'REPORT.md').read_text(encoding='utf-8');assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
    for field in p['required_per_run']['report_fields']:assert '## '+field in report
    assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
    assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
    files=[]
    for path in R.rglob('*'):
        if path.is_file() and path.name!='RECEIPTS.json':
            assert path.stat().st_size<20*1024**2
            files.append({'path':str(path.relative_to(R)),'bytes':path.stat().st_size,'sha256':sha(path)})
    receipts={'run_id':R.name,'saved_at_utc':now,'exact_protocol_fields':'PASS','delta_identical':True,'status_two_lines':True,
      'validation':'18 states,2 negative endpoints,4 coupled policies,35 scalar cases, independent18-state product-moment reproduction PASS',
      'new_independent_acceptance':'PENDING','old_A089_review':'A075 acceptance consumed','mirror':'SUPERVISOR_OWNED_NOT_VERIFIED','files':files}
    js(R/'out/RECEIPTS.json',receipts)
    for f in files:assert sha(R/f['path'])==f['sha256']
    print(json.dumps({'run_files_hashed':len(files),'schemas':'PASS','delta_equal':True,'states':18,'negative_states':2,'physical_policies':4,'scalar':coupled['scalar'],'old_parked_new_draw':'0','full_FEI':'OPEN'}))
if __name__=='__main__':main()
