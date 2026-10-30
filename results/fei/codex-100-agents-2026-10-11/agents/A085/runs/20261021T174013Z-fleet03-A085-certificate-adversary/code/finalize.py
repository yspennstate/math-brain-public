from pathlib import Path
import json,hashlib,datetime

R=Path(__file__).resolve().parents[1]; A=R.parents[1]
HOME=Path(r'~');ROOT=HOME/'brain_workers/FEI100_20261011'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
protocol=load(HOME/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
required=protocol['required_per_run']
base=HOME/'mop_fei100/reports/fei-2026-10-11'
sup=HOME/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
paths=[HOME/'AGENTS.md',ROOT/'BOARD.md',ROOT/'claude/B17/STREAM_NOTES.md']
paths += [base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [sup/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += [p for p in (sup/'sources').iterdir() if p.is_file() and p.suffix in ['.md','.txt','.tex','.json']]
paths += list((ROOT/'context').glob('*.txt'))
old=A/'runs/20261014T074749Z-fleet05-A085-certificate-adversary'
paths += [old/x for x in ['REPORT.md','PROGRESS.json','CLAIMS.json','PROOF.md'] if (old/x).exists()]
p96=ROOT/'agents/A096/runs/20261014T094929Z-fleet05-A096-live-gap-ledger'
p99=ROOT/'agents/A099/runs/20261021T155354Z-fleet03-A099-candidate-assembly'
paths += [p96/x for x in ['REPORT.md','DERIVATION.md','CLAIMS.json']]
paths += [p99/x for x in ['REPORT.md','STAGE6_ADDITIONS.tex','CLAIMS.json','CANDIDATE_MANUSCRIPT.tex']]
paths += [ROOT/'agents/A094/runs/20261021T155244Z-fleet03-A094-proof-chain-challenger/REPORT.md']
sources=[]
for p in paths:
    raw=p.read_bytes()
    try:txt=raw.decode('utf-8-sig');enc='utf-8-sig'
    except UnicodeDecodeError:txt=raw.decode('cp1252');enc='cp1252'
    sources.append({'path':str(p),'sha256':sha(p),'bytes':len(raw),'encoding':enc,'use':'Critical scopes: A096 DERIVATION 1-2; A099 STAGE6 NR1-NR2 and RS1-RS2. Other source texts provide campaign context, not blanket theorem acceptance.'})
put(R/'out/SOURCE_RECEIPTS.json',{'saved_at':now,'sources':sources,'source_scope':'Only explicitly reconstructed clauses are accepted. Hashing a text is not mathematical review. Marker-only later directories are not evidence.'})

oldprogress=load(old/'PROGRESS.json')
main=load(R/'out/FULLSUPPORT_CHECK.json'); auxiliary=load(R/'out/RESET_CHECK.json')
assert main['status']==auxiliary['status']=='PASS'
assert [r['n'] for r in main['cases']]==list(range(2,8))
lean=load(R/'out/LEAN_RECEIPT.json')
review={'reviewer':'A085','date':now,'verdict':'HOLDS_AT_SELECTED_ELEMENTARY_CLAUSE_SCOPE','source':str(p99/'STAGE6_ADDITIONS.tex'),'source_sha256':sha(p99/'STAGE6_ADDITIONS.tex'),'accepted_scope':['NR1 complete conservative reference identity','NR2 finite adaptive no-reset telescoping with physical reach weights','RS1 signed full terminal reset definition','RS2 exact same-account balance and necessary/sufficient test for its specified bill'],'excluded_scope':['A097 original floor/source price not reconstructed here','A099 complete integrated dependency chain remains unaudited here','No infinite tree limit or cheap reference for arbitrary Boolean function','No free channel or reference-label charge'],'reconstruction':str(R/'PROOF.md'),'new_obstruction_does_not_refute_reviewed_source':True}
put(R/'out/SCOPE_REVIEW.json',review)
statement=('For every integer n>=2 let F_n be the uniform Boolean sign on n+1 bits which is negative exactly at integer vertices 0,1,3; query least-significant bit j. Its squared Fourier law has full support, both physical children are nonconstant, Inf_j=2^-n, I=(3n-1)2^-n and H<=8I. Starting with matching complete root reference Q=P_F and giving both children the inherited marginal q, the conditional occupancy refund is exactly zero. On the j=0 point-defect child let a={y1}, t=2^-n, q_a=2t^2, q_0=1-6t+10t^2, p_0=(1-2t)^2 and M=2^(2n-2). Replace only q(a) by q(a)2^-M and add the removed mass to q(empty); leave the other terminal and already booked erasure unchanged. The new reference has full support and total variation <2^(1-2n), but its physically weighted signed complete reset bill is Z_n=[1-p_0 log2(1+q_a(1-2^-M)/q_0)]/2>3/8, with Z_n->1/2. Thus Z_n/Inf_j->infinity and no dimension-independent absolute-TV tolerance alone certifies an O(I) same-account reset. The first member has dimension three, minimal for full root support and two nonconstant children. This refutes an absolute-TV reset surrogate, not A099 exact RS2 or FEI. A multiplicative bound qtilde>=(1-eta)q on occupied atoms instead gives reset increase <=-log2(1-eta), for 0<=eta<1.')
claim={
 'claim_id':'A085-ABSOLUTE-TV-RESET-OBSTRUCTION','version':1,'exact_statement':statement,
 'hypotheses':['Bits; finite uniform Boolean cube; exact complete normalized reference','Full matching root and conservative common child marginal','One specified descendant reference reset; both full terminals and booked debit retained','Integers n>=2; full-support root and descendants references; no side atom discarded'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A085'],
 'proof_source':{'path':str(R/'PROOF.md'),'locators':'Sections 1-5','checker':str(R/'code/check_fullsupport.py'),'validation':str(R/'out/FULLSUPPORT_CHECK.json')},
 'proof_dependencies':[],'review_records':[],'status':'ANALYTIC_AUTHOR_PROOF_WITH_EXACT_FINITE_CERTIFICATES_INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':['Absolute total-variation proximity alone uniformly preserves O(I) complete-reference reset costs, even on full-support matching roots with two nonconstant children'],
 'first_unproved_line':None,'next_consumers':['A096','A097','A099','A081','A094','A092','B17','B20']}
assert set(claim)==set(required['claim_fields'])
put(R/'CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B17','packet_id':'A085',
 'gap_id':oldprogress['gap_id'],'attempt_id':'A085-stage6-fullsupport-reference-reset-precision',
 'method':'Explicit Boolean counterfamily, independent direct character/FWHT checks, outward dyadic log certificates and scoped exact-account reconstruction',
 'mathematical_delta':'A099 NR1/NR2/RS1/RS2 scoped HOLDS; absolute-TV reset surrogate refuted with full support, both children nonconstant, H<=8I, TV->0 and expected reset cost>3/8. No universal FEI constant improves.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_REVIEW_HOLDS_NEW_OBSTRUCTION_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A096-PAID-FLOOR-NO-RESET-HISTORY','version':1,'scope':'Elementary chain rule clauses only; no new acceptance of priced floor application'},{'claim_id':'A099-NR1-NR2-RS1-RS2','version':6,'scope':'Exact equations in pinned STAGE6_ADDITIONS.tex; locator, not a newly invented canonical registry claim'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'status':claim['status']}],
 'source_artifacts':['PROOF.md','out/SOURCE_RECEIPTS.json','out/SCOPE_REVIEW.json','out/FROZEN_SPEC.json','out/FROZEN_FULLSUPPORT_SPEC.json','code/check_reset.py','code/check_fullsupport.py','out/RESET_CHECK.json','out/FULLSUPPORT_CHECK.json','out/LEAN_RECEIPT.json'],
 'next_consumers':['A096','A097','A099','A081','A094','A092','B17','B20'],
 'next_action':'A094/A092 independently reconstruct full-support obstruction; A096/A097 supply an actual useful fresh descendant reset with certified weighted likelihood or multiplicative atom control against SAME U+r, retaining old debit and both terminals.',
 'stagnant_substantive_attempts':0,'blockers':['Universal useful-reset/reference selection remains OPEN','Independent review and supervisor/canonical/mirror adoption unverified','Core Lean runtime timed out: no target certification'],'packet_ids':['A085']}
expected={k.split(' (')[0] for k in required['progress_fields']}
assert set(progress)==expected
put(R/'PROGRESS.json',progress);put(R/'PACKET_DELTA.json',progress)

report=f'''# A085: the exact reset criterion survives; absolute reference tolerance fails

## exact target, quantifiers, hypotheses and units

Audit A099 v6 NR1--NR2 and RS1--RS2, then test the numerical-to-universal reset bridge on actual Boolean signs with a matching paid root, full support, both nonconstant children, old executed erasure and both complete terminal costs. Bits and physical uniform-cube influence throughout. The new theorem quantifies over every n>=2, not just tested dimensions. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Protocol 2026-10-11-execution-v2 read in full. Required campaign records, supplemental package and four supplied paper text exports were loaded; SOURCE_RECEIPTS pins their bytes and decoding. Current board 2026-10-21 17:34 UTC and B17 lead v2 were consumed. The lead's original A071/census instructions are completed prior work, as own LEARNED and prior run show; they are not rerun. Critical new sources: A096 run20261014T094929Z DERIVATION 1--2 and A099 run20261021T155354Z STAGE6_ADDITIONS NR1--NR2/RS1--RS2. A094 stage16 report was checked to avoid duplicating the existing point-path continuation proof. Paper theorems are context, not proof premises. Later own/peer folders with only .final markers are not successful stages. The current user deadline 23 October supersedes the protocol's old 21 October date. No campaign source or other agent folder was modified.

## complete derivation or exact first unsupported line

PROOF.md derives the full-support family F_n=-1 exactly at 0,1,3 in n+1 dimensions. The matching root costs H<=8I; I=(3n-1)2^-n and queried influence=2^-n. Both children are nonconstant. Their SAME inherited complete reference has zero conditional refund. A normalized positive reset moves less than 2^(1-2n) total variation but adds more than 3/8 bit to the expected complete terminal bill, tending to 1/2 bit. The three-bit first member is minimal under full-root-support/two-nonconstant-child conditions. The all-n proof handles n=2 separately and n>=3 by positive denominator/log bounds; no finite extrapolation or floating sign is used.

A099's exact account identity U+r-Z and its necessary/sufficient test HOLD at the specified elementary scope. The obstruction refutes an absolute-TV numerical substitute that those sources do not assert. It neither refutes their no-reset theorem nor establishes an FEI counterfamily. The original spectator family remains auxiliary evidence. A relative atom bound qtilde>=(1-eta)q instead certifies reset cost <=-log2(1-eta), to be compared with actual SAME unused U+r. First unsupported universal line: choose useful complete references/resets for arbitrary Boolean sources and pay their weighted likelihood, old debits, complementary terminals and channel costs from one dimension-independent influence account.

## executed validation with domain, arithmetic, commands and outputs

Each frozen specification precedes its search. Original fixed domain n=2..7: 1399 exact assertions PASS in {auxiliary['runtime_seconds']:.6f}s; pilot n=2,3:123 assertions. Stronger full-support fixed domain n=2..7: {main['assertions']} exact assertions PASS in {main['runtime_seconds']:.6f}s; pilot n=2,3:72 assertions. Pilot checks are not added to full counts. Commands are python -X utf8 code/check_reset.py [--pilot] and python -X utf8 code/check_fullsupport.py [--pilot], from the run. The two implementations enumerate declared truth tables with no symmetry reduction; direct integer character sums agree with FWHT, and independent physical edge counts confirm influence. Fraction laws verify full support, both children, normalized reset, exact total variation, zero refund and unchanged complementary liability. Outward 100-bit dyadic logs use 40 positive atanh terms and tail <=9/[4(81)3^81], with signed range-reduction exponents added AFTER positive ln2 division. Exact algebra supplies cancellation; interval overlap alone is not treated as an identity proof.

Rung: analytic author proof plus exact finite certificates, independent review pending. Fresh memok passed (physical free12.9GB, commit free24.8GB) before core Lean. Its 45-second attempt returned RUNTIME_UNVERIFIED, target/axioms unverified: no Lean certification is claimed. The submitted statement is only the integer-scaled last inequality, not the logarithm/Fourier theorem. No Mathlib build, GPU, detached research job, n escalation, heavy census or >100MB estimated mathematical helper was launched. Python peak memory is unmeasured. Runtime/precision claims are limited to saved receipts.

## proof dependencies and changed downstream conclusions

The new counterfamily proof is self-contained: finite character sums, physical edge counting, elementary ln bounds and exact complete-reference algebra. out/SCOPE_REVIEW.json accepts only pinned A099 NR1,NR2,RS1,RS2; it does not accept the complete integrated candidate or reconstruct A097's source floor price. No canonical claim version is changed. A096/A097/A099/A081/A094 must retain weighted likelihood or relative atom control when certifying future resets; finite absolute probability accuracy cannot guarantee universal admission near zero influence. Universal constant improvement: zero.

## one next mathematical action and independent reviewer

A094 or A092 should independently reconstruct PROOF Sections1--4, especially full support, n=2, and the unchanged terminal/debit. A096/A097 should prescribe one useful weak non-flat descendant reset and bound its complete signed log-likelihood against measured SAME U+r with both terminals and any channel bills retained. This is shorter than another root census or a smaller absolute tolerance.

## actual persistence receipts or precise save blocker

The four exact-schema protocol files, analytic proof, frozen specifications, independent checker code and exact outputs are saved under this run. out/PERSISTENCE_RECEIPTS.json records hashes, schema and size checks; rolling STATUS has two lines and WORKLOG/LEARNED are current. No intentional brain write, git, mail, other-agent write, trading access or external publication occurred. The required wake warned of stale personal-context notes, and the user was alerted before relying on them. A read-only brain recall reported a detached-refresh spawn failure; no refresh was intentionally started by this worker. All launched checks are bounded. Supervisor copying, canonical adoption, independent review and remote mirrors remain unverified. Local save is complete.

## Universal bridge

This stage sharpens C019 stopping-tree payment and C024 history-transfer certification: conservative finite no-reset transport and exact reset balance survive the scope audit, while absolute-TV reset admission fails on a full-support, cheap-matching-root Boolean family with two nonconstant children. The new obstruction is quantitative: TV<2^(1-2n) but expected reset bill>3/8 bit, with zero refund and queried influence2^-n; universal-constant improvement is zero. A useful influence-priced reset/reference choice with all old debits and both terminals paid remains open. NEXT asks for its weighted-likelihood certificate from the SAME unused bank, because the counterfamily shows that additional finite cases or absolute precision cannot supply that missing universal payment.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')

status='STATE: A085 stage6 complete: full-support matching-root absolute-TV reset surrogate refuted, both children nonconstant, Z>3/8 despite TV->0 and H<=8I; A099 NR1/NR2/RS1/RS2 scoped HOLDS; FEI OPEN.\nNEXT: A094/A092 review full-support all-n witness; A096/A097 certify one useful weak non-flat reset by weighted likelihood or multiplicative atom control against SAME U+r with old debit and both terminals.\n'
(A/'STATUS.md').write_text(status,encoding='utf-8')
tag='2026-10-21 stage6 fleet03'
for name,text in [('WORKLOG.md',f'\n## {tag}\nAudited exact A099 no-reset/reset clauses without repair. Derived full-support three-vertex Boolean family with matching H<=8I root, both nonconstant children, TV<2^(1-2n), Z>3/8 and zero refund. Original and strengthened fixed-domain certificates pass1399 and864 checks. Core Lean45s runtime-unverified; no formal claim. All-n proof and exact-schema outputs saved in {R.name}. General useful-reset same-bank selection remains OPEN.\n'),('LEARNED.md',f'\n## {tag}: complete reference accuracy must be logarithmic\nFor F_n negative exactly at vertices0,1,3 on n+1 bits, n>=2, root P has full support and H<=8I; Inf_j=2^-n, I=(3n-1)2^-n. Both physical children nonconstant. Matching root gives zero occupancy refund. On one-point child, q_a=2t^2,q0=1-6t+10t^2,p0=(1-2t)^2,M=2^(2n-2). Replace q_a by q_a2^-M, transfer removed mass to empty: TV<2^(1-2n), yet expected full resetZ=[1-p0log2(1+q_a(1-2^-M)/q0)]/2>3/8, tending1/2. Three dimensions minimal for full-support root plus both nonconstant children. Thus absolute-TV tolerance alone cannot preserve universal O(I) reset payment; compare exact weighted likelihood to SAME U+r. Relative qtilde>=(1-eta)q implies reset cost<=-log2(1-eta). A099 NR1/NR2/RS1/RS2 scoped HOLD; full integrated chain not accepted.\n')]:
    p=A/name;s=p.read_text(encoding='utf-8') if p.exists() else ''
    if tag not in s:p.write_text(s+text,encoding='utf-8')

# Re-read exact serialized schemas and every saved artifact; no hash self-reference.
assert load(R/'PACKET_DELTA.json')==load(R/'PROGRESS.json')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert set(load(R/'CLAIMS.json')[0])==set(required['claim_fields'])
assert set(load(R/'PROGRESS.json'))==expected
assert (R/'REPORT.md').read_text(encoding='utf-8').rstrip().endswith('missing universal payment.')
receipts=[]
for p in R.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
put(R/'out/PERSISTENCE_RECEIPTS.json',{'status':'PASS','saved_at':now,'protocol_exact_fields':True,'all_files_below_20MB':True,'claim_statement_hash_valid':True,'mathematical_certificates':[main['assertions'],auxiliary['assertions']],'artifacts':receipts,'rolling':[{'path':str(A/x),'sha256':sha(A/x)} for x in ['STATUS.md','WORKLOG.md','LEARNED.md']],'independent_review':'PENDING','remote_mirror':'UNVERIFIED'})
print(json.dumps({'status':'PASS','run':str(R),'gap_id':progress['gap_id'],'claim':claim['claim_id'],'fullsupport_assertions':main['assertions'],'auxiliary_assertions':auxiliary['assertions'],'saved_files':len(receipts)}))
