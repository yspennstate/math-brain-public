from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
RUN=Path(__file__).resolve().parents[1]
ROOT=RUN.parents[1]
CAMP=ROOT.parents[1]
PROTO=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
def write(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def save(p,x):write(p,json.dumps(x,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
main=json.loads((RUN/'out/EXACT_CHECK.json').read_text(encoding='utf-8'))
ind=json.loads((RUN/'out/INDEPENDENT.json').read_text(encoding='utf-8'))
assert main['status']==ind['status']=='PASS'
assert main['assertions']+ind['assertions']==115350
source_run=CAMP/'agents/A052/runs/20261023T055856Z-account03-A052-critical-source-structure'
source_claims=json.loads((source_run/'CLAIMS.json').read_text(encoding='utf-8'))
sources=[PROTO,CAMP/'BOARD.md',CAMP/'claude/B11/STREAM_NOTES.md',
 source_run/'PRECONDITIONING_PROOF.md',source_run/'REPORT.md',source_run/'CLAIMS.json',
 CAMP/'agents/A051/runs/20261023T050752Z-account03-A051-near-extremizer-definition/REPORT.md',
 CAMP/'agents/A054/runs/20261023T033823Z-account03-A054-connectedness-alternatives/REPORT.md',
 CAMP/'agents/A055/runs/20261023T042040Z-account03-A055-extremal-obstruction-referee/REPORT.md',
 ROOT/'runs/20261023T023627Z-account03-A053-near-tensor-perturbations/THIRD_QUERY_PROOF.md']
save(RUN/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'scope':'Report scope only unless a proof locator is explicitly given in REPORT.md'} for p in sources])
save(RUN/'out/REVIEW_RECORD.json',{
 'reviewer':'A053','source_claims':[{'claim_id':x['claim_id'],'version':x['version'],'statement_sha256':x['statement_sha256']} for x in source_claims],
 'source_proof_sha256':sha(source_run/'PRECONDITIONING_PROOF.md'),
 'accepted_scope':'Sections1--3: partition-preserving complete child orbit, quotient-rank covariance and compensated bank identity, including genuine critical eligibility',
 'verdict':'HOLDS_WITHOUT_REPAIR_AT_STATED_SCOPE','review_source':'REVIEW_A052.md',
 'finite_guards':'independent.py reproduces actual k2,3 activated quadratic guard and complete directional child minima',
 'excluded_scope':'No universal pair selector or full FEI acceptance; ancillary prior paid-family claims not newly reviewed; no shared adoption claimed',
 'contributor_conflict':'No repair supplied; A053 is not a contributor of the reviewed A052 source'})
cid='A053-ARBITRARY-SURGERY-CRITICAL-RADIUS'
statement='Let n>=3, p=2^-n, F any Boolean sign of Fourier support minimum Hamming distance at least3, and G any Boolean sign differing from F on exactly R vertices. For R>=1 every coordinate entropy decrement L_i is strictly less than [10R+(17/2)R^2]p. Every relevant coordinate is strictly paid at K_R=5R+(17/4)R^2, and at K=10R^2 the actual complete-child expected deficit exceeds the original deficit by more than (3/2)R^2p. For R0 the decrement is0. Therefore any least-essential-dimension positive fixed-K witness G, K>=0, cannot have R0 and must obey K<K_R for every such nearby seed, equivalently R>(2/17)(sqrt(25+17K)-5). No inherited fresh-bank claim or universal FEI theorem is made.'
claims=[{'claim_id':cid,'version':1,'exact_statement':statement,
 'hypotheses':['Uniform finite binary cube; normalized Walsh transform; entropy bits; n>=3','Arbitrary Boolean seed F with Fourier support distance>=3; edit set has exactly R distinct physical vertices','Ratio and payment statements require the queried coordinate relevant','Critical corollary requires an actual positive fixed-K witness of least essential dimension among all Boolean positive K-witnesses; no existence is asserted'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A053'],'proof_source':'MULTI_SURGERY_PROOF.md',
 'proof_dependencies':['Self-contained Hamming packing, Parseval, log-sum, proved binary-row curvature inequality and Boolean Fourier granularity'],
 'review_records':[{'reviewer':'A053','kind':'author proof reconstruction plus separate exact implementations','outcome':'115350 full checks PASS; independent-agent acceptance pending'}],
 'status':'AUTHOR_PROOF_EXACT_VALIDATION_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],
 'first_unproved_line':'No unsupported line in the stated restricted theorem is claimed. Criticality does not yet force a paid original block on the residual far-from-code class, nor a uniformly bounded edit radius.',
 'next_consumers':['B11','A051','A052','A055','A090','A094','B20']}]
save(RUN/'CLAIMS.json',claims)
versions=[str(x['claim_id'])+'@'+str(x['version'])+' (sections1--3 scoped review only)' for x in source_claims]
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B11','packet_id':'A053',
 'gap_id':'G-A053-CRITICAL-QUANTITATIVE-SEPARATION','attempt_id':'A053-stage19-arbitrary-surgery-critical-radius',
 'method':'Arbitrary edit energy, distance-three Hamming packing, exact occupied/empty signed rows, Boolean granularity, original complete-child bank; independent affine-preconditioning review',
 'mathematical_delta':'Every relevant original query is paid at5R+17R^2/4 for R edits of a distance-three-support seed; genuine K-critical witnesses must have R>(2/17)(sqrt(25+17K)-5). No odd-parity or factorization hypothesis. A052 no-free-preconditioning independently reconstructed at sections1--3 scope.',
 'deliverable_status':'COMPLETE_SAVED_LOCAL; independent review and supervisor copies pending',
 'mathematical_status':'RESTRICTED_CRITICAL_EXCLUSION_AUTHOR_PROVED_CHECKED; FULL_FEI_OPEN; UNIVERSAL_SELECTOR_OPEN',
 'claim_versions_used':versions,'claims_created_or_changed':[cid+'@1'],
 'source_artifacts':[str(p) for p in sources]+['MULTI_SURGERY_PROOF.md','REVIEW_A052.md','out/EXACT_CHECK.json','out/INDEPENDENT.json','out/FROZEN_SPEC_V3.json'],
 'next_consumers':['B11','A051','A052','A055','A090','A094','B20'],
 'next_action':'Prove a critical-source dichotomy: enter a paid near-code neighborhood or force unused independent cheap-parity rank after an ORIGINAL proper restriction, retaining SAME original deficit, spent bookings and both complete terminals. A090/A094 review beta granularity and critical-bank sign.',
 'stagnant_substantive_attempts':0,
 'blockers':['No universal near-code-or-unused-rank dichotomy','New theorem awaits independent-agent review; supervisor repository copying/adoption unverified','Brain self-care degraded/unverified: stale personal-context owner-model/state-of-mind sources; not premises'],
 'packet_ids':['A053']}
save(RUN/'PROGRESS.json',progress)
(RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())
write(ROOT/'STATUS.md','STATE: Stage19 saved: arbitrary R-edit distance-three seed neighborhood pays every relevant query at5R+17R^2/4; critical radius bound;115350 exact checks PASS;A052 invariance scoped HOLDS;FEI OPEN.\nNEXT: Critical near-code-or-unused-quotient-rank dichotomy after ORIGINAL restriction with SAME bank;A090/A094 review granularity and critical-sign step.\n')
stamp=datetime.now(timezone.utc).isoformat()
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write('\n'+stamp+' stage19: for arbitrary R-edit set of a distance-three Fourier-support Boolean seed, L_i<(10R+17R^2/2)2^-n. Every relevant coordinate paid at5R+17R^2/4; genuine critical witnesses necessarily outside explicit edit radius. Main99055 plus direct independent16295=115350 full checks PASS;pilot36689 excluded. Independent source A052 sections1--3 invariance reconstructed without repair; actual k2,3 compensation guards checked. No mathematical execution failure. Prior one-edit rate9 remains sharper; root-local theorem cannot be rebooked after lost packing. All jobs exited; independent-agent review and supervisor copying pending; FEI OPEN.\n')
with (ROOT/'LEARNED.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write('\nStage19: arbitrary R vertex surgery has energy4Rp and coefficient bound2Rp. At an original singleton of a distance-three support seed, empty rows cost<10Rp; occupied off-anchor beta<=4R^2p/(n+1), with beta0 or beta>=4p^2. Thus L_i<(10R+17R^2/2)p and any relevant query is paid at5R+17R^2/4; no odd-cardinality assumption is needed because relevance gives Inf_i>=2p. Genuine least-dimensional positive K witnesses must have K<5R+17R^2/4 for EVERY such nearby seed. This is root-local, not a fresh inherited bank. A052 partition-preserving affine maps preserve full child orbits and transported quotient ranks; extra apparent release is exactly the root influence charge. Critical far-from-code selection still open; universal constant gain0.\n')
proto=json.loads(PROTO.read_text(encoding='utf-8'))['required_per_run']
assert set(claims[0])==set(proto['claim_fields'])
assert set(progress)==set('packet_ids' if x.startswith('packet_ids ') else x for x in proto['progress_fields'])
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert all(s in report for s in proto['report_fields'])
assert report.rstrip().splitlines()[-1].startswith('C019')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((ROOT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and '__pycache__' not in str(p) and p.name not in ['PERSISTENCE_RECEIPTS.json','HANDOFF_CHECK.json']:
  assert p.stat().st_size<20_000_000
  receipts.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(RUN/'out/PERSISTENCE_RECEIPTS.json',{'schema':'PASS','compatibility_copy':'BYTE_IDENTICAL','files':receipts,'rolling':[{'path':str(p),'sha256':sha(p)} for p in [ROOT/'STATUS.md',ROOT/'WORKLOG.md',ROOT/'LEARNED.md']],'mirror':'not verified; supervisor pending'})
print(json.dumps({'saved':str(RUN),'schema':'PASS','full_checks':115350,'artifacts':len(receipts),'source_review_claims':versions},indent=2))
