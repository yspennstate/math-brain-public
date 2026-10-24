from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,datetime
run=Path(__file__).resolve().parents[1];agent=run.parent.parent;root=Path('~')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(name,obj):(run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
protocol_path=root/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'
protocol=json.loads(protocol_path.read_text(encoding='utf-8'))
full=json.loads((run/'out/CHECK_FULL.json').read_text(encoding='utf-8'))
pilot=json.loads((run/'out/CHECK_PILOT.json').read_text(encoding='utf-8'))
spec=json.loads((run/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
assert full['status']=='PASS' and full['roots']==163 and full['exact_assertions']==54226
assert full['admitted']==628 and full['not_admitted']==24 and full['interval_unresolved']==0
assert sha(run/'code/check.py')==spec['helper_sha256']

# No new input search: verify the sharpness lower bounds on the two already
# recorded even-dimensional quadratic rows, independently of the main checker.
z=Q(1,3);lnlo=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(32)),Q(0))
sharp=[]
for row in full['rows']:
    if row['name']=='quadratic' and row['d']%2==0:
        d=row['d'];s=Q(1,1<<(d//2));lhs=Q(row['profile_minus_Rhalf_over_e'][0])
        rhs=Q(5,2)+(Q(3,2)-4*s)/lnlo
        assert lhs>=rhs
        sharp.append({'d':d,'status':'PASS','saved_lower_bound':str(lhs),'analytic_lower_bound_upper_enclosure':str(rhs)})
assert len(sharp)==2
neg=sum(Q(x['signed_empty_boundary_bits'][1])<0 for x in full['rows'])
pos=sum(Q(x['signed_empty_boundary_bits'][0])>0 for x in full['rows'])
assert neg>0 and pos>0
dump('out/POST_PROOF_VALIDATION.json',{'status':'PASS','scope':'Two existing saved bent rows only; no additional Boolean search or dimension escalation','sharpness_rows':sharp,'strictly_negative_boundary_rows':neg,'strictly_positive_boundary_rows':pos,'remaining_rows':len(full['rows'])-neg-pos})

sources=[root/'AGENTS.md',protocol_path,root/'brain_workers/FEI100_20261011/BOARD.md',root/'brain_workers/FEI100_20261011/claude/B14/STREAM_NOTES.md',agent/'runs/20261021T195741Z-account03-A066-semigroup-dissipation/REPORT.md',agent/'runs/20261021T195741Z-account03-A066-semigroup-dissipation/DERIVATION.md',agent/'runs/20261021T195741Z-account03-A066-semigroup-dissipation/CLAIMS.json',agent/'runs/20261014T090057Z-account05-A066-semigroup-dissipation/DERIVATION.md',root/'brain_workers/FEI100_20261011/agents/A094/runs/20261022T230414Z-account03-A094-proof-chain-challenger/REPORT.md']
dump('out/SOURCE_MANIFEST.json',{'as_of':now,'scope':'Sources read for this stage; baseline paper audits remain in preceding reports. A094 is coordination only, not accepted as a proof dependency.','files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sources if p.exists()]})

statement=('For every d>=0 and Boolean b on d uniform binary coordinates with b(0)=1, set delta=2^(-d), c=b-2*1_(x=0,j=1), and F=c+1_(x=0,j=0)((-1)^z-1). For the physical DATA j query, retain both whole children F0=b+1_(x=0)((-1)^z-1) and F1=b-2*1_(x=0), including the dummy z in F1. With e=delta/2 and SAME R=(d+1)e,G=0, D_R=e, the complete entropy decrement satisfies DeltaH<=R/2+kappa e, kappa=5/2+3/(2ln2)<19/4. The coefficient1/2 and this additive constant are sharp along the bent subfamily. The actual mean terminal influence obeys Ibar>=R. For any fixed ORIGINAL quota A, prior debit tau>=0 and fixed finite-cost complete terminal references Q0,Q1, put U=A-E CE_child-tau. If U>=3R/2-e/4, booking R ONCE and spending L=max(DeltaH-5e,0) leaves U-R-L>=0 and the SAME child reserve R-e. The whole bill DeltaH+E CE_child+tau+(R-e)+(U-R-L)<=A+4e. No quota/reference is reset. In the bent d=2m,m>=2 subfamily, with Q_s=p_s and tau=0, the previous actual rate4 source>=2m and residual>=(59m+1)/32 remain valid. Arbitrary-seed source availability and arbitrary physical-split closure are NOT asserted. The heat translation retains its signed empty boundary, whose sign is not uniform for arbitrary b.')
claim_id='A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT'
claim={'claim_id':claim_id,'version':2,'exact_statement':statement,
 'hypotheses':['Finite uniform binary cube, Boolean signs, marked value b(0)=1; arbitrary d>=0','The specified two-control point attachment and actual physical j query; not every arbitrary-core split','Normalized prescribed complete terminal references with finite CE; original fixed quota A and tau already booked','Unused original source U>=3R/2-e/4; no renewal from local influence'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A066'],
 'proof_source':str(run/'DERIVATION.md'),'proof_dependencies':[],
 'review_records':[],'status':'ANALYTIC_AUTHOR_PROOF_EXACT_CHECKS_REVIEW_PENDING',
 'supersedes':[{'claim_id':claim_id,'version':1,'scope':'Extends the bent-only profile and same-bank data admission to arbitrary seeds; prior bent statements remain corollaries, immutable version1 preserved.'}],
 'refutes':[],
 'first_unproved_line':'Guarantee this inherited-source admission, or an alternative selected continuation, for general actual data queries after all prior debits, with cheap complete source references and both whole terminal debts retained; no fresh-reference reset price is supplied.',
 'next_consumers':['A070','A088','A094','A096','A097']}
dump('CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B14','packet_id':'A066',
 'gap_id':'C019-C024-INHERITED-DATA-AND-TERMINAL-PAYMENT','attempt_id':'A066-stage8-arbitrary-seed-signed-profile-v2',
 'method':'Jensen lower curvature from Parseval and marked-point inversion; C1 patch through zeros; fixed original source quota and exact old debit',
 'mathematical_delta':'Removes bent/flat seed restriction from the signed DATA profile; sharp half-reserve charge and3R/2-e/4 same-source admission retain old debit and both full terminal references. Source availability still fails on simple rare cores; full FEI OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT_REVIEW_PENDING','mathematical_status':'NARROW_ANALYTIC_PROOF_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':claim_id,'version':1,'use':'Extended, with bent corollaries preserved; no independent acceptance inferred.'}],
 'claims_created_or_changed':[{'claim_id':claim_id,'version':2}],
 'source_artifacts':['DERIVATION.md','out/SOURCE_MANIFEST.json','out/FROZEN_SPEC.json','code/check.py','out/CHECK_PILOT.json','out/CHECK_FULL.json','out/LEAN_ADMISSION.json'],
 'next_consumers':['A070','A088','A094','A096','A097'],
 'next_action':'After the paid j query expose one genuine seed-data coordinate, with SAME original A and inherited Q0,Q1, tau and actual L already booked; bound the new signed profile or exhibit the precise admission failure while retaining all complete terminals.',
 'stagnant_substantive_attempts':0,
 'blockers':['Independent review pending','Cheap complete references and unused-source admission not universal','Specified wrapper query does not cover every physical data split or a prescribed reference reset','Formal compiler held by memok exit1; no formal theorem certificate','Supervisor adoption and remote mirrors unverified'],
 'packet_ids':['A066']}
dump('PROGRESS.json',progress);dump('PACKET_DELTA.json',progress)

report=f'''# A066 stage 8: a sharp arbitrary-seed data profile with one original source

## exact target, quantifiers, hypotheses and units

For EVERY Boolean seed b on d>=0 uniform bits with b(0)=1, extend the last stage's specified two-control point attachment and pay its actual DATA j query from the SAME original quota after old debits. Both complete physical terminal functions and their prescribed normalized finite-cost references remain. Entropy/CE are in bits; heat areas and empty boundaries are in nats. This is version2 of A066-NONFLAT-DATA-RELEASE-AND-SOURCE-PAYMENT, not a new broad FEI candidate. The arbitrary seed is genuine; the query remains the specified wrapper split, not every arbitrary-core data query.

## sources actually read, revisions and theorem locators

Read the current BOARD, B14 STREAM_NOTES v2(11Oct23:25UTC), incoming own stage7 STATUS and prior complete derivation, plus execution protocol2026-10-11-execution-v2. B14's original heat/restriction target is already completed at its recorded baseline and is not recounted as progress. A094's latest REPORT(20261022T230414Z) leaves arbitrary-core signed source payment unpaid and is used for coordination only. Its independent acceptance of A095 is not treated as an acceptance of this proof. Prior threshold/percolation source audits remain as recorded; no new external paper theorem or novelty claim is used. Exact local source hashes are in out/SOURCE_MANIFEST.json. One read-only two-wording math recall supplied a generic split-profile warning, not this proof; its full returned text is saved in out/MATH_RECALL.json.

## complete derivation or exact first unsupported line

DERIVATION.md sections1–2 reconstruct the COMPLETE root/child spectra with no flatness assumption. For a_T=hat b(T), E(v)=sum[-(a_T-v)^2 log2((a_T-v)^2)], Parseval and sum a_T=b(0)=1 imply sum(a_T-v)^2<=1 on[delta,2delta]. Jensen gives E''>=N(2d-6/ln2). A C1 monotone-derivative patch across finitely many zero coefficients makes the midpoint inequality valid even where E'' does not exist. It follows that DeltaH<=R/2+kappa e, kappa=5/2+3/(2ln2)<19/4. This is sharper and broader than the previous bent-only coarse interval; d here is the seed dimension, equal to2m in stage7. The earlier32,861 checks concern that different domain, not a previous estimate of this stage's check count.

The bent subfamily approaches the exact kappa with error<=4*2^(-m)/ln2, proving sharpness of the half-reserve coefficient and its additive local constant. Destroyed edges are retained in the exact physical formula; Ibar>=R follows from I(b)>=2delta*t for the t marked pivotal neighbors. No unused source is inferred from this influence inequality.

For a FIXED original quota A, prescribed references Q0,Q1 and OLD debit tau, U=A-E CE_child-tau is the carried unused source. If U>=3R/2-e/4, book R once and pay L=max(DeltaH-5e,0)<=R/2-e/4. The actual data price uses4e, released D_R=e and L from U-R. The complete inequality DeltaH+E CE_child+tau+(R-e)+(U-R-L)<=A+4e retains both whole terminal CE/KL bills, the old debit, the SAME remaining reserve and unused original surplus. A is never reset to descendant influence. The optional A<=K Ibar comparison must itself be supplied; it is not hereditary for free.

The source hypothesis is essential. For the constant seed, rate-four actual terminal surplus<=9delta while R=(d+1)delta/2>9delta for all d>=18. This does not refute FEI, and no source bank is silently created at those nodes. The original bent-source payment remains a corollary with its earlier residual bound unchanged.

Heat translation keeps2DeltaK=ln2 DeltaH-Delta b_empty. The empty boundary now has both signs: {neg} finite rows are strictly negative and {pos} strictly positive; no universal sign is imported from the bent subcase. The semigroup law is unnormalized q_t=p exp(-2t|S|), with J bounded at0 and dominated by e^(-2t)J(0) at infinity on every fixed finite cube. Both endpoints and all boundaries are accounted for. A universal integrated influence payment, hence FEI, remains unproved.

Rung: analytic author proof with exact finite certificates, independent review pending. Core Lean source for only the cleared-denominator budget implication is saved, but fresh memory admission exited1(physical1.3GB free, commit16.7GB free); NO compiler started and NO formal certificate is claimed. The earlier stage7 timeout is not reused as evidence.

FIRST UNSUPPORTED UNIVERSAL LINE: ensure this source admission or a different selected continuation on arbitrary actual data splits after old debits, with a genuinely influence-priced complete inherited reference. The point-attachment representation, cheap initial source reference, indefinite eligibility and fresh-reset cost are separate unpaid obligations. The profile and Ibar>=R do not settle them.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json predates the search and pins helper SHA256. Exhaust every Boolean b(0)=1 at d=0,1,2,3:139 seeds, no symmetry quotient. Add eight declared cores per dimension4,5,6:24 targeted seeds,163 total. Maximum truth-table dimension8. Each has actual-P and prescribed half-P/half-uniform complete references, at ORIGINAL quotas4Ibar or8Ibar, with old debit Ibar/4 booked before any new reserve:652 cases. Integer Walsh coefficients, independent physical edge counts, exact complete terminal CE, reserve drop and the signed heat boundary are checked. Reference admission may FAIL or remain interval-unresolved; it is not forced green.

Commands from A066: python -X utf8 runs/{run.name}/code/check.py pilot and the same helper with full. Pilot PASS:{pilot['roots']} seeds/{pilot['reference_cases']} reference cases/{pilot['exact_assertions']} assertions in{pilot['seconds']:.6f}s. Full PASS:{full['roots']} seeds/{full['reference_cases']} references;{full['admitted']} admitted,{full['not_admitted']} NOT_ADMITTED,{full['interval_unresolved']} unresolved. {full['exact_assertions']} exact assertions in{full['seconds']:.6f}s, excluding duplicate pilot totals. The full count also includes the frozen15,810 integer budget tuples, of which2,569 meet the premises, and the d18 constant-core histogram guard. Logs use32-term range-reduced atanh series with explicit tail and outward2^-70 saved intervals. Post-proof checks inspect the two ALREADY saved bent rows for the sharpness lower bound; no new inputs or dimensions are searched. Their two predicates are saved separately, not added to the54,226 total.

The full checker uses both complete actual terminal references and prescribed full-support references. Failed bank admission is evidence that eligibility is not universal, not a failed profile theorem. The all-dimensional conclusion is the analytic Parseval/Jensen/C1 proof, never extrapolation from163 seeds. Estimate100MB; actual peak unmeasured;55s helper cap; no >300MB job, GPU, heavy job or detached producer. The optional formal launch was held at the admission gate, with its exact receipt saved.

## proof dependencies and changed downstream conclusions

The extended profile, zero handling, physical edge calculation and conditional budget are self-contained. The old bent statements remain corollaries; version1 files are not changed, and version2 does not claim new external acceptance. This narrows the same pending data-payment mechanism rather than adding another broad conjecture under the review cap. Consumers may substitute the uniform half-reserve profile and original-quota admission in the specified wrapper. They may NOT replace eligibility by total influence, renew A, reset either Q, or infer an all-query induction. Universal FEI constant improvement is zero.

## one next mathematical action and independent reviewer

After this paid j query, expose one genuine seed-data coordinate using the SAME original A and inherited terminal references, with tau and the ACTUAL L already booked. Bound the new signed profile or identify the exact failed admission, retaining both full terminals. A070/A088 should independently reconstruct the Jensen curvature and zero patch; A094 should challenge original-quota and old-debit ownership. A096/A097 are mathematical consumers. No review, message delivery or downstream adoption is claimed.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, DERIVATION.md, frozen spec, checker, complete outputs, source receipts, formal-admission hold and post-proof verification are saved here. STATUS has two lines; WORKLOG and LEARNED contain dated/durable updates. The finalizer validates exact protocol field sets, statement/helper hashes, compatibility equality and20MB ceilings, then rechecks all local byte/SHA256 receipts. The four protocol files and rolling files are locally durable; supervisor copy, canonical adoption, mirrors and independent review are unverified. No local research save blocker. Research writes stay in A066; no git, mail, brain-memory write, trading access or other-agent mutation. Brain wake remains degraded: model note87.1h old and state-of-mind note71.7h old; neither is a mathematical premise.

## Universal bridge

C019 stopping payment and C024 history transfer advance from a bent-only example to an arbitrary Boolean SEED profile in the same physical wrapper: the sharp half-reserve debit yields a concrete3R/2-e/4 original-source admission that retains old debits, both complete terminal CE/KL costs, the same reserve and signed heat boundary. Universal constant improvement is zero. Admission after prior histories, a general seed-data split and universally cheap complete source references remain unpaid. NEXT exposes an actual seed coordinate after the paid debit under unchanged owners, because that is the shortest identified move from this signed-profile lemma to a universal inherited-core payment rather than another root-only class estimate.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
(agent/'STATUS.md').write_text('STATE: A066 stage8 saved: arbitrary-seed sharp half-R DATA profile and3R/2-e/4 SAME-source admission;54226 exact checks PASS;review pending;formal admission held;FEI OPEN.\nNEXT: A070/A088/A094 review v2; expose one seed-data coordinate after paid j using SAME A,Q,tau and actual L, retaining both full terminal CE/KL bills.\n',encoding='utf-8',newline='\n')
lesson=('A066 stage8 v2: In the same two-control point attachment, ANY Boolean seed b(0)=1 has E_second>=N(2d-6/ln2), since Parseval/inversion imply sum(a-v)^2<=1 on[delta,2delta]. C1 derivative patch handles zero coefficients. Thus DeltaH<=R/2+(5/2+3/(2ln2))e<=R/2+19e/4; constants are sharp along bent seeds. Actual Ibar>=R includes erased edges. For FIXED original quota A, fixed complete terminal refs and prior tau, U=A-ECE-tau>=3R/2-e/4 books R once and pays L=max(DeltaH-5e,0); full terminals, tau, inherited R-e and U-R-L remain, bill<=A+4e. Do not renew A from local influence. Constant seeds d>=18 have actual rate4 bank<=9delta<R, so eligibility is not automatic. General boundary has both signs. Full FEI, arbitrary data splits, seed-source cost and repeated-reset eligibility remain open. Formal gate held at physical1.3GB; no compiler launched.')
for name,text in [('LEARNED.md',lesson),('WORKLOG.md',f'{run.name}: extended stage7 as version2 using Parseval/Jensen rather than flat spectra;163 actual seeds/652 references,628 admitted24 rejected,54226 exact assertions in5.010515s;15810 integer budget tuples and d18 scalar guard; two saved-row sharpness checks separately PASS. No unresolved intervals. Memory admission held formal attempt; no compiler or detached work. Required artifacts saved; full FEI OPEN.')]:
    p=agent/name
    if run.name not in p.read_text(encoding='utf-8'):
        with p.open('a',encoding='utf-8',newline='\n') as f:f.write('\n'+now+' '+run.name+' '+text+'\n')

req=protocol['required_per_run']
assert set(claim)==set(req['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in req['progress_fields']}
assert hashlib.sha256(statement.encode('utf-8')).hexdigest()==claim['statement_sha256']
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
for heading in req['report_fields']:assert '## '+heading in report
assert len((agent/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(p.stat().st_size<20_000_000 for p in run.rglob('*') if p.is_file())
dump('out/SCHEMA_VALIDATION.json',{'status':'PASS','claim_fields':len(claim),'progress_fields':len(progress),'report_fields':7,'statement_hash':True,'helper_frozen_hash':True,'compatibility_equal':True,'full_fei':'OPEN'})
files=[p for p in run.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']+[agent/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
receipt=[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]
dump('out/PERSISTENCE_RECEIPTS.json',{'created_at':now,'scope':'Local only; independent review and remote adoption unverified','files':receipt})
for x in receipt:
    p=Path(x['path']);assert p.stat().st_size==x['bytes'] and sha(p)==x['sha256']
print(json.dumps({'status':'PASS','files_hashed_and_rechecked':len(files),'exact_assertions':full['exact_assertions'],'post_proof_saved_rows':len(sharp),'version':2,'formal':'HELD_NO_COMPILER','full_fei':'OPEN'}))
print((agent/'STATUS.md').read_text(encoding='utf-8'))
