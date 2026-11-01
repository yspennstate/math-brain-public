from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

run=Path(__file__).resolve().parents[1]
own=run.parents[1]; team=own.parents[1]
campaign=Path(r'math-open-problems/reports\fei-2026-10-11')
supplement=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
now=datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,t):
    assert p.resolve().is_relative_to(own.resolve())
    with p.open('w',encoding='utf-8',newline='') as f:f.write(t)
def save(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
result=json.loads((run/'out/CHECK.json').read_text(encoding='utf-8'))
assert result['status']=='PASS' and result['assertions']==5731 and result['policies']==72
assert result['checker_sha256']==sha(run/'code/check.py')
assert result['elapsed_seconds']<60
assert result['witnesses'][-1]['reference_independent_lower_bill']=='9'
formal=(run/'out/LEAN.txt').read_text(encoding='utf-8')
assert 'SETUP_UNVERIFIED' in formal and 'no new compiler process' in formal
protocol=json.loads((campaign/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
a004=team/'agents/A004/runs/20261022T220858Z-fleet03-A004-constant-and-unit-ledger/CLAIMS.json'
source_claims=json.loads(a004.read_text(encoding='utf-8'))
target=next(x for x in source_claims if x['claim_id']=='A004-SHARP-REFERENCE-RESET-AND-SAME-BANK-FRONTIER')
dependency={'claim_id':target['claim_id'],'version':target['version'],'source':str(a004),'source_file_sha256':sha(a004),'declared_statement_sha256':target['statement_sha256'],'observed_UTF8_statement_sha256':hashlib.sha256(target['exact_statement'].encode('utf-8')).hexdigest(),'scope':'Abstract sharp cap and stated neutral one-frontier payment independently reconstructed; no canonical substitution'}
prior=own/'runs/20261021T175538Z-fleet03-A090-independent-reconstruction/REPORT.md'
source_list=[]
def source(p,scope):source_list.append({'path':str(p),'sha256':sha(p),'review_scope':scope})
source(campaign/'EXECUTION_PROTOCOL.json','Read in full; current user endpoint overrides old date')
source(team/'BOARD.md','Current target handoffs; extracted lines for A001/A004/A081/A086/A090/A094/A096/A097/A098/A099')
source(team/'claude/B18/STREAM_NOTES.md','Read in full; old census not resumed instead of productive reset gap')
source(a004,'Full two theorem statements; no producer derivation/checker used')
for a,stage in [('A094','20261022T230414Z-fleet03-A094-proof-chain-challenger'),('A096','20261021T210221Z-fleet03-A096-live-gap-ledger'),('A097','20261021T232544Z-fleet03-A097-cross-route-transfer'),('A099','20261022T231100Z-fleet03-A099-candidate-assembly')]:
    source(team/'agents'/a/'runs'/stage/'CLAIMS.json','Theorem-statement intake for next canonical-reset obligation, not independent acceptance of full chain')
source(supplement/'sources/ERASURE_REDUCTION.md','Section1 physical restriction definitions and channel identity read directly')
source(prior,'Previously reconstructed no-reset telescope and exact neutral root entropy, reused as checked baseline')
save(run/'SOURCE_RECEIPTS.json',{'saved_at':now,'sources':source_list,'reviewed_statement':target,'warning':'Byte hashes do not certify mathematical correctness or review of uninspected sections.'})
common={'version':1,'contributors':['A090'],'proof_source':{'path':str(run/'REPORT.md'),'checker':str(run/'code/check.py'),'certificate':str(run/'out/CHECK.json')},'proof_dependencies':[],'review_records':[],'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A004','A001','A086','A094','A096','A097','A099','B18','B20']}
def claim(cid,statement,**fields):
    c=dict(common,claim_id=cid,exact_statement=statement,statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest()); c.update(fields);return c
claims=[claim('A090-A004-SHARP-RESET-INDEPENDENT-RECONSTRUCTION',
 'For every finite actual Boolean physical restriction with normalized finite-cost incoming R, B_i+avg CE(P_child,R_minus_i)=CE(P,R)-c_i with conditional occupancy KL c_i>=0. Every signed reset costs exactly sum P log2(r/Q). For fixed normalized r,Q its sharp maximum over Boolean laws P<<r is log2 max_(r(T)>0)r(T)/Q(T), attained by a character and infinite when Q vanishes at a positive r atom. Thus Q>=alpha r on actual support caps the reset by log2(1/alpha). The A004 specified neutral AND3/Maj3 one-frontier smoothed reset fits its original quota3 with >363150/10^6 remaining and full terminals retained. These conclusions independently reconstruct A004@1 unchanged; an independently prescribed canonical reset still needs its own signed cost or domination.',
 hypotheses=['Uniform actual finite Boolean signs; logs bits, ordinary influence','Complete normalized references, P<<r, full empty/reference-only support retained','Fixed r,Q while maximizing over Boolean character test laws','Named nine-bit fixture and incoming matching reference for numeric application only'],
 proof_dependencies=[dependency],status='INDEPENDENT_RECONSTRUCTION_HOLDS_AT_SOURCE_SCOPE',
 review_records=[{'reviewer':'A090','timestamp':now,'verdict':'HOLDS for full source statement, no repair','producer_derivation_used':False,'independent_method':'Statement-only expansion of CE/KL; character saturation; own physical truth tables/Walsh and interval checker'}]),
 claim('A090-TWO-CONTROLLED-RESET-ANCESTOR-BANK',
 'For any finite adaptive Boolean query tree starting at a supplied paid reference, if each reset satisfies Q_new>=alpha_v Q_old on true support, total executed erasure plus expected full terminal CE is at most original CE plus E_path sum_resets log2(1/alpha_v). For the nine-bit neutral six-data-bit AND3 point edit by Maj3, initial reference P_F and original core quota3, at most two 7/8-dominated resets per path yield total bill<=H(F)+2log2(8/7)<3-170505/10^6, retaining all prior executed charges inside this account and both full terminal KL debts. In particular two full frontiers Q_new=7Q_old/8+U/8 are paid; arbitrary later no-reset continuation preserves the bound. This does not admit unrelated old charges, arbitrary incoming root references or arbitrary prescribed fresh floors.',
 hypotheses=['Finite physical adaptive tree, fresh coordinates, both fair outcomes retained','Supplied initial paid CE; domination applied against actual incoming already-reset reference','At most two resets per path and matching initial P_F for fixture application','Original quota3, no renewed descendant account, no additional unbooked debit'],
 proof_dependencies=[dependency,{'source':str(prior),'source_sha256':sha(prior),'scope':'Exact root entropy and original quota already independently reconstructed'}],
 status='AUTHOR_PROOF_AND_EXACT_CERTIFICATE_PENDING_INDEPENDENT_REVIEW',review_records=[{'reviewer':'A004/A094','verdict':'PENDING; A090 contributes this corollary'}]),
 claim('A090-NONFLAT-PRESCRIBED-RESET-OBSTRUCTION',
 'Let f=Maj5 with I(f)=15/8, initial matching reference P_f, and query physical bit0 with influence3/8. Both children are nonconstant with the same full-support nonflat spectrum r: six atoms9/64 including empty, ten atoms1/64. The query erasure and conditional KL refund both vanish. Reset only one fair child to the prescribed normalized full-support nonflat Q_m with empty mass2^-m and each other mass(1-2^-m)/15; retain the complete inherited r in the complementary child. The entire ledger L_m=[CE(r,Q_m)+H(r)]/2>=9m/128, so L_128>=9>15/2=4I(f), and L_m/I(f)>=3m/80. Arbitrary prescribed fresh-reference payment at a fixed original rate is therefore false even with positive query influence, both children nonconstant and both actual spectra full-support/nonflat. The Boolean function is fixed and only the imposed reference varies; this is not an FEI counterexample or a refutation of the source dominated-reset theorem.',
 hypotheses=['Specified actual five-bit Boolean majority and true initial matching reference','One physical query, both fair children and their full CE retained','Prescribed reference parameter integer m>=1, fixed before sampling','Only one child reset; no source entropy or complementary terminal discarded'],
 proof_dependencies=[],status='EXACT_BOOLEAN_REFERENCE_COST_OBSTRUCTION_PENDING_REVIEW',
 refutes=['Full support, non-flatness and nonconstant children alone guarantee payment for any independently prescribed reset from a fixed original O(I) quota'],
 review_records=[{'reviewer':'A004/A094','verdict':'PENDING; finite fixtures and all-m lower bound independently reproducible'}])]
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
save(run/'CLAIMS.json',claims)
next_action='A097/A099 supply one actual prescribed canonical floor after a dummy-data or off-branch query, its actual inherited reference, old active/control reset debit and both terminals; pay exact weighted reset excess from SAME remaining ancestor envelope. A004/A094 review the two-reset corollary and Maj5 guard.'
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B18','packet_id':'A090','gap_id':'C019-C024-PAID-FRESH-FLOOR-ADMISSION','attempt_id':'A090-stage7-sharp-reset-independent-reconstruction','method':'Statement-only proof reconstruction; exact normalized references and signed ledger; independent physical truth tables/Walsh; rational log intervals and character saturation','mathematical_delta':'A004 full reset theorem independently HOLDS. SAME fixture quota3 pays two dominated resets per path with >170505/10^6 margin. Fixed Maj5/full-support nonflat children refute arbitrary prescribed reset payment; L_128>=9>4I=15/2. No universal FEI constant or arbitrary canonical-floor admission.','deliverable_status':'COMPLETE_LOCAL_SCHEMA_AND_READBACK_VERIFIED','mathematical_status':'FULL_FEI_OPEN_SCOPED_SOURCE_ACCEPTED_TWO_COROLLARIES_PENDING_REVIEW','claim_versions_used':[dependency,{'source':str(prior),'sha256':sha(prior)}],'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':1,'status':c['status']} for c in claims],'source_artifacts':[str(run/x) for x in ['REPORT.md','CLAIMS.json','SOURCE_RECEIPTS.json','code/check.py','out/FROZEN_SPEC.json','out/CHECK.json','out/LEAN.txt']],'next_consumers':common['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Universal canonical-reset payment under actual remaining source budget unproved','Independent acceptance of A090 corollary/guard pending','Formal SETUP_UNVERIFIED; helper compute admission held, no compiler launched','Supervisor GitHub/brain adoption unverified; initial checklist working update shared-lock failure'],'packet_ids':['A090']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
save(run/'PROGRESS.json',progress);save(run/'PACKET_DELTA.json',progress)
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
write(own/'STATUS.md','STATE: Stage7 saved: A004 sharp reset independently HOLDS; SAME fixture quota3 pays TWO controlled reset frontiers, reserve>170505/10^6; Maj5 full-support/nonflat arbitrary-reset obstruction L128>=9>4I;5731 exact assertions PASS;FEI OPEN.\nNEXT: A097/A099 expose actual canonical dummy/off-branch reset with SAME remaining reference/bank and old debit; A004/A094 review two-reset corollary and Maj5 guard; formal check held by compute admission.\n')
notes=[('WORKLOG.md',f'\n{now} — Stage7: independently reconstructed A004 full sharp-reset statement without producer derivation. Exact5731 assertions, all72 ordered two-query/reset policies and5 Maj5 reference fixtures PASS in{result["elapsed_seconds"]:.3f}s. SAME quota3 leaves>0.170505 after two controlled reset frontiers (previous no-reset0.555796 minus two log2(8/7) costs). Maj5 has two nonconstant full-support/nonflat children and one prescribed reset L128>=9>4I=7.5; guard only, not FEI counterfamily. memok0 but formal helper SETUP_UNVERIFIED, no compiler. Initial checklist update failed shared lock. NEXT: {next_action}\n'),('LEARNED.md','\nStage7 durable fact: exact reset e=E_P log2(r/Q); for fixed normalized r,Q the maximum over Boolean squared laws P<<r equals log2 max r/Q, attained by an actual character. Thus supportwise domination is necessary and sufficient for a uniform cap over all those laws, although an actual node can use its weighted signed cost. With at most k dominated resets per adaptive path, the same ancestor pays original CE+k log2(1/alpha); no fresh bank is needed. On neutral AND3/Maj3, two alpha7/8 resets leave>170505/10^6 of quota3. Full-support/nonflat references alone do not suffice: Maj5 query0 has Inf3/8, B=refund=0, identical child spectra six9/64+ten1/64, both nonconstant. One fair child reset with Q(empty)=2^-m, others equal, while sibling retains full r costs Lm>=9m/128; m128 already exceeds fixed4I. This varies references on a fixed function, not H/I and not FEI. Formal compiler admission hold is UNVERIFIED, never a pass.\n')]
for name,t in notes:
    with (own/name).open('a',encoding='utf-8',newline='') as f:f.write(t)
report=(run/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
assert len((own/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert 8**10<2**2*7**10 and 489+80<600
validation={'saved_at':now,'status':'EXACT_CHECKER_AND_LOCAL_PROTOCOL_READBACK_PASS','assertions':5731,'domain':'72 ordered two-query/reset histories;5 fixed Maj5 references;16 character masks each','rung':'Direct mathematical proof and exact rational certificates; independent source acceptance; new corollary/obstruction review pending','formal_status':'SETUP_UNVERIFIED; memok exit0, further helper compute gate held; no compiler process launched','formal_target_verified':False,'source_acceptance':'A004@1 full statement independently reconstructed without repair','full_fei':'OPEN','research_writes':'A090 only; no git/shared research/brain store modifications','remote_adoption':'UNVERIFIED'}
save(run/'FINAL_VALIDATION.json',validation)
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(run/'out/ARTIFACT_RECEIPTS.json',{'saved_at':now,'status':'LOCAL_READBACK_PASS','artifacts':receipts,'remote_adoption':'UNVERIFIED'})
print(json.dumps({'status':'LOCAL_COMPLETE','claims':len(claims),'artifacts_hashed':len(receipts),'assertions':5731,'formal':'SETUP_UNVERIFIED','run':str(run)},indent=2))
