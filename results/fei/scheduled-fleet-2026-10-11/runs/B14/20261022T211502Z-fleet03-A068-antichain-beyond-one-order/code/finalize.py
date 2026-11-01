"""Persist A068's source-bound stage, without shared writes or external actions."""
from pathlib import Path
import datetime as dt
import hashlib, json
from fractions import Fraction
import verify as exact

RUN = Path(__file__).resolve().parent.parent
OWN = RUN.parent.parent
OWNER = Path(r'~')
PROTOCOL = OWNER/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def write(name,obj):
    (RUN/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

verification=json.loads((RUN/'out/verification.json').read_text(encoding='utf-8'))
pilot=json.loads((RUN/'out/pilot.json').read_text(encoding='utf-8'))
if verification['status']!='PASS' or verification['main_cases']!=4096 or verification['targeted_cases']!=27:
    raise SystemExit('Do not finalize a failed or incomplete verifier')
assert verification['helper_sha256']==sha((RUN/'code/verify.py').read_bytes())
write('out/HYPOTHESIS_SPEC.json',{'helper_version':'finalize-hypothesis-guards-v1','family':'three fixed Boolean/normalization boundary controls','parameter_domain':'one-bit shared-control violation; three-bit point defect; constant one-atom spectrum with nonnormalized reference','case_count':3,'symmetry':'none','arithmetic':'integer, Fraction and existing certified prime logarithms','memory_estimate_mb':20,'maximum_runtime_seconds':5})
gp,gm,beta=[-1,1],[1,-1],[-1,1]
dependent=[gp[i] if beta[i]==1 else gm[i] for i in range(2)]
assert dependent==[1,1] and sum(exact.influence(dependent))==0
assert (sum(exact.influence(gp))+sum(exact.influence(gm)))/2==1
defect=[-1]+[1]*7
defect_spectrum=[x*x for x in exact.walsh(defect)]
gap=exact.combine((1,exact.entropy(defect_spectrum)),(-1,{2:2*sum(exact.influence(defect))+Fraction(1,8)}))
exact.nonnegative(gap,'nonquadratic two-price counterexample strict margin')
assert exact.ce([Fraction(1)],[Fraction(2)])=={2:Fraction(-1)}
write('out/HYPOTHESIS_GUARDS.json',{'status':'PASS','cases':3,'independence':'shared beta=x gives actual constant F but predicted data influence1','quadratic':'three-bit point defect has H(beta)>2I(beta)+1/8 with exact prime-log certificate','normalization':'reference mass2 has complete cost-1 for an entropy0 point mass','note':'These violate hypotheses; none refutes the theorem.'})
now=dt.datetime.now(dt.timezone.utc).isoformat()
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8'))
statement=('For every pair of Boolean functions g_+,g_- on one uniform data cube X, every independent quadratic F2 sign beta on Z, and every pair of complete normalized references Q_+,Q_- supporting their full spectra, the explicit product reference R=Q times [(1-d)delta_empty+d P_beta], Q=pQ_+ +(1-p)Q_-, p=(1+E beta)/2, d=Pr(g_+!=g_-), satisfies H(F)<=Gamma_R(F)<=p Gamma_Q+(g_+)+(1-p)Gamma_Q-(g_-)+4 I(g_+g_-)+2 I_Z(F), where F=g_beta. For nonconstant beta, I(g_+g_-)<=4 I_X(F). Thus admitted complete threshold-terminal references imply Gamma_R(F)<=25 I(F), in every dimension, including weak/unequal identified pairs with independent relative controls. The original terminal references and their physical weights are retained.')
claim={
 'claim_id':'A068-ACTIVATED-QUADRATIC-CONTRAST', 'version':1,
 'exact_statement':statement,
 'hypotheses':['Uniform independent physical blocks X and Z','g_+,g_- are Boolean, sharing arbitrary data in X','beta is an F2 phase of degree at most two on Z','Q_+,Q_- are normalized full references with finite complete branch costs','The <25 corollary uses accepted complete terminal-reference cost <=C_reg influence, C_reg<8.937'],
 'statement_sha256':sha(statement.encode('utf-8')),
 'contributors':['A068'], 'proof_source':'REPORT.md, complete derivation or exact first unsupported line',
 'proof_dependencies':['A068-QUADRATIC-CONTEXT-RANK-REFERENCE@1 for threshold-terminal corollary only','Threshold baseline C001, source SHA256 5d87f625fbadad4aa9841416712b8193a869fa9dffcb4e9c200d2f39a62e6a10; elementary rank/log-sum/payment reconstructed locally'],
 'review_records':[{'kind':'author proof and exact independent-representation checks','verifier':'code/verify.py','output':'out/verification.json','rung':'proof; exact finite certificate; Lean not certified','independent_acceptance':False}],
 'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[], 'refutes':[],
 'first_unproved_line':'Not part of the proved scoped statement: carry the SAME inherited reference and old debits through overlapping/conditional relative controls, without a renewed contrast reserve.',
 'next_consumers':['A070','A088','A094','A066','A067','A096']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
write('CLAIMS.json',[claim])

sources=[]
def source(p,role):
    if p.is_file():
        raw=p.read_bytes()
        # Decode strictly. These PDF text extractions are genuinely cp1252.
        try:raw.decode('utf-8');encoding='utf-8'
        except UnicodeDecodeError:raw.decode('cp1252');encoding='cp1252'
        sources.append({'path':str(p),'sha256':sha(raw),'bytes':len(raw),'encoding':encoding,'role':role})
r=OWNER/'mop_fei100/reports/fei-2026-10-11'
for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
    source(r/name,'governing orientation; registry snapshot is not current proof acceptance')
s=OWNER/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
    source(s/name,'supplemental mathematical orientation')
for p in (s/'sources').glob('*.md'):
    source(p,'read-only source orientation; no theorem imported without local derivation')
for p in (OWNER/'brain_workers/FEI100_20261011/context').glob('*.txt'):
    source(p,'context text read with explicit source encoding; threshold Section8.2 and rank baseline relevant; percolation not a dependency')
source(OWNER/'brain_workers/FEI100_20261011/BOARD.md','stage-start coordination snapshot')
source(OWNER/'brain_workers/FEI100_20261011/claude/B14/STREAM_NOTES.md','B14 lead v2 direction')
for p in sorted((OWN/'runs').glob('*/REPORT.md')):
    if p.parent!=RUN:
        source(p,'A068 predecessor report; stage5 is active mathematical starting point')
write('out/SOURCES.json',sources)

report=(RUN/'REPORT.md').read_text(encoding='utf-8')
report=report.replace('Alternating rank is even.', 'Any nonzero alternating matrix has a nonsingular 2-by-2 principal minor, so its rank is at least two.')
report=report.replace('Orientation reads and exact source hashes will be recorded after validation.', 'Exact byte hashes, source sizes and encodings are recorded in out/SOURCES.json. The primary predecessor is A068 stage5 (20261014T052938Z); later stage directories are not presumed to contain new mathematics merely because their timestamps advanced.')
report=report.replace('PENDING. Frozen specification is in SPEC.json before any search. No claim is called checked until the exact verifier returns.',
 f'''Frozen specification SPEC.json precedes computation. The 256-case pilot PASSed {pilot['assertions']} assertions in {pilot['seconds']:.3f}s. The full verifier PASSed all 4096 ordered two-bit data-function pairs/quadratic two-bit selectors and all 27 prescribed weak/unequal threshold fixtures: {verification['assertions']} exact assertions in {verification['seconds']:.3f}s; {verification['sign_certificates']} distinct certified prime-log signs. No symmetry reduction, stochastic sample, or dimension escalation was used.

Commands (from A068):

    python -X utf8 -u runs/{RUN.name}/code/verify.py --pilot
    python -X utf8 -u runs/{RUN.name}/code/verify.py

The main domain includes constants, identical/opposite branches, all linear and quadratic phases, b=0,+/-1/2,+/-1, and d=0,1. Targeted q=1,3,5; weights (1,1),(2,1),(1,2); controls=2,3,4 include balanced/nonbalanced selectors, negative/zero merged coefficients and fixed ties. The separate physical truth-table FWHT, physical edge counts, derived coefficient formula, both spectral marginals, reference support/normalization, and complete reference payment are checked exactly. Uniform and softened inherited references independently test the log-sum transfer, rather than substituting exact spectra for the original references.

Entropy differences are rational linear combinations of prime logarithms. Forty-eight-term atanh series with a rational remainder certify every nonzero sign; identically zero prime coefficients certify equality. The source/helper hash is {verification['helper_sha256']}. Finite checks support the derivation; the all-dimensional statement follows from the full proof above.

Lean source code/Contrast.lean states the two denominator/marginal identities over Q. Formal compiler admission and its exact outcome are in out/LEAN_ADMISSION.json. The proof rung is author proof plus exact finite certificates, NOT a Lean-checked entropy theorem. No compiler result certifies the prose translation or its entire dependency chain.''')
extra='''

Three fixed hypothesis controls pass in out/HYPOTHESIS_GUARDS.json, under a frozen spec: sharing beta=x with g_+=x,g_-=-x gives constant F and invalidates the independent data-influence formula; a three-bit point-defect phase has H(beta)>2I(beta)+1/8 and invalidates the unrestricted two-price substitution; a reference of mass2 has negative cross-entropy and invalidates the entropy bound. These are out-of-hypothesis guards, not counterexamples to the theorem.

The source comparison is threshold_paper_38pp Section8.2, Proposition8.6 equations75--79 and Corollary8.7: the recovered bound charges two bits per physical selector and requires positive selector energy to absorb that amount. Our weak family has selector influence per active coordinate tending to zero. The current result replaces that uniform charge by the activated quadratic law and a disagreement-boundary debit. The component mixture/channel ingredients are standard; no literature novelty is asserted. Section8.3 independently explains why arbitrary selectors would contain full FEI.

Fresh memok returned exit1: physical free1.7GB below4GB, commit free11.5GB above8GB. Lean's own admission also held (snapshot physical3977MB below5500MB). No compiler was started and no admission override was used. The two rational Lean identities remain source-formalized but UNVERIFIED by a compiler; failed admission is not evidence against the mathematical identities.
'''
report=report.replace('## proof dependencies and changed downstream conclusions',extra+'\n## proof dependencies and changed downstream conclusions')
report=report.replace('Local artifact checkpoint only; hashes and validation receipts pending.', 'The four protocol files, code, frozen spec and exact outputs are saved locally. out/RECEIPTS.json records SHA256 and byte size; out/SCHEMA_CHECK.json validates exact protocol fields and the compatibility copy. STATUS is two lines; WORKLOG is appended and LEARNED updated. Independent review, supervisor collection, shared-registry adoption and mirror verification are not asserted.')
(RUN/'REPORT.md').write_text(report,encoding='utf-8')

progress={
 'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B14','packet_id':'A068','gap_id':'G-LOWSEL-COLLISION',
 'attempt_id':'A068-weak-pair-activation-original-terminal-reserve-v1',
 'method':'Disagreement-weighted product reference, log-sum KL contraction, weighted chi-square denominator certificate, Boolean entropy tensorization and quadratic polar rank',
 'mathematical_delta':'Uniform control decoding is unbounded on an actual weak odd-majority family; activated complete reference costs <=weighted old terminal bills+4I(g_+g_-)+2I_controls. One original 16I_data reserve pays all independent quadratic relative phases, giving <25I for admitted threshold terminals.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_AUTHOR_PROOF_COMPLETE; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':claim['proof_dependencies'],'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':['REPORT.md','CLAIMS.json','SPEC.json','code/verify.py','code/Contrast.lean','out/pilot.json','out/verification.json','out/SOURCES.json','out/LEAN_ADMISSION.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'After one actual overlapping control exposure, retain the inherited joint reference and full terminals and pay its nonflat signed conversion from the SAME unused original reserve after all old debits.',
 'stagnant_substantive_attempts':0,
 'blockers':['Overlapping/conditional phase extension remains open','Independent review and supervisor mirror collection unverified','Wake attachment integrity degraded; affected brain notes not premises'],
 'packet_ids':['A068']}
expected={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
write('PROGRESS.json',progress)
(RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())
(OWN/'STATUS.md').write_text('STATE: Stage17: independent weak/unequal quadratic contrast paid from SAME full terminal references; cost<=old bills+4I(disagreement)+2I_control; <25I threshold family; exact checks PASS; FEI OPEN.\nNEXT: Carry SAME inherited joint reference through an overlapping control query; pay nonflat signed conversion from remaining original reserve after old debits; A070/A088/A094 review.\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} | {RUN.name} | Replaced impossible uniform weak-pair decoder by activated quadratic law. Proved SAME full-reference bound old weighted bills+4I(g_+g_-)+2I_control; original16I_data reserve yields<25I for accepted threshold terminals, including rare/unequal pairs. Exact4096+27 cases,{verification["assertions"]} assertions PASS,{verification["seconds"]:.3f}s. Lean admission recorded separately; no full formal claim. Original text extraction UTF8 read failed honestly, then strictly decoded source cp1252. Full FEI and overlapping/previously-debited continuation remain OPEN.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('''\nActivation-sensitive weak-pair reference (A068 stage17): for independent quadratic beta and arbitrary Boolean g_+,g_- on a shared data cube, F=g_beta has exact data spectrum M=pP_+ +(1-p)P_- and control spectrum C=(1-d)delta_empty+dP_beta, d=Pr(g_+!=g_-). For ANY inherited full references Q_s, R=(pQ_+ +(1-p)Q_-) times C costs at most weighted old full bills+4I(g_+g_-)+2I_controls. Log-sum contraction pays reference mixing by actual JS; weighted chi-square gives JS<=4min(d,1-d)/ln2<3I(product), and h2(d)<=I(product). Nonconstant quadratic beta has both physical branch probabilities>=1/4; hence product influence<=4I_data. One original16I_data reserve yields<25I for complete threshold-terminal references. This allowance is spent ONCE and cannot be renewed at descendants. Shared data between g_+,g_- is allowed; sharing beta controls with them is not. The uniform control decoder fails by >=2sqrt(q)/3 on q-odd weak majority with matching quadratic on m=2q^2 controls. Do not absorb fixed bits by 'nonconstant I>=1': sparse thresholds refute that; use the disagreement boundary. Quadratic flatness under arbitrary single-point edits is NOT claimed.\n''')
schema={'claim_fields_exact':True,'progress_fields_exact':True,'packet_delta_byte_identical':(RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes(),'status_two_lines':len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2,'full_fei':'OPEN','independent_review':'PENDING'}
write('out/SCHEMA_CHECK.json',schema)
receipts=[]
for p in RUN.rglob('*'):
    if p.is_file() and p.name!='RECEIPTS.json':
        raw=p.read_bytes()
        assert len(raw)<20_000_000
        receipts.append({'path':str(p.relative_to(RUN)),'sha256':sha(raw),'bytes':len(raw)})
write('out/RECEIPTS.json',{'at_utc':now,'local_only':True,'files':receipts,'supervisor_copy':'UNVERIFIED','independent_review':'PENDING'})
print(json.dumps({'status':'COMPLETE_LOCAL','cases':verification['main_cases']+verification['targeted_cases'],'assertions':verification['assertions'],'files':len(receipts),'schema':schema,'report_sha256':sha((RUN/'REPORT.md').read_bytes())}))
