"""Persist the source-bound stage and verify its protocol schema."""
from pathlib import Path
import copy,hashlib,json
R=Path(__file__).resolve().parents[1];A=R.parents[1];B=A.parents[1]
def read(p):return Path(p).read_text(encoding='utf-8')
def put(p,s):Path(p).write_text(s,encoding='utf-8',newline='\n')
def save(p,obj):put(p,json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
v=json.loads(read(R/'out/VALIDATION.json'));iv=json.loads(read(R/'out/INDEPENDENT.json'))
assert v['status']==iv['status']=='PASS' and v['roots']==48 and iv['roots']==72
assert v['final_active_closures']==1944 and v['history_prefixes']==2816
assert iv['flat_boundary_count']==4
P=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(read(P));fields=protocol['required_per_run']
oldrun=A/'runs/20261021T185558Z-fleet03-A026-good-coordinate-erasure'
old=json.loads(read(oldrun/'CLAIMS.json'))[0]
base=B/'agents/A097/runs/20261014T050248Z-fleet05-A097-cross-route-transfer'
mixed=B/'agents/A097/runs/20261021T232544Z-fleet03-A097-cross-route-transfer'
depclaims=json.loads(read(mixed/'CLAIMS.json'))
dependencies=[{'claim_id':z['claim_id'],'version':z['version'],'statement_sha256':z['statement_sha256'],'source':str(mixed/'CLAIMS.json'),'acceptance':z['status']} for z in depclaims]
dependencies.insert(0,{'claim_id':'A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK','version':1,'statement_sha256':'67b1ea4ab05a49a28c016964eab7553aae10869565f2a70ed85c94c586cec341','source':str(base/'CLAIMS.json'),'acceptance':'source-complete baseline, imported only at stated scope'})
sources=[P,B/'BOARD.md',B/'claude/B06/STREAM_NOTES.md',oldrun/'REPORT.md',oldrun/'DERIVATION.md',oldrun/'CLAIMS.json',base/'DERIVATION.md',mixed/'DERIVATION.md',mixed/'REPORT.md',mixed/'CLAIMS.json',mixed/'code/check_transfer.py',B/'agents/A004/runs/20261022T220858Z-fleet03-A004-constant-and-unit-ledger/DERIVATION.md',B/'agents/A028/runs/20261022T205915Z-fleet03-A028-stopping-tree-payment/DERIVATION.md',B/'agents/A029/runs/20261022T221752Z-fleet03-A029-child-deficit-transport/REPORT.md']
receipts=[{'path':str(p),'sha256':sha(p),'size_bytes':p.stat().st_size} for p in sources if p.exists()]
save(R/'out/SOURCE_RECEIPT.json',{'scope':'current sources actually read plus imported stage17 intake; hashes identify versions, not proof acceptance','files':receipts,'unavailable_paths':[str(p) for p in sources if not p.exists()]})
save(R/'out/ATTEMPTS.json',{'pilot':'PASS:4 roots,272 own+72 helper predicates,32 prefixes,28 steps,0.1425313 seconds','first_main':'stopped at Python4300-digit rational-to-string serialization; no failed mathematical predicate','output_repair':'reported interval endpoints rounded outward to denominator2^40; minimum margin rounded downward; all sign comparisons remain exact','first_independent':'auxiliary nonflatness guard failed at a=1,b=1,r=1; actual on-floor is exactly uniform on4 atoms','repair':'retain flat boundary; nonflatness required only in original r>=2 local checks; no cost inequality or root domain removed','final_main':{k:z for k,z in v.items() if k!='rows'},'final_independent':iv})
save(R/'out/FLAT_BOUNDARY.json',{'root':{'a':1,'b':1,'r':1},'on_truth_table':[1,1,-1,1],'on_squared_spectrum':['1/4']*4,'on_complete_floor':['1/4']*4,'verification':'direct-character checker covers all four frozen source-reference shapes; all give this prescribed flat child','meaning':'flatness is a valid boundary, not a cost counterexample'})
d=read(R/'DERIVATION.md')
identity='''## 0. Exact decrement and complete-reference identity

For a Boolean f write P_f(S)=fhat(S)^2, M_i=marginal_i P_f, and B_i(f)=H(P_f)-H(M_i)=H(S_i|S_without_i). The exact restriction identity in bits is

    H(f)-[H(f_i+)+H(f_i-)]/2
       =B_i(f)+JS(P_f_i+,P_f_i-).

Indeed M_i=(P_f_i++P_f_i-)/2, and the Jensen-Shannon term is H(M_i)-[H(P_f_i+)+H(P_f_i-)]/2. Thus B is not the entire entropy decrement. If Q is a complete normalized reference and q=marginal_i Q, the exact no-reset identity is

    B_i(f)+[CE(P_f_i+,q)+CE(P_f_i-,q)]/2
      =CE(P_f,Q)-[KL(P_f||Q)-KL(M_i||q)].

The bracket is nonnegative by the conditional KL chain rule. This proves that arbitrary no-reset off-branch continuations cannot increase the complete-reference ledger. It does not remove the JS term from the true entropy decrement or supply a universal small reference. Coordinate selection must still exhibit some actual relevant coordinate for arbitrary Boolean f; no all-coordinate assertion follows from the present point-source history theorem.

'''
if '## 0. Exact decrement' not in d:d=d.replace('## 1. Original source',identity+'## 1. Original source')
d=d.replace('The final active a=1 boundary may stop the edited branch.','At the final active a=1 query the imported explicit point-spectrum rule ends the edited branch; its whole local closure costs at most the current W, and is checked separately at every eligible prefix.')
d+='''
## 6. Boundary and review audit

The r=1,a=1,b=1 dummy-on child has truth table (1,1,-1,1) and squared Fourier spectrum (1/4,1/4,1/4,1/4). Its prescribed complete floor is flat for every supplied calibrated source law. Nonflatness was an extraneous checker assertion, not a hypothesis of (3)-(9); the boundary is retained. Both Boolean children remain nonconstant. The original r>=2 on-floors remain checked as nonflat. This stage provides an author derivation and two finite computational representations, not a second human analytic review. A097's active/control source theorems are imported at their exact versions; their universal promotion is not assumed.
'''
put(R/'DERIVATION.md',d)
extension=''' Stage18 source-reference extension: Let F=1-2A_a+2A_(a+b+r) on disjoint uniform bits, a>=1,b>=0,r>=2 at the original ancestor. Supply one normalized finite-cost source reference with c_raw<=C0 I(1-2A_a), C0>=0, and use its empty-calibrated A097 complete floor. At a dummy-data query (b_current>=1,r_current>=1), keep the full inherited off-reference and reset the on-child to the canonical floor of the ACTUAL source marginal followed by empty calibration. If e=2^(1-a-b-r), c_off-c<14e, B_dummy<12e, and B_dummy+(c_off+W_on)/2<W+9e for W=c+10e(a+b+r). Conditional on the source-bound A096/A097 active/control clauses, every adaptive interleaving of active resets, control queries only while r_current>=2, dummy queries while r_current>=1, stopping, and the explicit final active point-spectrum closure has complete erasure-plus-terminal-reference ledger <=W_root+[8(r_root-1)+9b_root]e_root<=(2C0+10)I(F_root)-12e_root. All off-branches keep their complete inherited references and allow no-reset continuations; no ancestor quota is renewed. Structural source R=P_g uses the SAME initial rate18. This newly pays the previously unpaid dummy-DATA source-marginal reset; it does not construct an O(I) reference for arbitrary Boolean sources, pay arbitrary off-branch resets, or prove universal coordinate selection or FEI.'''
c=copy.deepcopy(old);c['version']=3;c['exact_statement']+=extension
c['hypotheses']+=['Stage18 extension only: original negative-cell point source and supplied normalized reference; bits, true physical flips and fair reach; C0 source-price supplied only once','Stage18 extension only: original r>=2; dummy local step admits b>=1,r>=1; final control query from r=1 excluded','Stage18 extension only: marginal then empty-calibrated SAME current source law; all complete normalizers and off-source atoms retained; no renewed bank or off-branch reset']
c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
c['contributors']+=['A026 stage18 dummy-source marginal proof; A096 active theorem and A097 canonical floor/control theorem credited']
c['proof_source']['stage18']=str(R/'DERIVATION.md');c['proof_source']['stage18_validation']=str(R/'out/VALIDATION.json');c['proof_source']['stage18_independent_representation']=str(R/'out/INDEPENDENT.json')
c['proof_dependencies']=[{'claim_id':old['claim_id'],'version':2,'statement_sha256':old['statement_sha256'],'source':str(oldrun/'CLAIMS.json'),'scope':'all prior conclusions retained'}]+dependencies
c['review_records']=[{'reviewer':'A026 alternate finite implementation, same author','method':iv['representation'],'result':'PASS72 roots/2002 predicates; not independent human acceptance'}]
c['status']='AUTHOR_PROOF_EXACT_VALIDATION_CONDITIONAL_IMPORTED_HISTORY_CLAUSES_REVIEW_PENDING'
c['supersedes']=[{'claim_id':old['claim_id'],'version':2,'scope':'retains all prior clauses and adds source-bound dummy-reset repair; not a new broad FEI candidate'}]
c['first_unproved_line']='For arbitrary non-point signed sources and supplied complete reference, pay a prescribed physical reset/history from the SAME genuinely unused source account, including both terminal debts; in particular no universal small reference or coordinate-selection theorem is established.'
c['next_consumers']=['A004','A028','A029','A087','A094','A096','A097','A098','A099','B20']
save(R/'CLAIMS.json',[c])
next_action='Reconstruct one prescribed reset inside an inherited off-branch on this SAME canonical source profile, without replacing its complete incoming reference or renewing the quota; A097/A096 audit local atom equation(3) and mixed-history substitution, A087/A094 audit existential scope.'
prog={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B06','packet_id':'A026','gap_id':'A026-SAME-SOURCE-HISTORY-PAYMENT','attempt_id':'stage18-dummy-data-source-marginal-reset','method':'Exact complete-reference likelihood comparison plus all-history ancestor-bank induction; FWHT and independent direct characters with rational log enclosures','mathematical_delta':'Previously unpaid dummy DATA reset now costs <9e from the SAME source account; local r=1 boundary included; mixed-history original rate retained, structural rate18, margin>=12e_root. No universal constant improves.','deliverable_status':'COMPLETE_LOCAL_SAVE_VERIFIED_PENDING_SUPERVISOR_MIRROR','mathematical_status':'SOURCE_BOUND_AUTHOR_PROOF_EXACT_CHECKS; IMPORTED_HISTORY_CLAUSES_CONDITIONAL; FULL_FEI_OPEN; INDEPENDENT_HUMAN_REVIEW_PENDING','claim_versions_used':[{'claim_id':old['claim_id'],'version':2}]+dependencies,'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':3}],'source_artifacts':str(R/'out/SOURCE_RECEIPT.json'),'next_consumers':c['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,'blockers':['Universal non-point source reference/unused-surplus theorem remains open','Final control r=1 and renewed off-branch resets outside proved scope','No independent human review or remote mirror verification','Lean not run: memory admission refused; arithmetic jobs estimated <=100MB, no peak measurement'],'packet_ids':['A026']}
save(R/'PROGRESS.json',prog);save(R/'PACKET_DELTA.json',prog)
report=f'''# A026 stage18: dummy-data reset stays on the original source account

The prescribed dummy-DATA reset costs less than9e beyond the current canonical envelope. Arbitrary active/control/dummy interleavings remain paid at the SAME original source rate, with at least12e_root left. Full FEI remains OPEN.

## {fields['report_fields'][0]}

Prove a supplied-reference extension for every a>=1,b>=0,r>=2 at the original ancestor F=1-2A_a+2A_(a+b+r), not just the 48 checked roots. R is normalized, finite on P_g, empty-calibrated from the actual supplied source law with c_raw<=C0 I(g). All costs are bits and all influences count uniform physical flips. A dummy local query requires b>=1,r>=1. On resets use the actual source marginal then empty calibration; off terminals keep their COMPLETE inherited references. Control queries stop at r=1; the final active query uses its explicit point-spectrum boundary. No child receives a fresh budget.

## {fields['report_fields'][1]}

Read current BOARD, B06 STREAM_NOTES v2 and own stage17 rolling frontier. B06's old transitive-class direction was already completed. A028 v6 already proves arbitrary biased-controller mixed JS transport, and A029 already gives finite-label mixed JS transport and the same-unused-ancestor criterion; these are consumed, not re-proved. A097's latest DERIVATION and claim A097-MIXED-ACTIVE-CONTROL-RESET-SAME-ANCESTOR@1 explicitly leave dummy-data reset unpaid. Its base A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK@1 supplies Q and W; A096-CANONICAL-ACTIVE-RESET-SAME-ANCESTOR@1 supplies active and final-point clauses. A004's reference-reset identity supplies the ledger interpretation; section0 also derives it directly. SOURCE_RECEIPT pins current bytes and exact claim hashes. Stage17's source intake pins the campaign files and four paper texts; they are reused baseline context, not claimed as a fresh full-paper audit. The user's current deadline overrides the archived protocol deadline.

## {fields['report_fields'][2]}

DERIVATION section0 gives the exact entropy decrement B_i+JS and the complete-reference no-reset identity; B_i alone is not that decrement. Sections1-3 compute BOTH off-reference atom contributions, prove k^-1<=1+e/s, c_off-c<14e, and c_new<=c for the actual marginal/calibration prescription. With B_dummy<12e this yields B_dummy+(c_off+W_on)/2<W+9e. This is a genuine new source-marginal change: treating the dummy coordinate as a control in the reference would be wrong. Section4 retains all debits and terminals, uses reach*e=e_root, and proves 5a*2^(b+r)-8(r-1)-9b>=12 for all dimensions by exact discrete induction. Thus the original K=2C0+10 remains sufficient (18 for structural source), not a new improved universal constant. The universal first unsupported line is the construction/payment of such a SAME unused source account for arbitrary non-point Boolean branches and prescribed histories. No all-coordinate assertion is promoted to existential selection.

## {fields['report_fields'][3]}

Frozen specs precede evaluation: FROZEN_SPEC, EXTENSION_SPEC and FINAL_CHECK_SPEC. Pilot:4 roots,272 own+72 helper predicates,32 prefixes,28 steps,PASS in0.143s. Final python -X utf8 code/check.py:48 roots with a=1,2,3; b=1,2; r=2,3; matching, uniform, increasing and dummy-singleton-spiked supplied source references. It checks every eligible active/control/dummy TYPE word and stopping prefix in fixed current-label order: {v['history_prefixes']} prefixes, {v['history_steps']} steps, {v['final_active_closures']} final active closures, {v['assertions']} own+{v['helper_assertions']} helper predicates,PASS in{v['seconds']:.3f}s. Source C0 is conservatively chosen once per original root (at least4); not every nonmatching reference uses18. No physical-label-permutation exhaustion or reference-law exhaustion is claimed.

python -X utf8 code/independent.py:72 local roots, adding r=1 to the same a,b,reference domain; {iv['assertions']} predicates,PASS in{iv['seconds']:.3f}s. Main uses integer FWHT; alternate uses direct character sums and a separately coded mixture/reference construction. Both use exact Fractions and rational22-term atanh intervals with a proved tail; only the log/CE primitive is shared. This is alternate computational reconstruction by the same author, not independent human analytic acceptance. Output intervals are rounded outward to dyadics; internal inequalities remain exact. ATTEMPTS preserves the first main serialization stop and an auxiliary nonflatness failure. The flat r=1,a=1,b=1 boundary is valid, not discarded; FLAT_BOUNDARY records its exact uniform spectrum and complete floor. Both children are nonconstant. The amended main additionally checks every final active closure with full terminal references. Arithmetic memory was estimated <=100MB; peak not measured. The Lean bookkeeping probe was NOT STARTED because memok refused admission (2.5GB free versus required4GB); no Lean certificate is claimed. No dimension escalation, GPU or detached job was used.

## {fields['report_fields'][4]}

This adds a narrow repair clause to A026-DISAGREEMENT-INFORMATION-RESERVE@3, retaining @2 rather than opening another broad FEI candidate. The dummy likelihood proof is source-complete; the global interleaving corollary imports A096 active and A097 control clauses at their recorded versions. A097 independently reconstructed the A096 clause; A097's new control clause and this stage's new clause still await independent human review. No blanket dependency acceptance is inferred from finite checks. A097/A096 may replace their explicit dummy-DATA exclusion with this paid prescription, including r=1, while retaining final-control and off-branch-reset exclusions. A028/A029 must keep their unused-source hypothesis; JS telescoping alone does not create this account. Source entropy, sector entropy, JS and reference-only atoms are already inside the complete CE and cannot be counted again as free reserves.

## {fields['report_fields'][5]}

{next_action} The exact generic non-point source bridge remains open; this next step tests the remaining history obstruction on the actual incoming reference rather than another fixed-family entropy estimate. Review must reconstruct equation(3), the c_new<=c marginal/calibration step and the original-quota substitution, not merely rerun the checker.

## {fields['report_fields'][6]}

All four protocol files, proof, frozen specs, copied helper, code and outputs are saved inside A026. PACKET_DELTA equals PROGRESS byte-for-byte. PERSISTENCE_RECEIPT verifies exact schema fields, statement hash, report fields, file sizes and hashes; rolling STATUS has exactly two lines. Local persistence is verified; supervisor copying, canonical adoption, remote mirrors, downstream use and independent human acceptance remain unverified. No git, mail, research-brain write, other-agent folder edit or trading-system action occurred. Nothing is left running. Brain self-care is degraded/unverified because the owner-model and state-of-mind sources are stale; personalization and current-state assumptions from those sources remain unverified.

## Universal bridge

This stage moves C019/C024 by paying the precise previously unpaid dummy-DATA source-marginal reset at <9e, including the r=1 boundary, and integrating it into arbitrary eligible active/control/dummy histories on the SAME original ancestor account with margin>=12e_root and structural rate18 unchanged. C018 universal coordinate selection and full FEI remain open; this does not prove an all-coordinate bound. The missing steps are a generic non-point source account, the last control boundary and a paid reset inside retained off-branches. NEXT attacks the actual inherited off-reference because that is the remaining concrete history-transfer obstruction; another isolated class entropy bound would not establish a universal source-owned induction.
'''
put(R/'REPORT.md',report)
put(A/'STATUS.md','STATE: Stage18 exact dummy-DATA canonical reset <9e; mixed active/control/dummy histories paid from SAME source quota, including r=1 dummy and final active boundary; full FEI OPEN, review pending.\nNEXT: Price one prescribed reset inside the actual retained off-reference without bank renewal; A097/A096 reconstruct atom and original-quota proof; generic non-point source remains open.\n')
entry='''\n2026-10-23 stage18 (20261023T001250Z): Consumed A028/A029 mixed-history results; advanced A097 unpaid dummy-data reset. Actual source marginal then empty calibration yields c_new<=c; full off-reference signed excess<14e, B<12e, local extra<9e. Same ancestor quota pays all eligible mixed histories, with margin>=12e_root; r=1 dummy boundary and final active closure retained. Final exact checks:48 roots/2816 prefixes/2768 steps/1944 final active closures;30920 own+1800 helper predicates. Alternate direct-character72 roots/2002 predicates;4 valid flat on-floor boundary cases. First main stop was rational string formatting; first alternate stop was extraneous nonflatness guard, corrected without weakening cost bounds. Lean not launched: memory admission refused. Full FEI open; independent review and supervisor mirror pending. NEXT retained off-reference reset, then generic non-point source bridge.\n'''
for name in ['WORKLOG.md','LEARNED.md']:
 text=read(A/name) if (A/name).exists() else ''
 if '2026-10-23 stage18 (20261023T001250Z)' not in text:put(A/name,text+entry)
# Receipt deliberately excludes its own hash and verifies the live persisted artifacts.
expected_progress=[x.replace('packet_ids (one primary ID, for compatibility)','packet_ids') for x in fields['progress_fields']]
assert set(prog)==set(expected_progress)
assert set(c)==set(fields['claim_fields'])
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert all('## '+x in read(R/'REPORT.md') for x in fields['report_fields'])
assert len(read(A/'STATUS.md').splitlines())==2
assert sha(R/'CLAIMS.json') and hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='PERSISTENCE_RECEIPT.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
save(R/'out/PERSISTENCE_RECEIPT.json',{'status':'PASS','exact_protocol_schemas':True,'statement_sha256':c['statement_sha256'],'packet_delta_byte_equal':True,'report_fields':fields['report_fields'],'rolling_status_lines':2,'independent_human_review':'PENDING','remote_mirror':'UNVERIFIED','files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]})
print(json.dumps({'status':'PERSISTED_AND_VERIFIED','files':len(files),'main_own_predicates':v['assertions'],'helper_predicates':v['helper_assertions'],'alternate_predicates':iv['assertions'],'main_prefixes':v['history_prefixes'],'final_active_closures':v['final_active_closures'],'claim':c['claim_id']+'@3'}))
