from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1];BASE=AGENT.parents[1]
OUT=RUN/'out'
def dump(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def statement_hash(c):return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
pilot=read(OUT/'PILOT.json');full=read(OUT/'CHECK.json');ver=read(OUT/'VERIFY.json')
assert all(d['status']=='PASS' and d['elapsed_seconds']<60 for d in [pilot,full,ver])
assert full['universal'][0]['functions']==65536 and full['private_functions']==74
assert pilot['private_functions']==10
total=pilot['exact_assertions']+full['exact_assertions']+ver['exact_assertions']
stamp=datetime.now(timezone.utc).isoformat()
review_run=BASE/'agents/A009/runs/20261014T054349Z-account05-A009-fractional-incidence-optimization'
claim=read(review_run/'CLAIMS.json')[0]
assert statement_hash(claim)==claim['statement_sha256']
dump(OUT/'HASH_CONVENTION.json',{'initial_validation':'FAILED before any protocol or rolling file writes: validator incorrectly assumed raw UTF-8 statement hash','recorded_source_hash':claim['statement_sha256'],'raw_statement_sha256':hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest(),'verified_source_convention':'sha256 UTF-8 json.dumps({statement: exact_statement, hypotheses: hypotheses}, sort_keys=True, separators=(comma,colon))','canonical_hash':statement_hash(claim),'source_locator':str(review_run/'code/finalize.py')+':16','resolution':'Match original source convention for imported and new claims; unchanged mathematics, no mathematical job rerun'})
claim['review_records'].append(dict(reviewer='A008',verdict='HOLDS_AT_WHOLE_ORIGINAL_SCOPE_NO_REPAIR',proof_source=str(RUN/'REVIEW_A009.md'),validation=[str(OUT/'PILOT.json'),str(OUT/'CHECK.json')],method='Independent direct physical truth tables and original chronological private-block queue replay; all-dimensional analytic reconstruction of every probability and payment clause',reviewer_supplied_substantive_repair=False,timestamp_utc=stamp))
claim['status']='WHOLE_INDEPENDENT_RECONSTRUCTION_BY_A008_LOCAL_ADOPTION_PENDING'
statement='For every nonconstant uniform Boolean function f, q=Pr(f=-1), v=4q(1-q), every finite nonempty table of signed conjunction implicants e of f=+1 of widths w_e>=k>=1, rarities pi_e=2^(-w_e), and positive globally fixed weights satisfying sum_(e:i in R_e)lambda_e<=1, put D=product_e(1+lambda_e*pi_e)-1 and a_k=(1-2^(-k))/k. Then sum_(i in R_e)Inf_i(f)>=2q*w_e/(2^(w_e)-1) for every gate, sum_e lambda_e*pi_e<=a_k I(f)/(2q), and the SAME signed original root-normalization contribution satisfies v log2 D <= [2 a_k(1-q)/ln 2]I(f). No monotonicity, privacy, independent-gate, product-spectrum or posterior assumptions are required. The rarity coefficient is sharp on a single AND_k gate at weight one. Substitution into A009-ARBITRARY-CORE-PRIVATE-LEAF-COMPLETE-PAYMENT v1, with its reference and weights unchanged, gives C_PL<399I/40<10I. This pays only root normalization universally; complete non-root occupation cost and full FEI remain open.'
new={
 'claim_id':'A008-ALL-BOOLEAN-IMPLICANT-ROOT-NORMALIZER-PAYMENT','version':1,'exact_statement':statement,
 'hypotheses':['Uniform physical cube and nonconstant Boolean f; costs in bits','Finite nonempty table of actual signed conjunction implicants of f=+1','Each gate has positive integer width and its actual rarity 2^-width','One positive packing-feasible weight vector fixed before the spectral set is sampled','The <10I corollary uses the unchanged full scope and actual private-block reference of A009 v1'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A008'],
 'proof_source':{'path':str(RUN/'ROOT_PAYMENT.md'),'code':[str(RUN/'code/check.py'),str(RUN/'code/verify.py')],'certificates':[str(OUT/'PILOT.json'),str(OUT/'CHECK.json'),str(OUT/'VERIFY.json')]},
 'proof_dependencies':[{'source':str(BASE.parents[1]/'mop_fei100/reports/fei-2026-10-11/source_material/reductions/paper/forests.tex'),'use':'Identity Lambda+log Z=log D and identification of the original root term only; local cube boundary lemma is proved directly'},{'claim_id':claim['claim_id'],'version':1,'statement_sha256':claim['statement_sha256'],'use':'<10I downstream corollary only; not used in the universal root theorem','status':'WHOLE_INDEPENDENTLY_RECONSTRUCTED_LOCALLY_BY_A008'}],
 'review_records':[{'reviewer':'A008','verdict':'ANALYTIC_PROOF_WITH_EXACT_FINITE_AND_INDEPENDENT_FIBER_CHECKS; NOT INDEPENDENT_AGENT_ACCEPTANCE','validation':str(OUT/'VERIFY.json'),'lean_status':'SETUP_UNVERIFIED; compute admission held, no compiler process'}],
 'status':'ANALYTIC_PROOF_EXACT_CHECKED_PENDING_INDEPENDENT_AGENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A006','A007','A009','A010','A015','A086','B02','B20']}
new['statement_sha256']=statement_hash(new)
dump(RUN/'CLAIMS.json',[claim,new])
protocol=read(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
progress={
 'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B02','packet_id':'A008','gap_id':'G-J-COST','attempt_id':'A008-stage6-universal-implicant-root-payment',
 'method':'Whole independent review; physical cube minimum-cut bound on every implicant fiber; packing sum; same-reference substitution; exact integer/Fraction enumeration',
 'mathematical_delta':'Universal signed-conjunction root normalization paid <=2(1-2^-k)(1-q)I/(k ln2), without monotonicity or private leaves. A009 v1 whole independently HOLDS; unchanged reference improves from <11I to <10I. Complete non-root occupation payment remains open.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'NARROW_UNIVERSAL_ACCOUNTING_LEMMA_PROVED_PENDING_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':claim['claim_id'],'version':1,'statement_sha256':claim['statement_sha256']}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'WHOLE_LOCAL_INDEPENDENT_REVIEW_HOLDS_NO_REPAIR'},{'claim_id':new['claim_id'],'version':1,'change':'NEW_NARROW_UNIVERSAL_ROOT_LEMMA_AND_SAME_REFERENCE_COROLLARY'}],
 'source_artifacts':[str(RUN/'ROOT_PAYMENT.md'),str(RUN/'REVIEW_A009.md'),str(OUT/'SOURCES.json'),str(OUT/'CHECK.json'),str(OUT/'VERIFY.json')],
 'next_consumers':['A006','A007','A009','A010','A015','A086','B02','B20'],
 'next_action':'A007/A086 independently reconstruct the fiber boundary and packing coefficient; A006/A009/A010 pay one complete non-root occupation bill on shared/leafless incidence with the SAME original reference, now using the universal root payment. No bank or reference reset.',
 'stagnant_substantive_attempts':0,'blockers':['Independent-agent review of new lemma pending','Lean compile not admitted due resource pressure; no certificate','Complete non-root occupation label/subset/attachment/rank payment open','Supervisor copy and mirror verification unobserved'], 'packet_ids':['A008']}
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)
dump(OUT/'LEAN.json',{'status':'SETUP_UNVERIFIED','exit_code':1,'output':'Compute admission held (hung window or under 5500 MB free); no new compiler process','statement':'example (w a b c : Nat) (hw : 2 <= w) (h : (w-1 <= a ∧ w-1 <= b) ∨ (w-1 <= a ∧ 1 <= c) ∨ w <= c) : w <= a+b+c := by omega','scope':'Only the induction-case arithmetic was submitted, not the whole cube boundary theorem. No Lean-checked result claimed.'})
sources=[]
paths=[BASE/'BOARD.md',BASE/'claude/B02/STREAM_NOTES.md',review_run/'PRIVATE_LEAF_PAYMENT.md',review_run/'CLAIMS.json',BASE/'agents/A006/runs/20261021T182437Z-account03-A006-posterior-forest-optimization/PROOF.md',BASE/'agents/A007/runs/20261021T211258Z-account03-A007-root-normalization/KMM_PAYMENT.md',BASE/'agents/A008/runs/20261014T021605Z-account05-A008-gate-label-compression/OCCUPATION_MASS.md']
repo=Path(r'~\mop_fei100');campaign=repo/'reports/fei-2026-10-11';supp=repo/'research_pushes/2026-10-11-full-fei-100-agents'
paths+=[campaign/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths+=[supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths+=[campaign/'source_material/reductions/paper/forests.tex']
paths+=[review_run/'code/finalize.py',BASE/'agents/A006/runs/20261014T074929Z-account05-A006-posterior-forest-optimization/JOINT_EDGE_SLICE.md']
paths+=list((BASE/'context').glob('*.txt'))
for p in paths:
 if p.exists():sources.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'read_scope':'Pinned source; new proof/review sources and protocol read directly; campaign/paper baseline consulted selectively this stage and inherited from earlier substantive runs, not newly reread wholesale'})
dump(OUT/'SOURCES.json',sources)
report=f'''# A008 stage 6: universal implicant root payment

## exact target, quantifiers, hypotheses and units

C020 / PI-J, original G-J-COST. Pay the SAME root normalization for every nonconstant Boolean f and every finite nonempty signed conjunction implicant table with positive feasible global packing weights and actual rarity 2^-width. ROOT_PAYMENT.md states the full all-dimensional quantifiers and width-dependent coefficient. Independently review A009 private-leaf complete-payment v1 as a whole. All entropy and cost units are bits; physical influences are uniform-cube influences. Full FEI remains OPEN. The newer owner deadline 2026-10-23 14:49 UTC supersedes the older endpoint in the baseline metadata; no schedule or clock is changed here.

## sources actually read, revisions and theorem locators

Read machine-wide AGENTS.md, full execution protocol revision {protocol['revision']}, current BOARD (2026-10-21 23:41 UTC), B02 lead v2, own STATUS/LEARNED and substantive stages 4/5. Historical lead tasks were already completed; current dispatch consumes A009's whole-review request and the shared/leafless gap. Read A009 PRIVATE_LEAF_PAYMENT/CLAIMS, A006 current PROOF and JOINT_EDGE_SLICE, A007 current KMM_PAYMENT, own occupation source, and original forests.tex queue/forestconditioning/forestcost/foresttarget. Campaign registries, README/current status/supplement and all four supplied paper versions were selectively consulted; earlier complete baseline reads are inherited, not claimed as new full rereads. out/SOURCES.json pins consulted files. No external theorem is required for the new cube min-cut proof.

## complete derivation or exact first unsupported line

ROOT_PAYMENT.md proves every nonempty proper subset of a w-cube has at least w boundary edges by layer induction. Every implicant fiber contains a true point, so averaging its false-set boundary gives sum_(i in R_e)Inf_i>=2q w_e/(2^w_e-1). Multiplying by fixed lambda_e and applying the physical packing rows yields S=sum lambda_e 2^-w_e<=a_k I/(2q), a_k=(1-2^-k)/k. Since ln D<=S, the SAME signed root term satisfies v log2 D<=2a_k(1-q)I/ln2. Neither monotonicity nor private incidence is used. The coefficient of the S bound is sharp on AND_k, and q>0, positive widths, actual implication, rarity and packing are checked where used.

REVIEW_A009.md reconstructs the unchanged whole private-leaf claim without repair: disjoint actual root/chronological events, all root/name/subset/count/multiset/attachment probabilities, posterior output ambiguity, physical conditional payment and original <843I/80<11I constant. It gives whole local independent HOLDS, not registry adoption. The new universal width-two root estimate subsequently improves this SAME reference to C_PL<399I/40<10I. The numerical ceiling changes because the root estimate improves; the function, weighting and event family do not change.

First unsupported universal line: a single fixed feasible reference whose COMPLETE expected non-root label/subset/attachment/rank occupation cost, after the legitimate actual-run posterior refund, is O(I) on shared/leafless incidence. A shared-neighbor attempt cannot reuse private rarity: K_(3,2) has b/a=4/7>1/4. Root payment removes one universal term and does not prove FEI or pay an arbitrary full forest.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes all checker executions. Pilot: 276 Boolean functions n=1,2,3 plus ten private-core graphs, {pilot['exact_assertions']} exact assertions, {pilot['elapsed_seconds']:.6f}s. Full: all 65,536 labelled n=4 functions and their 1,148,928 signed implicant faces; all 74 labelled private-core graphs on r<=3 with counts in {{1,2}}; {full['exact_assertions']} exact assertions, {full['elapsed_seconds']:.6f}s. Every proper cube cut n<=4 is checked, with exact physical influences and Walsh checks at small n. Every private output set, its trace-derived numerator, pointwise lower bound and whole subprobability is checked. Scalar mass/count bounds are checked through m=128; the proof supplies all-m induction. No symmetry reduction or domain escalation.

ADVERSARIAL_SPEC.json precedes an independent direct fiber replay on 276 functions, all signed implicants and all outside assignments; sharp AND widths through128, decreasing width coefficient, actual invalid-hypothesis fixtures, and exact logarithm enclosures on both D<1 and D>1. It passes {ver['exact_assertions']} assertions in {ver['elapsed_seconds']:.6f}s. Combined exact assertion count is {total:,}. Integer/Fraction decisions only; normalizer log intervals use twenty positive atanh terms with remainder 2*z^41/[41(1-z^2)] after binary reduction. Checkers import no author implementation.

Commands: python -X utf8 code/check.py --pilot; python -X utf8 code/check.py; python -X utf8 code/verify.py, from this run. All completed with exit0. Each algorithm stayed below60s; estimates80/30 MB, no job expected above300 MB, no memok trigger, no GPU or detached work. Lean induction-case arithmetic was submitted through lean_check.py but admission held (under5500 MB free or hung-window condition), exit1, NO compiler process. Rung: analytic proof plus exact finite checks, pending independent review; not Lean-checked. No retry to override admission. out/LEAN.json records the precise attempted statement and limitation.

## proof dependencies and changed downstream conclusions

The universal local inequality is proved directly and does not depend on A009, A006 optimization, a FEI assertion or a posterior relaxation. Original forests.tex is used only to identify Lambda+log Z=log D. The <10I application uses independently reconstructed A009 v1 at its unchanged statement hash. Dependencies are acyclic: A009 uses older A008 stage5, not this new root lemma. Existing occupation, connected-scale and full-family variational results are not re-proved or widened. A009's original claim receives a whole local independent review; A008 contributes to the new lemma/corollary and recuses as its independent referee.

The stream review cap is respected by completing an outstanding whole review and adding one narrow universal accounting lemma rather than another broad complete-cost candidate. Root normalization no longer needs a private-leaf or positive-controller hypothesis for conjunction implicant tables; all other controller/lift costs remain whatever their original statements require.

## one next mathematical action and independent reviewer

A007/A086 should independently reconstruct the physical fiber bound and packing coefficient, including mixed literal signs, empty false fibers and sharp AND_k cases. A006/A009/A010 should now pay one complete non-root occupation bill on genuinely shared/leafless incidence with the SAME global table/reference. Keep every label, subset, rank, attachment and output ambiguity term; no reference or bank reset. No messages were sent. This is the shortest next step because it isolates the only unhandled part of this particular root-plus-occupation ledger.

## actual persistence receipts or precise save blocker

The four required protocol files, proof, whole review, frozen specs, independent checkers, exact outputs and source hashes are saved in this unique A008 run; rolling STATUS/WORKLOG/LEARNED are updated only in A008. out/RECEIPTS.json checks exact field sets, statement hashes, equality of progress/delta, two-line status and file sizes/hashes. Files are below20MB. Supervisor copying, mirror verification and independent review of the new lemma are unobserved. No research save blocker; Lean admission is the precise formal-check blocker. Session wake warned of stale owner-model/state-of-mind notes and the owner was notified before relying on them. The compute snapshot showed97.5% commit and23.5GB free; no existing work was stopped. No git, mail, brain writes, shared-index edits or other-agent writes occurred; mandatory wake/checklist and formal-check admission were administrative helper calls.

## Universal bridge

C020 / PI-J moves by a universal payment of the SAME signed root normalizer for arbitrary Boolean signed-conjunction implicant tables: v log2 D<=2(1-2^-k)(1-q)I/(k ln2). No universal FEI constant is obtained. A009's whole complete private-leaf theorem is independently accepted locally and its unchanged reference improves from <11I to <10I by substitution. The remaining exact bridge is complete non-root occupation payment on shared/leafless incidence; NEXT addresses that bill after universally removing its root term, rather than collecting another isolated class result.
'''
report=report.replace('non-root label/subset/attachment/rank occupation cost','occupation cost of individual root rarities and labels/subsets/attachments/ranks')
report=report.replace('No git, mail, brain writes,','No git, mail, research brain writes,')
report=report.replace('No research save blocker;', 'The initial artifact validator assumed raw statement hashes and failed before writing protocol/rolling files. Inspection of A009 code/finalize.py:16 established its canonical statement-plus-hypotheses JSON convention; out/HASH_CONVENTION.json preserves both digests and the resolution. No mathematical assertion failed or mathematical job was repeated. No research save blocker;')
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(RUN/'CHECKPOINT.md').write_text('Stage6 artifacts complete locally; full FEI OPEN.\nNEXT: independently review ROOT_PAYMENT.md; pay the SAME complete occupation bill including individual root rarities, labels, subsets, attachments, ranks and final ambiguity on shared/leafless incidence. See REPORT.md and out/RECEIPTS.json.\n',encoding='utf-8')
status='STATE: A008 stage6 saved: universal signed-implicant SAME root term paid; A009 whole HOLDS, unchanged reference <10I; '+str(total)+' exact checks PASS; Lean admission held; FEI OPEN.\nNEXT: A007/A086 review fiber/packing bound; A006/A009/A010 pay COMPLETE non-root occupation on shared/leafless incidence with SAME fixed reference and full output ambiguity.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' | stage6/account03: reviewed A009 v1 whole without repair; proved universal signed-implicant local boundary and root packing payment; unchanged private reference <10I; '+str(total)+' exact assertions PASS. Lean admission held, no compiler, no retry. Full non-root occupation/FEI OPEN.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage6 durable lemma: any signed positive implicant R of width w>=1 gives sum_R Inf_i>=2q*w/(2^w-1), q=Pr(false), by minimum w-edge boundary of every nonempty proper w-cube fiber. No monotonicity or private leaves needed. Packing gives S=sum lambda*2^-w<=((1-2^-k)/k)*I/(2q), hence SAME signed v log2 D<=2(1-2^-k)(1-q)I/(k ln2). Sharp S coefficient on AND_k. This pays only roots, not complete labels/attachments. A009 v1 whole independently HOLDS; same private reference now C_PL<399I/40<10I from better root estimate. Shared-neighbor shortcut false: K_(3,2) has b/a=4/7>1/4. Lean admission held before compiler: not a certificate.\n')
# Validate schemas and readback; record receipts only after all substantive saves.
required_claim=set(protocol['required_per_run']['claim_fields'])
required_progress={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert all(set(c)==required_claim for c in read(RUN/'CLAIMS.json'))
assert set(read(RUN/'PROGRESS.json'))==required_progress
assert read(RUN/'PROGRESS.json')==read(RUN/'PACKET_DELTA.json')
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for c in read(RUN/'CLAIMS.json'):assert statement_hash(c)==c['statement_sha256']
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='RECEIPTS.json']
assert all(p.stat().st_size<20_000_000 for p in files)
dump(OUT/'RECEIPTS.json',{'timestamp_utc':stamp,'protocol_fields':'PASS','statement_hashes':'PASS','progress_delta_equal':True,'status_lines':2,'mathematical_assertions':total,'files':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],'rolling_files':[{'path':str(p),'sha256':sha(p)} for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']],'mirror':'UNOBSERVED'})
print(json.dumps({'status':'SAVED_AND_VALIDATED','exact_assertions':total,'files':len(files),'report':str(RUN/'REPORT.md'),'new_claim_hash':new['statement_sha256']}))
