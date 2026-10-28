"""Persist protocol records and read-back receipts in A017 only."""
from pathlib import Path
import datetime as dt,hashlib,json
R=Path(__file__).resolve().parents[1]; A=R.parents[1]; O=R/'out'
P=Path(r'math-open-problems/reports\fei-2026-10-11')
protocol=json.loads((P/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_bytes((json.dumps(x,indent=2)+'\n').encode('utf-8'))
def text(p,x):p.write_bytes(x.encode('utf-8'))
main=json.loads((O/'certificate.json').read_text(encoding='utf-8'));audit=json.loads((O/'audit.json').read_text(encoding='utf-8'))
formal=json.loads((O/'formal.json').read_text(encoding='utf-8'))
assert main['status']==audit['status']=='PASS'
formalstatus=formal.get('result',{}).get('status',formal.get('status','UNKNOWN'))
now=dt.datetime.now(dt.timezone.utc).isoformat()
statement=("For every pair of Boolean signs f,c on any finite uniform physical cube, put g=fc and let r(c) be the affine dimension over F2 of the nonzero Walsh support of c. Then |H(g)-H(f)|<=r(c), and either physical restriction has rank no greater than r(c). At every node of any finite adaptive stopping tree of actual restrictions, Phi=r(c)+H(g)-H(f) lies in [0,2r(c)], and Delta(g)-Delta(f)=Phi-average(Phi_children)-[r(c)-average(r(c_children))]. Thus all signed corrections telescope from ONE original reserve with both full terminals and rank refunds retained. If c avoids all queried coordinates, actual queried influence equals baseline queried influence and ONE already funded Phi_root suffices to transfer any supplied K-good baseline policy. If c is queried, the exact influence correction E[1_{c flips}f f_prime] is retained. Universal admission Phi_root<=K I(g) is FALSE for every finite K: opposite-slice point defects in dimension m+1, m>=2, give Phi=m, I(g)=(m+1)2^-m and actual query correction zero.")
claim=dict(claim_id='A017-FOUR-EDGE-COMPATIBILITY',version=6,exact_statement=statement,
 hypotheses=['Boolean signs on the SAME finite uniform physical cube','entropy in bits','actual restrictions of ONE root multiplier; no renewed dictionary or gate labels','both full terminal entropy and influence retained','the K-good transfer requires a supplied baseline policy and preexisting ORIGINAL unused reserve; it does not supply one','queried-influence equality requires multiplier independent of queried coordinates; otherwise retain the exact signed influence transfer'],
 statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),contributors=['A017 author derivation and two exact implementations'],
 proof_source={'path':'PROOF.md','sha256':sha(R/'PROOF.md'),'validation':['out/certificate.json','out/audit.json','out/formal.json']},
 proof_dependencies=['finite Walsh orthogonality','finite Shannon entropy chain rule and 0<=H<=log2(alphabet size)','exact physical influence restriction telescope'],
 review_records=[{'kind':'author exact verification','status':'PASS','assertions':main['assertions']+audit['assertions'],'independent_agent':False},
                 {'kind':'core Lean scalar rank-refund algebra ONLY','status':formalstatus,'scope':'No Lean formalization of Walsh block entropy, rank monotonicity, or the full FEI conjecture'}],
 status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[{'claim_id':'A017-FOUR-EDGE-COMPATIBILITY','version':5,'scope':'Continues the same pending C019 candidate; earlier scoped conclusions remain at their original source versions.'}],refutes=['Universal admission r(c)+H(fc)-H(f)<=K I(fc), for a fixed finite K and ALL actual Boolean f,c'],
 first_unproved_line='A translation/vacuum-normalized entropy-sensitive reserve, unlike the refuted rank envelope, is funded from the SAME depleted ORIGINAL influence source after old U and BOTH full terminals; positive-part payment also remains separate.',
 next_consumers=['A018','A019','A020','A024','A090','A091','B04','C019','C024'])
keys=protocol['required_per_run']['claim_fields'];assert set(claim)==set(keys);save(R/'CLAIMS.json',[claim])
nxt='Construct a translation/vacuum-normalized actual coherent reserve and admit it from SAME depleted original influence after old U/BOTH full terminals; require it to vanish on opposite-slice defects. A090/A091 reconstruct rank/refund and influence transport; A024 compare endpoint-normalized source admission.'
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B04',packet_id='A017',gap_id='C019-LOCALIZED-BAD-NODE-BOUNDARY-OWNERSHIP',
 attempt_id='A017-stage22-original-nonlinear-multiplier-reserve',
 method='Orthogonal Fourier-coset block entropy; hereditary affine-rank reserve and exact signed adaptive telescope; actual physical influence transfer; all-dimensional translated-defect source-price obstruction; two exact finite implementations.',
 mathematical_delta='Universal signed nonlinear-overlap history ledger with ONE fixed multiplier and retained rank refunds/physical influence transport; dimension-independent-in-depth correction cap 2r. Exact Boolean family refutes universal influence-price admission of this rank reserve. Full FEI, positive-part bill and normalized original source remain OPEN.',
 deliverable_status='LOCAL_COMPLETE_REVIEW_AND_SUPERVISOR_TRANSFER_PENDING',
 mathematical_status='AUTHOR_PROOF_WITH_EXACT_CERTIFICATES;RANK_RESERVE_SOURCE_PRICE_REFUTED;FULL_FEI_OPEN',
 claim_versions_used=[{'claim_id':'A017-FOUR-EDGE-COMPATIBILITY','version':5,'use':'prior frontier and proxy obstruction only; not a dependency of new proof'}],
 claims_created_or_changed=[{'claim_id':claim['claim_id'],'version':6}],
 source_artifacts=['REPORT.md','PROOF.md','CLAIMS.json','code/','out/'],next_consumers=claim['next_consumers'],next_action=nxt,
 stagnant_substantive_attempts=0,blockers=['Independent reconstruction pending.','Rank-reserve admission is rigorously false; a useful normalized source is still unpaid.','Signed correction control does not price positive variation or full bad-node boundary bill.','Supervisor remote transfer/adoption not verified.'],packet_ids=['A017'])
pk={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']};assert set(progress)==pk
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
base=Path(r'~\brain_workers\FEI100_20261011');supp=P.parents[1]/'research_pushes/2026-10-11-full-fei-100-agents'
sources=[P/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
sources += [base/'BOARD.md',base/'claude/B04/STREAM_NOTES.md',A/'runs/20261023T140902Z-account03-A017-recursive-addressing/PROOF.md',A/'runs/20261023T140902Z-account03-A017-recursive-addressing/REPORT.md',base/'agents/A024/runs/20261026T211725Z-account04-A024-biased-child-stability/REPORT.md']
sources += list((base/'context').glob('*.txt'))
sources += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','sources/OVERLAPPING_PRODUCT_NOTE.md','sources/ERASURE_REDUCTION.md']]
save(O/'SOURCE_RECEIPTS.json',dict(captured_at=now,intake_scope='Full execution protocol and local handoffs; targeted current matrices/plan, campaign notes and paper locators. Hashes captured on final readback, not a claim to have freshly read every line of every paper or registry. No percolation theorem used. Four paper text files have explicit cp1252 source decoding, after strict UTF-8 failed.',sources=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sources if p.exists()],
 brain='One read-only math recall returned general neighboring cards; no recalled card is a proof dependency. Wake stale-source alert disclosed. No brain writes.',coordination='A broad supervisor claim initially blocked writing; released after msg-89305b0a29. Narrow own-folder claim clm-3e1ac1f554 acquired before mutation.'))
report=f'''# A017 stage22: one nonlinear multiplier, one signed reserve

## exact target, quantifiers, hypotheses and units

For ALL Boolean f,c on the same finite uniform physical cube, transfer the ACTUAL signed restriction entropy correction through every finite adaptive stopping tree using ONE root multiplier and actual restrictions. Units: bits. Include queries of shared labels with exact influence transfer; the K-good policy corollary requires c to avoid those queries. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Execution protocol 2026-10-11-execution-v2 read in full; current BOARD B04 and neighboring frontier, lead STREAM_NOTES v2/open line, own stage21 PROOF/REPORT/checker and rolling files. Intake of current campaign matrices/plan B04 contract and original supplement. Threshold38pp Proposition8.6/Corollary8.2 and scope checks in both threshold/percolation versions were targeted reads, not a fresh full-paper reread; no percolation theorem is used. OVERLAPPING_PRODUCT_NOTE preserves the earlier product-subadditivity no-go and existing overlap-width envelope; the present history ledger claims no novelty for that general principle. A024 stage21 endpoint reserve is compared as a source-admission frontier, not used as a theorem. SOURCE_RECEIPTS records scopes and current readback hashes. Read-only math recall supplied no proof dependency.

## complete derivation or exact first unsupported line

PROOF sections1-2 prove |H(fc)-H(f)|<=r(c) by orthogonal amplitude blocks and the entropy chain rule, hereditary rank under actual restrictions, and the exact Phi drift with NONNEGATIVE rank refund. Every signed history is paid by ONE already allocated root Phi, preserving BOTH full actual terminals. Queries in the multiplier retain exact physical influence transport. Section3 gives an actual all-m Boolean family refuting universal rank-reserve admission: Phi/I=m*2^m/(m+1), although actual query correction is ZERO. The first unsupported line is a useful translation/vacuum-normalized coherent reserve admitted from the SAME original depleted influence account, after old U and both full terminals. A signed telescope is not a bound on the sum of positive corrections.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/spec.json precedes pilot and main. Commands: python -X utf8 code/check.py --freeze; --pilot; code/check.py. Pilot:2048 pairs,6144 queries,64 four-bit roots,576 stopped policies,51026 assertions PASS in0.793s. Main:65536 ALL three-bit f,c pairs,196608 queries (including queried multipliers),65536 ALL four-bit roots with fixed nonlinear AND2 multiplier,589824 stopped policies, {main['assertions']} assertions PASS in{main['elapsed_seconds']:.3f}s. The n4 domain is one specified multiplier, not all multipliers. Both full terminal entropies, coset masses, rank refunds, and physical influence correction are retained. Integer Walsh/prime-log coefficients and outward100-bit bounds from rational atanh64 series certify signs; no floating sign decisions. The frozen translated-defect domain m=2..8 checks the analytic obstruction's boundaries.

Separate frozen direct-character audit: python -X utf8 code/audit.py --freeze; code/audit.py;4096 roots/BOTH full children,{audit['assertions']} assertions PASS in{audit['elapsed_seconds']:.3f}s, with independent Fraction entropy and unreduced128-term logarithm bounds. Total main+audit:{main['assertions']+audit['assertions']} assertions. It checks zero/twice-rank endpoints and deliberately false source-price/influence-equality controls. These are separate author implementations, not external acceptance. No automatic dimension growth, GPU or detached process. Estimated main100MB/audit40MB/core Lean100MB; no job expected over300MB or1.5GB. Core-only Lean request: python -X utf8 code/formal.py; status {formalstatus}. Its exact named target is ONLY integer rank-refund algebra, not the analytic entropy theorem. Source, compiler and axiom evidence (if admitted) remain in out/formal.json.

## proof dependencies and changed downstream conclusions

A017-FOUR-EDGE-COMPATIBILITY@6 continues the existing pending C019 candidate rather than opening another broad candidate. This additional ledger is self-contained apart from finite orthogonality, entropy chain rule and physical restriction telescoping; earlier scoped conclusions stay at their original source versions. Stage21's corrected derivative proxy and quadratic obstruction are not reopened. The new reserve permits arbitrary nonlinear shared data and every adaptive query, but supplied-baseline physical-budget transfer requires the stated independence or the explicit signed correction. Its universal original-influence admission is FALSE. No independent acceptance, full-FEI implication, positive-part bill, or initial source payment is asserted.

## one next mathematical action and independent reviewer

{nxt}

## actual persistence receipts or precise save blocker

The four exact-schema protocol files, proof, frozen specifications, code and outputs persist in A017. PERSISTENCE_RECEIPTS records final readback hashes; every file is under20MB. PACKET_DELTA equals PROGRESS byte-for-byte with packet_ids=[A017]. STATUS has exactly two lines; dated WORKLOG and durable LEARNED are updated. The broad supervisor lease was released before own-folder mutation; stale brain wake was disclosed before relying on notes. Startup read failures and strict source-encoding failure supplied no mathematical evidence and were resolved without changing protected sources. No git, mail, external publication, brain mutation or other-agent file edits. Independent review, remote mirror and registry adoption remain supervisor-owned and unverified. No unrelated process was stopped. The bounded Lean helper cleans its owned process job on timeout/finally; no research job is left running.

## Universal bridge

This moves C019/C024 from character/bounded nonlinear reuse to an exact all-core signed interference ledger using ONE original multiplier, with hereditary rank refunds and all physical influence transport retained. It closes depth accounting conditionally on one supplied original reserve, and rigorously eliminates universal influence admission of the rank envelope by an actual Boolean family with reserve/I growing at least2^(m-1). The unpaid step is an entropy-sensitive normalized source that vanishes when the actual correction vanishes, funded after old debits and BOTH full terminals; positive variation remains a separate obligation. NEXT targets that source on the explicit opposite-slice control, where the rank bank provably wastes money, rather than extending another finite tensor family. Full FEI remains OPEN.
'''
for k in protocol['required_per_run']['report_fields']:assert '## '+k in report
text(R/'REPORT.md',report)
text(A/'STATUS.md','STATE: A017 stage22 saved: universal nonlinear-multiplier signed reserve/rank refunds; source-price rank envelope FALSE on translated defects;3502125 exact checks PASS; FEI OPEN/review pending.\nNEXT: '+nxt+'\n')
lesson=f'''\n\n2026-10-27 stage22 ({R.name}): For ALL overlapping Boolean f,c, Fourier-support affine rank r(c) bounds |H(fc)-H(f)|. Each actual restriction has rank<=r. Phi=r+H(fc)-H(f) is nonnegative and has exact signed drift Omega=Phi-avg childPhi-(r-avg childr). One root multiplier/gate dictionary carries through ALL adaptive histories with BOTH full terminals, no renewed per-level cost. If c avoids queries, actual queried influences agree; otherwise retain E[1_cflip f fprime], including characters. This does NOT pay positive variation. Universal rank-bank admission fails on opposite-slice point defects: Phi=m, actual I=(m+1)2^-m, true query correction0. Any useful coherent source must normalize away that artificial invoice. Main3473450+direct28675=3502125 exact assertions PASS; scalar Lean status {formalstatus}, entropy proof not formalized; external review pending.\n'''
if R.name not in (A/'LEARNED.md').read_text(encoding='utf-8'):
    with (A/'LEARNED.md').open('ab') as h:h.write(lesson.encode('utf-8'))
workline=f'\n{now} stage22 ({R.name}): resumed stage21 and B04 handoff; resolved broad supervisor claim before saving; proved global nonlinear signed reserve/rank refund and exact influence transfer; translated point-defect family refutes rank source admission. Main65536 pairs+65536 roots/all589824 stopped trees PASS ({main["assertions"]} checks), separate4096 direct audit PASS ({audit["assertions"]}); Lean scalar status {formalstatus}. Full FEI/source payment OPEN; artifacts saved; supervisor review/mirror pending.\n'
if 'stage22: resumed stage21' not in (A/'WORKLOG.md').read_text(encoding='utf-8') and R.name not in (A/'WORKLOG.md').read_text(encoding='utf-8'):
    with (A/'WORKLOG.md').open('ab') as h:h.write(workline.encode('utf-8'))
files=[]
for p in sorted(R.rglob('*')):
    if not p.is_file() or p.name=='PERSISTENCE_RECEIPTS.json' or '__pycache__' in p.parts:continue
    assert p.stat().st_size<20_000_000
    files.append(dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
save(O/'PERSISTENCE_RECEIPTS.json',dict(at=now,files=files,rolling=[dict(path=p.name,bytes=p.stat().st_size,sha256=sha(p)) for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']],remote_verification='PENDING_SUPERVISOR'))
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for row in files:assert sha(R/row['path'])==row['sha256']
text(R/'.final','LOCAL_COMPLETE; independent review and supervisor mirror pending\n')
print(json.dumps(dict(status='LOCAL_COMPLETE',files=len(files),main_checks=main['assertions'],audit_checks=audit['assertions'],formal_status=formalstatus,full_FEI='OPEN')))
