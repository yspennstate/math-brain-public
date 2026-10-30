from pathlib import Path
import json,hashlib,datetime

R=Path(__file__).resolve().parents[1];A=R.parents[1];BASE=A.parents[1]
def write(p,s):p.write_text(s,encoding='utf-8')
def js(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protocol=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
P=json.loads(protocol.read_text(encoding='utf-8'))
aud=json.loads((R/'out/AUDIT.json').read_text(encoding='utf-8'))
ex=json.loads((R/'out/EXHAUSTIVE.json').read_text(encoding='utf-8'))
cw=json.loads((R/'out/CONSTRUCTED_WITNESS.json').read_text(encoding='utf-8'))
assert aud['verdict']=='PASS' and ex['case_count']==256 and ex['strict']==0
statement=('On any finite Boolean restriction/admission DAG with slack S=KI-H, prescribed local stopping-hull credit increments delta_b=rho_M(child_b)-E rho_M(children), and unchanged credit on admissions, the exact capital supporting every subsequent query/admission/stopping choice is T(v,M)=max{(-S(v))_+,T(v,M+j),T(child_b,M)-delta_b}. It equals the maximum over actual paths of terminal deficit minus cumulative delta. For all Boolean functions on at most3 bits and all K>=0, T(v,empty)=rho_all(v). At K=1 the explicit Boolean family F_d(s,x)=chi_3(x) with its sign flipped only at the all-zero vertex, d>=0 selector bits and3 parity bits, has full stopping hull R_d=max_(0<=r<=3,0<=t<=d) 2^(-(d+3-r-t))*(H_(r+t)-I_(r,t))_+, where I_(r,t)=r+2*(r+t-2*r)/2^(r+t) for r+t>=1, H_m is the entropy of one mass (1-2/2^m)^2 and2^m-1 masses4/2^(2*m), and H_0=I_(0,0)=0. It obeys 0<R_d<=8*(d+4)/2^(d+3), while sequential local-hull admission capital T_d>=1/2; hence sup_d T_d/R_d=infinity. For d=1 exactly R_1=1/4 and T_1=1/2. Credit-owner and signed-debit labels can be preserved conditionally whenever this capital criterion holds. This is an admission-accounting obstruction at rate1, not a rate4 or FEI counterexample.')
hypotheses=['uniform independent physical bits and base2 Fourier entropy','finite acyclic physical restrictions, stop allowed, admissions cost no new credit','every query uses the exact CURRENT admitted-set stopping-hull allocator, with inherited actual credit retained','solvency required for every policy and every branch, individual nonnegative credit owners and signed debit owners retained','the explicit family conclusion uses K=1; no claim at K=4 or against influence-paid universal envelopes']
digest=hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest()
claim=dict(claim_id='A072-LOCAL-HULL-ADMISSION-DAMAGE-UNBOUNDED',version=1,exact_statement=statement,hypotheses=hypotheses,statement_sha256=digest,contributors=['A072'],proof_source=['PROOF.md','code/admission.py','code/verify.py','out/CONSTRUCTED_WITNESS.json','out/AUDIT.json','out/FAMILY_FORMULA_CHECKS.json','out/EXHAUSTIVE.json'],proof_dependencies=['A072-OTHER-CORE-STOPPING-CREDIT-HULL@1: finite Bellman framework; proof rederived here','finite character orthogonality, Shannon chain rule and the explicit positive atanh logarithm series'],review_records=[{'reviewer':'A072','independent_reviewer':False,'verdict':'AUTHOR_PROOF_AND_TWO_REPRESENTATION_AUDIT_PASS','scope':'all-d analytic family proof; exact four-bit backward recurrence and independent forward paths/subset hulls; no external acceptance'}],status='PROVED_LOCALLY_EXTERNAL_REVIEW_PENDING',supersedes=[],refutes=['Proposed generic implication: a full stopping-hull bank, enlarged by a universal constant factor, pays every sequential local-hull admission scheme (rate1 refutation; not a registered claim version).'],first_unproved_line='Construct an initially influence-paid, owner-coherent superharmonic envelope at a suitable absolute rate for arbitrary Boolean restriction/admission DAGs; no universal FEI bound is supplied.',next_consumers=['A071','A074','A075','A089','A092'])
js(R/'CLAIMS.json',[claim])
src=[protocol,BASE/'BOARD.md',BASE/'claude/B15/STREAM_NOTES.md',BASE/'agents/A071/runs/20261023T052248Z-fleet03-A071-search-space-design/REPORT.md',BASE/'agents/A071/runs/20261023T052248Z-fleet03-A071-search-space-design/PROOF.md',BASE/'agents/A071/runs/20261023T052248Z-fleet03-A071-search-space-design/CLAIMS.json',A/'runs/20261023T015130Z-fleet03-A072-exact-walsh-engine/PROOF.md',A/'runs/20261023T015130Z-fleet03-A072-exact-walsh-engine/code/arithmetic.py']
js(R/'out/SOURCE_PINS.json',[{'path':str(p),'sha256':sha(p),'role':'read-only source; source A071 finite certificate used for scope and dispatch, not as a premise of new family proof'} for p in src])
nextaction='A074/A092 reconstruct the all-d rate1 admission-damage proof; A071/A075/A089 build a coherent full-universe envelope at a suitable absolute rate with initial credit paid from influence, rather than infer admission safety from a root hull.'
progress=dict(protocol_revision=P['revision'],run_id=R.name,stream='B15',packet_id='A072',gap_id='C019-INHERITED-COMPONENT-ELIGIBILITY',attempt_id='A072-stage19-local-hull-admission-damage',method='Exact max-path capital recurrence; explicit Boolean parity/singleton-defect family; integer Walsh/inverse/edges; all-d proof; separate direct-character and subset-hull path audit.',mathematical_delta='Root global stopping-hull funding does not imply local-hull admission funding even up to any constant factor: actual rate1 family has R_d->0 and T_d>=1/2. Four-bit minimal witness R=1/4,T=1/2. Through3 bits all rates K>=0 have no admission damage. Full FEI OPEN; no rate4 obstruction claimed.',deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='NEW_THEOREM_PROVED_LOCALLY_EXTERNAL_REVIEW_PENDING; FULL_FEI_OPEN',claim_versions_used=['A072-OTHER-CORE-STOPPING-CREDIT-HULL@1 (framework reused and rederived)','A071-SAME-CREDIT-FOUR-CORE-CONTINUATION@1 (read-only dispatch/scope information, not new-proof premise)'],claims_created_or_changed=[claim['claim_id']+'@1'],source_artifacts=[str(p) for p in src],next_consumers=claim['next_consumers'],next_action=nextaction,stagnant_substantive_attempts=0,blockers=['Universal initial influence payment remains open.','New claim lacks external independent review.','Supervisor mirror/GitHub persistence is unverified; local research writes only.'],packet_ids=['A072'])
js(R/'PROGRESS.json',progress);js(R/'PACKET_DELTA.json',progress)
report=f'''# A072 stage19: local-hull admission damage can exceed the global reserve without bound

## exact target, quantifiers, hypotheses and units

Full FEI OPEN. Entropy bits, uniform physical cube. Derive the exact capital requirement for every future query/admission/stop under the prescribed current-mask hull allocator, retaining actual credit and each owner. Prove the all-K>=0 no-damage theorem through3 bits, then exhibit an actual Boolean all-d family at rate1 with unbounded robust-capital/global-hull ratio. This attacks an admission inference, not the FEI inequality or the actual rate4 finite source certificate.

## sources actually read, revisions and theorem locators

Execution protocol {P['revision']} read in full this stage; BOARD06:06UTC, unchanged B15 lead v2, own stage18 STATUS and engine; A071052248 REPORT, PROOF in full and CLAIMS, especially sharp-hull and actual-history sections. Earlier campaign/paper intake retained as background, with no new literature premise. SOURCE_PINS hashes actual read-only sources. A071 already closed all four remaining cores, so no duplicate finite-core search was run. Board reports A074's independent acceptance of A072 stage18; this stage does not claim independently to have accepted A071's new certificate.

## complete derivation or exact first unsupported line

PROOF sections1-5 give the exact max-path capital recurrence and owner-labelled conditional transfers; all rates K>=0 through3 bits; symbolic integer spectra, inverse signs and independent edges of F_d; exact unique-zero-path stopping hull; analytic positive-slack and entropy bounds for every d. The family has 0<R_d<=8(d+4)/2^(d+3), but robust local-admission capital T_d>=1/2. At d=1 exactly R=1/4,T=1/2. Thus there is no universal constant converting a global stopping-hull reserve into safe funding for arbitrary sequential local-hull allocators. The first unsupported universal line is an influence-paid coherent envelope at a suitable absolute rate for arbitrary Boolean restrictions; the rate1 family has I->3 and does not contradict such an envelope.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC preceded the fixed2-bit pilot and exhaustive3-bit rate1 census. Pilot:16 tables,164 checks,0 strict cases. Main:256 tables,{ex['checks']} checks,0 strict cases,{ex['runtime_seconds']:.3f}s. The theorem for all nonnegative real rates is proved analytically. CONSTRUCTION_SPEC freezes one analytically selected4-bit function, not an automatic dimensional sweep. Its backward capital recurrence and full forward paths passed135 checks in{cw['runtime_seconds']:.3f}s. Integer Walsh Parseval, sign inverse and direct edge counts are completed before any entropy comparison.

AUDIT_SPEC freezes a different direct-character/subset enumeration, forward path method and17 formula-only cases d=0..16; no large truth arrays are built. Author audit passes{aud['checks']} assertions and13645 pruned actual path nodes in{aud['runtime_seconds']:.3f}s. The all-d proof is symbolic, not extrapolated from these17 checks. Exact Fraction prime-log profiles and192-bit outward intervals with a proved atanh tail decide signs; rational cancellation decides exact equalities. No float verdict is used. First audit failed a tuple-versus-JSON-list equality after the R=1/4,T=1/2 checks had passed; FIRST_AUDIT_FAILURE preserves the issue, then serialization normalization repaired it. No mathematical mismatch arose. Each job was estimated100MB or less; no >300MB job or memok-gated search was needed. No Lean, GPU, external solver, detached job or process shedding was used.

Commands from this run: python -B -X utf8 code/admission.py --pilot; python -B -X utf8 code/admission.py; python -B -X utf8 code/admission.py --constructed; python -B -X utf8 code/verify.py; python -B -X utf8 code/finalize.py.

## proof dependencies and changed downstream conclusions

Finite stopping Bellman induction is reused from own stage18 and fully rederived. Integer character orthogonality and the explicit log remainder are the only numerical primitives. New claim {claim['claim_id']}@1 has an author proof and distinct author audit, with external review pending. It explains why A071's8784 actual-credit cuts are substantive: the conclusion cannot generally be deduced from root hull equality, even after a fixed-factor top-up. Nothing invalidates those separately checked rate4 cuts. No complete Boolean FEI case at rate4 is newly claimed.

## one next mathematical action and independent reviewer

{nextaction} The review must check both the universal max-path recurrence and the all-d Boolean argument, rather than only reproduce the four-bit example.

## actual persistence receipts or precise save blocker

All required files, code, proof, frozen specs and exact outputs are inside A072. PERSISTENCE checks exact schema fields, canonical claim hash, progress/delta identity, rolling STATUS shape and file sizes; MANIFEST records hashes. External acceptance and supervisor GitHub/brain mirroring remain unverified. No other agent folder or shared research index was written, and no git or message was sent. Brain self-care remains degraded/unverified: the owner-model and state-of-mind notes were approximately92 and77 hours old at intake, affecting personal-context reliability; neither is a mathematical premise. All research jobs have completed.

## Universal bridge

This stage moves C019 stopping-tree payment and C024 history transfer by separating their funding requirements exactly: prescribed local-hull admission capital is a max over actual path deficits, while the global hull is an expected stopping deficit, and an explicit all-dimensional Boolean family makes their ratio unbounded at rate1. It also closes all<=3-bit admission accounts at every nonnegative rate and gives the smallest4-bit obstruction. What remains is an initially influence-paid coherent envelope at an appropriate absolute rate, with old owners retained. NEXT is the shortest route toward full FEI because it removes a false constant-factor admission shortcut and directs the stream to prove coherence and initial payment together, rather than repeat its completed four-core census.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md','STATE: A072 stage19 saved: Boolean rate1 family has global hull->0 but local-admission capital>=1/2; four-bit exact1/4 vs1/2; all<=3-bit K>=0 coherent; FEI OPEN.\nNEXT: A074/A092 review all-d admission-damage proof; A071/A075/A089 construct influence-paid coherent full-universe envelope at suitable K; no root-hull-to-local shortcut.\n')
date=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{date} stage19: Read BOARD/A071 full-four-core closure; skipped duplicate second-core task. Proved exact robust-capital max-path recurrence; all<=3-bit functions have no admission damage for every K>=0. Rate1 Boolean parity3 singleton-flip/selector family has global hull->0, robust local-admission capital>=1/2;4-bit exact1/4 vs1/2. Pilot16+census256 passed; independent-representation author audit111 checks/13645 path nodes passed after repairing JSON tuple/list comparison. Full FEI and external review OPEN.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''
2026-10-23 stage19 durable: For fixed local hulls, actual credit moves by delta=rho_M(child)-E rho_M(children). The exact all-future solvency capital is max_path[terminal (H-KI)_+ minus cumulative delta], not an expected deficit. Equivalently T=max(need, admission-child T, query-child T-delta). All<=3-bit Boolean functions have T=rho_all for every K>=0 because every2-bit proper child has entropy0.
Actual Boolean obstruction at K=1: F_d=parity3 on d+3 bits flipped only at all-zero. Walsh W_A=2^n*1_(A=parity support)-2; independent edges give I=r+2(m-2r)/2^m on any exceptional-path restriction. Full hull R_d=max_(r<=3,t<=d)2^{-(d+3-r-t)}(H_(r+t)-I_(r,t))_+ <=8(d+4)/2^{d+3}->0. Yet all selector-only restrictions have positive slack, local selector hull0 and unchanged credit, followed by three-bit hull1/2. Thus robust sequential local-hull capital>=1/2, with no constant-factor comparison to root global hull; d1 gives exact1/4 versus1/2. This does NOT refute K4 finite cuts or an influence-paid bank (I->3). Use a coherent universe-wide envelope or pay the actual admission damage; never infer admission safety from root hull funding alone. Proof/code/certificates in stage19 run.
''')
expected_progress=[k.split(' (')[0] for k in P['required_per_run']['progress_fields']]
assert set(progress)==set(expected_progress)
assert set(claim)==set(P['required_per_run']['claim_fields'])
assert json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert all(('## '+s) in report for s in P['required_per_run']['report_fields'])
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in R.rglob('*') if p.is_file() and p.name not in ['MANIFEST.json','PERSISTENCE.json']]
assert all(p.stat().st_size<20*1024**2 for p in files)
js(R/'out/PERSISTENCE.json',{'schema':'PASS','claim_hash':'PASS','progress_delta_equal':True,'status_lines':2,'all_files_under20MB':True,'external_review':'PENDING','mirror':'UNVERIFIED','rolling_sha256':{p.name:sha(p) for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']},'saved_at_utc':date})
files=[p for p in R.rglob('*') if p.is_file() and p.name!='MANIFEST.json']
js(R/'out/MANIFEST.json',[{'path':str(p.relative_to(R)),'size':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)])
print(json.dumps({'files':len(files)+1,'schema':'PASS','claim':claim['claim_id'],'claim_sha256':digest,'full_fei':'OPEN'}))
