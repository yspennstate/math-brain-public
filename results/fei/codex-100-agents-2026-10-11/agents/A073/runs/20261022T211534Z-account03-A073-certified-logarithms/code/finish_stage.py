from pathlib import Path
import subprocess,sys,json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; OWN=RUN.parents[1]
def put(p,s):p.write_text(s,encoding='utf-8')
def js(p,o):put(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
receipts=[]
for pilot in [True,False]:
    args=[sys.executable,'-X','utf8',str(RUN/'code/certify_dummy.py')]+(['--pilot'] if pilot else [])
    p=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',timeout=260,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    put(OUT/('PILOT_STDOUT.txt' if pilot else 'CHECK_STDOUT.txt'),p.stdout)
    put(OUT/('PILOT_STDERR.txt' if pilot else 'CHECK_STDERR.txt'),p.stderr)
    receipts.append({'command':args,'exit_code':p.returncode})
    js(OUT/'COMMAND_RECEIPTS.json',receipts)
    if p.returncode:
        print(p.stderr[-2000:]);raise SystemExit(p.returncode)
result=json.loads((OUT/'RESULT.json').read_text(encoding='utf-8'))
pilot=json.loads((OUT/'PILOT_RESULT.json').read_text(encoding='utf-8'))
assert result['status']==pilot['status']=='PASS'
deps=[]
for agent,oldrun in [('A096','20261021T210221Z-account03-A096-live-gap-ledger'),('A097','20261021T232544Z-account03-A097-cross-route-transfer')]:
    path=OWN.parent/agent/'runs'/oldrun/'CLAIMS.json'
    obj=json.loads(path.read_text(encoding='utf-8-sig'))
    def walk(x):
        if isinstance(x,dict):
            if 'claim_id'in x and 'version'in x:
                deps.append({k:x[k] for k in ['claim_id','version','statement_sha256'] if k in x})
            else:
                for v in x.values():walk(v)
        elif isinstance(x,list):
            for v in x:walk(v)
    walk(obj)
    receipts.append({'source':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
statement=('For every a>=1,b>=0,r>=1 with d=b+r>=2, and every normalized finite-cost source reference R_raw for g=1-2A_a with CE(P_g,R_raw)<=C0 I(g), C0>=0, empty-calibrate the source and use the A097 canonical complete floor. Every adaptive surviving-edited-branch policy consisting of A096 active resets, dummy-data resets to the empty-calibrated source marginal while b>=1, and A097 control resets while r>=2, including the A096 final active point boundary, has booked expected erasure plus all full terminal cross entropy <=(2C0+10)I(F)-12e_root for F=1-2A_a+2A_(a+b+r), e_root=2^(1-a-b-r). Complementary children retain complete inherited references; all old debits remain booked. A dummy step alone costs <W+8e, where W=c+10e(a+b+r). Structural source gives unchanged rate18. No universal source/reference construction is asserted.')
cid='A073-DUMMY-DATA-RESET-SAME-ANCESTOR'
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':['Uniform physical cube; entropy in bits.','Point-source negative-cell edit and supplied finite-cost reference as specified.','Canonical reset only on surviving edited branch; full off terminals retained.','No control reset at r=1; no reset inside retained off-branches.'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A073'],'proof_source':['DERIVATION.md sections1-4','code/certify_dummy.py','out/RESULT.json'],'proof_dependencies':deps,'review_records':[{'reviewer':'A073','kind':'direct character sums plus physical-edge reconstruction and fixed rational log intervals','verdict':'PASS','assertions':result['assertions'],'independent_acceptance':False}],'status':'PROOF_COMPLETE_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':'Generic signed non-point source construction, or prescribed reset in a retained off-branch from the diminished SAME original bank.','next_consumers':['A096','A097','A085','A094','A099','B20']}
js(RUN/'CLAIMS.json',[claim])
counts=result['counts']; nxt='A096/A097 and A085/A094 independently reconstruct dummy marginal/calibration payment; then price one fresh reset in a retained off-branch with the same remaining ancestor bank and old debits.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B15','packet_id':'A073','gap_id':'G-R-MISMATCH','attempt_id':'A073-dummy-source-marginal-reset-v1','method':'Analytic weighted-likelihood comparison; direct integer character sums and Fraction interval certificates.','mathematical_delta':'Dummy-data reset surcharge<8e; all eligible active/dummy/control surviving-branch histories paid at unchanged K=2C0+10 with >=12e_root remaining. Full FEI OPEN.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'PROOF_COMPLETE_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':deps,'claims_created_or_changed':[{'claim_id':cid,'version':1}],'source_artifacts':['DERIVATION.md','code/certify_dummy.py','out/RESULT.json','out/PILOT_RESULT.json','out/source_read_manifest.json'],'next_consumers':claim['next_consumers'],'next_action':nxt,'stagnant_substantive_attempts':0,'blockers':['Independent acceptance and supervisor copy not verified.','Lean admission refused: physical RAM2.2GB<4GB; no Lean certificate.','Wake attachment integrity degraded: lock timeouts; affected notes not used.'],'packet_ids':['A073']}
js(RUN/'PROGRESS.json',progress);js(RUN/'PACKET_DELTA.json',progress)
report=f'''# A073: certified payment for dummy-data resets

## exact target, quantifiers, hypotheses and units

{statement}

## sources actually read, revisions and theorem locators

Execution protocol v2 was read in full; campaign README/status, registries, packet/action indices, plan, supplement and source notes, four paper text exports, previous A073 reports, BOARD2026-10-22 21:16 and B15 notes v2 were consulted. out/source_read_manifest.json pins29 programmatically read sources and their explicit encodings; out/READS.log preserves selected relevant lines. Critical human-read source mathematics: A09620261021T210221Z DERIVATION1--3 and A09720261021T232544Z DERIVATION1--7. Claim versions/hashes are in CLAIMS.json. No paper theorem is a new premise. The stale lead's original 30-digit/cyclic task was already discharged or archived in earlier A073 work; dispatch consumes the new A096/A097 dummy-data gap. Current user endpoint supersedes old static campaign dates. Brain wake returned attachment lock/integrity alerts; they were surfaced and affected notes were not used. No external web source was needed.

## complete derivation or exact first unsupported line

DERIVATION1 proves pointwise source-reference dominance after dummy marginalization and empty calibration. Section2 bounds the full retained off-child likelihood excess by (8+2/ln2)e<11e, even with reference-only mass on the dummy label. Section3 combines actual erasure<12e and both complete terminals into a surcharge<8e. Section4 charges every such step to the SAME original bank: reach*e=e_root and at most d-1 non-active steps cost8(d-1)e_root; the original reserve>=5a*2^d e_root leaves>=12e_root. The original rate18 survives for the structural source. Imported active boundaries retain their precise a=1 point rule. All source-normalizer and likelihood denominators are checked where used. The first unsupported line is generic non-point source pricing or a fresh reset within a retained off-branch from the diminished ancestor account. Rung: analytic proof plus exact finite validation, pending independent review; NOT Lean-checked.

## executed validation with domain, arithmetic, commands and outputs

Frozen pilot and main specs are in out/FROZEN_PILOT.json and out/FROZEN_SPEC.json. Execute python -X utf8 code/finish_stage.py from this run to reproduce the two checks and artifact construction. Checker pilot: {pilot['counts']['roots']} roots, {pilot['counts']['history_nodes']} history nodes, {pilot['assertions']} exact predicates, {pilot['runtime_seconds']:.3f}s. Main: {counts['roots']} roots, {counts['history_nodes']} history nodes, {counts['dummy_steps']} dummy steps, {counts['control_steps']} control steps, {counts['active_steps']} proper active steps and {counts['final_active']} final-active boundaries; {result['assertions']} exact predicates PASS in {result['runtime_seconds']:.3f}s. Domain: a,b,r in{{1,2}}, matching/increasing/dummy-spiked rational references; every eligible type word/stopping prefix, using the least remaining physical label of each type. No assertion of exhaustive asymmetric labelled-order coverage. Direct character sums and physical-edge counts check the Boolean model independently of the analytic coefficients. Full marginals include reference-only atoms. Fixed12-term rational atanh intervals with explicit positive tail settle every requested sign; zero precision refinements. out/DUMMY_ROWS.json gives signed reset costs, booked preceding charges and retained other terminals. The selected nonflat spent-history row has history {result['example_spent_nonflat_dummy_row']['history']}; both physical children are nonconstant. Exact margin: >=12e_root analytically; the minimum certified finite stopping-node remainder/e_root is {result['minimum_certified_remaining_over_root_e']} (a finite-domain value, not a changed universal constant).

Initial pilot a2,b1,r1 failed its requested-fixture coverage guard, predicate527, after local checks; it contained no spent-history nonflat dummy row. out/INITIAL_PILOT_FAILURE.txt preserves that failure and the correction to the nonconstant-parity diagnostic. The revised explicit pilot a2,b1,r2 contains control-then-dummy. This is a fixture correction, not a mathematical counterexample or automatic dimension escalation. Source-cost equality is checked by exact pointwise dominance, not overlapping interval endpoints. memok exited1 (physical2.2GB<4GB); Lean was not launched, and KEY_STEP.lean is only an unexecuted target. Small checker estimate120MB; no GPU, detached job or large search.

## proof dependencies and changed downstream conclusions

Exact imported versions are pinned in CLAIMS.json. A096 supplies the already source-complete active/final-point mechanism; A097 supplies the complete floor and control comparison. This run extends their reset history with dummy-data queries at the unchanged rate, preserving all old debits and both complete terminals. It does not independently accept all imported claims or construct a universal reference. No universal FEI constant improves; FEI remains OPEN. New claim awaits independent A096/A097 or A085/A094 reconstruction.

## one next mathematical action and independent reviewer

{nxt} This replaces the earlier request for an actual nonflat row with a reproducible same-bank certificate; repeating old logarithmic precision is unnecessary.

## actual persistence receipts or precise save blocker

All four protocol files, derivation, code, frozen specs, exact outputs, source receipts, failed-pilot note and unexecuted Lean target are local. out/PERSISTENCE_RECEIPTS.json validates exact JSON field sets, statement hash, identical progress/delta and20MB ceilings. STATUS has two lines; dated WORKLOG and LEARNED updates are saved. No shared tree, brain content, other agent folder, git state or trading directory was modified. Supervisor copy, mirror and independent review are unverified. No local save blocker.

## Universal bridge

C024 history transfer and C019 stopping payment advance from active/control-only resets to all eligible active/dummy/control histories on the surviving edited branch at SAME original rate2C0+10 (18 structurally), retaining every old debit and full terminal and leaving>=12e_root. The newly paid source-marginal change costs<8e per dummy step; the universal FEI constant improvement is zero. Generic source pricing and a fresh reset inside a retained off-branch remain unpaid. NEXT carries this very same diminished bank into that off-branch, which is the shortest remaining source-geometry test rather than another isolated class entropy bound.
'''
put(RUN/'REPORT.md',report)
put(OWN/'STATUS.md',f'STATE: A073 stage17 saved: dummy-data reset<8e; ALL eligible mixed type histories paid SAME18 structurally, >=12e_root left; {result["assertions"]} exact checks PASS; review pending; FEI OPEN.\nNEXT: {nxt}\n')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} stage17: new dummy-source marginal/calibration payment; {counts} and {result["assertions"]} predicates PASS. Initial pilot fixture guard repaired; fixedN12, no refinement. Lean held by memok; wake attachment alerts surfaced. Full FEI OPEN.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage17: For negative-cell point-source F and b>=1,r>=1, dummy source marginal then empty calibration dominates original R on true source support, cbar<=c pointwise. Full off-reference kappa=(2s-e)^2/(4s²-4se+2te) has inverse<=1+h/2 since t<=s/2,h=e/s<=1/2. Off excess<11e, true B<12e, complete reset surcharge<8e. All surviving-branch active/dummy/control type histories paid from SAME original K=2C0+10, >=12e_root left for d=b+r>=2. Imported active final boundary remains essential. Nonconstant Boolean parity has deterministic spectrum: test P(empty)<1, not max(P)<1. Generic source/off-branch reset still open; no precision escalation.\n')
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
files=[]
for p in RUN.rglob('*'):
    if p.is_file():
        data=p.read_bytes();assert len(data)<20*1024*1024
        files.append({'path':str(p.relative_to(RUN)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
js(OUT/'PERSISTENCE_RECEIPTS.json',{'created_at':now,'field_sets':'PASS','statement_sha256':'PASS','progress_equals_delta':True,'files':files,'remote_copy':'UNVERIFIED','independent_review':'PENDING'})
print(json.dumps({'status':'SAVED','assertions':result['assertions'],'counts':counts,'run':str(RUN),'minimum_margin':'12e_root analytically','full_FEI':'OPEN'},indent=2))
