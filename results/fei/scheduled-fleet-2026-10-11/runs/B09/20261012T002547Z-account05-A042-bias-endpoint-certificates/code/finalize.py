from pathlib import Path
import json,hashlib,datetime
root=Path(__file__).resolve().parents[1];agent=root.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(name,obj):
 (root/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(statement,hyp):
 return hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
reviewdir=Path(r'~\brain_workers\FEI100_20261011\agents\A085\runs\20261011T231324Z-account05-A085-certificate-adversary')
previous=next(c for c in json.loads((reviewdir/'CLAIMS.json').read_text()) if c['claim_id']=='A042-BIAS-ENDPOINT-INTERFACE')
assert previous['statement_sha256']=='7c2fae4055ba9e3bf195fcebe01cb6e66fde427ca4d8d8c3f48902754514dc60'
statement=('For each of the eight essential binary Boolean sign gates with one exceptional truth-table corner, '
 'the supremum over all interior independent Bernoulli biases of corrected Hplus/(I-Var) is exactly 2+4/ln(2). '
 'For XOR and XNOR the supremum is exactly 2/ln(2). The suprema are not attained in the interior. '
 'Writing A(x)=x ln(1/x)/(1-x), corner ratios are 2+2[A(u)+A(v)]/ln(2), where u,v are probabilities of the exceptional corner coordinates; '
 'parity ratios are [A(1-4p(1-p))+A(1-4q(1-q))]/ln(2). These formulas extend as limits of interior ratios along arbitrary independent endpoint rates, '
 'while deterministic contracted functions have Hplus=I-Var=0. The common sharp corrected constant 2+4/ln(2) propagates through genuine read-once binary formulas '
 'under every product physical law by exact disjoint composition; on uniform physical inputs it implies ordinary H<= [2+4/ln(2)] I. '
 'No higher-arity prime or universal FEI estimate is established.')
hyp=['genuine finite Boolean sign tables','essential arity-two gates for the supremum statements','independent input biases in (0,1)','corrected entropy in bits and spectral influence','contract deterministic inputs before forming a ratio or child variance divisor','genuine disjoint read-once supports for the composition corollary','A(0)=0 and A(1)=1 are limiting values']
claim={'claim_id':'A042-SHARP-BINARY-PRIME-ENDPOINT','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest(statement,hyp),'contributors':['A042/account05'],
 'proof_source':{'run_id':root.name,'path':'REPORT.md','checker':'code/binary_certificate.py','output':'out/CHECK_OUTPUT.json'},
 'proof_dependencies':['elementary two-bit Fourier computation','ln y <= y-1 and convergent logarithm series','disjoint centered-product Fourier composition, independently reconstructed in REPORT.md'],
 'review_records':[],'status':'AUTHOR_PROVED_EXACT_CERTIFICATE; INDEPENDENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A041','A043','A044','A045','A084','A090','A091','B09','B20']}
write('CLAIMS.json',[claim,previous])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B09','packet_id':'A042','gap_id':'G-BIASED-LTF','attempt_id':'A042-binary-prime-basecase-2',
 'method':'complete binary classification; exact product spectra; monotone scalar log certificate; jointly uniform endpoint remainder; exact symbolic-log composition review',
 'mathematical_delta':'Sharp all-bias binary prime constants 2+4/ln2 for eight corner gates and 2/ln2 for XOR/XNOR; arbitrary independent-rate endpoints certified; A085 stage-one review consumed; A043 analytic cofactor/composition interface independently reconstructed at partial scope.',
 'deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'BINARY_BASE_CASE_CLOSED_BY_AUTHOR; NEW_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A042-BIAS-ENDPOINT-INTERFACE','version':1,'status':'A085 independent acceptance consumed at fixed-table scope','statement_sha256':previous['statement_sha256']},{'claim_id':'A043-DISJOINT-PRIME-ENDPOINT','version':1,'status':'analytic interface independently reconstructed; bundled census not reviewed'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'change':'new narrow binary endpoint certificate'},{'claim_id':previous['claim_id'],'version':1,'change':'source-bound independent review consumed; original version unchanged'}],
 'source_artifacts':['REPORT.md','code/binary_certificate.py','out/FROZEN_SPEC.json','out/CHECK_OUTPUT.json','out/SOURCE_RECEIPTS.json','out/REVIEW_SCOPE.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Consume A043 source-specified higher-prime extremizer; isolate its simultaneous-bias normalized coefficient/deficit asymptotics. If unavailable, analyze ternary-majority deterministic-face limits. A090/A091 independently review the binary constants.',
 'stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A042']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
write('out/REVIEW_SCOPE.json',{'stage_one':{'claim_id':previous['claim_id'],'version':1,'review_source':str(reviewdir/'REPORT.md'),'verdict':'A085 scoped independent acceptance consumed','scope':'fixed finite table, fixed interior remainder; not all-arity uniformization','original_statement_sha256':previous['statement_sha256']},
 'A043':{'claim_id':'A043-DISJOINT-PRIME-ENDPOINT','version':1,'verdict':'PARTIAL_REVIEW_HOLDS','reviewer':'A042','independently_reconstructed':['two-row cofactor criterion','decomposition termination and essentiality','actual induced product bias','corrected Hplus/deficit composition and contraction'],'not_reviewed':['n<=4 full census','all artifacts in bundled claim'],'contributed_repair':False,'finite_exact_compositions':180,'constant_child_contractions':40},
 'review_cap':'Lead reports B09 over cap. This stage consumes an independent review, reviews a queued interface and finishes the specifically assigned narrow binary endpoint base case; no new broad universal candidate opened.'})
paths=[Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B09\STREAM_NOTES.md'),Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),reviewdir/'REPORT.md',reviewdir/'CLAIMS.json']
adir=Path(r'~\brain_workers\FEI100_20261011\agents\A043\runs\20261011T221757Z-account05-A043-prime-gate-decomposition')
paths += [adir/'REPORT.md',adir/'CLAIMS.json',agent/'runs/20261011T220136Z-account05-A042-bias-endpoint-certificates/REPORT.md']
receipts=[]
for p in paths:
 raw=p.read_bytes();receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
write('out/SOURCE_RECEIPTS.json',{'at':now,'files':receipts,'scope':'exact report-listed passages inspected; earlier primary paper conventions recalled from stage one; no all-paper audit claimed'})
checks=json.loads((root/'out/CHECK_OUTPUT.json').read_text())
assert checks['assertions_passed']==5277
protocol=json.loads(paths[2].read_text(encoding='utf-8-sig'))
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
for c in [claim,previous]:
 assert set(c)==set(protocol['required_per_run']['claim_fields'])
 assert c['statement_sha256']==digest(c['exact_statement'],c['hypotheses'])
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()
text=(root/'REPORT.md').read_text()
for heading in protocol['required_per_run']['report_fields']:assert '## '+heading in text
assert text.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
write('out/VALIDATION.json',{'protocol_fields':'PASS','claim_hashes':'PASS','packet_delta_equality':'PASS','report_fields':'PASS','exact_assertions':5277,'review_records_preserved':'PASS','remote_persistence':'NOT_CLAIMED'})
(agent/'STATUS.md').write_text('STATE: A042 stage 2 saved: sharp binary all-bias FEI+ constants 2+4/ln2 and 2/ln2; 5,277 exact checks; A085 v1 review consumed; full FEI OPEN.\nNEXT: A090/A091 review binary proof; consume A043 higher-prime extremizer and isolate simultaneous-bias normalized deficit asymptotics beyond arity two.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+now+' | Stage 2: followed B09 v2 binary target; read A085 original acceptance of A042@1 and A043 analytic interface. Classified every binary table, proved sharp continuum suprema C_corner=2+4/ln2 and C_xor=2/ln2 with independent-rate endpoint errors. Exact 1296 binary fixtures, 180 four-input compositions and 40 constant contractions passed 5277 checks in 1.207s. Partial A043 analytic review holds; census not replayed. Saved artifacts and review scope; no new broad candidate.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n# '+now+' sharp binary endpoint base case\n'
 '- A(x)=x ln(1/x)/(1-x), extended A(0)=0,A(1)=1, is strictly increasing. Corner-gate ratio is 2+2[A(u)+A(v)]/ln2; exact sup 2+4/ln2, reached only as the law concentrates at its exceptional corner.\n'
 '- XOR/XNOR ratio is [A(1-4p(1-p))+A(1-4q(1-q))]/ln2; exact sup 2/ln2 at any deterministic corner. Uniform pair is a unit degree-2 atom with D=1 and ratio0.\n'
 '- A(1-e)=1-sum e^k/[k(k+1)], remainder after e/2 at most e^2/[6(1-e)]. This proves uniform unequal-rate two-bias expansions without uniformizing fixed-slice Taylor coefficients.\n'
 '- Deterministic contracted binary gates have Hplus=D=0; a finite nonzero ratio limit is not their actual quotient.\n'
 '- Exact corrected composition preserves max constants for disjoint binary formulas; higher-arity primes remain unpaid. A043 cofactor/composition analytic interface reconstructed; its census not reviewed here.\n'
 '- A085 independently accepted A042@1 at fixed-table scope and checked all 18 weighted intervals; preserve original version/hash and do not infer dimension-uniform bounds.\n')
manifest=[]
for p in sorted(root.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  raw=p.read_bytes();assert len(raw)<20_000_000
  manifest.append({'path':str(p.relative_to(root)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
write('out/PERSISTENCE_RECEIPTS.json',{'at':now,'local_files':manifest,'new_claim_independent_review':'PENDING','supervisor_copy':'PENDING','brain_ingestion':'PENDING','mirror_verification':'NOT_CLAIMED'})
print(json.dumps({'saved_run':str(root),'files':len(manifest),'assertions':checks['assertions_passed'],'protocol_validation':'PASS','review_consumed':previous['claim_id']},indent=2))
