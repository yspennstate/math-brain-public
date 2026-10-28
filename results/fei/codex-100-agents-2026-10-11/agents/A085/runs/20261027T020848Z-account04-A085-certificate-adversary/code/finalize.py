from pathlib import Path
import json,hashlib,datetime

R=Path(__file__).resolve().parents[1]
A=R.parents[1]
run=R.name
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(name): return json.loads((R/name).read_text(encoding='utf-8'))
def save(name,data): (R/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
primary=read('out/CHECKS.json'); independent=read('out/INDEPENDENT_CHECKS.json')
assert primary['status']==independent['status']=='PASS'
formal=read('out/LEAN_ATTEMPT.json')
src=Path(r'agents\A097\runs\20261023T143952Z-account03-A097-cross-route-transfer')
old=json.loads((src/'CLAIMS.json').read_text(encoding='utf-8'))[0]
review=dict(old)
review['review_records']=list(old['review_records'])+[{
 'reviewer':'A085','at':now,'result':'SCOPED_STATEMENT_HOLDS; proof-text derivative t and query erasure corrections required',
 'artifact':str(R/'PROOF.md'),'independence':'No author helper imported; scalar rational grid, ghost profiles, integer-Walsh full children; separate integer-radical reproduction',
 'statement_unchanged':True,'contributor_conflict':False,
 'formal_status':'NOT_LEAN_CHECKED; helper RUNTIME_UNVERIFIED'}]
review['status']='INDEPENDENTLY_RECONSTRUCTED_SCOPED_STATEMENT_WITH_PROOF_TEXT_ERRATA'
statement=('For the actual two-bit Boolean table (-1,1,1,1), squared spectral law p=(1/4,1/4,1/4,1/4), '
 'A one nonempty atom and compatible calibrated q_b=(1/4,(3/4-b)/2,(3/4-b)/2,b), 0<b<1/3, '
 'the sharp floor-1/3 signed CE price is Delta(b)=(1/4)log2(432*b*(3/4-b)^2/25). '
 'Its interior sign boundary is bcrit=(7-2*sqrt(6))/12. For every integer m>=4 the two adjacent dyadic '
 'brackets bminus=floor(2^m*bcrit)/2^m and bplus=bminus+2^-m satisfy all hypotheses, have TV=2^-m '
 'and opposite price signs, with the same optimal target. Dimension two is minimal for this calibrated '
 'interior two-cell Boolean class. In the fixed m=4..160 Python binary64 conversion diagnostic, the first '
 'coincident converted bracket is m=58. This is a precision counterexample, not an FEI counterexample.')
new={
 'claim_id':'A085-SIGNED-ADMISSION-EXACT-SIGN-BOUNDARY','version':1,'exact_statement':statement,
 'hypotheses':['Uniform Boolean AND2 seed; arbitrary normalized calibrated references, not required to be Boolean spectra',
  'A fixed nonempty atom; fixed vacuum 1/4 and within-cell conditional profiles',
  'Finite-CE incoming 0<b<1/3; all logarithms bits',
  'Binary64 first is restricted to the frozen bracket sequence and observed Python conversion'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A085'],
 'proof_source':{'path':str(R/'PROOF.md'),'sha256':hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest(),
   'formal_verification':'NOT_CLAIMED; Lean algebra attempt timed out'},
 'proof_dependencies':[],
 'review_records':[{'reviewer':'A085 separate implementation','independent_person':False,
   'artifact':'out/INDEPENDENT_CHECKS.json','result':'790 exact assertions PASS; independent integer-square-root brackets'}],
 'status':'ANALYTIC_PROOF_AND_EXACT_CERTIFICATES_PENDING_EXTERNAL_REVIEW',
 'supersedes':[],'refutes':['Unclaimed extension: fixed absolute incoming-mass precision suffices to certify every signed compatible admission sign'],
 'first_unproved_line':'Construct a useful universally mandatory arbitrary-core profile/class and influence-priced original full source with sufficient CURRENT unused capacity.',
 'next_consumers':['A097','A093','A094','A098','A099','B17','B20']}
save('CLAIMS.json',[review,new])
next_action=('A097/A094 review exact sign-boundary control and corrected full-query identity; A050/A011 supply '
 'a REQUIRED compatible arbitrary-core admission/source and pay its certified signed price from SAME unused original B-C-U, '
 'retaining all old bills and BOTH full terminals. Do not set a fixed numerical precision ceiling.')
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':run,'stream':'B17','packet_id':'A085',
 'gap_id':'G-ORIGINAL-CORE-SOURCE-PRICE','attempt_id':'A085-stage21-signed-admission-precision-audit',
 'method':'Independent full-scope reconstruction; exact likelihood-polynomial sign control on dimension-minimal actual Boolean seed',
 'mathematical_delta':'A097 arbitrary-current supplied-owner claim statement reconstructs unchanged; derivative and full-query errata confirmed. All-m adjacent dyadic incoming references have opposite exact payment signs; frozen first binary64 alias m58. No universal capacity or FEI constant gain.',
 'deliverable_status':'COMPLETE_LOCAL_SCOPED_AUDIT_AND_EXACT_PRECISION_CERTIFICATE',
 'mathematical_status':'ANALYTIC_PROOF_PLUS_EXACT_CERTIFICATES; EXTERNAL_REVIEW_PENDING; FORMAL_CHECK_UNRESOLVED; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':old['claim_id'],'version':old['version'],'statement_sha256':old['statement_sha256']}],
 'claims_created_or_changed':[old['claim_id']+'@1 independent scoped review',new['claim_id']+'@1'],
 'source_artifacts':['PROOF.md','code/check.py','code/independent.py','out/FROZEN_SPEC.json',
  'out/INDEPENDENT_FROZEN_SPEC.json','out/CHECKS.json','out/INDEPENDENT_CHECKS.json',
  'out/DYADIC_BRACKETS.json','out/SOURCE_RECEIPTS.json','out/BASELINE_READS.json','out/LEAN_ATTEMPT.json'],
 'next_consumers':['A097','A093','A094','A098','A099','A050','A011','B17','B20'],
 'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal initial O(I) source and necessary affordable class remain unpaid',
  'Lean helper RUNTIME_UNVERIFIED after124.9s; no formal result certified',
  'Brain wake personal-context notes stale; not relied on for mathematics',
  'Supervisor mirrors, independent-person review of new sign certificate, and downstream adoption unverified'],
 'packet_ids':['A085']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

Audit A097-SIGNED-ARBITRARY-REFERENCE-FLOOR-OWNER@1 for EVERY finite calibrated current law under its stated interior/profile-preserving hypotheses, exact signed payment from the SAME original B-C-U across ALL full physical terminals, in bits. Test finite-precision substitution at its signed-price zero using an ACTUAL Boolean seed. Full FEI is OPEN.

# sources actually read, revisions and theorem locators

BOARD.md snapshot2026-10-27T02:08Z, B17 STREAM_NOTES v2, own STATUS/LEARNED and previous stage REPORT, machine AGENTS, execution protocol2026-10-11-execution-v2 read. A097 stage21 PROOF/CLAIMS/REPORT read in full; statement hash {old['statement_sha256']}. A093 stage21 DERIVATION and A099 v11 progress consumed; their derivative/query errata corroborated. Campaign registries/current plan/supplement/papers retained as baseline background, with22 explicit byte/encoding receipts in out/BASELINE_READS.json. Four supplied paper TXT files require explicit cp1252 decoding; this is a source-encoding fact, not evidence of damaged mathematics. No new literature attribution or external source claim. Math recall returned unrelated weak matches and is not a dependency.

# complete derivation or exact first unsupported line

PROOF.md reconstructs the scalar projection, finite CE/support conditions, zero-weight handling, full disjoint seed/controller cancellation, ALL-reach SAME-owner iff, and correct inherited physical-query identity. Reviewed statement HOLDS unchanged. Correct F' has factor t; correct query identity is B_j+mean CEchild-CEparent=-D_occ. Sign-boundary control uses the actual AND2 seed and exact factorization of432b(3/4-b)^2-25; all m>=4 adjacent dyadic references have opposite signed prices and TV2^-m with the same optimum. n=2 is minimal for this interior Boolean class. First unsupported universal line remains a useful mandatory arbitrary-core compatible class and an original O(I) complete source with enough CURRENT unused margin; no new universal bound follows from supplied capacity.

# executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json precedes evaluation. python -B -X utf8 code/check.py: {primary['exact_assertions']} exact assertions PASS in{primary['seconds']:.6f}s;322 profiles,756 rational trial points,157 fixed dyadic brackets m4..160,10 dimension0/1 table-event minimality cases and32 signed owner substitutions. Ghost profile mass retained; actual Walsh spectra and BOTH three-bit-seed physical children checked. python -B -X utf8 code/independent.py: {independent['exact_assertions']} separate exact assertions PASS in{independent['seconds']:.6f}s; integer radical isolation imports no primary/author helper. First binary64 alias in this FROZEN sequence m58; exact signs oppose. Arithmetic is Fraction/integer products, not floating log signs. The all-m and continuum conclusions use the written proof, not a finite extrapolation. Jobs are bounded55s/20s with80/40MB estimates; no search escalation. Before the separate formal check memok exited0 (physical7.7GB,commit17.4GB available). lean_check.py returned RUNTIME_UNVERIFIED after124.9s, translation fidelity UNVERIFIED: no Lean certification is claimed. out/LEAN_ATTEMPT.json records this unresolved formal attempt.

# proof dependencies and changed downstream conclusions

Original A097 claim copied unchanged with A085's scoped independent reconstruction record. Proof-text errata do not alter its minimizer, signed formula, or supplied-bank conclusion. Separate sign-control certificate is pending another person's review. Signed payment cannot use an unqualified absolute incoming-mass tolerance; an exact likelihood sign or rigorous interval is necessary near the zero. The example changes references on one fixed two-bit Boolean function (H=2,I=1), so it is NOT an FEI counterfamily. The independent checker caught an earlier explanatory I=3/2 copied from the three-bit seed; direct degree weighting corrected it to1 before completion. No upstream composite source theorem is accepted. Existing matched-floor endpoint frontier remains valid.

# one next mathematical action and independent reviewer

{next_action}

# actual persistence receipts or precise save blocker

Four protocol files, PROOF, frozen specs, portable own checkers, exact outputs, source receipts and formal limitation saved locally and read back by code/finalize.py. STATUS has exactly two lines; WORKLOG/LEARNED append dated results. out/PERSISTENCE_RECEIPTS.json verifies schemas, statement digests and file-size limits. Supervisor mirror/publication/downstream adoption remain UNVERIFIED; no git,mail,brain or other-agent-tree edits. Brain wake warned that personal context/dream notes are stale and the owner was informed; mathematics relies on current files and self-contained verification. The first baseline-reading attempt stopped at strict UTF8 decoding of the legacy paper text; rerun completed with explicit recorded cp1252, without changing sources. Formal helper timeout is a certification limitation, not evidence against the analytic claim.

Universal bridge: C024 history transfer advances by independent full-scope acceptance of A097's arbitrary-INCOMING-reference signed admission statement, corrected query wording, and an exact dimension-minimal precision control for its payment oracle. C018/C019/C020 gain no universal constant (gain0). What remains is an actually required arbitrary-core class/source whose complete cost fits SAME original remaining influence capacity after old bills and both full terminals. NEXT targets that unpaid universal supplier and exact admission liability; another optional restricted reset or fixed-precision sign screen cannot close full FEI.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A085 stage21 saved: A097 signed arbitrary-current SAME-owner statement HOLDS with known proof-text errata;4791+790 exact checks PASS; minimal2bit sign oracle aliases at frozen m58; FEI OPEN.\nNEXT: A097/A094 review exact sign control; A050/A011 supply REQUIRED arbitrary-core compatible source/admission paid from SAME unused original B-C-U, old bills/BOTH full terminals; no fixed precision cap.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n## {now} stage21 signed-admission precision audit\nReconstructed A097 arbitrary-incoming theorem independently, confirming derivative-t and full-query erasure wording corrections without changing its claim. Exact AND2 likelihood polynomial gives all-m opposite-price dyadic brackets; first binary64 alias in frozen m4..160 is58. Primary4791 and independent790 assertions PASS. Formal algebra helper timed out124.9s; no Lean claim. Baseline TXT encoding recovered explicitly as cp1252. Universal initial source remains unpaid. Run: {run}.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write(f'\n## {now} signed-current admission sign guard\nA097@1 statement reconstructs; correct derivative t(z-a)/(z(t-z)ln2), correct query B_j+meanCEchild-CEparent=-D_occ. For actual AND2 law uniform4, incoming q_b=(1/4,(3/4-b)/2,(3/4-b)/2,b), floor1/3 price Delta=log2(432b(3/4-b)^2/25)/4. Unique interior zero bcrit=(7-2sqrt6)/12; every m>=4 adjacent dyadics bracket it with TV2^-m and opposite signed prices, same target. Frozen diagnostic first binary64 alias m58; not a global algorithm minimum. Dimension2 is minimal for interior calibrated two-cell Boolean seed. Signed CURRENT-price tolerance must resolve cancellation exactly or by rigorous intervals; no fixed absolute input precision suffices. Analytic proof/exact4791+790 checks; Lean timeout is unresolved formal status, not a refutation. No universal source/capacity gain.\n')

protocol=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
fields=protocol['required_per_run']
expected={x.split(' (')[0] for x in fields['progress_fields']}
assert set(progress)==expected
for c in read('CLAIMS.json'):
 assert set(c)==set(fields['claim_fields'])
 assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
assert read('PROGRESS.json')==read('PACKET_DELTA.json')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for heading in fields['report_fields']: assert '# '+heading in report
receipts=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  data=p.read_bytes();assert len(data)<20*1024*1024
  receipts.append({'path':str(p.relative_to(R)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
save('out/PERSISTENCE_RECEIPTS.json',{'at':now,'schemas':'PASS','progress_equals_delta':True,'status_two_lines':True,'all_files_under_20MB':True,'remote_mirrors':'UNVERIFIED','files':receipts})
print(json.dumps({'status':'COMPLETE_LOCAL','files_checked':len(receipts),'primary_assertions':primary['exact_assertions'],'independent_assertions':independent['exact_assertions'],'FEI':'OPEN','Lean':formal['status']}))
